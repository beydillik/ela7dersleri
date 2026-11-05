TEKRAR = {"u3k3": [
 ("Dolaşım sistemi kan, kalp ve {damarlardan|bağırsaktan|akciğerden} oluşur.", "s. 104"),
 ("Dolaşım sistemi oksijeni, besin maddelerini ve hormonları hücrelere taşır; hücrelerde oluşan {atık maddelerin|besin maddelerinin} vücuttan uzaklaştırılmasını sağlar.", "s. 104"),
 ("Kasılıp gevşeme hareketiyle kanın damarlarda dolaşmasını sağlayan, özel kas dokusundan oluşan organa {kalp|akciğer|mide} denir.", "s. 104"),
 ("Kalpten çıkan kanı vücuda {atardamarlar|toplardamarlar|kılcal damarlar} taşır; vücuda dağılan kanı toplayıp kalbe {toplardamarlar|atardamarlar|kılcal damarlar} getirir.", "s. 104"),
 ("Kılcal damarlar atardamarlarla toplardamarları birbirine bağlar; kan ile hücreler arasında {madde alışverişini|ses iletimini|ışık geçişini} sağlar.", "s. 104"),
 ("Kalpten çıkan kanın akciğerlere gidip kalbe dönmesine {küçük|büyük} kan dolaşımı, vücuda yayılıp kalbe dönmesine {büyük|küçük} kan dolaşımı denir.", "s. 105"),
 ("Akciğerlere ulaşan kanın oksijen oranı {artar|azalır}, karbon dioksit oranı {azalır|artar}. Yetişkinlerde dinlenme anında nabız genellikle {60-100|10-30|150-200} atım/dakikadır.", "s. 105"),
]}
KISA = {"u3k3": [
 {"soru": "Küçük kan dolaşımı ile büyük kan dolaşımı arasındaki farkı yazınız.",
  "tetik": ["farkı"],
  "okut": ["İki dolaşımı ayrı ayrı tanımla (iki parça).", "Sebep ve sonuç yaz: “… çünkü …”", "Yalnız bir organın adını yaz."],
  "parcalar": [
   {"bas": "Küçük kan dolaşımı:", "ornek": "Kan kalpten akciğerlere gider ve tekrar kalbe döner.", "havuz": ["Kan kalpten tüm vücuda yayılır.", "Kan yalnızca bağırsaklara gider."], "k": ["akciğer"]},
   {"bas": "Büyük kan dolaşımı:", "ornek": "Kan kalpten tüm vücuda yayılır ve tekrar kalbe döner.", "havuz": ["Kan kalpten akciğerlere gider ve tekrar kalbe döner.", "Kan yalnızca akciğerlerde dolaşır."], "k": ["vücuda"]}],
  "kisa": "Küçük: kalpten akciğerlere gidip kalbe döner. Büyük: kalpten tüm vücuda yayılıp kalbe döner.",
  "cevap": "Küçük kan dolaşımında kan kalpten akciğerlere gider ve tekrar kalbe döner. Büyük kan dolaşımında ise kan kalpten tüm vücuda yayılır ve tekrar kalbe döner.",
  "anahtarlar": [{"ad": "küçük: kalp → akciğer → kalp", "k": ["akciğer"]}, {"ad": "büyük: kalp → tüm vücut → kalp", "k": ["vücuda"]}],
  "sayfa": "s. 105"},
 {"soru": "Atardamar, toplardamar ve kılcal damarın görevlerini yazınız.",
  "tetik": ["görevlerini"],
  "okut": ["Üç damarı ayrı ayrı yaz (üç parça).", "Benzerlik ve fark yaz.", "Evet ya da hayır yaz, sonra nedenini ekle."],
  "parcalar": [
   {"bas": "Atardamar:", "ornek": "Kalpten çıkan kanı vücuda taşır.", "havuz": ["Kanı kalbe geri getirir.", "Hücrelerle madde alışverişi yapar."], "k": ["kalpten"]},
   {"bas": "Toplardamar:", "ornek": "Vücuda dağılan kanı toplayıp kalbe getirir.", "havuz": ["Kalpten çıkan kanı vücuda taşır.", "Kan ile hücreler arasında madde alışverişini sağlar."], "k": ["toplay", "kalbe getir"]},
   {"bas": "Kılcal damar:", "ornek": "Kan ile hücreler arasında madde alışverişini sağlar.", "havuz": ["Kalpten çıkan kanı vücuda taşır.", "Kanı kalbe getirir."], "k": ["alışveriş"]}],
  "kisa": "Atardamar kalpten çıkan kanı vücuda taşır; toplardamar kanı toplayıp kalbe getirir; kılcal damar madde alışverişini sağlar.",
  "cevap": "Atardamar kalpten çıkan kanı vücuda taşır. Toplardamar vücuda dağılan kanı toplayıp kalbe getirir. Kılcal damar ise atardamarlarla toplardamarları birbirine bağlar ve kan ile hücreler arasında madde alışverişini sağlar.",
  "anahtarlar": [{"ad": "atardamar: kalpten vücuda", "k": ["kalpten"]}, {"ad": "toplardamar: kanı toplayıp kalbe getirir", "k": ["toplay", "kalbe getir"]}, {"ad": "kılcal damar: madde alışverişi", "k": ["alışveriş"]}],
  "sayfa": "s. 104"},
]}
OKUT = {"u3k3": [
 ["küçük ve büyük kan dolaşımında kanın nereye gidip geldiğini ayrı ayrı yazmanı", "kalbin kaç bölümden oluştuğunu söylemeni", "kan dolaşımını kimin keşfettiğini yazmanı"],
 ["atardamarın, toplardamarın ve kılcal damarın her birinin ne iş yaptığını yazmanı", "en kalın damarın hangisi olduğunu söylemeni", "damarların ne renk olduğunu anlatmanı"]]}
