TEKRAR = {"u3k10": [
 ("Yeterli ve dengeli beslenme böbreklerin sağlığı için önemlidir; gereğinden fazla su içmek, tuz ve protein ağırlıklı beslenmek böbreklerin {daha çok|daha az} çalışmasına neden olur.", "s. 137"),
 ("Düzenli yapılan egzersiz kan dolaşımını ve kalp atışını hızlandırır; böylece böbrekler daha {sağlıklı|yavaş|bozuk} çalışır.", "s. 137"),
 ("Sosyal faaliyetler insanı {stresten|uykudan|sudan} uzak tutar; stres vücutta birçok olumsuz etkiye yol açabilir.", "s. 137"),
 ("Gün içinde yeterli su içmek böbrek taşı oluşumu ve {idrar yolu enfeksiyonları|diş çürükleri|saç dökülmesi} gibi rahatsızlıkları azaltır.", "s. 137"),
 ("Yeterli su içmek vücudun sıvı dengesini korur ve {ödem|kemik} oluşumunu engeller; ayrıca vücut sıcaklığını düzenler.", "s. 137"),
 ("Teknoloji bağımlısı bireyler ekran başında uzun süre hareketsiz kalabilir; hareketsizlik kan akış hızını {yavaşlatabilir|hızlandırabilir} ve böbreklerin verimli çalışmasını engelleyebilir.", "s. 137"),
 ("Yeterli ve dengeli beslenme, spor ve su içmenin yanında {kişisel hijyene|ekran süresine} özen göstermek de sağlıklı yaşam için önemlidir.", "s. 137"),
]}
KISA = {"u3k10": [
 {"soru": "Yeterli su içmenin boşaltım sistemi sağlığına iki faydasını yazınız.",
  "tetik": ["iki faydasını"],
  "okut": ["İki ayrı fayda yaz (iki parça).", "Neden ve sonuç yaz.", "Tanım yaz: “X, … denir.”"],
  "parcalar": [
   {"bas": "Birinci fayda:", "ornek": "Böbrek taşı ve idrar yolu enfeksiyonları gibi rahatsızlıkları azaltır.", "havuz": ["Kemik gelişimini hızlandırır.", "Kalbin atış hızını yavaşlatır."], "k": ["taşı", "enfeksiyon"]},
   {"bas": "İkinci fayda:", "ornek": "Sıvı dengesini korur, ödem oluşumunu engeller.", "havuz": ["Alyuvar sayısını artırır.", "Kasları büyütür."], "k": ["ödem", "sıvı"]}],
  "kisa": "Böbrek taşı ve idrar yolu enfeksiyonlarını azaltır; sıvı dengesini korur, ödemi engeller.",
  "cevap": "Yeterli su içmek böbrek taşı oluşumu ve idrar yolu enfeksiyonları gibi rahatsızlıkları azaltır. Ayrıca vücudun sıvı dengesini koruyarak ödem oluşumunu engeller.",
  "anahtarlar": [{"ad": "böbrek taşı / idrar yolu enfeksiyonu azalır", "k": ["taşı", "enfeksiyon"]}, {"ad": "sıvı dengesi / ödem", "k": ["ödem", "sıvı"]}],
  "sayfa": "s. 137"},
 {"soru": "Düzenli egzersiz böbrek sağlığını nasıl etkiler? Yazınız.",
  "tetik": ["nasıl"],
  "okut": ["Etkiyi ve sonucunu yaz (iki parça).", "Tanım yaz: “X, … denir.”", "İki ayrı örnek yaz."],
  "parcalar": [
   {"bas": "Dolaşıma etkisi:", "ornek": "Kan dolaşımını ve kalp atışını hızlandırır.", "havuz": ["Kan dolaşımını yavaşlatır.", "Kalp atışını durdurur."], "k": ["hızlandır"]},
   {"bas": "Sonucu:", "ornek": "Böbrekler daha sağlıklı çalışır.", "havuz": ["Böbrekler daha yavaş çalışır.", "Böbrekler hiç çalışmaz."], "k": ["sağlıklı"]}],
  "kisa": "Kan dolaşımını ve kalp atışını hızlandırır; böbrekler daha sağlıklı çalışır.",
  "cevap": "Düzenli egzersiz kan dolaşımını ve kalp atışını hızlandırır. Böylece böbrekler daha sağlıklı çalışır.",
  "anahtarlar": [{"ad": "kan dolaşımı / kalp atışı hızlanır", "k": ["hızlandır"]}, {"ad": "böbrekler daha sağlıklı çalışır", "k": ["sağlıklı"]}],
  "sayfa": "s. 137"},
]}
ELLE = {"'Büyüme ve gelişimimiz için bol bol tuzlu gıdalar yemeliyiz.' ifadesi için ne söylenebilir?": "ne söylenebilir", "'Susamadığımız sürece su içmemeliyiz.' ifadesi için ne söylenebilir?": "ne söylenebilir", "'Aşırı protein alımından uzak durmalıyız.' ifadesi için ne söylenebilir?": "ne söylenebilir", "Düzenli egzersiz yapan birinde böbrekler için ne söylenebilir?": "ne söylenebilir", "Uygar Bey'in doktoru boşaltım sistemi rahatsızlığı için ona ne önerdi?": "ne önerdi"}
OKUT = {"u3k10": [
 ["yeterli su içmenin boşaltım sistemine iki faydasını yazmanı", "günde kaç bardak su içmen gerektiğini söylemeni", "suyun hangi kaynaklardan geldiğini anlatmanı"],
 ["egzersizin kan dolaşımına ne yaptığını ve bunun böbreklere etkisini anlatmanı", "hangi sporların böbreğe iyi geldiğini sıralamanı", "egzersizin kaslara faydasını anlatmanı"]]}
