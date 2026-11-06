"""Matematik (mat1) dikkat paketi — 4. Tema: Dönüşüm (u4k1–u4k4). 6 Kasım 2026, Kemal onayıyla."""

TEKRAR = {
"u4k1": [
 ("Bir şekli katlayınca iki parçayı tam üst üste getiren doğruya {simetri doğrusu|orta nokta|açıortay} denir.", "s. 203"),
 ("Bir noktanın bir doğruya göre simetriği, o noktanın {yansıma dönüşümü|öteleme|dönme} altındaki görüntüsüdür.", "s. 204"),
 ("Bir nokta ile görüntüsü simetri doğrusuna {eşit|farklı|iki kat} uzaklıktadır.", "s. 205"),
 ("Simetri doğrusu, nokta ile görüntüsünü birleştiren doğru parçasını {dik ortalar|eğik keser|hiç kesmez}.", "s. 205"),
 ("Bir çokgenin görüntüsünü çizmek için önce {köşelerin|kenar uzunluklarının|açılarının} görüntüsünü buluruz.", "s. 204"),
 ("Bir şekil ile yansıma dönüşümü altındaki görüntüsü {eştir|farklı büyüklüktedir|hiç benzemez}.", "s. 205"),
 ("Çizdiğimiz görüntüyü {simetri aynası|hesap makinesi|iletki} ya da asetat kâğıdıyla kontrol ederiz.", "s. 204"),
],
"u4k2": [
 ("Bir şekil bir doğruyla ikiye ayrıldığında iki parça birbirinin {görüntüsüyse|yarısı kadarsa|rengindeyse} şekil simetriktir.", "s. 205"),
 ("İkizkenar üçgenin {1|3|0} simetri doğrusu vardır.", "s. 205"),
 ("Düzgün beşgenin {5|1|10} simetri doğrusu vardır.", "s. 205"),
 ("Çeşitkenar üçgenin ve paralelkenarın simetri doğrusu {yoktur|ikidir|dörttür}.", "s. 205"),
 ("Gizli simetri doğrusunu bulmak için karşılıklı noktaları birleştiren parçalar {paralel|dik değil|farklı uzunlukta} olmalıdır.", "s. 206"),
 ("Bir üçgeni bir kenarına göre yansıtınca üçgen ile görüntüsü birleşir ve bir {dörtgen|daire|doğru} oluşur.", "s. 208"),
],
"u4k3": [
 ("Bir doğru parçasını dik kesen ve iki eş parçaya ayıran doğruya {orta dikme|açıortay|kenar} denir.", "s. 213"),
 ("Bir doğru parçasının simetri doğrusu aynı zamanda o parçanın {orta dikmesidir|açıortayıdır|uzantısıdır}.", "s. 213"),
 ("İnşa, yalnızca pergel ve {ölçüsüz cetvel|iletki|gönye} kullanarak çizim yapmaktır.", "s. 211"),
 ("Orta dikme inşasında A ve B merkezli yayların yarıçapları {eşit|farklı|sıfır} olmalıdır.", "s. 212"),
 ("Yaylar birbirini {iki|bir|hiçbir} noktada kesmelidir.", "s. 213"),
 ("Yayların kesişim noktalarını {ölçüsüz cetvelle|pergelle|iletkiyle} birleştiririz.", "s. 213"),
 ("Orta dikmenin üzerindeki her nokta doğru parçasının iki ucuna {eşit|farklı|en uzak} uzaklıktadır.", "s. 212"),
],
"u4k4": [
 ("Bir açıyı iki eş açıya ayıran ışına {açıortay|orta dikme|kenar} denir.", "s. 214"),
 ("Bir açıya ait simetri doğrusu aynı zamanda o açının {açıortayıdır|orta dikmesidir|köşesidir}.", "s. 214"),
 ("80°'lik bir açının açıortayı onu {40° ve 40°|30° ve 50°|80° ve 80°}'lik iki açıya ayırır.", "s. 214"),
 ("Açıortay inşasında ilk yayı çizerken pergelin sivri ucunu açının {köşesine|bir kolunun ucuna|dışına} koyarız.", "s. 213"),
 ("K ve L noktaları açının köşesine {eşit|farklı|iki kat} uzaklıktadır.", "s. 213"),
 ("K ve L merkezli yaylar {aynı açıklıkta|farklı açıklıkta|açıklık fark etmeden} çizilir.", "s. 213"),
 ("Bir doğru parçasının simetri doğrusu orta dikme, bir açının simetri doğrusu {açıortaydır|kenardır|köşedir}.", "s. 215"),
],
}

