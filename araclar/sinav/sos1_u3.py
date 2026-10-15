import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from ortak import Havuz, ONC
H = Havuz("sos1", 3, "s3"); a = H.add
K1, K2, K3, K4, K5, K6, K7, K8, K9, K10, K11, K12 = ("(s. 86–93)", "(s. 93–95)", "(s. 96–102)", "(s. 103–109)", "(s. 110–116)", "(s. 116–121)",
  "(s. 121–124)", "(s. 125–127)", "(s. 128–135)", "(s. 136–141)", "(s. 142–145)", "(s. 145–152)")

# --- Konu 1: Kuruluş ve büyüme
a("u3k1", "Orhan Bey ve I. Murad Dönemleri", "secim", soru="Osmanlı başkentleri hangi sırayla değişmiştir?",
  secenekler=["İstanbul → Bursa → Edirne", "Bursa → Edirne → İstanbul", "Edirne → Bursa → İstanbul", "Bursa → İstanbul → Edirne"], dogru=1,
  aciklama=f"Önce Bursa (Orhan Bey), sonra Edirne (I. Murad), sonra İstanbul (Fatih) {K1}.")
a("u3k1", "Osmanlı Beyliği'nin Kuruluşu", "secim", soru="Osmanlı Beyliği nerede kurulmuştur?",
  secenekler=["Söğüt ve çevresinde", "Konya'da", "Edirne'de", "Kahire'de"], dogru=0,
  aciklama=f"Osman Bey Dönemi'nde Söğüt ve çevresinde kuruldu {K1}.")
a("u3k1", "Malazgirt ve Türk Beylikleri", "kisa", soru="Anadolu'da Türk beyliklerinin kurulmasının yolunu açan Malazgirt Savaşı hangi yıl yapıldı?", yanit="1071", sayi=True,
  aciklama=f"26 Ağustos 1071 Malazgirt Savaşı bir dönüm noktasıdır {K1}.")
a("u3k1", "Cihan Devleti", "dy", ifade="Cihan devleti, dünya çapında büyük bir güce ve etkiye sahip olan devlet demektir.", dogru=True,
  aciklama=f"Cihan devleti dünyaya adalet ve düzen getirmeyi amaçlar {K1}.")
a("u3k1", "Fatih, Yavuz ve Kanuni Dönemleri", "eslestir", soru="Padişahları dönemlerindeki olaylarla eşleştir.", ciftler=[
  {"sol": "Orhan Bey", "sag": "Bursa fethedildi."},
  {"sol": "Fatih Sultan Mehmed", "sag": "İstanbul fethedildi."},
  {"sol": "Yavuz Sultan Selim", "sag": "Mısır fethedildi."},
  {"sol": "Kanuni Sultan Süleyman", "sag": "Devlet üç kıtaya yayıldı."}],
  aciklama=f"Bursa Orhan, İstanbul Fatih, Mısır Yavuz; Kanuni'de üç kıta {K1}.")

# --- Konu 2: Fetih, iskân, istimalet
a("u3k2", "İskân Politikası", "secim", soru="Fethedilen yerlere Anadolu'dan Türk-Müslüman toplulukların yerleştirilmesine ne denir?",
  secenekler=["İstimalet", "İskân", "Fetih", "Lonca"], dogru=1,
  aciklama=f"Halkı yeni yerlere yerleştirmek iskândır {K2}.")
a("u3k2", "İstimalet Politikası", "secim", soru="Fethedilen yerlerde halka adaletli ve hoşgörülü davranarak gönlünü kazanmayı amaçlayan politika hangisidir?",
  secenekler=["İskân", "İstimalet", "Sömürgecilik", "Reform"], dogru=1,
  aciklama=f"İstimalet: gönlü kazan, düzeni kur {K2}.")
