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

K4, K5, K6 = "(s. 26–31)", "(s. 32–36)", "(s. 37–41)"

# --- Konu 4: Ahiret Hayatının Aşamaları
a("u1k4", "Ölüm", "secim", soru="Ahiret hayatının aşamaları hangi seçenekte doğru sıralanmıştır?",
  secenekler=["Kıyamet – ölüm – mahşer – baas – mizan – cennet/cehennem",
              "Ölüm – baas – kıyamet – mizan – mahşer – cennet/cehennem",
              "Ölüm – kıyamet – baas – mahşer – mizan – cennet/cehennem",
              "Baas – ölüm – kıyamet – mahşer – cennet/cehennem – mizan"], dogru=2,
  aciklama=f"Önce ölüm, sonra kıyamet ve diriliş; en son hesap ve cennet/cehennem {K4}.")
a("u1k4", "Kıyamet", "dy", ifade="Cebrail'in sûra üflemesiyle kıyamet kopacaktır.", dogru=False,
  duzeltme="Sûra üflemekle görevli melek İsrafil'dir.",
  aciklama=f"Kıyamet, İsrafil sûra üfleyince kopar {K4}.")
a("u1k4", "Baas", "eslestir", soru="Kavramları anlamlarıyla eşleştir.", ciftler=[
  {"sol": "Baas", "sag": "Ölümden sonra yeniden diriliş"},
  {"sol": "Mahşer", "sag": "Hesap için toplanılan yer"},
  {"sol": "Mizan", "sag": "Sevap ve günahların tartıldığı terazi"},
  {"sol": "Berzah", "sag": "Kabir hayatı"}],
  aciklama=f"Her aşamanın kendi adı var; sırayı da hatırla {K4}.")
a("u1k4", "Mizan", "kisa", soru="Sevap ve günahların tartılacağı manevi adalet terazisine ne denir?", yanit="mizan",
  aciklama=f"Manevi adalet terazisine mizan denir {K4}.")
a("u1k4", "Cennet", "bosluk", havuz=["mahşer", "ceza"], cumleler=[
  {"c": "Cennet, inanıp salih amel işleyenlerin ___ yeridir.", "cevap": "mükâfat"},
  {"c": "Kıyametin ne zaman kopacağını yalnızca ___ bilir.", "cevap": "Allah"},
  {"c": "Ölümle kabir hayatı, yani ___ başlar.", "cevap": "berzah"}],
  aciklama=f"Cennet mükâfat yeridir; kıyametin vaktini yalnızca Allah bilir {K4}.")
a("u1k4", "Cehennem", "secim", soru="Allah'ın adaletiyle ilgili aşağıdaki bilgiler verilmiştir.",
  onculler=["İyiliği kat kat ödüllendirir.", "Kötülüğe hak ettiğinden fazla ceza verir.", "Günah işleyene tövbe için fırsat tanır."],
  kok="Kitaba göre bu bilgilerden hangileri doğrudur?", secenekler=["Yalnız I", "I ve II", "I ve III", "I, II ve III"], dogru=2,
  aciklama=f"Allah kötülüğe yalnızca misliyle karşılık verir; tövbe için fırsat tanır {K4}.")

# --- Konu 5: Melek ve Ahiret İnancının İnsana Kazandırdıkları
a("u1k5", "İyiliğe Yönelmek", "dytablo", soru="Melek ve ahiret inancı olan birinden beklenen davranışlara D, beklenmeyenlere Y seç.", ifadeler=[
  {"s": "Yalan söylemekten kaçınır.", "d": True}, {"s": "Komşusunu rahatsız eder.", "d": False},
  {"s": "Zorluklara sabreder.", "d": True}, {"s": "Haksızlık yapar.", "d": False}],
  aciklama=f"Bu inanç doğruluk, sabır ve iyiliğe yöneltir {K5}.")
a("u1k5", "Manevi Güç", "secim", soru="Meleklerin dua ettiğine ve desteklediğine inanan insan için hangisi söylenebilir?",
  secenekler=["Manevi olarak güçlü olur", "Kimseye güvenmez", "Sorumluluktan kaçar", "Hep yalnız hisseder"], dogru=0,
  aciklama=f"Meleklerin desteğine inanmak insanı manevi olarak güçlendirir {K5}.")
