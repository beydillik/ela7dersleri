import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from ortak import Havuz, ONC
H = Havuz("tr1", 1, "t1"); a = H.add
K1, K2, K3, K4, K5, K6, K7, K8, K9 = "(s. 12–17)", "(s. 12–14, 51–57)", "(s. 22–23, 44–46)", "(s. 49)", "(s. 34–35)", "(s. 30–32)", "(s. 38–41)", "(s. 47)", "(s. 59–64)"

# --- Konu 1: Kelimenin anlamını bulma
a("u1k1", "Bağlam", "secim", metin=["Deniz'in sınavdan önce eli ayağı titriyordu.", "Öğretmeni gülümseyerek omzuna dokundu.", "Deniz derin bir nefes aldı ve yüreği ferahladı."],
  soru="Metindeki “yüreği ferahladı” sözü hangi anlamda kullanılmıştır?",
  secenekler=["Korkusu arttı.", "İçi rahatladı.", "Hastalandı.", "Uykusu geldi."], dogru=1,
  aciklama=f"Öğretmenin dokunuşundan sonra derin nefes aldı. Bağlam, içinin rahatladığını söyler {K1}.")
a("u1k1", "Metindeki Anlam ve Sözlük Anlamı", "secim", soru="“Yüz” kelimesi hangi cümlede sayı anlamında kullanılmıştır?",
  secenekler=["Yüzünü soğuk suyla yıkadı.", "Denizde yüz metre yüzdü.", "Yüzü güneşten kızarmıştı.", "Bize güler yüzle baktı."], dogru=1,
  aciklama=f"“Yüz metre” bir sayıdır. Kelimenin anlamını cümle seçer {K1}.")
a("u1k1", "Tahmin Et, Sözlükle Kontrol Et", "dy", ifade="Bilmediğimiz bir kelimenin anlamını önce bağlamdan tahmin edip sonra sözlükten kontrol etmeliyiz.", dogru=True,
  aciklama=f"Önce tahmin, sonra sözlük {K1}.")
a("u1k1", "Kelime Grubu", "secim", soru="“Sınavı kazanmak için ter döktü.” cümlesinde “ter dökmek” ne anlama gelir?",
  secenekler=["Çok sıcaklamak", "Çok emek vermek", "Koşmak", "Hastalanmak"], dogru=1,
  aciklama=f"Kelime grubu birlikte anlam verir: ter dökmek, çok çalışmaktır {K1}.")
a("u1k1", "Anahtar Kelime", "secim", metin=["Arılar çiçekten çiçeğe konarak polen taşır.", "Bu sayede bitkiler tohum ve meyve verir.", "Arılar azalırsa sofralarımızdaki meyve de azalır."],
  soru="Bu metnin anahtar kelimeleri hangileridir?",
  secenekler=["sofra, tohum", "arı, polen, meyve", "çiçek, renk", "bitki, su"], dogru=1,
  aciklama=f"Metin arıların polen taşımasını ve meyveyi anlatıyor. Anahtar kelimeler bunlar {K1}.")

# --- Konu 2: Hikâyenin bölümleri ve unsurları
a("u1k2", "Serim", "secim", soru="Hikâyede kişilerin, yerin ve zamanın tanıtıldığı bölüm hangisidir?",
  secenekler=["Düğüm", "Çözüm", "Serim", "Ana fikir"], dogru=2,
  aciklama=f"Serim giriştir: kim, nerede, ne zaman {K2}.")
a("u1k2", "Düğüm", "eslestir", soru="Hikâyenin bölümlerini açıklamalarıyla eşleştir.", ciftler=[
  {"sol": "Serim", "sag": "Kişiler, yer ve zaman tanıtılır."},
  {"sol": "Düğüm", "sag": "Bir sorun çıkar, merak artar."},
  {"sol": "Çözüm", "sag": "Sorun bir sonuca bağlanır."}],
  aciklama=f"Giriş serim, gelişme düğüm, sonuç çözümdür {K2}.")
a("u1k2", "Karakterin Özellikleri", "secim", metin=["Efe takımdaki herkesin topa dokunmasını istiyordu.", "Gol atabilecekken topu arkadaşına pas verdi.", "Maçtan sonra da malzemeleri toplamaya ilk o koştu."],
  soru="Metne göre Efe'nin hangi özelliği vardır?",
  secenekler=["Bencil", "Paylaşımcı ve yardımsever", "Tembel", "Korkak"], dogru=1,
  aciklama=f"Pas vermesi ve malzeme toplaması onun paylaşımcı olduğunu gösterir {K2}.")
