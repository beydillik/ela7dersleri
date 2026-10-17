import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from ortak import Havuz, ONC
H = Havuz("din1", 3, "d3"); a = H.add
K1, K2, K3 = "(s. 87–93)", "(s. 94–97)", "(s. 98–99)"
K4, K5, K6 = "(s. 100–105)", "(s. 106–109)", "(s. 110–115)"

# --- Konu 1: Din Anlayışındaki Yorum Farklılıkları
a("u3k1", "Din", "dy", ifade="Din, kişiye ve zamana göre değişir.", dogru=False,
  duzeltme="Din anlayışı değişebilir; dinin temel ilkeleri değişmez.",
  aciklama=f"Dinin temel ilkeleri değişmez; değişebilen din anlayışıdır {K1}.")
a("u3k1", "İnsanın Yapısı", "dytablo", soru="Dinî yorum farklılıklarının sebebi olanlara D, olmayanlara Y seç.", ifadeler=[
  {"s": "İnsanların bilgi birikiminin farklı olması", "d": True},
  {"s": "İslam'ın farklı coğrafyalara yayılması", "d": True},
  {"s": "Bazı ayetlerin farklı şekillerde yorumlanması", "d": True},
  {"s": "Bütün insanların aynı yetenekte yaratılması", "d": False}],
  aciklama=f"İnsanlar farklı özelliklerde yaratılmıştır; bu da yorum farkına yol açar {K1}.")
a("u3k1", "Din Anlayışı", "secim", soru="Din anlayışıyla ilgili aşağıdaki bilgiler verilmiştir.",
  onculler=["İnsanların ilahi mesajı anlama ve yorumlamasıdır.", "Yorum içerdiği için bireyseldir.", "Allah tarafından peygamberler aracılığıyla gönderilir."],
  kok="Bu bilgilerden hangileri doğrudur?", secenekler=ONC, dogru=1,
  aciklama=f"Peygamberlerle gönderilen dindir; din anlayışı insanların yorumudur {K1}.")
a("u3k1", "Yorum Farklılıkları Zenginliktir", "bosluk", havuz=["ayrılık", "mimari"], cumleler=[
  {"c": "İslam'ın iki temel kaynağı Kur'an-ı Kerim ve ___ dir.", "cevap": "sünnet"},
  {"c": "Dinin temel ilkelerine bağlı yorumlar ayrılık değil ___ kabul edilir.", "cevap": "zenginlik"},
  {"c": "Yorum farklılıkları fıkıh, kelam ve ___ gibi ilimlerin doğmasına vesile oldu.", "cevap": "tasavvuf"}],
  aciklama=f"Yorumlar zenginliktir; fıkıh, kelam, tasavvuf gibi ilimler doğdu {K1}.")
a("u3k1", "İnsanın Yapısı", "secim",
  soru="Tıp eğitimi almış bir kişi, insanın yaratılışını anlatan ayetleri mesleki bilgisiyle yorumlar. Bu durum hangi sebebe örnektir?",
  secenekler=["İnsanların farklı özelliklerde yaratılması", "İslam'ın geniş coğrafyalara yayılması",
              "Camilerin farklı mimariyle yapılması", "Hz. Peygamber'e soru sorulması"], dogru=0,
  aciklama=f"Meslek ve bilgi birikimi insanın yapısıyla ilgilidir {K1}.")
a("u3k1", "Din Anlayışı", "kisa",
  soru="İnsanların ilahi mesajı anlama ve yorumlama sürecinde ortaya koydukları görüşlere ne denir?",
  yanit="din anlayışı", kabul=["dinanlayışı", "din anlayisi"],
  aciklama=f"Bu görüşlere din anlayışı denir {K1}.")

# --- Konu 2: İtikadi Yorumlar: Eşarilik ve Matüridilik
a("u3k2", "Yorum Biçimleri", "eslestir", soru="Yorum biçimlerini konularıyla eşleştir.", ciftler=[
  {"sol": "İtikadi yorumlar", "sag": "İnanç"},
  {"sol": "Fıkhi yorumlar", "sag": "İbadet"},
  {"sol": "Tasavvufi yorumlar", "sag": "Ahlak"}],
  aciklama=f"İnanç itikadi, ibadet fıkhi, ahlak tasavvufi yorumların konusudur {K2}.")
