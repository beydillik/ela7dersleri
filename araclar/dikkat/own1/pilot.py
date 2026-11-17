"""İngilizce (Own It, own1) okuma yaklaşımı — Unit 3 ve 4, u3k1–u4k6 (18 Kasım 2026, Kemal'le anlaşılan ilk dönem kapsamı).
Konu başına 3 ikiz çift; "Bu soru senden ne istiyor?" (NE) yalnız ikizlere. Testte sorulan sayı eskisi gibi
(TESTSORU = havuz büyümeden önceki soru sayısı; motor bunun 2'sini metinli sorulara ayırır).
İkiz kuralı: eşin doğru cevabı (ya da kalıbı) çeldiricilerden birinde (gerekirse eski sorunun çeldiricisi _eski ile değişti);
ipucu eşin cevabını söylemez. Bazı çiftler iki eski sorudan oluşur (aynı soru kalıbı, zıt cevap).
İngilizce farkı: {{…}} içi vurgulanamaz; VURGU yalnız Türkçe kısımda. Fark İngilizce cümledeyse NE adımı onu gösterir.
Dinleme soruları ikiz yapılmadı. Bilgi ve sayfalar kitaptan (kaynaklar/own1/unite3–4.md; SB s. N, WB s. N = [s. 1000+N]).
Yeniden çalıştırılabilir: _eski değişmiş şıkları da kabul eder."""
import json

def _konu(konu): return json.load(open(f"public/own1/konular/{konu}.json", encoding="utf-8"))

def _q(konu, bas):
    l = [q for q in _konu(konu)["sorular"] if q["soru"].startswith(bas)]
    assert l and (len(l) == 1 or all(q.get("ikiz") for q in l)), (konu, bas, len(l))
    return l[0]

def _S(konu, bas): return _q(konu, bas)["soru"]

