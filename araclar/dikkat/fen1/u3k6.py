TEKRAR = {"u3k6": [
 ("Uyku düzeni, yeterli ve dengeli beslenme, sosyal ve sportif faaliyetler dolaşım sistemi sağlığına {olumlu|olumsuz} etki eder; teknoloji bağımlılığının etkisi ise {olumsuzdur|olumludur}.", "s. 114"),
 ("Çocukların günde {8-10|4-5|12-14}, yetişkinlerin ise {7-9|2-3|11-12} saat uyuması gerekir.", "s. 115"),
 ("Kalp ve damar sağlığı için yeterli {su|şekerli içecek} içilmeli; hazır gıdalardan, aşırı şeker ve {tuzdan|sebzeden|meyveden} kaçınılmalıdır.", "s. 115"),
 ("Zeytinyağı, ceviz yağı ve fındık yağı gibi {sağlıklı|zararlı} yağlar; meyve, sebze ve tam tahıllı gıdalar kalp ve damar sağlığı için tercih edilmelidir.", "s. 115"),
 ("Spor yapmak kanın vücutta {hızlı|yavaş} dolaşımını sağlar; böylece organlara daha fazla {oksijen ve besin|atık madde} iletilir.", "s. 115"),
 ("Sosyal ve sportif faaliyetler kişiyi {stresten|uykudan|sudan} uzak tutarak kalp ve damar sağlığını korur.", "s. 115"),
 ("Uzun süre ekran başında kalmak {hareketsizliğe|hareketliliğe} neden olur ve dolaşım sistemi rahatsızlıklarına yol açabilir. Bunun için ekran süresi {kısaltılmalı|uzatılmalı} ya da kısa yürüyüşler yapılmalıdır.", "s. 115"),
]}
KISA = {"u3k6": [
 {"soru": "Spor yapmak dolaşım sistemi sağlığını nasıl korur? Yazınız.",
  "tetik": ["nasıl"],
  "okut": ["Etkiyi ve sonucunu yaz (iki parça).", "Tanım yaz: “X, … denir.”", "İki ayrı örnek yaz."],
  "parcalar": [
   {"bas": "Kana etkisi:", "ornek": "Kanın vücutta hızlı dolaşmasını sağlar.", "havuz": ["Kanın dolaşımını yavaşlatır.", "Kanı koyulaştırır."], "k": ["hızlı"]},
   {"bas": "Sonucu:", "ornek": "Organlara daha fazla oksijen ve besin iletilir; kişiyi stresten uzak tutar.", "havuz": ["Kalbin çalışması durur.", "Kan hücreleri azalır."], "k": ["oksijen", "stres"]}],
  "kisa": "Kanın hızlı dolaşmasını sağlar; organlara daha fazla oksijen ve besin gider, stresi azaltır.",
  "cevap": "Spor yapmak kanın vücutta hızlı dolaşmasını sağlar. Böylece organlara daha fazla oksijen ve besin iletilir; ayrıca kişiyi stresten uzak tutarak kalp ve damar sağlığını korur.",
  "anahtarlar": [{"ad": "kan hızlı dolaşır", "k": ["hızlı"]}, {"ad": "organlara daha çok oksijen ve besin / stresten uzak tutar", "k": ["oksijen", "stres"]}],
  "sayfa": "s. 115"},
 {"soru": "Uzun süre ekran başında kalmak dolaşım sistemine neden zarar verir? Yazınız.",
  "tetik": ["neden"],
  "okut": ["Davranışı ve sonucunu yaz (iki parça).", "Benzerlik ve fark yaz.", "Evet ya da hayır yaz."],
  "parcalar": [
   {"bas": "Davranış:", "ornek": "Uzun süre hareketsiz kalmaya neden olur.", "havuz": ["Çok hareket ettirir.", "Çok su içirir."], "k": ["hareketsiz"]},
   {"bas": "Sonuç:", "ornek": "Kalbi ve kan dolaşımını olumsuz etkileyerek rahatsızlıklara yol açar.", "havuz": ["Kan dolaşımını hızlandırarak korur.", "Kalbi güçlendirir."], "k": ["olumsuz", "rahatsız"]}],
  "kisa": "Hareketsiz kalmaya neden olur; kalbi ve kan dolaşımını olumsuz etkiler.",
  "cevap": "Uzun süre ekran başında vakit geçirmek hareketsiz kalmaya neden olur. Bu durum kalbi ve kan dolaşımını olumsuz etkileyerek dolaşım sistemi rahatsızlıklarına yol açar.",
  "anahtarlar": [{"ad": "hareketsiz kalma", "k": ["hareketsiz"]}, {"ad": "kalbi / dolaşımı olumsuz etkiler", "k": ["olumsuz", "rahatsız"]}],
  "sayfa": "s. 115"},
]}
ELLE = {"Mehmet'in damar rahatsızlığı yaşamasının nedeni neydi?": "nedeni neydi", "'Düzenli egzersiz kan dolaşımını yavaşlatır.' ifadesi için ne söylenebilir?": "ne söylenebilir", "Uzun süre ekran başında kalan biri dolaşım sistemi için ne yapmalıdır?": "ne yapmalıdır", "Çevremizdeki insanlar için ne yapmalıyız?": "ne yapmalıyız"}
OKUT = {"u3k6": [
 ["sporun kana ne yaptığını ve bunun dolaşıma faydasını anlatmanı", "hangi sporu yapman gerektiğini söylemeni", "sporun kaslara faydasını anlatmanı"],
 ["ekran başında uzun kalmanın dolaşım sistemine neden zarar verdiğini, sebebiyle yazmanı", "ekran süresinin kaç saat olması gerektiğini söylemeni", "ekranın uykuya etkisini anlatmanı"]]}
