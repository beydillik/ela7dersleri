import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from ortak import Havuz, ONC
H = Havuz("bil1", 1, "b1"); a = H.add

# --- Konu 1: Buluş, İcat ve Teknoloji (s. 11)
a("u1k1", "Buluş", "eslestir", soru="Kavramları anlamlarıyla eşleştir.", ciftler=[
  {"sol": "Buluş", "sag": "Var olan ama bilinmeyeni öğrenmek"},
  {"sol": "Keşif", "sag": "Bilinmeyen bir kıtayı bulmak"},
  {"sol": "İcat", "sag": "Var olanları birleştirip yeni bir şey yapmak"},
  {"sol": "Teknik", "sag": "Bir meslekte kullanılan yöntemlerin tümü"}],
  aciklama="Buluş öğrenmek, keşif yer bulmak, icat yeni şey yapmaktır (s. 11).")
a("u1k1", "İcat", "dytablo", soru="İcat olanlara D, olmayanlara Y seç.", ifadeler=[
  {"s": "Kibrit", "d": True}, {"s": "Araba", "d": True}, {"s": "Yer çekiminin fark edilmesi", "d": False}, {"s": "Daktilo", "d": True}],
  aciklama="Kibrit, araba, daktilo icattır; yer çekiminin fark edilmesi buluştur (s. 11).")
a("u1k1", "Bilim", "dy", ifade="Bilim ile teknoloji arasında döngüsel bir ilişki vardır.", dogru=True,
  aciklama="Bilim teknolojiyi üretir, teknoloji de bilimi hızlandırır (s. 11).")
a("u1k1", "Teknoloji", "kisa", soru="\"Techne\" (yapmak) ve \"logos\" (bilmek) sözcüklerinden gelen kavram nedir?", yanit="teknoloji",
  aciklama="Teknoloji, yapmayı bilmek anlamındaki iki sözcükten gelir (s. 11).")
a("u1k1", "İnovasyon", "secim", soru="Aşağıdakilerden hangisi inovasyona örnektir?",
  secenekler=["Cep telefonuyla görüntülü konuşma", "Ateşin fark edilmesi", "Yeni bir gezegenin bulunması", "Suyun kaldırma kuvvetinin fark edilmesi"], dogru=0,
  aciklama="Görüntülü iletişim kitaptaki inovasyon örneğidir; diğerleri buluş ya da keşiftir (s. 11).")
a("u1k1", "Teknik", "bosluk", havuz=["keşif", "endüstri"], cumleler=[
  {"c": "Bir meslekte kullanılan yöntemlerin tümüne ___ denir.", "cevap": "teknik"},
  {"c": "Deneylere ve gerçeklere dayanan düzenli bilgilere ___ denir.", "cevap": "bilim"},
  {"c": "Yaratıcılığın ticari ustalıkla birleşmesine ___ denir.", "cevap": "inovasyon"}],
  aciklama="Teknik yöntem, bilim düzenli bilgi, inovasyon yararlı yeniliktir (s. 11).")

# --- Konu 2: Endüstri Devrimleri (s. 11–12)
a("u1k2", "Endüstri 1.0", "eslestir", soru="Sanayi devrimlerini anahtar kelimeleriyle eşleştir.", ciftler=[
  {"sol": "Endüstri 1.0", "sag": "Su ve buhar gücü"},
  {"sol": "Endüstri 2.0", "sag": "Elektrik ve üretim bandı"},
  {"sol": "Endüstri 3.0", "sag": "Elektronik ve otomasyon"},
  {"sol": "Endüstri 4.0", "sag": "Akıllı cihazlar ve yapay zekâ"}],
  aciklama="1.0 makineleşme, 2.0 elektrik, 3.0 otomasyon, 4.0 dijitalleşme (s. 12).")
a("u1k2", "Endüstri", "kisa", soru="Endüstrinin Türkçedeki diğer adı nedir?", yanit="sanayi",
  aciklama="Sanayi ya da endüstri, makinelerle toplu üretim yapan faaliyet dalıdır (s. 12).")
