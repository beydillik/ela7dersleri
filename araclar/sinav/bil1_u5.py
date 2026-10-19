import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from ortak import Havuz, ONC, ONC2
H = Havuz("bil1", 5, "b5"); a = H.add

# --- Konu 1: Mimar ve Mimari Tasarım (s. 70–72 + program)
a("u5k1", "Mimar", "kisa", soru="İnsanların yaşayacağı yapıların çizimlerini yapan ve yapılmasını yöneten uzmana ne denir?",
  yanit="mimar", kabul=["mimarlar"],
  aciklama="Yapıların tasarısını çizen ve uygulamasını yöneten uzman mimardır (s. 71).")
a("u5k1", "Mimar Sinan", "secim", soru="Mimar Sinan ile ilgili bilgiler verilmiştir.",
  onculler=["Osmanlı'nın en görkemli döneminde yaşamıştır.", "Toplam 375 mimari eseri vardır.", "Hep aynı kalıpla çalışmıştır."],
  kok="Bu bilgilerden hangileri doğrudur?", secenekler=ONC, dogru=1,
  aciklama="Sinan Osmanlı'nın görkemli döneminde yaşadı, 375 eseri var; kalıplara bağlı kalmadı (s. 71).")
a("u5k1", "Mimarın Görevleri", "dytablo", soru="Mimarın görevi ise D, değilse Y seç.", ifadeler=[
  {"s": "Binanın planını çizmek", "d": True}, {"s": "Binanın maketini hazırlamak", "d": True},
  {"s": "Binanın imar planına uygunluğunu incelemek", "d": True}, {"s": "Binada satılacak ürünlerin fiyatını belirlemek", "d": False}],
  aciklama="Plan, maket ve imar planı incelemesi mimarın görevleridir (s. 72).")
a("u5k1", "Mimari Tasarım", "dy", ifade="Mimari tasarım coğrafi yapıdan, iklimden ve kültürel farklılıklardan etkilenir.", dogru=True,
  aciklama="Mimari tasarım coğrafya, iklim ve kültürle şekillenir (s. 71).")
a("u5k1", "Peyzaj Tasarımı", "bosluk", havuz=["topografya", "kiriş"], cumleler=[
  {"c": "Binaları saran dış çevrenin tasarımına ___ tasarımı denir.", "cevap": "peyzaj"},
  {"c": "Mimar Sinan bir ___ iken mimari zekâsıyla öne çıktı.", "cevap": "yeniçeri"},
  {"c": "Bir binayı görünce onu güzel bulmamız estetik ___ ile ilgilidir.", "cevap": "algı"}],
  aciklama="Peyzaj dış çevre tasarımıdır; Sinan yeniçeriydi; güzel bulmak estetik algıdır (s. 71–72; program).")
a("u5k1", "Mimari Mekân", "dy", ifade="Okul bahçesi kapalı bir mekândır.", dogru=False,
  duzeltme="Okul bahçesi açık bir mekândır; sınıf kapalı mekândır.",
  aciklama="Bahçe ve avlu açık, oda ve sınıf kapalı mekândır (program; s. 72).")
a("u5k1", "Estetik Algı", "secim", soru="Hangisi bir binanın estetik algısıyla en çok ilgilidir?",
  secenekler=["Binanın imar planına uygunluğu", "Binanın renginin ve biçiminin göze güzel gelmesi", "Binanın kaç işçiyle yapıldığı", "Binanın tapu kaydı"], dogru=1,
  aciklama="Estetik algı, yapıyı güzel bulup bulmamamızdır (program).")

# --- Konu 2: İşlevlerine Göre Mimari Yapılar (s. 72–74 + program)
a("u5k2", "Konut", "eslestir", soru="Yapıyı ait olduğu grupla eşleştir.", ciftler=[
  {"sol": "Villa", "sag": "Konut"},
  {"sol": "Plaza", "sag": "İş merkezi"},
  {"sol": "Hastane", "sag": "Hizmet binası"},
  {"sol": "Baraj", "sag": "Mühendislik yapısı"}],
  aciklama="Kitap yapıları kullanım amacına göre dört gruba ayırır (s. 72).")
a("u5k2", "Hizmet Binaları", "secim", soru="Hangisi hizmet binalarından biri değildir?",
  secenekler=["Okul", "Sinema", "Liman", "Köşk"], dogru=3,
  aciklama="Köşk bir konuttur; okul, sinema ve liman hizmet binasıdır (s. 72).")
a("u5k2", "Mühendislik Yapıları", "kisa", soru="Köprü, viyadük, baraj ve yol gibi yapılara mühendislik yapıları dışında hangi ad verilir?",
  yanit="sanat yapıları", kabul=["sanat yapısı", "sanat yapilari"],
  aciklama="Mühendislik yapılarına sanat yapıları da denir (s. 72).")
