import json, os
ONC = ["Yalnız I", "I ve II", "II ve III", "I, II ve III"]
Q = []
def add(konu, kavram, tur, **k): Q.append({"id": f"f1-{len(Q)+1:02d}", "konu": konu, "kavram": kavram, "tur": tur, **k})
P1, P2, P3, P4, P5, P6, P7 = "(s. 15–19)", "(s. 19, 22–23)", "(s. 20–21, 26–28)", "(s. 24–25, 30–32)", "(s. 34–42)", "(s. 43–45)", "(s. 46–50)"

# --- Konu 1: Uzay ve Uzay Araçları
add("u1k1", "Uzay Sondası", "eslestir", soru="Uzay araçlarını görevleriyle eşleştir.", ciftler=[
  {"sol": "Uzay roketi", "sag": "Uzay araçlarını yeryüzünden yörüngeye ya da daha uzağa taşır."},
  {"sol": "Yapay uydu", "sag": "Dünya'nın çevresinde belirli bir yörüngede döner; iletişim ve gözlem için kullanılır."},
  {"sol": "Uzay sondası", "sag": "Bir gök cismini incelemek için gönderilen, içinde insan olmayan robot araçtır."},
  {"sol": "Uzay mekiği", "sag": "Astronotları ve malzemeleri uzay istasyonuna taşır, yeniden kullanılabilir."}],
  aciklama=f"Roket taşır, uydu yörüngede döner, sonda inceler, mekik astronot taşır {P1}.")
add("u1k1", "Uzay İstasyonu", "secim", soru="Uzay araçlarıyla ilgili aşağıdaki ifadeler verilmiştir.",
  onculler=["Uzay sondalarının içinde insan bulunmaz.", "Uzay roketleri bugün hâlâ yalnızca tek kullanımlıktır.", "Uzay istasyonu yeniden kullanılabilen bir araçtır."],
  kok="Bu ifadelerden hangileri doğrudur?", secenekler=ONC, dogru=0,
  aciklama=f"Sondalarda insan yoktur. Roketler önceden tek kullanımlıktı, artık yeniden kullanılabiliyor. Uzay istasyonu yeniden kullanılamaz; bakım ve onarımla ömrü uzatılır {P1}.")
add("u1k1", "Uzay Mekiği", "dy", ifade="Uzay mekiğini, Dünya'dan kontrol edilen bir robot yönetir.", dogru=False,
  duzeltme="Uzay mekiğini içindeki astronotlar kontrol eder.", aciklama=f"Uzay sondası ve uydu Dünya'dan kontrol edilir; uzay mekiğini ise içindeki astronotlar kontrol eder {P1}.")
add("u1k1", "Uzay Sondası", "kisa", soru="Bir gök cismini incelemek için gönderilen, içinde insan bulunmayan robot uzay aracına ne ad verilir?",
  yanit="uzay sondası", kabul=["sonda"], aciklama=f"Uzay sondası robot bir kâşiftir; Dünya'dan kontrol edilir {P1}.")
add("u1k1", "Uzay İstasyonu", "secim", soru="Uzay istasyonu ile ilgili aşağıdakilerden hangisi yanlıştır?",
  secenekler=["Dünya'nın yörüngesinde dolanır.", "Astronotlar burada yaşar ve deney yapar.", "Yeniden kullanılabilen bir uzay aracıdır.", "Bakım ve onarımla ömrü uzatılabilir."], dogru=2,
  aciklama=f"Uzay istasyonu yeniden kullanılamaz; bakım ve onarımla ömrü uzatılır {P1}.")
