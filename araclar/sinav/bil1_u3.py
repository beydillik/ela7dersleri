import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from ortak import Havuz, ONC
H = Havuz("bil1", 3, "b3"); a = H.add

# --- Konu 1: Tasarım Sürecinin Aşamaları (s. 32–34 + program)
a("u3k1", "Beş Temel Basamak", "bosluk", havuz=["sunum", "afiş"], cumleler=[
  {"c": "Tasarımın ilk basamağı problemi ___ basamağıdır.", "cevap": "tanımlama"},
  {"c": "İkinci basamakta önceki araştırmalardan bilgi ___.", "cevap": "toplanır"},
  {"c": "Son basamak, tasarımın hazır hâle geldiği ___ basamağıdır.", "cevap": "uygulama"}],
  aciklama="Basamaklar: problemi tanımlama, bilgi toplama, yaratıcılık-buluş, çözüm bulma, uygulama (s. 33).")
a("u3k1", "Yaratıcılık ve Buluş Süreci", "dy", ifade="Kitaba göre tasarımın en önemli basamağı uygulamadır.", dogru=False,
  duzeltme="En önemli basamak yaratıcılık ve buluş sürecidir.",
  aciklama="Hipotezin geliştirildiği yaratıcılık ve buluş süreci en önemli aşamadır (s. 33).")
a("u3k1", "Görselleştirme", "secim", soru="Görselleştirme ile ilgili aşağıdaki bilgiler verilmiştir.",
  onculler=["Çizerek yapılabilir.", "Maket yapılarak yapılabilir.", "Bilgisayar programlarıyla yapılabilir."],
  kok="Bu bilgilerden hangileri doğrudur?", secenekler=ONC, dogru=3,
  aciklama="Görselleştirme yazarak, çizerek, maketle ya da bilgisayarla yapılabilir (s. 34).")
a("u3k1", "Değerlendirme ve Sunma", "secim", soru="Tasarım hangi açılardan değerlendirilmez?",
  secenekler=["Özgünlük", "İşlevsellik", "Tasarımcının yaşı", "Sürdürülebilirlik"], dogru=2,
  aciklama="Özgünlük, işlevsellik, yapılabilirlik ve sürdürülebilirlik ölçütleridir (s. 34).")
a("u3k1", "Problem Odaklı Düşünme", "kisa", soru="Bir problemi küçük parçalarına ayırarak incelemeye ne tür düşünme denir? (İki kelime: ___ odaklı düşünme)",
  yanit="problem", kabul=["problem odaklı", "problem odaklı düşünme"],
  aciklama="Problemi parçalara ayırmak problem odaklı düşünmedir (program).")
a("u3k1", "Tasarım Süreci", "eslestir", soru="Aşamaları yapılan işle eşleştir.", ciftler=[
  {"sol": "Problem tanımlama", "sag": "Rahatsız eden durumu belirlemek"},
  {"sol": "Görselleştirme", "sag": "Fikri çizerek göstermek"},
  {"sol": "Planlama", "sag": "Üretimin adımlarını netleştirmek"},
  {"sol": "Değerlendirme ve sunma", "sag": "Ürünü incelemek ve anlatmak"}],
  aciklama="Her aşamanın kendi işi vardır (s. 34).")

# --- Konu 2: Teknik Resim ve Perspektif (s. 35–38)
a("u3k2", "Teknik Resim", "dy", ifade="Teknik resmi yalnızca o dili konuşan mühendisler anlayabilir.", dogru=False,
  duzeltme="Teknik resim dile bakılmadan dünyanın her yerinde kullanılabilir.",
  aciklama="Teknik resim mühendislerin ortak dilidir (s. 35).")
a("u3k2", "Perspektif", "secim", soru="Resimde yolun iki yanındaki direkler uzaklaştıkça küçülüyor. Burada hangi teknik kullanılmıştır?",
  secenekler=["Üç görünüş", "Perspektif", "Teknik rapor", "Beyin fırtınası"], dogru=1,
  aciklama="Perspektifte gözden uzaklaşan her şey küçük görünür (s. 35).")