a("u3k2", "Türkmen ve Ahi Desteği", "dy", ifade="Ahiler, Osmanlı'ya destek veren bir esnaf teşkilatıdır.", dogru=True,
  aciklama=f"Türkmenler ve esnaf teşkilatı Ahiler Osmanlı'ya destek verdi {K2}.")
a("u3k2", "İmar ve Yeni Şehirler", "secim", soru="İskân politikasının amaçlarıyla ilgili aşağıdaki ifadeler verilmiştir.",
  onculler=["Fethedilen yerlerde kalıcı hâkimiyet kurmak", "Konargöçerleri yerleşik hayata geçirmek", "Fethedilen yerleri boş bırakmak"],
  kok="Bunlardan hangileri iskânın amaçları arasındadır?", secenekler=ONC, dogru=1,
  aciklama=f"İskânla yerleşim yerleri kuruldu; cami, köprü, han yapıldı {K2}.")
a("u3k2", "Derviş ve Abdallar", "secim", soru="İstimalet politikasında halkın güvenini kazanan ve Türk kültürünü tanıtan kişiler kimlerdir?",
  secenekler=["Yeniçeriler", "Derviş ve abdallar", "Kadılar", "Kaptanıderyalar"], dogru=1,
  aciklama=f"Derviş ve abdallar gönül elçileri gibi çalıştı {K2}.")

# --- Konu 3: İstanbul'un fethi
a("u3k3", "Gemilerin Karadan Yürütülmesi", "secim", soru="İstanbul kuşatmasında gemilerin karadan Haliç'e indirilmesinin nedeni nedir?",
  secenekler=["Haliç girişine çekilen zincirin aşılamaması", "Denizin donması", "Gemilerin eskimesi", "Askerlerin yorulması"], dogru=0,
  aciklama=f"Zincir aşılamayınca gemiler karadan yürütüldü {K3}.")
a("u3k3", "Rumeli Hisarı", "dy", ifade="Rumeli Hisarı, Doğu Roma'ya denizden yardım gelmesini engellemek için yaptırıldı.", dogru=True,
  aciklama=f"Anadolu Hisarı'nın karşısına yapılan Rumeli Hisarı Boğaz'ı kapattı {K3}.")
a("u3k3", "Fethin Sonuçları", "bosluk", havuz=["40", "Yavuz"], cumleler=[
  {"c": "İstanbul ___ gün süren kuşatmanın ardından fethedildi.", "cevap": "53"},
  {"c": "II. Mehmed fetihten sonra ___ unvanını aldı.", "cevap": "Fatih"},
  {"c": "Fetihle yaklaşık 1000 yıllık ___ İmparatorluğu yıkıldı.", "cevap": "Doğu Roma"}],
  aciklama=f"53 gün, Fatih unvanı, Doğu Roma'nın sonu {K3}.")
a("u3k3", "Şahi Topları", "secim", soru="İstanbul kuşatması için Macar usta Urban'a döktürülen büyük toplara ne ad verilir?",
  secenekler=["Şahi", "Grejuva", "Mancınık", "Kadırga"], dogru=0,
  aciklama=f"Şahi dev bir toptur. Grejuva ise Doğu Roma'nın Rum ateşidir {K3}.")
a("u3k3", "Fethin Nedenleri", "secim", soru="İstanbul'un fethinin nedenleriyle ilgili aşağıdaki ifadeler verilmiştir.",
  onculler=["İstanbul, Osmanlı'nın toprak bütünlüğüne engel oluyordu.", "Şehir önemli ticaret yolları üzerindeydi.", "Hz. Muhammed'in (sav) fethi müjdeleyen hadisi vardı."],
  kok="Bu ifadelerden hangileri fethin nedenleri arasındadır?", secenekler=ONC, dogru=3,
  aciklama=f"Toprak bütünlüğü, ticaret yolları ve hadisteki müjde: üçü de neden {K3}.")