add("u1k1", "Yapay Uydu", "bosluk", havuz=["uzay mekiği"], cumleler=[
  {"c": "Uzay araçlarını yeryüzünden yörüngeye taşıyan araç: ___", "cevap": "uzay roketi"},
  {"c": "Televizyon yayını ve hava durumu bilgisi için kullanılan araç: ___", "cevap": "yapay uydu"},
  {"c": "Uydular enerjilerini ___ sayesinde elde eder.", "cevap": "güneş panelleri"},
  {"c": "Astronotların yaşayıp deney yaptığı, yörüngede dolanan araç: ___", "cevap": "uzay istasyonu"}],
  aciklama=f"Roket taşır, uydu iletişim ve gözlem yapar, enerji güneş panellerinden gelir, istasyon uzaydaki ev ve laboratuvardır {P1}.")

# --- Konu 2: Teleskoplar ve Gözlemevleri
add("u1k2", "Uzay Teleskobu", "secim", soru="Uzay teleskoplarıyla ilgili aşağıdaki ifadeler verilmiştir.",
  onculler=["Atmosferin engellediği ışınlardan etkilenmezler.", "Yer tabanlı teleskoplara göre daha net ve ayrıntılı görüntü elde ederler.", "Yapay uyduların gökyüzünde bıraktığı ışık izleri onların gözlemini zorlaştırmaz."],
  kok="Bu ifadelerden hangileri doğrudur?", secenekler=ONC, dogru=3,
  aciklama=f"Atmosfer, hava kirliliği ve uyduların ışık izleri yeryüzünden gözlemi zorlaştırır; uzay teleskobu bu sorunlarla karşılaşmaz, daha net görüntü alır {P2}.")
add("u1k2", "Gözlemevi", "secim", soru="Bir gözlemevi kurmak için dört bölge inceleniyor.",
  tablo={"baslik": "Bölgelerin özellikleri", "basliklar": ["Bölge", "Yükseklik", "Yerleşim yerine", "Deprem kuşağı", "Yılda açık gün"],
         "satirlar": [["K", "Yüksek", "Şehrin içinde", "Değil", "300"], ["L", "Alçak", "Uzak", "Değil", "280"], ["M", "Yüksek", "Uzak", "Üzerinde", "290"], ["N", "Yüksek", "Uzak", "Değil", "310"]]},
  kok="", secenekler=["K", "L", "M", "N"], dogru=3, metinBaslik="",
  aciklama=f"Gözlemevi yüksek, yerleşim yerlerinden uzak, deprem kuşağında olmayan ve havası gözleme uygun (açık gün sayısı çok) yerlere kurulur. Hepsini sağlayan N'dir {P2}.")
Q[-1]["soru"] = "Bir gözlemevi kurmak için dört bölge inceleniyor. Tabloya göre gözlemevi için en uygun bölge hangisidir?"
del Q[-1]["kok"]; del Q[-1]["metinBaslik"]
add("u1k2", "James Webb Uzay Teleskobu", "dy", ifade="James Webb Uzay Teleskobu, Hubble Uzay Teleskobu'ndan yaklaşık 100 kat daha güçlüdür.", dogru=True,
  aciklama=f"James Webb tenis kortu büyüklüğündedir ve Hubble'dan 100 kat daha güçlüdür {P2}.")
add("u1k2", "Yer Tabanlı Teleskop", "dytablo", soru="Teleskoplarla ilgili her ifade için Doğru (D) ya da Yanlış (Y) seç.", ifadeler=[
  {"s": "Hubble Uzay Teleskobu 1990'da Dünya yörüngesine taşındı.", "d": True},
  {"s": "James Webb, rokete sığması için origami tekniğiyle katlandı.", "d": True},
  {"s": "Yer tabanlı teleskopların maliyeti uzay teleskoplarından yüksektir.", "d": False},
  {"s": "Işık kirliliği gökyüzü gözlemini kolaylaştırır.", "d": False}],
  aciklama=f"Yer tabanlı teleskoplar ucuzdur, bakımı kolaydır. Işık kirliliği gözlemi zorlaştırır {P2}.")