a("u3k2", "Kaçma Noktası", "bosluk", havuz=["orijin", "taslak"], cumleler=[
  {"c": "Perspektif çiziminde önce ___ çizgisi çizilir.", "cevap": "ufuk"},
  {"c": "Paralel çizgilerin birleşiyor gibi göründüğü noktaya ___ noktası denir.", "cevap": "kaçma"},
  {"c": "Gözden uzaklaşan her şey ___ görünür.", "cevap": "küçük"}],
  aciklama="Ufuk çizgisi, kaçma noktası ve küçülme perspektifin temelidir (s. 35–36).")
a("u3k2", "Üç Görünüş", "dytablo", soru="Üç görünüşten biriyse D, değilse Y seç.", ifadeler=[
  {"s": "Önden görünüş", "d": True}, {"s": "Üstten görünüş", "d": True}, {"s": "İçten görünüş", "d": False}, {"s": "Yandan görünüş", "d": True}],
  aciklama="Üretim için ön, üst ve yan görünüşler çizilir (s. 37).")
a("u3k2", "Teknik Çizim", "kisa", soru="Teknik çizim yapan kişiye ne denir? (İki kelime)", yanit="teknik ressam", kabul=["ressam"],
  aciklama="Teknik çizim yapan kişilere teknik ressam denir (s. 35).")
a("u3k2", "Ufuk Çizgisi", "secim", soru="Göz hizamızdan geçen yatay çizgiye ne denir?",
  secenekler=["Kaçma noktası", "Kesit çizgisi", "Ölçü oku", "Ufuk çizgisi"], dogru=3,
  aciklama="Ufuk çizgisi göz hizasından geçen yatay çizgidir (s. 36).")

# --- Konu 3: Problem Tanımlama ve Fikir Geliştirme (s. 34, 39–40 + program)
a("u3k3", "Problem", "secim", soru="Bir durumun problem sayılması için gereken koşullarla ilgili bilgiler verilmiştir.",
  onculler=["Kişide rahatsızlık uyandırmalı.", "Birden fazla çözüm yolu olmalı.", "Hiç kimse onu fark etmemeli."],
  kok="Bu bilgilerden hangileri doğrudur?", secenekler=ONC, dogru=1,
  aciklama="Problem rahatsızlık uyandırmalı ve birden çok çözümü olmalıdır (s. 34).")
a("u3k3", "Hipotez", "kisa", soru="Araştırmacının kendi görüşleriyle ortaya koyduğu geçici çözüme ne denir?", yanit="hipotez",
  aciklama="Geçici çözüm hipotezdir (s. 40).")
a("u3k3", "Beyin Fırtınası", "dy", ifade="Beyin fırtınasında söylenen fikirler hemen eleştirilir.", dogru=False,
  duzeltme="Beyin fırtınasında fikirler eleştirilmez; her fikir yazılır.",
  aciklama="Eleştirilme korkusu olmadan çok fikir üretilir (program).")
a("u3k3", "Balık Kılçığı Diyagramı", "eslestir", soru="Yöntemleri işleriyle eşleştir.", ciftler=[
  {"sol": "Beyin fırtınası", "sag": "Çok sayıda fikir üretir"},
  {"sol": "Balık kılçığı diyagramı", "sag": "Problemin nedenlerini bulur"},
  {"sol": "Karar diyagramı", "sag": "Seçenekleri dallar hâlinde gösterir"},
  {"sol": "Kontrol diyagramı", "sag": "Ölçümün sınırlar içinde olup olmadığını gösterir"}],
  aciklama="Programdaki dört fikir geliştirme yönteminin her biri farklı işe yarar (program).")
a("u3k3", "Kontrol Diyagramı", "secim", soru="Kontrol diyagramında bir ölçüm alt sınırın altına düştü. Bu ne anlama gelir?",
  secenekler=["Her şey yolunda", "Bir sorun olabilir", "Grafik bitti", "Yeni fikir gerekmez"], dogru=1,
  aciklama="Sınırların dışına çıkan ölçüm bir sorun olduğunu gösterir (program).")
a("u3k3", "Tasarım Problemi", "dy", ifade="Tasarım problemini seçtikten sonra o probleme bugünkü çözümler araştırılır.", dogru=True,
  aciklama="Mevcut çözümler araştırılır ve eksik yanları belirlenir (s. 39).")
