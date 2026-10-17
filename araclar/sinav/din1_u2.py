import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from ortak import Havuz, ONC
H = Havuz("din1", 2, "d2"); a = H.add
K1, K2, K3 = "(s. 49–52)", "(s. 53–56)", "(s. 51, 56–60)"

# --- Konu 1: Hac İbadeti: Şartları ve Kavramları
a("u2k1", "Tavaf", "kisa", soru="Kâbe'nin etrafında yedi kez dönmeye ne denir?", yanit="tavaf",
  aciklama=f"Kâbe'nin etrafında yedi tur dönmek tavaftır {K1}.")
a("u2k1", "Haccın Şartları", "dytablo", soru="Haccın şartlarından olanlara D, olmayanlara Y seç.", ifadeler=[
  {"s": "Sağlıklı olmak", "d": True}, {"s": "Yol güvenliğine sahip olmak", "d": True},
  {"s": "Hafız olmak", "d": False}, {"s": "Belirli ekonomik güce sahip olmak", "d": True}],
  aciklama=f"Hac, gitmeye gücü yetene farzdır; hafız olmak şart değildir {K1}.")
a("u2k1", "Hac", "dy", ifade="Hac yalnızca bedenle yapılan bir ibadettir.", dogru=False,
  duzeltme="Hac hem mal hem bedenle yapılır.",
  aciklama=f"Hac hem mal hem bedenle yapılan bir ibadettir {K1}.")
a("u2k1", "Vakfe", "eslestir", soru="Kavramları anlamlarıyla eşleştir.", ciftler=[
  {"sol": "Tavaf", "sag": "Kâbe'nin etrafında yedi kez dönmek"},
  {"sol": "Say", "sag": "Safa ile Merve arasında yedi kez gidip gelmek"},
  {"sol": "Vakfe", "sag": "Arafat'ta bir süre durup beklemek"},
  {"sol": "Telbiye", "sag": "\"Lebbeyk\" diye başlayan dua"}],
  aciklama=f"Hacda her görevin kendi adı var {K1}.")
a("u2k1", "İhram", "secim", soru="İhramla ilgili aşağıdaki bilgiler verilmiştir.",
  onculler=["Erkeklerin giydiği dikişsiz, beyaz örtüye de ihram denir.", "İhrama girilen sınırlara mikat denir.", "İhramlıyken parfüm kullanılabilir."],
  kok="Bu bilgilerden hangileri doğrudur?", secenekler=ONC, dogru=1,
  aciklama=f"İhramlıyken parfüm, kolonya gibi ürünler kullanılmaz {K1}.")
a("u2k1", "Tavaf", "bosluk", havuz=["Merve", "mikat"], cumleler=[
  {"c": "Kâbe'nin etrafında bir tur dönmeye ___ denir.", "cevap": "şavt"},
  {"c": "Tavafa ___ selamlanarak başlanır.", "cevap": "Hacerülesved"},
  {"c": "Say ___ Tepesi'nde başlar.", "cevap": "Safa"}],
  aciklama=f"Bir tur şavttır; tavaf Hacerülesved'de, say Safa'da başlar {K1}.")

# --- Konu 2: Haccın Yapılışı: Farzları ve Vacipleri
a("u2k2", "Müzdelife", "secim", soru="Hacda aşağıdaki görevlerden hangisi doğru sırayla verilmiştir?",
  secenekler=["İhram – Arafat vakfesi – Müzdelife vakfesi – şeytan taşlama",
              "Arafat vakfesi – ihram – şeytan taşlama – Müzdelife vakfesi",
              "Şeytan taşlama – ihram – Müzdelife vakfesi – Arafat vakfesi",
              "Müzdelife vakfesi – Arafat vakfesi – ihram – şeytan taşlama"], dogru=0,
  aciklama=f"İhramla başlanır; Arafat'tan Müzdelife'ye, sonra Mina'ya geçilir {K2}.")
a("u2k2", "Haccın Farzları", "dytablo", soru="Haccın farzı olanlara D, farzı olmayanlara Y seç.", ifadeler=[
  {"s": "İhrama girmek", "d": True}, {"s": "Şeytan taşlamak", "d": False},
  {"s": "Arafat'ta vakfe yapmak", "d": True}, {"s": "Veda tavafı yapmak", "d": False}],
  aciklama=f"Farzlar: ihram, Arafat vakfesi, tavaf; şeytan taşlama ve veda tavafı vaciptir {K2}.")