a("u3k2", "Matüridilik", "dy", ifade="Matüridilik, inanç esaslarının anlaşılmasında aklın önemli bir yeri olduğunu savunur.", dogru=True,
  aciklama=f"Matüridilik akli delilleri ön planda tutar {K2}.")
a("u3k2", "Eşarilik", "secim", soru="Ebülhasan Eşari ile ilgili hangisi doğrudur?",
  secenekler=["Basra'da doğmuş, Bağdat'ta vefat etmiştir.", "Semerkant'ın Matürit kasabasında doğmuştur.",
              "Fıkhi bir mezhebin kurucusudur.", "Medine halkının uygulamalarını esas almıştır."], dogru=0,
  aciklama=f"İmam Eşari Basra'da doğdu, Bağdat'ta vefat etti; Eşarilik itikadi mezheptir {K2}.")
a("u3k2", "Mezhep", "kisa", soru="Sözlükte \"gidilecek yol, takip edilen yöntem\" anlamına gelen kavram nedir?",
  yanit="mezhep", aciklama=f"Mezhebin sözlük anlamı \"gidilecek yol, yöntem\"dir {K2}.")
a("u3k2", "İtikat", "dytablo", soru="İtikadın konularından olanlara D, olmayanlara Y seç.", ifadeler=[
  {"s": "Meleklere inanmak", "d": True}, {"s": "Kader ve kazaya inanmak", "d": True},
  {"s": "Abdestin nasıl alınacağı", "d": False}, {"s": "Ahirete inanmak", "d": True}],
  aciklama=f"Abdestin alınışı ibadetle ilgilidir; itikadın konusu değildir {K2}.")
a("u3k2", "Yaygın Oldukları Yerler", "secim", soru="Bir itikadi mezheple ilgili şu bilgiler verilmiştir:",
  onculler=["Ebu Mansur Matüridi'nin görüşlerine dayanır.", "Akli delilleri ön planda tutar.", "Orta Asya Türk Cumhuriyetleri'nde yaygındır."],
  kok="Bu bilgiler hangi mezheple ilgilidir?", secenekler=["Eşarilik", "Hanefilik", "Şafiilik", "Matüridilik"], dogru=3,
  aciklama=f"Üç bilgi de Matüridiliğe aittir {K2}.")

# --- Konu 3: Fıkhi Yorumlar: Dört Mezhep
a("u3k3", "Hanefilik", "eslestir", soru="Fıkhi mezhepleri dayandıkları âlimle eşleştir.", ciftler=[
  {"sol": "Hanefilik", "sag": "Ebu Hanife"},
  {"sol": "Malikilik", "sag": "Malik bin Enes"},
  {"sol": "Şafiilik", "sag": "Muhammed bin İdris Şafii"},
  {"sol": "Hanbelilik", "sag": "Ahmed bin Hanbel"}],
  aciklama=f"Her mezhep kurucusunun adıyla anılır {K3}.")
a("u3k3", "Fıkıh", "dytablo", soru="Fıkhi mezhep olanlara D, olmayanlara Y seç.", ifadeler=[
  {"s": "Hanbelilik", "d": True}, {"s": "Matüridilik", "d": False},
  {"s": "Malikilik", "d": True}, {"s": "Eşarilik", "d": False}],
  aciklama=f"Eşarilik ve Matüridilik itikadi mezheplerdir {K3}.")
a("u3k3", "Şafiilik", "secim",
  soru="Mekke, Medine ve Bağdat gibi ilim merkezlerinde eğitim alması görüşlerini etkileyen mezhep imamı kimdir?",
  secenekler=["İmam Şafii", "İmam Malik", "Ebu Hanife", "Ahmed bin Hanbel"], dogru=0,
  aciklama=f"İmam Şafii'nin fıkıh anlayışında bu ilim merkezleri etkilidir {K3}.")
