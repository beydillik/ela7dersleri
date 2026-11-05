TEKRAR = {"u3k2": [
 ("Sindirim sistemi rahatsızlıkları genellikle {yaşam tarzından|kalıtımdan|iklimden} kaynaklanır. Doğru beslenme, yeterli sıvı alımı ve düzenli {egzersiz|uykusuzluk|ekran süresi} sağlığı korur.", "s. 99"),
 ("Yeterli miktarda protein, karbohidrat, yağ ve vitamin almak sindirim sürecini {dengeler|bozar|durdurur}. Bu besinler bağışıklık sistemini de güçlendirir.", "s. 99"),
 ("Aşırı yağlı, çok baharatlı ve paketli gıdalar mide {rahatsızlıklarına|iyileşmesine} ve aşırı kilo almaya neden olabilir.", "s. 99"),
 ("Yeterli su içmek ve düzenli, dengeli, yeterli {öğünlerle|atıştırmalıklarla|ayaküstü yemeklerle} beslenmek sindirim organlarının sağlıklı çalışmasına yardımcı olur.", "s. 99"),
 ("Düzenli fiziksel aktivite bağırsakların kasılma ve gevşeme hareketlerini {artırır|yavaşlatır|durdurur}. Kan akışı hızlanınca besinler daha {kolay|zor} sindirilir.", "s. 99"),
 ("Uzun süre hareketsiz kalmak bağırsak hareketlerini {yavaşlatır|hızlandırır}. Ekran başında kalan kişi yemeği farkında olmadan {hızlı|yavaş} yiyebilir.", "s. 99"),
 ("Stres sindirim sistemi organlarını olumsuz etkiler. Düzenli spor insanı stresten {uzaklaştırabilir|yaklaştırabilir|etkilemez}.", "s. 99"),
]}
KISA = {"u3k2": [
 {"soru": "Düzenli egzersiz sindirim sistemi sağlığını nasıl etkiler? Yazınız.",
  "tetik": ["nasıl"],
  "okut": ["Etkiyi ve sonucunu yaz (iki parça).", "Tanım yaz: “X, … denir.”", "İki ayrı örnek yaz."],
  "parcalar": [
   {"bas": "Bağırsaklara etkisi:", "ornek": "Bağırsakların kasılma ve gevşeme hareketlerini artırır.", "havuz": ["Bağırsakları tembelleştirir.", "Mide öz suyunu azaltır."], "k": ["hareket"]},
   {"bas": "Sonucu:", "ornek": "Kan dolaşımı artar, besinler daha kolay sindirilir.", "havuz": ["Besinler daha zor sindirilir.", "Öğün sayısı azalır."], "k": ["kolay", "dolaşım"]}],
  "kisa": "Bağırsakların hareketini artırır; kan dolaşımı hızlanır, besinler kolay sindirilir.",
  "cevap": "Düzenli fiziksel aktivite bağırsakların kasılma ve gevşeme hareketlerini artırır. Kan dolaşımı hızlandığı için besinler daha kolay sindirilir.",
  "anahtarlar": [{"ad": "bağırsak hareketini artırır", "k": ["hareket"]}, {"ad": "besinler kolay sindirilir", "k": ["kolay", "dolaşım"]}],
  "sayfa": "s. 99"},
 {"soru": "Ekran başında uzun süre kalmak sindirim sistemine neden zarar verebilir? İki sebep yazınız.",
  "tetik": ["neden", "İki sebep"],
  "okut": ["Neden → iki ayrı sebep yaz.", "Evet ya da hayır yaz, sonra nedenini ekle.", "Önce tanım, sonra örnek yaz."],
  "parcalar": [
   {"bas": "Birinci sebep:", "ornek": "Hareketsiz kalmak bağırsak hareketlerini yavaşlatır.", "havuz": ["Bağırsak hareketlerini hızlandırır.", "Mide öz suyu çoğalır."], "k": ["yavaşlat"]},
   {"bas": "İkinci sebep:", "ornek": "Yemek hızlı ve fazla yenir ya da öğünler atlanır.", "havuz": ["Öğünler tam ve düzenli yenir.", "Su daha çok içilir."], "k": ["hızlı", "fazla", "atlan"]}],
  "kisa": "Hareketsiz kalmak bağırsak hareketlerini yavaşlatır; yemek hızlı ve fazla yenir ya da öğün atlanır.",
  "cevap": "Uzun süre hareketsiz kalmak bağırsak hareketlerini yavaşlatır. Ayrıca yemekler farkında olmadan hızlı ve fazla yenir ya da öğünler atlanır; öne eğilerek oturmak da sindirim sistemine baskı yapar.",
  "anahtarlar": [{"ad": "bağırsak hareketini yavaşlatır", "k": ["yavaşlat"]}, {"ad": "hızlı / fazla yeme ya da öğün atlama", "k": ["hızlı", "fazla", "atla"]}],
  "sayfa": "s. 99"},
]}
ELLE = {"Stresten uzaklaşmak için kitap ne öneriyor?": "ne öneriyor", "Ekran karşısında uzun süre öne eğilerek oturmak neye yol açabilir?": "neye yol açabilir"}
OKUT = {"u3k2": [
 ["egzersizin sindirim sistemine ne yaptığını ve bunun sonucunu anlatmanı", "hangi sporların yapılması gerektiğini sıralamanı", "egzersizin kalbe faydasını anlatmanı"],
 ["ekran başında kalmanın sindirime zarar vermesinin iki sebebini yazmanı", "günde kaç saat ekrana bakılabileceğini söylemeni", "ekranın gözlere zararını anlatmanı"]]}
