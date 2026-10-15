import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from ortak import Havuz, ONC
H = Havuz("tr1", 2, "t2"); a = H.add
K1, K2 = "(s. 77, 90, 92, 95)", "(s. 75–78, 101–104)"

# --- Konu 1: Kelimeler arası anlam ilişkileri
a("u2k1", "Eş Anlamlı Kelimeler", "eslestir", soru="Kelimeleri eş anlamlılarıyla eşleştir.", ciftler=[
  {"sol": "muhacir", "sag": "göçmen"},
  {"sol": "ziyan", "sag": "zarar"},
  {"sol": "zafer", "sag": "galibiyet"},
  {"sol": "huzur", "sag": "gönül rahatlığı"}],
  aciklama=f"Eş anlamlı kelimeler farklı yazılır, aynı anlamı verir {K1}.")
a("u2k1", "Zıt Anlamlı Kelimeler", "secim", soru="Hangi kelime çifti zıt anlamlı değildir?",
  secenekler=["esaret – özgürlük", "karanlık – aydınlık", "gelmek – gelmemek", "zafer – yenilgi"], dogru=2,
  aciklama=f"“-me” eki olumsuzluk yapar, zıt anlam yapmaz. “Gelmek”in zıttı “gitmek”tir {K1}.")
a("u2k1", "Somut ve Soyut Kelimeler", "dytablo", soru="Kelime somutsa D, soyutsa Y seç.", ifadeler=[
  {"s": "siper", "d": True}, {"s": "istiklal", "d": False}, {"s": "toprak", "d": True}, {"s": "cesaret", "d": False}],
  aciklama=f"Siper ve toprak duyularla algılanır; istiklal ve cesaret algılanmaz {K1}.")
a("u2k1", "Ölçüte Göre Sınıflandırma", "secim", soru="Sınıflandırma ile ilgili aşağıdaki ifadeler verilmiştir.",
  onculler=["Sınıflandırmaya başlamadan önce bir ölçüt seçilir.", "Ölçüt değişirse gruplar da değişebilir.", "Her grup için ayrı bir ölçüt kullanılır."],
  kok="Sınıflandırma ile ilgili yukarıdakilerden hangileri doğrudur?", secenekler=ONC, dogru=1,
  aciklama=f"Önce ölçüt seçilir ve bütün kelimelerde aynı ölçüt kullanılır {K1}.")
a("u2k1", "Anlamca Çelişen Kelimeler", "secim", soru="Hangi cümlede anlamca çelişen kelimeler birlikte kullanılmıştır?",
  secenekler=["Tören yaklaşık bir saat sürdü.", "Mutlaka erken gelmelisin.", "Belki yarın yağmur yağar.", "Hiç şüphesiz bu roman en güzeli olabilir."], dogru=3,
  aciklama=f"“Hiç şüphesiz” kesinlik, “olabilir” ihtimal bildirir; birlikte olmaz {K1}.")
a("u2k1", "Duyguyu Yansıtan Kelime Seçimi", "dy",
  ifade="Şair, Elif'in acısını anlatırken “kahrolmak” yerine “üzülmek” kelimesini seçseydi acı daha güçlü anlatılırdı.", dogru=False,
  duzeltme="“Kahrolmak” daha güçlü bir kelimedir; acıyı daha iyi anlatır.",
  aciklama="“Kahrolmak” çok büyük üzüntüdür. Kelime seçimi duygunun gücünü belirler (s. 102).")

# --- Konu 2: Çıkarım ve metnin mesajı
a("u2k2", "Yazılan ve Sezdirilen Anlam", "secim",
  metin=["Selin sınav kâğıdını alınca yüzü kıpkırmızı oldu.", "Kâğıdı hemen çantasına sakladı.", "Teneffüste kimseyle konuşmadı."],
  soru="Bu metinde sezdirilen (açıkça yazılmayan) bilgi hangisidir?",
  secenekler=["Selin sınavından düşük not almış olabilir.", "Selin sınav kâğıdını aldı.", "Selin kâğıdı çantasına koydu.", "Selin teneffüste kimseyle konuşmadı."], dogru=0,
  aciklama="Öbür şıklar metinde yazıyor. Kâğıdı saklaması düşük notu sezdiriyor.")
