import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from ortak import Havuz, ONC
H = Havuz("din1", 1, "d1"); a = H.add
K1, K2, K3 = "(s. 14–17)", "(s. 18–21)", "(s. 22–25)"

# --- Konu 1: Varlıklar Âlemi
a("u1k1", "Âlem", "kisa", soru="Allah'ın yarattığı bütün varlıklara ne ad verilir?", yanit="âlem", kabul=["alem"],
  aciklama=f"Yaratılan her şeye âlem denir {K1}.")
a("u1k1", "Görülebilen Varlıklar", "dytablo", soru="Gözle ya da araçla görülebilenlere D, görülemeyenlere Y seç.", ifadeler=[
  {"s": "Dağ", "d": True}, {"s": "Melek", "d": False}, {"s": "Mikrop (mikroskopla)", "d": True}, {"s": "Merhamet", "d": False}],
  aciklama=f"Dağ ve mikrop görülebilir; melek ve merhamet görülemez {K1}.")
a("u1k1", "Gayb", "dy", ifade="Gaybı yalnızca Allah bilir.", dogru=True,
  aciklama=f"Kur'an'a göre gaybı yalnızca Allah bilir {K1}.")
a("u1k1", "Cin", "dy", ifade="Cinlerin hiçbir sorumluluğu yoktur.", dogru=False,
  duzeltme="Cinler de insanlar gibi Allah'ın emirlerinden sorumludur.",
  aciklama=f"Cinler de kulluk için yaratılmıştır, sorumludur {K1}.")
a("u1k1", "Şeytan", "secim", soru="Şeytanla ilgili aşağıdaki bilgiler verilmiştir.",
  onculler=["Cinlerdendir.", "Hz. Âdem için saygıyla eğilmedi.", "Nurdan yaratılmıştır."],
  kok="Bu bilgilerden hangileri doğrudur?", secenekler=ONC, dogru=1,
  aciklama=f"Şeytan cinlerdendir ve emre karşı geldi; nurdan yaratılanlar meleklerdir {K1}.")
a("u1k1", "Melek", "bosluk", havuz=["topraktan", "insanlar"], cumleler=[
  {"c": "Melekler ___ yaratılmıştır.", "cevap": "nurdan"},
  {"c": "Görülemeyen varlıklar Kur'an'da ___ kavramıyla anlatılır.", "cevap": "gayb"},
  {"c": "Akıl, sevgi ve ___ gözle görülmez ama vardır.", "cevap": "merhamet"}],
  aciklama=f"Melek nurdandır; görülmeyenler gaybdır {K1}.")

# --- Konu 2: Melekler
a("u1k2", "Cebrail", "eslestir", soru="Melekleri görevleriyle eşleştir.", ciftler=[
  {"sol": "Cebrail", "sag": "Peygamberlere vahiy getirir"},
  {"sol": "Azrail", "sag": "Ölüm vakti gelenin canını alır"},
  {"sol": "Mikâil", "sag": "Yağmur ve rızıkla görevlidir"},
  {"sol": "İsrafil", "sag": "Sûra iki kez üfler"}],
  aciklama=f"Dört büyük meleğin her birinin ayrı görevi var {K2}.")
a("u1k2", "Meleklerin Özellikleri", "secim", soru="Aşağıdakilerden hangisi meleklerin özelliklerinden biri değildir?",
  secenekler=["Nurdan yaratılmışlardır", "Yeme ve uyuma ihtiyaçları vardır", "Farklı şekillere girebilirler", "Sayılarını yalnızca Allah bilir"], dogru=1,
  aciklama=f"Meleklerin yeme, içme, uyuma ihtiyaçları yoktur {K2}.")
