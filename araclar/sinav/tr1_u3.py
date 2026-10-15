import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from ortak import Havuz, ONC, ONC2
H = Havuz("tr1", 3, "t3"); a = H.add

# --- Konu 1: Hikâyede duygu, bakış açısı ve bölümler ("Eskici")
a("u3k1", "Duygunun Sebebi", "eslestir", soru="Hasan'ın duygularını sebepleriyle eşleştir.", ciftler=[
  {"sol": "Vapurda çok eğlendi.", "sag": "Vinçleri, sandalları seyretti."},
  {"sol": "Durgunlaştı.", "sag": "Yolcular bilmediği bir dilde konuşmaya başladı."},
  {"sol": "Durmadan konuştu.", "sag": "Eskici Türkçe biliyordu."},
  {"sol": "Hıçkıra hıçkıra ağladı.", "sag": "Eskici gidiyordu."}],
  aciklama="Her duygunun bir sebebi vardır: Neden böyle hissetti? (s. 122–125)")
a("u3k1", "Duygunun İletişime Etkisi", "dy",
  ifade="Hasan halasının evinde anladığı Arapçayı hemen konuşmaya başladı.", dogru=False,
  duzeltme="Hasan anladığı Arapçayı bile konuşmadı, aylarca sustu.",
  aciklama="Yalnız ve kırgın olan Hasan susmayı seçti (s. 124).")
a("u3k1", "Bölümün Başladığı Cümle", "secim", soru="“Eskici” hikâyesiyle ilgili aşağıdaki ifadeler verilmiştir.",
  onculler=["Serimde Hasan vapurla yola çıkar.", "Düğümde Hasan kimseyle anlaşamaz ve susar.", "Çözümde Hasan İstanbul'a geri döner."],
  kok="Yukarıdakilerden hangileri doğrudur?", secenekler=ONC, dogru=1,
  aciklama="Hasan İstanbul'a dönmez; çözümde eskici gider, ikisi de ağlar (s. 125).")
a("u3k1", "Hikâye Unsurları", "bosluk", havuz=["başlık", "yazar"], cumleler=[
  {"c": "Olayın geçtiği yere ___ denir.", "cevap": "mekân"},
  {"c": "Olayın ne zaman geçtiğini ___ unsuru gösterir.", "cevap": "zaman"},
  {"c": "Hikâyede yaşanan, anlatılan şeye ___ denir.", "cevap": "olay"}],
  aciklama="Hikâye unsurları: olay, kişiler, mekân, zaman (s. 130).")
a("u3k1", "Olay Akışına Göre Özet", "secim", soru="Hangisi “Eskici”nin olay akışına uygun özetidir?",
  secenekler=["Eskici ağlar, sonra Hasan vapura biner, en sonda halasının evine gider.",
              "Hasan halasının yanına gönderilir, aylarca susar, eskiciyle konuşur, eskici gidince ağlar.",
              "Hasan trende deve görür; hikâye burada biter.",
              "Hasan eskiciye ayakkabı yapmayı öğrenir ve İzmit'e gider."], dogru=1,
  aciklama="Özette olaylar olduğu sırayla, kısaca anlatılır (s. 129).")
a("u3k1", "Bölümler Arası Geçiş", "kisa", soru="“Fakat, bir gün, nihayet” gibi bölümleri birbirine bağlayan ifadelere ne ad verilir?",
  yanit="geçiş ifadesi", kabul=["geçiş", "geçiş ifadeleri", "bağlantı ifadesi"],
  aciklama="Bu ifadeler okuru yeni bölüme geçirir (s. 129).")

# --- Konu 2: Eş sesli, deyim, kalıp ifade, öznel ve nesnel ("Ya Hayır Söyle...")
a("u3k2", "Kalıp İfade", "eslestir", soru="Durumu söylenen kalıp ifadeyle eşleştir.", ciftler=[
  {"sol": "Hasta bir arkadaşa", "sag": "Geçmiş olsun."},
  {"sol": "Yemek yiyen birine", "sag": "Afiyet olsun."},
  {"sol": "Sabah karşılaşınca", "sag": "Günaydın."},
  {"sol": "Çalışan birine", "sag": "Kolay gelsin."}],
  aciklama="Kalıp ifadeler belli durumlarda hep aynı biçimde söylenir (s. 134–135).")
a("u3k2", "Öznel ve Nesnel İfade", "dytablo", soru="İfade nesnelse D, öznelse Y seç.", ifadeler=[
  {"s": "“Hayır işlemek”, iyi bir iş yapmak demektir.", "d": True},
  {"s": "Günaydın, en güzel selamdır.", "d": False},
  {"s": "Türkiye'nin başkenti Ankara'dır.", "d": True},
  {"s": "Bu metin çok sıkıcı.", "d": False}],
  aciklama="Nesnel ifade kontrol edilebilir; öznel ifade kişisel görüştür (s. 138).")
