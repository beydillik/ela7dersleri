"""İngilizce (MEB, ing1) okuma yaklaşımı — 3., 4., 5. ünite u3k1–u5k2 (18 Kasım 2026, Kemal'le anlaşılan ilk dönem kapsamı).
Konu başına 3 ikiz çift; "Bu soru senden ne istiyor?" (NE) yalnız ikizlere. Testte sorulan sayı eskisi gibi
(TESTSORU = havuz büyümeden önceki soru sayısı = 10; motor bunun 2'sini metinli sorulara ayırır).
İkiz kuralı: eşin doğru cevabı çeldiricilerden birinde (gerekirse eski sorunun çeldiricisi _eski ile değiştirildi); ipucu eşin cevabını söylemez.
İngilizce farkı: {{…}} içi vurgulanamaz (motor bağlam sayar); VURGU yalnız Türkçe kısımda. Fark İngilizce cümledeyse NE adımı onu gösterir.
Dinleme soruları ikiz yapılmadı. Bilgi ve sayfalar kitaptan (kaynaklar/ing1/unite3–5.md)."""
import json

def _konu(konu): return json.load(open(f"public/ing1/konular/{konu}.json", encoding="utf-8"))

def _q(konu, bas):
    l = [q for q in _konu(konu)["sorular"] if q["soru"].startswith(bas)]
    assert l and (len(l) == 1 or all(q.get("ikiz") for q in l)), (konu, bas, len(l))
    return l[0]

def _S(konu, bas): return _q(konu, bas)["soru"]

def _eski(konu, bas, degis, ipucu=None, aciklama=None, adimlar=None):
    """Eski sorunun bir çeldiricisini ikiz eşinin cevabıyla değiştirir (doğru şık aynı kalır); gerekirse ipucu/açıklama da."""
    q = _q(konu, bas)
    y = {k: q[k] for k in ("soru", "secenekler", "dogru", "ipucu", "aciklama", "kavram", "yardim", "dinle") if k in q}
    for a, b in degis.items(): assert a in q["secenekler"] or b in q["secenekler"], (konu, a)   # yeniden çalıştırınca zaten değişmiş olabilir
    y["secenekler"] = [degis.get(s, s) for s in q["secenekler"]]
    assert y["secenekler"][y["dogru"]] == q["secenekler"][q["dogru"]]
    if ipucu: y["ipucu"] = ipucu
    if aciklama: y["aciklama"] = aciklama
    if adimlar: y["yardim"] = dict(y.get("yardim") or {}, adimlar=adimlar)
    return y

def Y(soru, secenekler, dogru, ipucu, aciklama, kavram, hatirla=None):
    e = {"soru": soru, "secenekler": secenekler, "dogru": dogru, "ipucu": ipucu, "aciklama": aciklama, "kavram": kavram}
    if hatirla: e["yardim"] = {"hatirla": hatirla}
    return e

