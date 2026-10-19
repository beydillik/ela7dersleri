import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from ortak import Havuz, ONC
H = Havuz("bil1", 4, "b4"); a = H.add

# --- Konu 1: Bilgisayar Destekli Tasarım (s. 58–60)
a("u4k1", "Bilgisayar Destekli Tasarım", "kisa", soru="Üretilecek bir parçanın önce bilgisayar ortamında oluşturulmasına ne denir? (Kısaltmasıyla yazabilirsin.)",
  yanit="bilgisayar destekli tasarım", kabul=["bdt", "bilgisayar destekli tasarim"],
  aciklama="Parçanın önce bilgisayarda oluşturulması bilgisayar destekli tasarımdır (s. 59).")
a("u4k1", "Bilgi Çağı", "dy", ifade="21. yüzyıl bilgi çağı olarak da adlandırılır.", dogru=True,
  aciklama="21. yüzyılda bilgiye ulaşma şekli ve hızı değişti (s. 59).")
a("u4k1", "Simülasyon", "secim", soru="Bir binanın depreme dayanımı inşa edilmeden önce bilgisayarda deneniyor. Bu işlem hangisidir?",
  secenekler=["Simülasyon", "Arşivleme", "Konstrüksiyon", "Montaj"], dogru=0,
  aciklama="Bilgisayar yoluyla modelleyip denemek simülasyondur (s. 60).")
a("u4k1", "BDT'nin Yararları", "secim", soru="Bilgisayar destekli tasarımın yararları ile ilgili bilgiler verilmiştir.",
  onculler=["Kısa sürede daha çok seçenek üretilir.", "İnsandan kaynaklanan hatalar en aza iner.", "Bilgiye erişim süresi kısalır."],
  kok="Bu bilgilerden hangileri doğrudur?", secenekler=ONC, dogru=3,
  aciklama="Üçü de kitapta sayılan yararlardandır (s. 60).")
a("u4k1", "Konstrüksiyon", "bosluk", havuz=["orijin", "animasyon"], cumleler=[
  {"c": "Bir yapıyı taşıyan ve bir araya gelip yapıyı oluşturan öğelerin bütününe ___ denir.", "cevap": "konstrüksiyon"},
  {"c": "Bina yapılmadan bilgisayarda denenmesine ___ denir.", "cevap": "simülasyon"},
  {"c": "Akıllı binalarda işlerin kendiliğinden yönetilmesine ___ denir.", "cevap": "otomasyon"}],
  aciklama="Konstrüksiyon yapının iskeleti, simülasyon bilgisayarda deneme, otomasyon kendiliğinden yönetimdir (s. 59–60).")
a("u4k1", "Yapım Sürecinin Takibi", "dytablo", soru="Yapım sürecinde bilgisayarla yapılan bir işse D, değilse Y seç.", ifadeler=[
  {"s": "Malzeme stok kontrolü", "d": True}, {"s": "Maliyet analizi", "d": True}, {"s": "Tuğlaları elle taşımak", "d": False}, {"s": "İşçi takibi", "d": True}],
  aciklama="Stok, maliyet ve işçi takibi bilgisayarla yapılır (s. 60).")
a("u4k1", "Kullanım Alanları", "dy", ifade="Bilgisayar destekli tasarım yalnızca bina tasarımında kullanılır.", dogru=False,
  duzeltme="Sinema efektleri, oyunlar, çizgi filmler ve şehir planlamada da kullanılır.",
  aciklama="BDT birçok alanda kullanılır (s. 60).")

# --- Konu 2: Boyutlar ve Koordinat Sistemi (s. 61–62)
a("u4k2", "Boyut", "dy", ifade="Nokta boyutsuz olarak kabul edilir.", dogru=True,
  aciklama="Kitaba göre nokta boyutsuzdur (s. 61).")
a("u4k2", "Üç Boyut", "eslestir", soru="Şekli boyut sayısıyla eşleştir.", ciftler=[
  {"sol": "Çizgi", "sag": "Tek boyutlu"},
  {"sol": "Kare", "sag": "İki boyutlu"},
  {"sol": "Küp", "sag": "Üç boyutlu"}],
  aciklama="Çizgide uzunluk; karede en-boy; küpte en-boy-derinlik vardır (s. 61).")
