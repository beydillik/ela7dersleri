"""Fen (fen1) okuma pilotu verisi — 11 Kasım 2026 (Kemal'in kararı; ders.json "okuPilot": true).
Öğren: sorunun kalbine dokunma yok, soru kelimesi sarı vurgulu (VURGU yoksa tetik). Test (u3k1, u3k2): iki seçenekli
"Bu soru senden ne istiyor?" (NE) ve ikiz sorular (IKIZ: aynı kök, tek kelime farkı, art arda). Sözlükler: araclar/dikkat/uret.py başlığı."""

# Soru kelimesinin yanında anlamı değiştiren sözcük olan sorular (yalnız bunlarda; diğerlerinde tetik yeter)
VURGU = {
 "Şehirde teleskopla net görüntü almayı en çok ne zorlaştırır?": ["en çok ne zorlaştırır"],
 "Kan bağışı yapabilmek için en az kaç yaşında olmak gerekir?": ["en az kaç"],
 "Kan bağışında ilk adım hangisidir?": ["ilk adım hangisidir"],
 "Bağışlanan organ bir hastaya verilirken önce neye bakılır?": ["önce neye bakılır"],
 "Çocukların günde kaç saat uyuması gerekir?": ["Çocukların", "kaç saat"],
 "Aşağıdakilerden hangisi dolaşım sistemi sağlığına zarar verir?": ["hangisi", "zarar verir"],
 "Kalp ve damar sağlığı için hangisinden kaçınmalıyız?": ["hangisinden kaçınmalıyız"],
 "Soluk alırken diyafram ne yapar?": ["Soluk alırken", "ne yapar"],
 "Kitaptaki ağaç benzetmesinde ağacın gövdesi hangi yapıya benzetilir?": ["gövdesi", "hangi yapıya"],
 # ikizler: farkı yaratan sözcük + soru kelimesi
 "Karbohidratların kimyasal sindirimi nerede başlar?": ["Karbohidratların", "nerede"],
 "Proteinlerin kimyasal sindirimi nerede başlar?": ["Proteinlerin", "nerede"],
 "Besinlerin sindirimi hangi organda başlar?": ["hangi organda başlar"],
 "Besinlerin sindirimi hangi organda tamamlanır?": ["hangi organda tamamlanır"],
 "Hangisi fiziksel sindirime örnektir?": ["Hangisi fiziksel"],
 "Hangisi kimyasal sindirime örnektir?": ["Hangisi kimyasal"],
 "Karaciğerin salgıladığı safra sıvısı nereye gönderilir?": ["nereye gönderilir"],
 "Karaciğerin salgıladığı safra sıvısı nerede toplanır?": ["nerede toplanır"],
 "Düzenli egzersiz bağırsak hareketlerini nasıl etkiler?": ["Düzenli egzersiz", "nasıl etkiler"],
 "Uzun süre hareketsiz kalmak bağırsak hareketlerini nasıl etkiler?": ["Uzun süre hareketsiz kalmak", "nasıl etkiler"],
 "Hangisi sindirim sistemi sağlığı için doğru bir davranıştır?": ["Hangisi", "doğru"],
 "Hangisi sindirim sistemi sağlığı için yanlış bir davranıştır?": ["Hangisi", "yanlış"],
 "Özden'in hangi alışkanlığı sindirim sistemi için hatalıdır?": ["hangi alışkanlığı", "hatalıdır"],
 "Özden'in hangi alışkanlığı doğrudur?": ["hangi alışkanlığı doğrudur"],
}