a("u1k2", "Bakış Açısı", "dy", ifade="Jonathan'ın anne ve babası için önemli olan uçmayı öğrenmekti.", dogru=False,
  duzeltme="Anne ve babası için önemli olan yiyecek bulmak ve sağlıklı kalmaktı.",
  aciklama=f"Aynı olaya herkes farklı bakar. Uçmak Jonathan için önemliydi {K2}.")
a("u1k2", "Bölümler Arası Bağlantı", "secim", soru="İyi bir hikâyede bölümler arasındaki bağ için hangisi doğrudur?",
  secenekler=["Olaylar arasında kopukluk olmalıdır.", "Kişiler bölümden bölüme değişmelidir.", "Olaylar sebep-sonuçla birbirine bağlanmalıdır.", "Her bölüm farklı bir dille yazılmalıdır."], dogru=2,
  aciklama=f"Her olay bir öncekinin sonucu gibi akmalı. Okur “Bu nereden çıktı?” dememeli {K2}.")

# --- Konu 3: Konu, ana fikir ve özetleme
a("u1k3", "Konu", "secim", metin=["Deprem anında masanın altına girmeliyiz.", "Evde bir deprem çantası hazır bulunmalıdır.", "Ailece toplanma alanını önceden öğrenmeliyiz."],
  soru="Bu metnin konusu hangisidir?",
  secenekler=["Depreme hazırlık", "Okul gezisi", "Spor yapmak", "Kitap okumak"], dogru=0,
  aciklama=f"Konu “Ne anlatılıyor?” sorusunun cevabıdır ve kısadır {K3}.")
a("u1k3", "Ana Fikir", "secim", metin=["Deniz bisiklet sürmeyi öğrenmek istiyordu.", "İlk günlerde sık sık düştü, dizleri yaralandı.", "Vazgeçmedi, her gün biraz daha denedi.", "Bir ay sonra parkta rahatça bisiklet sürüyordu."],
  soru="Bu metnin ana fikri hangisidir?",
  secenekler=["Bisiklet pahalı bir taşıttır.", "Vazgeçmeden çalışan, sonunda başarır.", "Parklar oyun alanıdır.", "Düşmek tehlikelidir."], dogru=1,
  aciklama=f"Ana fikir yazarın vermek istediği mesajdır: vazgeçme {K3}.")
a("u1k3", "Yardımcı Fikir", "secim", soru="Ana fikri “Spor yapmak sağlığımızı korur.” olan bir metinde hangisi yardımcı fikir olabilir?",
  secenekler=["Düzenli spor kalbi güçlendirir.", "Bilgisayar oyunları eğlencelidir.", "Kışın kar yağar.", "Kitaplar bilgi verir."], dogru=0,
  aciklama=f"Yardımcı fikir ana fikri destekler. Kalbi güçlendirmek sağlığı korumaktır {K3}.")
a("u1k3", "Önemli ve Önemsiz Bilgi", "dy", ifade="Özet yazarken metindeki küçük ayrıntıları ve kendi yorumumuzu da eklemeliyiz.", dogru=False,
  duzeltme="Özet; önemli bilgilerle, olay sırasını bozmadan ve kendi cümlelerimizle yazılır. Yorum katılmaz.",
  aciklama=f"Özet kısa, sıralı ve yorumsuz olmalıdır {K3}.")
a("u1k3", "Başlık", "secim", metin=["Ormanda kaybolan köpek Pamuk'u bütün mahalle aradı.", "Çocuklar afiş astı, büyükler sokakları dolaştı.", "Akşam Pamuk bulununca herkes sevindi."],
  soru="Bu metne en uygun başlık hangisidir?",
  secenekler=["Ormandaki Ağaçlar", "Mahallece Pamuk'u Aradık", "Kış Geldi", "Afiş Nasıl Yapılır?"], dogru=1,
  aciklama=f"Başlık metnin konusunu haber vermeli. Metin Pamuk'u aramayı anlatıyor {K3}.")

# --- Konu 4: Noktalı virgül
a("u1k4", "Tür ve Takımları Ayırma", "secim", soru="Hangi cümlede noktalı virgül tür ve takımları ayırmak için kullanılmıştır?",
  secenekler=["Annem; Ali, Can ve Ece'yi çağırdı.", "Manavdan elma, armut; kasaptan kıyma, tavuk aldık.", "Çok yorulmuştu; erkenden uyudu.", "Sabah oldu; güneş doğdu."], dogru=1,
  aciklama=f"Virgülle sıralanmış iki grup var. Grupların arasına noktalı virgül gelir {K4}.")