def _eski(konu, bas, degis, ipucu=None, aciklama=None, adimlar=None):
    """Eski sorunun bir çeldiricisini ikiz eşinin cevabıyla değiştirir (doğru şık aynı kalır); gerekirse ipucu/açıklama da."""
    q = _q(konu, bas)
    y = {k: q[k] for k in ("soru", "secenekler", "dogru", "ipucu", "aciklama", "kavram", "yardim", "dinle") if k in q}
    for a, b in degis.items(): assert a in q["secenekler"] or b in q["secenekler"], (konu, a)
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
# Unit 3
A1a = _S("u3k1", "Boşluğa hangisi gelir? {{In my country"); A1b = "Boşluğa hangisi gelir? {{When their guests left, they came outside to ___ goodbye.}}"
A1c = _S("u3k1", "Boşluğa hangisi gelir? {{Mr Hicks"); A1d = "Boşluğa hangisi gelir? {{Kazue's brother was very friendly and he ___ a lot.}}"
A1e = _S("u3k1", "Kazue'nin ailesi Japonya'dan"); A1f = "Hikâyeye göre Kazue havalimanına gelince yazar ne yaptı?"
A2a = _S("u3k2", "Boşluğa hangisi gelir? {{Kazue sometimes"); A2b = "Boşluğa hangisi gelir? {{Kazue quietly ___ in my ear that Japanese people don't usually do that.}}"
A2c = _S("u3k2", "Boşluğa hangisi gelir? {{I asked Luis"); A2d = "Boşluğa hangisi gelir? {{In the 1950s, machines could translate written texts, but they could not ___ spoken language.}}"
A2e = _S("u3k2", "Hangisi zıt anlamlı"); A2f = "Hangisi benzer anlamlı iki kelimedir?"
A3a = _S("u3k3", "{{Most people couldn't"); A3b = _S("u3k3", "{{It's possible that")
A3c = _S("u3k3", "Boşluğa hangisi gelir? {{Today, you"); A3d = "Boşluğa hangisi gelir? {{For centuries, nobody ___ read Egyptian hieroglyphics.}}"
A3e = _S("u3k3", "Boşluğa hangisi gelir? {{When she was younger"); A3f = "Boşluğa hangisi gelir? {{Don't speak too quietly during the presentation tomorrow. People ___ hear you.}}"
A4a = _S("u3k4", "Boşluğa hangisi gelir? {{Paula"); A4b = "Boşluğa hangisi gelir? {{I like ___ jokes, but I can never make them sound funny.}}"
A4c = _S("u3k4", "Boşluğa hangisi gelir? {{Mike"); A4d = "Boşluğa hangisi gelir? {{I ___ sorry to Luisa yesterday.}}"
A4e = _S("u3k4", "Boşluğa hangisi gelir? {{I'm not very good"); A4f = "Boşluğa hangisi gelir? {{I know I said I was 16, but I wasn't telling ___.}}"
A5a = _S("u3k5", "Hangisi {{since}} ile"); A5b = _S("u3k5", "Hangisi {{for}} ile")
A5c = _S("u3k5", "Boşluğa hangisi gelir? {{She hasn't seen"); A5d = _S("u3k5", "Boşluğa hangisi gelir? {{We've lived")
A5e = _S("u3k5", "Boşluğa hangisi gelir? {{A: How long have you known"); A5f = "Boşluğa hangisi gelir? {{A: How long have you lived here? B: ___ about six months.}}"
A6a = _S("u3k6", "Boşluğa hangisi gelir? {{They ___ much Russian"); A6b = "Boşluğa hangisi gelir? {{Sorry! I ___ so busy since I got here.}}"
A6c = _S("u3k6", "Boşluğa hangisi gelir? {{I can't play football"); A6d = _S("u3k6", "Boşluğa hangisi gelir? {{I ___ in London")
A6e = _S("u3k6", "Hangisi {{these days}}"); A6f = "Hangisi {{before}} ile aynı anlama gelir?"
# Unit 4
B1a = _S("u4k1", "{{get ill}} kelimesinin zıt"); B1b = "{{relax}} kelimesinin zıt anlamlısı hangisi?"
B1c = _S("u4k1", "Doktor: {{Does your chest"); B1d = _S("u4k1", "Tom: {{I think I'm getting ill")
B1e = _S("u4k1", "{{Don't ___ about your exams"); B1f = "Azra'nın ateşi var. {{It isn't a good idea to do school work if you want to ___.}} Boşluğa hangisi gelir?"
B2a = _S("u4k2", "Astronotlar: {{If they get stressed"); B2b = _S("u4k2", "{{Astronauts ___ a lot on Earth")
B2c = _S("u4k2", "{{He ___ a lot when he exercises"); B2d = "{{After a stressful week, we all need to ___ and have a little fun.}}"
B2e = _S("u4k2", "{{Some astronauts go ___!"); B2f = "{{We all need to get enough ___, but in space, that's not easy.}}"
B3a = _S("u4k3", "{{I have some time to do my homework"); B3b = _S("u4k3", "{{The team has three or four")
B3c = _S("u4k3", "{{We spent too ___ time"); B3d = _S("u4k3", "{{If you lose too ___ games")
B3e = _S("u4k3", "Bugün doğum günün"); B3f = _S("u4k3", "{{I want to go out, but I'm coughing")
B4a = _S("u4k4", "{{We get most of our energy"); B4b = _S("u4k4", "{{This helps food pass")
B4c = _S("u4k4", "{{There is a lot of this in cheese"); B4d = "{{The food tofu is very high in this.}}"
B4e = _S("u4k4", "{{I try to eat ___ with plenty"); B4f = "{{Her doctor told her not to eat ___ such as milk or cheese.}}"
B5a = _S("u4k5", "{{My team loses every game!}}"); B5b = _S("u4k5", "{{I sneeze a lot in the summer.}}")
B5c = _S("u4k5", "{{___ Paula stay at home"); B5d = _S("u4k5", "{{We ___ to eat lots of fruit")
B5e = _S("u4k5", "{{Should I drink more water?}}"); B5f = "{{Should I drink coffee at night?}} — {{No, you ___.}}"
B6a = _S("u4k6", "{{I can recommend ___"); B6b = _S("u4k6", "Robby: {{Jogging isn't your thing?")
B6c = _S("u4k6", "{{Have you ever tried ___ with a cat"); B6d = "{{Why don't you ___ a sports club after school?}}"
B6e = _S("u4k6", "Hangi kalıptan sonra fiil {{-ing}}"); B6f = "Hangi kalıptan sonra fiil yalın gelir?"