a("u5k2", "İş Merkezleri", "dy", ifade="Fabrika ve depo, kitapta iş merkezleri arasında sayılır.", dogru=True,
  aciklama="Mağaza, han, otel, fabrika, depo ve plaza iş merkezleridir (s. 72).")
a("u5k2", "İşlev-Mekân İlişkisi", "secim", soru="Bir mekânın tasarımı incelenirken sorulan sorular verilmiştir.",
  onculler=["Mekânın en önemli işlevi nedir?", "Aydınlatma ve ses yalıtımı özellikleri nelerdir?", "Nerelere yapılması lazım?"],
  kok="Bunlardan hangileri kitapta sorulur?", secenekler=ONC, dogru=3,
  aciklama="Kitap bu üç soruyu ve biçimsel özellikleri sorar (s. 73).")
a("u5k2", "İşlevsellik", "dy", ifade="İşlevsellik, bir binanın yalnızca süslü görünmesidir.", dogru=False,
  duzeltme="İşlevsellik, binanın yapılış amacına uygun çalışmasıdır.",
  aciklama="İşlevsel yapı amacına uygun, kullanılabilir yapıdır (program).")
a("u5k2", "Mekânsal Analoji", "secim", soru="Bir öğrenci kütüphane ile müzeyi gözlemleyip ikisinde de sessiz ve aydınlık ortam gerektiğini buluyor. Öğrenci ne yapmıştır?",
  secenekler=["Mekânsal analoji", "Simülasyon", "Peyzaj tasarımı", "Toplu konut"], dogru=0,
  aciklama="Mekânları gözlemleyip benzerlik bulmak mekânsal analojidir (program).")

# --- Konu 3: Yaşam Biçimi ve Geleneksel Evler (s. 75–76)
a("u5k3", "Harran Evleri", "eslestir", soru="Geleneksel evi özelliğiyle eşleştir.", ciftler=[
  {"sol": "Harran evleri", "sag": "Tuğladan konik kubbe"},
  {"sol": "Kapadokya evleri", "sag": "Peribacasına oyulmuş"},
  {"sol": "Safranbolu", "sag": "UNESCO Dünya Miras Listesi"},
  {"sol": "Karadeniz evi", "sag": "Alt katta hayvan barınağı"}],
  aciklama="Her geleneksel ev kendi yaşam biçimini ve çevresini yansıtır (s. 75–76).")
a("u5k3", "Toplu Konut", "secim", soru="Kitaba göre toplu konutların ortaya çıkmasının nedeni hangisidir?",
  secenekler=["Göçler sonucu büyük kentlerde konut açığı", "Kapadokya'daki yanardağlar", "Harran'da ağacın az olması", "Pagodaların yayılması"], dogru=0,
  aciklama="Göçlerle büyük kentlerde konut açığı oluştu, toplu konutlar doğdu (s. 75).")
a("u5k3", "Kültürel Kanıt", "dy", ifade="Kitaba göre yapılar yalnızca insanı çevreden koruyan bir kalkandır.", dogru=False,
  duzeltme="Yapılar aynı zamanda birer kültürel kanıttır.",
  aciklama="Yapılar hem korur hem de kültürün kanıtıdır (s. 75).")
a("u5k3", "Kapadokya Evleri", "secim", soru="Kapadokya ile ilgili bilgiler verilmiştir.",
  onculler=["Evler kardan ve buzdan yapılmıştır.", "Peribacalarını yağmur ve rüzgârın aşındırması oluşturmuştur.", "Taşlar hava ile temas edene kadar yumuşaktır."],
  kok="Bu bilgilerden hangileri doğrudur?", secenekler=ONC, dogru=2,
  aciklama="Peribacaları aşınmayla oluştu, taşlar kolay oyulur; kar-buz iglodur (s. 76).")
a("u5k3", "Safranbolu Evleri", "kisa", soru="Safranbolu adını hangi bitkiden alır?",
  yanit="safran", kabul=["safran bitkisi"],
  aciklama="Safranbolu adını safran bitkisinden alır (s. 76).")
a("u5k3", "Harran Evleri", "dy", ifade="Harran evlerinin kubbeli yapısı evi yazın serin, kışın sıcak tutar.", dogru=True,
  aciklama="Kubbeli yapı sıcak ve kurak yazlarda evi serin tutar (s. 76).")
a("u5k3", "Yaşam Biçimi", "bosluk", havuz=["iglo", "pagoda"], cumleler=[
  {"c": "Harran evleri ___ tekniğiyle yapılmıştır.", "cevap": "bindirme"},
  {"c": "Tipik Karadeniz evinin alt katı hayvan ___ olarak kullanılır.", "cevap": "barınağı"},
  {"c": "Evler bölgesel, iklimsel ve ___ olanaklara göre değişmiştir.", "cevap": "teknik"}],
  aciklama="Evler yaşam biçimine, bölgeye, iklime ve tekniğe göre şekillenir (s. 75–76).")

