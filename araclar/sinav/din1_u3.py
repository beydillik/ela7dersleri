import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from ortak import Havuz, ONC
H = Havuz("din1", 3, "d3"); a = H.add
K1, K2, K3 = "(s. 87–93)", "(s. 94–97)", "(s. 98–99)"

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

H.yaz()
