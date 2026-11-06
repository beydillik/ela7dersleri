"""Dikkat paketi testi (Ela'nın ayarlarıyla). Önce: cd public && python3 -m http.server 8765 &
Kullanım: python3 araclar/dikkat/test_dikkat.py <kod> <konu>     örn. fen1 u3k1"""
import json, re, sys
from playwright.sync_api import sync_playwright

import os
KOD, KONU = sys.argv[1], sys.argv[2]
KOK = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
D = json.load(open(os.path.join(KOK, "public", KOD, "konular", KONU + ".json"), encoding="utf-8"))
SONUC = []
def ok(ad, kosul, ayrinti=""):
    SONUC.append((ad, bool(kosul))); print(("✓ " if kosul else "✗ ") + ad + (f"  [{ayrinti}]" if ayrinti and not kosul else ""))

TUM = [k["soru"] for k in D["kavramlar"]] + D["sorular"] + D.get("metinli", [])
def bulmali(q):   # motordaki kalpTum ile aynı: bölge sorunun bütün kelimelerini kapsıyorsa bulma adımı yok
    kel = lambda x: re.findall(r"[^\W_]+", x)
    b = {w for x in q.get("bolge", []) for w in kel(x)}
    return bool(q.get("bolge")) and not all(w in b for w in kel(q["soru"]))
def tam(t): return re.compile(r"^[a-d]\) " + re.escape(t) + r"$")
def bul_q(metin):
    es = [q for q in TUM if q["soru"] in metin]   # en uzun eşleşme ("Hangisi doğrudur?" başka sorunun içinde de geçer)
    if es: return max(es, key=lambda q: len(q["soru"]))
    raise Exception("soru bulunamadı: " + metin[:80])
# Matematik: tuş takımı (cevap) ve sayı doğrusu (nokta) soruları da sorunun kalbinden sonra açılır
def alan(q): return ".kp" if "cevap" in q else ".sd-pick" if "nokta" in q else ".opts"
def cevapla(page, kap, q):
    """Aynı metinli birden çok soru olabilir (görseli farklı): yanlış çıkarsa sıradaki adayı dener."""
    if "cevap" in q or "nokta" in q:
        es = [x for x in TUM if x["soru"] == q["soru"] and ("cevap" in x or "nokta" in x)]
        es = [q] + [x for x in es if x is not q]
        for x in es:
            _cevapla1(page, kap, x)
            if not page.is_visible(f"{kap} .fb.hint"): break
        return True
    return False
def _cevapla1(page, kap, q):
    if "cevap" in q:
        for ch in str(q["cevap"]):
            k = {"-": "−", ".": ","}.get(ch, ch)
            page.locator(f"{kap} .kp-k[data-k='{k}']").first.click()
        page.locator(f"{kap} .kp-ok").first.click()
    elif "nokta" in q:
        page.locator(f"{kap} .sd-hit[data-x='{q['nokta']}']").first.dispatch_event("click")
    else: return False
    return True

