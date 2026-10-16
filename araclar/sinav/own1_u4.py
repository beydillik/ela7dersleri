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

H.yaz()
