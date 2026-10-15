"""Sınav Provası soru havuzu üretici ve doğrulayıcı (bütün dersler için ortak).
Kullanım: her ders/ünite için araclar/sinav/<kod>_u<no>.py dosyası H = Havuz("fen1", 2, "f2") ile başlar,
H.add(...) ile soruları ekler, en sonda H.yaz() çağırır. Çıktı: public/<kod>/sinav/u<no>.json.
Kurallar: kavram, konunun kavramlar[].ad değerleriyle birebir; açıklama Ela'nın anlayacağı 1–2 kısa cümle (≤ ~18 kelime) + sayfa."""
import json, os, re
KOK = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ONC = ["Yalnız I", "I ve II", "II ve III", "I, II ve III"]
ONC2 = ["Yalnız I", "Yalnız II", "I ve III", "II ve III"]

class Havuz:
    def __init__(self, kod, unite, onek):
        self.kod, self.unite, self.onek, self.Q = kod, unite, onek, []
    def add(self, konu, kavram, tur, **k):
        q = {"id": f"{self.onek}-{len(self.Q)+1:02d}", "konu": konu, "kavram": kavram, "tur": tur, **k}
        self.Q.append(q); return q
    def dogrula(self):
        Q, h, tur, dag, per = self.Q, [], {}, [0, 0, 0, 0], {}
        ad = {}
        for k in {q["konu"] for q in Q}:
            f = f"{KOK}/public/{self.kod}/konular/{k}.json"
            if not os.path.exists(f): h.append(f"konu dosyası yok: {k}"); ad[k] = set(); continue
            ad[k] = {x["ad"] for x in json.load(open(f, encoding="utf-8")).get("kavramlar", [])}
        ids = set()
        for q in Q:
            i = q["id"]; t = q["tur"]
            if i in ids: h.append(i + ": id tekrar")
            ids.add(i)
            tur[t] = tur.get(t, 0) + 1; per[q["konu"]] = per.get(q["konu"], 0) + 1
            if q["kavram"] not in ad.get(q["konu"], set()): h.append(f"{i}: kavram yok '{q['kavram']}' ({q['konu']})")
            a = q.get("aciklama", "")
            if not a: h.append(i + ": açıklama yok")
            elif len(re.sub(r"\(s\.[^)]*\)", "", a).split()) > 20: h.append(f"{i}: açıklama uzun ({len(a.split())} kelime)")
            if t == "secim":
                s = q.get("secenekler", [])
                if len(s) != 4 or len(set(s)) != 4 or not (isinstance(q.get("dogru"), int) and 0 <= q["dogru"] < 4): h.append(i + ": seçenek/doğru")
                else: dag[q["dogru"]] += 1
                if q.get("onculler") and (not q.get("kok") or len(q["onculler"]) not in (2, 3)): h.append(i + ": öncül/kök")
                if not q.get("soru"): h.append(i + ": soru yok")
            elif t == "dy":
                if not isinstance(q.get("dogru"), bool) or not q.get("ifade"): h.append(i + ": dy")
                if q["dogru"] is False and not q.get("duzeltme"): h.append(i + ": yanlış ifadede düzeltme yok")
            elif t == "dytablo":
                if len(q.get("ifadeler", [])) < 3 or any(not isinstance(x.get("d"), bool) for x in q["ifadeler"]): h.append(i + ": dytablo")
            elif t == "bosluk":
                for c in q.get("cumleler", []):
                    if c["c"].count("___") != 1: h.append(i + ": ___ sayısı")
                cv = [c["cevap"] for c in q.get("cumleler", [])]
                if len(cv) != len(set(cv)): h.append(i + ": aynı cevap iki kez")
                if set(q.get("havuz", [])) & set(cv): h.append(i + ": havuz cevap içeriyor (motor ekler)")
                if len(q.get("cumleler", [])) < 3: h.append(i + ": boşluk az")
            elif t == "eslestir":
                if not 3 <= len(q.get("ciftler", [])) <= 5: h.append(i + ": eşleştirme sayısı")
            elif t == "kisa":
                if not q.get("yanit") or not q.get("soru"): h.append(i + ": kısa")
            else: h.append(f"{i}: bilinmeyen tür {t}")
        return h, tur, dag, per
    def yaz(self, aciklama="Sınav Provası soru havuzu. Sorular kitaba ve sitedeki konu anlatımına dayanarak yazıldı; okul testlerinin yalnızca biçimi örnek alındı."):
        h, tur, dag, per = self.dogrula()
        print(f"{self.kod} u{self.unite}: soru {len(self.Q)} | tür {tur} | konu {per} | doğru şık {dag}")
        if h: print("HATA:", *h, sep="\n  "); raise SystemExit(1)
        os.makedirs(f"{KOK}/public/{self.kod}/sinav", exist_ok=True)
        json.dump({"unite": self.unite, "ders": self.kod, "aciklama": aciklama, "sorular": self.Q},
                  open(f"{KOK}/public/{self.kod}/sinav/u{self.unite}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("Sorun yok, yazıldı.")