# --- Konu 4: Mısır seferi ve Preveze
a("u3k4", "Mercidabık ve Ridaniye", "secim", soru="Memlük Devleti'ne son veren savaşlar hangileridir?",
  secenekler=["Çaldıran ve Malazgirt", "Mercidabık ve Ridaniye", "Preveze ve Turnadağ", "Kosova ve Niğbolu"], dogru=1,
  aciklama=f"1516 Mercidabık ve 1517 Ridaniye ile Memlük Devleti yıkıldı {K4}.")
a("u3k4", "Halifelik ve Kutsal Emanetler", "dy", ifade="Mısır Seferi'nden sonra Osmanlı padişahları halife unvanını taşımaya başladı.", dogru=True,
  aciklama=f"Kutsal emanetler de İstanbul'a getirildi, Topkapı'da korunuyor {K4}.")
a("u3k4", "Preveze Deniz Zaferi", "secim", soru="1538'de Preveze'de Haçlı donanmasını yenen Osmanlı denizcisi kimdir?",
  secenekler=["Piri Reis", "Barbaros Hayreddin Paşa", "Andrea Doria", "Seydi Ali Reis"], dogru=1,
  aciklama=f"Barbaros donanmayı hilal düzeninde dizerek kazandı. Andrea Doria Haçlı komutanıdır {K4}.")
a("u3k4", "Mısır Seferi'nin Sonuçları", "secim", soru="Mısır Seferi'nin ekonomik sonucu hangisidir?",
  secenekler=["Baharat Yolu Osmanlı denetimine geçti.", "Bursa başkent oldu.", "Matbaa açıldı.", "Yeniçeri Ocağı kaldırıldı."], dogru=0,
  aciklama=f"Baharat Yolu Osmanlı'ya geçti, Mısır vergileri ekonomiyi güçlendirdi {K4}.")
a("u3k4", "Yavuz Sultan Selim", "kisa", soru="Yavuz Sultan Selim'in Safevileri yendiği savaş hangisidir?", yanit="Çaldıran", kabul=["Çaldıran Savaşı"],
  aciklama=f"1514 Çaldıran Savaşı doğu sınırını güçlendirdi {K4}.")

# --- Konu 5: Coğrafi keşifler ve sömürgecilik
a("u3k5", "Deniz Seyahatlerinin Nedenleri", "secim", soru="Avrupalıların yeni ticaret yolları aramasının temel nedeni nedir?",
  secenekler=["Osmanlı'nın İpek ve Baharat Yollarını kontrol etmesi", "Avrupa'da nüfusun azalması", "Matbaanın bulunmaması", "Haçlı Seferlerinin kazanılması"], dogru=0,
  aciklama=f"Yollar Osmanlı'daydı; Avrupalılar Doğu'ya yeni yol aradı {K5}.")
a("u3k5", "Amerika ve Dünya Turu", "eslestir", soru="Denizcileri başarılarıyla eşleştir.", ciftler=[
  {"sol": "Bartolomeu Dias", "sag": "Ümit Burnu'na ulaştı (1487)."},
  {"sol": "Kristof Kolomb", "sag": "Amerika'ya ulaştı (1492)."},
  {"sol": "Vasco da Gama", "sag": "Deniz yoluyla Hindistan'a vardı (1497)."},
  {"sol": "Macellan ve Del Cano", "sag": "Dünya'nın yuvarlak olduğunu kanıtladı."}],
  aciklama=f"Dias 1487, Kolomb 1492, Gama 1497; Macellan-Del Cano dünya turu {K5}.")
a("u3k5", "Sömürgecilik", "kisa", soru="Bir devletin başka toprakları ele geçirip oradaki kaynakları kendi çıkarı için kullanmasına ne denir?", yanit="sömürgecilik",
  aciklama=f"Başkasının kaynağını almak sömürgeciliktir {K5}.")