a("u3k3", "Karar Diyagramı", "secim", soru="Tasarımcı 'Lamba pilli mi, fişli mi olsun?' sorusunun sonuçlarını dallar hâlinde çizdi. Hangi yöntemi kullandı?",
  secenekler=["Karar diyagramı", "Balık kılçığı diyagramı", "Perspektif", "Antropometri"], dogru=0,
  aciklama="Seçenekleri ve sonuçlarını dallarla gösteren şema karar diyagramıdır (program).")

# --- Konu 4: Bilimsel Araştırma Basamakları (s. 41)
a("u3k4", "Sorun", "dytablo", soru="Araştırılacak sorunun özelliği ise D, değilse Y seç.", ifadeler=[
  {"s": "Çözülebilir olmalı", "d": True}, {"s": "Güncel olmalı", "d": True}, {"s": "Belirsiz yazılmalı", "d": False}, {"s": "Özgün olmalı", "d": True}],
  aciklama="Sorun çözülebilir, önemli, özgün, güncel ve açık olmalıdır (s. 41).")
a("u3k4", "Güvenilir Veri", "secim", soru="Araştırmada toplanan verilerle ilgili aşağıdaki bilgiler verilmiştir.",
  onculler=["Güvenilir olmalıdır.", "Eksiksiz olmalıdır.", "Kaynağı önemli değildir."],
  kok="Bu bilgilerden hangileri doğrudur?", secenekler=ONC, dogru=1,
  aciklama="Veriler güvenilir ve eksiksiz olmalı; kaynakların güvenilir olmasına özen gösterilir (s. 41).")
a("u3k4", "Sunum", "eslestir", soru="Basamakları yapılan işle eşleştir.", ciftler=[
  {"sol": "Sorun", "sag": "Araştırılacak konuyu belirlemek"},
  {"sol": "Plan", "sag": "Amaca giden yolu yazmak"},
  {"sol": "Araştırma", "sag": "Kaynaklardan bilgi toplamak"},
  {"sol": "Sunum", "sag": "Sonuç ve önerileri anlatmak"}],
  aciklama="Her basamağın kendi işi vardır (s. 41).")
a("u3k4", "Plan", "dy", ifade="Araştırma planında ulaşılmak istenen amaç belirtilmelidir.", dogru=True,
  aciklama="Plan, amaca uygun bilgi sağlamak için izlenen bir kılavuzdur (s. 41).")
a("u3k4", "Değerlendirme", "secim", soru="Probleme en uygun çözüm yolunun seçildiği basamak hangisidir?",
  secenekler=["Sorun", "Plan", "Araştırma", "Değerlendirme"], dogru=3,
  aciklama="Değerlendirmede en uygun çözüm seçilir, veriler sınıflandırılır (s. 41).")
a("u3k4", "Araştırma", "bosluk", havuz=["prototip", "maket"], cumleler=[
  {"c": "Doğru toplanmış veriler ___ yola götürür.", "cevap": "doğru"},
  {"c": "Eksik toplanmış veriler ___ yola götürür.", "cevap": "yanlış"},
  {"c": "Bilgi kitaplardan, dergilerden ve ___ toplanabilir.", "cevap": "kurumlardan"}],
  aciklama="Veri toplama doğru yapılırsa doğru karar verilir (s. 41).")

# --- Konu 5: Ergonomi (s. 43–44)
a("u3k5", "Ergonomi", "kisa", soru="Yaşamın insana uygun hâle getirilmesine ne denir?", yanit="ergonomi",
  aciklama="Ergonomi yaşamın insana uygun hâle getirilmesidir (s. 44).")
a("u3k5", "Antropometri", "eslestir", soru="Bilim dallarını ilgi alanlarıyla eşleştir.", ciftler=[
  {"sol": "Fizyoloji", "sag": "Kas çalışması ve enerji"},
  {"sol": "Psikoloji", "sag": "Renk ve düzenle hoş ortam"},
  {"sol": "Sosyoloji", "sag": "Toplumsal sorunlar"},
  {"sol": "Antropometri", "sag": "İnsanın vücut ölçüleri"}],
  aciklama="Dört bilim dalı ergonomiye farklı yönlerden yardım eder (s. 43).")
a("u3k5", "Ergonominin Konuları", "dytablo", soru="Ergonominin konusuysa D, değilse Y seç.", ifadeler=[
  {"s": "Gürültü", "d": True}, {"s": "Aydınlatma", "d": True}, {"s": "Reklam filmi", "d": False}, {"s": "Mola saatleri", "d": True}],
  aciklama="Gürültü, aydınlatma, ısı, titreşim ve mola saatleri ergonominin konularıdır (s. 43).")