EKSORU = {
 "u3k1": [
  Y(A1b, ["wave", "smile", "shake"], 0, "{{goodbye}} ile birlikte kullanılan hareketi düşün: ayrılırken elle yapılır.",
    "Misafirler giderken dışarı çıkıp el salladılar: {{wave goodbye}} (SB s. 130).", "wave"),
  _eski("u3k1", "Boşluğa hangisi gelir? {{Mr Hicks", {"waved": "smiled"}),
  Y(A1d, ["greeted", "smiled", "shook"], 1, "{{very friendly}}: çok cana yakın. Cana yakın biri yüzüyle ne yapar?",
    "Kazue'nin kardeşi çok cana yakındı ve çok gülümsedi: {{he smiled a lot}} (WB s. 24).", "smile"),
  Y(A1f, ["Onunla el sıkıştı.", "Ona gülümsedi.", "Onu selamladı."], 2, "Hikâyenin ilk cümlelerine bak: {{I ___ her at the airport when she arrived.}}",
    "{{I greeted her at the airport when she arrived.}} Yazar Kazue'yi havalimanında selamladı (WB s. 24).", "greet"),
 ],
 "u3k2": [
  Y(A2b, ["shouted", "posted", "whispered"], 2, "{{quietly}}: sessizce. {{in my ear}}: kulağıma.",
    "Kazue kulağına sessizce fısıldadı: {{whispered}} (WB s. 24).", "whisper"),
  Y(A2d, ["describe", "whisper", "interpret"], 2, "Yazılı metin değil, konuşma çevriliyor. Konuşmayı başka dile aktaran kelimeyi düşün.",
    "Makineler yazıyı çevirebiliyordu ama konuşmayı çeviremiyordu: {{they could not interpret spoken language}} (SB s. 36).", "interpret"),
  Y(A2f, ["shout – whisper", "post – describe", "translate – interpret"], 2, "İkisi de bir dili başka dile aktarmakla ilgili olan çifti bul.",
    "{{translate}} ve {{interpret}} ikisi de başka dile çevirmek demek (yazı / konuşma) (SB s. 35–36).", "translate"),
 ],
 "u3k3": [
  Y(A3d, ["could", "can", "won't be able to"], 0, "{{For centuries}}: yüzyıllar boyunca. Bu cümle geçmişi anlatıyor.",
    "Kitapta: {{For centuries, nobody could read Egyptian hieroglyphics.}} Geçmiş: {{could}} (SB s. 37).", "could"),
  _eski("u3k3", "Boşluğa hangisi gelir? {{When she was younger", {"will be able to": "won't be able to"}),
  Y(A3f, ["can", "won't be able to", "couldn't"], 1, "{{tomorrow}}: yarın. Çok sessiz konuşursan ne olur?",
    "Yarınki sunumda çok sessiz konuşursan insanlar seni duyamayacak: {{won't be able to}} (SB s. 37).", "won't be able to"),
 ],
 "u3k4": [
  Y(A4b, ["saying", "telling", "say"], 1, "{{jokes}} hangi fiille kullanılıyordu? {{like}}'tan sonra fiil {{-ing}} alıyor.",
    "Şaka anlatmak {{tell a joke}}: {{I like telling jokes.}} (WB s. 27).", "tell a joke"),
  Y(A4d, ["told", "said", "spoke"], 1, "{{sorry}} hangi fiille kullanılıyordu? Geçmiş hâlini düşün.",
    "{{say sorry}} → {{said}}: {{I said sorry to Luisa.}} (SB s. 130).", "say sorry"),
  Y(A4f, ["the truth", "lies", "hello"], 0, "Konuşan kişi 16 yaşında olduğunu söylemiş ama bu doğru değilmiş. {{wasn't}} olumsuz: neyi söylemiyormuş?",
    "16 yaşında olduğunu söyledi ama doğruyu söylemiyordu: {{I wasn't telling the truth.}} (WB s. 30).", "tell the truth"),
 ],
 "u3k5": [
  _eski("u3k5", "Hangisi {{since}} ile", {"two months": "three weeks"},
        aciklama="{{since my birthday}}: doğum günümden beri. {{three weeks}} ve {{a while}} süredir: {{for}} ile kullanılır (SB s. 120)."),
  _eski("u3k5", "Hangisi {{for}} ile", {"last week": "my birthday"},
        aciklama="{{for three weeks}}: üç haftadır. {{my birthday}} ve {{yesterday}} bir an gösterir: {{since}} ile kullanılır (SB s. 120)."),
  Y(A5f, ["Since", "For", "Ago"], 1, "Cevaptan sonra bir süre geliyor: {{about six months}}.",
    "Süre → {{for}}: {{For about six months.}} (WB s. 28).", "for"),
 ],
 "u3k6": [
  Y(A6b, ["was", "'ve been", "am"], 1, "{{since I got here}}: buraya geldiğimden beri. Durum hâlâ sürüyor mu?",
    "Mario buraya geldiğinden beri hâlâ çok meşgul → present perfect: {{I've been so busy since I got here.}} (SB s. 39).", "present perfect"),
  Y(A6f, ["earlier", "since I was born", "at the moment"], 0, "{{before}} eskiden demek. Şimdiden önceki zamanı anlatan ifadeyi bul.",
    "{{before}} = {{earlier}}: eskiden, daha önce. {{Before, I didn't use to think about intonation, but now …}} (WB s. 29).", "before / later on"),
 ],
 "u4k1": [
  _eski("u4k1", "{{Don't ___ about your exams", {}, ipucu="Sınavdan önce insanın hissettiği gerginliği anlatan kelimeyi düşün."),
  Y(B1b, ["get stressed", "sneeze", "get better"], 0, "{{relax}} rahatlamak demek. Rahatlamanın tersi olan duyguyu bul.",
    "{{relax}} ↔ {{get stressed}}: {{If they get stressed, they relax.}} (SB s. 48).", "get stressed"),
  _eski("u4k1", "Doktor: {{Does your chest", {"relaxing": "sneezing"}),
  _eski("u4k1", "Tom: {{I think I'm getting ill", {"relaxing": "coughing"}),
  Y(B1f, ["get stressed", "get better", "have a fever"], 1, "Ateşi olan biri ne ister? Hastalığın bitmesini anlatan kelimeyi düşün.",
    "Ders çalışmak iyi bir fikir değil, Azra iyileşmek istiyorsa: {{if you want to get better}} (WB s. 32).", "get better"),
 ],
 "u4k2": [
  Y(B2d, ["relax", "sweat", "sneeze"], 0, "{{have a little fun}}: biraz eğlenmek. Eğlenmeye benzeyen, dinlenmeyi anlatan kelimeyi düşün.",
    "Yorucu bir haftadan sonra dinlenmek gerekir. Kitapta: {{We all need to relax and have a little fun.}} (WB s. 38).", "relax"),
  _eski("u4k2", "{{Some astronauts go ___!", {"sleeping": "sleep", "training": "sweating"}),
  Y(B2f, ["jogging", "sweating", "sleep"], 2, "{{get enough}}: yeterince almak. Uzayda günde 16 kez güneş doğar; bu neyi zorlaştırır?",
    "{{We all need to get enough sleep, but in space, that's not easy.}} (SB s. 48).", "get enough sleep"),
 ],
 "u4k3": [
  _eski("u4k3", "Bugün doğum günün", {}, ipucu="Mutluluk bir sorun mu? Duyguyu güçlendiren kelimeyi seç."),
 ],
 "u4k4": [
  _eski("u4k4", "{{We get most of our energy", {"fat": "fibre"}),
  _eski("u4k4", "{{This helps food pass", {"calories": "carbohydrates"}),
  Y(B4d, ["fat", "fibre", "protein"], 2, "Tofu, kasları ve vücudu güçlendiren besin bakımından zengindir.",
    "Tofuda bol protein vardır: {{tofu … is full of protein}} (WB s. 35, WB s. 36).", "protein"),
  Y(B4f, ["a balanced diet", "dairy products", "calories"], 1, "{{milk}} ve {{cheese}}: süt ve peynir. Sütten yapılan yiyecekler hangisi?",
    "Süt ve peynir süt ürünleridir: {{dairy products}} (SB s. 131).", "dairy products"),
 ],
 "u4k5": [
  Y(B5f, ["should", "shouldn't", "ought"], 1, "Kısa cevap {{No}} ile başlıyor: olumsuz.",
    "{{No, you shouldn't.}} Kahve gece uykuyu kaçırır: {{You shouldn't drink coffee at night.}} (WB s. 39).", "Should I …?"),
 ],
 "u4k6": [
  Y(B6d, ["joining", "join", "joined"], 1, "{{Why don't you}} kalıbından sonra fiil nasıl geliyordu? Forumdaki öneriyi hatırla.",
    "{{Why don't you}} + fiil yalın: {{Why don't you join a sports club?}} Kitaptaki örnek: {{Why don't you look online for some ideas?}} (SB s. 53).", "Why don't you …?"),
  Y(B6f, ["How about …?", "Have you tried …?", "Make sure you …"], 2, "Robby'nin uyarısını hatırla: {{… listen to something gentle.}}",
    "{{Make sure you}} + fiil yalın: {{Make sure you listen to something gentle.}} (SB s. 52).", "Make sure you …"),
 ],
}