METINLI = {"u3k3": [
 {"metin": ["Kalpten çıkan kan akciğerlere gider.", "Akciğerlerde kanın oksijen oranı artar, karbon dioksit oranı azalır.", "Oksijenlenmiş kan kalbin sol tarafına geri döner."],
  "soru": "Metinde anlatılan dolaşım hangisidir?", "bolge": ["anlatılan dolaşım hangisidir"],
  "serit": "Metinde anlatılan dolaşımın adı", "kanit": [0, 2],
  "secenekler": ["Küçük kan dolaşımı", "Büyük kan dolaşımı", "Kanın hücrelerle madde alışverişi"], "dogru": 0, "tuzak": [],
  "ipucu": "Kan kalpten nereye gidiyor ve nereye dönüyor?", "kanitIpucu": "Kanın kalpten nereye gittiğini söyleyen cümleyi bul.",
  "aciklama": "Kalpten çıkan kanın akciğerlere gidip tekrar kalbe dönmesine küçük kan dolaşımı denir (s. 105).", "kavram": "Küçük Kan Dolaşımı"},
 {"metin": ["Okulda sınıflar arası futbol turnuvası vardı.", "Barış maçta çok koştu.", "Maç bitince arkadaşı Berat ona sarıldı ve Barış'ın kalbinin çok hızlı attığını fark etti.", "Öğretmenleri ikisinden ellerini kalplerinin üzerine koymalarını istedi.", "İki arkadaşın kalbi farklı hızlarda atıyordu."],
  "soru": "Barış'ın kalbinin Berat'ınkinden hızlı atmasının sebebi nedir?", "bolge": ["hızlı atmasının sebebi nedir"],
  "serit": "Barış'ın kalbinin hızlı atmasının sebebi", "kanit": [1],
  "secenekler": ["Maçta çok koşması", "Berat'ın ona sarılması", "Elini kalbinin üzerine koyması"], "dogru": 0, "tuzak": [1, 2],
  "ipucu": "Barış maçta ne yaptı? Nabız neye göre değişir?", "kanitIpucu": "Barış'ın maçta ne yaptığını anlatan cümleyi bul.",
  "aciklama": "Barış maçta çok koştuğu için kalbi hızlı atıyor. Nabız (kalp atış hızı) yaşa, cinsiyete ve aktiviteye göre değişir (s. 101, 105).", "kavram": "Kalp"}]}