KISA = {
"u4k1": [
 {"soru": "Arkadaşın bir üçgenin görüntüsünü çizdi ama bir köşenin görüntüsü simetri doğrusuna daha yakın çıktı. Hatayı nasıl bulur ve düzeltirsin?",
  "tetik": ["nasıl bulur ve düzeltirsin"], "okut": ["", "", ""],
  "parcalar": [
   {"bas": "Hatayı bulmak için:", "ornek": "Köşe ile görüntüsünün doğruya uzaklığını kare kare sayarım.", "havuz": ["Üçgenin rengine bakarım.", "Üçgenin alanını hesaplarım."], "k": ["uzaklı", "say"]},
   {"bas": "Düzeltmek için:", "ornek": "Görüntüyü doğrunun öbür yanına aynı uzaklıkta yeniden koyarım.", "havuz": ["Üçgeni silip hiç çizmem.", "Görüntüyü doğrunun üstüne koyarım."], "k": ["aynı uzaklı", "eşit uzaklı"]}],
  "kisa": "Uzaklıkları say; görüntüyü aynı uzaklığa koy.",
  "cevap": "Köşe ile görüntüsünün simetri doğrusuna uzaklığını kare kare sayarım; eşit değilse hata oradadır. Görüntüyü doğrunun öbür yanına aynı uzaklıkta yeniden koyar, köşeleri birleştiririm.",
  "anahtarlar": [{"ad": "uzaklıkları say", "k": ["uzaklı"]}, {"ad": "aynı uzaklığa koy", "k": ["aynı uzaklı", "eşit uzaklı"]}],
  "sayfa": "s. 205"},
 {"soru": "Bir şekil ile yansıma dönüşümü altındaki görüntüsünde neler aynı kalır, ne değişir? Yaz.",
  "tetik": ["neler aynı kalır, ne değişir"], "okut": ["", "", ""],
  "parcalar": [
   {"bas": "Aynı kalan:", "ornek": "Kenar uzunlukları ve açılar aynı kalır; şekiller eştir.", "havuz": ["Şeklin yeri aynı kalır.", "Hiçbir şey aynı kalmaz."], "k": ["eş", "kenar", "açı"]},
   {"bas": "Değişen:", "ornek": "Yönü ters döner: sağdaki parça solda görünür.", "havuz": ["Şekil iki kat büyür.", "Şeklin rengi değişir."], "k": ["ters", "yön"]}],
  "kisa": "Kenarlar ve açılar aynı; yönü ters.",
  "cevap": "Kenar uzunlukları ve açılar aynı kalır; şekil ile görüntüsü eştir. Yalnızca yönü ters döner: şeklin sağında olan parça görüntüde solda görünür.",
  "anahtarlar": [{"ad": "kenar/açı aynı", "k": ["kenar", "açı"]}, {"ad": "yön ters", "k": ["ters", "yön"]}],
  "sayfa": "s. 205"}],
"u4k2": [
 {"soru": "Paralelkenarı köşegeninden kesince iki eş parça oluşur. Paralelkenar yine de neden simetrik değildir? Yaz.",
  "tetik": ["neden simetrik değildir"], "okut": ["", "", ""],
  "parcalar": [
   {"bas": "Çünkü:", "ornek": "Köşegenden katlayınca parçalar üst üste gelmez.", "havuz": ["Parçalar eş değildir.", "Paralelkenarın köşegeni yoktur."], "k": ["üst üste", "katla"]},
   {"bas": "Yani:", "ornek": "Simetri için eş olmak yetmez; parçalar birbirinin görüntüsü olmalı.", "havuz": ["Her eş parça simetriktir.", "Simetri için renk aynı olmalı."], "k": ["yetmez", "görüntü"]}],
  "kisa": "Katlayınca üst üste gelmez; eş olmak yetmez.",
  "cevap": "Köşegenden katlayınca iki parça üst üste gelmez. Simetri için parçaların eş olması yetmez; birbirinin görüntüsü olmaları gerekir.",
  "anahtarlar": [{"ad": "üst üste gelmez", "k": ["üst üste"]}, {"ad": "eş olmak yetmez", "k": ["yetmez", "görüntü"]}],
  "sayfa": "s. 205"},
 {"soru": "İki eş şeklin gizli bir simetri doğrusuna göre simetrik olup olmadığını nasıl kontrol edersin? Yaz.",
  "tetik": ["nasıl kontrol edersin"], "okut": ["", "", ""],
  "parcalar": [
   {"bas": "Önce:", "ornek": "Karşılıklı noktaları birleştiririm; parçalar paralel mi bakarım.", "havuz": ["Şekillerin alanını hesaplarım.", "Şekilleri renklerine göre ayırırım."], "k": ["paralel"]},
   {"bas": "Sonra:", "ornek": "Parçaların orta noktaları aynı doğru üzerinde mi bakarım.", "havuz": ["En uzun parçayı silerim.", "Parçaları toplarım."], "k": ["orta nokta", "aynı doğru"]}],
  "kisa": "Parçalar paralel mi, orta noktalar tek doğruda mı?",
  "cevap": "Karşılıklı noktaları birleştiririm. Bu parçalar birbirine paralel olmalı ve hepsinin orta noktası aynı doğru üzerinde olmalı; o doğru gizli simetri doğrusudur.",
  "anahtarlar": [{"ad": "parçalar paralel", "k": ["paralel"]}, {"ad": "orta noktalar aynı doğruda", "k": ["orta nokta"]}],
  "sayfa": "s. 206"}],
"u4k3": [
 {"soru": "Arkadaşın orta dikme inşa ederken B merkezli yayı daha küçük açıklıkla çizdi. Ne olur, nasıl düzeltirsin?",
  "tetik": ["Ne olur", "nasıl düzeltirsin"], "okut": ["", "", ""],
  "parcalar": [
   {"bas": "Ne olur:", "ornek": "Yayların kesiştiği noktalar iki uca eşit uzak olmaz; çizilen doğru orta dikme olmaz.", "havuz": ["Hiçbir şey değişmez.", "Doğru parçası uzar."], "k": ["eşit uzak", "orta dikme olmaz"]},
   {"bas": "Düzeltmek için:", "ornek": "İki yayı da aynı pergel açıklığıyla çizerim.", "havuz": ["Cetvelle ölçüp ortaya nokta koyarım.", "Yayları silip iletki kullanırım."], "k": ["aynı açıklık", "aynı pergel"]}],
  "kisa": "Orta dikme olmaz; iki yayı aynı açıklıkla çiz.",
  "cevap": "Yaylar eş olmadığı için kesişim noktaları iki uca eşit uzak olmaz; çizilen doğru parçayı ortadan kesmez, orta dikme olmaz. Düzeltmek için iki yayı da aynı pergel açıklığıyla çizerim.",
  "anahtarlar": [{"ad": "orta dikme olmaz", "k": ["eşit uzak", "orta dikme olmaz"]}, {"ad": "aynı açıklık", "k": ["aynı pergel", "aynı açıklık"]}],
  "sayfa": "s. 212"},
 {"soru": "Orta dikme inşasında pergel açıklığı neden AB'nin yarısından uzun olmalıdır? Yaz.",
  "tetik": ["neden AB'nin yarısından uzun olmalıdır"], "okut": ["", "", ""],
  "parcalar": [
   {"bas": "Kısa olursa:", "ornek": "Yaylar birbirine değmez, kesişmez.", "havuz": ["Yaylar çok kalın olur.", "Pergel kırılır."], "k": ["değmez", "kesişmez"]},
   {"bas": "Bu yüzden:", "ornek": "İki kesişim noktası bulamayız, orta dikmeyi çizemeyiz.", "havuz": ["Doğru parçası kısalır.", "Açıortay çizmiş oluruz."], "k": ["kesişim", "çizemeyiz"]}],
  "kisa": "Yoksa yaylar kesişmez; kesişim noktası çıkmaz.",
  "cevap": "Açıklık AB'nin yarısından kısa olursa yaylar birbirine değmez, kesişmez. O zaman iki kesişim noktası bulamayız ve orta dikmeyi çizemeyiz.",
  "anahtarlar": [{"ad": "yaylar kesişmez", "k": ["kesişmez", "değmez"]}, {"ad": "kesişim noktası çıkmaz", "k": ["kesişim"]}],
  "sayfa": "s. 212"}],
"u4k4": [
 {"soru": "Orta dikme inşası ile açıortay inşası arasında hangi benzerlik ve fark var? Yaz.",
  "tetik": ["hangi benzerlik ve fark var"], "okut": ["", "", ""],
  "parcalar": [
   {"bas": "Benzerlik:", "ornek": "İkisinde de pergelle eş yaylar çizip kesişim noktasını buluruz.", "havuz": ["İkisinde de iletkiyle ölçeriz.", "İkisinde de cetvelle uzunluk ölçeriz."], "k": ["eş yay", "pergel"]},
   {"bas": "Fark:", "ornek": "Orta dikme bir doğru parçası için, açıortay bir açı için çizilir.", "havuz": ["Açıortay yalnız karede çizilir.", "Orta dikme yalnız dairede çizilir."], "k": ["doğru parçası", "açı için"]}],
  "kisa": "İkisinde eş yaylar; biri parça, öteki açı için.",
  "cevap": "İkisinde de pergel ve ölçüsüz cetvel kullanır, eş yaylar çizip kesişim noktasını buluruz. Orta dikme bir doğru parçasının, açıortay ise bir açının simetri doğrusudur.",
  "anahtarlar": [{"ad": "eş yaylar / pergel", "k": ["eş yay", "pergel"]}, {"ad": "parça / açı", "k": ["parça", "açı"]}],
  "sayfa": "s. 215"},
 {"soru": "Açıortay inşasının ilk adımında K ve L noktaları neden köşeye eşit uzaklıktadır? Yaz.",
  "tetik": ["neden köşeye eşit uzaklıktadır"], "okut": ["", "", ""],
  "parcalar": [
   {"bas": "Çünkü:", "ornek": "İkisi de köşe merkezli aynı yayın üzerindedir.", "havuz": ["İkisi de açının dışındadır.", "İkisi de cetvelle ölçüldü."], "k": ["aynı yay", "köşe merkez"]},
   {"bas": "Yani:", "ornek": "Uzaklıkları pergel açıklığı kadardır: AK = AL.", "havuz": ["AK, AL'nin iki katıdır.", "Uzaklıkları hiç bilinmez."], "k": ["pergel açıklığı", "AK = AL"]}],
  "kisa": "Aynı yayın üzerinde; AK = AL.",
  "cevap": "K ve L, köşe merkezli aynı yayın kollarla kesiştiği noktalardır. İkisinin de köşeye uzaklığı pergel açıklığı kadardır: AK = AL.",
  "anahtarlar": [{"ad": "aynı yay", "k": ["aynı yay"]}, {"ad": "AK = AL", "k": ["AK = AL"]}],
  "sayfa": "s. 213"}],
}