a("u3k5", "Ergonomi", "secim", soru="Hangisi ergonominin amaçlarından biri değildir?",
  secenekler=["Aşırı zorlamayı önlemek", "Çalışanın sağlığını korumak", "Gereksiz hareketleri önlemek", "Ürünü daha süslü yapmak"], dogru=3,
  aciklama="Ergonomi sağlığı korur, zorlanmayı ve gereksiz hareketi önler (s. 43).")
a("u3k5", "Ergonomik Düzenleme", "dy", ifade="Kitaptaki örnekte tabakalar çalışanın önüne asılınca dönme hareketine gerek kalmamıştır.", dogru=True,
  aciklama="Tabakalar öne asılınca hareket israfı yok edilmiştir (s. 44).")
a("u3k5", "Psikoloji", "secim", soru="Çalışma odasında rahatlatıcı renkler ve düzenli bir yerleşim kullanıldı. Ergonomi burada hangi daldan yararlanmıştır?",
  secenekler=["Antropometri", "Psikoloji", "Fizyoloji", "Sosyoloji"], dogru=1,
  aciklama="Renk, şekil ve düzenle hoş ortam psikolojinin konusudur (s. 43).")

# --- Konu 6: Tasarım Geliştirme Kriterleri (s. 34, 42–46 + program)
a("u3k6", "Estetik", "eslestir", soru="Kriterleri sorularıyla eşleştir.", ciftler=[
  {"sol": "Ergonomik", "sag": "İnsana uygun mu?"},
  {"sol": "Estetik", "sag": "Göze güzel geliyor mu?"},
  {"sol": "İşlevsel", "sag": "İşe yarıyor mu?"},
  {"sol": "Yalın", "sag": "Sade ve anlaşılır mı?"}],
  aciklama="Her kriter tasarıma bir soru sorar (s. 45).")
a("u3k6", "Malzeme ve Maliyet", "secim", soru="Tasarımda kullanılacak malzemelerle ilgili aşağıdaki bilgiler verilmiştir.",
  onculler=["Kolay bulunabilmelidir.", "Dayanıklı olmalıdır.", "Geri dönüşüme uygun olmalıdır."],
  kok="Bu bilgilerden hangileri doğrudur?", secenekler=ONC, dogru=3,
  aciklama="Malzeme kolay bulunur, dayanıklı, ekonomik ve geri dönüşüme uygun olmalıdır (s. 45).")
a("u3k6", "Özgün-Yenilikçi", "dy", ifade="Özgün tasarım, benzerlerinin aynısı olan tasarımdır.", dogru=False,
  duzeltme="Özgün tasarım benzerlerinden ayrı ve üstündür.",
  aciklama="Özgün-yenilikçi tasarım bir buluş sonucu ortaya çıkar (s. 45).")
a("u3k6", "Sürdürülebilirlik", "secim", soru="Hangisi sürdürülebilir bir tasarım kararıdır?",
  secenekler=["Bir kez kullanılıp atılan tabak", "Tamir edilebilen sandalye", "Kısa sürede bozulan oyuncak", "Geri dönüşmeyen ambalaj"], dogru=1,
  aciklama="Uzun süre kullanılan, atık azaltan ürün geleceği de düşünür (s. 34; program).")
a("u3k6", "İşlevsel", "kisa", soru="Bir objenin kullanıldığı duruma göre işe yarar olmasına ne denir?", yanit="işlevsellik", kabul=["işlevsel", "islevsellik", "islevsel"],
  aciklama="İşlevsellik, objenin kullanıldığı duruma göre işe yaramasıdır (s. 45).")
a("u3k6", "Estetik", "bosluk", havuz=["titreşim", "ölçek"], cumleler=[
  {"c": "Sanatla, güzellikle ve tatla ilgilenen felsefe dalına ___ denir.", "cevap": "estetik"},
  {"c": "Karmaşık olmayan, sade tasarıma ___ tasarım denir.", "cevap": "yalın"},
  {"c": "Benzerlerinden ayrı ve üstün tasarım ___ tasarımdır.", "cevap": "özgün"}],
  aciklama="Estetik, yalın ve özgün tasarım geliştirme kriterleridir (s. 45).")