add("u1k2", "Gözlemevi", "kisa", soru="Teleskopların yerleştirildiği kubbe benzeri yapılara gözlemevi denir. Gözlemevinin diğer adı nedir?",
  yanit="rasathane", aciklama=f"Gözlemevinin diğer adı rasathanedir {P2}.")
add("u1k2", "Işık Kirliliği", "secim", soru="Şehirlerde teleskopla net görüntü almak zordur. Bunun en önemli sebebi aşağıdakilerden hangisidir?",
  secenekler=["Işık kirliliği", "Ses kirliliği", "Toprak kirliliği", "Su kirliliği"], dogru=0,
  aciklama=f"Yanlış ve fazla kullanılan ışık gökyüzü gözlemini olumsuz etkiler; bu yüzden yaylalarda ve yüksek yerlerde daha net gözlem yapılır {P2}.")

# --- Konu 3: Türkiye Uzayda
add("u1k3", "Gözlem Uydusu", "secim", soru="Aşağıdaki uydularımızdan hangisi bir gözlem uydusudur?",
  secenekler=["Türksat 5A", "İMECE", "Türksat 6A", "Türksat 5B"], dogru=1,
  aciklama="İMECE gözlem uydusudur; Türksat uyduları haberleşme uydusudur (s. 20).")
add("u1k3", "Haberleşme Uydusu", "eslestir", soru="Uyduları ve kuruluşu doğru açıklamayla eşleştir.", ciftler=[
  {"sol": "Türksat 6A", "sag": "İlk yerli ve millî haberleşme uydumuzdur (2024)."},
  {"sol": "İMECE", "sag": "Dünya'nın her yerinden görüntü alabilen gözlem uydumuzdur (2023)."},
  {"sol": "Türksat 1B", "sag": "Uzaydaki ilk haberleşme uydumuzdur (1994)."},
  {"sol": "TÜBİTAK UZAY", "sag": "Yerli ve millî uydular geliştiren araştırma kuruluşudur."}],
  aciklama="Türksat 1B ilk, Türksat 6A ilk yerli ve millî haberleşme uydumuzdur; İMECE gözlem uydusudur (s. 20–21).")
add("u1k3", "Gözlem Uydusu", "dy", ifade="Bilsat ve Rasat, görev süresini doldurup ömrünü tamamlamış gözlem uydularımızdır.", dogru=True,
  aciklama="Kitap, Bilsat ve Rasat'ı ömrünü tamamlamış gözlem uyduları olarak verir (s. 21).")
add("u1k3", "Astronot", "kisa", soru="1961'de Vostok 1 aracıyla Dünya'nın yörüngesine giren ve uzaya çıkan ilk insan kimdir?",
  yanit="Yuri Gagarin", kabul=["Gagarin"], aciklama="Uzaya çıkan ilk insan kozmonot Yuri Gagarin'dir (s. 26).")
add("u1k3", "Alper Gezeravcı", "secim", soru="Alper Gezeravcı'nın görev armasıyla ilgili aşağıdaki ifadeler verilmiştir.",
  onculler=["Arma, yer ve gök arasındaki bağlantıyı simgeleyen sekiz köşeli Selçuklu yıldızı içindedir.", "Bayrağımızın etrafındaki 16 yıldız, 16 Türk devletini temsil eder.", "Turkuaz renkli Türkiye haritası, uzayda yapılan 13 deneyi simgeler."],
  kok="Bu ifadelerden hangileri doğrudur?", secenekler=ONC, dogru=1,
  aciklama="Turkuaz renkli harita, Dünya üzerinde Türkiye'yi gösterir; deneyleri simgelemez (s. 27).")
add("u1k3", "Alper Gezeravcı", "bosluk", havuz=["14", "TÜBİTAK UZAY"], cumleler=[
  {"c": "Alper Gezeravcı uzayda ___ gün kaldı.", "cevap": "18"},
  {"c": "Gezeravcı uzayda ___ bilimsel deney yaptı.", "cevap": "13"},
  {"c": "Kısa adı TUA olan ___ 2018'de kuruldu.", "cevap": "Türkiye Uzay Ajansı"}],
  aciklama="14 gün kalması planlanıyordu ama hava koşulları yüzünden 18 gün kaldı; 13 deney yaptı. TUA, Türkiye Uzay Ajansı'dır (s. 26–28).")
