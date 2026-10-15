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
H.yaz()