a("u3k5", "Osmanlı İçin Sonuçlar", "dy", ifade="Coğrafi keşifler Osmanlı'nın ticaret gelirlerini artırmıştır.", dogru=False,
  duzeltme="İpek ve Baharat Yolları önemini yitirdi; Osmanlı'nın gelirleri azaldı.",
  aciklama=f"Yeni yollar bulununca Osmanlı'nın yolları önemini kaybetti {K5}.")
a("u3k5", "Yerli Halklar İçin Sonuçlar", "secim", soru="Coğrafi keşiflerin yerli halklara etkisi hangisidir?",
  secenekler=["Zenginleştiler.", "Kültürleri zarar gördü, nüfusları azaldı.", "Avrupa'ya göç ettiler.", "Hiç etkilenmediler."], dogru=1,
  aciklama=f"Salgınlar ve baskı yüzünden yerli kültürler büyük zarar gördü {K5}.")

# --- Konu 6: Rönesans, reform, aydınlanma
a("u3k6", "Rönesans", "secim", soru="Rönesans hangi ülkede başlamıştır?",
  secenekler=["İngiltere", "Almanya", "İtalya", "İspanya"], dogru=2,
  aciklama=f"Rönesans İtalya'da başladı, sonra Avrupa'ya yayıldı {K6}.")
a("u3k6", "Martin Luther", "secim", soru="Reform hareketini Almanya'da başlatan din adamı kimdir?",
  secenekler=["Galileo", "Martin Luther", "Kopernik", "Newton"], dogru=1,
  aciklama=f"Luther 1517'de bildirisini Wittenberg Kilisesi'nin kapısına astı {K6}.")
a("u3k6", "Reform", "eslestir", soru="Kilisenin uygulamalarını anlamlarıyla eşleştir.", ciftler=[
  {"sol": "Aforoz", "sag": "Dinden çıkarma"},
  {"sol": "Endüljans", "sag": "Para karşılığı günah bağışlama belgesi"},
  {"sol": "Enterdi", "sag": "Bir bölge halkını dinî haklardan mahrum bırakma"}],
  aciklama=f"Bu yanlış uygulamalar Reform'a yol açtı {K6}.")
a("u3k6", "Aydınlanma Çağı", "dy", ifade="Aydınlanma Çağı'nda doğru bilgiye akıl, gözlem ve deney yoluyla ulaşılabileceği savunuldu.", dogru=True,
  aciklama=f"Aydınlanma: akıl, gözlem, deney {K6}.")
a("u3k6", "Rönesans'ın Nedenleri", "secim", soru="Hangisi Rönesans'ın nedenlerinden biri değildir?",
  secenekler=["Matbaayla kitapların çoğalması", "Eski eserlerin yeniden incelenmesi", "Burjuvanın sanata destek vermesi", "Fransız İhtilali"], dogru=3,
  aciklama=f"Fransız İhtilali (1789) Rönesans'tan çok sonradır {K6}.")

# --- Konu 7: Sanayi İnkılabı ve Fransız İhtilali
a("u3k7", "Sanayi İnkılabı", "secim", soru="Sanayi İnkılabı hangi ülkede başlamıştır?",
  secenekler=["Fransa", "İngiltere", "İtalya", "Osmanlı Devleti"], dogru=1,
  aciklama=f"XVIII. yüzyılın ikinci yarısında İngiltere'de, buhar makinesiyle başladı {K7}.")
a("u3k7", "Fransız İhtilali", "kisa", soru="Fransız İhtilali hangi yıl başlamıştır?", yanit="1789", sayi=True,
  aciklama=f"14 Temmuz 1789'da Bastille Hapishanesi ele geçirildi {K7}.")
a("u3k7", "Ham Madde ve Pazar", "secim", soru="Sanayi İnkılabı sömürgeciliği neden hızlandırdı?",
  secenekler=["Fabrikaların ham madde ve pazar ihtiyacı arttı.", "Avrupa'da nüfus azaldı.", "Gemiler yasaklandı.", "Ticaret durdu."], dogru=0,
  aciklama=f"Kömür, pamuk, kauçuk gibi ham madde ihtiyacı sömürgeciliği hızlandırdı {K7}.")
