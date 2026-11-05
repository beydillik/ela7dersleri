"""Dikkat paketi üreticisi (her ders için ortak).
Konu dosyalarına (public/<kod>/konular/<konu>.json) şu alanları yazar: dikkat, isinma:false, eskiKonu:false, tekrar, kisaCevap,
her soruda tetik + bolge ("sorunun kalbi"), isteğe bağlı metinli (Test'te 2 kısa sorunun yerine geçen metinli sorular).

Kullanım:  python3 -I araclar/dikkat/uret.py <kod> [konu …]        örn.  python3 -I araclar/dikkat/uret.py fen1 u3k1 u3k2
Veri:      araclar/dikkat/<kod>/<konu>.py  (bir dosyada birden çok konu olabilir). Dosyadaki sözlükler (anahtar = konu kimliği):
  TEKRAR  = {konu: [(cümle, sayfa), …]}      Hatırla ve Tekrarla; cümlede {doğru|çeldirici|çeldirici}
  KISA    = {konu: [ {soru, tetik, okut[3], parcalar, kisa, cevap, anahtarlar, sayfa}, … ]}   okut[0] doğru: "…-manı/-meni" biçiminde
  OKUT    = {konu: [[3 şık], [3 şık]]}         (isteğe bağlı) KISA'daki okut'ları sırayla değiştirir
  METINLI = {konu: [ {metin[], soru, bolge[], serit, kanit[], secenekler[3], dogru, tuzak[], ipucu, kanitIpucu, aciklama, kavram}, … ]}
  ELLE    = {soru metni: tetik ifadesi}       kalıpla bulunamayan soru kelimeleri
  BOLGE   = {soru metni: [ifade, …]}           otomatik "sorunun kalbi" bölgesini elle değiştirir
Hata varsa hiçbir dosya yazılmaz. Sayıları yazdırır. Kitap sayfası kuralı: [s. N] işaretinin ÜSTÜNDEKİ metin N. sayfadadır.
"""
import json, re, sys, os, glob

KOK = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
KOD = sys.argv[1]; ISTENEN = sys.argv[2:]
GEN = r"(?:hangisi\w*|hangileri\w*|hangi \w+|ne için|nedir|nelerdir|neler|ne olur|ne denir|ne yapar|ne işe yarar|kaç(?: kat| yıl| sınıfa| tane)?|kim(?= kontrol)|nerede(?:dir)?|nereye|nereden|nasıl\w*|neyi \w+|neye \w+|neden|niçin|DEĞİLDİR|ARANMAZ|doğrudur|yanlıştır|nedenidir)"

def norm(s):
    return s.lower().replace("ı", "i").replace("İ", "i").replace("ş", "s").replace("ğ", "g").replace("ü", "u").replace("ö", "o").replace("ç", "c").replace("'", "").replace("’", "")

veri = {k: {} for k in ("TEKRAR", "KISA", "OKUT", "METINLI", "ELLE", "BOLGE")}
for f in sorted(glob.glob(os.path.join(os.path.dirname(__file__), KOD, "*.py"))):
    g = {}; exec(open(f, encoding="utf-8").read(), g)
    for k in veri: veri[k].update(g.get(k, {}))

EKSIK = []
def tetik_bul(soru):
    a = re.escape(veri["ELLE"][soru]) if soru in veri["ELLE"] else GEN
    m = re.search(r"(?<!\w)" + a + r"(?!\w)", soru, re.I)
    if not m: EKSIK.append(soru); return None
    return m.group(0)

def bolge_bul(soru, tetik):
    """Sorunun kalbi: soru kelimesinden sorunun sonuna (ilk '?') kadar. Soru kelimesi başta ise: soru kelimesi + son 3 kelime
    (kısa sorularda bütün soru). Elle: BOLGE."""
    if soru in veri["BOLGE"]: return veri["BOLGE"][soru]
    t = tetik[0]; i = soru.find(t)
    j = soru.find("?", i); j = len(soru) if j < 0 else j
    parca = soru[i:j].rstrip(" .")
    bas = soru[:i].strip()
    if bas and not bas.endswith((".", "?", "!")):
        # Kısa bölge ("hangisidir", "nedir") anlam taşımaz: aynı cümlede 2–3 kelime geriye genişlet ("kanı vücuda taşıyan damar hangisidir")
        n = len(parca.split()); geri = 3 if n == 1 else 2 if n <= 3 else 0
        if geri:
            cumle = re.split(r"(?<=[.?!])\s+", bas)[-1].split()
            ek = [w for w in cumle[-geri:] if not w.startswith(("'", '"', "“"))]
            if ek: parca = soru[soru.rfind(" ".join(ek), 0, i):j].rstrip(" .")
        return [parca]
    kel = parca.split()
    if len(kel) <= 5: return [parca]
    son = " ".join(kel[-3:])
    return [t, son] if son not in t and t not in son else [parca]

