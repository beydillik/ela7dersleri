# Türkçe (tr1) 3. Tema, Konu 7 — Kısa Çizgi ve Eğik Çizgi (s. 142, 163, 168). Dikkat paketi verisi.
TEKRAR = {"u3k7": [
 ("“Ankara-Bakü arasındaki iletişim” sözünde kısa çizgi {ile, arasında|-den -e kadar|adres} anlamı verir.", "s. 142"),
 ("“Saat 14.00-16.00 arasında” sözünde kısa çizgi {-den -e kadar|ve|adres} anlamı verir.", "s. 142"),
 ("Adreste bina numarası ile daire numarası arasına {eğik çizgi|kısa çizgi|virgül} konur: No.: 14/5.", "s. 163"),
 ("“Kızılay/Ankara” yazılışında eğik çizgi {semt ile şehri|iki ülkeyi|iki saati} ayırır.", "s. 163"),
 ("Tarih yazarken gün, ay ve yıl arasına {eğik çizgi|kısa çizgi|noktalı virgül} konabilir: 12/04/2025.", "s. 163"),
 ("Bir ekin farklı biçimleri arasına {eğik çizgi|kısa çizgi|üç nokta} konur: -lık/-lik.", "s. 163"),
 ("“Beşiktaş ( ) Fenerbahçe karşılaşması” sözündeki boşluğa {kısa çizgi|eğik çizgi} gelir.", "s. 168"),
]}
KISA = {"u3k7": [
 {"soru": "Kısa çizgi ile eğik çizginin kullanıldığı yerleri birer örnekle yazınız.",
  "tetik": ["kullanıldığı yerleri"],
  "parcalar": [
   {"bas": "Kısa çizgi:", "ornek": "“İle, arasında, -den -e” anlamında kullanılır: Ankara-Bakü, 14.00-16.00.", "havuz": ["Adreste kullanılır: Kızılay/Ankara.", "Tarihte kullanılır: 12/04/2025."], "k": ["ile", "arası", "-den -e", "kadar"]},
   {"bas": "Eğik çizgi:", "ornek": "Adreste, tarihte ve ekin biçimlerinde kullanılır: Kızılay/Ankara, 12/04/2025.", "havuz": ["“İle” anlamında kullanılır: Aydın-İzmir.", "Saat aralığında kullanılır: 14.00-16.00."], "k": ["adres", "tarih", "biçim"]}],
  "kisa": "Kısa çizgi: ile, arası, -den -e (Ankara-Bakü). Eğik çizgi: adres, tarih, ek biçimleri (12/04/2025).",
  "cevap": "Kısa çizgi “ile, arasında, -den -e kadar” anlamı verir: Ankara-Bakü arasındaki uçuşlar, saat 14.00-16.00. Eğik çizgi ise adreste, tarihte ve bir ekin farklı biçimleri arasında kullanılır: Kızılay/Ankara, 12/04/2025, -lık/-lik.",
  "anahtarlar": [{"ad": "kısa çizgi: ile / arası / -den -e", "k": ["ile", "arası", "-den -e", "kadar"]}, {"ad": "eğik çizgi: adres / tarih / ek biçimleri", "k": ["adres", "tarih", "biçim"]}],
  "sayfa": "s. 142, 163"},
 {"soru": "“Gül Sokak No.: 14/5 Kızılay/Ankara” (s. 163) adresindeki eğik çizgilerin ne gösterdiğini yazınız.",
  "tetik": ["ne gösterdiğini"],
  "parcalar": [
   {"bas": "14/5:", "ornek": "14 numaralı binanın 5 numaralı dairesi", "havuz": ["14 ile 5 arasındaki sayılar", "14 Mayıs tarihi"], "k": ["daire"]},
   {"bas": "Kızılay/Ankara:", "ornek": "Kızılay semti ile Ankara şehri", "havuz": ["Kızılay'dan Ankara'ya giden yol", "Kızılay ve Ankara takımlarının maçı"], "k": ["semt", "şehir", "şehr", "ilçe"]}],
  "kisa": "14/5: 14 numaralı binanın 5 numaralı dairesi; Kızılay/Ankara: semt ve şehir.",
  "cevap": "“14/5” yazılışında eğik çizgi bina numarası ile daire numarasını ayırır: 14 numaralı binanın 5 numaralı dairesi. “Kızılay/Ankara” yazılışında ise semt ile şehri ayırır: Kızılay semti, Ankara şehri.",
  "anahtarlar": [{"ad": "bina / daire numarası", "k": ["daire"]}, {"ad": "semt / şehir", "k": ["semt", "şehir", "şehr", "ilçe"]}],
  "sayfa": "s. 163"},
]}
OKUT = {"u3k7": [
 ["iki işaretin nerelerde kullanıldığını ayrı ayrı yazıp her birine örnek vermeni", "yalnız kısa çizginin örneğini yazmanı", "iki işaretin nasıl çizildiğini anlatmanı"],
 ["iki eğik çizginin adreste neyi neyden ayırdığını yazmanı", "adresi baştan sona okumanı", "eğik çizginin tarihteki görevini anlatmanı"]]}
SERIT = {
 "Tabloya göre kütüphane en uzun süre hangi gün açıktır?": "En uzun saat aralığının olduğu gün",
 "Metinde kısa çizgi hangi anlamda kullanılmıştır?": "Kısa çizginin geçtiği cümle",
 "Davetiyeye göre aşağıdakilerden hangisi söylenemez?": "Davetiyede yazanlarla çelişen yargı",
}
ELLE = {
 "“Aydın-İzmir güzergâhı” (s. 142) sözünde kısa çizgi ne anlama gelir?": "ne anlama gelir",
 "“-a/-e” yazılışında eğik çizgi ne gösterir?": "ne gösterir",
 "“Seminer saat 14.00-16.00 arasında yapılacak.” (s. 142) Seminer ne kadar sürer?": "ne kadar",
}
