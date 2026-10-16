# -*- coding: utf-8 -*-
"""Matematik 3. Tema (İstatistiksel Araştırma) Sınav Provası havuzu: python3 araclar/sinav/mat1_u3.py"""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from ortak import Havuz, ONC
KOK = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")); sys.path.insert(0, KOK)
from gen_mat1 import altin_svg, kar_svg, atlama_svg, fidan_svg, kardes_svg, persentil_svg, cizgi_svg
H = Havuz("mat1", 3, "m3")
a = H.add
S1, S2, S3 = "(s. 159–164)", "(s. 165–168)", "(s. 169–170, 192–193)"
S4, S5 = "(s. 171–172)", "(s. 173–179)"

# --- Konu 1: Veri türleri
a("u3k1", "Kesikli Veri", "dytablo", soru="Her ifade için Doğru ya da Yanlış seç.", ifadeler=[
  {"s": "Kardeş sayısı kesikli veridir.", "d": True},
  {"s": "Boy uzunluğu kesikli veridir.", "d": False},
  {"s": "Vücut sıcaklığı sürekli veridir.", "d": True},
  {"s": "En sevilen renk nicel veridir.", "d": False}],
  aciklama=f"Boy ölçülür: sürekli. Renk sözcüktür: kategorik {S1}.")
a("u3k1", "Nicel Veri", "eslestir", soru="Her veriyi türüyle eşleştir.", ciftler=[
  {"sol": "Göz rengi", "sag": "Kategorik veri"},
  {"sol": "Okuldaki öğrenci sayısı", "sag": "Kesikli veri"},
  {"sol": "Aylık yağış miktarı", "sag": "Sürekli veri"}],
  aciklama=f"Sözcük: kategorik. Sayarak bulunan: kesikli. Ölçerek bulunan: sürekli {S1}.")
a("u3k1", "Sürekli Veri", "secim", soru="Veri türleriyle ilgili aşağıdaki ifadeler verilmiştir.",
  onculler=["Nicel veriler sayısal olarak ifade edilir.", "Sürekli veri iki ölçüm arasında sınırsız değer alabilir.", "Atılan gol sayısı sürekli veridir."],
  kok="Bu ifadelerden hangileri doğrudur?", secenekler=ONC, dogru=1,
  aciklama=f"Goller sayılır; 1,5 gol olmaz: gol sayısı kesiklidir {S1}.")
a("u3k1", "Kategorik Veri", "bosluk", cumleler=[
  {"c": "Sözcükle ifade edilen veriye ___ veri denir.", "cevap": "kategorik"},
  {"c": "İki değer arasında başka değer alamayan veriye ___ veri denir.", "cevap": "kesikli"},
  {"c": "İki ölçüm arasında sınırsız değer alabilen veriye ___ veri denir.", "cevap": "sürekli"}],
  havuz=["nicel", "örneklem"], aciklama=f"Sözcük: kategorik. Arada değer yok: kesikli. Arada değer var: sürekli {S1}.")
a("u3k1", "Araştırmanın 4 Adımı", "secim", soru="İstatistiksel araştırmanın adımları sırasıyla hangisidir?",
  secenekler=["Soru → Toplama → Analiz → Yorum", "Toplama → Soru → Yorum → Analiz", "Analiz → Soru → Toplama → Yorum", "Soru → Analiz → Toplama → Yorum"], dogru=0,
  aciklama=f"Sor, topla, analiz et, yorumla {S1}.")
a("u3k1", "Sürekli Veri", "kisa", soru="Boy uzunluğu, kardeş sayısı, vücut sıcaklığı, ürün fiyatı, okuldaki sınıf sayısı: Bunlardan kaç tanesi sürekli veridir?",
  yanit="3", sayi=True, aciklama=f"Boy, vücut sıcaklığı ve fiyat süreklidir; kardeş ve sınıf sayısı kesiklidir {S1}.")

# --- Konu 2: Araştırma sorusu, evren ve örneklem
a("u3k2", "Örneklem", "dy", ifade="Örneklem, evrenden daha büyük bir gruptur.", dogru=False,
  duzeltme="Örneklem, evreni temsil eden daha küçük bir gruptur.", aciklama=f"Evren en geniş gruptur; örneklem onun içinden seçilir {S2}.")