METINLI = {"u3k6": [
 {"metin": ["Çocukların günde 8-10 saat uyuması gerekir.", "Düzenli uyku dolaşım sisteminin sağlığı için çok önemlidir.", "Selin ise her gece 6 saat uyuyor."],
  "soru": "Selin'in dolaşım sistemi sağlığı için ne yapması gerekir?", "bolge": ["ne yapması gerekir"],
  "serit": "Selin'in yapması gereken", "kanit": [0],
  "secenekler": ["Her gece 8-10 saat uyumak", "Her gece 6 saat uyumaya devam etmek", "Daha az su içmek"], "dogru": 0, "tuzak": [1],
  "ipucu": "Çocukların kaç saat uyuması gerekiyor? Selin kaç saat uyuyor?", "kanitIpucu": "Çocukların kaç saat uyuması gerektiğini söyleyen cümleyi bul.",
  "aciklama": "Çocukların günde 8-10 saat uyuması gerekir; düzenli uyku dolaşım sistemi sağlığı için çok önemlidir (s. 115).", "kavram": "Düzenli Uyku"},
 {"metin": ["Mehmet akşam yemeğinde çok yağlı ve tuzlu yiyecekler yedikten sonra başının şiddetle ağrıdığını fark etti.", "Doktor testlerden sonra ona damar rahatsızlığı olduğunu söyledi.", "Mehmet gün içinde çok hareket etmediğini, genellikle yağlı, tuzlu ve hazır gıdalar yediğini anlattı.", "Doktor ona yeterince su içmesini; az yağlı, az tuzlu, taze yiyecekler yemesini söyledi.", "Sporu da hayatının bir parçası yapmasını istedi."],
  "soru": "Doktorun Mehmet'e önerdiği beslenme hangisidir?", "bolge": ["önerdiği beslenme hangisidir"],
  "serit": "Doktorun önerdiği beslenme", "kanit": [3],
  "secenekler": ["Az yağlı, az tuzlu ve taze yiyecekler yemek", "Yağlı, tuzlu ve hazır gıdalar yemek", "Akşamları daha çok yemek"], "dogru": 0, "tuzak": [1],
  "ipucu": "Soru Mehmet'in ne yediğini değil, doktorun ne önerdiğini soruyor.", "kanitIpucu": "Doktorun Mehmet'e ne söylediğini anlatan cümleyi bul.",
  "aciklama": "Doktor yeterince su içmesini; az yağlı, az tuzlu, taze ve sağlıklı yiyecekler yemesini önerdi. Hazır gıdalardan, aşırı şeker ve tuzdan kaçınılmalıdır (s. 113, 115).", "kavram": "Yağlı, Tuzlu ve Hazır Gıdalar"}]}