add("u1k3", "Astronomi ve Astronom", "secim", soru="Gök cisimlerinin konumlarını, hareketlerini, yapılarını ve uzaklıklarını inceleyen bilim dalı hangisidir?",
  secenekler=["Astronomi", "Jeoloji", "Biyoloji", "Meteoroloji"], dogru=0, aciklama=f"Astronomi (gök bilimi) gök cisimlerini inceler {P3}.")

# --- Konu 4: Uzay Teknolojisinin Faydaları ve Uzay Kirliliği
add("u1k4", "Enerji ve İletişim Alanında", "dytablo", soru="Uzay teknolojisinin faydalarıyla ilgili her ifade için D ya da Y seç.", ifadeler=[
  {"s": "Navigasyonda kullanılan GPS, uzay teknolojisi sayesinde çalışır.", "d": True},
  {"s": "Bebek maması gibi toz gıdalar, astronot yiyecekleri için geliştirilen teknolojiden doğmuştur.", "d": True},
  {"s": "Güneş panelleri yalnızca uydularda kullanılır.", "d": False},
  {"s": "Duman dedektörü, uzay araştırmaları sırasında geliştirilen bir üründür.", "d": True}],
  aciklama=f"Güneş panelleri bugün evlerde de elektrik üretir {P4}.")
add("u1k4", "Sağlık Alanında", "eslestir", soru="Uzay teknolojisinin kullanıldığı alanları örnekleriyle eşleştir.", ciftler=[
  {"sol": "Sağlık", "sag": "MR ve ultrason cihazları"}, {"sol": "Gıda", "sag": "Toz bebek maması ve puding"},
  {"sol": "Ulaşım", "sag": "Navigasyon (GPS)"}, {"sol": "Endüstri", "sag": "Termal battaniye ve ısıya dayanıklı kıyafet"}],
  aciklama=f"Uzay araştırmaları için geliştirilen teknolojiler sağlık, gıda, ulaşım ve endüstride kullanılıyor {P4}.")
add("u1k4", "Uzay Kirliliği", "secim", soru="Uzay kirliliğiyle ilgili aşağıdaki ifadeler verilmiştir.",
  onculler=["Uzay çöpleri yalnızca görevini bitirmiş uydulardan oluşur.", "Çok hızlı hareket ettikleri için küçük bir uzay çöpü bile uzay aracına büyük zarar verebilir.", "Önlem alınmazsa haberleşmede ve uzay araştırmalarında aksamalar olabilir."],
  kok="Bu ifadelerden hangileri doğrudur?", secenekler=ONC, dogru=2,
  aciklama=f"Uzay çöpleri yalnızca uydular değildir; roket parçaları ve yakıt tankları da uzay çöpüdür {P4}.")
add("u1k4", "Ulaşım Alanında", "kisa", soru="Akıllı telefon ve otomobillerde yol tarifi almak için kullanılan, uzay teknolojisi sayesinde çalışan sistemin kısa adı nedir?",
  yanit="GPS", kabul=["küresel konumlama sistemi", "navigasyon"], aciklama=f"GPS, Küresel Konumlama Sistemi'dir {P4}.")
add("u1k4", "Uzay Çöpünün Zararı ve Çözümü", "secim", soru="Aşağıdakilerden hangisi uzay çöpü sorununa çözüm olamaz?",
  secenekler=["Uzay çöplerini yakalayıp Dünya'ya getirmek", "Daha çevreci uzay teknolojileri geliştirmek", "Görevi biten uyduları yörüngede kendi hâline bırakmak", "Atık bırakmayan uzay araçları tasarlamak"], dogru=2,
  aciklama=f"Görevi biten uydular yörüngede bırakılırsa uzay çöpü artar {P4}.")
