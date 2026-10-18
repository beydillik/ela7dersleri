import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from ortak import Havuz, ONC
H = Havuz("bil1", 2, "b2"); a = H.add

# --- Konu 1: Tasarım Elemanları 1 (s. 23–24 + program)
a("u2k1", "Nokta", "eslestir", soru="Elemanları anlamlarıyla eşleştir.", ciftler=[
  {"sol": "Nokta", "sag": "Yer belirten işaret"},
  {"sol": "Çizgi", "sag": "Noktanın bir doğrultudaki uzantısı"},
  {"sol": "Aralık", "sag": "İki şeyin arasındaki açıklık"},
  {"sol": "Yön", "sag": "Bir şeyin baktığı taraf"}],
  aciklama="Nokta yer, çizgi uzantı, aralık mesafe, yön taraftır (s. 24).")
a("u2k1", "Çizgi", "dy", ifade="Çizgi, bir noktanın verilen doğrultudaki uzantısıdır.", dogru=True,
  aciklama="Nokta bir yöne uzayınca çizgi oluşur (s. 24).")
a("u2k1", "Şekil", "dytablo", soru="Geometrik şekilse D, değilse Y seç.", ifadeler=[
  {"s": "Kare", "d": True}, {"s": "Yaprak", "d": False}, {"s": "Üçgen", "d": True}, {"s": "Bulut", "d": False}],
  aciklama="Kare ve üçgen geometrik; yaprak ve bulut organik şekildir (program).")
a("u2k1", "Biçim-Form", "secim", soru="Aşağıdakilerden hangisi üç boyutlu bir formdur?",
  secenekler=["Daire", "Kare", "Küre", "Çizgi"], dogru=2,
  aciklama="Kürenin eni, boyu ve derinliği vardır; form üç boyutludur (program).")
a("u2k1", "Mekân", "bosluk", havuz=["doku", "ritim"], cumleler=[
  {"c": "Resimde nesnenin olduğu dolu kısma ___ alan denir.", "cevap": "pozitif"},
  {"c": "Nesnenin etrafında kalan boş kısma ___ alan denir.", "cevap": "negatif"},
  {"c": "İki şeyin arasındaki açıklığa ___ denir.", "cevap": "aralık"}],
  aciklama="Dolu alan pozitif, boş alan negatif; iki şeyin arası aralıktır (s. 24; program).")
a("u2k1", "Nokta", "dy", ifade="Noktaların sayısı arttıkça etkileri değişmez.", dogru=False,
  duzeltme="Noktaların sayısı arttıkça etkileri de değişir.",
  aciklama="Çok sayıda nokta desen ya da şekil oluşturabilir (s. 24).")
a("u2k1", "Yön", "kisa", soru="Bir şeyin belli bir noktaya göre baktığı tarafa ne denir?", yanit="yön",
  aciklama="Belli bir noktaya göre olan taraf yöndür (s. 24).")

# --- Konu 2: Tasarım Elemanları 2 (s. 24 + program)
a("u2k2", "Renk", "secim", soru="Renk ile ilgili aşağıdaki bilgiler verilmiştir.",
  onculler=["Işığın cisimlerden yansımasıyla oluşur.", "Sıcak renkler uyarıcıdır.", "Soğuk renkler dinlendiricidir."],
  kok="Bu bilgilerden hangileri doğrudur?", secenekler=ONC, dogru=3,
  aciklama="Renk ışığın yansımasıdır; sıcak renk uyarır, soğuk renk dinlendirir (s. 24).")
a("u2k2", "Valör (Değer)", "dy", ifade="Valör, bir rengin açıklık ya da koyuluk derecesidir.", dogru=True,
  aciklama="Açıktan koyuya sıralanan tonlar valörü gösterir (program).")
a("u2k2", "Işık-Gölge", "secim", soru="Masa lambası topun sağ tarafındadır. Topun gölgesi nereye düşer?",
  secenekler=["Sağ tarafa", "Sol tarafa", "Lambanın üstüne", "Gölge oluşmaz"], dogru=1,
  aciklama="Gölge ışığın karşı tarafına düşer; ışık sağdan gelirse gölge soldadır (s. 24).")
a("u2k2", "Doku", "eslestir", soru="Elemanları örnekleriyle eşleştir.", ciftler=[
  {"sol": "Doku", "sag": "Ağaç kabuğunun pürüzlü yüzeyi"},
  {"sol": "Yazı", "sag": "Afişteki slogan"},
  {"sol": "Oran", "sag": "Ağacın evden büyük çizilmesi"},
  {"sol": "Işık-Gölge", "sag": "Lambanın arkasına düşen karanlık"}],
  aciklama="Her eleman günlük bir örnekle eşleşir (s. 24).")