a("u3k2", "Örneklem Evreni Temsil Etmeli", "secim",
  soru="“Antalya'daki ortaokul öğrencilerinin günlük ekran süreleri nasıl bir eğilim gösterir?” sorusu için hangisi uygun bir örneklemdir?",
  secenekler=["Antalya'nın farklı ilçelerindeki okullardan seçilen öğrenciler", "Bir okulun oyun kulübü üyeleri", "İstanbul'daki bir okulun öğrencileri", "Sadece öğretmenler"], dogru=0,
  aciklama=f"Örneklem evrenin içinde olmalı ve ona benzemeli {S2}.")
a("u3k2", "Evren", "eslestir", soru="Her kavramı anlamıyla eşleştir.", ciftler=[
  {"sol": "Evren", "sag": "Verilerin toplanabileceği en geniş grup"},
  {"sol": "Örneklem", "sag": "Evreni temsil eden küçük grup"},
  {"sol": "Değişebilirlik", "sag": "Verilerin kişiden kişiye farklı olması"},
  {"sol": "Araştırma sorusu", "sag": "Grubun verileriyle cevaplanan soru"}],
  aciklama=f"Evren en geniş grup, örneklem onu temsil eden küçük grup {S2}.")
a("u3k2", "İyi Araştırma Sorusu", "secim", soru="Defne su tüketimini araştırmak için şu soruları yazdı.",
  onculler=["Su içmeyi sever misiniz?", "7/A sınıfı öğrencilerinin günlük su tüketimlerinin eğilimi nasıldır?",
            "7/A'daki kız ve erkek öğrencilerin günlük su tüketimlerinin eğilimi nasıl değişmektedir?"],
  kok="Bunlardan hangileri araştırma sorusu olarak uygundur?", secenekler=ONC, dogru=2,
  aciklama=f"I. sorunun cevabı evet/hayır; ne ölçüleceği belli değil {S2}.")
a("u3k2", "Değişebilirlik", "dytablo", soru="Her ifade için Doğru ya da Yanlış seç.", ifadeler=[
  {"s": "Evrenin tamamından veri toplamak her zaman kolaydır.", "d": False},
  {"s": "Kalp ritmi kişinin yaşına göre değişebilir.", "d": True},
  {"s": "TÜİK bazı araştırmalarda evrenin tamamına hazır verilerle ulaşabilir.", "d": True}],
  aciklama=f"Evrene ulaşmak çoğu zaman zor ve pahalıdır; bu yüzden örneklem seçilir {S2}.")
a("u3k2", "Evren", "kisa", soru="Araştırma sorusuna yönelik verilerin toplanabileceği en geniş gruba ne denir?", yanit="evren",
  aciklama=f"En geniş grup evrendir {S2}.")

# --- Konu 3: Veri toplama ve kişisel veriler
a("u3k3", "Kişisel Veri", "secim", soru="Hangisinin cevabı kişisel veri içermez?",
  secenekler=["Ev adresiniz nedir?", "Banka hesabınızda ne kadar para var?", "Bir haftada kaç gün vardır?", "Boyunuz kaç metredir?"], dogru=2,
  aciklama=f"Adres, banka ve boy bilgisi kişiye aittir {S3}.")
a("u3k3", "İzin ve Gizlilik", "dy", ifade="Anket verileri izin alınmadan başkalarıyla paylaşılabilir.", dogru=False,
  duzeltme="Anket verileri izin alınmadan paylaşılmaz.", aciklama=f"İzinsiz paylaşmak kişisel verilerin gizliliğini ihlal eder {S3}.")
a("u3k3", "Anket Sorusu", "bosluk", cumleler=[
  {"c": "Örneklemdeki her kişiye tek tek sorulan soruya ___ sorusu denir.", "cevap": "anket"},
  {"c": "Hazır verileri resmî kurumlar gibi ___ kaynaklardan alırız.", "cevap": "güvenilir"},
  {"c": "Kişisel verilerin korunmasıyla ilgili temel kanunun kısa adı ___ olarak yazılır.", "cevap": "KVKK"}],
  havuz=["TÜİK", "rastgele"], aciklama=f"Anket sorusu kişiye sorulur; KVKK kişisel verileri korur {S3}.")