# --- Konu 7: Maket, Model ve Prototip (s. 42, 47–49)
a("u3k7", "Prototip", "eslestir", soru="Kavramları anlamlarıyla eşleştir.", ciftler=[
  {"sol": "Taslak", "sag": "Tasarımın ilk çizimi"},
  {"sol": "Maket", "sag": "Ölçekle küçültülmüş üç boyutlu kopya"},
  {"sol": "Prototip", "sag": "Üretimden önceki elle tutulur ilk örnek"},
  {"sol": "Model", "sag": "Bir sistemin basit örneği"}],
  aciklama="Her biri tasarımın farklı bir aşamasını gösterir (s. 42, 47).")
a("u3k7", "Model", "dy", ifade="Modeller her zaman aslından küçük yapılır.", dogru=False,
  duzeltme="Molekül modeli gibi bazı modeller aslından büyüktür.",
  aciklama="Güneş sistemi modeli küçük, molekül modeli büyüktür (s. 47).")
a("u3k7", "3D Yazıcı", "secim", soru="3D yazıcı ile ilgili aşağıdaki bilgiler verilmiştir.",
  onculler=["Nesneyi katman katman oluşturur.", "Yalnızca kâğıt kullanabilir.", "Bilgisayarda hazırlanan tasarımı basar."],
  kok="Bu bilgilerden hangileri doğrudur?", secenekler=["Yalnız I", "I ve II", "I ve III", "II ve III"], dogru=2,
  aciklama="3D yazıcı plastik, seramik, metal tozu kullanır; bilgisayardaki tasarımı katmanlarla basar (s. 47).")
a("u3k7", "Maket", "secim", soru="Maketin taslaktaki ürüne benzemesi için en çok neye dikkat edilmelidir?",
  secenekler=["Ölçülerde hata yapmamaya", "Pahalı boya kullanmaya", "Hızlı bitirmeye", "Büyük yapmaya"], dogru=0,
  aciklama="Maket belirli bir ölçekle yapılır; ölçülerde hata yapılmamalıdır (s. 47).")
a("u3k7", "Uygulama Takvimi", "bosluk", havuz=["broşür", "ufuk"], cumleler=[
  {"c": "Yapım aşamaları öncelik ___ göre belirlenir.", "cevap": "sırasına"},
  {"c": "Uygulama takvimi zaman ___ önler.", "cevap": "kaybını"},
  {"c": "Tasarım güvenlik ___ dikkat edilerek yapılır.", "cevap": "önlemlerine"}],
  aciklama="Sıra ve takvim işi kolaylaştırır; güvenlik her zaman önce gelir (s. 49).")
a("u3k7", "Taslak", "kisa", soru="Tasarım önerisinin ayrıntıları gösterilen ilk çizimine ne denir?", yanit="taslak",
  aciklama="Taslak önerinin ilk hâlinin çizimidir (s. 42).")

# --- Konu 8: İş Güvenliği ve Geri Dönüşüm (s. 50–51)
a("u3k8", "Öğretmen Gözetimi", "dy", ifade="Kesici ve delici araçlar öğretmen gözetiminde kullanılmalıdır.", dogru=True,
  aciklama="Tehlikeli araçlar kendi başına kullanılmaz (s. 50).")
a("u3k8", "İş Güvenliği", "dytablo", soru="Atölyede doğru davranışsa D, yanlışsa Y seç.", ifadeler=[
  {"s": "Aldığım malzemeyi yerine koyarım.", "d": True}, {"s": "Arkadaşımla şakalaşarak çalışırım.", "d": False},
  {"s": "Uyarı tabelalarına uyarım.", "d": True}, {"s": "Bozulan elektrikli aleti kendim tamir ederim.", "d": False}],
  aciklama="Tabelalara uyulur; şakalaşma kazaya yol açar, tamiri yetkililer yapar (s. 50).")
a("u3k8", "Geri Dönüşümün Faydaları", "secim", soru="Hangisi geri dönüşümün faydalarından biri değildir?",
  secenekler=["Atık miktarı azalır", "Doğal kaynaklar korunur", "Enerji tasarrufu sağlanır", "Çöp miktarı artar"], dogru=3,
  aciklama="Geri dönüşüm atığı azaltır, kaynakları korur, enerji tasarrufu sağlar (s. 51).")