a("u1k2", "Kiramen Kâtibin", "kisa", soru="İnsanın sevap ve günahlarını yazan \"değerli yazıcılar\" hangi meleklerdir?", yanit="Kiramen Kâtibin",
  kabul=["kiramen katibin", "kiramenkatibin", "yazıcı melekler"],
  aciklama=f"Sağımızda ve solumuzdaki yazıcı melekler Kiramen Kâtibin'dir {K2}.")
a("u1k2", "Münker ve Nekir", "dy", ifade="Münker ve Nekir, sorgu melekleri olarak bilinir.", dogru=True,
  aciklama=f"Münker ve Nekir insanları sorguya çeker {K2}.")
a("u1k2", "İsrafil", "dy", ifade="Mikâil, sûra üflemekle görevli melektir.", dogru=False,
  duzeltme="Sûra üflemekle görevli melek İsrafil'dir.",
  aciklama=f"Sûra İsrafil üfler; Mikâil yağmur ve rızıkla görevlidir {K2}.")
a("u1k2", "Azrail", "secim", soru="\"Sizin için görevlendirilen ölüm meleği canınızı alacak…\" (Secde suresi 11. ayet) Ayette sözü edilen melek hangisidir?",
  secenekler=["Cebrail", "Mikâil", "İsrafil", "Azrail"], dogru=3,
  aciklama=f"Ölüm meleği Azrail'dir; Melekülmevt diye de anılır {K2}.")

# --- Konu 3: Dünya Hayatı ve Ahiret
a("u1k3", "Ahiret", "secim", soru="Dünya hayatı sona erince başlayan ve sonsuza kadar süren hayata ne denir?",
  secenekler=["Ömür", "Ecel", "Ahiret", "Âlem"], dogru=2,
  aciklama=f"Ahiret, dünya hayatından sonra başlayan sonsuz hayattır {K3}.")
a("u1k3", "Ömür", "eslestir", soru="Kavramları anlamlarıyla eşleştir.", ciftler=[
  {"sol": "Ömür", "sag": "Doğumdan ölüme kadar geçen süre"},
  {"sol": "Ecel", "sag": "Ölüm için belirlenen zaman"},
  {"sol": "Amel defteri", "sag": "Yaptıklarımızın yazıldığı defter"}],
  aciklama=f"Ömür yaşam süresi, ecel ölüm vaktidir {K3}.")
a("u1k3", "Ahirete İman", "dy", ifade="Ahirete inanmak, İslam'ın inanç esaslarındandır.", dogru=True,
  aciklama=f"Ahirete iman inanç esaslarındandır {K3}.")
a("u1k3", "Ecel", "kisa", soru="Ölüm için belirlenen ve takdir edilen zamana ne denir?", yanit="ecel",
  aciklama=f"Ölüm vaktinin gelmesine ecel denir {K3}.")
a("u1k3", "Hayatın Amacı", "secim", soru="Hayat ve ölümle ilgili aşağıdaki bilgiler verilmiştir.",
  onculler=["Allah her şeyi bir amaçla yaratmıştır.", "İnsan için hayat bu dünyadan ibarettir.", "Allah, kimin daha güzel amel yapacağını sınar."],
  kok="Kitaba göre bu bilgilerden hangileri doğrudur?", secenekler=["Yalnız I", "I ve II", "I ve III", "I, II ve III"], dogru=2,
  aciklama=f"Hayat dünyadan ibaret değildir; dünyadan sonra ahiret vardır {K3}.")
a("u1k3", "Amel Defteri", "bosluk", havuz=["mizan", "ömür"], cumleler=[
  {"c": "İnsanın dünyada yaptığı her şey ___ defterine yazılır.", "cevap": "amel"},
  {"c": "Ahiret sözlükte \"son, sonra olan, son ___\" demektir.", "cevap": "gün"},
  {"c": "Hz. Âdem'den itibaren bütün ___ ahireti haber vermiştir.", "cevap": "peygamberler"}],
  aciklama=f"Yaptıklarımız amel defterine yazılır; ahireti bütün peygamberler bildirdi {K3}.")

H.yaz()
