#!/usr/bin/env python3
"""Own it! 3 ünite kelime kartları (PDF) üreticisi.

Kullanım:  python3 gen_own1_kartlar.py 1      → public/own1/kartlar/unite1.pdf

Veri konu dosyalarından gelir (public/own1/konular/<id>.json): kavram adı (İngilizce), akilda (Türkçe),
ornek / ornekTr (kitaptan birebir cümle + sayfa), svg (çizim). Zıt / benzer kelimeler aşağıdaki
UNITELER sözlüğünde elle verilir. Yeni ünite = UNITELER'e bir kayıt + ders.json'da ünitenin "kartlar" alanı.

PDF düzeni:
  kart sayfaları: A4'e 10 kart (2 × 5). Kesik çizgiden kes, ortadaki çizgiden katla.
              Üst yarı: İngilizce kelime, çizim, örnek cümle. Alt yarı ters basılı: Türkçe, zıt/benzer, cümlenin Türkçesi.
              Zıt ve benzer kelimeler ayrı karttır; ana kelimenin hemen sağında, aynı satırda durur.
              Eşi olmayan kelimeler en sonda ikişer ikişer dizilir.
  son sayfa:  öğretmen/öğrenci için "katla ve kontrol et" listesi (Türkçe sütun arkaya katlanır).
Gereken: playwright (chromium). Fontlar kaynaklar/fontlar/ içinde (SIL OFL), PDF'e gömülür.
"""
import base64, html, json, re, sys
from pathlib import Path

KOK = Path(__file__).resolve().parent
KONU = KOK / "public/own1/konular"
FONT = KOK / "kaynaklar/fontlar"

UNITELER = {
    1: {
        "baslik": "Unit 1: Be inspired",
        "konular": [("u1k1", "adjective"), ("u1k2", "adjective"), ("u1k4", "phrasal verb")],
        # kelime: (etiket, İngilizce, Türkçe)
        "ek": {
            "calm": ("zıt", "anxious", "endişeli"), "cheerful": ("zıt", "grumpy", "huysuz"),
            "confident": ("zıt", "shy", "utangaç"), "helpful": ("zıt", "unhelpful", "yardım etmeyen"),
            "patient": ("zıt", "impatient", "sabırsız"), "sociable": ("zıt", "unsociable", "sosyal olmayan"),
            "sensible": ("zıt", "silly", "saçma davranan"), "sensitive": ("zıt", "insensitive", "duyarsız"),
            "ambitious": ("zıt", "unambitious", "hırssız"), "talented": ("zıt", "untalented", "yeteneksiz"),
            "active": ("zıt", "lazy", "tembel"), "inspiring": ("zıt", "uninspiring", "ilham vermeyen"),
            "take care of": ("benzer", "look after", "bakmak"), "look up to": ("benzer", "admire", "hayran olmak"),
        },
    },
}

SVGBG = "#2b2050"  # own teması çizim zemini


def font_css():
    parcalar = []
    for aile, dosya, kalinlik, stil in [
        ("Fredoka", "fredoka-latin-ext-400-normal", 400, "normal"), ("Fredoka", "fredoka-latin-400-normal", 400, "normal"),
        ("Fredoka", "fredoka-latin-ext-600-normal", 600, "normal"), ("Fredoka", "fredoka-latin-600-normal", 600, "normal"),
        ("Nunito", "nunito-latin-ext-400-normal", 400, "normal"), ("Nunito", "nunito-latin-400-normal", 400, "normal"),
        ("Nunito", "nunito-latin-ext-700-normal", 700, "normal"), ("Nunito", "nunito-latin-700-normal", 700, "normal"),
        ("Nunito", "nunito-latin-ext-400-italic", 400, "italic"), ("Nunito", "nunito-latin-400-italic", 400, "italic"),
        ("Nunito", "nunito-latin-ext-700-italic", 700, "italic"), ("Nunito", "nunito-latin-700-italic", 700, "italic"),
    ]:
        b64 = base64.b64encode((FONT / f"{dosya}.woff2").read_bytes()).decode()
        aralik = "U+0100-024F, U+1E00-1EFF, U+20A0-20CF" if "ext" in dosya else "U+0000-00FF, U+2000-206F, U+2190-21FF"
        parcalar.append(f"@font-face{{font-family:'{aile}';font-weight:{kalinlik};font-style:{stil};"
                        f"src:url(data:font/woff2;base64,{b64}) format('woff2');unicode-range:{aralik};}}")
    return "\n".join(parcalar)


def sayfa_ayir(tr):
    """'Türkçe cümle. (SB s. 14)' → ('Türkçe cümle.', 'SB s. 14')"""
    m = re.search(r"\s*\(((?:SB|WB) s\. [^)]*)\)\s*$", tr or "")
    return (tr[:m.start()].strip(), m.group(1)) if m else ((tr or "").strip(), "")