a("u2k2", "Mina", "eslestir", soru="Yerleri, orada yapılan görevle eşleştir.", ciftler=[
  {"sol": "Arafat", "sag": "Farz olan vakfe"},
  {"sol": "Müzdelife", "sag": "Taş toplama ve vacip vakfe"},
  {"sol": "Mina", "sag": "Şeytan taşlama ve kurban kesimi"},
  {"sol": "Safa ve Merve", "sag": "Say"}],
  aciklama=f"Her yerin kendine ait bir görevi var {K2}.")
a("u2k2", "Müzdelife", "kisa", soru="Hacı adaylarının Arafat'tan sonra geçip taş topladıkları yer neresidir?", yanit="Müzdelife",
  aciklama=f"Arafat'tan sonra Müzdelife'ye geçilir, taş toplanır {K2}.")
a("u2k2", "Kâbe", "dy", ifade="Veda tavafı, Mekke'den ayrılmadan önce yapılır.", dogru=True,
  aciklama=f"Hacdaki son görev veda tavafıdır {K2}.")
a("u2k2", "Haccın Vacipleri", "secim", soru="Hacda yapılan bazı görevler şunlardır:",
  onculler=["Kâbe'yi tavaf etmek", "Say yapmak", "Saçları tıraş etmek veya kısaltmak"],
  kok="Bunlardan hangileri haccın vaciplerindendir?", secenekler=ONC, dogru=2,
  aciklama=f"Tavaf farzdır; say ve tıraş vaciptir {K2}.")

# --- Konu 3: Haccın Kazandırdıkları ve Umre
a("u2k3", "Hac ile Umre", "secim", soru="Aşağıdakilerden hangisi umrede yapılmaz?",
  secenekler=["İhrama girmek", "Kâbe'yi tavaf etmek", "Say yapmak", "Arafat'ta vakfe yapmak"], dogru=3,
  aciklama=f"Arafat vakfesi yalnızca hacda vardır {K3}.")
a("u2k3", "Hac ile Umre", "dy", ifade="Umre yalnızca hac günlerinde yapılabilir.", dogru=False,
  duzeltme="Umre, hac günleri dışında yılın her zamanı yapılabilir.",
  aciklama=f"Umrenin hac gibi belirli bir vakti yoktur {K3}.")
a("u2k3", "Umre", "kisa", soru="İmkânı olan her Müslüman için umre yapmanın hükmü nedir?", yanit="sünnet",
  aciklama=f"Umre yapmak sünnettir {K3}.")
a("u2k3", "Ahlaki Gelişim", "eslestir", soru="Hacdaki görevi, hatırlattığı değerle eşleştir.", ciftler=[
  {"sol": "İhram", "sag": "Kimsenin kimseden üstün olmadığı"},
  {"sol": "Arafat vakfesi", "sag": "Sabırlı olmak"},
  {"sol": "Şeytan taşlama", "sag": "Kötü huylardan uzak durmak"},
  {"sol": "Say", "sag": "Zorluklarla mücadele etmek"}],
  aciklama=f"Hacdaki görevler insana güzel ahlak kazandırır {K3}.")
a("u2k3", "Umrenin Yapılışı", "bosluk", havuz=["vakfe", "kurban"], cumleler=[
  {"c": "Umre için önce ___ girilir.", "cevap": "ihrama"},
  {"c": "Kâbe'de umre ___ yapılır.", "cevap": "tavafı"},
  {"c": "Saçlar tıraş edilerek ya da kısaltılarak ___ çıkılır.", "cevap": "ihramdan"}],
  aciklama=f"Umre: ihram, tavaf, say, tıraş {K3}.")
a("u2k3", "Birlik ve Kardeşlik", "secim",
  metin=["Tavafta farklı ülkelerden gelen, farklı diller konuşan binlerce Müslüman yan yana yürüyordu.",
         "Hepsi aynı duaları ediyordu."],
  soru="Bu gözleme göre hac hakkında hangisi söylenebilir?",
  secenekler=["Müslümanlar arasında kardeşlik bağını güçlendirir", "Yalnızca bir ülkenin insanlarına aittir",
              "İnsanları birbirinden uzaklaştırır", "Sadece bedensel bir yolculuktur"], dogru=0,
  aciklama=f"Hac, farklı yerlerden Müslümanları kardeş gibi bir araya getirir {K3}.")
a("u2k3", "Haccın Manevi Yönü", "dy", ifade="Hac, insanın Allah'a bağlılığını artırır ve kalbini temizler.", dogru=True,
  aciklama=f"Hac insanı manevi yönden geliştiren bir ibadettir {K3}.")

H.yaz()