a("u2k2", "Çıkarım: İpucu + Bildiğin", "bosluk", havuz=["başlık", "yazar"], cumleler=[
  {"c": "Çıkarım yaparken metindeki ___ kullanırız.", "cevap": "ipuçlarını"},
  {"c": "İpuçlarına kendi ___ ekleriz.", "cevap": "bildiklerimizi"},
  {"c": "Çıkarımı metinden bir ___ ile destekleriz.", "cevap": "kanıt"}],
  aciklama="Çıkarım = ipucu + bildiğin; sonra kanıt cümlesi gösterilir.")
a("u2k2", "Kanıtını Göster", "secim", soru="“Hatice Nine için bayrak, evinden bile değerlidir.” çıkarımının kanıtı hangisi olabilir?",
  secenekler=["Ortalık ağarıyor, kadınlar gelip gidiyordu.", "Salihli'de birkaç ev yanmadan kalmıştı.", "Evi yansa da tek isteği, toprağının bayrağının altında olmasıydı.", "Oğlu onu bir eşekle getirdi."], dogru=2,
  aciklama=f"Evi yanan Nine'nin tek isteği bayrağının altında olmak; çıkarımı bu destekler {K2}.")
a("u2k2", "Sözün Asıl Anlamı", "secim", soru="Hatice Nine'nin “Ben elli senedir onu kovalıyorum.” sözüyle anlatmak istediği nedir?",
  secenekler=["Elli yıldır koşu yaptığını", "Yıllardır bayrağının altında yaşamayı özlediğini", "Bayrağı kaybettiğini", "Elli yaşında olduğunu"], dogru=1,
  aciklama=f"Nine yıllardır özgür bir yurtta, bayrağının altında yaşamayı özlemektedir {K2}.")
a("u2k2", "Karakterin Duygusunu Çıkarma", "eslestir", soru="Davranışları gösterdiği duyguyla eşleştir.", ciftler=[
  {"sol": "Koşarak gelip annesine sarıldı.", "sag": "sevinç"},
  {"sol": "Ellerini ovuşturup ikide bir yutkundu.", "sag": "heyecan"},
  {"sol": "Kapıyı çarpıp odasına kapandı.", "sag": "öfke"}],
  aciklama="Yazar duyguyu her zaman söylemez; davranışlardan çıkarırız.")
a("u2k2", "Metnin Mesajı", "kisa", soru="Yazarın metinle okura vermek istediği düşünceye ne ad verilir? (Bu konudaki adıyla yaz.)",
  yanit="mesaj", kabul=["ana fikir", "anafikir"],
  aciklama="Mesaj, yazarın vermek istediği düşüncedir; ana fikre çok benzer.")

# --- Konu 3: Sıralı kronolojik metin yapısı ve önemli bilgiler
K3 = "(s. 80–81, 85–88, 106)"
a("u2k3", "Metin Yapısı", "secim", soru="Metin yapısıyla ilgili aşağıdaki ifadeler verilmiştir.",
  onculler=["Metin yapısı, bilgilerin metinde nasıl düzenlendiğini gösterir.", "Kronolojik yapıda tarihler ve sıra bildiren kelimeler ipucudur.", "Metin yapısını bilmek önemli bilgiyi bulmayı kolaylaştırır."],
  kok="Yukarıdakilerden hangileri doğrudur?", secenekler=ONC, dogru=3,
  aciklama="Üçü de doğru: Yapıyı tanıyan, önemli bilgiyi kolay bulur.")
a("u2k3", "Sıralı Kronolojik Metin Yapısı", "dy",
  ifade="Sıralı kronolojik metinlerde olaylar en sondan başa doğru anlatılır.", dogru=False,
  duzeltme="Olaylar oluş sırasına göre, ilkten sona doğru anlatılır.",
  aciklama=f"Kronolojik yapıda ilk olan önce gelir {K3}.")