# --- Konu 4: Mimariyi Etkileyen Unsurlar (s. 77–78 + program)
a("u5k4", "İklim", "secim", soru="Kuzeye gidildikçe evlerde hangi değişiklik görülür?",
  secenekler=["Pencereler büyür, çatılar düzleşir", "Pencereler küçülür, çatılar dikleşir", "Geniş avlular yapılır", "Duvarlar incelir"], dogru=1,
  aciklama="Kuzeye gittikçe pencereler küçülür, çatılar dikleşir (s. 77).")
a("u5k4", "Coğrafi Yapı", "dytablo", soru="Kitaptaki bilgilere göre doğruysa D, yanlışsa Y seç.", ifadeler=[
  {"s": "Deniz kıyısındaki evlerde büyük camlar ve teras düşünülür.", "d": True},
  {"s": "Yaylalarda rüzgâra karşı güçlendirilmiş çatılar yapılır.", "d": True},
  {"s": "Eğimli arazideki ve ovadaki yapılar hep aynıdır.", "d": False}],
  aciklama="Kıyıda büyük cam, yaylada güçlü çatı; eğimli arazi ile ova farklıdır (s. 77).")
a("u5k4", "Topografya", "kisa", soru="Dağ, tepe, yayla ve vadi gibi farklı yüksekliklerle ilgili kavram hangisidir?",
  yanit="topografya", kabul=["topoğrafya", "topografik oluşumlar"],
  aciklama="Yeryüzünü şekillendiren değişik yükseklikler topografik oluşumlardır (s. 77).")
a("u5k4", "İnanç ve Kültür", "secim", soru="Budistlerin dinî yapılarına ne ad verilir?",
  secenekler=["Tulou", "İglo", "Torf ev", "Pagoda"], dogru=3,
  aciklama="Pagoda, Budistlerin dinî yapısıdır (s. 78).")
a("u5k4", "Tulou Evleri", "eslestir", soru="Evi bulunduğu yerle eşleştir.", ciftler=[
  {"sol": "Tulou evler", "sag": "Çin"},
  {"sol": "İglo", "sag": "Kutuplar"},
  {"sol": "Torf evler", "sag": "İzlanda"}],
  aciklama="Tulou Çin'de, iglo kutuplarda, torf ev İzlanda'dadır (s. 77–78).")
a("u5k4", "Torf Ev", "dy", ifade="Torf evler ahşap ya da taş evlere göre çok daha iyi yalıtım sağlar.", dogru=True,
  aciklama="Toprakla kaplı torf evler iyi yalıtım sağlar (s. 78).")
a("u5k4", "İglo", "bosluk", havuz=["tuğla", "bambu"], cumleler=[
  {"c": "Eskimolar igloları kardan ve ___ yapar.", "cevap": "buzdan"},
  {"c": "Tulou, Çince'de ___ yapı anlamına gelir.", "cevap": "toprak"},
  {"c": "Bir yerde uzun süre gözlenen hava olaylarının ortalamasına ___ denir.", "cevap": "iklim"}],
  aciklama="İglo kar-buz, Tulou toprak yapıdır; iklim uzun süreli ortalamadır (s. 77–78).")

# --- Konu 5: Konutun Çevreyle Uyumu (program)
a("u5k5", "Konutun Yönü", "secim", soru="Ülkemiz gibi kuzey yarım küredeki soğuk bir yerde ev, güneş ısısından çok yararlanmak için hangi yöne bakmalıdır?",
  secenekler=["Kuzeye", "Güneye", "Hiçbir yöne", "Yalnızca yere"], dogru=1,
  aciklama="Soğuk iklimlerde binalar güneye yönlendirilir (program).")
a("u5k5", "Doğal Işık Durumu", "dy", ifade="Gün ışığından iyi yararlanan bir ev, lambalar için daha çok elektrik harcar.", dogru=False,
  duzeltme="Gün ışığı lambalar için harcanan enerjiyi azaltır.",
  aciklama="Gün ışığı yenilenebilir bir kaynaktır, aydınlatma enerjisini azaltır (program).")
a("u5k5", "Gürültü", "kisa", soru="Aralarında uyum bulunmayan, düzensiz ve istenmeyen seslerin bütününe ne denir?",
  yanit="gürültü", kabul=["gurultu"],
  aciklama="TDK'ya göre bu seslerin bütünü gürültüdür (program).")
a("u5k5", "Erişilebilirlik", "secim", soru="Bir binanın girişine rampa yapılması hangi kavramla ilgilidir?",
  secenekler=["Manzara", "Topografya", "Erişilebilirlik", "Peyzaj"], dogru=2,
  aciklama="Rampa engelli bireylerin binayı kendi başına kullanmasını sağlar: erişilebilirlik (program).")
