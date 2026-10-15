import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from ortak import Havuz, ONC
H = Havuz("fen1", 3, "f3"); a = H.add
P1, P2, P3, P4, P5, P6, P7, P8, P9, P10 = "(s. 89–95)", "(s. 96–100)", "(s. 101–106)", "(s. 107)", "(s. 109–112)", "(s. 113–116)", "(s. 117–122)", "(s. 123–128)", "(s. 129–134)", "(s. 135–139)"

# --- Konu 1: Sindirim sistemi
a("u3k1", "Sindirim", "secim", soru="Besinlerin sindirim sisteminde izlediği yol hangisinde doğru verilmiştir?",
  secenekler=["Ağız → yemek borusu → yutak → mide → ince bağırsak", "Ağız → yutak → yemek borusu → mide → ince bağırsak → kalın bağırsak",
              "Ağız → mide → yutak → kalın bağırsak → ince bağırsak", "Ağız → yutak → mide → yemek borusu → kalın bağırsak"], dogru=1,
  aciklama=f"Sıra: ağız, yutak, yemek borusu, mide, ince bağırsak, kalın bağırsak {P1}.")
a("u3k1", "Yutak ve Yemek Borusu", "dy", ifade="Yemek borusunda besinlerin kimyasal sindirimi yapılır.", dogru=False,
  duzeltme="Yutak ve yemek borusu besini yalnızca taşır; burada sindirim olmaz.",
  aciklama=f"Yemek borusu besini mideye taşır ama sindirmez {P1}.")
a("u3k1", "İnce Bağırsak", "kisa", soru="Besinlerin sindirimi hangi organda tamamlanır?", yanit="ince bağırsak", kabul=["incebağırsak"],
  aciklama=f"Sindirim ince bağırsakta biter. Villuslar besini kana geçirir {P1}.")
a("u3k1", "Karaciğer ve Pankreas", "secim", soru="Sindirim sistemiyle ilgili aşağıdaki ifadeler verilmiştir.",
  onculler=["Karaciğer ve pankreas sindirime yardımcı organlardır.", "Safra sıvısı yağların fiziksel sindirimine yardım eder.", "Proteinlerin kimyasal sindirimi ağızda başlar."],
  kok="Bu ifadelerden hangileri doğrudur?", secenekler=ONC, dogru=1,
  aciklama=f"Protein sindirimi ağızda değil midede başlar {P1}.")
a("u3k1", "Sindirim", "eslestir", soru="Organları görevleriyle eşleştir.", ciftler=[
  {"sol": "Ağız", "sag": "Karbohidratların kimyasal sindirimi başlar."},
  {"sol": "Mide", "sag": "Proteinlerin kimyasal sindirimi başlar."},
  {"sol": "Kalın bağırsak", "sag": "Su, bazı mineral ve vitaminler emilir."},
  {"sol": "Anüs", "sag": "Sindirilmeyen besinler vücuttan atılır."}],
  aciklama=f"Her organın bir işi var. Sindirim ağızda başlar, atık anüsten çıkar {P1}.")

# --- Konu 2: Sindirim sisteminin sağlığı
a("u3k2", "Su ve Düzenli Öğünler", "secim", soru="Ruhi kahvaltı yapmıyor, öğle yemeğini cips ile geçiştiriyor. Ruhi'nin hangi alışkanlığı sindirim sistemi için hatalıdır?",
  secenekler=["Öğün atlaması", "Su içmesi", "Sebze yemesi", "Spor yapması"], dogru=0,
  aciklama=f"Öğün atlamak ve öğünü atıştırmalıkla geçiştirmek doğru değildir {P2}.")
a("u3k2", "Düzenli Egzersiz", "dy", ifade="Düzenli egzersiz bağırsakların hareketini artırır.", dogru=True,
  aciklama=f"Spor bağırsakları uyarır, besinler daha kolay sindirilir {P2}.")
