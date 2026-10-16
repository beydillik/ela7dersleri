import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from ortak import Havuz, ONC, ONC2
H = Havuz("own1", 4, "o4"); a = H.add
SB47, SB48, SB49, SB56, SB131 = "(SB s. 47)", "(SB s. 48)", "(SB s. 49)", "(SB s. 56)", "(SB s. 131)"
WB32, WB94 = "(WB s. 32)", "(WB s. 94)"

# --- Konu 1: Health and fitness 1 (cough, get better, get ill, get stressed, have a fever, sneeze)
a("u4k1", "get ill", "secim", soru="{{to become sick}} tanımı hangi kelimenindir?",
  secenekler=["get better", "get ill", "get stressed", "relax"], dogru=1,
  aciklama=f"Hasta olmak: {{{{get ill}}}} {SB47}.")
a("u4k1", "get better", "eslestir", soru="Kelimeleri Türkçeleriyle eşleştir.", ciftler=[
  {"sol": "cough", "sag": "öksürmek"},
  {"sol": "sneeze", "sag": "hapşırmak"},
  {"sol": "get better", "sag": "iyileşmek"},
  {"sol": "have a fever", "sag": "ateşi olmak"}],
  aciklama=f"Sağlık kelimeleri {SB47}.")
a("u4k1", "have a fever", "bosluk", havuz=["relax", "train"], cumleler=[
  {"c": "He's very hot. I'm sure he has a ___.", "cevap": "fever"},
  {"c": "I'm sorry you're ill. I hope you get ___ soon.", "cevap": "better"},
  {"c": "Does your chest hurt? You're ___ a lot.", "cevap": "coughing"}],
  aciklama=f"Sıcaklık, iyileşme ve göğüs ağrısı ipuçlarına bak {SB131}.")
a("u4k1", "get stressed", "dy", ifade="{{get stressed}} ile {{relax}} aynı anlama gelir.", dogru=False,
  duzeltme="Zıt anlamlıdır: stres olmak ↔ rahatlamak.",
  aciklama=f"{{{{Don't get stressed – relax!}}}} {WB32}.")
a("u4k1", "sneeze", "kisa", soru="Hapşırmak. İngilizce yaz.", yanit="sneeze",
  aciklama=f"Hapşırmak: {{{{sneeze}}}} {SB47}.")
a("u4k1", "cough", "secim", soru="Sağlık kelimeleri ve anlamları:", onculler=["{{cough}}: öksürmek", "{{get better}}: hasta olmak", "{{sneeze}}: hapşırmak"],
  kok="Hangileri doğrudur?", secenekler=ONC2, dogru=2,
  aciklama=f"{{{{get better}}}} iyileşmek; hasta olmak {{{{get ill}}}} {SB47}.")

# --- Konu 2: Health and fitness 2 (go jogging, train, warm up, work out, sweat, relax, get enough sleep)
a("u4k2", "warm up", "secim", soru="{{to exercise gently before doing sport}} tanımı hangi kelimenindir?",
  secenekler=["work out", "sweat", "go jogging", "warm up"], dogru=3,
  aciklama=f"Spordan önce hafif egzersiz: {{{{warm up}}}} {SB47}.")
a("u4k2", "work out", "bosluk", havuz=["sneezes", "coughs"], cumleler=[
  {"c": "Lucia is very fit because she ___ at the gym every day.", "cevap": "works out"},
  {"c": "He ___ a lot when he exercises. His clothes get very wet!", "cevap": "sweats"},
  {"c": "Sam is ___ for a half marathon at the moment.", "cevap": "training"}],
  aciklama=f"Spor salonu, ıslak kıyafet ve yarış ipuçlarına bak {WB32}.")