OKUT = {
"u4k1": [
 ["arkadaşının hatasını nasıl bulup düzelteceğini yazmanı", "üçgenin görüntüsünü çizmeni", "simetri doğrusunu tanımlamanı"],
 ["şekil ile görüntüsünde neyin aynı kaldığını ve neyin değiştiğini yazmanı", "şeklin görüntüsünü çizmeni", "yalnız neyin değiştiğini söylemeni"]],
"u4k2": [
 ["paralelkenarın neden simetrik olmadığını yazmanı", "paralelkenarın köşegenini çizmeni", "simetrik bir şekil örneği vermeni"],
 ["iki eş şeklin simetrik olup olmadığını nasıl kontrol edeceğini yazmanı", "iki şekli üst üste çizmeni", "şekillerin kaç köşesi olduğunu saymanı"]],
"u4k3": [
 ["küçük yay çizilince ne olacağını ve nasıl düzelteceğini yazmanı", "orta dikmeyi tanımlamanı", "AB'nin uzunluğunu ölçmeni"],
 ["pergel açıklığının neden AB'nin yarısından uzun olması gerektiğini yazmanı", "AB'nin yarısını hesaplamanı", "pergelin nasıl tutulduğunu anlatmanı"]],
"u4k4": [
 ["iki inşa arasındaki benzerliği ve farkı yazmanı", "açıortayı tanımlamanı", "yalnız orta dikme inşasını anlatmanı"],
 ["K ve L'nin neden köşeye eşit uzak olduğunu yazmanı", "K ve L noktalarını çizmeni", "açının kaç derece olduğunu bulmanı"]],
}