a("u3k2", "Eş Sesli Kelimeler", "secim", soru="Hangi cümlede “hayır” kelimesi öteki cümlelerden farklı bir anlamda kullanılmıştır?",
  secenekler=["Hayır, bu akşam gelemem.", "Hayır, o çanta benim değil.", "Hayır, bunu ben söylemedim.", "Bu çeşmeyi hayır için yaptırdı."], dogru=3,
  aciklama="Son cümlede “hayır” iyilik demektir; ötekilerde olumsuz cevaptır (s. 135).")
a("u3k2", "Deyim", "secim", soru="Deyimlerle ilgili aşağıdaki ifadeler verilmiştir.",
  onculler=["Kalıplaşmıştır, kelimeleri değiştirilemez.", "Her zaman öğüt veren bir yargı bildirir.", "Çoğunlukla gerçek anlamından ayrı bir anlam taşır."],
  kok="Yukarıdakilerden hangileri doğrudur?", secenekler=ONC2, dogru=2,
  aciklama="Öğüt veren yargı atasözüdür; deyim çoğunlukla bir durumu anlatır.")
a("u3k2", "Metindeki Anlam ve Sözlük Anlamı", "bosluk", havuz=["başlangıç", "kazanç"], cumleler=[
  {"c": "“Yeğlemek” ___ etmek demektir.", "cevap": "tercih"},
  {"c": "“Akıbet” bir işin ___ demektir.", "cevap": "sonu"},
  {"c": "Kelimenin anlamını önce cümleden ___ ederiz.", "cevap": "tahmin"}],
  aciklama="Önce cümleden tahmin, sonra sözlükten kontrol (s. 136).")
a("u3k2", "Anahtar Söz Varlığı", "kisa", soru="Bir metnin konusunu taşıyan ve metinde sık geçen kelimelere ne ad verilir?",
  yanit="anahtar kelime", kabul=["anahtar kelimeler", "anahtar söz varlığı", "anahtar sözcük"],
  aciklama="Bunlar metnin anahtar söz varlığıdır (s. 136).")

# --- Konu 3: Bilgilendirici metin: giriş, gelişme, sonuç ve düşünceyi geliştirme
K3 = "(s. 167)"
a("u3k3", "Giriş", "eslestir", soru="Bölümü görevle eşleştir.", ciftler=[
  {"sol": "Giriş", "sag": "Konuyu tanıtır, ilgi çeker."},
  {"sol": "Gelişme", "sag": "Konuyu açıklar ve destekler."},
  {"sol": "Sonuç", "sag": "Toparlar, ana fikri vurgular."}],
  aciklama=f"Bilgilendirici metnin bölümleri: giriş, gelişme, sonuç {K3}.")
a("u3k3", "Sonuç", "secim", metin=["İletişim, insanlar arasında köprü kurar.", "Dinlemek de konuşmak kadar önemlidir.", "Kısacası iyi iletişim, iyi dinlemekle başlar."],
  soru="Bu metinde sonuç bölümünü gösteren ifade hangisidir?", secenekler=["İletişim", "Dinlemek", "Kısacası", "köprü"], dogru=2,
  aciklama="“Kısacası” metni toparlar; sonucun ipucudur.")
a("u3k3", "Yolu Metinde Bulma", "dytablo", soru="Cümle ile düşünceyi geliştirme yolu doğru eşleşmişse D, yanlışsa Y seç.", ifadeler=[
  {"s": "“Nezaket, iletişimin sağlam zemini gibidir.” → benzetme", "d": True},
  {"s": "“Mevlana «Hayır söyleyin ki hayır bulasınız.» der.” → tanık gösterme", "d": True},
  {"s": "“Açık bir ifade, belirsiz bir ifadeden daha etkilidir.” → tanımlama", "d": False}],
  aciklama="Üçüncü cümlede “daha” var; bu karşılaştırmadır (s. 134, 167).")
a("u3k3", "Bölümler Arası Akış", "secim", soru="“Dinlemeden kurulan iletişim eksik kalır. ___ iletişim bir üstünlük kurma çabası değildir.” Boşluğa hangisi gelmelidir?",
  secenekler=["Örneğin", "Çünkü", "Kısacası", "Oysa"], dogru=1,
  aciklama=f"İkinci cümle ilkinin sebebini veriyor; “çünkü” gelir {K3}.")
a("u3k3", "Anlatıma Katkısı", "secim", soru="Düşünceyi geliştirme yollarının anlatıma katkısıyla ilgili hangisi yanlıştır?",
  secenekler=["Tanık gösterme düşünceyi inandırıcı yapar.", "Örneklendirme düşünceyi somutlaştırır.", "Sayısal veriler düşünceyi kanıtlar.", "Benzetme metni her zaman kısaltır."], dogru=3,
  aciklama="Benzetme anlatımı canlandırır; metni kısaltmak görevi değildir (s. 168).")
