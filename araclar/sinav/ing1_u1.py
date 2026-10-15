import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from ortak import Havuz
H = Havuz("ing1", 1, "e1"); a = H.add
K1, K2, K3 = "(s. 10–20)", "(s. 10–26)", "(s. 11–26)"

# --- Konu 1: Appearance
a("u1k1", "tall", "secim", soru="{{What does she look like?}} sorusuna uygun cevap hangisidir?",
  secenekler=["She is tall and slim.", "She is honest.", "She is ten years old.", "She likes music."], dogru=0,
  aciklama=f"{{{{look like}}}} görünüşü sorar: boy, beden, saç {K1}.")
a("u1k1", "curly", "secim", soru="Hangisi saçı anlatan bir kelimedir?",
  secenekler=["generous", "curly", "punctual", "honest"], dogru=1,
  aciklama=f"{{{{curly}}}} kıvırcık demektir; saç için kullanılır {K1}.")
a("u1k1", "blonde", "bosluk", havuz=["is", "eyes"], cumleler=[
  {"c": "She ___ long blonde hair.", "cevap": "has"},
  {"c": "He is old. He has ___ hair.", "cevap": "gray"},
  {"c": "My brother is ___. He is not short.", "cevap": "tall"}],
  aciklama=f"Saç ve göz için {{{{has}}}}. Yaşlı biri gri saçlıdır {K1}.")
a("u1k1", "beautiful", "eslestir", soru="Kelimeleri Türkçe anlamlarıyla eşleştir.", ciftler=[
  {"sol": "slim", "sag": "ince, zayıf"},
  {"sol": "handsome", "sag": "yakışıklı"},
  {"sol": "cute", "sag": "sevimli"},
  {"sol": "young", "sag": "genç"}],
  aciklama=f"{{{{slim}}}} ince, {{{{handsome}}}} yakışıklı, {{{{cute}}}} sevimli, {{{{young}}}} genç {K1}.")
a("u1k1", "young", "kisa", soru="{{young}} kelimesinin zıt anlamlısını İngilizce yaz.", yanit="old",
  aciklama=f"{{{{young}}}} genç, {{{{old}}}} yaşlı {K1}.")
a("u1k1", "slim", "dy", ifade="{{She has blue eyes.}} cümlesinde göz için {{has}} kullanılmıştır.", dogru=True,
  aciklama=f"Özellik için {{{{is}}}}, saç ve göz için {{{{has}}}} {K1}.")

# --- Konu 2: Personality
a("u1k2", "honest", "secim", soru="{{What is he like?}} sorusuna uygun cevap hangisidir?",
  secenekler=["He is tall.", "He has curly hair.", "He is honest and generous.", "He is twelve."], dogru=2,
  aciklama=f"{{{{What is he like?}}}} kişiliği sorar {K2}.")
a("u1k2", "selfish", "secim", soru="{{Caring only about yourself, not others.}} tanımı hangi kelimenindir?",
  secenekler=["generous", "selfish", "punctual", "outgoing"], dogru=1,
  aciklama=f"Yalnız kendini düşünen kişi {{{{selfish}}}}, yani bencildir {K2}.")
a("u1k2", "punctual", "eslestir", soru="Kelimeleri anlamlarıyla eşleştir.", ciftler=[
  {"sol": "punctual", "sag": "dakik"},
  {"sol": "stubborn", "sag": "inatçı"},
  {"sol": "outgoing", "sag": "dışa dönük"},
  {"sol": "easy-going", "sag": "uysal, rahat"}],
  aciklama=f"Kişilik kelimeleri: dakik, inatçı, dışa dönük, uysal {K2}.")
a("u1k2", "stubborn", "dytablo", soru="Olumsuz bir özellikse D, değilse Y seç.", ifadeler=[
  {"s": "stubborn", "d": True},
  {"s": "honest", "d": False},
  {"s": "selfish", "d": True},
  {"s": "generous", "d": False}],
  aciklama=f"{{{{stubborn}}}} ve {{{{selfish}}}} olumsuz özelliklerdir {K2}.")
a("u1k2", "generous", "kisa", soru="{{Willing to give and share.}} tanımı hangi kelimenindir? İngilizce yaz.", yanit="generous",
  aciklama=f"Vermeye ve paylaşmaya istekli kişi {{{{generous}}}}, yani cömerttir {K2}.")
a("u1k2", "honest", "dy", ifade="{{She never tells lies.}} cümlesi dürüst bir kişiyi anlatır.", dogru=True,
  aciklama=f"Hiç yalan söylemeyen kişi {{{{honest}}}}tır {K2}.")

# --- Konu 3: Comparatives
a("u1k3", "taller than", "secim", soru="Dave 182 cm, Nina 162 cm. Hangi cümle doğrudur?",
  secenekler=["Nina is taller than Dave.", "Dave is taller than Nina.", "Dave is shorter than Nina.", "Nina is older than Dave."], dogru=1,
  aciklama=f"182 cm daha uzundur: {{{{Dave is taller than Nina.}}}} {K3}.")
a("u1k3", "better than", "secim", soru="{{good}} kelimesinin karşılaştırma hâli hangisidir?",
  secenekler=["gooder", "more good", "better", "best"], dogru=2,
  aciklama=f"{{{{good}}}} düzensizdir: {{{{better}}}} {K3}.")
a("u1k3", "more outgoing than", "secim", soru="{{Anne is ___ punctual than Jane.}} Boşluğa ne gelir?",
  secenekler=["more", "-er", "most", "than"], dogru=0,
  aciklama=f"Uzun sıfatlarda {{{{more}}}} kullanılır {K3}.")
a("u1k3", "heavier than", "eslestir", soru="Sıfatları karşılaştırma hâlleriyle eşleştir.", ciftler=[
  {"sol": "heavy", "sag": "heavier"},
  {"sol": "slim", "sag": "slimmer"},
  {"sol": "bad", "sag": "worse"},
  {"sol": "young", "sag": "younger"}],
  aciklama=f"{{{{y}}}} → {{{{i}}}}, son harf ikilenir, {{{{bad}}}} düzensizdir {K3}.")
a("u1k3", "younger than", "kisa", soru="{{than}} kelimesinin Türkçe anlamı nedir?", yanit="-den", kabul=["den", "dan", "-dan", "den daha", "dan daha"],
  aciklama=f"{{{{than}}}} = -den, -dan (daha) {K3}.")
a("u1k3", "slimmer than", "dy", ifade="{{slim}} kelimesinin karşılaştırma hâli {{slimer}} olarak yazılır.", dogru=False,
  duzeltme="Son harf ikilenir: slimmer.",
  aciklama=f"Kısa kelime ünlü + ünsüzle bitince son harf ikilenir: {{{{slimmer}}}} {K3}.")
H.yaz()