METINLI = {"u3k10": [
 {"metin": ["Teknoloji bağımlısı kişiler ekran başında uzun süre hareketsiz kalabilir.", "Hareketsizlik kan akış hızını yavaşlatabilir.", "Bu durum böbreklerin verimli çalışmasını engelleyebilir."],
  "soru": "Uzun süre ekran başında kalmanın böbreklere etkisi nedir?", "bolge": ["böbreklere etkisi nedir"],
  "serit": "Ekran başında kalmanın böbreklere etkisi", "kanit": [2],
  "secenekler": ["Böbreklerin verimli çalışmasını engelleyebilir", "Kan akış hızını artırır", "Böbrekleri daha sağlıklı çalıştırır"], "dogru": 0, "tuzak": [1],
  "ipucu": "“Böbreklerin” kelimesinin geçtiği cümleyi oku.", "kanitIpucu": "Böbreklere ne olduğunu söyleyen cümleyi bul.",
  "aciklama": "Ekran başında hareketsiz kalmak kan akış hızını yavaşlatabilir ve böbreklerin verimli çalışmasını engelleyebilir (s. 137).", "kavram": "Teknoloji Bağımlılığı"},
 {"metin": ["Uygar Bey bir süredir belinden sırtına doğru yayılan şiddetli bir ağrı hissediyordu.", "Doktora gitti ve yapılan testlerde boşaltım sistemi rahatsızlığı tespit edildi.", "Doktor ona yeterince su içmesini önerdi.", "Tedavi sürecinin sonunda Uygar Bey sağlığına kavuştu."],
  "soru": "Doktorun Uygar Bey'e önerisi nedir?", "bolge": ["önerisi nedir"],
  "serit": "Doktorun önerisi", "kanit": [2],
  "secenekler": ["Yeterince su içmek", "Belindeki ağrıya alışmak", "Tedaviyi bırakmak"], "dogru": 0, "tuzak": [1, 2],
  "ipucu": "Soru ağrıyı değil, doktorun ne önerdiğini soruyor.", "kanitIpucu": "Doktorun önerisini anlatan cümleyi bul.",
  "aciklama": "Doktor yeterince su içmesini önerdi. Yeterli su içmek böbrek taşı ve idrar yolu enfeksiyonu gibi rahatsızlıkları azaltır (s. 135, 137).", "kavram": "Yeterli Su İçmek"}]}