a("u1k4", "Özneden Sonra", "secim", soru="“Öğretmenimiz ___ Ece, Can ve Mert'i tebrik etti.” Boşluğa hangi işaret gelmelidir?",
  secenekler=["Nokta (.)", "Soru işareti (?)", "Noktalı virgül (;)", "Üç nokta (…)"], dogru=2,
  aciklama=f"Sıralanan kelimeler özneyle karışmasın diye özneden sonra noktalı virgül konabilir {K4}.")
a("u1k4", "Noktalı Virgül Nedir?", "dy", ifade="Noktalı virgülden sonra gelen kelime (özel isim değilse) büyük harfle başlar.", dogru=False,
  duzeltme="Noktalı virgül cümleyi bitirmez; ondan sonra küçük harfle devam edilir.",
  aciklama=f"Noktalı virgül noktadan zayıftır, cümle bitmez. Küçük harfle devam edilir {K4}.")
a("u1k4", "Virgül mü, Noktalı Virgül mü?", "dytablo", soru="Noktalama doğruysa D, yanlışsa Y seç.", ifadeler=[
  {"s": "Elma, armut, ayva aldım.", "d": True},
  {"s": "Elma; armut; ayva aldım.", "d": False},
  {"s": "Seçil doğa, tarih; Berke su altı, uzay belgeseli izledi.", "d": True}],
  aciklama=f"Tek grup varsa virgül yeter. İki grup varsa aralarına noktalı virgül gelir {K4}.")
a("u1k4", "Sıralı Cümleleri Ayırma", "secim", soru="Hangi cümlede noktalı virgül, ögeleri arasında virgül olan sıralı cümleleri ayırmıştır?",
  secenekler=["Annem pazardan domates, biber aldı; babam salata yaptı.", "Sınıf başkanı; Ayşe, Zeynep ve Mert'i seçti.", "Kitap, defter; kalem, silgi.", "Bugün hava güzel."], dogru=0,
  aciklama=f"İki yüklem var: aldı, yaptı. İlk cümlede virgül olduğu için arada noktalı virgül var {K4}.")

# --- Konu 5: İkilemeler ve üç nokta
a("u1k5", "İkilemeler Ayrı Yazılır", "secim", soru="Hangi cümlede ikilemenin yazımı doğrudur?",
  secenekler=["Çolukçocuk parka gittik.", "Kar gündengüne eriyor.", "Omuz omuza yürüdük.", "Yavaş-yavaş yürüdü."], dogru=2,
  aciklama=f"İkilemeler ayrı yazılır; araya çizgi konmaz: omuz omuza {K5}.")
a("u1k5", "Araya İşaret Konmaz", "dy", ifade="“Dostlukta iyi-kötü her anı paylaşmalıyız.” cümlesinde ikilemenin yazımı doğrudur.", dogru=False,
  duzeltme="İkilemenin arasına kısa çizgi konmaz: iyi kötü.",
  aciklama=f"İkilemenin arasına virgül ya da çizgi konmaz {K5}.")
a("u1k5", "Eksik Bırakılan Cevap", "eslestir", soru="Üç noktanın kullanıldığı cümleleri görevleriyle eşleştir.", ciftler=[
  {"sol": "— Ödevini yaptın mı? — Şey…", "sag": "Eksik bırakılan cevap"},
  {"sol": "Barış… Barış!..", "sag": "Seslenmeyi pekiştirme"},
  {"sol": "Kapıyı yavaşça açtı ve…", "sag": "Sözü okuyucuya bırakma"}],
  aciklama=f"Üç noktanın üç görevi: eksik cevap, pekiştirme, sözü okura bırakma {K5}.")
a("u1k5", "Ünlemden Sonra İki Nokta", "secim", soru="Hangisinin noktalaması doğrudur?",
  secenekler=["Eyvah!...", "Gerçekten mi?...", "Barış!..", "Of!...."], dogru=2,
  aciklama=f"Ünlem ve soru işaretinden sonra iki nokta yeter: !.. ve ?.. {K5}.")
a("u1k5", "İkileme", "kisa", soru="“Yavaş yavaş, tekrar tekrar, iyi kötü” gibi anlamı güçlendirmek için yan yana kullanılan kelimelere ne denir?", yanit="ikileme", kabul=["ikilemeler"],
  aciklama=f"İki kelime yan yana, anlam güçlenir: ikileme {K5}.")