def kontrol_kisa(kod, d, hata):
    for i, t in enumerate(d["tekrar"]):
        p = re.findall(r"\{([^{}]+)\}", t["c"])
        if not p: hata.append(f"{kod} tekrar {i+1}: boşluk yok")
        for b in p:
            o = [x.strip() for x in b.split("|")]
            if len(o) < 2 or len(set(o)) != len(o): hata.append(f"{kod} tekrar {i+1}: boşluk seçenekleri hatalı {o}")
        if not t["s"]: hata.append(f"{kod} tekrar {i+1}: sayfa yok")
    if len(d["tekrar"]) < 4: hata.append(f"{kod}: en az 4 Hatırla ve Tekrarla cümlesi")
    for i, q in enumerate(d["kisaCevap"]):
        for t in q["tetik"] + q.get("bolge", []):
            if t not in q["soru"]: hata.append(f"{kod} kisa {i+1}: tetik/bölge soruda yok: {t}")
        if len(q["okut"]) != 3 or len(set(q["okut"])) != 3: hata.append(f"{kod} kisa {i+1}: okut 3 farklı şık olmalı")
        for p in q["parcalar"]:
            kk = [norm(x) for x in p["k"]]
            if not any(x in norm(p["ornek"]) for x in kk): hata.append(f"{kod} kisa {i+1} {p['bas']}: örnek kendi kökünü karşılamıyor")
            for h in p["havuz"]:
                if any(x in norm(h) for x in kk): hata.append(f"{kod} kisa {i+1} {p['bas']}: çeldirici kökü içeriyor: {h}")
            if any(x in norm(p["bas"]) for x in kk): hata.append(f"{kod} kisa {i+1}: cümle başı kökü içeriyor: {p['bas']}")
        for a in q["anahtarlar"]:
            if not any(norm(x) in norm(q["kisa"]) for x in a["k"]): hata.append(f"{kod} kisa {i+1}: kısa cevap anahtarı karşılamıyor: {a['ad']}")
            if not any(norm(x) in norm(q["cevap"]) for x in a["k"]): hata.append(f"{kod} kisa {i+1}: uzun örnek anahtarı karşılamıyor: {a['ad']}")
        if len(q["kisa"]) >= len(q["cevap"]): hata.append(f"{kod} kisa {i+1}: kısa cevap uzun örnekten kısa olmalı")

def kontrol_metinli(kod, d, hata):
    adlar = {k["ad"] for k in d["kavramlar"]}
    for i, q in enumerate(d.get("metinli", [])):
        n = f"{kod} metinli {i+1}"
        if not 2 <= len(q["metin"]) <= 8: hata.append(f"{n}: metin 2–8 cümle olmalı")
        for t in q["bolge"]:
            if t not in q["soru"]: hata.append(f"{n}: bölge soruda yok: {t}")
        if not q["kanit"] or any(not (0 <= c < len(q["metin"])) for c in q["kanit"]): hata.append(f"{n}: kanıt indeksi hatalı")
        if len(q["secenekler"]) != 3 or len(set(q["secenekler"])) != 3: hata.append(f"{n}: 3 farklı şık olmalı")
        if q["dogru"] not in range(3): hata.append(f"{n}: doğru indeksi hatalı")
        if q["dogru"] in q.get("tuzak", []): hata.append(f"{n}: doğru şık tuzak olamaz")
        for c in q.get("tuzak", []):
            kok = lambda t: {w[:4] for w in re.findall(r"\w+", norm(t)) if len(w) >= 4}   # Türkçe ekler için kaba kök: ilk 4 harf
            ort = kok(q["secenekler"][c]) & kok(" ".join(q["metin"]))
            if not ort: hata.append(f"{n}: tuzak şık metindeki kelimeleri içermiyor: {q['secenekler'][c]}")
        if q.get("kavram") and q["kavram"] not in adlar: hata.append(f"{n}: kavram yok: {q['kavram']}")
        for a in ("serit", "aciklama", "ipucu", "kanitIpucu"):
            if not q.get(a): hata.append(f"{n}: {a} eksik")
        if not re.search(r"s\. \d+", q["aciklama"]): hata.append(f"{n}: açıklamada sayfa yok")

hata, yaz = [], []
for kod in (ISTENEN or sorted(veri["TEKRAR"])):
    yol = os.path.join(KOK, "public", KOD, "konular", kod + ".json")
    d = json.load(open(yol, encoding="utf-8"))
    d["dikkat"] = True; d["isinma"] = False; d["eskiKonu"] = False
    d["tekrar"] = [{"c": c, "s": s} for c, s in veri["TEKRAR"][kod]]
    kc = json.loads(json.dumps(veri["KISA"][kod]))
    for q, ok in zip(kc, veri["OKUT"].get(kod, [])): q["okut"] = ok
    for q in kc: q["bolge"] = bolge_bul(q["soru"], q["tetik"])
    d["kisaCevap"] = kc
    n = 0
    for q in [k["soru"] for k in d["kavramlar"] if k.get("soru")] + d["sorular"]:
        t = tetik_bul(q["soru"])
        if t: q["tetik"] = [t]; q["bolge"] = bolge_bul(q["soru"], q["tetik"]); n += 1
    if kod in veri["METINLI"]: d["metinli"] = veri["METINLI"][kod]
    else: d.pop("metinli", None)
    kontrol_kisa(kod, d, hata); kontrol_metinli(kod, d, hata)
    yaz.append((yol, d))
    print(f"{kod}: Hatırla ve Tekrarla {len(d['tekrar'])} cümle / {sum(len(re.findall(r'{[^{}]+}', t['c'])) for t in d['tekrar'])} boşluk"
          f" | kısa cevap {len(kc)} | sorunun kalbi {n} soru | metinli {len(d.get('metinli', []))}")
    if os.environ.get("GOSTER"):
        for q in [k["soru"] for k in d["kavramlar"] if k.get("soru")] + d["sorular"] + kc + d.get("metinli", []):
            print("    ", q.get("bolge"), "←", q["soru"])
if EKSIK: print("SORU KELİMESİ BULUNAMADI (ELLE'ye ekle):", *EKSIK, sep="\n  ")
if EKSIK or hata: print("HATA:", *hata, sep="\n  "); sys.exit(1)
for yol, d in yaz: open(yol, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
print("Sorun yok; yazıldı.")