a("u4k2", "get enough sleep", "dytablo", soru="Cümleler doğru mu, yanlış mı?", ifadeler=[
  {"s": "Koichi Wakata uzayda her gün en az iki saat egzersiz yaptı.", "d": True},
  {"s": "Uzayda yeterince uyumak çok kolaydır.", "d": False},
  {"s": "Astronotlar stres olunca Dünya manzarasını izleyip rahatlıyor.", "d": True},
  {"s": "Chris Hadfield uzayda maraton koştu.", "d": True}],
  aciklama=f"Uzayda 16 gün doğumu var; uyumak kolay değil {SB48}.")
a("u4k2", "relax", "kisa", soru="Rahatlamak, dinlenmek. İngilizce yaz.", yanit="relax",
  aciklama=f"Rahatlamak: {{{{relax}}}}; zıddı {{{{get stressed}}}} {SB47}.")
a("u4k2", "go jogging", "secim", soru="{{Some astronauts go ___! One astronaut even ran a marathon in space.}}",
  secenekler=["jogging", "training", "relaxing", "sweating"], dogru=0,
  aciklama=f"Koşuya çıkmak: {{{{go jogging}}}} {SB48}.")
a("u4k2", "train", "dy", ifade="Astronotlar uzaya gitmeden önce Dünya'da çok antrenman yapar.", dogru=True,
  aciklama=f"{{{{Astronauts train a lot on Earth.}}}} {SB48}")

# --- Konu 3: Quantifiers
a("u4k3", "too much", "secim", soru="{{There was ___ noise and I couldn't sleep.}}",
  secenekler=["too many", "a few", "too much", "enough of"], dogru=2,
  aciklama=f"{{{{noise}}}} sayılamaz: {{{{too much noise}}}} {WB94}.")
a("u4k3", "a few", "bosluk", havuz=["too", "very"], cumleler=[
  {"c": "This can happen in just a ___ weeks.", "cevap": "few"},
  {"c": "We all need a ___ fun!", "cevap": "little"},
  {"c": "There aren't ___ chairs for everyone.", "cevap": "enough"}],
  aciklama=f"{{{{weeks}}}} sayılabilir, {{{{fun}}}} sayılamaz {SB49}.")
a("u4k3", "too many", "dytablo", soru="Cümleler doğru mu, yanlış mı?", ifadeler=[
  {"s": "{{too many}} sayılabilen isimlerle kullanılır.", "d": True},
  {"s": "{{a little}} sayılabilen isimlerle kullanılır.", "d": False},
  {"s": "{{enough}} sıfattan sonra gelir: {{old enough}}.", "d": True},
  {"s": "{{too}} ile {{very}} aynı anlamdadır.", "d": False}],
  aciklama=f"{{{{a little}}}} sayılamayanla; {{{{too}}}} 'fazla' demek {WB94}.")
a("u4k3", "adjective + enough", "secim", soru="{{Are you ___ to be an astronaut?}}",
  secenekler=["enough old", "old enough", "too enough", "very enough"], dogru=1,
  aciklama=f"Sıfat önce, {{{{enough}}}} sonra {SB49}.")
a("u4k3", "too + adjective", "secim", soru="Miktar cümleleri:", onculler=["{{I'm very happy. Let's celebrate.}}", "{{We need a few luck.}}", "{{The list is too long.}}"],
  kok="Hangileri doğrudur?", secenekler=ONC2, dogru=2,
  aciklama=f"{{{{luck}}}} sayılamaz: {{{{a little luck}}}} {SB49}.")
a("u4k3", "enough + noun", "eslestir", soru="Cümleleri anlamlarıyla eşleştir.", ciftler=[
  {"sol": "There aren't enough chairs.", "sag": "Yeterince sandalye yok."},
  {"sol": "There were too many options.", "sag": "Çok fazla seçenek vardı."},
  {"sol": "I have a little time.", "sag": "Biraz vaktim var."},
  {"sol": "I've got a few messages.", "sag": "Birkaç mesajım var."}],
  aciklama=f"Miktar kalıpları {WB94}.")

