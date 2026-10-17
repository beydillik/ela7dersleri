import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from ortak import Havuz, ONC
H = Havuz("din1", 2, "d2"); a = H.add
K1, K2, K3 = "(s. 49–52)", "(s. 53–56)", "(s. 51, 56–60)"
K4, K5, K6 = "(s. 61–67)", "(s. 68–74)", "(s. 75–79)"

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

# --- Konu 4: Kurban İbadeti
a("u2k4", "Kurban", "kisa", soru="Kurban ibadetinin hükmü nedir?", yanit="vacip",
  aciklama=f"Kurban, mal ile yapılan vacip bir ibadettir {K4}.")
a("u2k4", "Kurbanlık Hayvanlar", "dytablo", soru="Kurban edilebilecek hayvanlara D, edilemeyenlere Y seç.", ifadeler=[
  {"s": "Deve", "d": True}, {"s": "Manda", "d": True}, {"s": "Tavuk", "d": False}, {"s": "Keçi", "d": True}],
  aciklama=f"Koyun, keçi, sığır, manda ve deve kurban edilebilir {K4}.")
a("u2k4", "Kurbanlık Hayvanlar", "eslestir", soru="Hayvanı, doldurması gereken yaşla eşleştir.", ciftler=[
  {"sol": "Koyun", "sag": "1 yaş"}, {"sol": "Sığır", "sag": "2 yaş"}, {"sol": "Deve", "sag": "5 yaş"}],
  aciklama=f"Koyun ve keçi 1, sığır ve manda 2, deve 5 yaş {K4}.")
a("u2k4", "Etin Paylaşımı", "dy", ifade="Kurban kesen kişi kurbanının etinden hiç yiyemez.", dogru=False,
  duzeltme="Kendisi de yiyebilir, ailesine de yedirebilir.",
  aciklama=f"Et üçe bölünür; bir kısmı aile içinde yenir {K4}.")
a("u2k4", "Kurban Kesmenin Şartları", "secim", soru="Kurbanla ilgili bazı durumlar şunlardır:",
  onculler=["Müslüman olmak", "Yolculuk hâlinde olmak", "Maddi durumu yeterli olmak"],
  kok="Bunlardan hangileri kurban kesmekle yükümlü olmanın şartlarındandır?",
  secenekler=["Yalnız I", "I ve III", "II ve III", "I, II ve III"], dogru=1,
  aciklama=f"Mukim olmak, yani yolculukta olmamak şarttır {K4}.")
a("u2k4", "Kurban", "bosluk", havuz=["Musa", "süt"], cumleler=[
  {"c": "Kurban, Zilhicce ayının 10, 11 ve ___. günlerinde kesilir.", "cevap": "12"},
  {"c": "Kurban ibadeti Hz. ___ ile oğlunun teslimiyetine dayanır.", "cevap": "İbrahim"},
  {"c": "Kurban tığlamada kesimden önce hayvana tuz ve ___ verilir.", "cevap": "su"}],
  aciklama=f"Zilhicce 10–12; Hz. İbrahim; tuz ve su {K4}.")

# --- Konu 5: Hac ve Kurbanın Kültürümüze Yansımaları
a("u2k5", "Adak Kurbanı", "eslestir", soru="Kurban çeşidini, kesiliş nedeniyle eşleştir.", ciftler=[
  {"sol": "Akika kurbanı", "sag": "Yeni doğan çocuk için"},
  {"sol": "Adak kurbanı", "sag": "Bir dileğin gerçekleşmesi için"},
  {"sol": "Şükür kurbanı", "sag": "Allah'a şükretmek için"}],
  aciklama=f"Her kurban çeşidinin kesiliş nedeni farklıdır {K5}.")
a("u2k5", "Akika Kurbanı", "dytablo", soru="Doğru olanlara D, yanlış olanlara Y seç.", ifadeler=[
  {"s": "Akika kurbanı sünnettir.", "d": True}, {"s": "Adak kurbanı müstehaptır.", "d": False},
  {"s": "Şükür kurbanının etinden herkes yiyebilir.", "d": True}, {"s": "Adak sahibi kendi adak kurbanından yiyebilir.", "d": False}],
  aciklama=f"Akika sünnet, adak vacip, şükür müstehap; adak sahibi ve ailesi yiyemez {K5}.")
a("u2k5", "Hacı Uğurlama ve Hacı Kapısı", "kisa", soru="Hacca gidenin evinin boyanıp süslenen dış kapısına ne ad verilir?",
  yanit="hacı kapısı", kabul=["haci kapisi", "hacı kapı"],
  aciklama=f"Bu geleneğe hacı kapısı denir {K5}.")
a("u2k5", "Teşrik Tekbiri", "secim", soru="Teşrik tekbiri getirmeye ne zaman başlanır?",
  secenekler=["Arife Günü sabah namazından sonra", "Bayramın ilk günü ikindi namazından sonra",
              "Bayramın dördüncü günü sabah namazından sonra", "Ramazan ayının son günü"], dogru=0,
  aciklama=f"Arife Günü sabahı başlar, bayramın 4. günü ikindisinde biter {K5}.")