# ---------- ikiz soruları ----------
# u3k1
A1a = _S("u3k1", "{{To go from one residence"); A1b = "{{To receive a diploma}} tanımı hangi kelimenin?"
A1c = _S("u3k1", "{{Helen ___ in New York"); A1d = "{{Helen ___ to Miami in 2015. She lives there now.}} Hangisi uygun?"
A1e = _S("u3k1", "{{Bill ___ chemistry"); A1f = "{{Bill ___ from university in 2008.}} Boşluğa ne gelir?"
# u3k2
A2a = _S("u3k2", "{{A reward for winning"); A2b = "{{To stop living, to pass away}} tanımı hangi kelimenin?"
A2c = _S("u3k2", "{{My friend James has"); A2d = "{{My friend James won an excellent ___ in photography.}}"
A2e = _S("u3k2", "Bir çift için hangisi önce"); A2f = "Bir çift için hangisi en son olur?"
# u3k3
A3a = _S("u3k3", "{{Mehmed II died ___"); A3b = _S("u3k3", "{{Louis Braille was born ___")
A3c = _S("u3k3", "{{___ did you get married?}}"); A3d = "{{___ did you move to New York?}} — {{Because I wanted to make music in New York.}} Boşluğa ne gelir?"
A3e = _S("u3k3", "{{When were you born?}}"); A3f = "{{Where were you born?}} Hangisi uygun cevap?"
# u4k1
B1a = _S("u4k1", "Hangisi memeli değildir"); B1b = "Hangisi memelidir?"
B1c = _S("u4k1", "Hangisi bir kuştur"); B1d = "Hangisi bir kuş değildir ({{bird}})?"
B1e = _S("u4k1", "{{It's an animal. Does it live in the jungle"); B1f = "{{It's an animal. Does it live in the desert? Yes, it does.}} Hangi hayvan olabilir?"
# u4k2
B2a = _S("u4k2", "{{There aren't any Dodo"); B2b = "{{There aren't many tigers in the world.}} Kaplan için hangisi doğru?"
B2c = _S("u4k2", "Ormanları kesip tarla"); B2d = "Havayı ve suyu kirli hâle getirmek hangi kelimeyle anlatılır?"
B2e = _S("u4k2", "{{Don't kill the elephants"); B2f = "{{Don't kill the tigers for their ___.}} Boşluğa hangisi gelir?"
# u4k3
B3a = _S("u4k3", "Sokak hayvanları ({{stray animals}}) için hangisi iyi"); B3b = "Sokak hayvanları ({{stray animals}}) için hangisi kötü bir öneridir?"
B3c = _S("u4k3", "{{should}}'dan sonra"); B3d = "{{stop}}'tan sonra fiil nasıl gelir?"
B3e = _S("u4k3", "{{Destroy the forests.}}"); B3f = "{{Protect the forests.}} Bu iyi bir davranış. Hangi öneri doğru?"
# u5k1
C1a = _S("u5k1", "Maria'nın en sevdiği"); C1b = "Maria'nın hiç izlemediği program hangisidir? {{I never watch soap operas.}}"
C1c = _S("u5k1", "{{Companies try to sell"); C1d = "{{It informs people about the latest events happening all over the world.}} Bu hangi program?"
C1e = _S("u5k1", "{{A group of people"); C1f = _S("u5k1", "{{It is a kind of TV show.")
# u5k2
C2a = _S("u5k2", "{{My favourite TV programmes are sitcoms"); C2b = "{{I never watch soap operas. They're ___.}} Boşluğa hangisi gelir?"
C2c = _S("u5k2", "{{Nora: I find them boring"); C2d = "{{Nora: I find them boring. I prefer amusing programmes.}} Nora nasıl programları sevmez?"
C2e = _S("u5k2", "{{Lisa: I prefer soap operas"); C2f = "{{Lisa: I prefer soap operas. They have more drama and emotional depth.}} Hangisi yanlıştır?"