add("u1k4", "Uzay Kirliliği", "dy", ifade="Uzay Gözetim Ağı (SSN), uzay çöplerini radar ve teleskoplarla izler.", dogru=True,
  aciklama=f"SSN, uzay çöplerini radar ve teleskoplarla izler {P4}.")

# --- Konu 5: Yıldızların Doğumu ve Yaşamı
add("u1k5", "Küçük Kütleli Yıldız", "secim", soru="Güneş gibi küçük kütleli bir yıldızın yaşam sürecindeki sıralama hangisinde doğru verilmiştir?",
  secenekler=["Bulutsu → ön yıldız → yıldız → kırmızı dev → gezegenimsi bulutsu → beyaz cüce",
              "Bulutsu → ön yıldız → yıldız → kırmızı süperdev → süpernova → kara delik",
              "Ön yıldız → bulutsu → yıldız → beyaz cüce → kırmızı dev",
              "Bulutsu → yıldız → ön yıldız → süpernova → beyaz cüce"], dogru=0,
  aciklama=f"Küçük kütleli yıldız kırmızı dev, sonra gezegenimsi bulutsu olur; geriye beyaz cüce kalır {P5}.")
add("u1k5", "Işık Yılı", "bosluk", havuz=["zaman", "süpernova"], cumleler=[
  {"c": "Işık yılı bir ___ ölçü birimidir.", "cevap": "uzunluk"},
  {"c": "Küçük kütleli yıldızın yaşamı sonunda geriye ___ kalır.", "cevap": "beyaz cüce"},
  {"c": "Büyük kütleli yıldız, patlamadan önce ___ hâline gelir.", "cevap": "kırmızı süperdev"},
  {"c": "Yıldızlar ___ denen bölgelerde doğar.", "cevap": "bulutsu"}],
  aciklama=f"Işık yılı uzaklık ölçer. Küçük kütleli yıldız beyaz cüce olur; büyük kütleli yıldız kırmızı süperdev olup patlar. Yıldızlar bulutsuda doğar {P5}.")
add("u1k5", "Yaşamı Kütle Belirler", "dy", ifade="Bir yıldızın kütlesi ne kadar büyükse yaşamı o kadar uzun olur.", dogru=False,
  duzeltme="Kütle ne kadar büyükse yaşam o kadar kısa olur.", aciklama=f"Yıldızların yaşam sürecini kütleleri belirler: büyük kütle, kısa yaşam {P5}.")
add("u1k5", "Büyük Kütleli Yıldız", "kisa", soru="Büyük kütleli yıldızların yaşamını sona erdiren patlamanın adı nedir?",
  yanit="süpernova", kabul=["süpernova patlaması"], aciklama=f"Büyük kütleli yıldızların yaşamı süpernova patlamasıyla son bulur {P5}.")
add("u1k5", "Bulutsu", "secim", soru="Yıldızlarla ilgili aşağıdaki ifadeler verilmiştir.",
  onculler=["Atbaşı, Orion ve Tarantula bilinen bulutsulardandır.", "Bulutsular hidrojen gazı, toz ve diğer materyallerden oluşur.", "Güneş, yaşamını süpernova patlamasıyla bitirecektir."],
  kok="Bu ifadelerden hangileri doğrudur?", secenekler=ONC, dogru=1,
  aciklama=f"Güneş küçük kütleli bir yıldızdır; kırmızı dev olur ve sonunda beyaz cüceye dönüşür, süpernova olmaz {P5}.")