a("u3k7", "Fransız İhtilali ve Osmanlı", "secim", soru="Fransız İhtilali'nin yaydığı hangi akım çok milletli Osmanlı Devleti'nde isyanlara yol açtı?",
  secenekler=["Hümanizm", "Milliyetçilik", "Sömürgecilik", "Rönesans"], dogru=1,
  aciklama=f"“Her millete bir devlet” anlayışı Balkanlarda isyanlar çıkardı {K7}.")
a("u3k7", "Sanayi İnkılabı ve Osmanlı", "dy", ifade="Avrupa'nın ucuz fabrika malları Osmanlı'daki el tezgâhlarını zor duruma düşürdü.", dogru=True,
  aciklama=f"Ucuz mallar yüzünden yerli üretim azaldı, atölyeler kapandı {K7}.")

# --- Konu 8: Lale Devri ve Nizâm-ı Cedîd
a("u3k8", "İlk Türk Matbaası", "secim", soru="İlk Türk matbaasını 1727'de kim açmıştır?",
  secenekler=["Yirmisekiz Mehmed Çelebi", "İbrahim Müteferrika", "Damat İbrahim Paşa", "Patrona Halil"], dogru=1,
  aciklama=f"İbrahim Müteferrika 1727'de ilk Türk matbaasını açtı {K8}.")
a("u3k8", "Tulumbacılar Ocağı", "secim", soru="1720'de kurulan, Osmanlı'nın ilk itfaiye teşkilatı hangisidir?",
  secenekler=["Tulumbacılar Ocağı", "Yeniçeri Ocağı", "Divan-ı Hümayun", "Enderun"], dogru=0,
  aciklama=f"Tulumbacılar Ocağı ilk itfaiye teşkilatıdır {K8}.")
a("u3k8", "Lale Devri", "bosluk", havuz=["1789", "1826"], cumleler=[
  {"c": "Lale Devri ___ yılında Pasarofça Antlaşması ile başladı.", "cevap": "1718"},
  {"c": "Lale Devri ___ yılında Patrona Halil İsyanı ile sona erdi.", "cevap": "1730"},
  {"c": "İlk Türk matbaası ___ yılında açıldı.", "cevap": "1727"}],
  aciklama=f"Lale Devri 1718–1730; matbaa 1727 {K8}.")
a("u3k8", "Nizâm-ı Cedîd", "dy", ifade="Nizâm-ı Cedîd, “Yeni Düzen” anlamına gelir ve III. Selim'in yeniliklerinin adıdır.", dogru=True,
  aciklama=f"Nizâm-ı Cedîd = Yeni Düzen (III. Selim) {K8}.")
a("u3k8", "III. Selim'in Diğer Yenilikleri", "secim", soru="Hangisi III. Selim Dönemi'nin yeniliklerinden biri değildir?",
  secenekler=["İrâd-ı Cedîd Hazinesi", "Avrupa'da daimî elçilikler", "Kara Mühendishanesi", "Tanzimat Fermanı"], dogru=3,
  aciklama=f"Tanzimat Fermanı 1839'da Abdülmecid zamanında ilan edildi {K8}.")

# --- Konu 9: II. Mahmud, Tanzimat, sanayileşme, Türk modası
a("u3k9", "Vaka-i Hayriye", "secim", soru="1826'da Yeniçeri Ocağı'nın kaldırılmasına ne ad verilir?",
  secenekler=["Vaka-i Hayriye", "Tanzimat", "Islahat", "Lale Devri"], dogru=0,
  aciklama=f"Vaka-i Hayriye “Hayırlı Olay” demektir {K9}.")