EKSORU = {
 "u3k1": [
  _eski("u3k1", "{{To go from one residence", {"grow up": "graduate"}),
  Y(A1b, ["move", "graduate", "study"], 1, "{{diploma}} okulu bitirince verilir. Okulu bitirmeyi anlatan kelimeyi düşün.",
    "{{To receive a diploma}}: diploma almak, yani {{graduate}} (mezun olmak) (s. 55).", "graduate"),
  _eski("u3k1", "{{Helen ___ in New York", {"graduated": "moved"},
        ipucu="{{till 2015}} “2015'e kadar” demek. Helen o zamana kadar New York'tan ayrılmadı."),
  Y(A1d, ["stayed", "moved", "was born"], 1, "{{to Miami}} “Miami'ye” demek. Bir yerden başka bir yere gitmeyi anlatan kelimeyi bul.",
    "{{Helen moved to Miami in 2015.}} 2015'te Miami'ye taşındı; şimdi orada yaşıyor. {{move}}: taşınmak (s. 46, s. 55).", "move"),
  _eski("u3k1", "{{Bill ___ chemistry", {},
        ipucu="{{chemistry}} bir derstir, bir bölümdür. Bir bölümde eğitim almayı anlatan kelimeyi bul."),
  Y(A1f, ["studied", "graduated", "grew up"], 1, "{{from university}} kalıbına bak: okul kelimesinden önce {{from}} alan kelimeyi düşün.",
    "Bill 2008'de üniversiteden mezun oldu: {{graduated from university}} (s. 56).", "graduate"),
 ],
 "u3k2": [
  _eski("u3k2", "{{My friend James has", {},
        ipucu="{{has}} “sahip” demek. James yıllardır fotoğrafçılık yapıyor: bir işte yıllar içinde ilerlemeyi anlatan kelimeyi düşün."),
  _eski("u3k2", "{{A reward for winning", {"alone": "die"}),
  Y(A2b, ["award", "die", "career"], 1, "{{stop living}} “yaşamayı bırakmak” demek. Biyografiler genelde bu olayla biter.",
    "{{To stop living, to pass away}}: ölmek, yani {{die}} (s. 55).", "die"),
  Y(A2d, ["award", "career", "biography"], 0, "{{won}} “kazandı” demek. Kazanılan bir şey hangisi?",
    "{{win an award}}: ödül kazanmak. James fotoğrafçılıkta bir ödül kazandı (s. 46, s. 55).", "award"),
  Y(A2f, ["get engaged", "get married", "raise children"], 2, "Bill'in hayatında sıra: önce evlendi, sonra ne oldu?",
    "Önce nişanlanılır, sonra evlenilir, çocuk yetiştirmek en sonda gelir. Bill 2012'de evlendi, 2015'te oğlu oldu (s. 56).", "raise"),
 ],
 "u3k3": [
  Y(A3d, ["Why", "When", "Where"], 0, "Cevaba bak: {{Because}} ile başlıyor.",
    "Cevap {{Because}} ile başlıyorsa soru {{Why}} ile sorulur: {{Why did you move to New York?}} (s. 57).", "Why did you …?"),
  Y(A3f, ["In Phoenix, Arizona.", "Well... A long time ago, in 1944.", "To find a better job."], 0, "{{Where}} bir yer sorar. Hangi cevap bir yer söylüyor?",
    "{{Where were you born?}} — {{In Phoenix, Arizona.}} Doğduğu yeri söyler (s. 61).", "When / Where were you born?"),
 ],
 "u4k1": [
  _eski("u4k1", "Hangisi memeli değildir", {}, ipucu="Memeliler sütle beslenir, vücutlarında kıl vardır. Hangisinin kanatları var?",
        adimlar=["Memelilerin vücudunda kıl vardır, yavruları sütle beslenir.", "Kuşların kanadı vardır.", "Şıklardan hangisi kanatlı ve uçuyor?"]),
  Y(B1b, ["eagle", "lizard", "whale"], 2, "Memeliler sıcakkanlıdır ve yavruları sütle beslenir. Kuş ve sürüngen olanı ele.",
    "{{whale}} (balina) bir memelidir. {{eagle}} kuş, {{lizard}} sürüngendir (s. 64, s. 67).", "mammal"),
  Y(B1d, ["owl", "eagle", "horse"], 2, "Kuşların kanatları vardır. Kanadı olmayan hayvanı bul.",
    "{{horse}} (at) bir memelidir. {{owl}} ve {{eagle}} kuştur (s. 64, s. 67).", "bird"),
  Y(B1f, ["tiger", "camel", "whale"], 1, "{{desert}} kumlu ve susuz bir yerdir. Orada yaşayabilen hayvanı düşün.",
    "{{Camels can survive in the deserts for a long time.}} Deve çölde yaşar (s. 74).", "desert"),
 ],
 "u4k2": [
  Y(B2b, ["It is extinct.", "It is endangered.", "It is poisonous."], 1, "{{many}} “çok” demek. {{aren't many}}: çok yok, az var.",
    "{{This means there aren't many tigers in the world.}} Kaplanların nesli tehlikede: {{endangered}} (s. 70).", "endangered"),
  Y(B2d, ["pollute", "hunt", "destroy"], 0, "Kirli hâle getirmeyi anlatan kelimeyi düşün.",
    "{{pollute}}: kirletmek. {{They also polluted the environment.}} (s. 68).", "pollute"),
  _eski("u4k2", "{{Don't kill the elephants", {"milk": "fur"},
        ipucu="Fillerin ağzının iki yanından çıkan uzun beyaz dişleri düşün."),
  Y(B2f, ["tusks", "fur", "wings"], 1, "Kaplanların vücudu siyah ve turuncu çizgilerle kaplıdır.",
    "Kaplanların güzel, çizgili kürkleri vardır. {{Don't kill the animals for their fur.}} (s. 70).", "fur"),
 ],
 "u4k3": [
  _eski("u4k3", "{{Destroy the forests.}}", {}, ipucu="Bu davranışı yapmalı mıyız, yapmamalı mı? Fiilin yazımına da bak."),
  Y(B3b, ["We should feed the stray animals.", "We should hunt the stray animals.", "We should protect the stray animals."], 1,
    "Hayvanlara zarar veren öneriyi bul.",
    "Sokak hayvanlarını avlamak kötü bir öneridir. Kitap onları beslemeyi öneriyor: {{Feed the stray animals.}} (s. 70).", "feed"),
  _eski("u4k3", "{{should}}'dan sonra", {"-s ile: should protects": "-ing ile: should protecting"}),
  Y(B3d, ["Yalın hâliyle: stop hunt", "-ing ile: stop hunting", "-s ile: stop hunts"], 1, "Kitaptaki öneriyi hatırla: {{Stop … the animals for their skin, fur or teeth.}}",
    "{{stop}}'tan sonra fiil {{-ing}} alır: {{Stop hunting the animals for their skin, fur or teeth.}} (s. 69, s. 75).", "stop hunting"),
  Y(B3f, ["We should protect the forests.", "We shouldn't protect the forests.", "We shouldn't to protect the forests."], 0,
    "Bu davranışı yapmalı mıyız, yapmamalı mı? Fiilin yazımına da bak.",
    "İyi davranış {{should}} ile önerilir: {{We should protect the forests.}} (s. 69, s. 75).", "should"),
 ],
 "u5k1": [
  Y(C1b, ["Haberler", "Pembe diziler", "Gerçeklik şovları"], 1, "{{never}} “asla, hiç” demek. Cümlede hangi program geçiyor?",
    "{{I never watch soap operas.}} Maria pembe dizileri hiç izlemez (s. 84).", "soap opera"),
  Y(C1d, ["news", "commercial", "sitcom"], 0, "{{latest events}} “en son olaylar” demek.",
    "Dünyadaki en son olayları anlatan program haberlerdir: {{news}} (s. 87).", "news"),
  _eski("u5k1", "{{A group of people", {"news": "soap opera"}),
 ],
 "u5k2": [
  _eski("u5k2", "{{My favourite TV programmes are sitcoms", {}, aciklama="Sevdiği program eğlenceli: {{They're amusing.}} Kitapta: {{I think they are amusing.}} (s. 90)."),
  Y(C2b, ["amusing", "boring", "educational"], 1, "{{never watch}} “hiç izlemem” demek. Sevmediğimiz bir programı nasıl anlatırız?",
    "{{I never watch soap operas. They are boring.}} Pembe dizileri sıkıcı bulur (s. 84).", "boring"),
  Y(C2d, ["Eğlenceli programları", "Sıkıcı programları", "Komik programları"], 1, "{{I find them …}} “onları … buluyorum” demek. Sevmediği programları nasıl buluyor?",
    "{{I find them boring.}} Nora sıkıcı programları sevmez (s. 85).", "boring"),
  Y(C2f, ["Lisa pembe dizileri sevmiyor.", "Lisa pembe dizileri tercih ediyor.", "Lisa'ya göre pembe dizilerde daha çok dram var."], 0,
    "Her seçeneği cümleyle karşılaştır. Cümleye uymayanı bul.",
    "{{I prefer soap operas.}} Lisa pembe dizileri tercih ediyor, yani seviyor. {{more drama}}: daha çok dram (s. 97).", "prefer"),
 ],
}