a("u1k2", "Endüstri 5.0", "secim", soru="Endüstri 5.0 ile ilgili aşağıdaki bilgiler verilmiştir.",
  onculler=["İnsan, toplum ve çevreyi öne çıkarır.", "Japon modelidir.", "Süper akıllı toplum olarak tanımlanır."],
  kok="Bu bilgilerden hangileri doğrudur?", secenekler=ONC, dogru=3,
  aciklama="Toplum 5.0, insanı, toplumu, çevreyi öne çıkaran Japon modelidir; süper akıllı toplum da denir (s. 12).")
a("u1k2", "Endüstri 3.0", "dy", ifade="Üretimin maliyeti düşük ülkelere yaptırılmasına Endüstri 3,5 yani küreselleşme denir.", dogru=True,
  aciklama="Otomasyondan sonraki bu adıma Endüstri 3,5 (küreselleşme) denir (s. 12).")
a("u1k2", "Endüstri 4.0", "dy", ifade="Endüstri 4.0 gelecekte yaşanacak bir devrimdir, bugün yoktur.", dogru=False,
  duzeltme="Endüstri 4.0 bugünü anlatır; gelecek Endüstri 5.0'dır.",
  aciklama="Kitapta Endüstri 4.0 \"bugün\", 5.0 \"gelecek\" diye geçer (s. 12).")
a("u1k2", "Yeni Meslekler", "secim", soru="Endüstriyel gelişmelerin mesleklere etkisi için hangisi doğrudur?",
  secenekler=["Hiçbir meslek değişmemiştir", "Bütün meslekler ortadan kalkmıştır", "Bazı meslekler yok olmuş, yenileri ortaya çıkmıştır", "Sadece çiftçilik kalmıştır"], dogru=2,
  aciklama="Yok olan mesleklerin yerine Dijital Terzi gibi yeni meslekler çıktı (s. 12).")

# --- Konu 3: Tasarım ve Tasarım Dalları (s. 13–14)
a("u1k3", "Tasarım", "dy", ifade="Tasarımın en önemli özelliği planlamadır.", dogru=True,
  aciklama="Planlamanın olduğu her yerde bir tasarımdan söz edilebilir (s. 13).")
a("u1k3", "Endüstriyel Tasarım", "dytablo", soru="Ürün endüstriyel tasarıma giriyorsa D, girmiyorsa Y seç.", ifadeler=[
  {"s": "Tencere", "d": True}, {"s": "Okul afişi", "d": False}, {"s": "Sandalye", "d": True}, {"s": "Park düzenlemesi", "d": False}],
  aciklama="Seri üretilen 3 boyutlu eşyalar endüstriyel tasarımdır; afiş grafik, park çevre tasarımıdır (s. 13–14).")
a("u1k3", "Grafik Tasarım", "secim", soru="Aşağıdakilerden hangisi grafik tasarımın alanına girmez?",
  secenekler=["Broşür", "Uyarı işareti", "Kitap kapağı", "Bina"], dogru=3,
  aciklama="Bina mimari-çevre tasarımıdır; diğerleri okunan ve izlenen görüntülerdir (s. 14).")
a("u1k3", "Mimari-Çevre Tasarımı", "bosluk", havuz=["grafik", "seramik"], cumleler=[
  {"c": "Bina, peyzaj ve iç mekân ___ tasarımının alanıdır.", "cevap": "çevre"},
  {"c": "Seri üretime uygun ürün tasarlama işine ___ tasarım denir.", "cevap": "endüstriyel"},
  {"c": "Tasarımın en önemli özelliği ___ yapmaktır.", "cevap": "planlama"}],
  aciklama="Çevre tasarımı yaşadığımız yerlerle, endüstriyel tasarım seri üretimle ilgilidir (s. 13–14).")
a("u1k3", "Tasarımın Unsurları", "secim", soru="Tasarımın unsurlarıyla ilgili aşağıdakiler verilmiştir.",
  onculler=["Ürünün fiyatı", "Renk", "Doku"], kok="Bunlardan hangileri tasarımın unsurlarındandır?", secenekler=ONC, dogru=2,
  aciklama="Renk ve doku duyularla algılanan unsurlardır; fiyat değildir (s. 13).")