SB50, SB51, SB52, SB53, SB54, SB57 = "(SB s. 50)", "(SB s. 51)", "(SB s. 52)", "(SB s. 53)", "(SB s. 54)", "(SB s. 57)"
WB35, WB36, WB37, WB38, WB95 = "(WB s. 35)", "(WB s. 36)", "(WB s. 37)", "(WB s. 38)", "(WB s. 95)"

# --- Konu 4: Healthy eating (9 kelime)
a("u4k4", "carbohydrates", "secim", soru="{{We get most of our energy from these. You find them in bread and pasta.}} Hangisi?",
  secenekler=["vitamins", "fibre", "carbohydrates", "dairy products"], dogru=2,
  aciklama=f"Ekmek ve makarna, enerji: {{{{carbohydrates}}}} {WB35}.")
a("u4k4", "dairy products", "eslestir", soru="Kelimeleri tanımlarıyla eşleştir.", ciftler=[
  {"sol": "dairy products", "sag": "sütten yapılan yiyecekler"},
  {"sol": "fibre", "sag": "yiyeceklerin vücuttan geçmesine yardım eder"},
  {"sol": "protein", "sag": "büyümeye ve güçlü olmaya yardım eder"},
  {"sol": "calories", "sag": "besindeki enerjiyi sayarız"}],
  aciklama=f"Kitaptaki bulmaca ipuçları {WB35}.")
a("u4k4", "vitamins", "bosluk", havuz=["fat", "fibre"], cumleler=[
  {"c": "Ben often seems to get ill. I think he needs more ___.", "cevap": "vitamins"},
  {"c": "You need to eat more ___ if you train a lot.", "cevap": "calories"},
  {"c": "Good ___ is important if you are training for a marathon.", "cevap": "nutrition"}],
  aciklama=f"Hastalık, antrenman ve maraton ipuçlarına bak {SB131}.")
a("u4k4", "fat", "dy", ifade="Peynir ve çikolatada çok lif ({{fibre}}) vardır.", dogru=False,
  duzeltme="Peynir ve çikolatada çok yağ ({{fat}}) vardır.",
  aciklama=f"{{{{There is a lot of this in cheese and chocolate.}}}}: {{{{fat}}}} {WB35}.")
a("u4k4", "protein", "kisa", soru="Vücudun büyümesine ve güçlü olmasına yardım eden besin. Türkçesiyle aynı yazılan İngilizce kelimeyi yaz.", yanit="protein",
  aciklama=f"{{{{Protein helps our bodies to grow and be strong.}}}} {WB38}")
a("u4k4", "a balanced diet", "secim", soru="Beslenme kelimeleri:", onculler=["{{a balanced diet}}: birçok farklı yiyeceğin iyi bir karışımı", "{{nutrition}}: yediğimiz yiyecekler ve vücudun onları kullanması", "{{calories}}: yiyecekteki yağ"],
  kok="Hangileri doğrudur?", secenekler=ONC, dogru=1,
  aciklama=f"{{{{calories}}}} besindeki enerji; yağ {{{{fat}}}} {WB38}.")

# --- Konu 5: should, shouldn't, ought to
a("u4k5", "should", "secim", soru="{{I have a fever.}} Hangisi doğru tavsiye?",
  secenekler=["You should go to school.", "You should to stay in bed.", "You should stay in bed.", "You shoulds stay in bed."], dogru=2,
  aciklama=f"{{{{should}}}} + V1, {{{{to}}}} yok: {{{{You should stay in bed.}}}} {SB51}")
a("u4k5", "ought to", "secim", soru="Cümleler:", onculler=["{{He oughts to eat more protein.}}", "{{We ought to eat lots of fruit.}}", "{{You should worry so much.}}"],
  kok="Hangileri doğru yazılmıştır?", secenekler=ONC2, dogru=1,
  aciklama=f"{{{{ought}}}} değişmez; endişe için {{{{shouldn't worry}}}} {WB36}.")
