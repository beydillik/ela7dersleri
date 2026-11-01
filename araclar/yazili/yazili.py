import re
"""Yazılıya Hazırlık veri üretici ve doğrulayıcı (bütün dersler için ortak).
Kullanım: araclar/yazili/<kod>_<id>.py dosyası Y = Yazili("fen1", "d1y1", ...) ile başlar, kazanım, formül,
MEB sorusu (ikizleriyle), Kuark'ın hatası ve prova yazılılarını ekler, en sonda Y.yaz() çağırır.
Çıktı: public/<kod>/yazili/<id>.json. JSON elle düzenlenmez; betik düzenlenip yeniden çalıştırılır.

Madde (bir sorunun a, b, c… kısmı):
  {"harf", "soru", "formul"?, "iskele"? (Sınav Provası soru biçimi: secim/dy/dytablo/bosluk/eslestir/kisa),
   "cevap"? (örnek cevap), "anahtarlar"? [{"ad", "k": [kök…]} | {"ad", "sira": [[kök…], [kök…], …]}], "puan"? (prova)}
  - iskele + cevap: önce iskele (seçmeli/eşleştirme…) sonra yazma; yalnız iskele: madde iskeleyle puanlanır.
  - Anahtar kökleri Türkçe karakterli yazılır; motor karşılaştırırken harfleri sadeleştirir (ı→i, ş→s…).
"""
import json, os, re, unicodedata

KOK = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ISKELE_TUR = {"secim", "dy", "dytablo", "bosluk", "eslestir", "kisa"}


def sade(s):
    s = str(s).replace("I", "ı").replace("İ", "i").lower()
    s = s.translate(str.maketrans("ıçğöşüâîû", "icgosuaiu"))
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def sira_tamam(metin, sira):
    """Sıra anahtarı: her öğe (alternatif kökler) bir öncekinden SONRA geçmeli (açgözlü arama; motordaki yzSira ile aynı)."""
    t, i = sade(metin), 0
    for alt in sira:
        yer = [t.find(sade(x), i) for x in alt]; yer = [y for y in yer if y >= 0]
        if not yer: return False
        i = min(yer) + 1
    return True


def parca_ok(p, metin):
    """Basamak 2 parça kontrolü (motordaki yzParcaOk ile aynı)."""
    t = sade(metin).strip()
    if not t: return False
    if p.get("serbest"): return len(t) >= 3
    if p.get("hepsi"): return all(any(sade(x) in t for x in g) for g in p["hepsi"])
    if p.get("sira"): return sira_tamam(metin, p["sira"])
    return any(sade(x) in t for x in p.get("k", []))