a("u5k5", "Manzara", "eslestir", soru="Konutla ilgili kararı kavramla eşleştir.", ciftler=[
  {"sol": "Göle bakan büyük pencere", "sag": "Manzara"},
  {"sol": "Yola karşı ses yalıtımı", "sag": "Gürültü"},
  {"sol": "Kapı ve tezgâhı insan boyuna göre yapmak", "sag": "Antropometri"},
  {"sol": "Güneye bakan pencereler", "sag": "Yön"}],
  aciklama="Her karar konutun çevreyle ve insanla uyumunu sağlar (program).")
a("u5k5", "Sürdürülebilir Konut", "secim", soru="Programa göre sürdürülebilir konut için yöresel malzeme örnekleri verilmiştir.",
  onculler=["Karadeniz'de ahşap", "İç Anadolu'da kerpiç ya da taş", "Kutuplarda plastik"],
  kok="Bunlardan hangileri programdaki örneklerdir?", secenekler=ONC, dogru=1,
  aciklama="Program Karadeniz için ahşap, İç Anadolu için kerpiç ya da taşı örnek verir (program).")
a("u5k5", "Antropometri ve Konut", "dy", ifade="Evdeki kapı, merdiven ve tezgâhlar insanın vücut ölçülerine göre tasarlanmalıdır.", dogru=True,
  aciklama="Antropometri, insan ölçülerine uygun tasarım için kullanılır (program).")

# --- Konu 6: Mekân Tasarımı (s. 79–82 + program)
a("u5k6", "Kolon ve Kiriş", "eslestir", soru="Yapı elemanını göreviyle eşleştir.", ciftler=[
  {"sol": "Kolon", "sag": "Dik (düşey) taşıyıcı"},
  {"sol": "Kiriş", "sag": "Yatay taşıyıcı"},
  {"sol": "Temel", "sag": "Yükü zemine dağıtır"},
  {"sol": "Çatı", "sag": "Binanın üst örtüsü"}],
  aciklama="Kolon dik, kiriş yatay taşır; temel yükü zemine verir; çatı üst örtüdür (s. 79).")
a("u5k6", "Çatı Tipleri", "secim", soru="Hangisi kitapta geçen çatı tiplerinden biri değildir?",
  secenekler=["Beşik", "Kelebek", "Piramit", "Kubbe"], dogru=3,
  aciklama="Beşik, kelebek ve piramit kitaptaki çatı tiplerindendir (s. 79).")
a("u5k6", "Kuş Bakışı Çizim", "kisa", soru="Bir yeri yüksekten aşağıya, bütün genişliğiyle bakılmış gibi çizmeye ne denir?",
  yanit="kuş bakışı", kabul=["kuş bakışı çizim", "kus bakisi"],
  aciklama="Yukarıdan, bütün genişliğiyle bakış kuş bakışıdır (s. 81).")
a("u5k6", "Konut Tasarım Soruları", "dytablo", soru="Hayalindeki evi tasarlamadan önce kitapta sorulan bir soruysa D, değilse Y seç.", ifadeler=[
  {"s": "Bu yer nasıl bir iklimde?", "d": True}, {"s": "Ne iş yapıyorsunuz?", "d": True},
  {"s": "Hobileriniz neler?", "d": True}, {"s": "Hangi takımı tutuyorsunuz?", "d": False}],
  aciklama="Coğrafya, iklim, meslek, aile ve hobiler sorulur (s. 80).")
a("u5k6", "Temel", "secim", soru="Binada yükün ilerleyiş sırası hangisinde doğru verilmiştir?",
  secenekler=["Kiriş → kolon → temel → zemin", "Temel → kiriş → çatı → zemin", "Kolon → çatı → kiriş → temel", "Zemin → temel → kolon → kiriş"], dogru=0,
  aciklama="Kiriş yükü kolona, kolon temele, temel zemine aktarır (s. 79).")
a("u5k6", "Ev Planı", "dy", ifade="Kitaptaki ev planlarında yatak odaları, banyo, mutfak, salon ve veranda görülür.", dogru=True,
  aciklama="Tek katlı ve iki katlı ev planlarında bu bölümler vardır (s. 79).")
a("u5k6", "Mimari Tasarımın Sunumu", "secim", soru="Programa göre mimari tasarımın sunumunda adımlar hangi sırayla yapılır?",
  secenekler=["Değerlendir → uygula → planla → tasarla", "Planla → tasarla → uygula → değerlendir", "Uygula → planla → değerlendir → tasarla", "Tasarla → değerlendir → planla → uygula"], dogru=1,
  aciklama="Sunum planlanır, tasarlanır, uygulanır ve değerlendirilir (program).")

H.yaz()