# Test'e eklenen ikiz sorular (bilgiler kitaptan; sayfalar: [s. N] işaretinin üstündeki metin N. sayfadadır)
EKSORU = {
 "u3k1": [
  {"soru": "Proteinlerin kimyasal sindirimi nerede başlar?", "secenekler": ["Ağızda", "Midede", "İnce bağırsakta"], "dogru": 1,
   "ipucu": "Mide öz suyundaki enzimler hangi besine etki ediyordu?",
   "aciklama": "Mide öz suyundaki enzimlerle proteinlerin kimyasal sindirimi midede başlar. (s. 95)", "kavram": "Mide"},
  {"soru": "Besinlerin sindirimi hangi organda başlar?", "secenekler": ["Ağızda", "Midede", "İnce bağırsakta"], "dogru": 0,
   "ipucu": "Besinin vücuda alındığı ilk organı düşün.",
   "aciklama": "Fiziksel ve kimyasal sindirim ağızda başlar. (s. 95)", "kavram": "Ağız"},
  {"soru": "Hangisi kimyasal sindirime örnektir?", "secenekler": ["Besinin dişlerle çiğnenmesi", "Enzimlerin besini yapı taşlarına ayırması", "Villusların besini emmesi"], "dogru": 1,
   "ipucu": "Kimyasal sindirimde besini ne ayrıştırıyordu?",
   "aciklama": "Enzimler ve su besini yapı taşlarına ayırır; bu kimyasal sindirimdir. (s. 92)", "kavram": "Sindirim"},
  {"soru": "Karaciğerin salgıladığı safra sıvısı nerede toplanır?", "secenekler": ["Safra kesesinde", "İnce bağırsakta", "Midede"], "dogru": 0,
   "ipucu": "Karaciğerin altındaki küçük keseyi hatırla.",
   "aciklama": "Safra sıvısı karaciğerin altındaki safra kesesinde toplanır; sonra ince bağırsağa gönderilir. (s. 92)", "kavram": "Karaciğer ve Pankreas"},
 ],
 "u3k2": [
  {"soru": "Düzenli egzersiz bağırsak hareketlerini nasıl etkiler?", "secenekler": ["Artırır", "Yavaşlatır", "Etkilemez"], "dogru": 0,
   "ipucu": "Sen hareket edince bağırsakların da çalışır.",
   "aciklama": "Düzenli fiziksel aktivite bağırsakların kasılma ve gevşeme hareketlerini uyarır, hareketliliğini artırır. (s. 99)", "kavram": "Düzenli Egzersiz"},
  {"soru": "Uzun süre hareketsiz kalmak bağırsak hareketlerini nasıl etkiler?", "secenekler": ["Artırır", "Yavaşlatır", "Etkilemez"], "dogru": 1,
   "ipucu": "Sen durunca bağırsaklarına ne olur?",
   "aciklama": "Uzun süre hareketsiz kalmak bağırsak hareketlerini yavaşlatır. (s. 99)", "kavram": "Ekran Başında Hareketsizlik"},
  {"soru": "Hangisi sindirim sistemi sağlığı için yanlış bir davranıştır?", "secenekler": ["Öğünleri atıştırmalıkla geçiştirmek", "Yeterli su içmek", "Düzenli egzersiz yapmak"], "dogru": 0,
   "ipucu": "Su ve Düzenli Öğünler kartını hatırla.",
   "aciklama": "Düzenli, dengeli ve yeterli öğünler sindirime yardım eder. Öğünleri atıştırmalıkla geçiştirmek bu düzeni bozar. (s. 99)", "kavram": "Su ve Düzenli Öğünler"},
 ],
}

IKIZ = {
 "u3k1": [
  ["Karbohidratların kimyasal sindirimi nerede başlar?", "Proteinlerin kimyasal sindirimi nerede başlar?"],
  ["Besinlerin sindirimi hangi organda başlar?", "Besinlerin sindirimi hangi organda tamamlanır?"],
  ["Hangisi fiziksel sindirime örnektir?", "Hangisi kimyasal sindirime örnektir?"],
  ["Karaciğerin salgıladığı safra sıvısı nereye gönderilir?", "Karaciğerin salgıladığı safra sıvısı nerede toplanır?"],
 ],
 "u3k2": [
  ["Düzenli egzersiz bağırsak hareketlerini nasıl etkiler?", "Uzun süre hareketsiz kalmak bağırsak hareketlerini nasıl etkiler?"],
  ["Hangisi sindirim sistemi sağlığı için doğru bir davranıştır?", "Hangisi sindirim sistemi sağlığı için yanlış bir davranıştır?"],
  ["Özden'in hangi alışkanlığı sindirim sistemi için hatalıdır?", "Özden'in hangi alışkanlığı doğrudur?"],
 ],
}

# Testte sorulan soru sayısı eskisiyle aynı kalır (havuz büyüdü; her çözüşte sorular değişir)
TESTSORU = {"u3k1": 11, "u3k2": 9}