a("u3k9", "Takvim-i Vekayi", "secim", soru="1831'de çıkarılan ilk resmî Osmanlı gazetesi hangisidir?",
  secenekler=["Tercümân-ı Ahvâl", "Takvim-i Vekayi", "Tasvîr-i Efkâr", "Mecelle"], dogru=1,
  aciklama=f"Takvim-i Vekayi ilk resmî gazetedir; diğerleri özel gazetelerdir {K9}.")
a("u3k9", "Tanzimat Fermanı", "dy", ifade="Tanzimat Fermanı ile padişah ilk kez kendi yetkilerini sınırladı.", dogru=True,
  aciklama=f"3 Kasım 1839 Tanzimat Fermanı padişahın yetkisini sınırladı {K9}.")
a("u3k9", "Nazırlıklar", "secim", soru="II. Mahmud Divan teşkilatını kaldırıp yerine ne kurdu?",
  secenekler=["Nazırlıklar (bakanlıklar)", "Loncalar", "Vakıflar", "Medreseler"], dogru=0,
  aciklama=f"Divan yerine nazırlıklar kuruldu {K9}.")
a("u3k9", "Türk Modası", "secim", soru="XVIII. yüzyılda Avrupa'da Osmanlı kültürüne duyulan ilgiyle ortaya çıkan akım hangisidir?",
  secenekler=["Türk Modası", "Rönesans", "Reform", "Hümanizm"], dogru=0,
  aciklama=f"Türk Modası: Osmanlı kültürü Avrupa'yı etkiledi {K9}.")

# --- Konu 10: Kültür izleri ve devlet yönetimi
a("u3k10", "Külliye", "secim", soru="Cami, medrese, darüşşifa ve imaret gibi yapıların bir arada bulunduğu yapı topluluğuna ne denir?",
  secenekler=["Külliye", "Bedesten", "Lonca", "Divan"], dogru=0,
  aciklama=f"Külliyede ibadet, eğitim ve sağlık bir aradadır {K10}.")
a("u3k10", "Veziriazam", "secim", soru="Osmanlı'da padişahtan sonra en yetkili devlet adamı kimdir?",
  secenekler=["Kazasker", "Defterdar", "Veziriazam", "Nişancı"], dogru=2,
  aciklama=f"Veziriazam padişahın vekiliydi ve mührünü taşırdı {K10}.")
a("u3k10", "Divan Üyeleri", "eslestir", soru="Divan üyelerini görevleriyle eşleştir.", ciftler=[
  {"sol": "Defterdar", "sag": "Gelir ve giderleri denetler."},
  {"sol": "Nişancı", "sag": "Belgelere padişahın tuğrasını çeker."},
  {"sol": "Kaptanıderya", "sag": "Donanmadan sorumludur."},
  {"sol": "Kazasker", "sag": "Büyük davalara bakar, kadı atar."}],
  aciklama=f"Divan'da her işe bir sorumlu vardı {K10}.")
a("u3k10", "Merkez ve Taşra Yönetimi", "dy", ifade="Osmanlı'da taşra yönetimi, başkentteki saray ve Divan'ın yönetimidir.", dogru=False,
  duzeltme="Başkent merkez yönetimidir; taşra, merkezden uzak eyalet ve sancakların yönetimidir.",
  aciklama=f"Merkez = başkent, taşra = uzak eyalet ve sancaklar {K10}.")
a("u3k10", "Divan-ı Hümayun", "secim", soru="Divan-ı Hümayun hangi padişah döneminde kaldırılmıştır?",
  secenekler=["Fatih", "Kanuni", "II. Mahmud", "III. Ahmed"], dogru=2,
  aciklama=f"II. Mahmud Divan'ı kaldırıp nazırlıkları kurdu {K10}.")

