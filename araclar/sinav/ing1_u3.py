import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from ortak import Havuz
H = Havuz("ing1", 3, "e3"); a = H.add

# --- Konu 1: Doğumdan Okula
a("u3k1", "be born", "secim", soru="{{Amanda Key was ___ in Madrid.}} Boşluğa hangisi gelir?",
  secenekler=["moved", "born", "graduated", "grew up"], dogru=1,
  aciklama="{{was born}} doğdu: Madrid'de doğdu (s. 61).")
a("u3k1", "graduate", "secim", soru="{{To receive a diploma}} tanımı hangi kelimenin?",
  secenekler=["move", "stay", "graduate", "grow up"], dogru=2,
  aciklama="Diploma almak mezun olmaktır: {{graduate}} (s. 55).")
a("u3k1", "grow up", "dytablo", soru="Emma'nın hayatına göre D ya da Y seç.", ifadeler=[
  {"s": "Emma was born in Italy.", "d": True},
  {"s": "Emma grew up in England.", "d": False},
  {"s": "Emma moved to England to attend a university.", "d": True}],
  aciklama="Emma İtalya'da doğdu ve orada büyüdü, üniversite için İngiltere'ye taşındı (s. 57).")
a("u3k1", "move", "eslestir", soru="Kelimeleri Türkçe anlamlarıyla eşleştir.", ciftler=[
  {"sol": "be born", "sag": "doğmak"},
  {"sol": "grow up", "sag": "büyümek"},
  {"sol": "move", "sag": "taşınmak"},
  {"sol": "graduate", "sag": "mezun olmak"}],
  aciklama="{{be born}} doğmak, {{grow up}} büyümek, {{move}} taşınmak, {{graduate}} mezun olmak (s. 46).")
a("u3k1", "study", "bosluk", havuz=["died", "raised"], cumleler=[
  {"c": "Bill was ___ in 1986.", "cevap": "born"},
  {"c": "He ___ up in Liverpool.", "cevap": "grew"},
  {"c": "He ___ chemistry at university.", "cevap": "studied"}],
  aciklama="Bill 1986'da doğdu ({{born}}), Liverpool'da büyüdü ({{grew}}), kimya okudu ({{studied}}) (s. 56).")
a("u3k1", "move", "kisa", soru="{{move}} fiilinin geçmiş hâlini yaz. ({{We ___ to Manchester in 1954.}})", yanit="moved",
  aciklama="{{move}} → {{moved}}: 1954'te taşındılar (s. 52).")
a("u3k1", "stay", "dy", ifade="{{He left school and stayed at home most of the time.}} cümlesine göre Edison çoğu zaman evde kaldı.", dogru=True,
  aciklama="{{stayed at home}} evde kaldı demektir (s. 51).")

# --- Konu 2: Aile ve Kariyer
a("u3k2", "get married", "secim", soru="{{Marcy and Robert ___ in a beautiful ceremony in Los Angeles last week.}}",
  secenekler=["got married", "graduated", "raised two kids", "died"], dogru=0,
  aciklama="Güzel bir törenle evlendiler: {{got married}} (s. 61).")
a("u3k2", "award", "secim", soru="{{Jessica Milton is a brilliant musician. She's got five music ___ so far.}}",
  secenekler=["careers", "awards", "biographies", "children"], dogru=1,
  aciklama="Başarılı müzisyen ödül kazanır: {{awards}} (s. 62).")
a("u3k2", "raise", "eslestir", soru="Kelimeleri Türkçe anlamlarıyla eşleştir.", ciftler=[
  {"sol": "get engaged", "sag": "nişanlanmak"},
  {"sol": "get married", "sag": "evlenmek"},
  {"sol": "raise", "sag": "çocuk yetiştirmek"},
  {"sol": "career", "sag": "kariyer"},
  {"sol": "award", "sag": "ödül"}],
  aciklama="Kelime listesi ve tanımlar kitabın 46. ve 55. sayfalarında (s. 46, s. 55).")
a("u3k2", "die", "dy", ifade="{{He died in 2010 at the age of 72.}} cümlesine göre Oliver 2010'da doğdu.", dogru=False,
  duzeltme="Oliver 2010'da öldü; {{died}} öldü demektir.",
  aciklama="{{died}} öldü demektir; Oliver 1938'de doğdu (s. 59).")