a("u1k3", "Ürün Tasarımı ve Tercih", "dy", ifade="Teknik olarak aynı kalitedeki iki üründen birini seçerken tasarımın hiçbir rolü yoktur.", dogru=False,
  duzeltme="Ürün tasarımı, aynı kalitedeki iki ürünün seçiminde önemli rol oynar.",
  aciklama="Bazen tek başına tasarım müşterinin seçimini belirler (s. 13).")

# --- Konu 4: Teknoloji-Tasarım İlişkisi ve STEAM (s. 15–17 + program)
a("u1k4", "Teknoloji-Tasarım İlişkisi", "dy", ifade="Teknoloji ve tasarım sürecinin bir sonu vardır.", dogru=False,
  duzeltme="Teknoloji ve tasarım sürecinin sonu yoktur; insanlar hep daha iyisini arar.",
  aciklama="İhtiyaçlar değiştikçe araç-gereçler de değişir; süreç bitmez (s. 15).")
a("u1k4", "Teknolojinin Faydaları", "dytablo", soru="Teknolojinin faydalarına D, zararlarına Y seç.", ifadeler=[
  {"s": "Teşhis ve tedavi süresinin kısalması", "d": True}, {"s": "Küresel ısınmanın artması", "d": False},
  {"s": "Bilgiye kolay ulaşmak", "d": True}, {"s": "Yüz yüze iletişimin azalması", "d": False}],
  aciklama="Tıp ve bilgiye erişim faydadır; küresel ısınma ve az iletişim zarardır (s. 15).")
a("u1k4", "Teknolojinin Zararları", "secim", soru="Aşağıdakilerden hangisi teknolojinin zararlarından biridir?",
  secenekler=["Ulaşımın gelişmesi", "Matbaanın gelişmesi", "Eğitimin kolaylaşması", "Birçok insanın işsiz kalması"], dogru=3,
  aciklama="Üretim makinelere geçince birçok insan işsiz kaldı (s. 15).")
a("u1k4", "Sorun ve Çözüm", "eslestir", soru="Sorunları onlar için üretilmiş teknolojilerle eşleştir.", ciftler=[
  {"sol": "Çamaşırların kirlenmesi", "sag": "Çamaşır makinesi"},
  {"sol": "Uzaktaki küçük şeyleri görememek", "sag": "Mikroskop"},
  {"sol": "Kırışık giysiler", "sag": "Ütü"}],
  aciklama="Her teknoloji bir soruna çözüm olarak üretilmiştir (s. 15–16).")
a("u1k4", "STEAM", "kisa", soru="Bilim, teknoloji, mühendislik, sanat ve matematiği birlikte kullanan öğrenme yaklaşımının kısa adı nedir?", yanit="STEAM",
  kabul=["steam"], aciklama="STEAM, beş alanın İngilizce baş harflerinden oluşur (program).")
a("u1k4", "Ölçütle Değerlendirme", "secim", soru="Programa göre iki ambalajı karşılaştırırken hangisi ölçüt olarak kullanılabilir?",
  secenekler=["Ambalajın rengi", "Geri dönüşüm oranı", "Ambalajı kimin aldığı", "Ambalajın satıldığı gün"], dogru=1,
  aciklama="Programdaki ölçütler: enerji tüketimi, çevresel etki, geri dönüşüm oranı (program).")
a("u1k4", "Aynı İşlev, Farklı Tasarım", "dy", ifade="Aynı işi yapan farklı tasarımdaki ürünler, yaratıcılık ve hayal gücü gelişmiş kişilerin eseridir.", dogru=True,
  aciklama="Farklı görünen ama aynı işi yapan ürünler yaratıcılığın eseridir (s. 17).")