a("u2k2", "Oran", "bosluk", havuz=["vurgu", "ritim"], cumleler=[
  {"c": "Nesnelerin büyüklük-küçüklük bakımından birbiriyle ilişkisine ___ denir.", "cevap": "oran"},
  {"c": "Nesnelerin dış yapı özelliklerinin oluşturduğu elemana ___ denir.", "cevap": "doku"},
  {"c": "Dile ait görsel işaretlerle yapılan iletişime ___ denir.", "cevap": "yazı"}],
  aciklama="Oran büyüklük, doku yüzey, yazı iletişimdir (s. 24).")
a("u2k2", "Renk", "dy", ifade="Dinlenme odası için sıcak ve uyarıcı renkler en uygun seçimdir.", dogru=False,
  duzeltme="Dinlenme odası için gevşetici, dinlendirici soğuk renkler uygundur.",
  aciklama="Soğuk renkler gevşetici ve dinlendiricidir (s. 24).")
a("u2k2", "Yazı", "kisa", soru="Afişteki slogan hangi tasarım elemanına örnektir?", yanit="yazı",
  aciklama="Slogan, dile dair görsel işaretlerle yapılan iletişimdir (s. 24).")

# --- Konu 3: Tasarım İlkeleri 1 (s. 27–28 + program)
a("u2k3", "Ritim", "eslestir", soru="İlkeleri örnekleriyle eşleştir.", ciftler=[
  {"sol": "Ritim", "sag": "Gece ile gündüzün birbirini izlemesi"},
  {"sol": "Vurgu", "sag": "Düz elbisenin üstündeki kolye"},
  {"sol": "Denge", "sag": "Parçaların eşit dağılması"},
  {"sol": "Zıtlık", "sag": "Siyah zemine beyaz yazı"}],
  aciklama="Kitap ve programdaki örnekler ilkelerle eşleşir (s. 27; program).")
a("u2k3", "Vurgu", "secim", soru="Tasarımda göz alıcı olan odak noktasına ne denir?",
  secenekler=["Denge", "Ritim", "Harmoni", "Vurgu"], dogru=3,
  aciklama="Göz alıcı odak noktası vurgudur (s. 27).")
a("u2k3", "Denge", "dy", ifade="Denge, parçaların bütün içinde eşit olarak dağılmasıdır.", dogru=True,
  aciklama="Eşit dağılım tasarımı kararlı gösterir (s. 27).")
a("u2k3", "Hareket", "secim", soru="Resimdeki topun arkasına hız çizgileri ve ok çizilmiş. Hangi ilke sağlanmıştır?",
  secenekler=["Hareket", "Birlik", "Harmoni", "Denge"], dogru=0,
  aciklama="Yön veren çizgiler hareket hissi oluşturur (s. 28; program).")
a("u2k3", "Ritim", "dy", ifade="Ritim yalnızca birbirinin aynısı olan elemanlarla sağlanabilir.", dogru=False,
  duzeltme="Ritim farklı ya da zıt elemanlarla da sağlanabilir.",
  aciklama="Kitaba göre ritmik etki farklı veya zıt elemanlarla da olur (s. 27).")
a("u2k3", "Zıtlık", "kisa", soru="Açık-koyu, büyük-küçük gibi karşıt elemanların yan yana kullanılmasına ne denir?", yanit="zıtlık", kabul=["kontrast"],
  aciklama="Karşıtların yan yana gelmesi zıtlıktır (kontrast) (program).")
a("u2k3", "Vurgu", "dytablo", soru="Vurgu sağlıyorsa D, sağlamıyorsa Y seç.", ifadeler=[
  {"s": "Metindeki koyu yazılmış bölüm", "d": True}, {"s": "Gri noktalar arasındaki tek kırmızı nokta", "d": True},
  {"s": "Hep aynı renk ve boyda tekrar eden desen", "d": False}],
  aciklama="Dikkati bir yere çeken şey vurgudur; aynı tekrar ritimdir (s. 27).")

# --- Konu 4: Tasarım İlkeleri 2 (s. 24, 27–28)
a("u2k4", "Harmoni", "eslestir", soru="İlkeleri kitaptaki örnekleriyle eşleştir.", ciftler=[
  {"sol": "Harmoni", "sag": "Düğmenin kumaşın rengine uygun olması"},
  {"sol": "Birlik (Bütünlük)", "sag": "Klasik mobilyalı odaya klasik perde"},
  {"sol": "Oran-Orantı", "sag": "Binadaki pencerelerin sayısı ve büyüklüğü"}],
  aciklama="Kitap her ilkeyi bir günlük örnekle anlatır (s. 27).")
a("u2k4", "Çeşitlilik", "secim", soru="Değişiklik ve zıtlıkları içeren tasarım ilkesi hangisidir?",
  secenekler=["Denge", "Çeşitlilik", "Birlik", "Ritim"], dogru=1,
  aciklama="Çeşitlilik değişiklik ve zıtlıkları içerir (s. 27).")
a("u2k4", "Eleman mı, İlke mi?", "dytablo", soru="Tasarım ilkesiyse D, tasarım elemanıysa Y seç.", ifadeler=[
  {"s": "Harmoni", "d": True}, {"s": "Doku", "d": False}, {"s": "Çeşitlilik", "d": True}, {"s": "Nokta", "d": False}],
  aciklama="Harmoni ve çeşitlilik ilke; doku ve nokta elemandır (s. 24, 27).")
