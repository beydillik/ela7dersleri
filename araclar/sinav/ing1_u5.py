import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from ortak import Havuz
H = Havuz("ing1", 5, "e5"); a = H.add

# --- Konu 1: TV Programı Türleri
a("u5k1", "commercial", "secim", soru="{{Companies try to sell their products by introducing them in very short films.}} Bu hangi programdır?",
  secenekler=["documentary", "commercial", "reality show", "news"], dogru=1,
  aciklama="Ürünü kısa filmle tanıtan program reklamdır: {{commercial}} (s. 87).")
a("u5k1", "sitcom", "secim", soru="{{A sitcom is short for situational comedy.}} Paragrafa göre {{sitcom}} hangisidir?",
  secenekler=["A serious TV show with dramatic themes.", "A reality show featuring real people.", "A program discussing current events.", "A humorous show about characters in funny situations."], dogru=3,
  aciklama="{{sitcom}} komik durumlardaki karakterleri anlatan bir programdır (s. 97).")
a("u5k1", "news", "eslestir", soru="Programları Türkçe anlamlarıyla eşleştir.", ciftler=[
  {"sol": "news", "sag": "haberler"},
  {"sol": "documentary", "sag": "belgesel"},
  {"sol": "soap opera", "sag": "pembe dizi"},
  {"sol": "quiz show", "sag": "bilgi yarışması"},
  {"sol": "commercial", "sag": "reklam"}],
  aciklama="Programların adları kitabın 82. sayfasında (s. 82).")
a("u5k1", "reality show", "dytablo", soru="Kitaptaki tanımlara göre D ya da Y seç.", ifadeler=[
  {"s": "In a reality show, you can follow the lives of real people.", "d": True},
  {"s": "The news informs people about the latest events.", "d": True},
  {"s": "You can watch soap operas only at night.", "d": False}],
  aciklama="Pembe diziler gündüz yayınlanır: {{You can watch it daytime.}} (s. 87).")
a("u5k1", "quiz show", "bosluk", havuz=["commercials", "remote control"], cumleler=[
  {"c": "I could answer only five questions out of ten. It was a difficult ___.", "cevap": "quiz show"},
  {"c": "It's really good to watch a ___ because they are educative.", "cevap": "documentary"},
  {"c": "I like ___. They are funny and enjoyable.", "cevap": "sitcoms"}],
  aciklama="Soru cevaplanır {{quiz show}}, öğretir {{documentary}}, güldürür {{sitcoms}} (s. 87).")
a("u5k1", "soap opera", "dy", ifade="{{It is usually melodramatic.}} cümlesi pembe diziyi ({{soap opera}}) anlatır.", dogru=True,
  aciklama="Pembe diziler gündüz yayınlanır ve çok duygusaldır (s. 87).")
a("u5k1", "documentary", "kisa", soru="Belgesel kelimesinin İngilizcesini yaz.", yanit="documentary",
  aciklama="Belgesel {{documentary}}: gerçek konuları anlatır, öğretir (s. 87).")

# --- Konu 2: Tercih Belirtme
a("u5k2", "prefer", "secim", soru="{{Jim: I prefer quiz shows. They make me think and test my knowledge.}} Hangisi doğrudur?",
  secenekler=["Jim enjoys watching talk shows.", "Jim enjoys quiz shows.", "Jim never watches quiz shows.", "Jim prefers soap operas."], dogru=1,
  aciklama="Jim bilgi yarışmalarını tercih ediyor (s. 97).")
a("u5k2", "prefer … to …", "secim", soru="{{Mike: I like quiz shows because they keep me engaged. Lisa: I prefer soap operas.}} Hangisi doğrudur?",
  secenekler=["Mike prefers quiz shows to soap operas.", "Mike prefers soap operas to quiz shows.", "Lisa prefers quiz shows to soap operas.", "Lisa never watches TV."], dogru=0,
  aciklama="Mike bilgi yarışmasını, Lisa pembe diziyi seviyor (s. 97).")
a("u5k2", "Which programmes do you prefer watching?", "secim", soru="{{Nora: ___? Jane: I like documentaries and quiz shows.}} Nora ne sordu?",
  secenekler=["Where is the remote control", "Which programmes do you prefer watching", "What did you do last night", "How are you"], dogru=1,
  aciklama="Jane tercihini söylüyor; soru tercih soruyor (s. 85).")
a("u5k2", "boring", "eslestir", soru="Sıfatları Türkçe anlamlarıyla eşleştir.", ciftler=[
  {"sol": "boring", "sag": "sıkıcı"},
  {"sol": "amusing", "sag": "eğlenceli"},
  {"sol": "educational", "sag": "eğitici"},
  {"sol": "interesting", "sag": "ilginç"}],
  aciklama="Program hakkında görüş bildiren sıfatlar (s. 84, s. 85).")
a("u5k2", "prefer", "dy", ifade="{{I prefer watch the news.}} cümlesi doğru yazılmıştır.", dogru=False,
  duzeltme="Doğrusu: {{I prefer watching the news.}}",
  aciklama="{{prefer}}'dan sonra fiil {{-ing}} alır (s. 83, s. 90).")
a("u5k2", "amusing", "bosluk", havuz=["silly", "remote"], cumleler=[
  {"c": "I like documentaries and quiz shows. They are ___.", "cevap": "educational"},
  {"c": "I find them boring. I prefer ___ programmes.", "cevap": "amusing"},
  {"c": "I never watch soap operas. They are ___.", "cevap": "boring"}],
  aciklama="Eğitici {{educational}}, eğlenceli {{amusing}}, sıkıcı {{boring}} (s. 84, s. 85).")
a("u5k2", "favourite", "kisa", soru="Boşluğa gelen kelimeyi yaz: {{My ___ TV programme is the news.}} (En sevdiğim TV programı haberler.)", yanit="favourite", kabul=["favorite"],
  aciklama="En sevdiğim: {{favourite}} (s. 84).")

H.yaz()