add("u1k5", "Işık Yılı", "dytablo", soru="Her ifade için D ya da Y seç.", ifadeler=[
  {"s": "Proxima Centauri, Güneş sistemimize yaklaşık 4,24 ışık yılı uzaklıktadır.", "d": True},
  {"s": "Işık yılı bir zaman birimidir.", "d": False},
  {"s": "Ön yıldız, donuk kırmızı bir yapıdır.", "d": True},
  {"s": "Büyük kütleli bir yıldızın yaşamı sonunda geriye nötron yıldızı ya da kara delik kalabilir.", "d": True}],
  aciklama=f"Işık yılı uzaklık birimidir: ışığın bir yılda aldığı yol {P5}.")

# --- Konu 6: Takımyıldızlar
add("u1k6", "Kutup Yıldızı'nı Bulma", "secim", soru="Büyükayı takımyıldızını kullanarak Kutup Yıldızı nasıl bulunur?",
  secenekler=["Cezvenin uçtaki iki yıldızı arasındaki mesafenin 5 katı kadar ilerlenir.", "Cezvenin sapındaki üç yıldızın ortasına bakılır.", "Kraliçe takımyıldızının en parlak yıldızına bakılır.", "Gökyüzünde güney yönüne bakılır."], dogru=0,
  aciklama=f"Cezvenin uç kısmındaki iki yıldız arasındaki mesafenin 5 katı uzakta Kutup Yıldızı bulunur {P6}.")
add("u1k6", "Yıldız Kümesi", "dy", ifade="Takımyıldız ile yıldız kümesi aynı anlama gelir.", dogru=False,
  duzeltme="Yıldız kümesi, birbirine kütle çekimiyle bağlı yıldız grubudur; takımyıldız ise gökyüzünde yakın görünüp şekil oluşturan yıldızlardır.",
  aciklama=f"Kitap, yıldız kümesi ile takımyıldızın farklı anlamlara geldiğini vurgular {P6}.")
add("u1k6", "Kutup Yıldızı", "kisa", soru="Kuzey yarım kürede her zaman kuzey yönünü gösteren yıldızın adı nedir?",
  yanit="Kutup Yıldızı", kabul=["Polaris", "kutup"], aciklama=f"Kutup Yıldızı'nın diğer adı Polaris'tir; hep kuzeyi gösterir {P6}.")
add("u1k6", "Takımyıldız", "eslestir", soru="Kavramları açıklamalarıyla eşleştir.", ciftler=[
  {"sol": "Büyükayı", "sag": "Yedi yıldızdan oluşur, cezveye benzer."}, {"sol": "Kraliçe", "sag": "W harfine benzeyen takımyıldızdır."},
  {"sol": "Kutup Yıldızı", "sag": "Hep kuzey yönünü gösterir."}, {"sol": "Yıldız kümesi", "sag": "Birbirine kütle çekimiyle bağlı yıldız grubudur."}],
  aciklama=f"Büyükayı cezve, Kraliçe W biçimindedir; Kutup Yıldızı kuzeyi gösterir; yıldız kümesi kütle çekimiyle bağlıdır {P6}.")

# --- Konu 7: Galaksi ve Evren
add("u1k7", "İç İçe Kavramlar", "secim", soru="Aşağıdakilerden hangisi küçükten büyüğe doğru sıralanmıştır?",
  secenekler=["Dünya → Güneş sistemi → Samanyolu → evren", "Evren → Samanyolu → Güneş sistemi → Dünya", "Dünya → Samanyolu → Güneş sistemi → evren", "Güneş sistemi → Dünya → evren → Samanyolu"], dogru=0,
  aciklama=f"Dünya Güneş sistemindedir, Güneş sistemi Samanyolu'nda, Samanyolu da evrendedir {P7}.")
add("u1k7", "Andromeda Galaksisi", "kisa", soru="Samanyolu galaksisine en yakın galaksinin adı nedir?",
  yanit="Andromeda", aciklama=f"Samanyolu'na en yakın galaksi Andromeda'dır; o da sarmaldır {P7}.")