IKIZ = {
 "u3k1": [[A1a, A1b], [A1c, A1d], [A1e, A1f]], "u3k2": [[A2a, A2b], [A2c, A2d], [A2e, A2f]],
 "u3k3": [[A3a, A3b], [A3c, A3d], [A3e, A3f]], "u4k1": [[B1a, B1b], [B1c, B1d], [B1e, B1f]],
 "u4k2": [[B2a, B2b], [B2c, B2d], [B2e, B2f]], "u4k3": [[B3a, B3b], [B3c, B3d], [B3e, B3f]],
 "u5k1": [[C1a, C1b], [C1c, C1d], [C1e, C1f]], "u5k2": [[C2a, C2b], [C2c, C2d], [C2e, C2f]],
}

# Testte sorulan sayı eskisi gibi (18 Kasım 2026 öncesi: 10 soru, 2'si metinli)
TESTSORU = {k: 10 for k in IKIZ}

NE = {
 A1a: ["Başka bir yere gitmeyi anlatan kelimeyi", "Diploma almayı anlatan kelimeyi"], A1b: ["Diploma almayı anlatan kelimeyi", "Başka bir yere gitmeyi anlatan kelimeyi"],
 A1c: ["Helen'in 2015'e kadar ne yaptığını", "Helen'in 2015'te ne yaptığını"], A1d: ["Helen'in 2015'te ne yaptığını", "Helen'in 2015'e kadar ne yaptığını"],
 A1e: ["Bill'in kimyayla ilgili ne yaptığını", "Bill'in 2008'de ne yaptığını"], A1f: ["Bill'in 2008'de ne yaptığını", "Bill'in kimyayla ilgili ne yaptığını"],
 A2a: ["Yarışmada kazanılanı anlatan kelimeyi", "Yaşamın sona ermesini anlatan kelimeyi"], A2b: ["Yaşamın sona ermesini anlatan kelimeyi", "Yarışmada kazanılanı anlatan kelimeyi"],
 A2c: ["James'in fotoğrafçılıkta sahip olduğu şeyi", "James'in fotoğrafçılıkta kazandığı şeyi"], A2d: ["James'in fotoğrafçılıkta kazandığı şeyi", "James'in fotoğrafçılıkta sahip olduğu şeyi"],
 A2e: ["En önce olanı", "En son olanı"], A2f: ["En son olanı", "En önce olanı"],
 A3a: ["Gün, ay ve yıldan önce gelen kelimeyi", "Yalnız yıldan önce gelen kelimeyi"], A3b: ["Yalnız yıldan önce gelen kelimeyi", "Gün, ay ve yıldan önce gelen kelimeyi"],
 A3c: ["Cevabı bir yıl olan sorunun kelimesini", "Cevabı bir sebep olan sorunun kelimesini"], A3d: ["Cevabı bir sebep olan sorunun kelimesini", "Cevabı bir yıl olan sorunun kelimesini"],
 A3e: ["Doğduğu zamanı söyleyen cevabı", "Doğduğu yeri söyleyen cevabı"], A3f: ["Doğduğu yeri söyleyen cevabı", "Doğduğu zamanı söyleyen cevabı"],
 B1a: ["Memeli olmayan hayvanı", "Memeli olan hayvanı"], B1b: ["Memeli olan hayvanı", "Memeli olmayan hayvanı"],
 B1c: ["Kuş olan hayvanı", "Kuş olmayan hayvanı"], B1d: ["Kuş olmayan hayvanı", "Kuş olan hayvanı"],
 B1e: ["Ormanda yaşayan hayvanı", "Çölde yaşayan hayvanı"], B1f: ["Çölde yaşayan hayvanı", "Ormanda yaşayan hayvanı"],
 B2a: ["Dünyada hiç kalmayan hayvanın durumunu", "Dünyada az kalan hayvanın durumunu"], B2b: ["Dünyada az kalan hayvanın durumunu", "Dünyada hiç kalmayan hayvanın durumunu"],
 B2c: ["Ormanı kesmeyi anlatan kelimeyi", "Kirletmeyi anlatan kelimeyi"], B2d: ["Kirletmeyi anlatan kelimeyi", "Ormanı kesmeyi anlatan kelimeyi"],
 B2e: ["Fillerin hangi parçası için öldürüldüğünü", "Kaplanların hangi parçası için öldürüldüğünü"], B2f: ["Kaplanların hangi parçası için öldürüldüğünü", "Fillerin hangi parçası için öldürüldüğünü"],
 B3a: ["İyi olan öneriyi", "Kötü olan öneriyi"], B3b: ["Kötü olan öneriyi", "İyi olan öneriyi"],
 B3c: ["should'dan sonraki fiilin hâlini", "stop'tan sonraki fiilin hâlini"],
 B3d: ["stop'tan sonraki fiilin hâlini", "should'dan sonraki fiilin hâlini"],
 B3e: ["Kötü davranış için doğru öneriyi", "İyi davranış için doğru öneriyi"], B3f: ["İyi davranış için doğru öneriyi", "Kötü davranış için doğru öneriyi"],
 C1a: ["Maria'nın en sevdiği programı", "Maria'nın hiç izlemediği programı"], C1b: ["Maria'nın hiç izlemediği programı", "Maria'nın en sevdiği programı"],
 C1c: ["Ürün satmaya çalışan programı", "En son olayları anlatan programı"], C1d: ["En son olayları anlatan programı", "Ürün satmaya çalışan programı"],
 C1e: ["Komik durumları anlatan programı", "Duygusal olayları anlatan programı"], C1f: ["Duygusal olayları anlatan programı", "Komik durumları anlatan programı"],
 C2a: ["Sevilen programı anlatan kelimeyi", "Hiç izlenmeyen programı anlatan kelimeyi"], C2b: ["Hiç izlenmeyen programı anlatan kelimeyi", "Sevilen programı anlatan kelimeyi"],
 C2c: ["Nora'nın sevdiği programları", "Nora'nın sevmediği programları"], C2d: ["Nora'nın sevmediği programları", "Nora'nın sevdiği programları"],
 C2e: ["Cümleye uyan seçeneği", "Cümleye uymayan seçeneği"], C2f: ["Cümleye uymayan seçeneği", "Cümleye uyan seçeneği"],
}

