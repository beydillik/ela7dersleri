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

H.yaz()
