import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from ortak import Havuz, ONC
H = Havuz("sos1", 2, "s2"); a = H.add
K1, K2, K3, K4, K5 = "(s. 58–62)", "(s. 62–67)", "(s. 68–71)", "(s. 72–74)", "(s. 74–79)"

# --- Konu 1: Küreselleşme: ekonomi, ulaşım, iletişim
a("u2k1", "Küreselleşme", "kisa", soru="Dünyanın ekonomik, kültürel ve siyasi olarak birbirine daha bağlı hâle gelmesi sürecine ne denir?", yanit="küreselleşme",
  aciklama=f"Dünya birbirine bağlanıyor: küreselleşme {K1}.")
a("u2k1", "Uluslararası Şirketler ve Yerel İşletmeler", "secim", soru="Aşağıdakilerden hangisi küreselleşmenin ekonomide getirdiği sorunlardan biridir?",
  secenekler=["Küçük yerel işletmelerin zor durumda kalması", "Ürünlere ulaşmanın kolaylaşması", "Ticaretin dünya çapında yapılması", "Ulaşımın hızlanması"], dogru=0,
  aciklama=f"Büyük şirketler büyüdü, küçük yerel işletmeler zorlandı {K1}.")
a("u2k1", "Orta Koridor", "secim", soru="Çin'den başlayıp Kazakistan, Hazar Denizi, Azerbaycan ve Gürcistan üzerinden Türkiye'ye ve Avrupa'ya uzanan yol hangisidir?",
  secenekler=["İpek Yolu", "Orta Koridor", "Kral Yolu", "Baharat Yolu"], dogru=1,
  aciklama=f"Bu ulaşım yolu Orta Koridor'dur {K1}.")
a("u2k1", "E-Ticaret", "dy", ifade="E-ticaret sayesinde evden çıkmadan başka ülkelerle alışveriş yapılabilir.", dogru=True,
  aciklama=f"E-ticaretle evden dünyaya alışveriş yapılır {K1}.")
a("u2k1", "Hızlı Ulaşım", "secim", soru="Sanayi İnkılabı'ndan sonra ulaşımın hızlanması hangisine yol açmıştır?",
  secenekler=["Turizm seyahatlerinin azalmasına", "İş ve turizm amaçlı seyahatlerin artmasına", "Toplumların birbirinden uzaklaşmasına", "Ticaretin ülke içinde kalmasına"], dogru=1,
  aciklama=f"Kolay ve hızlı yolculuk iş ve turizm seyahatlerini artırdı {K1}.")

# --- Konu 2: Kültür, sağlık ve çevre
a("u2k2", "Sağlıkta Küreselleşme", "secim", soru="Küreselleşmenin sağlık üzerindeki etkileriyle ilgili aşağıdaki ifadeler verilmiştir.",
  onculler=["Teşhis ve tedavi kolaylaştı.", "Hastalıkların yayılması hızlandı.", "Sağlık sorunları yalnızca tek bir ülkeyi etkiler oldu."],
  kok="Bu ifadelerden hangileri doğrudur?", secenekler=ONC, dogru=1,
  aciklama=f"Sağlık sorunları artık tüm dünyayı etkiliyor. Örnek: COVID-19 {K2}.")
a("u2k2", "Dilde Bozulma", "dy", ifade="Ana dile başka dillerden çok fazla sözcük girmesi dilin bozulmasına yol açabilir.", dogru=True,
  aciklama=f"Dilimize sahip çıkmalıyız {K2}.")
a("u2k2", "Yerelden Evrensele", "secim", soru="Küresel çevre sorunlarını azaltmak için bireyin yapabileceği en temel şey hangisidir?",
  secenekler=["İhtiyacından fazla alışveriş yapmak", "Bilinçli tüketmek ve israfı önlemek", "Sorunu yalnızca devlete bırakmak", "Daha çok araba kullanmak"], dogru=1,
  aciklama=f"Değişim önce bireyden başlar: bilinçli tüketim, israfı önlemek {K2}.")
a("u2k2", "Küresel Çevre Sorunları", "dytablo", soru="Küresel çevre sorunu olanlara D, olmayanlara Y seç.", ifadeler=[
  {"s": "İklim krizi", "d": True},
  {"s": "Ormansızlaşma", "d": True},
  {"s": "E-ticaret", "d": False},
  {"s": "Su kirliliği", "d": True}],
  aciklama=f"Çevre sorunları yerelden küresele dönüştü. E-ticaret bir alışveriş biçimidir {K2}.")
a("u2k2", "Kültür Yolu Festivalleri", "secim", soru="Geleneksel el sanatlarımızın ve millî musikimizin dijital sergi ve konserlerle tanıtıldığı etkinlik hangisidir?",
  secenekler=["Kültür Yolu Festivalleri", "Orta Koridor", "İyilik Gemileri", "Yeşil Dönüşüm"], dogru=0,
  aciklama=f"Kültür Yolu Festivalleri değerlerimizi modern yollarla yaşatır {K2}.")

# --- Konu 3: Komşularımız ve Türk dünyası
a("u2k3", "Kara Sınırı Komşularımız", "kisa", soru="Türkiye'nin karadan kaç komşusu vardır?", yanit="8", kabul=["sekiz"], sayi=True,
  aciklama=f"Bulgaristan, Yunanistan, Gürcistan, Ermenistan, Azerbaycan, İran, Irak, Suriye: 8 {K3}.")
a("u2k3", "Kara Sınırı Komşularımız", "secim", soru="Aşağıdakilerden hangisi Türkiye'nin kara sınırı komşularından biri değildir?",
  secenekler=["Gürcistan", "İran", "Mısır", "Bulgaristan"], dogru=2,
  aciklama=f"Mısır'la kara sınırımız yoktur {K3}.")