a("u3k3", "İzin ve Gizlilik", "secim", soru="Kişisel verileri korumak için aşağıdaki davranışlar verilmiştir.",
  onculler=["Paylaşmadan önce bilgilerin kimlere görüneceğini kontrol etmek", "İzin metnini okumadan “Tüm izinleri kabul ediyorum.” demek",
            "Sosyal medya hesabını herkese açık değil, gizli yapmak"],
  kok="Bunlardan hangileri doğru davranıştır?", secenekler=["Yalnız I", "I ve III", "II ve III", "I, II ve III"], dogru=1,
  aciklama=f"İzin metni okunmadan onaylanmamalıdır {S3}.")
a("u3k3", "Veri Toplama Planı", "eslestir", soru="Veri toplama planındaki her soruyu uygun cevapla eşleştir.", ciftler=[
  {"sol": "Nerede?", "sag": "Sınıfta"},
  {"sol": "Ne zaman?", "sag": "Salı günü ilk derste"},
  {"sol": "Nasıl?", "sag": "Mezurayla ölçerek"},
  {"sol": "Nasıl kaydedilecek?", "sag": "Tabloya yazarak"}],
  aciklama=f"Plan: nerede, ne zaman, nasıl toplanacak ve nasıl kaydedilecek {S3}.")
a("u3k3", "Güvenilir Kaynak", "secim", soru="Mustafa Bey orman yangını verilerine güvenilir bir adresten ulaşmak istiyor. Hangisi en uygundur?",
  secenekler=["Uzantısı gov.tr olan resmî kurum sitesi", "Kaynağı yazmayan bir paylaşım", "Bir forumdaki yorum", "Bir arkadaşının tahmini"], dogru=0,
  aciklama=f"gov.tr, edu.tr, org.tr uzantılı resmî adresler güvenilirdir {S3}.")
a("u3k3", "KVKK", "dy", ifade="KVKK'nin amacı kişilerin özel hayatının gizliliğini korumaktır.", dogru=True,
  aciklama=f"KVKK özel hayatın gizliliğini, temel hak ve özgürlükleri korur {S3}.")

# --- Konu 4: Nokta ve çizgi grafiği
a("u3k4", "Çizgi Grafiği", "secim", soru="Grafiğe göre gram altının fiyatı en yüksek hangi gündedir?", svg=altin_svg(),
  secenekler=["27 Ekim", "31 Ekim", "10 Kasım", "11 Kasım"], dogru=3, aciklama=f"En üstteki nokta 11.11: 5 624 TL {S4}.")
a("u3k4", "Artış, Azalış, Sabit", "kisa", soru="Fidan grafiğine göre fidan 4. haftadan 5. haftaya kaç cm uzamıştır?", svg=fidan_svg(),
  yanit="3", sayi=True, aciklama="21 − 18 = 3 cm.")
a("u3k4", "Nokta Grafiği", "kisa", soru="Nokta grafiğine göre kardeşi olmayan kaç öğrenci vardır?", svg=kardes_svg(),
  yanit="2", sayi=True, aciklama="Kardeşi olmayan: 0'ın üstündeki noktalar, 2 öğrenci.")
a("u3k4", "Hangi Grafik?", "eslestir", soru="Her veri setini en uygun grafikle eşleştir.", ciftler=[
  {"sol": "Bir sınıftaki öğrencilerin kardeş sayıları", "sag": "Nokta grafiği"},
  {"sol": "Bir ürünün 10 günlük fiyatı", "sag": "Çizgi grafiği"},
  {"sol": "Sınıfta en sevilen meyveler", "sag": "Sütun grafiği"}],
  aciklama=f"Tekrar eden sayılar: nokta. Zamanla değişim: çizgi. Kategoriler: sütun {S4}.")
a("u3k4", "Nokta Grafiği Ne Zaman Uymaz?", "dytablo", soru="Her ifade için Doğru ya da Yanlış seç.", ifadeler=[
  {"s": "Nokta grafiğinde aynı değerler üst üste yığılır.", "d": True},
  {"s": "Günlük altın fiyatları nokta grafiğiyle en iyi gösterilir.", "d": False},
  {"s": "Çizgi grafiği zamana bağlı değişimi gösterir.", "d": True},
  {"s": "Sütun grafiğinde değişimi izlemek çizgi grafiğinden daha kolaydır.", "d": False}],
  aciklama=f"Sürekli veride değerler hep farklıdır; değişimi çizgi grafiği daha açık gösterir {S4}.")