def vurgula(cumle, kelime):
    """Örnek cümlede kelimeyi kalın yap (çekimli ve araya kelime girmiş hâlleriyle: gives up, cheers me up)."""
    p = kelime.split()
    desen = r"\b" + re.escape(p[0][:-1] if len(p[0]) > 3 and p[0].endswith("e") else p[0]) + r"\w*"
    for x in p[1:]:
        desen += r"(?:\s+\w+)?\s+" + re.escape(x) + r"\b"
    m = re.search(desen, cumle, re.I)
    e = html.escape
    return e(cumle) if not m else e(cumle[:m.start()]) + "<b>" + e(m.group(0)) + "</b>" + e(cumle[m.end():])


def rozet(en, isaret):
    """Çizimi olmayan zıt/benzer kartı için harf rozeti (mercan zemin, baş harf, ↔ ya da = işareti)."""
    h = html.escape(en[0].lower())
    return (f"<svg viewBox='0 0 120 120' xmlns='http://www.w3.org/2000/svg'><rect width='120' height='120' rx='22' fill='#e2553f'/>"
            f"<text x='60' y='80' text-anchor='middle' font-family='Fredoka' font-weight='600' font-size='64' fill='#fff'>{h}</text>"
            f"<circle cx='96' cy='24' r='15' fill='#fff'/><text x='96' y='31' text-anchor='middle' font-family='Nunito' font-weight='700' "
            f"font-size='22' fill='#e2553f'>{isaret}</text></svg>")


def ek_formul(es, ana):
    """unhelpful ← un- + helpful gibi ek kuralını bul (yoksa boş)."""
    for ek in ("un", "in", "im"):
        if es == ek + ana:
            return f"{ek}- + {ana}"
    return ""


def kartlar_oku(u):
    """Satır listesi döner: [ana, eş] çiftleri önce, eşi olmayanlar ikişer ikişer sonda."""
    ciftler, tekler, sozluk = [], [], {}
    for kid, _ in u["konular"]:
        for w in json.loads((KONU / f"{kid}.json").read_text(encoding="utf-8")).get("kelimeler", []):
            sozluk[w["en"]] = w
    for kid, tur in u["konular"]:
        d = json.loads((KONU / f"{kid}.json").read_text(encoding="utf-8"))
        for k in d["kavramlar"]:
            ornek_tr, sayfa = sayfa_ayir(k.get("ornekTr"))
            svg = re.sub(r"(<rect[^>]*?)fill='#1b2340'", r"\1fill='" + SVGBG + "'", k["svg"], count=1)
            ek = u["ek"].get(k["ad"])
            ana = {"en": k["ad"], "tr": k["akilda"], "tur": tur, "ornek": k.get("ornek", ""), "ornekTr": ornek_tr,
                   "sayfa": sayfa, "svg": svg, "ek": ek, "ana": True}
            if not ek:
                tekler.append(ana)
                continue
            w = sozluk.get(ek[1], {})
            e_tr, e_sf = sayfa_ayir(w.get("ornekTr"))
            es = {"en": ek[1], "tr": w.get("tr", ek[2]), "tur": "opposite" if ek[0] == "zıt" else "synonym",
                  "ornek": w.get("ornek", ""), "ornekTr": e_tr, "sayfa": e_sf, "svg": rozet(ek[1], "↔" if ek[0] == "zıt" else "="),
                  "ek": (ek[0], k["ad"], k["akilda"]), "formul": ek_formul(ek[1], k["ad"]), "ana": False}
            ciftler.append([ana, es])
    return ciftler + [tekler[i:i + 2] for i in range(0, len(tekler), 2)]