IKIZ = {
 "u3k1": [[A1a, A1b], [A1c, A1d], [A1e, A1f]], "u3k2": [[A2a, A2b], [A2c, A2d], [A2e, A2f]],
 "u3k3": [[A3a, A3b], [A3c, A3d], [A3e, A3f]], "u3k4": [[A4a, A4b], [A4c, A4d], [A4e, A4f]],
 "u3k5": [[A5a, A5b], [A5c, A5d], [A5e, A5f]], "u3k6": [[A6a, A6b], [A6c, A6d], [A6e, A6f]],
 "u4k1": [[B1a, B1b], [B1c, B1d], [B1e, B1f]], "u4k2": [[B2a, B2b], [B2c, B2d], [B2e, B2f]],
 "u4k3": [[B3a, B3b], [B3c, B3d], [B3e, B3f]], "u4k4": [[B4a, B4b], [B4c, B4d], [B4e, B4f]],
 "u4k5": [[B5a, B5b], [B5c, B5d], [B5e, B5f]], "u4k6": [[B6a, B6b], [B6c, B6d], [B6e, B6f]],
}

# Testte sorulan sayı eskisi gibi (18 Kasım 2026 öncesi soru sayısı; 2'si metinli)
TESTSORU = {"u3k1": 8, "u3k2": 9, "u3k3": 11, "u3k4": 9, "u3k5": 10, "u3k6": 12,
            "u4k1": 8, "u4k2": 9, "u4k3": 11, "u4k4": 10, "u4k5": 11, "u4k6": 10}