a("u2k3", "Zaman İpuçları", "bosluk", havuz=["çünkü", "bu yüzden"], cumleler=[
  {"c": "Lokma ___ ağızda parçalanır.", "cevap": "önce"},
  {"c": "Mideden geçen besin ___ ince bağırsağa ulaşır.", "cevap": "ardından"},
  {"c": "Uzun bir yolculuktan sonra ___ Samsun'a varıldı.", "cevap": "nihayet"}],
  aciklama="Önce, ardından, nihayet olayların sırasını gösterir.")
a("u2k3", "Zaman Çizelgesi", "eslestir", soru="Samsun yolculuğunda tarihleri olaylarla eşleştir.", ciftler=[
  {"sol": "16 Mayıs 1919", "sag": "Bandırma vapuruna binildi."},
  {"sol": "17 Mayıs 1919", "sag": "İnebolu'ya gelindi."},
  {"sol": "18 Mayıs 1919", "sag": "Sinop'a gelindi."},
  {"sol": "19 Mayıs 1919", "sag": "Samsun'a çıkıldı."}],
  aciklama="Yolculuk gün gün anlatılır: vapur, İnebolu, Sinop, Samsun (s. 85–86).")
a("u2k3", "Önemli Bilgi ve Detay", "dytablo", soru="Samsun yolculuğunu özetleyeceksin. Bilgi özette kalmalıysa D, detaysa Y seç.", ifadeler=[
  {"s": "Mustafa Kemal 19 Mayıs 1919'da Samsun'a çıktı.", "d": True},
  {"s": "Karaya saat 07.00'de bir sandalla ayak bastı.", "d": False},
  {"s": "Bu gün, Millî Mücadele'nin ilk günü sayılır.", "d": True},
  {"s": "Otelin yatakları komşu evlerden getirildi.", "d": False}],
  aciklama="Özette “ne oldu, ne zaman oldu” kalır; saat ve yatak gibi ayrıntılar çıkar (s. 86).")
a("u2k3", "Anahtar Kelime", "secim",
  metin=["Mehmet Âkif Ersoy, Millî Mücadele yıllarında şiirleriyle milletine güç verdi.", "İstiklâl Marşı'nı yazdı ve Türk milletine armağan etti.", "Şiirleri Safahat adlı eserde toplandı."],
  soru="Bu metnin konusunu en iyi taşıyan anahtar kelime grubu hangisidir?",
  secenekler=["yıl – güç – eser", "Mehmet Âkif – İstiklâl Marşı – şiir", "millet – armağan – ad", "Safahat – yedi – kitap"], dogru=1,
  aciklama="Metin, Mehmet Âkif'i ve şiirlerini, özellikle İstiklâl Marşı'nı anlatır (s. 106).")

# --- Konu 4: Görselle ve çoklu ortamla anlatılan anlam
K4 = "(s. 88, 95–97, 100)"
a("u2k4", "Görseldeki İpuçları", "secim", soru="Bir resimde sahilde kova ve kürekle kumdan kale yapan çocuklar, yanlarında bir şemsiye var. Bu görselden hangisi çıkarılamaz?",
  secenekler=["Çocuklar deniz kenarındadır.", "Hava güneşli olabilir.", "Çocuklar oyun oynamaktadır.", "Çocuklar kardeştir."], dogru=3,
  aciklama="Kardeş oldukları görselde hiçbir ipucuyla gösterilmiyor.")
a("u2k4", "Başlık ve Görselden Tahmin", "dy",
  ifade="Başlık ve görselden yaptığımız tahmini, içeriği izledikten sonra kontrol ederiz.", dogru=True,
  aciklama="Önce tahmin ve gerekçe, sonra kontrol (s. 95–96).")
a("u2k4", "Eş Anlam Oluşturma", "eslestir", soru="Durumları ögenin işleviyle eşleştir.", ciftler=[
  {"sol": "Ekranda “1915” yazıyor, anlatıcı da “1915'te” diyor.", "sag": "Eş anlam oluşturma"},
  {"sol": "Sözlerin arkasında hüzünlü bir müzik çalıyor.", "sag": "Anlamı destekleme"},
  {"sol": "Yazısız bir karikatür bir düşünceyi anlatıyor.", "sag": "Tek başına anlam oluşturma"}],
  aciklama=f"Aynı bilgi eş anlam, güçlendirme destek, yalnız anlatım tek başına {K4}.")