CSS = """
@page { size: A4; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: 'Nunito', sans-serif; color: #251b3d; }
.sayfa { width: 210mm; height: 297mm; position: relative; page-break-after: always; overflow: hidden; }
.sayfa:last-child { page-break-after: auto; }
.ust { position: absolute; top: 4.5mm; left: 7mm; right: 7mm; display: flex; justify-content: space-between; align-items: baseline;
       font-size: 8.5pt; color: #645a7c; }
.ust b { font-family: 'Fredoka'; font-weight: 600; font-size: 11pt; color: #3a2a6b; }
.alt { position: absolute; bottom: 3.5mm; left: 7mm; right: 7mm; font-size: 6.5pt; color: #8a80a0; display: flex; justify-content: space-between; }
.izgara { position: absolute; top: 11mm; left: 7mm; width: 196mm; height: 275mm; display: grid;
          grid-template-columns: 98mm 98mm; grid-template-rows: repeat(5, 55mm); }
.kart { position: relative; border: .3mm dashed #b9aed0; display: grid; grid-template-rows: 27.5mm 27.5mm; }
.kat { position: absolute; left: 0; right: 0; top: 27.5mm; border-top: .35mm dashed #6c4bd8; }
.kat span { position: absolute; right: 2mm; top: -2.1mm; background: #fff; padding: 0 1mm; font-size: 5.5pt; color: #6c4bd8; letter-spacing: .3mm; }
.on, .arka { display: flex; gap: 3mm; padding: 2.6mm 3.2mm; align-items: center; }
.on svg { width: 19mm; height: 19mm; flex: none; }
.on .m { min-width: 0; }
.en { font-family: 'Fredoka'; font-weight: 600; font-size: 17pt; line-height: 1.02; color: #3a2a6b; }
.tur { display: inline-block; font-size: 6pt; text-transform: uppercase; letter-spacing: .25mm; color: #fff; background: #6c4bd8;
       border-radius: 1mm; padding: .3mm 1.2mm; margin-left: 1.5mm; vertical-align: 2.2mm; font-weight: 700; }
.ornek { font-size: 7.6pt; line-height: 1.22; margin-top: 1.1mm; font-style: italic; }
.ornek b { font-style: italic; background: #fff1a8; padding: 0 .5mm; border-radius: .6mm; }
.iliski { font-size: 8pt; margin-top: 1.2mm; color: #645a7c; } .iliski b { font-family: 'Fredoka'; font-weight: 600; color: #3a2a6b; font-size: 9.5pt; }
.iliski i { font-style: normal; font-weight: 700; color: #e2553f; text-transform: uppercase; font-size: 6.2pt; letter-spacing: .2mm; margin-right: 1mm; }
.formul { display: inline-block; margin-top: 1.2mm; font-size: 7.6pt; background: #fff1a8; border-radius: .8mm; padding: .3mm 1.4mm; font-weight: 700; color: #3a2a6b; }
.tur.es { background: #e2553f; }
.sf { font-size: 5.8pt; color: #8a80a0; margin-top: .6mm; font-style: normal; }
.arka { transform: rotate(180deg); flex-direction: column; align-items: flex-start; justify-content: center; gap: 1mm; background: #f7f4fb; }
.tr { font-family: 'Fredoka'; font-weight: 600; font-size: 14pt; color: #251b3d; line-height: 1.05; }
.tr small { font-family: 'Nunito'; font-weight: 400; font-size: 7pt; color: #645a7c; margin-left: 1.5mm; }
.ekk { font-size: 7.8pt; } .ekk i { font-style: normal; font-weight: 700; color: #e2553f; text-transform: uppercase; font-size: 6.2pt; letter-spacing: .2mm; margin-right: 1mm; }
.ekk b { font-family: 'Fredoka'; font-weight: 600; color: #3a2a6b; }
.otr { font-size: 7pt; color: #645a7c; line-height: 1.2; }
/* öğretmen listesi */
.liste { position: absolute; top: 15mm; left: 9mm; right: 9mm; }
.liste h2 { font-family: 'Fredoka'; font-weight: 600; font-size: 15pt; color: #3a2a6b; }
.liste p.y { font-size: 8.5pt; color: #645a7c; margin: 1mm 0 3mm; }
table { width: 100%; border-collapse: collapse; font-size: 8.4pt; }
td, th { padding: 1.35mm 1.6mm; border-bottom: .2mm solid #e4dcf1; vertical-align: middle; text-align: left; }
th { font-size: 6.8pt; text-transform: uppercase; letter-spacing: .25mm; color: #645a7c; font-weight: 700; border-bottom: .4mm solid #3a2a6b; }
td.no { color: #8a80a0; width: 6mm; } td.kutu { width: 13mm; white-space: nowrap; color: #b9aed0; font-size: 10pt; letter-spacing: .6mm; }
td.w { font-family: 'Fredoka'; font-weight: 600; font-size: 10.5pt; color: #3a2a6b; width: 30mm; }
td.c { font-style: italic; font-size: 7.6pt; line-height: 1.2; }
td.c b { font-style: italic; }
td.fold, th.fold { width: 0; padding: 0; border-left: .45mm dashed #6c4bd8; }
td.t { font-family: 'Fredoka'; font-size: 9.6pt; width: 34mm; padding-left: 3mm; }
td.z { font-size: 7.4pt; color: #645a7c; width: 30mm; }
th.t { padding-left: 3mm; }
"""