NE = {
 A1a: ["Tanışırken yapılan hareketi", "Vedalaşırken yapılan hareketi"], A1b: ["Vedalaşırken yapılan hareketi", "Tanışırken yapılan hareketi"],
 A1c: ["Gelenleri karşılarken yapılanı", "Cana yakın birinin yüzüyle yaptığını"], A1d: ["Cana yakın birinin yüzüyle yaptığını", "Gelenleri karşılarken yapılanı"],
 A1e: ["Japonların tanışırken yapmadığını", "Yazarın havalimanında yaptığını"], A1f: ["Yazarın havalimanında yaptığını", "Japonların tanışırken yapmadığını"],
 A2a: ["Kazue'nin internette yaptığını", "Kazue'nin kulağa yaptığını"], A2b: ["Kazue'nin kulağa yaptığını", "Kazue'nin internette yaptığını"],
 A2c: ["Bir yerin nasıl olduğunu anlatmayı", "Konuşmayı başka dile çevirmeyi"], A2d: ["Konuşmayı başka dile çevirmeyi", "Bir yerin nasıl olduğunu anlatmayı"],
 A2e: ["Zıt anlamlı çifti", "Benzer anlamlı çifti"], A2f: ["Benzer anlamlı çifti", "Zıt anlamlı çifti"],
 A3a: ["couldn't geçen cümlenin zamanını", "will be able to geçen cümlenin zamanını"], A3b: ["will be able to geçen cümlenin zamanını", "couldn't geçen cümlenin zamanını"],
 A3c: ["Bugün yapılabileni anlatan kelimeyi", "Yüzyıllarca yapılamayanı anlatan kelimeyi"], A3d: ["Yüzyıllarca yapılamayanı anlatan kelimeyi", "Bugün yapılabileni anlatan kelimeyi"],
 A3e: ["Geçmişte yapamadığını anlatan kelimeyi", "Yarın yapamayacağını anlatan kelimeyi"], A3f: ["Yarın yapamayacağını anlatan kelimeyi", "Geçmişte yapamadığını anlatan kelimeyi"],
 A4a: ["hello ile kullanılan fiili", "jokes ile kullanılan fiili"], A4b: ["jokes ile kullanılan fiili", "hello ile kullanılan fiili"],
 A4c: ["joke ile kullanılan fiilin geçmişini", "sorry ile kullanılan fiilin geçmişini"], A4d: ["sorry ile kullanılan fiilin geçmişini", "joke ile kullanılan fiilin geçmişini"],
 A4e: ["Söylerken yüzün kızardığı şeyi", "Konuşanın söylemediği şeyi"], A4f: ["Konuşanın söylemediği şeyi", "Söylerken yüzün kızardığı şeyi"],
 A5a: ["since ile kullanılan ifadeyi", "for ile kullanılan ifadeyi"], A5b: ["for ile kullanılan ifadeyi", "since ile kullanılan ifadeyi"],
 A5c: ["a long time ifadesinden önce gelen kelimeyi", "2010 yılından önce gelen kelimeyi"], A5d: ["2010 yılından önce gelen kelimeyi", "a long time ifadesinden önce gelen kelimeyi"],
 A5e: ["Bir cümleden önce gelen kelimeyi", "Bir süreden önce gelen kelimeyi"], A5f: ["Bir süreden önce gelen kelimeyi", "Bir cümleden önce gelen kelimeyi"],
 A6a: ["Bitmiş bir dönemi anlatan fiili", "Hâlâ süren durumu anlatan fiili"], A6b: ["Hâlâ süren durumu anlatan fiili", "Bitmiş bir dönemi anlatan fiili"],
 A6c: ["Dün olup biten işi anlatan fiili", "Hâlâ süren işi anlatan fiili"], A6d: ["Hâlâ süren işi anlatan fiili", "Dün olup biten işi anlatan fiili"],
 A6e: ["these days ile aynı anlamı", "before ile aynı anlamı"], A6f: ["before ile aynı anlamı", "these days ile aynı anlamı"],
 B1a: ["Hasta olmanın zıddını", "Rahatlamanın zıddını"], B1b: ["Rahatlamanın zıddını", "Hasta olmanın zıddını"],
 B1c: ["Göğsü ağrıyan kişinin yaptığını", "Burnu kızaran kişinin yaptığını"], B1d: ["Burnu kızaran kişinin yaptığını", "Göğsü ağrıyan kişinin yaptığını"],
 B1e: ["Sınavdan önce yapma denen şeyi", "Hasta birinin istediği durumu"], B1f: ["Hasta birinin istediği durumu", "Sınavdan önce yapma denen şeyi"],
 B2a: ["Astronotların stresliyken yaptığını", "Astronotların uzaya gitmeden önce yaptığını"], B2b: ["Astronotların uzaya gitmeden önce yaptığını", "Astronotların stresliyken yaptığını"],
 B2c: ["Egzersizde kıyafeti ıslatan şeyi", "Eğlenmekle birlikte gereken şeyi"], B2d: ["Eğlenmekle birlikte gereken şeyi", "Egzersizde kıyafeti ıslatan şeyi"],
 B2e: ["Astronotların uzayda yaptığı sporu", "Uzayda yeterince almanın zor olduğu şeyi"], B2f: ["Uzayda yeterince almanın zor olduğu şeyi", "Astronotların uzayda yaptığı sporu"],
 B3a: ["Sayılamayan isimle kullanılanı", "Sayılabilen isimle kullanılanı"], B3b: ["Sayılabilen isimle kullanılanı", "Sayılamayan isimle kullanılanı"],
 B3c: ["time ile kullanılanı", "games ile kullanılanı"], B3d: ["games ile kullanılanı", "time ile kullanılanı"],
 B3e: ["Sorun olmayan duyguyu anlatan cümleyi", "Dışarı çıkmayı engelleyen durumu anlatan cümleyi"],
 B3f: ["Dışarı çıkmayı engelleyen durumu anlatan cümleyi", "Sorun olmayan duyguyu anlatan cümleyi"],
 B4a: ["Enerjinin çoğunu veren besini", "Yiyeceğin vücuttan geçmesine yardım edeni"], B4b: ["Yiyeceğin vücuttan geçmesine yardım edeni", "Enerjinin çoğunu veren besini"],
 B4c: ["Peynir ve çikolatada bol olanı", "Tofuda bol olan besini"], B4d: ["Tofuda bol olan besini", "Peynir ve çikolatada bol olanı"],
 B4e: ["Bol proteinli ve lifli beslenmeyi", "Süt ve peynir gibi yiyecekleri"], B4f: ["Süt ve peynir gibi yiyecekleri", "Bol proteinli ve lifli beslenmeyi"],
 B5a: ["Takımı hep kaybedene tavsiyeyi", "Yazın çok hapşırana tavsiyeyi"], B5b: ["Yazın çok hapşırana tavsiyeyi", "Takımı hep kaybedene tavsiyeyi"],
 B5c: ["Soru cümlesinin başına gelen kelimeyi", "Arkasından to gelen kelimeyi"], B5d: ["Arkasından to gelen kelimeyi", "Soru cümlesinin başına gelen kelimeyi"],
 B5e: ["Olumlu kısa cevabı", "Olumsuz kısa cevabı"], B5f: ["Olumsuz kısa cevabı", "Olumlu kısa cevabı"],
 B6a: ["recommend kelimesinden sonraki fiilin hâlini", "You could kalıbından sonraki fiilin hâlini"], B6b: ["You could kalıbından sonraki fiilin hâlini", "recommend kelimesinden sonraki fiilin hâlini"],
 B6c: ["Have you tried kalıbından sonraki fiilin hâlini", "Why don't you kalıbından sonraki fiilin hâlini"], B6d: ["Why don't you kalıbından sonraki fiilin hâlini", "Have you tried kalıbından sonraki fiilin hâlini"],
 B6e: ["Arkasından -ing gelen kalıbı", "Arkasından yalın fiil gelen kalıbı"], B6f: ["Arkasından yalın fiil gelen kalıbı", "Arkasından -ing gelen kalıbı"],
}