a("u3k2", "Ekran Başında Hareketsizlik", "secim", soru="Uzun süre ekran başında oturmak sindirimi nasıl etkiler?",
  secenekler=["Bağırsak hareketlerini hızlandırır.", "Bağırsak hareketlerini yavaşlatır.", "Sindirimi hiç etkilemez.", "Mideyi güçlendirir."], dogru=1,
  aciklama=f"Hareketsizlik bağırsakları yavaşlatır. Ekran başında fazla da yenebilir {P2}.")
a("u3k2", "Hazır ve Paketli Gıdalar", "dytablo", soru="Sindirim sistemi sağlığı için doğru olanlara D, yanlış olanlara Y seç.", ifadeler=[
  {"s": "Paketli ve çok baharatlı yiyecekleri sık yemek", "d": False},
  {"s": "Gün içinde yeterli su içmek", "d": True},
  {"s": "Öğünleri düzenli ve dengeli yapmak", "d": True},
  {"s": "Stresle başa çıkmak için spor yapmak", "d": True}],
  aciklama=f"Paketli ve çok baharatlı gıdalar mideye zarar verebilir {P2}.")
a("u3k2", "Dengeli Beslenme", "secim", soru="Sindirim sistemi rahatsızlıkları genellikle neden kaynaklanır?",
  secenekler=["Uzun boylu olmaktan", "Yaşam tarzından", "Kitap okumaktan", "Mevsimden"], dogru=1,
  aciklama=f"Beslenme, hareket ve stres gibi yaşam tarzı sindirimi etkiler {P2}.")

# --- Konu 3: Kalp, damarlar ve kan dolaşımı
a("u3k3", "Dolaşım Sistemi", "kisa", soru="Dolaşım sistemi kan, kalp ve hangi yapılardan oluşur?", yanit="damarlar", kabul=["damar"],
  aciklama=f"Dolaşım sistemi: kan, kalp ve damarlar {P3}.")
a("u3k3", "Atardamar", "eslestir", soru="Damarları görevleriyle eşleştir.", ciftler=[
  {"sol": "Atardamar", "sag": "Kanı kalpten vücuda taşır."},
  {"sol": "Toplardamar", "sag": "Kanı vücuttan kalbe getirir."},
  {"sol": "Kılcal damar", "sag": "Kan ile hücreler arasında madde alışverişi sağlar."}],
  aciklama=f"Atardamar götürür, toplardamar getirir, kılcal damar alışveriş yapar {P3}.")
a("u3k3", "Küçük Kan Dolaşımı", "secim", soru="“Kalp → akciğer → kalp” yolu hangi dolaşımdır?",
  secenekler=["Büyük kan dolaşımı", "Sindirim", "Küçük kan dolaşımı", "Boşaltım"], dogru=2,
  aciklama=f"Küçük dolaşımda kan akciğere gider, oksijen alıp kalbe döner {P3}.")
a("u3k3", "Büyük Kan Dolaşımı", "bosluk", havuz=["akciğer", "mide"], cumleler=[
  {"c": "Büyük dolaşımda oksijence zengin kan kalbin ___ tarafından çıkar.", "cevap": "sol"},
  {"c": "Vücuttan dönen kan kalbin ___ tarafına gelir.", "cevap": "sağ"},
  {"c": "Kanın atardamar duvarına yaptığı basınca ___ denir.", "cevap": "nabız"}],
  aciklama=f"Temiz kan soldan çıkar, kirli kan sağa döner. Nabzı bilekte hissederiz {P3}.")
a("u3k3", "Kalp", "dy", ifade="Kalp, özel kas dokusundan oluşan bir organdır.", dogru=True,
  aciklama=f"Kalp kasılıp gevşeyerek kanı pompalar {P3}.")

# --- Konu 4: Kanın yapısı
a("u3k4", "Alyuvar", "secim", soru="Oksijen ve karbon dioksidi taşıyan kan hücresi hangisidir?",
  secenekler=["Akyuvar", "Kan pulcuğu", "Plazma", "Alyuvar"], dogru=3,
  aciklama=f"Alyuvar kana kırmızı rengi verir ve gazları taşır {P4}.")