a("u3k8", "Geri Dönüşüm", "kisa", soru="Atıkların işlenip yeniden ham madde olarak üretime katılmasına ne denir? (İki kelime)", yanit="geri dönüşüm", kabul=["geridönüşüm"],
  aciklama="Atıkların ikinci bir ham maddeye dönüştürülmesi geri dönüşümdür (s. 51).")
a("u3k8", "Kazaya Karşı Dikkat", "secim", soru="Atölyede bir arkadaşın elini kesti. Ne yapmalısın?",
  secenekler=["Hemen öğretmene haber vermeliyim", "Kimseye söylememeliyim", "Çalışmaya devam etmeliyim", "Kendim dikiş atmalıyım"], dogru=0,
  aciklama="Herhangi bir kaza ya da yaralanma hemen öğretmene bildirilir (s. 50).")
a("u3k8", "İkincil Kullanım", "eslestir", soru="Durumları kavramlarla eşleştir.", ciftler=[
  {"sol": "Boş kavanozu kalemlik yapmak", "sag": "İkincil kullanım"},
  {"sol": "Eski şişeleri eritip yeni şişe yapmak", "sag": "Geri dönüşüm"},
  {"sol": "Koruyucu gözlük takmak", "sag": "Kişisel korunma"}],
  aciklama="Ürünü başka işe kullanmak ikincil kullanım, ham maddeye dönüştürmek geri dönüşümdür (s. 50–51).")

# --- Konu 9: Değerlendirme, Tanıtım ve Sunum (s. 52–57)
a("u3k9", "Afiş", "dy", ifade="Afişteki mesaj 10 kelimeden uzun olursa okunma oranı artar.", dogru=False,
  duzeltme="Mesaj 5–6 kelime olmalı; 10 kelime ve üstünde okuma oranı düşer.",
  aciklama="Kısa mesaj gözden kaçmaz (s. 54).")
a("u3k9", "Göze ve Kulağa Hitap Eden Araçlar", "eslestir", soru="Tanıtım araçlarını türleriyle eşleştir.", ciftler=[
  {"sol": "Broşür", "sag": "Göze hitap eder"},
  {"sol": "Radyo", "sag": "Kulağa hitap eder"},
  {"sol": "Televizyon", "sag": "Hem göze hem kulağa hitap eder"}],
  aciklama="Tanıtım araçları üç şekilde sınıflandırılır (s. 53).")
a("u3k9", "Ürün Değerlendirme", "dytablo", soru="Değerlendirmede sorulan bir soruysa D, değilse Y seç.", ifadeler=[
  {"s": "Sorunu çözdü mü?", "d": True}, {"s": "Kullanıcı ihtiyaçlarını karşılıyor mu?", "d": True},
  {"s": "Tasarımcı kaç yaşında?", "d": False}, {"s": "Üretime uygun mu?", "d": True}],
  aciklama="Değerlendirme soruları tasarımın işe yarayıp yaramadığını ölçer (s. 52).")
a("u3k9", "Ürün Tanıtımı", "secim", soru="Pazarlamanın ilk ve en önemli adımı hangisidir?",
  secenekler=["Ürünü saklamak", "Fiyatı artırmak", "Tanıtım (görsel sunum)", "Maketi bozmak"], dogru=2,
  aciklama="Tanıtım, yani görsel sunum, pazarlamanın ilk ve en önemli adımıdır (s. 53).")
a("u3k9", "Yeniden Tasarım", "secim", soru="Değerlendirmede ürününün bir eksiği bulundu. Döngüsel tasarım sürecine göre ne yaparsın?",
  secenekler=["Eksikleri düzeltip tasarımı geliştiririm", "Tasarımı hemen satarım", "Tasarımı çöpe atarım", "Hiçbir şey yapmam"], dogru=0,
  aciklama="Döngüsel süreçte eksikler giderilerek tasarım geliştirilir (s. 57).")
a("u3k9", "Göze Hitap Eden Araçlar", "kisa", soru="Bir ürünü tanıtan, kısa açıklamalar ve fotoğraflar içeren, çok sayıda basılıp dağıtılan materyale ne denir?", yanit="broşür", kabul=["brosur"],
  aciklama="Broşür ürünü kısa metin ve fotoğraflarla tanıtır (s. 55).")

H.yaz()