def kart_html(k):
    e = html.escape
    if k is None:
        return '<div class="kart" style="border-color:transparent"></div>'
    ek = k["ek"]
    ek_html = f'<div class="ekk"><i>{e(ek[0])}</i><b>{e(ek[1])}</b> · {e(ek[2])}</div>' if ek else ""
    if k["ornek"]:
        on_alt = f'<div class="ornek">{vurgula(k["ornek"], k["en"])}</div>' + (f'<div class="sf">{e(k["sayfa"])}</div>' if k["sayfa"] else "")
    else:  # kitapta cümlesi olmayan zıt/benzer kelime: ilişki ve ek kuralı
        on_alt = (f'<div class="iliski"><i>{e(ek[0])}</i><b>{e(ek[1])}</b></div>'
                  + (f'<div class="formul">{e(k["formul"])}</div>' if k.get("formul") else ""))
    return f"""<div class="kart"><div class="on">{k['svg']}<div class="m">
      <div class="en">{e(k['en'])}<span class="tur{'' if k['ana'] else ' es'}" lang="en">{e(k["tur"])}</span></div>{on_alt}</div></div>
      <div class="arka"><div class="tr">{e(k['tr'])}</div>{ek_html}{f'<div class="otr">{e(k["ornekTr"])}</div>' if k['ornekTr'] else ''}</div>
      <div class="kat"><span>KATLA</span></div></div>"""


def belge(no, u, satirlar):
    e = html.escape
    yuvalar = [k for s_ in satirlar for k in (s_ + [None])[:2]]   # her satır 2 yuva; tek kalan satırın sağı boş
    anlar = [k for k in yuvalar if k and k["ana"]]
    sayfalar = []
    parca = [yuvalar[i:i + 10] for i in range(0, len(yuvalar), 10)]
    toplam = len(parca) + 1
    kaynak = "Örnek cümleler: Own it! 3 Student's Book / Workbook (Cambridge University Press)"
    for s, grup in enumerate(parca, 1):
        sayfalar.append(f"""<section class="sayfa"><div class="ust"><span><b>Own it! 3 · {e(u['baslik'])}</b> · Vocabulary cards</span>
          <span>Solda kelime, sağda zıttı / benzeri · ✂ kes · mor çizgiden katla</span></div>
          <div class="izgara">{''.join(kart_html(k) for k in grup + [None] * (10 - len(grup)))}</div>
          <div class="alt"><span>{kaynak}</span><span>{s} / {toplam}</span></div></section>""")
    satir = "".join(f"""<tr><td class="no">{i}</td><td class="kutu">☐☐☐</td><td class="w">{e(k['en'])}</td><td class="c">{vurgula(k['ornek'], k['en'])}</td>
        <td class="fold"></td><td class="t">{e(k['tr'])}</td><td class="z">{f'{e(k["ek"][0])}: {e(k["ek"][1])}' if k['ek'] else ''}</td></tr>"""
                    for i, k in enumerate(anlar, 1))
    sayfalar.append(f"""<section class="sayfa"><div class="liste"><h2>Own it! 3 · {e(u['baslik'])} — Katla ve kontrol et</h2>
      <p class="y">Kâğıdı mor kesik çizgiden arkaya katla. İngilizce kelimeye bak, Türkçesini söyle, sonra aç ve kontrol et. Her doğruda bir kutuyu işaretle (3 tur).</p>
      <table><thead><tr><th></th><th>Tur</th><th>Word</th><th>Example</th><th class="fold"></th><th class="t">Türkçe</th><th>Zıt / benzer</th></tr></thead><tbody>{satir}</tbody></table></div>
      <div class="alt"><span>{kaynak}</span><span>{toplam} / {toplam}</span></div></section>""")
    return f"<!doctype html><html lang='tr'><head><meta charset='utf-8'><style>{font_css()}{CSS}</style></head><body>{''.join(sayfalar)}</body></html>", len(parca)


def main():
    no = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    u = UNITELER[no]
    satirlar = kartlar_oku(u)
    kartlar = [k for s_ in satirlar for k in s_]
    eksik = [k["en"] for k in kartlar if k["ana"] and (not k["ornek"] or not k["sayfa"])]
    if eksik:
        sys.exit(f"örnek cümlesi/sayfası eksik: {eksik}")
    vurgusuz = [k["en"] for k in kartlar if k["ornek"] and "<b>" not in vurgula(k["ornek"], k["en"])]
    hedef = KOK / f"public/own1/kartlar/unite{no}.pdf"
    hedef.parent.mkdir(parents=True, exist_ok=True)
    metin, kart_sayfa = belge(no, u, satirlar)
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.set_content(metin, wait_until="load")
        pg.evaluate("document.fonts.ready")
        pg.pdf(path=str(hedef), format="A4", print_background=True, prefer_css_page_size=True)
        b.close()
    es = sum(1 for k in kartlar if not k["ana"])
    print(f"{hedef.relative_to(KOK)}: {len(kartlar)} kart ({len(kartlar) - es} ana + {es} zıt/benzer), "
          f"{kart_sayfa} kart sayfası + 1 liste sayfası" + (f" | vurgulanamayan: {vurgusuz}" if vurgusuz else ""))


if __name__ == "__main__":
    main()