a("u3k4", "Akyuvar", "dy", ifade="Kanda en çok sayıda bulunan hücreler akyuvarlardır.", dogru=False,
  duzeltme="En çok alyuvar, en az akyuvar bulunur.",
  aciklama=f"Alyuvar en çok, akyuvar en az bulunan kan hücresidir {P4}.")
a("u3k4", "Kan Pulcukları", "eslestir", soru="Kanın bölümlerini görevleriyle eşleştir.", ciftler=[
  {"sol": "Plazma", "sag": "Kanın sıvı kısmıdır, çoğu sudur."},
  {"sol": "Alyuvar", "sag": "Oksijen ve karbon dioksit taşır."},
  {"sol": "Akyuvar", "sag": "Vücudu mikroplara karşı savunur."},
  {"sol": "Kan pulcuğu", "sag": "Pıhtılaşarak kanamayı durdurur."}],
  aciklama=f"Plazma sıvı kısım; alyuvar taşır, akyuvar korur, pulcuk pıhtı yapar {P4}.")
a("u3k4", "Kanın Görevleri", "secim", soru="Aşağıdakilerden hangisi kanın görevlerinden biri değildir?",
  secenekler=["Hücrelere oksijen taşımak", "Besinleri sindirmek", "Vücut sıcaklığını düzenlemek", "Mikroplara karşı korumak"], dogru=1,
  aciklama=f"Kan taşır, korur ve ısıtır. Sindirim, sindirim sisteminin işidir {P4}.")
a("u3k4", "Plazma", "kisa", soru="Kanın sıvı kısmına ne ad verilir?", yanit="plazma",
  aciklama=f"Plazma kanın sıvı kısmıdır; büyük kısmı sudur {P4}.")

# --- Konu 5: Kan ve organ bağışı
a("u3k5", "Kimler Kan Verebilir?", "secim", soru="Aşağıdakilerden hangisi kan bağışçısı olabilir?",
  secenekler=["15 yaşında, 55 kg, sağlıklı bir öğrenci", "30 yaşında, 70 kg, sağlıklı bir yetişkin", "40 yaşında, 45 kg bir yetişkin", "70 yaşında, 80 kg bir yetişkin"], dogru=1,
  aciklama=f"Kan vermek için 18–65 yaş, 50 kg üstü ve sağlıklı olmak gerekir {P5}.")
a("u3k5", "Kan Bağışında 4 Adım", "bosluk", havuz=["ameliyat", "nakil"], cumleler=[
  {"c": "Kan bağışında ilk adım ___ işlemidir.", "cevap": "kayıt"},
  {"c": "Kayıttan sonra doktor ___ yapılır.", "cevap": "muayenesi"},
  {"c": "Kan verdikten sonra ikram ve ___ adımı gelir.", "cevap": "dinlenme"}],
  aciklama=f"Sıra: kayıt, muayene, kan alma, ikram ve dinlenme {P5}.")
a("u3k5", "Organ Nakli", "dy", ifade="Organ nakli için organ yalnızca yaşayan bir kişiden alınabilir.", dogru=False,
  duzeltme="Organ canlı bir kişiden ya da yaşamını yitirmiş birinden alınabilir.",
  aciklama=f"Organ, canlı kişiden ya da yaşamını yitirmiş birinden alınabilir {P5}.")
a("u3k5", "Organ Bağışının Kuralları", "secim", soru="Bağışlanan organlar ihtiyaç sahiplerine verilirken önce neye bakılır?",
  secenekler=["Hastanın maddi durumuna", "Kan ve doku uyumuna", "Hastanın cinsiyetine", "Hastanın yaşadığı şehre"], dogru=1,
  aciklama=f"Önce kan ve doku uyumuna, sonra aciliyete bakılır {P5}.")
