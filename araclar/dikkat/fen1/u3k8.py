TEKRAR = {"u3k8": [
 ("Bağımlılık; bir maddenin sorunlara yol açmasına rağmen alınmaya devam edilmesi ve bırakma isteğine rağmen {bırakılamamasıdır|bırakılmasıdır|unutulmasıdır}.", "s. 125"),
 ("Kontrolü sağlanmadan kullanılan {her madde ya da davranış|yalnızca tütün} bağımlılık oluşturabilir.", "s. 125"),
 ("Aşırı kilo alımından kaçınılmalı, öğünlerde besinler yeterli ve {dengeli|dengesiz} alınmalıdır. Böylece diyaframın hareketi {kolaylaşır|zorlaşır}.", "s. 125"),
 ("Spor yapmak vücudun nefes alıp verme ihtiyacını artırır; bu durum akciğerleri ve solunumda görevli kasları {güçlendirir|zayıflatır}.", "s. 125"),
 ("Solunum sistemi sağlığı için kirli ve {tozlu|havadar} ortamlardan uzak durulmalı, uzun süre kalınan kapalı mekânlar {havalandırılmalıdır|kapalı tutulmalıdır}.", "s. 125"),
 ("Bağımlılık yapıcı maddeler solunum ve {dolaşım|boşaltım|sindirim} sistemi rahatsızlıklarına yol açabilir; sosyal çevreyi ve aile ilişkilerini de {olumsuz|olumlu} etkiler.", "s. 126"),
 ("{Yeşilay|Kızılay|Türk Dil Kurumu}, bağımlılıklardan bireyi ve toplumu korumak amacıyla çalışan bir sivil toplum kuruluşudur. Yeşilay Haftası her yıl {1-7 Mart|1-7 Mayıs|1-7 Eylül} tarihlerinde kutlanır.", "s. 126"),
]}
KISA = {"u3k8": [
 {"soru": "Solunum sistemi sağlığını korumak için iki davranış yazınız.",
  "tetik": ["iki davranış"],
  "okut": ["İki ayrı davranış yaz (iki parça).", "Neden ve sonuç yaz.", "Tanım yaz: “X, … denir.”"],
  "parcalar": [
   {"bas": "Birinci davranış:", "ornek": "Temiz havada yürüyüş ya da egzersiz yapmak.", "havuz": ["Kapalı ortamları hiç havalandırmamak.", "Tozlu ortamlarda uzun süre kalmak."], "k": ["egzersiz", "yürüyüş"]},
   {"bas": "İkinci davranış:", "ornek": "Kirli ve tozlu ortamlardan uzak durmak, kapalı mekânları havalandırmak.", "havuz": ["Tütün ürünleri kullanmak.", "Ağızdan hızlı nefes almak."], "k": ["uzak", "havalandır"]}],
  "kisa": "Temiz havada egzersiz yapmak; kirli ve tozlu ortamlardan uzak durmak, kapalı mekânları havalandırmak.",
  "cevap": "Temiz havada yürüyüş ya da egzersiz yapmak. Kirli ve tozlu ortamlardan uzak durmak ve uzun süre kalınan kapalı mekânları havalandırmak.",
  "anahtarlar": [{"ad": "temiz havada egzersiz / yürüyüş", "k": ["egzersiz", "yürüyüş"]}, {"ad": "kirli ortamdan uzak durmak / havalandırmak", "k": ["uzak", "havalandır"]}],
  "sayfa": "s. 125"},
 {"soru": "Bağımlılık nedir? Yazınız.",
  "tetik": ["nedir"],
  "okut": ["Tanımı yaz (iki parça).", "Benzerlik ve fark yaz.", "Evet ya da hayır yaz."],
  "parcalar": [
   {"bas": "Kullanım:", "ornek": "Bir maddenin sorunlara yol açmasına rağmen alınmaya devam edilmesidir.", "havuz": ["Maddenin bir kez denenmesidir.", "Bir maddeyi hiç kullanmamaktır."], "k": ["rağmen"]},
   {"bas": "Bırakma:", "ornek": "Bırakma isteğine rağmen bırakılamamasıdır.", "havuz": ["Kısa süre kullanılıp unutulmasıdır.", "Doktor önerisiyle kullanılmasıdır."], "k": ["bırakıl"]}],
  "kisa": "Zararlarına rağmen kullanmaya devam etmek ve bırakma isteğine rağmen bırakılamamasıdır.",
  "cevap": "Bağımlılık, bir maddenin ruhsal, fiziksel ya da sosyal sorunlara yol açmasına rağmen alınmaya devam edilmesi ve bırakma isteğine rağmen bırakılamamasıdır.",
  "anahtarlar": [{"ad": "zarara rağmen kullanmaya devam", "k": ["rağmen"]}, {"ad": "bırakılamama", "k": ["bırakıl"]}],
  "sayfa": "s. 125"},
]}
ELLE = {"Doktora göre Elif'in yaşadığı yerde hava kirliliğine ne yol açıyordu?": "ne yol açıyordu", "Spor yapmak akciğerlere ne kazandırır?": "ne kazandırır", "Uzun süre kaldığımız kapalı ortamlar için ne yapmalıyız?": "ne yapmalıyız", "'Tütün ürünlerinden uzak durmalıyız.' ifadesi için ne söylenebilir?": "ne söylenebilir", "'Ağızdan nefes alıp vermeliyiz.' ifadesi için ne söylenebilir?": "ne söylenebilir"}
BOLGE = {"'Tütün ürünleri sadece solunum sistemi sağlığına zarar verir.' ifadesi neden yanlıştır?": ["ifadesi neden yanlıştır"]}
OKUT = {"u3k8": [
 ["solunum sistemini korumak için yapabileceğin iki davranışı yazmanı", "hava kirliliğinin nedenlerini sıralamanı", "sigaranın zararlarını anlatmanı"],
 ["bağımlılığın ne demek olduğunu tanımlamanı", "bağımlılığa yol açan maddeleri sıralamanı", "Yeşilay'ın ne iş yaptığını anlatmanı"]]}