with sync_playwright() as pw:
    b = pw.chromium.launch(); ctx = b.new_context(viewport={"width": 390, "height": 900})
    page = ctx.new_page(); hatalar = []
    page.on("console", lambda m: hatalar.append(m.text) if m.type == "error" and "ERR_" not in m.text else None)
    page.on("pageerror", lambda e: hatalar.append("PAGEERROR " + str(e)))
    page.route("**/fonts.g*/**", lambda r: r.abort())
    page.route("**/ortak/bulut.js", lambda r: r.fulfill(body="", content_type="text/javascript"))
    # Ela'nın kullanım modu: kart bekleme, şık bekleme, yanlış sonrası bekleme, Öğren kilidi açık
    page.add_init_script("localStorage.setItem('ela7:ayar', JSON.stringify({mod:'ozel', sikBekle:true, oyunKilit:true, ogrenKilit:true, hataDur:true, kartBekle:true, hedefliTekrar:false, tamamEsik:75}));")
    page.clock.install()
    page.goto(f"http://localhost:8765/{KOD}/#{KONU}"); page.wait_for_selector("#panel .stage")
    def ileri(ms=100):
        page.clock.run_for(ms); page.evaluate("document.querySelectorAll('.koc').forEach(x => x.remove())")

    # Rozet
    rz = page.locator(".yz-rozet .yzr").all_inner_texts()
    ok("Rozet sade (yalnız 'Yazılıda çıkacak/çıkabilir' ya da hiç)", all(t in ("Yazılıda çıkacak", "Yazılıda çıkabilir") for t in rz), str(rz))

    # ---------- Öğren
    ilk_kart = True; soru_say = 0; seri_test = None; kalp_ok = 0; ilk_bulmali = True; yanlis_test = False; tum_gor = False; kp_test = False
    adim = int(page.inner_text("#pgTxt").split("/")[1].split()[0])
    # Türkçe/Matematik: "Hazır mısın?" (hazirlik) ve kavramlardaki "Birlikte çözelim" (cozum) / "Sıra sende" (sende) birer adımdır
    ek_adim = (1 if (D.get("hazirlik") or {}).get("maddeler") else 0) + sum(bool(k.get("cozum")) + bool(k.get("sende")) for k in D["kavramlar"])
    beklenen = 1 + 2 * len(D["kavramlar"]) + 3 + ek_adim
    ok(f"Öğren: ara 'Hatırlayalım' adımı yok (adım sayısı {adim})", adim == beklenen, f"beklenen {beklenen}")
    SENDE = [a["soru"] for k in D["kavramlar"] for f in ("cozum", "sende") for a in (k.get(f) or {}).get("adimlar", []) if a.get("soru")]
    for _ in range(120):
        if page.query_selector("#htBox") or page.query_selector("#kisaBox"): break
        hz = page.query_selector("[data-hz-atla]")   # Hazır mısın?: bu testin konusu değil, geç
        if hz: hz.click(); ileri(100); continue
        bos = page.query_selector(".coz-adim li.bos")   # Sıra sende: boş adımdaki soruyu doğru cevapla
        if bos:
            bt = bos.inner_text(); sq = next(x for x in SENDE if x["soru"] in bt and all(o in bt for o in x.get("secenekler", [])))   # aynı metinli sorular şıklarıyla ayrılır
            ileri(8000)
            if not cevapla(page, ".coz-adim li.bos", sq): page.locator(".coz-adim li.bos .opt").nth(sq["dogru"]).click()
            ileri(100); continue
        ad = page.query_selector("[data-adim]:visible")   # Birlikte çözelim / Sıra sende: adımları aç
        if ad: ad.click(); ileri(100); continue
        ok_hatirla = page.query_selector(".recall")
        if ok_hatirla: ok("Öğren: Hatırlayalım ekranı çıkmamalı", False); break
        if page.query_selector("#qbox"):
            soru_say += 1
            q = bul_q(page.inner_text("#qbox .q-text"))
            serbest = page.query_selector("#qbox .kalp-not") is None
            kp_simdi = False
            if "cevap" in q and bulmali(q) and not serbest and not kp_test:
                kp_test = kp_simdi = True; ok("Tuş takımı: sorunun kalbi bulunana kadar gizli", page.is_hidden("#qbox .kp"))
            if not bulmali(q):
                if not tum_gor: tum_gor = True; ok("Kısa soru (bölge = sorunun tamamı): bulma adımı yok, şıklar açık", serbest and page.is_visible(f"#qbox {alan(q)}"))
            elif ilk_bulmali:
                ilk_bulmali = False
                ok(f"Soru: şıklar/cevap alanı ({alan(q)}) gizli, 'Soru neyi soruyor?' notu var, bekleme çubuğu yok",
                   page.is_hidden(f"#qbox {alan(q)}") and page.is_visible("#qbox .kalp-not") and page.query_selector("#qbox .kb-cubuk, #qbox .opts.bekle") is None)
                yanlis = page.locator("#qbox .kk:not(.kk-b)")
                if yanlis.count():
                    yanlis.first.click(); ileri(50)
                    ok("Soru: yanlış kelimeye dokununca 'Burası değil' ve şıklar hâlâ gizli", "Burası değil" in page.inner_text("#qbox .kalp-not") and page.is_hidden(f"#qbox {alan(q)}"))
                page.locator("#qbox .kk-b").first.click(); ileri(50)
                ok("Soru: sorunun kalbine dokununca bölge kırmızı, şıklar açık", page.locator("#qbox .kk-run.kalp").count() > 0 and page.is_visible(f"#qbox {alan(q)}"))
            elif not serbest:
                page.locator("#qbox .kk-b").first.click(); ileri(50); kalp_ok += 1
            else:
                seri_test = soru_say
                ok(f"Seri ödülü: {soru_say}. soruda bulma adımı yok, şıklar doğrudan açık", page.is_visible(f"#qbox {alan(q)}"))
            if kp_simdi:
                ok("Tuş takımı: sorunun kalbi bulununca açık", page.is_visible("#qbox .kp"))
                yanlis_s = "9" if str(q["cevap"]) != "9" else "8"
                page.locator("#qbox .kp-k[data-k='" + yanlis_s + "']").first.click(); page.locator("#qbox .kp-ok").first.click(); ileri(50)
                ok("Tuş takımı: yanlış cevapta 'Sorunun kalbine tekrar bak'", page.is_visible("#qbox .kalp-hatir")); ileri(800)
            if bulmali(q) and "secenekler" in q and not yanlis_test and not ilk_bulmali and page.query_selector("#qbox .kk-run"):   # bir yanlış cevap: sorunun kalbi hatırlatması
                yanlis_test = True
                yanl = [j for j in range(len(q["secenekler"])) if j != q["dogru"]][0]
                page.locator("#qbox .opt").nth(yanl).click(); ileri(50)
                ok("Yanlış cevapta 'Sorunun kalbine tekrar bak' hatırlatması", page.is_visible("#qbox .kalp-hatir"))
            ileri(8000)
            if not cevapla(page, "#qbox", q): page.locator("#qbox .opt").nth(q["dogru"]).click()
            ileri(50)
        nx = page.query_selector("[data-next]:not([disabled])")
        if nx:
            if ilk_kart and page.query_selector(".kb-not.sessiz"):
                ilk_kart = False
                ok("Bilgi kartı: görünür kilit ve çubuk yok", page.query_selector(".kb-cubuk") is None and "kilitli" not in (nx.get_attribute("class") or ""))
                nx.click(); ileri(50)
                ok("Bilgi kartı: erken geçişte kısa not çıkar, kart değişmez", page.is_visible(".kb-not.sessiz"))
                ileri(16000); page.click("[data-next]"); ileri(50); continue
            ileri(16000); page.click("[data-next]"); ileri(50)
        else: ileri(200)
    SERI_OGREN = seri_test is not None

    # Hatırla ve Tekrarla: kart kilidi yok
    ok("Hatırla ve Tekrarla adımı geldi", page.query_selector("#htBox") is not None)
    ok("HT: kartta çubuk yok", page.query_selector("#htBox .kb-cubuk") is None)
    page.click("[data-basla]"); ileri(50)
    ok("HT: 'Okudum, şimdi tekrarla' hemen çalışır", page.query_selector("#htBox select") is not None)
    ileri(6000)
    for t in D["tekrar"]:
        for dog in [m.split("|")[0].strip() for m in re.findall(r"\{([^{}]+)\}", t["c"])]:
            page.select_option("#htBox select", label=dog); ileri(30)
        ileri(6000)
    ok("HT: tur bitti, Devam açık", page.get_attribute("[data-next]", "disabled") is None)
    page.click("[data-next]"); ileri(100)

    # Kısa cevap
    ok("Kısa Cevap adımı geldi", page.query_selector("#kisaBox") is not None)
    for qi, q in enumerate(D["kisaCevap"]):
        if bulmali(q):
            ok(f"KC{qi+1}: önce sorunun kalbi, şıklar gizli, çubuk yok", page.is_hidden("#kisaBox .opts") and page.is_visible("#kisaBox .kalp-not") and page.query_selector("#kisaBox .kb-cubuk") is None)
            page.locator("#kisaBox .kk-b").first.click(); ileri(50)
        else: ok(f"KC{qi+1}: kısa soru, bulma yok, ön soru şıkları doğrudan açık", page.is_visible("#kisaBox .opts"))
        txt = page.locator("#kisaBox .opt").all_inner_texts()
        ok(f"KC{qi+1}: 3 ön soru şıkkı, büyük harfle ve öğretmen dilinde", len(txt) == 3 and all(t[0].isupper() for t in txt) and any(q["okut"][0][1:] in t for t in txt), str(txt)[:120])
        page.locator("#kisaBox .opt:not([data-j='0'])").first.click(); ileri(50)
        ok(f"KC{qi+1}: yanlış ön soru şıkkı kapanır" + (", kırmızı kısım hatırlatılır" if bulmali(q) else ""), page.locator("#kisaBox .opt[disabled]").count() == 1 and (page.is_visible("#kisaBox .kalp-hatir") or not bulmali(q)))
        page.click("#kisaBox .opt[data-j='0']"); ileri(50)
        page.click("[data-yaz]"); ileri(50)
        ok(f"KC{qi+1}: kalıp ekranında 'Soru senden şunu istiyor'" + (" ve kırmızı bölge" if bulmali(q) else ""), "Soru senden şunu istiyor" in page.inner_text("#kisaBox") and (page.locator("#kisaBox .kk-run.kalp").count() > 0 or not bulmali(q)))
        for k, p in enumerate(q["parcalar"]): page.fill(f"#kisaBox input[data-p='{k}']", p["ornek"])
        page.click("[data-kontrol]"); ileri(50)
        ok(f"KC{qi+1}: kontrol tam, 'Kalıpsız dene' düğmesi yok", page.locator("#kisaBox .kw span.hit").count() == len(q["anahtarlar"]) and page.query_selector("[data-serbest]") is None)
        page.click("[data-ileri]"); ileri(50)
    page.click("[data-next]"); ileri(100)
    ok("Öğren bitti", "Konuyu bitirdin" in page.inner_text("#stage"))

    # ---------- Test
    page.click("[data-tab=test]"); ileri(300)
    page.click("[data-basla]"); ileri(200)
    toplam = int(re.search(r"/ (\d+)", page.inner_text(".akis .progress span")).group(1))
    ok(f"Test: toplam soru sayısı değişmedi ({toplam})", toplam == len(D["sorular"]))
    metinli_gor = 0; yanlis2 = False; tuzak_gor = False; sonuclar = []
    seri_gor = False
    for _ in range(60):
        if page.query_selector(".akis") is None: break
        qtext = page.inner_text("#sq .q-text"); q = bul_q(qtext); met = bool(q.get("kanit")) and ("metin" in q or "tablo" in q)   # metinli alanı (Fen) ya da konudaki kanıtlı soru (Türkçe)
        no = int(re.search(r"Soru (\d+) /", page.inner_text(".akis .progress span")).group(1))
        if bulmali(q) and not met and page.query_selector("#sq .kalp-not") is None and page.locator("#sq .opt[disabled]").count() == 0: seri_gor = True
        if page.query_selector("#sq .kalp-not") and "ok" not in (page.get_attribute("#sq .kalp-not", "class") or ""):
            if met: ok(f"Metinli: önce yalnız soru (metin gizli)", page.is_hidden("#sq .pasaj"))
            page.locator("#sq .kk-b").first.click(); ileri(50)
        if met:
            metinli_gor += 1
            if metinli_gor == 1 and D.get("metinli"):
                ok("Metinli: metinli sorular testin sonunda", no > toplam - len(D["metinli"]))
            ok("Metinli: 'Aradığın' şeridi ve metin açıldı, şıklar kanıttan önce gizli", page.is_visible("#sq .kalp-serit") and page.is_visible("#sq .pasaj") and page.is_hidden("#sq .opts"))
            page.click(f"#sq .cumle[data-c='{q['kanit'][0]}']"); ileri(50)
            ok("Metinli: kanıt bulununca şıklar açıldı", page.is_visible("#sq .opts"))
            if q.get("tuzak") and not tuzak_gor:
                metin_tz = q["secenekler"][q["tuzak"][0]]
                page.locator("#sq .opt", has_text=tam(metin_tz)).click(); ileri(50); tuzak_gor = True
                ok("Metinli: tuzak şık seçilince 'Bu bir tuzak şık!'", "tuzak şık" in page.inner_text("#sq .fb"))
        dogru_metin = ["Metinde açıkça yazıyor.", "Metinde yazmıyor, ima ediliyor."][q["dogru"]] if q.get("ima") else q["secenekler"][q["dogru"]] if "secenekler" in q else None
        if not yanlis2 and not met and bulmali(q) and "secenekler" in q:
            yanlis2 = True
            for t in [x for j, x in enumerate(q["secenekler"]) if j != q["dogru"]][:2]:
                page.locator("#sq .opt", has_text=tam(t)).first.click(); ileri(50)
            ok("Test: iki yanlışta 'Neden yanlış yaptın?' sorulmuyor, Sonraki açık", page.query_selector("#sqEk .hn") is None and page.get_attribute("[data-sonraki]", "disabled") is None)
            ok("Test: cevap gösterilince 'Sorunun kalbi' satırı", page.is_visible("#sq .kalp-hatir"))
        elif "cevap" in q or "nokta" in q:
            ok_k = page.is_visible(f"#sq {alan(q)}"); ileri(8000); cevapla(page, "#sq", q); ileri(50)
            if not ok_k: ok(f"Test: {alan(q)} sorunun kalbinden sonra açık", False, qtext[:60])
        else:
            if not q.get("ima"):   # aynı metinli sorular: şıkları ekrandakilerle uyuşanı seç
                ekran = page.locator("#sq .opt").all_inner_texts()
                for x in [q] + [x for x in TUM if x is not q and x["soru"] == q["soru"] and "secenekler" in x]:
                    if all(any(re.fullmatch(r"[a-d]\) " + re.escape(o), e) for e in ekran) for o in x["secenekler"]): q = x; dogru_metin = x["secenekler"][x["dogru"]]; break
            ileri(8000); loc = page.locator("#sq .opt:not([disabled])", has_text=tam(dogru_metin))
            if loc.count():
                loc.first.click(); ileri(50)
                for x in [x for x in TUM if x is not q and x["soru"] == q["soru"] and "secenekler" in x]:   # aynı metinli başka soru (görseli farklı)
                    if not page.is_visible("#sq .fb.hint"): break
                    l2 = page.locator("#sq .opt:not([disabled])", has_text=tam(x["secenekler"][x["dogru"]]))
                    if l2.count(): l2.first.click(); ileri(50)
            else: print("ESLESMEDI:", qtext, "| beklenen:", dogru_metin, "| şıklar:", page.locator("#sq .opt").all_inner_texts(), "| kalp-not:", page.query_selector("#sq .kalp-not") is not None, "| opts gizli:", page.is_hidden("#sq .opts"))
        if not page.query_selector("[data-sonraki]"): print("DURUM:", page.inner_text("#panel")[:500]); break
        if page.get_attribute("[data-sonraki]", "disabled") is not None: ileri(15000)
        if page.get_attribute("[data-sonraki]", "disabled") is not None:
            print("TAKILDI:", qtext, "| met:", met, "| şıklar:", [(o.inner_text(), o.get_attribute("class"), o.is_disabled()) for o in page.locator("#sq .opt").all()], "| fb:", page.inner_text("#sq .fb")[:150] if page.is_visible("#sq .fb") else "-", "| opts gizli:", page.is_hidden("#sq .opts"), "| kalp:", page.get_attribute("#sq .kalp-not", "class") if page.query_selector("#sq .kalp-not") else None)
            page.screenshot(path="/tmp/takildi.png"); break
        if not page.query_selector("[data-sonraki]"): print("DURUM:", page.inner_text("#panel")[:400]); break
        page.click("[data-sonraki]"); ileri(200)
    if kalp_ok >= 5: ok("Seri ödülü çalışıyor (5 üst üste bulunca bulmalı bir soru bulmasız geldi)", SERI_OGREN or seri_gor)
    else: print("   (bilgi) Öğren'de seri için yeterli bulmalı soru yok:", kalp_ok)
    beklenen_m = len(D.get("metinli", [])) + sum(1 for x in D["sorular"] if x.get("kanit") and ("metin" in x or "tablo" in x))
    ok(f"Test: {beklenen_m} metinli (kanıtlı) soru geldi", metinli_gor >= beklenen_m, str(metinli_gor))
    sonuc = page.inner_text("#panel")
    ok("Test bitti (sonuç ekranı)", "Sonuç" in sonuc or "tamamladın" in sonuc, sonuc[:80])
    print("   (bilgi) test sonu kartı:", "var" if page.query_selector(".kalp-kart") else "yok (eşik tutmadı)")
    page.screenshot(path=f"/tmp/dk_{KONU}_sonuc.png", full_page=False)

    # Çalışma kâğıdı
    page.click("[data-tab=bak]"); ileri(100); page.click("[data-konu-ck]"); ileri(50)
    with ctx.expect_page() as yeni: page.click("[data-ck-yap]")
    kg = yeni.value; kg.wait_for_load_state(); html = kg.content()
    ok("Kâğıt: '[[' yok, 'Soru senden şunu istiyor' var", "[[" not in html and "Soru senden şunu istiyor" in html)
    kg.close()
    ok("390 px'te yatay taşma yok", not page.evaluate("document.documentElement.scrollWidth > innerWidth"))
    ok("Konsolda hata yok", not hatalar, "; ".join(hatalar[:3]))
    b.close()
yok = [s for s in SONUC if not s[1]]
print(f"\n{len(SONUC) - len(yok)}/{len(SONUC)} kontrol geçti")
sys.exit(1 if yok else 0)