# --- Konu 6: Düşünceyi geliştirme yolları
a("u1k6", "Tanımlama", "secim", soru="“Kesir, bir bütünün eş parçalarını gösteren sayıdır.” cümlesinde hangi düşünceyi geliştirme yolu kullanılmıştır?",
  secenekler=["Tanımlama", "Benzetme", "Tanık gösterme", "Sayısal veri"], dogru=0,
  aciklama=f"“Nedir?” sorusuna cevap veren, “-dir” ile biten cümle tanımdır {K6}.")
a("u1k6", "Benzetme", "secim", soru="“Hayat, tıpkı bir nehrin suyu gibi akıp gider.” cümlesinde hangi yol kullanılmıştır?",
  secenekler=["Örneklendirme", "Karşılaştırma", "Benzetme", "Tanımlama"], dogru=2,
  aciklama=f"Ortak özellik ve “gibi” varsa benzetmedir {K6}.")
a("u1k6", "Sayısal Verilerden Yararlanma", "secim", soru="Hangi cümlede sayısal verilerden yararlanılmıştır?",
  secenekler=["Kitap okumak hayal gücünü geliştirir.", "Okulumuzdaki öğrencilerin yüzde 70'i her gün kitap okuyor.", "Kitap, insanın en iyi dostudur.", "Atatürk “Okumak çok önemlidir.” der."], dogru=1,
  aciklama=f"Sayı ve yüzde varsa sayısal verilerden yararlanılmıştır {K6}.")
a("u1k6", "Tanık Gösterme", "eslestir", soru="Cümleleri düşünceyi geliştirme yollarıyla eşleştir.", ciftler=[
  {"sol": "Heraklit, bir nehirde iki kez yıkanılamayacağını söyler.", "sag": "Tanık gösterme"},
  {"sol": "Meyveler, örneğin elma ve portakal, vitamin bakımından zengindir.", "sag": "Örneklendirme"},
  {"sol": "Kedi, köpeğe göre daha bağımsız bir hayvandır.", "sag": "Karşılaştırma"}],
  aciklama=f"Ünlü sözü tanık, “örneğin” örneklendirme, “göre” karşılaştırmadır {K6}.")
a("u1k6", "Karşılaştırma", "dy", ifade="“Gençlikte çok görünen vakit, yaş ilerledikçe azalır.” cümlesinde karşılaştırma yapılmıştır.", dogru=True,
  aciklama=f"Gençlik ile ileri yaş karşılaştırılıyor {K6}.")

# --- Konu 7: Sebep-sonuç metin yapısı
a("u1k7", "Sebep ve Sonuç", "secim", soru="“Yağmur yağdığı için maç ertelendi.” cümlesinde sebep hangisidir?",
  secenekler=["Maçın ertelenmesi", "Yağmurun yağması", "Maçın oynanması", "Seyircilerin gelmesi"], dogru=1,
  aciklama=f"“Neden?” diye sor: yağmur yağdığı için. Cevap sebeptir {K7}.")
a("u1k7", "İpucu İfadeleri", "secim", soru="“Servis geç geldi, ___ derse geç kaldık.” Boşluğa hangisi gelmelidir?",
  secenekler=["çünkü", "bu yüzden", "örneğin", "gibi"], dogru=1,
  aciklama=f"Boşluktan sonra sonuç geliyor. Sonucu “bu yüzden” bağlar {K7}.")
a("u1k7", "Sebep-Sonuç Zinciri", "secim", soru="Hangisi bir sebep-sonuç zinciridir?",
  secenekler=["Elma, armut ve kiraz meyvedir.", "Uyuyamadı, yorgun kalktı, derste dikkati dağıldı.", "Kedi miyavlar, köpek havlar.", "Bugün pazartesi."], dogru=1,
  aciklama=f"Her sonuç yeni bir sebep olmuş: uykusuzluk, yorgunluk, dikkatsizlik {K7}.")
a("u1k7", "İpucu İfadeleri", "dytablo", soru="Her ifade için Doğru ya da Yanlış seç.", ifadeler=[
  {"s": "“çünkü” sebebi gösterir.", "d": True},
  {"s": "“bu yüzden” sebebi gösterir.", "d": False},
  {"s": "“-den dolayı” sebebi gösterir.", "d": True},
  {"s": "“sonuç olarak” sonucu gösterir.", "d": True}],
  aciklama=f"Sebep: çünkü, -den dolayı. Sonuç: bu yüzden, sonuç olarak {K7}.")