# --- Konu 5: Ülkemizde ve Dünyada Teknoloji (s. 18–19)
a("u1k5", "Teknoloji Üreten Ülkeler", "eslestir", soru="Ülke gruplarını özellikleriyle eşleştir.", ciftler=[
  {"sol": "Teknoloji üretenler", "sag": "Dünyanın teknoloji ihtiyacını karşılar"},
  {"sol": "Teknoloji kullananlar", "sag": "Teknolojiyi satın alıp kullanır"},
  {"sol": "İkisinin de dışında kalanlar", "sag": "Teknolojiden kopuktur"}],
  aciklama="Bilim ve teknoloji açısından ülkeler üç gruba ayrılır (s. 18).")
a("u1k5", "Ar-Ge", "kisa", soru="Kitaba göre \"parayı bilgiye, yenilik bilgiyi paraya döndüren süreç\" nedir?", yanit="Ar-Ge",
  kabul=["arge", "araştırma geliştirme", "araştırma-geliştirme"], aciklama="Ar-Ge, araştırma ve geliştirme demektir (s. 18).")
a("u1k5", "Güney Kore Örneği", "secim", soru="Güney Kore ile ilgili aşağıdaki bilgiler verilmiştir.",
  onculler=["Teknolojiyi yalnızca dışarıdan satın aldı.", "Ar-Ge çalışmalarına önem verdi.", "Üniversitelerini sanayiyle bütünleştirdi."],
  kok="Bu bilgilerden hangileri kitaba göre doğrudur?", secenekler=ONC, dogru=2,
  aciklama="Güney Kore Ar-Ge'ye ve eğitime önem verdi, teknolojiyi geliştirip sattı (s. 18).")
a("u1k5", "TÜBİTAK", "dy", ifade="TÜBİTAK 1963 yılında kurulmuştur.", dogru=True,
  aciklama="TÜBİTAK, üniversiteler dışındaki ilk bilim kurumu olarak 1963'te kuruldu (s. 19).")
a("u1k5", "Türkiye Araştırma Alanı", "secim", soru="Aşağıdakilerden hangisi Türkiye Araştırma Alanı'ndaki gruplardan biri değildir?",
  secenekler=["Kamu kuruluşları", "Özel sektör", "Üniversiteler", "Spor kulüpleri"], dogru=3,
  aciklama="Dört grup: kamu kuruluşları, özel sektör, üniversiteler ve STK'lar (s. 19).")
a("u1k5", "Teknolojinin Dışında Kalanlar", "dy", ifade="Teknolojinin dışında kalan ülkeler dünyaya en çok teknoloji satan ülkelerdir.", dogru=False,
  duzeltme="Bu ülkeler teknolojik olarak kopuktur; ne yenilik yapar ne yabancı teknolojiyi benimser.",
  aciklama="Dünyaya teknoloji satanlar, teknoloji üreten ülkelerdir (s. 18).")

# --- Konu 6: Yeni Teknolojiler 1 (s. 21–22)
a("u1k6", "Yapay Zekâ", "eslestir", soru="Teknolojileri anlamlarıyla eşleştir.", ciftler=[
  {"sol": "Yapay zekâ", "sag": "Kendi başına düşünen ve öğrenen makine"},
  {"sol": "Büyük veri", "sag": "Çok veriyi anlamlı hâle getirmek"},
  {"sol": "Bulut bilişim", "sag": "Bilgiye internetle her yerden ulaşmak"},
  {"sol": "Artırılmış gerçeklik", "sag": "Gerçek görüntünün üstüne sanal nesne"}],
  aciklama="Bunlar son yıllarda hayatımıza giren teknolojilerdir (s. 21–22).")
a("u1k6", "Büyük Veri", "dy", ifade="Büyük veri, sadece diskte çok yer kaplayan veri demektir.", dogru=False,
  duzeltme="Büyük veri, farklı kaynaklardan gelen verilerin anlamlı ve işlenebilir hâle getirilmesidir.",
  aciklama="Adı öyle düşündürür ama tam olarak öyle değildir (s. 21).")