a("u4k2", "İki Boyut", "secim", soru="Hangisinin alanı bulunur ama hacmi bulunmaz?",
  secenekler=["Küp", "Dikdörtgen", "Üçgen piramit", "Dikdörtgenler prizması"], dogru=1,
  aciklama="İki boyutlu şekillerin alanı bulunur; dikdörtgen iki boyutludur (s. 61).")
a("u4k2", "Koordinat Sistemi", "eslestir", soru="Eksenleri adlarıyla eşleştir.", ciftler=[
  {"sol": "x ekseni", "sag": "Apsis (yatay)"},
  {"sol": "y ekseni", "sag": "Ordinat (dikey)"},
  {"sol": "z ekseni", "sag": "Kot (düşey)"}],
  aciklama="x apsis, y ordinat, z kot adını alır (s. 62).")
a("u4k2", "Orijin", "kisa", soru="Koordinat eksenlerinin kesiştiği noktaya ne denir?", yanit="orijin", kabul=["koordinat merkezi"],
  aciklama="Eksenlerin kesim noktası orijin ya da koordinat merkezidir (s. 62).")
a("u4k2", "Koordinat", "secim", soru="Koordinat ile ilgili bilgiler verilmiştir.",
  onculler=["Yalnızca üç boyutlu çizimde kullanılır.", "Bir noktanın konumunu belirler.", "Harita çiziminde kullanılır."],
  kok="Bu bilgilerden hangileri doğrudur?", secenekler=ONC, dogru=2,
  aciklama="Koordinat konum belirler ve haritada kullanılır; iki boyutlu çizimde de vardır (s. 62).")
a("u4k2", "Tek Boyut", "bosluk", havuz=["renk", "ses"], cumleler=[
  {"c": "Çizginin yalnızca ___ boyutu vardır.", "cevap": "uzunluk"},
  {"c": "Üç boyutlu cisimlerde ___ bulunur.", "cevap": "hacim"},
  {"c": "İki boyutlu şekillerin ___ bulunur.", "cevap": "alanı"}],
  aciklama="Çizgi uzunluk; iki boyut alan; üç boyut hacim (s. 61).")

# --- Konu 3: Taslaktan 2B ve 3B Çizime (s. 62–63 + program)
a("u4k3", "CAD Programları", "eslestir", soru="Programları kitaptaki kullanım amacıyla eşleştir.", ciftler=[
  {"sol": "AutoCAD", "sag": "Hassas teknik tasarım (CAD)"},
  {"sol": "Photoshop", "sag": "Resim ve grafik işleme"},
  {"sol": "Tinkercad", "sag": "Kurulumsuz, çevrimiçi 2B-3B çizim"},
  {"sol": "Canva", "sag": "Görsel iletişim tasarımı"}],
  aciklama="Her programın kendi kullanım amacı vardır (s. 62).")
a("u4k3", "İki Boyutlu Çizim", "kisa", soru="Kitaba göre ofis programları içinde yer alan ve 2B çizim yapılabilen program hangisidir?", yanit="paint",
  aciklama="Ofis programları içindeki Paint ile 2B çizim yapılır (s. 62).")
a("u4k3", "Tinkercad", "dy", ifade="Tinkercad kullanmak için bilgisayara kurulum yapmak gerekir.", dogru=False,
  duzeltme="Tinkercad kurulum gerektirmeden çevrimiçi çalışır.",
  aciklama="Tinkercad'de yapılan çizimler 3D yazıcıda da yazdırılabilir (s. 62).")
a("u4k3", "Üç Boyutlu Çizim", "dytablo", soru="Üç boyutlu nesne ise D, iki boyutlu şekil ise Y seç.", ifadeler=[
  {"s": "Küre", "d": True}, {"s": "Elips", "d": False}, {"s": "Piramit", "d": True}, {"s": "Çokgen", "d": False}, {"s": "Küp", "d": True}],
  aciklama="Piramit, küp, küre üç boyutlu; çokgen, elips, dikdörtgen, daire iki boyutludur (program).")
a("u4k3", "Işık, Doku ve Malzeme", "secim", soru="Bilgisayarda çizilen 3B bir nesnenin daha gerçek görünmesi için hangileri kullanılır?",
  secenekler=["Ses, müzik, video", "Işık, doku, malzeme", "x, y, z eksenleri", "Başlık, metin, slayt"], dogru=1,
  aciklama="Işık, doku ve malzeme özellikleri 3B nesnenin algısını değiştirir (program).")