a("u2k4", "Anlamı Destekleme", "secim", soru="Bir belgeselde anlatıcı “Kağnılar zorlu yollarda ilerledi.” derken ekranda çamurlu yolda ağır ağır ilerleyen kağnılar görünüyor. Görüntünün işlevi nedir?",
  secenekler=["Anlatılanla çelişmek", "Anlatılanı canlandırıp güçlendirmek", "Yeni ve ilgisiz bir bilgi vermek", "Sözün yerine tamamen geçmek"], dogru=1,
  aciklama="Görüntü sözü gözümüzün önüne getirip güçlendiriyor; anlamı destekliyor.")
a("u2k4", "Tek Başına Anlam Oluşturma", "dy",
  ifade="Bir görsel, yazı ya da ses olmadan hiçbir şey anlatamaz.", dogru=False,
  duzeltme="Yazısız bir fotoğraf ya da karikatür de tek başına anlam oluşturabilir.",
  aciklama=f"Görsel tek başına da anlam oluşturabilir {K4}.")
a("u2k4", "Medya Metninde İçerik ve Tasarım", "dytablo", soru="Ölçüt görsel tasarımla ilgiliyse D, içerikle ilgiliyse Y seç.", ifadeler=[
  {"s": "Yazılar büyük ve okunaklı olmalı.", "d": True},
  {"s": "Bilgiler doğru olmalı.", "d": False},
  {"s": "Renkler birbirine uymalı.", "d": True},
  {"s": "Tarihî yerin önemi anlatılmalı.", "d": False}],
  aciklama="Yazı boyu ve renk tasarımdır; doğru bilgi ve anlatım içeriktir (s. 100).")

# --- Konu 5: İkna teknikleri 1
K5 = "(s. 89–90, 99)"
a("u2k5", "Karşılıkta Bulunma", "eslestir", soru="Cümleleri ikna tekniğiyle eşleştir.", ciftler=[
  {"sol": "Geçen hafta sana yardım ettim, şimdi sen bana yardım et.", "sag": "Karşılıkta bulunma"},
  {"sol": "Canım torunum, ricamı kırma.", "sag": "Sevgi (hoşlanma)"},
  {"sol": "Yıllardır söylediğimi yaptım, yine yapacağım.", "sag": "Tutarlılık"},
  {"sol": "Ben yirmi yıldır bu konuyu araştırıyorum.", "sag": "Otorite"}],
  aciklama=f"Her teknik başka bir şeye dayanır: iyilik, sevgi, değişmezlik, uzmanlık {K5}.")
a("u2k5", "Sevgi (Hoşlanma)", "dy",
  ifade="İnsanlar sevdikleri kişilerden gelen istekleri daha çabuk kabul eder.", dogru=True,
  aciklama="Bu, sevgi (hoşlanma) tekniğinin tanımıdır (s. 99).")
a("u2k5", "Tutarlılık", "secim", soru="Karikatürde bir liderin “Milletin bağımsızlığı her şeyin üstündedir.” sözünün yanında cephede en önde yer alması gösteriliyor. Bu karikatür hangi tekniği anlatır?",
  secenekler=["Kıtlık", "Tutarlılık", "Karşılıkta bulunma", "Toplumsal kanıt"], dogru=1,
  aciklama="Söz ile davranış birbirini tutuyor; bu tutarlılıktır (s. 89).")
a("u2k5", "Otorite", "secim", soru="Otorite tekniğiyle ilgili aşağıdaki ifadeler verilmiştir.",
  onculler=["Konuşan kişi dinleyenlere geçmişte yaptığı iyiliği hatırlatır.", "Konuşan kişi bilgisini ve uzmanlığını gösterir.", "İnsanlar uzman ve güvenilir kişilere daha kolay inanır."],
  kok="Yukarıdakilerden hangileri doğrudur?", secenekler=ONC, dogru=2,
  aciklama="Geçmişteki iyiliği hatırlatmak karşılıkta bulunmadır (s. 99).")