a("u2k5", "Bayramlaşma", "dy", ifade="Bayram namazını yalnızca erkekler kılabilir.", dogru=False,
  duzeltme="Erkekler için vaciptir; kadınlar ve çocuklar da kılabilir.",
  aciklama=f"Bayram namazını kadınlar ve çocuklar da kılabilir {K5}.")
a("u2k5", "Hacı Ziyareti", "secim",
  metin=["– Hacdan ne getirdin?", "– Birlik ve beraberlik bilinci, sabır ve hoşgörü getirdim.", "– Bir de tadımlık zemzem ve hurma getirdim."],
  soru="Bu konuşmaya göre hac, kişiye en çok ne kazandırmıştır?",
  secenekler=["Yalnızca hediyeler", "Çok para", "Sabır ve hoşgörü gibi değerler", "Yeni bir meslek"], dogru=2,
  aciklama=f"Hacı, hacdan değerler getirdiğini söyler; zemzem ve hurma tadımlıktır {K5}.")

# --- Konu 6: Kâfirun Suresi
a("u2k6", "1–3. Ayetler", "eslestir", soru="Ayetlerin okunuşunu anlamıyla eşleştir. (3. ve 5. ayet aynıdır.)", ciftler=[
  {"sol": "Ḳul yâ eyyühel kâfirûn", "sag": "De ki: \"Ey Kâfirler!\""},
  {"sol": "Lâ a'büdü mâ ta'büdûn", "sag": "Ben sizin kulluk ettiklerinize kulluk etmem."},
  {"sol": "Velâ entüm âbidûne mâ a'büd", "sag": "Siz de benim kulluk ettiğime kulluk edecek değilsiniz."},
  {"sol": "Velâ ene âbidümmâ abettüm", "sag": "Ben sizin kulluk ettiklerinize kulluk edecek değilim."},
  {"sol": "Leküm dînüküm veliye dîn", "sag": "Sizin dininiz size, benim dinim de banadır."}],
  aciklama=f"Kâfirun suresinin okunuşu ve anlamı ayet ayet {K6}.")
a("u2k6", "1–3. Ayetler", "secim", soru="Kâfirun suresinin ilk üç ayeti hangi seçenekte doğru sırada verilmiştir?",
  secenekler=["Ḳul yâ eyyühel kâfirûn → Lâ a'büdü mâ ta'büdûn → Velâ entüm âbidûne mâ a'büd",
              "Lâ a'büdü mâ ta'büdûn → Ḳul yâ eyyühel kâfirûn → Velâ entüm âbidûne mâ a'büd",
              "Velâ entüm âbidûne mâ a'büd → Lâ a'büdü mâ ta'büdûn → Ḳul yâ eyyühel kâfirûn",
              "Ḳul yâ eyyühel kâfirûn → Leküm dînüküm veliye dîn → Lâ a'büdü mâ ta'büdûn"], dogru=0,
  aciklama=f"Sure \"Ḳul\" ile başlar; \"Leküm dînüküm\" son ayettir {K6}.")
a("u2k6", "Kâfir", "dy", ifade="Kâfir, Allah'ı tek ve eşsiz kabul eden kişi demektir.", dogru=False,
  duzeltme="Kâfir, Allah'ı tek ve eşsiz kabul etmeyen kişi demektir.",
  aciklama=f"Kâfir, Allah'ın varlığını ve birliğini inkâr edendir {K6}.")
a("u2k6", "Okunduğu Zamanlar", "kisa", soru="Kâfirun suresi namazlarda hangi sureden sonra okunur?",
  yanit="Fatiha", kabul=["fatiha suresi", "fatihadan"],
  aciklama=f"Namazlarda Fatiha suresinden sonra okunur {K6}.")
a("u2k6", "Surenin İnişi", "secim", soru="Kâfirun suresiyle ilgili şu bilgiler verilmiştir:",
  onculler=["Müşriklerin teklifini reddetmek için indirilmiştir.", "Tevhitten taviz verilmeyeceğini vurgular.", "Haccın nasıl yapılacağını anlatır."],
  kok="Bu bilgilerden hangileri doğrudur?", secenekler=ONC, dogru=1,
  aciklama=f"Surede hac anlatılmaz; teklif reddedilir ve tevhit vurgulanır {K6}.")
a("u2k6", "Tevhit", "bosluk", havuz=["yedi", "şavt"], cumleler=[
  {"c": "Allah'ın birliğine inanmaya ___ denir.", "cevap": "tevhit"},
  {"c": "Kâfirun suresi ___ ayettir.", "cevap": "altı"},
  {"c": "Sure, Mekkeli ___ teklifini reddetmek için indi.", "cevap": "müşriklerin"}],
  aciklama=f"Tevhit; altı ayet; müşriklerin teklifi {K6}.")

H.yaz()