a("u4k3", "Taslak Çizim", "secim", soru="Bir tasarımın bilgisayarda ürüne dönüştürülme sırası hangisinde doğru verilmiştir?",
  secenekler=["3B çizim → taslak → 2B çizim", "Taslak çizim → bilgisayarda 2B → 3B", "2B çizim → 3B → taslak", "Taslak → 3B yazıcı → 2B"], dogru=1,
  aciklama="Önce elle taslak, sonra bilgisayarda 2B ve 3B çizim yapılır (s. 63; program).")
a("u4k3", "Resim ve Grafik Programları", "dy", ifade="Kitapta Photoshop, Corel ve Picasa resim ve grafik işlemek için hazırlanmış programlar arasında sayılır.", dogru=True,
  aciklama="Bu programlar resim ve grafik işlemek içindir (s. 62).")

# --- Konu 4: Çoklu Ortam ve Sunu Hazırlama (s. 64–68)
a("u4k4", "Çoklu Ortam", "kisa", soru="Bir içeriğin ses, görüntü, grafik, animasyon ve müzikle sunulmasına ne denir? (İki kelime)", yanit="çoklu ortam", kabul=["multimedya"],
  aciklama="Çoklu ortamın diğer adı multimedyadır (s. 64).")
a("u4k4", "Çoklu Ortam Araçları", "dytablo", soru="Çoklu ortam aracıysa D, değilse Y seç.", ifadeler=[
  {"s": "Metin", "d": True}, {"s": "Video", "d": True}, {"s": "Gönye", "d": False}, {"s": "Animasyon", "d": True}],
  aciklama="Metin, ses, video, fotoğraf, animasyon ve görseller çoklu ortam araçlarıdır (s. 64).")
a("u4k4", "Sunu", "dy", ifade="Sunu, metin, resim ve grafiklerden düzenli şekilde hazırlanan slaytlar grubudur.", dogru=True,
  aciklama="Kitapta sunu PowerPoint ile hazırlanır (s. 65).")
a("u4k4", "Sunu Hazırlama Basamakları", "bosluk", havuz=["montaj", "orijin"], cumleler=[
  {"c": "Sunu hazırlamanın ilk basamağı konu ___ basamağıdır.", "cevap": "tespiti"},
  {"c": "Sunu hazırlamanın son basamağı değerlendirme ve ___ basamağıdır.", "cevap": "sunma"},
  {"c": "Konu belirlendikten sonra konu ___.", "cevap": "araştırılır"}],
  aciklama="Konu tespitiyle başlanır, araştırılır; en sonda değerlendirilip sunulur (s. 64).")
a("u4k4", "Tutarlılık ve Gereksizlik", "secim", soru="Sunuda konuyla ilgisi olmayan resim, ses ve kelimelerin çıkarılması hangi ilkedir?",
  secenekler=["Kişiselleştirme", "Ön alıştırma", "Tutarlılık", "Resim"], dogru=2,
  aciklama="Tutarlılık ilkesi gereksiz öğeleri çıkarmayı söyler (s. 64; açıklama kitap dışı).")
a("u4k4", "Parçalara Bölme ve Dikkat Çekme", "eslestir", soru="İlkeleri anlamlarıyla eşleştir.", ciftler=[
  {"sol": "Parçalara bölme", "sag": "Uzun konuyu küçük bölümlere ayırmak"},
  {"sol": "Dikkat çekme", "sag": "Önemli noktaları belirginleştirmek"},
  {"sol": "Tutarlılık", "sag": "İlgisiz görsel ve sesleri çıkarmak"}],
  aciklama="Her ilke sunuyu daha kolay izlenir yapar (s. 64; açıklama kitap dışı).")
a("u4k4", "Sunum İlkeleri", "secim", soru="Kitapta bilgisayarla sunu hazırlarken dikkat edilecek ilke grupları verilmiştir.",
  onculler=["Konu dışı işlemleri azaltma", "Renkleri karıştırma", "Slayt sayısını artırma"],
  kok="Bunlardan hangileri kitaptaki ilke gruplarındandır?", secenekler=ONC, dogru=0,
  aciklama="Gruplar: konu dışı işlemleri azaltma, temel süreçleri yönetme, üretici süreçleri geliştirme (s. 64).")

H.yaz()