a("u2k4", "Oran-Orantı", "secim", soru="Oran ile ilgili aşağıdaki bilgiler verilmiştir.",
  onculler=["Kitapta eleman olarak geçer.", "Kitapta ilke olarak geçer.", "Yalnız renklerle ilgilidir."],
  kok="Bu bilgilerden hangileri doğrudur?", secenekler=ONC, dogru=1,
  aciklama="Oran hem eleman hem ilkedir; renkle ilgili değildir (s. 24, 27).")
a("u2k4", "Birlik (Bütünlük)", "dy", ifade="Modern bir odaya çok eski tarzda bir dolap koymak bütünlüğü güçlendirir.", dogru=False,
  duzeltme="Elemanlar tutarlı kullanılmazsa bütünlük bozulur.",
  aciklama="Bütünlük için çizgi, renk, malzeme tutarlı kullanılmalıdır (s. 27).")
a("u2k4", "Harmoni", "kisa", soru="Bir bütünün parçaları arasındaki uygunluğa ne denir?", yanit="harmoni", kabul=["uyum"],
  aciklama="Parçalar arasındaki uygunluk harmonidir (s. 27).")
a("u2k4", "Oran-Orantı", "bosluk", havuz=["doku", "yazı"], cumleler=[
  {"c": "Bir parçanın diğer parçalarla ve bütünle ilişkisine ___ denir.", "cevap": "oran-orantı"},
  {"c": "Farklılık ve zıtlıkları bir arada kullanmaya ___ denir.", "cevap": "çeşitlilik"},
  {"c": "Tüm parçalarda aranan bütünsel uyuma ___ denir.", "cevap": "bütünlük"}],
  aciklama="Oran-orantı ilişki, çeşitlilik farklılık, bütünlük uyumdur (s. 27).")

# --- Konu 5: Analoji ve Yeniden Yorumlama (s. 29–30 + program)
a("u2k5", "Analoji", "secim", soru="Aşağıdakilerden hangisi analojiye örnektir?",
  secenekler=["Kuş kanadına benzeyen uçak kanadı tasarlamak", "Kalemi masaya koymak", "Kitabın sayfasını çevirmek", "Odayı süpürmek"], dogru=0,
  aciklama="Birbirini andıran iki şeyi ilişkilendirmek analojidir (program).")
a("u2k5", "Yeniden Yorumlama", "dy", ifade="Yeniden yorumlamada ürün anlamı bozulmadan, kendi fikrimizle dönüştürülür.", dogru=True,
  aciklama="Ürün bağlamından koparılmadan dönüştürülür (program).")
a("u2k5", "Ürün Analizi", "dytablo", soru="Kitaptaki ürün analizi sorularından biriyse D, değilse Y seç.", ifadeler=[
  {"s": "Kullanıcılar için güvenli mi?", "d": True}, {"s": "Hangi malzemeler kullanılmış?", "d": True},
  {"s": "Kaç kişi beğenmiş?", "d": False}, {"s": "Hangi parçalardan oluşmuş?", "d": True}],
  aciklama="Güvenlik, malzeme ve parçalar analiz sorusudur; beğeni değildir (s. 30).")
a("u2k5", "Kesme, Katlama, Birleştirme", "bosluk", havuz=["eritme", "dökme"], cumleler=[
  {"c": "Kartonu makasla şekline göre ___.", "cevap": "keseriz"},
  {"c": "Kâğıdı çizgisinden ___.", "cevap": "katlarız"},
  {"c": "Parçaları yapıştırıcıyla ___.", "cevap": "birleştiririz"}],
  aciklama="Kâğıt-kartonla kesme, katlama, birleştirme yapılır (s. 29).")
a("u2k5", "Taslaktan Özgün Ürüne", "secim", soru="Özgün bir ürün oluşturmanın doğru sırası hangisidir?",
  secenekler=["Ürünü yap → taslak çiz", "Taslak çiz → ürüne dönüştür", "Ürünü sat → taslak çiz", "Ürünü paketle → taslak çiz"], dogru=1,
  aciklama="Önce eleman ve ilkelerle taslak, sonra ürün yapılır (program).")
a("u2k5", "Biçimsel ve İşlevsel Değişiklik", "dy", ifade="Kitap, kullandığımız bir üründe şekil ya da işlev değişikliği yapmamızı ister.", dogru=True,
  aciklama="Üründe şeklen ya da işlevsel değişiklik yapılır (s. 29).")
a("u2k5", "Analoji", "kisa", soru="Birbirine benzeyen ya da birbirini andıran iki şeyi ilişkilendirmeye ne denir?", yanit="analoji", kabul=["benzetme"],
  aciklama="İki benzer unsuru ilişkilendirmek analojidir (program).")

H.yaz()