a("u3k3", "Ayrıntıdaki Farklılıklar", "secim", soru="Fıkhi yorumlarla ilgili şu bilgiler verilmiştir:",
  onculler=["Helaller ve haramlar konusunda âlimler hemfikirdir.", "Farz ibadetler konusunda âlimler farklı görüştedir.",
            "Tahiyyatta işaret parmağının kaldırılıp indirilmesi gibi ayrıntılarda farklılık vardır."],
  kok="Bu bilgilerden hangileri doğrudur?", secenekler=["Yalnız I", "II ve III", "I ve III", "I, II ve III"], dogru=2,
  aciklama=f"Farz ibadetlerde âlimler hemfikirdir; farklılık ayrıntılardadır {K3}.")
a("u3k3", "Hanefilik", "kisa", soru="Fıkıhtaki yetkinliği sebebiyle İmam-ı Azam diye tanınan âlim kimdir?",
  yanit="Ebu Hanife", kabul=["ebuhanife", "numan bin sabit"],
  aciklama=f"İmam-ı Azam, Ebu Hanife'dir {K3}.")
a("u3k3", "Hanbelilik", "bosluk", havuz=["Basra", "tefsir"], cumleler=[
  {"c": "Ahmed bin Hanbel hayatının büyük bölümünde ___ ilmiyle uğraştı.", "cevap": "hadis"},
  {"c": "İmam Malik hayatını ___ şehrinde geçirdi.", "cevap": "Medine"},
  {"c": "Ebu Hanife'nin asıl adı ___ bin Sabit'tir.", "cevap": "Numan"}],
  aciklama=f"Hanbel – hadis, Malik – Medine, Ebu Hanife – Numan bin Sabit {K3}.")

# --- Konu 4: Tasavvufi Yorumlar
a("u3k4", "Yesevilik", "eslestir", soru="Tasavvufi yorumları dayandıkları kişiyle eşleştir.", ciftler=[
  {"sol": "Yesevilik", "sag": "Ahmed Yesevi"}, {"sol": "Kadirilik", "sag": "Abdülkadir Geylani"},
  {"sol": "Mevlevilik", "sag": "Mevlana Celaleddin Rumi"}, {"sol": "Nakşibendilik", "sag": "Bahaeddin Nakşibend"},
  {"sol": "Bektaşilik", "sag": "Hacı Bektaş Veli"}],
  aciklama=f"Her tasavvufi yorum kurucusunun adıyla anılır {K4}.")
a("u3k4", "Tasavvufi Yorumların Amaçları", "dytablo", soru="Tasavvufi yorumların amaçlarından olanlara D, olmayanlara Y seç.", ifadeler=[
  {"s": "Allah'a içtenlikle yönelmek", "d": True}, {"s": "Hz. Peygamber'i örnek almak", "d": True},
  {"s": "Zengin ve ünlü olmak", "d": False}, {"s": "İbadet bilinci kazanmak", "d": True}],
  aciklama=f"Zengin ve ünlü olmak tasavvufun amaçlarından değildir {K4}.")
a("u3k4", "Alevilik Bektaşilik", "dy", ifade="Alevilik ile Bektaşilik aynı şeydir.", dogru=False,
  duzeltme="Aynı şey değildir; ama ikisinde de Hz. Ali ve Ehlibeyt sevgisi ön plandadır.",
  aciklama=f"İkisi aynı değildir; ortak noktaları Hz. Ali ve Ehlibeyt sevgisidir {K4}.")
a("u3k4", "Tasavvuf", "secim", soru="Hangisi başlıca tasavvufi yorumlardan biri değildir?",
  secenekler=["Kadirilik", "Nakşibendilik", "Malikilik", "Yesevilik"], dogru=2,
  aciklama=f"Malikilik fıkhi bir yorumdur {K4}.")
a("u3k4", "Mevlevilik", "bosluk", havuz=["Buhara", "Yesi"], cumleler=[
  {"c": "Mevlana bugünkü Afganistan'daki ___ şehrinde doğdu.", "cevap": "Belh"},
  {"c": "Mevlana daha sonra ___ şehrine yerleşti.", "cevap": "Konya"},
  {"c": "Mevlevi dervişlerinin musiki eşliğinde dönerek zikretmesine ___ denir.", "cevap": "sema"}],
  aciklama=f"Mevlana Belh'te doğdu, Konya'ya yerleşti; Mevlevilikte sema öne çıkar {K4}.")