METINLI = {
"u4k1": [
 {"metin": ["Kareli kâğıtta dikey bir simetri doğrusu çizildi.", "A noktası doğrunun 4 kare solunda.", "B noktası ise doğrunun 2 kare sağında."],
  "soru": "Metne göre A noktasının görüntüsü doğrunun kaç kare sağında olur?", "bolge": ["A noktasının görüntüsü", "kaç kare sağında olur"],
  "serit": "A′ noktasının doğruya uzaklığı", "kanit": [1],
  "secenekler": ["4 kare", "2 kare", "8 kare"], "dogru": 0, "tuzak": [],
  "ipucu": "Nokta ile görüntüsü simetri doğrusuna eşit uzaklıktadır. Soru A'yı soruyor.", "kanitIpucu": "A noktasından söz eden cümleyi bul.",
  "aciklama": "A doğrunun 4 kare solunda, görüntüsü 4 kare sağında olur. 2 kare B'nin uzaklığı; 8 kare A ile A′ arası (s. 205).", "kavram": "Eşit Uzaklık"},
 {"metin": ["Elif aynanın önüne bir oyuncak araba koydu.", "Araba aynaya 15 cm uzaklıkta duruyordu.", "Arabanın uzunluğu 10 cm idi.", "Elif aynada arabanın görüntüsünü gördü.", "Görüntüdeki arabanın burnu ters tarafa bakıyordu.", "Elif bunu defterine çizdi."],
  "soru": "Metne göre arabanın görüntüsü aynaya kaç cm uzaklıkta görünür?", "bolge": ["görüntüsü aynaya kaç cm uzaklıkta görünür"],
  "serit": "Görüntünün aynaya uzaklığı", "kanit": [1],
  "secenekler": ["15 cm", "10 cm", "30 cm"], "dogru": 0, "tuzak": [],
  "ipucu": "Nesne ile görüntüsü aynaya eşit uzaklıktadır.", "kanitIpucu": "Arabanın aynaya uzaklığını veren cümleyi bul.",
  "aciklama": "Nesne ile görüntüsü aynaya eşit uzaklıktadır: 15 cm. 10 cm arabanın uzunluğu, 30 cm araba ile görüntüsü arası (s. 204–205). Hikâye kitap dışı.", "kavram": "Yansıma Dönüşümü"}],
"u4k2": [
 {"metin": ["Öğretmen tahtaya bir ikizkenar üçgen, bir düzgün beşgen ve bir yarım daire çizdi.", "İkizkenar üçgenin 1, düzgün beşgenin 5, yarım dairenin 1 simetri doğrusu olduğunu gösterdi.", "Sonra her şeklin altına adını yazdı."],
  "soru": "Metne göre en çok simetri doğrusu olan şekil hangisidir?", "bolge": ["en çok simetri doğrusu olan şekil hangisidir"],
  "serit": "En çok simetri doğrusu olan şekil", "kanit": [1],
  "secenekler": ["Düzgün beşgen", "İkizkenar üçgen", "Yarım daire"], "dogru": 0, "tuzak": [],
  "ipucu": "Sayıları karşılaştır; soru en çoğu soruyor.", "kanitIpucu": "Simetri doğrusu sayılarını veren cümleyi bul.",
  "aciklama": "Düzgün beşgenin 5, ikizkenar üçgenin ve yarım dairenin 1'er simetri doğrusu vardır; en çok düzgün beşgen. Kitap bu sayıları etkinlikte öğrenciye buldurur (s. 205).", "kavram": "Birden Çok Simetri Doğrusu"},
 {"metin": ["Can kâğıttan bir paralelkenar kesti.", "Paralelkenarı bir köşegeninden kesip ikiye ayırdı.", "İki parçanın eş olduğunu gördü.", "Sonra parçaları köşegenden katlayarak üst üste getirmeye çalıştı.", "Parçalar tam üst üste gelmedi.", "Can paralelkenarın simetrik olup olmadığını düşündü."],
  "soru": "Metne göre paralelkenarın simetrik olmadığını gösteren bilgi hangisidir?", "bolge": ["simetrik olmadığını gösteren bilgi hangisidir"],
  "serit": "Simetrik olmadığını gösteren bilgi", "kanit": [4],
  "secenekler": ["Katlayınca parçalar üst üste gelmedi.", "İki parça eş çıktı.", "Can kâğıttan kesti."], "dogru": 0, "tuzak": [1, 2],
  "ipucu": "Simetri için eş olmak yetmez; parçalar katlayınca çakışmalı.", "kanitIpucu": "Katlayınca ne olduğunu söyleyen cümleyi bul.",
  "aciklama": "Paralelkenarın parçaları eş olsa da katlayınca çakışmaz; simetri doğrusu yoktur (s. 205). Hikâye kitap dışı.", "kavram": "Simetri Doğrusu Olmayan Şekiller"}],
"u4k3": [
 {"metin": ["Kerim AB doğru parçasının orta dikmesini inşa ediyor.", "Önce A merkezli bir yay, sonra aynı açıklıkla B merkezli bir yay çizdi.", "Yaylar K ve L noktalarında kesişti."],
  "soru": "Metne göre Kerim orta dikmeyi bulmak için hangi noktaları birleştirmelidir?", "bolge": ["hangi noktaları birleştirmelidir"],
  "serit": "Birleştirilecek noktalar", "kanit": [2],
  "secenekler": ["K ve L", "A ve B", "A ve K"], "dogru": 0, "tuzak": [],
  "ipucu": "Yayların kesiştiği iki noktayı ölçüsüz cetvelle birleştiririz.", "kanitIpucu": "Yayların kesiştiği noktaları söyleyen cümleyi bul.",
  "aciklama": "Yayların kesişim noktaları K ve L birleştirilince orta dikme çıkar. A ve B parçanın uçlarıdır (s. 212–213).", "kavram": "Orta Dikme İnşası"},
 {"metin": ["Sınıfta iki ağacın arasına bir bank konacak.", "Bank iki ağaca eşit uzaklıkta olmalı.", "Ela ağaçları kareli kâğıtta A ve B noktalarıyla gösterdi.", "Sonra AB'nin orta dikmesini pergel ve ölçüsüz cetvelle inşa etti.", "Bankın rengini de maviye boyamayı önerdi.", "Öğretmen Ela'nın çizimini panoya astı."],
  "soru": "Metne göre bank nereye konmalıdır?", "bolge": ["bank nereye konmalıdır"],
  "serit": "İki ağaca eşit uzak yer", "kanit": [1, 3],
  "secenekler": ["AB'nin orta dikmesi üzerindeki bir noktaya", "A noktasının hemen yanına", "Panonun önüne"], "dogru": 0, "tuzak": [2],
  "ipucu": "Orta dikmenin üzerindeki her nokta iki uca eşit uzaklıktadır.", "kanitIpucu": "Bankın nasıl bir yerde olması gerektiğini söyleyen cümleyi bul.",
  "aciklama": "Orta dikmenin üzerindeki her nokta A'ya ve B'ye eşit uzaklıktadır (s. 212). Hikâye kitap dışı.", "kavram": "İki Uca Eşit Uzak"}],
"u4k4": [
 {"metin": ["Deniz 70°'lik bir açı çizdi.", "Açının açıortayını pergel ve ölçüsüz cetvelle inşa etti.", "Açıortay açıyı iki eş açıya ayırdı."],
  "soru": "Metne göre oluşan açılardan her biri kaç derecedir?", "bolge": ["her biri kaç derecedir"],
  "serit": "Açıortayın oluşturduğu her açı", "kanit": [0, 2],
  "secenekler": ["35°", "70°", "140°"], "dogru": 0, "tuzak": [],
  "ipucu": "Açıortay açıyı iki eş açıya ayırır: her biri açının yarısıdır.", "kanitIpucu": "Açının ölçüsünü veren cümleyi bul.",
  "aciklama": "70° ÷ 2 = 35°. 70° bütün açıdır (s. 214). Açı ölçüsü kitap dışı.", "kavram": "İki Eş Açı"},
 {"metin": ["Mert bir açının açıortayını inşa ediyor.", "Pergelin sivri ucunu açının köşesine koydu ve iki kolu kesen bir yay çizdi.", "Yayın kolları kestiği noktalara K ve L adını verdi.", "Sonra K ve L merkezli, aynı açıklıkta iki yay çizdi.", "Bu yaylar E noktasında kesişti.", "Mert kâğıdını çantasına koymadan önce adını yazdı."],
  "soru": "Metne göre açıortayı çizmek için Mert son olarak hangi noktaları birleştirmelidir?", "bolge": ["son olarak hangi noktaları birleştirmelidir"],
  "serit": "Açıortay için son adımda birleştirilecek noktalar", "kanit": [4],
  "secenekler": ["Köşe ile E", "K ile L", "K ile E"], "dogru": 0, "tuzak": [],
  "ipucu": "Yayların kesiştiği nokta köşeyle birleştirilir.", "kanitIpucu": "Yayların kesiştiği noktayı söyleyen cümleyi bul.",
  "aciklama": "E noktası köşeyle birleştirilince açıortay çıkar. K ile L'yi birleştirmek açıortay değil, KL parçasını verir (s. 213–214).", "kavram": "Açıortay İnşası"}],
}