# İkizlerde farkı yaratan sözcük + soru kelimesi sarı (yalnız Türkçe kısım; {{…}} içi vurgulanamaz)
VURGU = {
 A1a: ["tanımı hangi kelimenin"], A1b: ["tanımı hangi kelimenin"],
 A1c: ["Hangisi uygun"], A1d: ["Hangisi uygun"],
 A1e: ["Boşluğa ne gelir"], A1f: ["Boşluğa ne gelir"],
 A2a: ["tanımı hangi kelimenin"], A2b: ["tanımı hangi kelimenin"],
 A2e: ["hangisi önce olur"], A2f: ["hangisi en son olur"],
 A3c: ["Boşluğa ne gelir"], A3d: ["Boşluğa ne gelir"],
 A3e: ["Hangisi uygun cevap"], A3f: ["Hangisi uygun cevap"],
 B1a: ["Hangisi", "memeli değildir"], B1b: ["Hangisi", "memelidir"],
 B1c: ["Hangisi", "bir kuştur"], B1d: ["Hangisi", "bir kuş değildir"],
 B1e: ["Hangi hayvan"], B1f: ["Hangi hayvan"],
 B2a: ["Dodo kuşu", "hangisi doğru"], B2b: ["Kaplan için", "hangisi doğru"],
 B2c: ["Ormanları kesip tarla yapmak", "hangi kelimeyle"], B2d: ["kirli hâle getirmek", "hangi kelimeyle"],
 B2e: ["Boşluğa hangisi gelir"], B2f: ["Boşluğa hangisi gelir"],
 B3a: ["hangisi iyi bir öneridir"], B3b: ["hangisi kötü bir öneridir"],
 B3c: ["sonra fiil nasıl gelir"], B3d: ["sonra fiil nasıl gelir"],
 B3e: ["kötü bir davranış", "Hangi öneri"], B3f: ["iyi bir davranış", "Hangi öneri"],
 C1a: ["en sevdiği program", "hangisidir"], C1b: ["hiç izlemediği program", "hangisidir"],
 C1c: ["Bu hangi program"], C1d: ["Bu hangi program"],
 C1e: ["Bu hangi program"], C1f: ["Bu hangi program"],
 C2a: ["Boşluğa hangisi gelir"], C2b: ["Boşluğa hangisi gelir"],
 C2c: ["nasıl programları sever"], C2d: ["nasıl programları sevmez"],
 C2e: ["Hangisi doğrudur"], C2f: ["Hangisi yanlıştır"],
 # Öğren: soru kelimesi kalıbın dışında kalan eski soru (vurgusuz geliyordu)
 "Memeli yavrular doğunca neyle beslenir?": ["neyle beslenir"],
}

# Yeni soruların "sorunun kalbi" bölgeleri (eski soruların bölgeleri bolge.py'de; Türkçe kısmı kısa olan TUM)
BOLGE = {
 A1b: "TUM", A1d: "TUM", A1f: "TUM",
 A2b: "TUM", A2d: "TUM", A2f: ["hangisi en son olur"],
 A3d: "TUM", A3f: "TUM",
 B1b: "TUM", B1d: ["bir kuş değildir"], B1f: "TUM",
 B2b: ["Kaplan için hangisi doğru"], B2d: ["hangi kelimeyle anlatılır"], B2f: "TUM",
 B3b: ["hangisi kötü bir öneridir"], B3d: ["sonra fiil nasıl gelir"], B3f: ["iyi bir davranış", "Hangi öneri doğru"],
 C1b: ["hiç izlemediği program hangisidir"], C1d: "TUM",
 C2b: "TUM", C2d: ["nasıl programları sevmez"], C2f: ["yanlıştır"],
}