a("u4k5", "shouldn't", "bosluk", havuz=["oughts"], cumleler=[
  {"c": "You ___ worry about the test – it'll be easy!", "cevap": "shouldn't"},
  {"c": "If you're always late for class, you ___ get up earlier.", "cevap": "should"},
  {"c": "A balanced diet ___ to include some fat.", "cevap": "ought"}],
  aciklama=f"Kolay sınav, geç kalmak ve {{{{to}}}} ipuçlarına bak {WB95}.")
a("u4k5", "Should I …?", "dy", ifade="{{Should I stay at home?}} sorusuna olumlu kısa cevap {{Yes, you should.}} olur.", dogru=True,
  aciklama=f"Kısa cevap: {{{{Yes, you should.}}}} / {{{{No, you shouldn't.}}}} (WB s. 94)")
a("u4k5", "What should …?", "kisa", soru="Boşluğa tek kelime yaz: {{What ___ I do to improve my English?}}", yanit="should",
  aciklama=f"Tavsiye istemek: {{{{What should I do?}}}} {SB51}")
a("u4k5", "should", "dytablo", soru="Rapordaki öneriler doğru mu, yanlış mı?", ifadeler=[
  {"s": "Her dersin ortasında kısa bir ara olmalı.", "d": True},
  {"s": "Kantin daha çok fast food satmalı.", "d": False},
  {"s": "Spor salonu bütün gün açık olmalı.", "d": True},
  {"s": "Bütün sınavlar aynı haftada olmalı.", "d": False}],
  aciklama=f"Fiona ve Sanjay'in önerileri {SB54}.")

# --- Konu 6: Giving advice
a("u4k6", "How about + -ing?", "secim", soru="{{How about ___ jogging? Exercise always works for me!}}",
  secenekler=["go", "going", "to go", "goes"], dogru=1,
  aciklama=f"{{{{How about}}}} + {{{{-ing}}}}: {{{{going}}}} {SB52}.")
a("u4k6", "Why don't you …?", "secim", soru="Hangisi doğru bir öneridir?",
  secenekler=["Why not you look online?", "Why you don't look online?", "Why doesn't you look online?", "Why don't you look online?"], dogru=3,
  aciklama=f"Kalıp: {{{{Why don't you}}}} + V1 {SB53}.")
a("u4k6", "I recommend + -ing", "bosluk", havuz=["try", "sit"], cumleler=[
  {"c": "I can recommend ___ a therapy dog.", "cevap": "trying"},
  {"c": "Have you ever tried ___ with a cat?", "cevap": "sitting"},
  {"c": "Have you tried ___ healthy snacks at home?", "cevap": "making"}],
  aciklama=f"{{{{recommend}}}} ve {{{{tried}}}} + {{{{-ing}}}} {WB37}.")
a("u4k6", "Make sure you …", "dy", ifade="{{Do sure you listen to something gentle.}} doğru bir cümledir.", dogru=False,
  duzeltme="{{Make sure you listen to something gentle.}}",
  aciklama=f"{{{{do sure}}}} değil, {{{{make sure}}}} {SB57}.")
a("u4k6", "Have you tried + -ing?", "eslestir", soru="Günlük ifadeleri anlamlarıyla eşleştir.", ciftler=[
  {"sol": "Seriously?", "sag": "Are you joking?"},
  {"sol": "Tell me about it!", "sag": "I know exactly what you mean."},
  {"sol": "I'll give it a shot.", "sag": "I'm going to try it."},
  {"sol": "... isn't really my thing.", "sag": "I don't really like ..."}],
  aciklama=f"Everyday English kutusu {SB52}.")
a("u4k6", "You could always/just …", "secim", soru="Öneri kalıpları:", onculler=["{{You could always ask your mum.}}", "{{How about going for a walk?}}", "{{Why don't you look online?}}"],
  kok="Hangileri doğru yazılmıştır?", secenekler=ONC, dogru=3,
  aciklama=f"Üçü de doğru öneri kalıbı {SB53}.")

H.yaz()