a("u3k4", "Kadirilik", "secim", soru="Bir tasavvufi yorumla ilgili şu bilgiler verilmiştir:",
  onculler=["Abdülkadir Geylani'nin görüşlerine dayanır.", "Kurucusu Bağdat'ta ilim öğrenmiştir.", "Irak başta olmak üzere hemen her yerde kabul görmüştür."],
  kok="Bu bilgiler hangi tasavvufi yorumla ilgilidir?", secenekler=["Yesevilik", "Kadirilik", "Mevlevilik", "Nakşibendilik"], dogru=1,
  aciklama=f"Üç bilgi de Kadiriliğe aittir {K4}.")
a("u3k4", "Yesevilik", "kisa", soru="Ahmed Yesevi'nin tasavvufu sade bir dille anlattığı şiirlere ne ad verilir?",
  yanit="hikmet", kabul=["hikmetler"], aciklama=f"Bu şiirlere hikmet denir {K4}.")

# --- Konu 5: Kültürümüzdeki Tasavvufi Yorumlar
a("u3k5", "Tasavvufi Eserler", "eslestir", soru="Eserleri yazarlarıyla eşleştir.", ciftler=[
  {"sol": "Mesnevi", "sag": "Mevlana"}, {"sol": "Divan-ı Hikmet", "sag": "Ahmed Yesevi"},
  {"sol": "Makalat", "sag": "Hacı Bektaş Veli"}, {"sol": "Fütûhu'l-Gayb", "sag": "Abdülkadir Geylani"}],
  aciklama=f"Bu eserler tasavvufi düşünceleri aktaran en bilinen eserlerdendir {K5}.")
a("u3k5", "Mevlana'nın Yedi Öğüdü", "eslestir", soru="Mevlana'nın öğütlerini benzetmeleriyle eşleştir.", ciftler=[
  {"sol": "Cömertlik ve yardımda", "sag": "Akarsu gibi ol"}, {"sol": "Şefkat ve merhamette", "sag": "Güneş gibi ol"},
  {"sol": "Kusur örtmede", "sag": "Gece gibi ol"}, {"sol": "Alçak gönüllülükte", "sag": "Toprak gibi ol"},
  {"sol": "Hoşgörüde", "sag": "Deniz gibi ol"}],
  aciklama=f"Mevlana güzel ahlakı doğadan benzetmelerle anlatır {K5}.")
a("u3k5", "Sosyal Yardımlaşma", "dy", ifade="Tekke ve dergâhlarda yalnızca Müslümanlara yemek verilmiştir.", dogru=False,
  duzeltme="Müslüman olsun ya da olmasın ihtiyaç sahibi herkes yemek ve barınma bulmuştur.",
  aciklama=f"İhtiyaç sahibi herkes, Müslüman olsun olmasın, yardım bulmuştur {K5}.")
a("u3k5", "Mevlana Haftası ve Şebiarus", "secim", soru="Mevlana Haftası hangi tarihler arasında düzenlenir?",
  secenekler=["1–7 Ocak", "7–17 Aralık", "10–20 Mart", "23–30 Nisan"], dogru=1,
  aciklama=f"Mevlana Haftası her yıl 7–17 Aralık arasındadır {K5}.")
a("u3k5", "Sema, Semah ve Zikir", "bosluk", havuz=["telbiye", "vakfe"], cumleler=[
  {"c": "Mevlevilikte ___ öne çıkar.", "cevap": "sema"},
  {"c": "Alevilik Bektaşilikte ___ öne çıkar.", "cevap": "semah"},
  {"c": "Kadirilik ve Nakşibendilikte ___ öne çıkar.", "cevap": "zikir"}],
  aciklama=f"Sema Mevlevilikte, semah Alevilik Bektaşilikte, zikir Kadirilik ve Nakşibendilikte {K5}.")
a("u3k5", "Mutasavvıf", "kisa", soru="İslam'ın ahlaki değerlerini öne çıkaran, ahlaklı bireyler yetiştirmeye çalışan kimseye ne denir?",
  yanit="mutasavvıf", kabul=["mutasavvif", "mutasavvıflar"], aciklama=f"Böyle kimseye mutasavvıf denir {K5}.")