a("u3k2", "raise", "bosluk", havuz=["moved", "born"], cumleler=[
  {"c": "Jack ___ three children alone.", "cevap": "raised"},
  {"c": "They got ___ and had a son.", "cevap": "married"},
  {"c": "He ___ in 1938.", "cevap": "died"}],
  aciklama="Yetiştirdi {{raised}}, evlendiler {{got married}}, öldü {{died}} (s. 46, s. 54, s. 59).")
a("u3k2", "career", "kisa", soru="Kariyer kelimesinin İngilizcesini yaz.", yanit="career",
  aciklama="Kariyer {{career}}: {{an excellent career in photography}} (s. 46).")
a("u3k2", "award", "dytablo", soru="Oliver Bennett'in biyografisine göre D ya da Y seç.", ifadeler=[
  {"s": "Oliver was born in Manchester.", "d": True},
  {"s": "Oliver met his wife at a music festival.", "d": True},
  {"s": "Oliver never won an award.", "d": False}],
  aciklama="Manchester'da doğdu, eşiyle festivalde tanıştı ve birkaç müzik ödülü kazandı (s. 59).")

# --- Konu 3: Geçmişi Sorma ve Tarihler
B, W, Y, D, O, A = ("When / Where were you born?", "When did you …?", "Why did you …?", "Did you …?", "in / on + tarih", "at the age of")
a("u3k3", W, "secim", soru="{{Kevin: ___ did you get married? Tom: I met my wife in 2014, and we got married in the same year.}}",
  secenekler=["Why", "Where", "When", "Who"], dogru=2,
  aciklama="Cevap bir yıl: zaman soran {{When}} gelir (s. 57).")
a("u3k3", Y, "secim", soru="{{David: ___? Mr Williams: To find a better job in here.}} David hangi soruyu sordu?",
  secenekler=["When were you born", "Why did you move to New York", "Where were you born", "Did you get married"], dogru=1,
  aciklama="Cevap bir sebep söylüyor; sebebi {{Why}} sorar (s. 61).")
a("u3k3", O, "bosluk", havuz=["by", "to"], cumleler=[
  {"c": "Louis Braille was born ___ 1809.", "cevap": "in"},
  {"c": "Mehmed II died ___ 3rd May, 1481.", "cevap": "on"},
  {"c": "He died in 2010 ___ the age of 72.", "cevap": "at"}],
  aciklama="Yıl {{in}}, gün ve ay {{on}}, yaş {{at the age of}} (s. 49, s. 59).")
a("u3k3", B, "eslestir", soru="Soruları cevaplarıyla eşleştir.", ciftler=[
  {"sol": "When were you born?", "sag": "In 1946."},
  {"sol": "Where were you born?", "sag": "In Phoenix, Arizona."},
  {"sol": "Why did you move to New York?", "sag": "Because I wanted to make music."},
  {"sol": "Did you always live in Manchester?", "sag": "No. I was born in Birmingham."}],
  aciklama="{{When}} zaman, {{Where}} yer, {{Why}} sebep, {{Did}} evet/hayır sorar (s. 52, s. 57, s. 61).")
a("u3k3", B, "dy", ifade="{{When did you born?}} doğru yazılmış bir sorudur.", dogru=False,
  duzeltme="Doğru soru: {{When were you born?}}",
  aciklama="Doğum {{were}} ile sorulur: {{When were you born?}} (s. 52).")
a("u3k3", A, "kisa", soru="Boşluğa gelen kelimeyi yaz: {{He died at the ___ of 72.}}", yanit="age",
  aciklama="Kalıp {{at the age of}}: … yaşında (s. 59).")
a("u3k3", W, "dytablo", soru="Time to Quiz yarışmasına göre D ya da Y seç.", ifadeler=[
  {"s": "Newton was born in 1642.", "d": True},
  {"s": "Gutenberg invented the printing machine in 1447.", "d": True},
  {"s": "Marie Curie discovered Radium first.", "d": False}],
  aciklama="Marie Curie önce polonyumu keşfetti; diğer iki cevap doğru sayıldı (s. 50).")

H.yaz()