# Türkçe kısımda farkı yaratan sözcük + soru kelimesi sarı ({{…}} içi vurgulanamaz)
VURGU = {
 A1b: ["Boşluğa hangisi gelir"], A1d: ["Boşluğa hangisi gelir"],
 A1e: ["tanışırken", "ne yapmadığını"], A1f: ["Hikâyeye göre", "havalimanına gelince", "ne yaptı"],
 A2b: ["Boşluğa hangisi gelir"], A2d: ["Boşluğa hangisi gelir"],
 A2e: ["zıt anlamlı"], A2f: ["benzer anlamlı"],
 A3d: ["Boşluğa hangisi gelir"], A3f: ["Boşluğa hangisi gelir"],
 A4b: ["Boşluğa hangisi gelir"], A4d: ["Boşluğa hangisi gelir"], A4f: ["Boşluğa hangisi gelir"],
 A5f: ["Boşluğa hangisi gelir"], A6b: ["Boşluğa hangisi gelir"],
 A6f: ["aynı anlama gelir"],
 B1b: ["zıt anlamlısı hangisi"],
 B1f: ["Boşluğa hangisi gelir"],
 B3e: ["Hangisi doğru"], B3f: ["Hangisi doğru"],
 B5a: ["Tavsiye hangisi"], B5b: ["Tavsiye hangisi"],
 B6e: ["fiil", "alır"], B6f: ["fiil yalın gelir"],
 # Öğren: soru kelimesi kalıbın dışında kalan eski kavram soruları (vurgusuz geliyordu)
 _konu("u3k6")["kavramlar"][0]["soru"]["soru"]: ["bitti mi"],
 _konu("u4k2")["kavramlar"][0]["soru"]["soru"]: ["hafif tempoda koşuya çıkmak"],
}

# Yeni soruların "sorunun kalbi" bölgeleri (eski soruların bölgeleri bolge.py'de)
BOLGE = {
 A1b: "TUM", A1d: "TUM", A1f: ["havalimanına gelince yazar ne yaptı"],
 A2b: "TUM", A2d: "TUM", A2f: ["benzer anlamlı"],
 A3d: "TUM", A3f: "TUM",
 A4b: "TUM", A4d: "TUM", A4f: "TUM",
 A5f: "TUM", A6b: "TUM", A6f: ["aynı anlama gelir"],
 B1b: "TUM", B1f: ["Boşluğa hangisi gelir"],
 B2d: "TUM", B2f: "TUM",
 B4d: "TUM", B4f: "TUM",
 B5f: "TUM",
 B6d: "TUM", B6f: ["fiil yalın gelir"],
}