a("u3k5", "Toplumsal Dayanışma", "secim", soru="Kan ve organ bağışıyla ilgili aşağıdaki ifadeler verilmiştir.",
  onculler=["18 yaşından küçükler kan bağışı yapabilir.", "Organ bağışı gönüllülük esasına dayanır.", "Bağış, toplumsal dayanışmanın güzel bir örneğidir."],
  kok="Bu ifadelerden hangileri doğrudur?", secenekler=ONC, dogru=2,
  aciklama=f"18 yaşından küçükler kan veremez. Bağış gönüllüdür ve yardımlaşmadır {P5}.")

# --- Konu 6: Dolaşım sisteminin sağlığı
a("u3k6", "Düzenli Uyku", "secim", soru="Çocukların dolaşım sistemi sağlığı için günde kaç saat uyuması gerekir?",
  secenekler=["4–5 saat", "5–6 saat", "8–10 saat", "12–14 saat"], dogru=2,
  aciklama=f"Çocuklar 8–10, yetişkinler 7–9 saat uyumalıdır {P6}.")
a("u3k6", "Dengeli Beslenme", "secim", soru="Aşağıdakilerden hangisi sağlıklı bir yağdır?",
  secenekler=["Zeytinyağı", "Kızartma yağı", "Margarin", "Hazır gıda yağı"], dogru=0,
  aciklama=f"Zeytinyağı, ceviz yağı ve fındık yağı sağlıklı yağlardır {P6}.")
a("u3k6", "Spor ve Sosyal Faaliyetler", "dy", ifade="Düzenli egzersiz kan dolaşımını yavaşlatır.", dogru=False,
  duzeltme="Spor kanın vücutta hızlı dolaşmasını sağlar.",
  aciklama=f"Spor yapınca kan hızlı dolaşır, organlara daha çok oksijen gider {P6}.")
a("u3k6", "Yağlı, Tuzlu ve Hazır Gıdalar", "secim", soru="Mehmet çok yağlı, tuzlu yiyor ve az hareket ediyor. Doktor ona hangisini önermez?",
  secenekler=["Bol su içmesini", "Az tuzlu yemesini", "Spor yapmasını", "Hazır gıdaları artırmasını"], dogru=3,
  aciklama=f"Doktor su, az yağ, az tuz ve spor önerdi. Hazır gıda zararlıdır {P6}.")
a("u3k6", "Uzun Ekran Süresi", "kisa", soru="Uzun süre ekran başında kalmak hangi durumu doğurarak kalbe zarar verir?", yanit="hareketsizlik", kabul=["hareketsiz kalmak", "hareketsiz"],
  aciklama=f"Ekran hareketsizliğe yol açar. Ara ara kısa yürüyüşler yapmalıyız {P6}.")

# --- Konu 7: Solunum sistemi
a("u3k7", "Solunum Sistemi", "secim", soru="Havanın solunum sisteminde izlediği yol hangisinde doğru verilmiştir?",
  secenekler=["Burun → gırtlak → yutak → bronş → soluk borusu", "Burun → yutak → gırtlak → soluk borusu → bronş → alveol",
              "Ağız → yemek borusu → bronş → alveol", "Burun → soluk borusu → yutak → alveol → bronş"], dogru=1,
  aciklama=f"Hava burun, yutak, gırtlak, soluk borusu, bronş ve alveol yolunu izler {P7}.")
a("u3k7", "Burun", "dytablo", soru="Burunla ilgili ifadeler için D ya da Y seç.", ifadeler=[
  {"s": "Mukus sıvısı kuru havayı nemlendirir.", "d": True},
  {"s": "Burundaki kıllar toz ve mikropları tutar.", "d": True},
  {"s": "Ses telleri burnun içindedir.", "d": False}],
  aciklama=f"Burun havayı nemlendirir, ısıtır, temizler. Ses telleri gırtlaktadır {P7}.")
a("u3k7", "Akciğerler ve Alveoller", "kisa", soru="Akciğerde oksijenin kana geçtiği hava keselerine ne ad verilir?", yanit="alveol", kabul=["alveoller"],
  aciklama=f"Gaz değişimi alveollerde olur {P7}.")