a("u3k3", "Gelişme", "kisa", soru="Bilgilendirici metinde konunun açıklandığı ve örneklerle desteklendiği, en uzun bölüme ne ad verilir?",
  yanit="gelişme", kabul=["gelişme bölümü"],
  aciklama=f"Konu gelişmede açıklanır ve desteklenir {K3}.")
# --- Konu 4: Karşılaştırma: iki metin ve bir grafik ("Sağlıklı Aile", s. 151 grafiği)
TAB4 = {"baslik": "Genel ağ üzerinden yapılan telefon aramaları (s. 151)", "basliklar": ["Yıl", "Arama sayısı"],
        "satirlar": [["2010", "45.172"], ["2011", "17.017"], ["2012", "7.236"], ["2013", "4.840"], ["2014", "8.716"], ["2015", "2.957"], ["2016", "2.223"]]}
a("u3k4", "Grafikten Yargı Doğrulama", "dytablo", soru="Tabloya göre her ifade için Doğru ya da Yanlış seç.", tablo=TAB4, ifadeler=[
  {"s": "Arama sayısı 2010'dan 2013'e kadar her yıl azalmıştır.", "d": True},
  {"s": "2015'te arama sayısı bir önceki yıla göre artmıştır.", "d": False},
  {"s": "Arama sayısı en düşük değerine 2016'da inmiştir.", "d": True},
  {"s": "2012'deki arama sayısı 10 binden fazladır.", "d": False}],
  aciklama="Her yargıyı tablodaki sayıyla kontrol et; bir önceki yıla bak (s. 151).")
a("u3k4", "Artış ve Azalma", "bosluk", havuz=["eşitlik", "dikey"], cumleler=[
  {"c": "Bir yılın sayısı bir öncekinden büyükse ___ vardır.", "cevap": "artış"},
  {"c": "Bir yılın sayısı bir öncekinden küçükse ___ vardır.", "cevap": "azalma"},
  {"c": "Artış ya da azalmayı bulmak için bir ___ yıla bakılır.", "cevap": "önceki"}],
  aciklama="Bir öncekine bak: büyükse artış, küçükse azalma (s. 151).")
a("u3k4", "Karşılaştırma Ölçütü", "secim", soru="İki metni karşılaştırmaya başlamadan önce ilk olarak ne yapılmalıdır?",
  secenekler=["Metinlerin uzunluğu ölçülmelidir.", "Karşılaştırma ölçütü seçilmelidir.", "Yazarların hayatı araştırılmalıdır.", "Daha kısa olan metin seçilmelidir."], dogru=1,
  aciklama="Önce ölçüt seçilir: Neye göre bakıyorum? Kitapta ölçütler saygı, empati gibi kavramlardır (s. 150).")
a("u3k4", "Benzerlik ve Farklılık", "eslestir", soru="İfadeyi anlattığı şeyle eşleştir.", ciftler=[
  {"sol": "İkisi de saygıyı önemser.", "sag": "Benzerlik"},
  {"sol": "Biri aileyi anlatır, öteki ise sanal ortamı.", "sag": "Farklılık"},
  {"sol": "Saygı, empati, zorbalık", "sag": "Karşılaştırma ölçütü"}],
  aciklama="Ortak yön benzerlik, ayrı yön farklılıktır; neye göre baktığımız ölçüttür (s. 150).")
a("u3k4", "Metinleri Karşılaştırma", "secim", soru="“Sağlıklı Aile” metniyle ilgili aşağıdaki ifadeler verilmiştir.",
  onculler=["Kuşaklar arasındaki düşünce farklılıklarına saygı duyulduğunu söyler.", "Çocukların başkalarıyla karşılaştırılmasını önerir.", "Koşulsuz seven kişinin sevdiğini dinlediğini anlatır."],
  kok="Yukarıdakilerden hangileri metinde vardır?", secenekler=["Yalnız I", "I ve III", "II ve III", "I, II ve III"], dogru=1,
  aciklama="Metne göre çocuklar başkalarıyla karşılaştırılmaz; II yanlıştır (s. 149).")
a("u3k4", "Grafik Okuma", "kisa", soru="Kitaptaki grafikte yatay eksende yıllar vardır. Dikey eksende ne gösterilir?",
  yanit="arama sayısı", kabul=["arama sayısı", "aramaların sayısı", "telefon arama sayısı", "arama"],
  aciklama="Dikey eksende arama sayısı, yatay eksende yıllar vardır (s. 151).")
H.yaz()