a("u1k6", "Artırılmış Gerçeklik", "secim", soru="Telefonla odaya bakıp almak istediğin koltuğun odada nasıl duracağını görmek hangi teknolojiye örnektir?",
  secenekler=["Bulut bilişim", "Artırılmış gerçeklik", "Büyük veri", "Güneş çatısı"], dogru=1,
  aciklama="Sanal nesnenin gerçek görüntüye bindirilmesi artırılmış gerçekliktir (s. 21).")
a("u1k6", "Giyilebilir Teknoloji", "dytablo", soru="Giyilebilir teknoloji olanlara D, olmayanlara Y seç.", ifadeler=[
  {"s": "Akıllı saat", "d": True}, {"s": "Sanal gerçeklik gözlüğü", "d": True}, {"s": "Buzdolabı", "d": False}, {"s": "Güneş çatısı", "d": False}],
  aciklama="Üzerimizde taşıdığımız akıllı saat ve gözlük giyilebilirdir (s. 22).")
a("u1k6", "Bulut Bilişim", "bosluk", havuz=["drone", "nano"], cumleler=[
  {"c": "Bilgiye internetle istenen yerde ulaşmayı ___ bilişim sağlar.", "cevap": "bulut"},
  {"c": "Kendi başına düşünüp öğrenen makine yetisine yapay ___ denir.", "cevap": "zekâ"},
  {"c": "Akıllı saat ___ teknolojiye örnektir.", "cevap": "giyilebilir"}],
  aciklama="Bulut, yapay zekâ ve giyilebilir teknoloji yeni teknolojilerdir (s. 21–22).")
a("u1k6", "Yapay Zekâ", "dy", ifade="Yapay zekâ fikrinin temelinde insanlar gibi öğrenebilen makineler yapma düşüncesi vardır.", dogru=True,
  aciklama="Düşünebilen ve öğrenebilen makineler yapmak temel fikirdir (s. 21).")

# --- Konu 7: Yeni Teknolojiler 2 (s. 21–22)
a("u1k7", "Drone", "kisa", soru="İnsansız hava araçlarına verilen, İngilizcede \"erkek arı\" anlamına gelen ad nedir?", yanit="drone",
  kabul=["dron", "insansız hava aracı"], aciklama="Drone günümüzde insansız hava aracı anlamında kullanılır (s. 21).")
a("u1k7", "Güneş Çatıları", "dy", ifade="Güneş çatıları normal bir çatı gibi görünür ama elektrik üretir.", dogru=True,
  aciklama="Güneş çatıları güneş enerjisinden elektrik üretir (s. 21).")
a("u1k7", "Nano Cihazlar", "secim", soru="Aşağıdakilerden hangisi nano cihazlara örnektir?",
  secenekler=["Drone", "Karbon nanotüp", "Akıllı saat", "Uçan taksi"], dogru=1,
  aciklama="Sensörler, karbon nanotüpler, nano güneş pilleri nano cihazlardır (s. 21).")
a("u1k7", "Sürücüsüz Araç", "dy", ifade="Sürücüsüz araçlar sürücü olmadan kendi kendine yol alabilir.", dogru=True,
  aciklama="Bu araçların denemeleri 2008'de başladı (s. 22).")
a("u1k7", "Nesnelerin İnterneti", "secim", soru="İnternete bağlı bir giysinin veri göndermesi hangisine örnektir?",
  secenekler=["Endüstri 1.0", "Grafik tasarım", "Keşif", "Nesnelerin interneti"], dogru=3,
  aciklama="Kitap \"interneti nesneler kullanacak\" der: giysiler bile internete bağlanır (s. 22).")
a("u1k7", "Yakın Gelecek Teknolojileri", "dytablo", soru="Kitabın yakın gelecek örneklerinden olanlara D, olmayanlara Y seç.", ifadeler=[
  {"s": "Uçan taksi", "d": True}, {"s": "3 boyutlu yazıcıyla ev yapmak", "d": True}, {"s": "Buhar makinesi", "d": False}, {"s": "Ev robotları", "d": True}],
  aciklama="Uçan taksi, 3B yazıcıyla ev ve ev robotu yakın gelecek örneklerindendir; buhar makinesi eskidir (s. 22).")

H.yaz()