a("u3k5", "Tekke, Zaviye ve Dergâh", "dytablo", soru="Tekke, zaviye ve dergâhla ilgili doğrulara D, yanlışlara Y seç.", ifadeler=[
  {"s": "Ahlak ve adap kuralları öğretilir.", "d": True},
  {"s": "Aynı tasavvufi görüşü benimseyenler bir araya gelir.", "d": True},
  {"s": "Zaviye büyük bir saray demektir.", "d": False}],
  aciklama=f"Zaviye \"küçük tekke\" demektir {K5}.")

# --- Konu 6: Alevilik Bektaşilik
a("u3k6", "Görgü Cemi", "eslestir", soru="Cem çeşitlerini amaçlarıyla eşleştir.", ciftler=[
  {"sol": "Görgü cemi", "sag": "Bir yılın muhasebesi yapılır"},
  {"sol": "İkrar cemi", "sag": "Yola girdiğini sözlü olarak ifade eder"},
  {"sol": "Abdal Musa cemi", "sag": "Dargınlar barıştırılır"}],
  aciklama=f"Üç cemin amacı farklıdır: muhasebe, yola giriş, barışma {K6}.")
a("u3k6", "Cem ve Cemevi", "eslestir", soru="Kavramları tanımlarıyla eşleştir.", ciftler=[
  {"sol": "Cemevi", "sag": "Ayinicemlerin yapıldığı yer"}, {"sol": "Erkân", "sag": "Cemin usulü ve kuralları"},
  {"sol": "Musahiplik", "sag": "Yol kardeşliği"}, {"sol": "Gülbank", "sag": "Bismişah ile başlayan dua"},
  {"sol": "Dede", "sag": "Erkânları yöneten önder"}],
  aciklama=f"Bu kavramlar Alevilik Bektaşiliğin temel kavramlarıdır {K6}.")
a("u3k6", "Abdal Musa Cemi", "dy", ifade="Abdal Musa ceminde kişiyi yola alma amacı vardır.", dogru=False,
  duzeltme="Abdal Musa ceminde yola alınma ya da görgü amacı yoktur; amaç barıştırmaktır.",
  aciklama=f"Abdal Musa cemi dargınları barıştırmak için yapılır {K6}.")
a("u3k6", "Gülbank", "secim", soru="Gülbankle ilgili şu bilgiler verilmiştir:",
  onculler=["\"Bismişah\" sözüyle başlar.", "\"Hû, Allah Allah\" ifadeleriyle biter.", "Yalnızca cenazelerde okunur."],
  kok="Bu bilgilerden hangileri doğrudur?", secenekler=ONC, dogru=1,
  aciklama=f"Gülbank ikrar, ad koyma, sofra gibi pek çok durumda okunur {K6}.")
a("u3k6", "Erkân ve On İki Hizmet", "kisa", soru="Cem erkânında On iki imam'a nispetle yapılan görevlerin genel adı nedir?",
  yanit="on iki hizmet", kabul=["oniki hizmet", "12 hizmet"], aciklama=f"Bu görevlere on iki hizmet denir {K6}.")
a("u3k6", "Dede ve Ocak", "bosluk", havuz=["rehber", "yolculuk"], cumleler=[
  {"c": "Ocakların başında ___ bulunur.", "cevap": "dede"},
  {"c": "Musahiplik, Hz. Peygamber'in ensar ve ___ kardeş ilan etmesine dayanır.", "cevap": "muhaciri"},
  {"c": "Cem sözlükte bir araya gelmek, ___ anlamına gelir.", "cevap": "toplanmak"}],
  aciklama=f"Ocağın başında dede vardır; musahiplik ensar-muhacir kardeşliğine dayanır {K6}.")
a("u3k6", "İkrar Cemi", "secim",
  soru="Ali, Alevilik Bektaşilik yoluna girdiğini dede ve topluluk önünde sözlü olarak ifade edecek. Hangi cem düzenlenir?",
  secenekler=["Görgü cemi", "Abdal Musa cemi", "İkrar cemi", "Şebiarus töreni"], dogru=2,
  aciklama=f"Yola girdiğini sözlü olarak ifade etmek için ikrar cemi yapılır {K6}.")

H.yaz()