a("u1k5", "Sabır", "eslestir", soru="İnancı, insana kazandırdığıyla eşleştir.", ciftler=[
  {"sol": "Yaptıklarım yazılıyor", "sag": "Kötülükten kaçınmak"},
  {"sol": "Dünya imtihan yeridir", "sag": "Sabretmek"},
  {"sol": "Hayat ölümle bitmez", "sag": "Huzur bulmak"},
  {"sol": "Hesap vereceğim", "sag": "Sorumlu davranmak"}],
  aciklama=f"Her inanç insana güzel bir özellik kazandırır {K5}.")
a("u1k5", "Sabır", "kisa", soru="Ahirete inanan insan dünyayı nasıl bir yer olarak görür? (iki kelime)", yanit="imtihan yeri",
  kabul=["imtihan", "sınav yeri", "imtihan yeridir"],
  aciklama=f"Ahirete inanan dünyanın bir imtihan yeri olduğunu bilir {K5}.")
a("u1k5", "Hayata Anlam", "dy", ifade="Ahiret inancı, insanın hayatını anlamlandırmasına yardım eder.", dogru=True,
  aciklama=f"Ahirete inanmak hayatı anlamlandırır {K5}.")
a("u1k5", "İnanç ve Davranış", "secim", soru="Hadiste, Allah'a ve ahiret gününe iman eden kişiden aşağıdakilerden hangisi istenmemiştir?",
  secenekler=["Misafirine ikram etmesi", "Komşusunu rahatsız etmemesi", "Ya hayır söylemesi ya da susması", "Komşusuyla tartışması"], dogru=3,
  aciklama=f"Hadiste ikram, komşuyu rahatsız etmemek ve güzel söz öğütlenir {K5}.")

# --- Konu 6: Nâs Suresi
a("u1k6", "İlk Üç Ayet", "eslestir", soru="Ayet numarasını okunuşuyla eşleştir.", ciftler=[
  {"sol": "1. ayet", "sag": "Ḳul eûẕü birabbinnâs"},
  {"sol": "3. ayet", "sag": "İlâhinnâs"},
  {"sol": "4. ayet", "sag": "Min şerril vesvâsil ḫannâs"},
  {"sol": "6. ayet", "sag": "Minel cinneti vennâs"}],
  aciklama=f"Sıra: Rab, Melik, İlah; sonra vesveseci, kalpler, cin ve insan {K6}.")
a("u1k6", "Son Üç Ayet", "secim", soru="Nâs suresinin okunuşunda 4. ayetten sonra hangisi gelir?",
  secenekler=["Melikinnâs", "Elleẕî yüvesvisü fî sudûrinnâs", "İlâhinnâs", "Ḳul eûẕü birabbinnâs"], dogru=1,
  aciklama=f"4. ayetten sonra 5. ayet \"Elleẕî yüvesvisü fî sudûrinnâs\" gelir {K6}.")
a("u1k6", "Muavvizeteyn", "dy", ifade="Felak ve Nâs surelerine birlikte Muavvizeteyn denir.", dogru=True,
  aciklama=f"Muavvizeteyn, Felak ve Nâs'ın ortak adıdır {K6}.")
a("u1k6", "Nâs Suresi", "kisa", soru="\"Nâs\" kelimesinin anlamı nedir?", yanit="insanlar", kabul=["insan"],
  aciklama=f"Nâs \"insanlar\" demektir {K6}.")
a("u1k6", "Okunduğu Zamanlar", "bosluk", havuz=["yemekten", "ellerine"], cumleler=[
  {"c": "Hz. Peygamber Felak ve Nâs'ı her gün ___ önce okurdu.", "cevap": "yatmadan"},
  {"c": "Bu iki surenin her ___ sonra okunmasını tavsiye etmiştir.", "cevap": "namazdan"},
  {"c": "Surede, insanların ___ vesvese veren vesvesecinin kötülüğünden Allah'a sığınılır.", "cevap": "kalplerine"}],
  aciklama=f"Yatmadan önce ve namazdan sonra okunur; vesvese kalbe verilir {K6}.")
a("u1k6", "Allah'a Sığınmak", "secim", soru="Nâs suresiyle ilgili aşağıdaki bilgiler verilmiştir.",
  onculler=["Namazlarda okunan kısa surelerdendir.", "Adını \"nâs\" kelimesinden alır.", "Surede meleklere sığınılır."],
  kok="Bu bilgilerden hangileri doğrudur?", secenekler=ONC, dogru=1,
  aciklama=f"Surede meleklere değil, insanların Rabbi olan Allah'a sığınılır {K6}.")

H.yaz()