a("u1k7", "Çok Sebep Bir Sonuç", "secim", metin=["Selin her gün düzenli çalıştı.", "Bilmediği konuları öğretmenine sordu.", "Sınavdan önceki gece de erken uyudu.", "Bu yüzden sınavdan yüksek not aldı."],
  soru="Bu metin hangi sebep-sonuç şemasına uygundur?",
  secenekler=["Bir sebep, çok sonuç", "Çok sebep, bir sonuç", "Sebep-sonuç zinciri", "Sebep-sonuç yok"], dogru=1,
  aciklama=f"Üç sebep tek bir sonuca götürüyor: yüksek not {K7}.")

# --- Konu 8: Söz sanatları ve şiirin ahengi
a("u1k8", "Kişileştirme", "secim", soru="“Dağlar karlı başını göğe kaldırdı.” dizesinde hangi söz sanatı vardır?",
  secenekler=["Abartma", "Kişileştirme", "Konuşturma", "Benzetme"], dogru=1,
  aciklama=f"Başını kaldırmak insana ait bir davranış. Dağlara verilmiş: kişileştirme {K8}.")
a("u1k8", "Abartma", "secim", soru="“Gözlerimden seller aktı.” dizesinde hangi söz sanatı vardır?",
  secenekler=["Abartma", "Konuşturma", "Kişileştirme", "Tanık gösterme"], dogru=0,
  aciklama=f"Gözden sel akmaz. Gerçekte olamayacak kadar büyütülmüş: abartma {K8}.")
a("u1k8", "Konuşturma", "dy", ifade="Karınca, “Kış gelmeden yiyecek toplamalıyım.” dedi. Bu cümlede konuşturma vardır.", dogru=True,
  aciklama=f"İnsan dışı bir varlık konuşuyorsa konuşturmadır {K8}.")
a("u1k8", "Dize ve Dörtlük", "kisa", soru="Altı dörtlükten oluşan bir şiir kaç dizedir?", yanit="24", sayi=True,
  aciklama=f"Bir dörtlük 4 dizedir. 6 × 4 = 24 {K8}.")
a("u1k8", "Uyak ve Redif", "secim", soru="“güller / bülbüller” sözcüklerinin sonundaki “-ler” eki için hangisi doğrudur?",
  secenekler=["Uyaktır.", "Rediftir.", "Hece ölçüsüdür.", "Dörtlüktür."], dogru=1,
  aciklama=f"Dize sonunda tekrar eden aynı ek rediftir. Benzer ses uyaktır {K8}.")

# --- Konu 9: İkna eden paragraf
a("u1k9", "İkna Paragrafı", "secim", soru="Hangisi bir ikna paragrafının konusu olabilir?",
  secenekler=["Ankara'nın nüfusu", "Kedimin rengi", "Annemi kampa gitmeme izin vermesi için ikna etmek", "Suyun kaynama sıcaklığı"], dogru=2,
  aciklama=f"İkna paragrafı bir isteği ya da öneriyi kabul ettirmek için yazılır {K9}.")
a("u1k9", "Gerekçeler", "secim", soru="İkna paragrafında gerekçe vermenin amacı nedir?",
  secenekler=["İsteğin neden haklı olduğunu göstermek", "Konuyu değiştirmek", "Okuru güldürmek", "Paragrafı uzatmak"], dogru=0,
  aciklama=f"Gerekçeler isteğin neden haklı olduğunu gösterir {K9}.")
a("u1k9", "Reddedilmeye Karşı Cevap", "secim", soru="“Derslerim aksar diye düşünebilirsin ama kurs haftada yalnızca üç saat.” cümlesi ikna paragrafının hangi bölümüdür?",
  secenekler=["İstek", "Faydalar", "Reddedilmeye karşı cevap", "Başlık"], dogru=2,
  aciklama=f"Karşıdakinin endişesini tahmin edip cevap veriyor {K9}.")
a("u1k9", "Faydalar ve Önemi", "bosluk", havuz=["başlık", "özet"], cumleler=[
  {"c": "İkna paragrafının girişinde ___ açıkça söylenir.", "cevap": "istek"},
  {"c": "Ardından isteğin neden haklı olduğunu gösteren ___ verilir.", "cevap": "gerekçeler"},
  {"c": "Sonunda isteğin ___ anlatılır.", "cevap": "faydaları"}],
  aciklama=f"Sıra: istek, gerekçeler, itiraza cevap, faydalar {K9}.")
a("u1k9", "Plan ve Taslak", "dy", ifade="İkna paragrafı planlama, taslak yazma, gözden geçirme ve paylaşma sırasıyla yazılır.", dogru=True,
  aciklama=f"Planla, yaz, düzelt, paylaş {K9}.")
H.yaz()