add("u1k7", "Evren", "bosluk", havuz=["Andromeda", "Gagarin"], cumleler=[
  {"c": "Dünya, yıldızlar, gezegenler ve galaksiler gibi tüm gök cisimlerini içine alan boşluğa ___ denir.", "cevap": "evren"},
  {"c": "Galaksileri ilk keşfeden bilim insanı: ___", "cevap": "Edwin Hubble"},
  {"c": "Güneş sistemi, ___ galaksisinde yer alır.", "cevap": "Samanyolu"},
  {"c": "Güneş sistemi, Samanyolu'nun ___ (Orion) kolunda bulunur.", "cevap": "Avcı"}],
  aciklama=f"Evren her şeyi içine alır. Galaksileri Edwin Hubble keşfetti. Güneş sistemi Samanyolu'nun Avcı kolundadır {P7}.")
add("u1k7", "Galaksilerin Farkları", "dy", ifade="Bütün galaksilerin büyüklükleri ve şekilleri aynıdır.", dogru=False,
  duzeltme="Galaksilerin büyüklükleri, şekilleri ve içlerindeki gök cismi sayıları farklıdır.", aciklama=f"Galaksiler birbirinin aynısı değildir {P7}.")
add("u1k7", "Samanyolu Galaksisi", "secim", soru="Galaksilerle ilgili aşağıdaki ifadeler verilmiştir.",
  onculler=["Samanyolu, sarmal kolları olan bir galaksidir.", "Andromeda'nın çapı, Samanyolu'nun çapının yaklaşık iki katıdır.", "Galaksileri ilk keşfeden bilim insanı Yuri Gagarin'dir."],
  kok="Bu ifadelerden hangileri doğrudur?", secenekler=ONC, dogru=1,
  aciklama=f"Galaksileri ilk keşfeden Edwin Hubble'dır; Gagarin uzaya çıkan ilk insandır {P7}.")

# ---------- Doğrulama
kok = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public/fen1")
ad = {k: {x["ad"] for x in json.load(open(f"{kok}/konular/{k}.json", encoding="utf-8"))["kavramlar"]} for k in {q["konu"] for q in Q}}
h, tur, dag = [], {}, [0, 0, 0, 0]
for q in Q:
    tur[q["tur"]] = tur.get(q["tur"], 0) + 1
    if q["kavram"] not in ad[q["konu"]]: h.append(f"{q['id']}: kavram yok {q['kavram']}")
    if not q.get("aciklama"): h.append(q["id"] + ": açıklama yok")
    t = q["tur"]
    if t == "secim":
        if len(q["secenekler"]) != 4 or len(set(q["secenekler"])) != 4 or not 0 <= q["dogru"] < 4: h.append(q["id"] + ": seçenek")
        dag[q["dogru"]] += 1
    if t == "dy" and not isinstance(q["dogru"], bool): h.append(q["id"] + ": dy")
    if t == "bosluk":
        for c in q["cumleler"]:
            if c["c"].count("___") != 1: h.append(q["id"] + ": ___ sayısı")
        if set(q["havuz"]) & {c["cevap"] for c in q["cumleler"]}: h.append(q["id"] + ": havuz cevap içeriyor (motor ekler)")
    if t == "eslestir" and len(q["ciftler"]) < 3: h.append(q["id"] + ": eşleştirme az")
    if t == "kisa" and not q.get("yanit"): h.append(q["id"] + ": yanıt yok")
per = {}
for q in Q: per[q["konu"]] = per.get(q["konu"], 0) + 1
print("soru", len(Q), "| tür", tur, "| konu", per, "| doğru şık (secim, karışmadan önce)", dag)
print("HATA:" if h else "Sorun yok.", *h, sep="\n")
json.dump({"unite": 1, "ders": "fen1", "aciklama": "Sınav Provası soru havuzu (Ünite 1). Sorular kitaba dayanarak yazıldı; soru bankası sorularının yalnızca biçimi örnek alındı.", "sorular": Q},
          open(f"{kok}/sinav/u1.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