a("u3k7", "Soluk Alma ve Verme", "secim", soru="Soluk alırken aşağıdakilerden hangisi olur?",
  secenekler=["Diyafram kasılıp düzleşir.", "Göğüs boşluğu daralır.", "Diyafram gevşeyip kubbeleşir.", "Akciğerlerdeki hava dışarı atılır."], dogru=0,
  aciklama=f"Diyafram kasılınca soluk alırız, gevşeyince veririz {P7}.")
a("u3k7", "Soluk Borusu ve Bronşlar", "bosluk", havuz=["kalp", "mide"], cumleler=[
  {"c": "Ağaç benzetmesinde ağacın gövdesi ___ borusuna benzer.", "cevap": "soluk"},
  {"c": "Dallar ___ benzer.", "cevap": "bronşlara"},
  {"c": "Yapraklar ___ benzer.", "cevap": "alveollere"}],
  aciklama=f"Gövde soluk borusu, dallar bronşlar, yapraklar alveollerdir {P7}.")

# --- Konu 8: Solunum sağlığı ve bağımlılık
a("u3k8", "Yeşilay", "secim", soru="Yeşilay ile ilgili aşağıdaki ifadeler verilmiştir.",
  onculler=["İlk adı Hilâl-i Ahdar'dır.", "Her yıl 1–7 Mart Yeşilay Haftası'dır.", "Teknoloji bağımlılığı alanında da çalışır."],
  kok="Bu ifadelerden hangileri doğrudur?", secenekler=ONC, dogru=3,
  aciklama=f"Üçü de doğru. Yeşilay tütün, teknoloji ve kumar bağımlılığıyla çalışır {P8}.")
a("u3k8", "Destek Hatları", "kisa", soru="Sigarayı bırakmak isteyenlerin arayabileceği danışma hattının numarası kaçtır?", yanit="171", sayi=True,
  aciklama=f"ALO 171 Sigara Bırakma Danışma Hattı'dır {P8}.")
a("u3k8", "Havalandırma ve Maske", "secim", soru="Hangisi solunum sistemi sağlığı için doğru bir davranış değildir?",
  secenekler=["Kapalı odayı havalandırmak", "Tozlu ortamda maske takmak", "Temiz havada yürümek", "Kapalı ve dumanlı ortamda uzun süre kalmak"], dogru=3,
  aciklama=f"Kirli ve dumanlı ortamlardan uzak durmalıyız {P8}.")
a("u3k8", "Bağımlılık", "dy", ifade="Tütün ürünleri yalnızca solunum sistemine zarar verir.", dogru=False,
  duzeltme="Bağımlılık yapıcı maddeler solunum ve dolaşım sistemine, ilişkilere de zarar verir.",
  aciklama=f"Bağımlılık hem solunuma hem dolaşıma hem de ilişkilere zarar verir {P8}.")
a("u3k8", "Spor ve Temiz Hava", "secim", soru="Spor yapmak solunum sistemi için neden faydalıdır?",
  secenekler=["Akciğerleri ve solunum kaslarını güçlendirir.", "Nefes almayı durdurur.", "Akciğerleri küçültür.", "Diyaframı ortadan kaldırır."], dogru=0,
  aciklama=f"Spor nefes ihtiyacını artırır, bu da akciğerleri güçlendirir {P8}.")

# --- Konu 9: Boşaltım sistemi
a("u3k9", "Boşaltım Sistemi", "secim", soru="İdrarın vücuttaki yolu hangisinde doğru verilmiştir?",
  secenekler=["Böbrek → mesane → üreter → üretra", "Mesane → böbrek → üretra → üreter", "Böbrek → üreter → mesane → üretra", "Üreter → böbrek → mesane → üretra"], dogru=2,
  aciklama=f"Böbrek idrarı yapar, üreter taşır, mesane biriktirir, üretra dışarı atar {P9}.")