a("u3k4", "Artış, Azalış, Sabit", "secim", soru="Altın grafiğinde fiyat hangi iki gün arasında azalmıştır?", svg=altin_svg(),
  onculler=["27 Ekim → 28 Ekim", "31 Ekim → 5 Kasım", "10 Kasım → 11 Kasım"],
  kok="Bunlardan hangilerinde fiyat azalmıştır?", secenekler=["Yalnız I", "I ve II", "II ve III", "I, II ve III"], dogru=1,
  aciklama="10 Kasım'dan 11 Kasım'a çizgi yukarı çıkıyor: artış.")
a("u3k4", "Çizgi Grafiği", "bosluk", cumleler=[
  {"c": "Çizgi grafiğinde yatay eksende genellikle ___ vardır.", "cevap": "zaman"},
  {"c": "Çizgi aşağı iniyorsa değer ___ demektir.", "cevap": "azalmış"},
  {"c": "Aynı değerlerin üst üste yığıldığı grafiğe ___ grafiği denir.", "cevap": "nokta"}],
  havuz=["artmış", "sütun"], aciklama=f"Yatayda zaman; aşağı iniş azalış; yığılma nokta grafiğinde {S4}.")

# --- Konu 5: Temsil değeri ve tahmin
a("u3k5", "Eğilim", "secim", soru="Kar grafiğine göre ortalama kar örtülü gün sayısı ile ilgili hangisi doğrudur?", svg=kar_svg(),
  secenekler=["Her dönem artmıştır.", "Genel eğilim azalıştır.", "Hiç değişmemiştir.", "En düşük değer 1970–1980'dedir."], dogru=1,
  aciklama=f"30,0'dan 22,4'e iniyor: genel eğilim azalış {S5}.")
a("u3k5", "Temsil Değeri", "kisa", soru="Esra Bayrak'ın atlayışları: 5,17 · 5,27 · 5,38 · 5,37 · 5,36 m. Bu verilerin aritmetik ortalaması kaç metredir?",
  yanit="5,31", sayi=True, aciklama=f"Toplam 26,55; 26,55 ÷ 5 = 5,31 m {S5}.")
a("u3k5", "Temsil Değeri Listede Olmayabilir", "dy", ifade="Bir veri setini temsil eden değer, mutlaka veri setindeki sayılardan biri olmalıdır.", dogru=False,
  duzeltme="Temsil değeri veri setinde yer almayabilir.", aciklama=f"Kar verisinin ortalaması 27,8 tabloda yoktur ama veriyi temsil eder {S5}.")
a("u3k5", "Veriyle İddiayı Sınama", "secim", soru="Mühendis “1 litre benzinle en az 13 km” diyor. 10 sürüşte ortalama 11,97 km, ortanca 12,1 km, tepe değer 10,5 km bulundu.",
  onculler=["Ortalama iddiayı desteklemiyor.", "Ortanca iddiayı desteklemiyor.", "Tepe değer iddiayı destekliyor."],
  kok="Bu ifadelerden hangileri doğrudur?", secenekler=ONC, dogru=1, aciklama=f"Üç ölçü de 13'ten küçüktür; tepe değer de desteklemez {S5}.")
a("u3k5", "Referans Değeri", "secim", soru="Grafiğe göre 6 aylık bir bebeğin baş çevresi 44,5 cm. Bu bebek hangi persentil değerindedir?", svg=persentil_svg(),
  secenekler=["P25", "P50", "P75", "P75'in çok üstünde"], dogru=2, aciklama=f"6 ayda P75 = 44,5 cm {S5}.")
a("u3k5", "Veri Ötesi: Tahmin", "eslestir", soru="Her kavramı anlamıyla eşleştir.", ciftler=[
  {"sol": "Eğilim", "sag": "Çizginin genel yönü"},
  {"sol": "Tahmin", "sag": "Eğilime bakarak gelecek hakkında yorum"},
  {"sol": "Referans değeri", "sag": "Karşılaştırma için önceden belirlenmiş değer"},
  {"sol": "Temsil değeri", "sag": "Veri setini özetleyen tek sayı"}],
  aciklama=f"Eğilim genel yön, tahmin veri ötesi yorum {S5}.")
a("u3k5", "Temsil Değeri", "kisa", soru="Kar örtülü gün sayıları: 30,0 · 29,6 · 30,0 · 27,1 · 22,4. Bu verilerin ortancası kaçtır?",
  yanit="29,6", sayi=True, aciklama=f"Sıralı: 22,4 · 27,1 · 29,6 · 30,0 · 30,0. Ortadaki 29,6 {S5}.")

H.yaz()