# --- Konu 11: Eğitim ve hukuk
a("u3k11", "Enderun Mektebi", "secim", soru="Saray içinde kurulan ve devletin üst düzey yöneticilerini yetiştiren okul hangisidir?",
  secenekler=["Sıbyan mektebi", "Enderun Mektebi", "Rüştiye", "İdadî"], dogru=1,
  aciklama=f"Enderun saray içindeki yönetici okuluydu {K11}.")
a("u3k11", "Şer'i ve Örfi Hukuk", "secim", soru="Osmanlı hukuku ile ilgili aşağıdaki ifadeler verilmiştir.",
  onculler=["Şer'i Hukuk İslam dininin kurallarına dayanır.", "Örfi Hukuk padişahların koyduğu kurallar ve geleneklerden oluşur.", "Adalet işlerini kaptanıderyalar yürütürdü."],
  kok="Bu ifadelerden hangileri doğrudur?", secenekler=ONC, dogru=1,
  aciklama=f"Osmanlı'da adalet işlerini kadılar yürütürdü {K11}.")
a("u3k11", "Mecelle ve Kanun-ı Esasi", "eslestir", soru="Belgeleri açıklamalarıyla eşleştir.", ciftler=[
  {"sol": "Mecelle", "sag": "İlk medeni kanun niteliğindeki hukuk metni"},
  {"sol": "Kanun-ı Esasi", "sag": "İlk anayasa"},
  {"sol": "Kanunname", "sag": "Padişahların çıkardığı kuralların toplandığı metin"}],
  aciklama=f"Mecelle medeni kanun, Kanun-ı Esasi anayasadır {K11}.")
a("u3k11", "Sıbyan Mektebi", "dy", ifade="Sıbyan mekteplerinde yalnızca erkek çocuklar eğitim görürdü.", dogru=False,
  duzeltme="Erkeklerin yanında 8-9 yaşına kadar kızlar da eğitim görürdü.",
  aciklama=f"Sıbyan mekteplerinde kızlar da okurdu {K11}.")
a("u3k11", "Batı Tarzı Okullar", "kisa", soru="İlk üniversite sayılan Osmanlı okulunun adı nedir?", yanit="Darülfünun",
  aciklama=f"Darülfünun bugünkü İstanbul Üniversitesi'nin temelidir {K11}.")

# --- Konu 12: Sanat, günlük hayat, vakıflar, Ahilik
a("u3k12", "Vakıf", "secim", soru="Kişilerin mal veya mülklerini toplum yararına süresiz bağışlamasına ne denir?",
  secenekler=["Lonca", "Vakıf", "Ahilik", "Külliye"], dogru=1,
  aciklama=f"Vakfedilen mal satılamaz, devredilemez {K12}.")
a("u3k12", "Ahilik", "secim", soru="Anadolu'da halkı meslek alanında yetiştiren ve ahlaki yönden eğiten Ahilik teşkilatının kurucusu kimdir?",
  secenekler=["Ahi Evran", "Mimar Sinan", "Ahmet Cevdet Paşa", "Akşemsettin"], dogru=0,
  aciklama=f"Ahiliğin kurucusu Ahi Evran'dır {K12}.")
a("u3k12", "Süsleme Sanatları", "kisa", soru="Güzel yazı yazma sanatına ne ad verilir?", yanit="hat", kabul=["hat sanatı"],
  aciklama=f"Hat güzel yazı sanatıdır {K12}.")
a("u3k12", "Mehter Takımı", "dy", ifade="Mehter Takımı, Osmanlı ordusunun resmî müzik topluluğudur.", dogru=True,
  aciklama=f"Mehter ordunun resmî müziğidir; Mozart bile etkilendi {K12}.")
a("u3k12", "Lonca", "secim", soru="Ahilikten sonra aynı meslekten esnafın oluşturduğu, devlet denetimindeki meslek örgütü hangisidir?",
  secenekler=["Lonca", "Divan", "Vakıf", "Enderun"], dogru=0,
  aciklama=f"Ahiliğin yerini loncalar aldı {K12}.")
H.yaz()