METINLI = {"u3k8": [
 {"metin": ["Spor yapmak vücudun nefes alıp verme ihtiyacını artırır.", "Bu durum akciğerleri ve solunumda görevli kasları güçlendirir.", "Temiz havada yürüyüş yapmak solunum sistemi için faydalıdır."],
  "soru": "Spor yapmanın akciğerlere faydası nedir?", "bolge": ["akciğerlere faydası nedir"],
  "serit": "Sporun akciğerlere faydası", "kanit": [1],
  "secenekler": ["Akciğerleri ve solunum kaslarını güçlendirmesi", "Nefes alıp verme ihtiyacını azaltması", "Temiz havada yürüyüşü engellemesi"], "dogru": 0, "tuzak": [1, 2],
  "ipucu": "“Akciğerleri” kelimesinin geçtiği cümleyi oku.", "kanitIpucu": "Akciğerlere ne olduğunu söyleyen cümleyi bul.",
  "aciklama": "Spor yapmak nefes alıp verme ihtiyacını artırır; bu da akciğerleri ve solunumda görevli kasları güçlendirir (s. 125).", "kavram": "Spor ve Temiz Hava"},
 {"metin": ["Elif büyük bir şehirde yaşıyor.", "Son zamanlarda nefes darlığı ve öksürük gibi rahatsızlıklar yaşıyordu.", "Doktor, çevrelerindeki yoğun araç trafiği ve fabrikaların hava kirliliğine yol açtığını söyledi.", "Bu kirliliğin solunum sistemi sağlığını olumsuz etkilediğini anlattı.", "Elif'in ailesi bir çözüm yolu aramaya başladı."],
  "soru": "Elif'in solunum sistemi rahatsızlıklarına yol açan durum nedir?", "bolge": ["rahatsızlıklarına yol açan durum nedir"],
  "serit": "Elif'in rahatsızlığına yol açan durum", "kanit": [2, 3],
  "secenekler": ["Araç trafiği ve fabrikaların yol açtığı hava kirliliği", "Büyük bir şehirde yaşamayı sevmesi", "Ailesinin çözüm yolu araması"], "dogru": 0, "tuzak": [1, 2],
  "ipucu": "Doktor rahatsızlığın sebebi olarak neyi söyledi?", "kanitIpucu": "Doktorun söylediklerini anlatan cümlelerden birine dokun.",
  "aciklama": "Yoğun araç trafiği ve fabrikalar hava kirliliğine yol açar; bu kirlilik solunum sistemi sağlığını olumsuz etkiler (s. 123).", "kavram": "Hava Kirliliği"}]}