a("u2k5", "İkna Etmek", "bosluk", havuz=["kanıt", "başlık"], cumleler=[
  {"c": "Birini bir düşünceye razı etmeye ___ etmek denir.", "cevap": "ikna"},
  {"c": "Uzmanlığını göstermek ___ tekniğidir.", "cevap": "otorite"},
  {"c": "Söz ile davranışın aynı olması ___ tekniğidir.", "cevap": "tutarlılık"}],
  aciklama="İkna; otorite uzmanlık, tutarlılık söz-davranış uyumudur.")
a("u2k5", "Karşılıkta Bulunma", "kisa", soru="İnsanın kendisine iyilik yapan birinin sözüne ikna olmasına ne ad verilir?",
  yanit="karşılıkta bulunma", kabul=["karsilikta bulunma", "karşılık"],
  aciklama="Bu teknik karşılıkta bulunmadır (s. 99).")

# --- Konu 6: İkna teknikleri 2
K6 = "(s. 98–99)"
a("u2k6", "Toplumsal Kanıt", "eslestir", soru="Cümleleri ikna tekniğiyle eşleştir.", ciftler=[
  {"sol": "Okulun yarısı kulübe katıldı, sen de katıl!", "sag": "Toplumsal kanıt"},
  {"sol": "Kayıt için son iki gün!", "sag": "Kıtlık"},
  {"sol": "Kirli bir şehir mi, temiz bir şehir mi?", "sag": "Karşıtlık"},
  {"sol": "Önce sizin oyununuzu, sonra bizimkini oynayalım.", "sag": "Uzlaşma"}],
  aciklama=f"Çoğunluk, azlık, zıtlık ve ortak çözüm dört ayrı tekniktir {K6}.")
a("u2k6", "Kıtlık", "dy",
  ifade="Kıtlık tekniğinde bir şeyin çok bol olduğu vurgulanır.", dogru=False,
  duzeltme="Kıtlık tekniğinde bir şeyin az ya da sınırlı olduğu vurgulanır.",
  aciklama="Azlık vurgulanınca ilgi artar (s. 99).")
a("u2k6", "Karşıtlık", "secim",
  metin=["Esaretin utancı ile bağımsızlığın onuru arasındaki savaşta tarafımız bellidir.", "Karşımızda karanlık bir düşman, önümüzde aydınlık bir gelecek var."],
  soru="Bu cümlelerde hangi ikna tekniği kullanılmıştır?",
  secenekler=["Uzlaşma", "Karşılıkta bulunma", "Karşıtlık", "Sevgi (hoşlanma)"], dogru=2,
  aciklama="Esaret – bağımsızlık, karanlık – aydınlık zıtlıkları kullanılmış (s. 98).")
a("u2k6", "Uzlaşma", "secim", soru="Uzlaşma tekniğiyle ilgili aşağıdaki ifadeler verilmiştir.",
  onculler=["Kişi uyumlu ve çözüm odaklı olduğunu gösterir.", "İnsanlar sorun çıkarmayan kişilere güvenir.", "Kişi zamanın çok az kaldığını vurgular."],
  kok="Yukarıdakilerden hangileri uzlaşma tekniğini anlatır?", secenekler=ONC, dogru=1,
  aciklama="Zamanın azlığını vurgulamak kıtlıktır (s. 99).")
a("u2k6", "İkna Metnini Çözümleme", "dytablo", soru="Konuşma metnindeki (s. 98) bölüm ile tekniğin eşleşmesi doğruysa D, yanlışsa Y seç.", ifadeler=[
  {"s": "2. bölüm: Bütün millet omuz omuza → toplumsal kanıt", "d": True},
  {"s": "4. bölüm: Zamanımız dardır → kıtlık", "d": True},
  {"s": "3. bölüm: Ömrümü cephelerde geçirdim → uzlaşma", "d": False}],
  aciklama="Cephe deneyimini öne sürmek otoritedir; öbür ikisi doğru (s. 98).")
a("u2k6", "Toplumsal Kanıt", "kisa", soru="Başkalarının yaygın davranışlarını öne sürerek ikna etmeye ne ad verilir?",
  yanit="toplumsal kanıt", kabul=["toplumsal kanit"],
  aciklama="Bu teknik toplumsal kanıttır (s. 99).")
H.yaz()