# "Bu soru senden ne istiyor?" — [doğru, yanlış]; yanlış = Ela'nın tipik yanlış okuması (ikizlerde eşinin istediği)
NE = {
 # u3k1
 "Karbohidratların kimyasal sindirimi nerede başlar?": ["Karbohidratların sindiriminin başladığı yeri", "Proteinlerin sindiriminin başladığı yeri"],
 "Proteinlerin kimyasal sindirimi nerede başlar?": ["Proteinlerin sindiriminin başladığı yeri", "Karbohidratların sindiriminin başladığı yeri"],
 "Besinlerin sindirimi hangi organda başlar?": ["Sindirimin başladığı organı", "Sindirimin tamamlandığı organı"],
 "Besinlerin sindirimi hangi organda tamamlanır?": ["Sindirimin tamamlandığı organı", "Sindirimin başladığı organı"],
 "Hangisi fiziksel sindirime örnektir?": ["Fiziksel sindirime bir örneği", "Kimyasal sindirime bir örneği"],
 "Hangisi kimyasal sindirime örnektir?": ["Kimyasal sindirime bir örneği", "Fiziksel sindirime bir örneği"],
 "Karaciğerin salgıladığı safra sıvısı nereye gönderilir?": ["Safranın gönderildiği yeri", "Safranın toplandığı yeri"],
 "Karaciğerin salgıladığı safra sıvısı nerede toplanır?": ["Safranın toplandığı yeri", "Safranın gönderildiği yeri"],
 "Besinlerin sindirim sisteminde izlediği doğru yol hangisidir?": ["Besinin geçtiği organların sırasını", "Sindirimin başladığı organı"],
 "Fiziksel sindirimin kimyasal sindirime faydası nedir?": ["Fiziksel sindirimin kimyasal sindirime nasıl yardım ettiğini", "Fiziksel sindirimin ne olduğunu"],
 "Aşağıdakilerden hangisi sindirime yardımcı olan bir organdır?": ["Sindirime yardım eden organı", "Besinin içinden geçtiği organı"],
 "Elma parçaları mideye ulaşınca ne olur?": ["Elmaya midede ne olduğunu", "Elmaya ağızda ne olduğunu"],
 "Sindirilmeyen besinler vücuttan hangi yapıyla uzaklaştırılır?": ["Atıkların vücuttan atıldığı yapıyı", "Besinlerin emildiği yapıyı"],
 "Safra sıvısının görevi nedir?": ["Safranın ne işe yaradığını", "Safrayı hangi organın salgıladığını"],
 # u3k2
 "Düzenli egzersiz bağırsak hareketlerini nasıl etkiler?": ["Egzersizin bağırsaklara etkisini", "Hareketsizliğin bağırsaklara etkisini"],
 "Uzun süre hareketsiz kalmak bağırsak hareketlerini nasıl etkiler?": ["Hareketsizliğin bağırsaklara etkisini", "Egzersizin bağırsaklara etkisini"],
 "Hangisi sindirim sistemi sağlığı için doğru bir davranıştır?": ["Sindirim için doğru olan davranışı", "Sindirim için yanlış olan davranışı"],
 "Hangisi sindirim sistemi sağlığı için yanlış bir davranıştır?": ["Sindirim için yanlış olan davranışı", "Sindirim için doğru olan davranışı"],
 "Özden'in hangi alışkanlığı sindirim sistemi için hatalıdır?": ["Özden'in hatalı alışkanlığını", "Özden'in doğru alışkanlığını"],
 "Özden'in hangi alışkanlığı doğrudur?": ["Özden'in doğru alışkanlığını", "Özden'in hatalı alışkanlığını"],
 "Sindirim sistemi rahatsızlıkları genellikle neden kaynaklanır?": ["Rahatsızlıkların sebebini", "Rahatsızlıkların sonucunu"],
 "Ruhi kahvaltı yapmıyor, öğle yemeğini atıştırmalıkla geçiştiriyor, az su içiyor ve spor yapmıyor. Hangi değişiklik ona iyi gelir?": ["Ruhi'ye iyi gelecek değişikliği", "Ruhi'nin yaptığı hatayı"],
 "Hareket ettiğimizde kan dolaşımı artar. Bunun sindirime faydası nedir?": ["Kan dolaşımı artınca sindirime ne faydası olduğunu", "Kan dolaşımının neden arttığını"],
 "Ekran karşısında uzun süre öne eğilerek oturmak neye yol açabilir?": ["Öne eğilerek oturmanın sonucunu", "Öne eğilerek oturmanın sebebini"],
 "Uzun ekran süresi yemek yemeyi nasıl etkileyebilir?": ["Ekranın yemek yeme biçimine etkisini", "Ekranın bağırsak hareketlerine etkisini"],
 "Hazır ve paketli gıdalar sindirim sistemini nasıl etkiler?": ["Paketli gıdaların sindirime etkisini", "Dengeli beslenmenin sindirime etkisini"],
}

# Eklenen soruların "sorunun kalbi" bölgeleri (NE olduğu için dokunma adımı çalışmaz; çalışma kâğıdı ve yedek için)
BOLGE = {
 "Proteinlerin kimyasal sindirimi nerede başlar?": ["nerede başlar"],
 "Besinlerin sindirimi hangi organda başlar?": ["hangi organda başlar"],
 "Hangisi kimyasal sindirime örnektir?": "TUM",
 "Karaciğerin salgıladığı safra sıvısı nerede toplanır?": ["nerede toplanır"],
 "Düzenli egzersiz bağırsak hareketlerini nasıl etkiler?": ["bağırsak hareketlerini nasıl etkiler"],
 "Uzun süre hareketsiz kalmak bağırsak hareketlerini nasıl etkiler?": ["bağırsak hareketlerini nasıl etkiler"],
 "Hangisi sindirim sistemi sağlığı için yanlış bir davranıştır?": ["yanlış bir davranıştır"],
}