a("u2k3", "Türk Dünyasıyla İş Birliği", "secim", soru="Türk Devletleri Teşkilatı toplantılarında kabul edilen Ortak Türk Alfabesi kaç harften oluşur?",
  secenekler=["29", "34", "28", "40"], dogru=1,
  aciklama=f"Ortak Türk Alfabesi 34 harftir {K3}.")
a("u2k3", "Yurtta Sulh, Cihanda Sulh", "dy", ifade="“Yurtta sulh, cihanda sulh.” sözündeki “sulh” kelimesi “savaş” demektir.", dogru=False,
  duzeltme="“Sulh” barış demektir: yurtta barış, dünyada barış.",
  aciklama=f"Sulh barıştır {K3}.")
a("u2k3", "Yurt Dışı Yardımlar", "eslestir", soru="Türkiye'nin yardımlarını yapıldığı yerlerle eşleştir.", ciftler=[
  {"sol": "Kuzey Makedonya", "sag": "Maarif okulu"},
  {"sol": "Kolombiya", "sag": "Mobil kütüphane"},
  {"sol": "Somali", "sag": "Eğitim ve araştırma hastanesi"}],
  aciklama=f"Türkiye eğitim, kültür ve sağlıkta yardım yapar {K3}.")

# --- Konu 4: Barış, savaş, göç, mülteciler
a("u2k4", "Ara Buluculuk", "secim", soru="Anlaşmazlık yaşayan taraflar arasında sorunun çözümüne yardımcı olmaya ne denir?",
  secenekler=["Göç", "Ara buluculuk", "Küreselleşme", "E-ticaret"], dogru=1,
  aciklama=f"Ara bulucu, iki tarafı buluşturan köprüdür {K4}.")
a("u2k4", "Mülteciler", "secim", soru="Savaş, çatışma veya baskı nedeniyle ülkesini terk etmek zorunda kalan insanlara ne denir?",
  secenekler=["Turist", "Mülteci", "Komşu", "Yerli"], dogru=1,
  aciklama=f"Ülkesini zorunlu olarak terk eden insanlar mültecidir {K4}.")
a("u2k4", "Göç", "dy", ifade="Göçün nedenleri yalnızca ekonomik sorunlardır.", dogru=False,
  duzeltme="Göçün nedenleri güvenlik ya da ekonomik sorunlar olabilir.",
  aciklama=f"İnsanlar güvenlik için de daha iyi yaşam için de göç eder {K4}.")
a("u2k4", "Barış", "bosluk", havuz=["göç", "e-ticaret"], cumleler=[
  {"c": "Saygı, güven ve anlayış içinde çatışmadan yaşamaya ___ denir.", "cevap": "barış"},
  {"c": "Can ve mal güvenliğini tehdit eden, yıkıma yol açan olaylara ___ denir.", "cevap": "savaş"},
  {"c": "Krizlerde sığınanlara kucak açan Türkiye, güvenli bir ___ olarak görülür.", "cevap": "liman"}],
  aciklama=f"Savaş yıkar, barış korur. Türkiye güvenli bir limandır {K4}.")
a("u2k4", "Göçmenlerin Uyumu", "secim", soru="Göç eden insanların yeni yerlerine uyumu için hangisi önemlidir?",
  secenekler=["Toplumun onları anlayışla karşılaması", "Onlarla hiç konuşmamak", "Eğitimden uzak tutulmaları", "Yalnız yaşamaları"], dogru=0,
  aciklama=f"Göçmen uyum sağlamalı, toplum da anlayışla karşılamalıdır {K4}.")

# --- Konu 5: İklim krizi ve insani yardım
a("u2k5", "İklim Krizi", "secim", soru="Küresel iklim krizinin temel nedeni hangisidir?",
  secenekler=["Atmosfere fazla sera gazı salınması", "Ağaç dikilmesi", "Bisiklet kullanımının artması", "Geri dönüşüm"], dogru=0,
  aciklama=f"Fosil yakıt, orman kesimi ve sanayi fazla sera gazı salınımına yol açar {K5}.")
a("u2k5", "Ortak Sorumluluk", "kisa", soru="Türkiye'nin Sıfır Emisyon Hedefi hangi yıl içindir?", yanit="2053", sayi=True,
  aciklama=f"Hedef: 2053 Sıfır Emisyon {K5}.")
a("u2k5", "Yardım Kurumları", "secim", soru="Aşağıdakilerden hangisi Türkiye'nin yardımlarını ulaştıran kurumlardan biri değildir?",
  secenekler=["AFAD", "TİKA", "Türk Kızılay", "Orta Koridor"], dogru=3,
  aciklama=f"Yardımlar TİKA, AFAD ve Türk Kızılay ile ulaştırılır. Orta Koridor bir ulaşım yoludur {K5}.")
a("u2k5", "İyilik Gemileri", "dy", ifade="Türk Kızılay, İyilik Gemileri ile Gazze'ye insani yardım ulaştırmaktadır.", dogru=True,
  aciklama=f"İyilik Gemileri Gazze'ye gıda, su ve barınma malzemesi taşır {K5}.")
a("u2k5", "Empati", "secim", soru="Yardım etme isteğini güçlendiren en temel duygu hangisidir?",
  secenekler=["Kıskançlık", "Empati", "Öfke", "Korku"], dogru=1,
  aciklama=f"Karşındakinin hissettiğini anlamak, yani empati, bizi yardıma yöneltir {K5}.")
H.yaz()