a("u3k9", "Böbrekler", "kisa", soru="Kanı süzen (filtreleyen) organ hangisidir?", yanit="böbrek", kabul=["böbrekler"],
  aciklama=f"Böbrekler kanı süzer, atıklardan idrar oluşur {P9}.")
a("u3k9", "Mesane (İdrar Kesesi)", "eslestir", soru="Boşaltım organlarını görevleriyle eşleştir.", ciftler=[
  {"sol": "Böbrek", "sag": "Kanı süzer, idrarı oluşturur."},
  {"sol": "Üreter", "sag": "İdrarı böbrekten mesaneye taşır."},
  {"sol": "Mesane", "sag": "İdrarı biriktirir."},
  {"sol": "Üretra", "sag": "İdrarı vücut dışına atar."}],
  aciklama=f"Süz, taşı, biriktir, at: böbrek, üreter, mesane, üretra {P9}.")
a("u3k9", "Deri", "dy", ifade="Terleme, vücut sıcaklığını dengelemeye de yardım eder.", dogru=True,
  aciklama=f"Ter su ve tuzu atar, vücut sıcaklığını dengeler {P9}.")
a("u3k9", "Diğer Yardımcı Organlar", "secim", soru="Sindirim sonucu oluşan zararlı maddeleri daha az zararlı hâle getiren organ hangisidir?",
  secenekler=["Deri", "Karaciğer", "Akciğer", "Mesane"], dogru=1,
  aciklama=f"Karaciğer zararlı maddeleri daha az zararlı hâle getirir {P9}.")

# --- Konu 10: Boşaltım sisteminin sağlığı
a("u3k10", "Yeterli Su İçmek", "secim", soru="Hangisi yeterli su içmenin faydalarından biridir?",
  secenekler=["Böbrek taşı oluşumunu azaltır.", "Böbrekleri tembelleştirir.", "Vücut sıcaklığını bozar.", "Ödem oluşturur."], dogru=0,
  aciklama=f"Yeterli su böbrek taşı ve idrar yolu enfeksiyonu riskini azaltır {P10}.")
a("u3k10", "Dengeli Beslenme", "dy", ifade="Tuz ve protein ağırlıklı beslenmek böbreklerin daha çok çalışmasına neden olur.", dogru=True,
  aciklama=f"Çok tuz ve protein böbrekleri yorar. Ölçülü beslenmeliyiz {P10}.")
a("u3k10", "Teknoloji Bağımlılığı", "secim", soru="Ekran başında uzun süre hareketsiz kalmak böbrekleri nasıl etkiler?",
  secenekler=["Kan akış hızını yavaşlatarak", "Böbrekleri büyüterek", "Su ihtiyacını sıfırlayarak", "Hiç etkilemez"], dogru=0,
  aciklama=f"Hareketsizlik kan akışını yavaşlatır, bu da boşaltımı olumsuz etkiler {P10}.")
a("u3k10", "Yeterli Su İçmek", "dytablo", soru="Boşaltım sistemi sağlığı için doğru olanlara D, yanlış olanlara Y seç.", ifadeler=[
  {"s": "Susamadıkça su içmemek", "d": False},
  {"s": "Kişisel hijyene özen göstermek", "d": True},
  {"s": "Gereğinden çok fazla su içmek", "d": False},
  {"s": "Düzenli spor yapmak", "d": True}],
  aciklama=f"Su ne az ne çok olmalı. Hijyen ve spor böbreği korur {P10}.")
a("u3k10", "Sosyal Faaliyetler", "secim", soru="Sosyal faaliyetler boşaltım sisteminin sağlığına nasıl katkı sağlar?",
  secenekler=["Stresten uzak tutar.", "Su ihtiyacını azaltır.", "Tuz ihtiyacını artırır.", "Uyku süresini kısaltır."], dogru=0,
  aciklama=f"Sosyal faaliyetler stresi azaltır; stres vücuda zarar verir {P10}.")
H.yaz()