class Yazili:
    def __init__(self, kod, id, **ust):
        """ust: baslik, ders, senaryo, sure, tarih, dagilim, giris, kapsamDisi, puanNotu, kaynakNotu; isteğe bağlı
        soruBaslik/soruEtiket/soruGiris (MEB dışı soru seti, ör. öğretmenin çalışma kâğıdı), kazanimAd ("konu"),
        ikizsiz=True (yalnız verilen sorular: "Benzerini çöz" yok)."""
        self.kod, self.id = kod, id
        self.d = {"id": id, **ust, "kazanimlar": [], "formuller": [], "mebSorular": [], "kuarkHata": [], "provalar": []}

    def kazanim(self, **k): self.d["kazanimlar"].append(k); return k
    def formul(self, **k): self.d["formuller"].append(k); return k
    def meb(self, **k): self.d["mebSorular"].append(k); return k
    def kuark(self, **k): self.d["kuarkHata"].append(k); return k
    def prova(self, **k): self.d["provalar"].append(k); return k

    # ---------- doğrulama ----------
    def _iskele(self, q, yer, h):
        t = q.get("tur")
        if t not in ISKELE_TUR: h.append(f"{yer}: iskele türü '{t}'"); return
        if t == "secim":
            s = q.get("secenekler", [])
            if len(s) != 4 or len(set(s)) != 4 or not 0 <= q.get("dogru", -1) < 4: h.append(f"{yer}: secim 4 farklı şık + dogru")
        elif t == "dy":
            if not isinstance(q.get("dogru"), bool) or not q.get("ifade"): h.append(f"{yer}: dy")
        elif t == "dytablo":
            if len(q.get("ifadeler", [])) < 2 or any(not isinstance(x.get("d"), bool) for x in q["ifadeler"]): h.append(f"{yer}: dytablo")
        elif t == "bosluk":
            cs = q.get("cumleler", [])
            if len(cs) < 2 or any(c["c"].count("___") != 1 for c in cs) or len({c["cevap"] for c in cs}) != len(cs): h.append(f"{yer}: bosluk")
            if set(q.get("havuz", [])) & {c["cevap"] for c in cs}: h.append(f"{yer}: havuzda cevap var (cevaplar motorca eklenir)")
        elif t == "eslestir":
            if not 3 <= len(q.get("ciftler", [])) <= 5: h.append(f"{yer}: eslestir 3–5 çift")
        elif t == "kisa":
            if not q.get("yanit"): h.append(f"{yer}: kisa yanit")
        if not q.get("aciklama"): h.append(f"{yer}: iskele açıklaması yok")

    def _madde(self, m, yer, h, prova=False):
        if not m.get("soru"): h.append(f"{yer}: soru yok")
        if not m.get("iskele") and not m.get("cevap"): h.append(f"{yer}: ne iskele ne cevap")
        if m.get("iskele"): self._iskele(m["iskele"], yer + " iskele", h)
        if m.get("formul") and m["formul"] not in {f["id"] for f in self.d["formuller"]}: h.append(f"{yer}: formül yok '{m['formul']}'")
        if m.get("cevap"):
            an = m.get("anahtarlar") or []
            if not an: h.append(f"{yer}: anahtar yok")
            for a in an:
                if not a.get("ad") or not (a.get("k") or a.get("sira")): h.append(f"{yer}: anahtar eksik {a}")
                # örnek cevap kendi anahtarlarını karşılamalı (motorun otomatik işaretlemesiyle aynı mantık)
                cv = sade(m["cevap"])
                if a.get("k") and not any(sade(x) in cv for x in a["k"]): h.append(f"{yer}: örnek cevap '{a['ad']}' anahtarını karşılamıyor")
                if a.get("sira") and not sira_tamam(cv, a["sira"]): h.append(f"{yer}: örnek cevap sıra anahtarını karşılamıyor")
        if prova and not isinstance(m.get("puan"), int): h.append(f"{yer}: puan yok")
        if m.get("basamak"): self._basamak(m, yer, h)

    def _basamak(self, m, yer, h):
        b, an = m["basamak"], m.get("anahtarlar") or []
        sec = b.get("sec")
        if sec is not None and (len(sec.get("secenekler", [])) != 3 or len(set(sec["secenekler"])) != 3 or sec.get("dogru") != 0 or not sec.get("ipucu") or not sec.get("aciklama")): h.append(f"{yer}: basamak 1 (3 farklı şık, dogru 0, ipucu, açıklama)")
        if not b.get("parcalar"): h.append(f"{yer}: parça yok")
        for j, p in enumerate(b.get("parcalar", [])):
            if not p.get("bas") or not p.get("ornek") or len(p.get("havuz", [])) != 2: h.append(f"{yer} parça {j + 1}: bas/ornek/havuz(2)")
            if not parca_ok(p, p.get("ornek", "")): h.append(f"{yer} parça {j + 1}: örnek kendi kontrolünü geçmiyor")
            if not p.get("serbest") and any(parca_ok(p, x) for x in p.get("havuz", [])): h.append(f"{yer} parça {j + 1}: çeldirici doğru sayılıyor")
        sablon = " ".join(p.get("bas", "") for p in b.get("parcalar", []))
        for a in an:
            if (a.get("k") and any(sade(x) in sade(sablon) for x in a["k"])) or (a.get("sira") and sira_tamam(sablon, a["sira"])):
                h.append(f"{yer}: cümle başları '{a['ad']}' anahtarını kendiliğinden karşılıyor")
        kc = m.get("kisaCevap", "")
        if not kc: h.append(f"{yer}: kısa cevap yok")
        elif an:
            r = sum(1 for a in an if (a.get("k") and any(sade(x) in sade(kc) for x in a["k"])) or (a.get("sira") and sira_tamam(kc, a["sira"]))) / len(an)
            if r < .7: h.append(f"{yer}: kısa cevap anahtarların %{round(r * 100)}'ini karşılıyor (en az %70)")
        if len(kc) > len(m.get("cevap", "")) and len(m.get("cevap", "")) > 40: h.append(f"{yer}: kısa cevap örnek cevaptan uzun")

    def _soru(self, q, yer, h, prova=False):
        if q.get("kazanim") not in self.kodlar: h.append(f"{yer}: kazanım yok '{q.get('kazanim')}'")
        if not q.get("maddeler"): h.append(f"{yer}: madde yok")
        harfler = [m.get("harf") for m in q.get("maddeler", [])]
        if harfler != list("abcdef"[:len(harfler)]): h.append(f"{yer}: harfler {harfler}")
        for m in q.get("maddeler", []): self._madde(m, f"{yer}{m.get('harf')}", h, prova)
        if prova and sum(m.get("puan", 0) for m in q["maddeler"]) != q.get("puan"): h.append(f"{yer}: madde puanları toplamı ≠ {q.get('puan')}")
        if "svg" in q and '"' in q["svg"]: h.append(f"{yer}: SVG'de çift tırnak")

    def dogrula(self):
        h, d = [], self.d
        self.kodlar = {k["kod"] for k in d["kazanimlar"]}
        konular = {k["id"] for u in json.load(open(f"{KOK}/public/{self.kod}/ders.json", encoding="utf-8"))["uniteler"] for k in u["konular"]}
        for k in d["kazanimlar"]:
            for f in ("kod", "ad", "kisa", "soru", "konular", "maddeler", "kelimeler", "hatalar"):
                if not k.get(f): h.append(f"{k.get('kod')}: {f} eksik")
            for c in k.get("konular", []):
                if c not in konular: h.append(f"{k['kod']}: konu yok {c}")
        ids = set()
        for q in d["mebSorular"]:
            if q["id"] in ids: h.append("id tekrar " + q["id"])
            ids.add(q["id"]); self._soru(q, q["id"], h)
            if len(q.get("ikizler", [])) < 1 and not d.get("ikizsiz"): h.append(q["id"] + ": ikiz yok")
            for i, z in enumerate(q.get("ikizler", [])):
                z.setdefault("kazanim", q["kazanim"]); z.setdefault("id", f"{q['id']}i{i + 1}")
                if z["id"] in ids: h.append("id tekrar " + z["id"])
                ids.add(z["id"]); self._soru(z, z["id"], h)
        for i, k in enumerate(d["kuarkHata"]):
            if k.get("kazanim") not in self.kodlar: h.append(f"kuark {i}: kazanım")
            if len(k.get("secenekler", [])) != 3 or not 0 <= k.get("dogru", -1) < 3 or len(set(k["secenekler"])) != 3: h.append(f"kuark {i}: 3 şık")
            for f in ("soru", "kuark", "ipucu", "aciklama", "dogruCevap"):
                if not k.get(f): h.append(f"kuark {i}: {f} yok")
            t = k.get("tamamla")
            if t:
                if k.get("tur") not in ("eksik", "yanilgi"): h.append(f"kuark {i}: tur eksik|yanilgi")
                if not parca_ok(t, t.get("ornek", "")) or len(t.get("havuz", [])) != 2 or any(parca_ok(t, x) for x in t["havuz"]): h.append(f"kuark {i}: tamamla (örnek kontrolü / 2 çeldirici)")
        yan = sum(1 for k in d["kuarkHata"] if k.get("tur") == "yanilgi")
        if yan > len(d["kuarkHata"]) / 2: h.append(f"kuark: yanılgı türü {yan} (eksik türünden az olmalı)")
        for z in d["kazanimlar"]:   # Hatırladığını Tekrarla: {doğru|çeldirici…}
            for j, t in enumerate(z.get("tekrar", [])):
                bs = re.findall(r"\{([^{}]+)\}", t["c"])
                if not bs or "{" in re.sub(r"\{[^{}]+\}", "", t["c"]) or not t.get("s"): h.append(f"{z['kod']} tekrar {j + 1}: boşluk/sayfa")
                for b in bs:
                    o = [x.strip() for x in b.split("|")]
                    if len(o) < 2 or len(set(o)) != len(o) or not all(o): h.append(f"{z['kod']} tekrar {j + 1}: '{b}' en az 1 çeldirici, tekrarsız")
            if z.get("tekrar") and len(z["tekrar"]) < 4: h.append(f"{z['kod']}: tekrar en az 4 cümle")
        for q in d["mebSorular"] + [z for q0 in d["mebSorular"] for z in q0.get("ikizler", [])]:
            for m in q["maddeler"]:
                for x in m.get("tetik", []):
                    if x not in m["soru"]: h.append(f"{q['id']}{m['harf']}: tetik '{x}' soru metninde yok")
        dag = {}
        for p in d["provalar"]:
            if p["id"] in ids: h.append("id tekrar " + p["id"])
            ids.add(p["id"]); top = 0; say = {}
            for n, q in enumerate(p["sorular"]):
                self._soru(q, f"{p['id']}-{n + 1}", h, prova=True); top += q.get("puan", 0)
                say[q["kazanim"]] = say.get(q["kazanim"], 0) + 1
            if top != 100: h.append(f"{p['id']}: toplam puan {top}")
            for q in p["sorular"]:
                if q.get("benzer") and q["benzer"] not in {x["id"] for x in d["mebSorular"]}: h.append(f"{p['id']}: benzer '{q['benzer']}' yok")
            if d.get("dagilim") and say != d["dagilim"]: h.append(f"{p['id']}: dağılım {say} ≠ senaryo {d['dagilim']}")
        return h

    def yaz(self):
        h = self.dogrula()
        d = self.d
        madde = lambda qs: sum(len(q["maddeler"]) for q in qs)
        ikiz = [z for q in d["mebSorular"] for z in q.get("ikizler", [])]
        print(f"kazanım {len(d['kazanimlar'])} | formül {len(d['formuller'])} | MEB soru {len(d['mebSorular'])} ({madde(d['mebSorular'])} madde) | "
              f"ikiz {len(ikiz)} ({madde(ikiz)} madde) | Kuark'ın hatası {len(d['kuarkHata'])} | prova {len(d['provalar'])} × "
              f"{[len(p['sorular']) for p in d['provalar']]} soru ({sum(madde(p['sorular']) for p in d['provalar'])} madde)")
        dag = [k["dogru"] for k in d["kuarkHata"]]
        bm = [m for q in d["mebSorular"] for m in q["maddeler"] if m.get("basamak")]
        print(f"basamaklı madde {len(bm)} | parça {sum(len(m['basamak']['parcalar']) for m in bm)} | kısa cevap ort. {round(sum(len(m['kisaCevap']) for m in bm) / max(1, len(bm)))} harf (örnek cevap ort. {round(sum(len(m['cevap']) for m in bm) / max(1, len(bm)))})")
        print("Kuark doğru şık dağılımı (motor karıştırır):", [dag.count(i) for i in range(3)])
        if h:
            print("HATA:", *h, sep="\n"); raise SystemExit(1)
        os.makedirs(f"{KOK}/public/{self.kod}/yazili", exist_ok=True)
        f = f"{KOK}/public/{self.kod}/yazili/{self.id}.json"
        json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("Sorun yok. Yazıldı:", os.path.relpath(f, KOK))