METINLI = {"u3k2": [
 {"metin": ["Ece her gün ekran başında uzun süre hareketsiz oturuyor.", "Uzun süre hareketsiz kalmak bağırsak hareketlerini yavaşlatır.", "Bu yüzden sindirim süreci olumsuz etkilenir."],
  "soru": "Ece'nin sindirimini olumsuz etkileyen durum nedir?", "bolge": ["sindirimini olumsuz etkileyen durum nedir"],
  "serit": "Ece'nin sindirimini bozan durum", "kanit": [0, 1],
  "secenekler": ["Uzun süre hareketsiz oturması", "Bağırsak hareketlerinin hızlanması", "Her gün çok su içmesi"], "dogru": 0, "tuzak": [1],
  "ipucu": "Ece ne yapıyor? Bu durum bağırsaklara ne oluyor?", "kanitIpucu": "Ece'nin ne yaptığını anlatan cümleyi bul.",
  "aciklama": "Uzun süre hareketsiz kalmak bağırsak hareketlerini yavaşlatır; sindirim süreci bundan olumsuz etkilenir (s. 99).", "kavram": "Ekran Başında Hareketsizlik"},
 {"metin": ["Ruhi bir şirkette masa başında çalışıyor.", "Sabahları evden aceleyle çıktığı için kahvaltı yapmıyor.", "Öğle yemeklerini genellikle atıştırmalık yiyeceklerle geçiştiriyor.", "Akşam yemeklerini hep geç saatlerde yiyor ve bazen su içmeyi unutuyor.", "Spor yapmaya da zaman ayırmıyor.", "Son günlerde midesinde şişkinlik ve kramplar oluyor."],
  "soru": "Ruhi'nin beslenmesinde yapması gereken değişiklik hangisidir?", "bolge": ["beslenmesinde yapması gereken değişiklik hangisidir"],
  "serit": "Ruhi'nin beslenmesinde yapması gereken değişiklik", "kanit": [1, 2, 3],
  "secenekler": ["Öğün atlamadan düzenli ve dengeli beslenmek, yeterli su içmek", "Akşam yemeklerini daha geç saatlerde yemek", "Masa başında daha uzun süre çalışmak"], "dogru": 0, "tuzak": [1],
  "ipucu": "Ruhi'nin yemek ve su alışkanlıklarını anlatan cümlelere bak. Hangisi yanlış bir alışkanlık?", "kanitIpucu": "Ruhi'nin kahvaltı, öğle ya da akşam yemeğini anlatan cümlelerden birine dokun.",
  "aciklama": "Yeterli su içmek; düzenli, dengeli ve yeterli öğünlerle beslenmek sindirim organlarının sağlıklı çalışmasına yardımcı olur (s. 96, 99).", "kavram": "Su ve Düzenli Öğünler"}]}
