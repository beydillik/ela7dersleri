import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from ortak import Havuz, ONC
H = Havuz("fen1", 2, "f2"); a = H.add
P1, P2, P3, P4 = "(s. 59–63)", "(s. 64–67)", "(s. 68–70)", "(s. 71–80)"

# --- Konu 1: Fiziksel Anlamda İş
a("u2k1", "Kuvvet Var, Hareket Yok", "secim", soru="Aşağıdakilerin hangisinde fiziksel anlamda iş yapılmaz?",
  secenekler=["Yerdeki kutuyu masanın üstüne kaldırmak", "Alışveriş arabasını ileri itmek", "Okulun duvarını var gücüyle itmek", "Kovayı kuyudan yukarı çekmek"], dogru=2,
  aciklama=f"Duvar yerinden oynamaz. Kuvvet var ama hareket yoksa iş yapılmaz {P1}.")
a("u2k1", "Fiziksel Anlamda İş", "secim", soru="Fiziksel anlamda iş yapılmasıyla ilgili aşağıdaki ifadeler verilmiştir.",
  onculler=["Cisme kuvvet uygulanmalıdır.", "Cisim, kuvvetin doğrultusunda yer değiştirmelidir.", "Bilgisayar başında ödev yapmak fiziksel anlamda iştir."],
  kok="Bu ifadelerden hangileri doğrudur?", secenekler=ONC, dogru=1,
  aciklama=f"İş için kuvvet ve kuvvet yönünde hareket gerekir. Ödev yapmak günlük dildeki iştir {P1}.")
a("u2k1", "Kuvvet ile Hareket Farklı Doğrultuda", "dy", ifade="Çantasını sırtında taşıyarak düz yolda yürüyen öğrenci, çantaya fiziksel anlamda iş yapar.", dogru=False,
  duzeltme="Kuvvet yukarı, hareket ileri doğrudur. Doğrultular aynı olmadığı için iş yapılmaz.",
  aciklama=f"Çantaya uygulanan kuvvet yukarı, hareket ileri. Doğrultular farklıysa iş yok {P1}.")
a("u2k1", "Joule", "kisa", soru="Kuvvet newton, yol metre alınırsa işin birimi nedir?", yanit="joule", kabul=["jul", "J"],
  aciklama=f"İşin birimi joule'dür, J ile gösterilir {P1}.")
a("u2k1", "Kuvvet Uygulamak", "kisa", soru="Kuvvetin birimi nedir?", yanit="newton", kabul=["N", "nivtın"],
  aciklama=f"Kuvvetin birimi newtondur, N ile gösterilir {P1}.")
a("u2k1", "İşin Büyüklüğü", "secim", soru="Ali aynı kutuyu düz zeminde önce 2 m, sonra 6 m itiyor. Kuvvet ikisinde de aynıdır. Buna göre hangisi doğrudur?",
  secenekler=["İki durumda da iş eşittir.", "İkinci durumda daha çok iş yapılır.", "Birinci durumda daha çok iş yapılır.", "İki durumda da iş yapılmaz."], dogru=1,
  aciklama=f"Kuvvet aynıysa daha uzun yol, daha çok iş demektir {P1}.")
a("u2k1", "Fiziksel Anlamda İş", "dytablo", soru="Her durum için fiziksel anlamda iş yapılıyorsa D, yapılmıyorsa Y seç.", ifadeler=[
  {"s": "Halteri başının üstünde hareketsiz tutan sporcu", "d": False},
  {"s": "Kitap kolisini merdivenden yukarı çıkaran Ahmet", "d": True},
  {"s": "Masayı ittiği yönde kaydıran öğrenci", "d": True},
  {"s": "Yerinden oynamayan dolabı iten çocuk", "d": False}],
  aciklama=f"Hareket yoksa iş de yoktur. Kuvvet yönünde hareket varsa iş yapılır {P1}.")

# --- Konu 2: Enerji ve Kinetik Enerji
a("u2k2", "Enerji", "kisa", soru="İş yapabilme yeteneğine ne denir?", yanit="enerji",
  aciklama=f"İş yapabilme yeteneğine enerji denir {P2}.")
a("u2k2", "Kinetik Enerji", "secim", soru="Aşağıdakilerden hangisi kinetik enerjiye sahip değildir?",
  secenekler=["Parkta bisiklet süren çocuk", "Denizde ilerleyen tekne", "Rafta duran kitap", "Yuvarlanan top"], dogru=2,
  aciklama=f"Kinetik enerji hareketten gelir. Rafta duran kitap hareket etmiyor {P2}.")
a("u2k2", "Kütle ve Kinetik Enerji", "secim", soru="Aynı hızla giden bir kamyon ile bir otomobil için hangisi doğrudur?",
  secenekler=["Otomobilin kinetik enerjisi daha fazladır.", "İkisinin kinetik enerjisi eşittir.", "İkisinin de kinetik enerjisi yoktur.", "Kamyonun kinetik enerjisi daha fazladır."], dogru=3,
  aciklama=f"Hızlar aynıysa kütlesi büyük olanın kinetik enerjisi fazladır {P2}.")
a("u2k2", "Hız ve Kinetik Enerji", "dy", ifade="Kütleleri aynı iki koşucudan daha hızlı koşanın kinetik enerjisi daha fazladır.", dogru=True,
  aciklama=f"Kütle aynıysa hızı fazla olanın kinetik enerjisi fazladır {P2}.")
a("u2k2", "Doğru Orantı", "secim", soru="Kinetik enerjiyle ilgili aşağıdaki ifadeler verilmiştir.",
  onculler=["Kinetik enerji yalnızca hıza bağlıdır.", "Kütlesi ve hızı artan cismin kinetik enerjisi artar.", "Yavaşlayan bisikletin kinetik enerjisi azalır."],
  kok="Bu ifadelerden hangileri doğrudur?", secenekler=ONC, dogru=2,
  aciklama=f"Kinetik enerji yalnız hıza değil, kütleye de bağlıdır {P2}.")
a("u2k2", "Enerjinin Farklı Şekilleri", "bosluk", havuz=["newton", "kuvvet"], cumleler=[
  {"c": "Hareket eden cismin enerjisine ___ enerji denir.", "cevap": "kinetik"},
  {"c": "Enerjinin birimi ___ olarak alınır.", "cevap": "joule"},
  {"c": "Lambanın etrafı aydınlatması ___ enerjisine örnektir.", "cevap": "ışık"}],
  aciklama=f"Hareket enerjisi kinetiktir. Enerji, iş gibi joule ile ölçülür {P2}.")
a("u2k2", "Hız ve Kinetik Enerji", "secim", soru="Kütleleri aynı iki özdeş araba aynı yolda fren yapıyor. Hangisi daha uzun mesafede durur?",
  secenekler=["Daha hızlı giden araba", "Daha yavaş giden araba", "İkisi aynı mesafede durur", "Duran araba"], dogru=0,
  aciklama=f"Hızlı gidenin kinetik enerjisi fazladır. Bu yüzden daha geç durur {P2}.")

# --- Konu 3: Potansiyel Enerji
a("u2k3", "Çekim Potansiyel Enerjisi", "secim", soru="Aynı ağırlıktaki iki kitaptan biri alt rafta, diğeri üst rafta duruyor. Hangisi doğrudur?",
  secenekler=["Alt raftakinin çekim potansiyel enerjisi daha fazladır.", "Üst raftakinin çekim potansiyel enerjisi daha fazladır.", "İkisinin çekim potansiyel enerjisi eşittir.", "İkisinin de enerjisi yoktur."], dogru=1,
  aciklama=f"Ağırlıklar aynıysa daha yüksekteki cismin enerjisi fazladır {P3}.")
a("u2k3", "Esnek Cisim", "secim", soru="Aşağıdakilerden hangisi esnek bir cisim değildir?",
  secenekler=["Paket lastiği", "Sünger", "Sarmal yay", "Cam bardak"], dogru=3,
  aciklama=f"Esnek cisim, kuvvet kalkınca eski hâline döner. Cam bardak dönmez, kırılır {P3}.")
a("u2k3", "Esneklik Potansiyel Enerjisi", "dy", ifade="Sıkıştırılan sarmal yay esneklik potansiyel enerjisi depolar.", dogru=True,
  aciklama=f"Yay gerilince ya da sıkışınca enerji depolar {P3}.")
a("u2k3", "Potansiyel Enerji", "bosluk", havuz=["kinetik", "ışık"], cumleler=[
  {"c": "Ağaç dalında duran elma ___ potansiyel enerjisine sahiptir.", "cevap": "çekim"},
  {"c": "Gerilmiş paket lastiği ___ potansiyel enerjisine sahiptir.", "cevap": "esneklik"},
  {"c": "Çekim potansiyel enerjisi ağırlığa ve ___ bağlıdır.", "cevap": "yüksekliğe"}],
  aciklama=f"Potansiyel enerjinin iki çeşidi var: çekim ve esneklik {P3}.")
a("u2k3", "Ağırlık ve Çekim Potansiyel Enerjisi", "secim", soru="Aynı yükseklikten havuza önce hafif, sonra ağır bir çocuk atlıyor. Hangisi daha çok su sıçratır?",
  secenekler=["Hafif çocuk", "Ağır çocuk", "İkisi aynı", "Hiçbiri su sıçratmaz"], dogru=1,
  aciklama=f"Aynı yükseklikte ağır olanın çekim potansiyel enerjisi fazladır {P3}.")
a("u2k3", "Kinetik ve Potansiyel Enerji", "eslestir", soru="Durumları sahip oldukları enerjiyle eşleştir.", ciftler=[
  {"sol": "Yuvarlanan top", "sag": "Kinetik enerji"},
  {"sol": "Dalda duran elma", "sag": "Çekim potansiyel enerjisi"},
  {"sol": "Gerilmiş paket lastiği", "sag": "Esneklik potansiyel enerjisi"}],
  aciklama=f"Hareket kinetik, yükseklik çekim, esneme esneklik enerjisidir {P3}.")
a("u2k3", "Esneklik Potansiyel Enerjisi", "secim", soru="Bir paket lastiğinin depoladığı enerjiyi artırmak için ne yapılmalıdır?",
  secenekler=["Lastik daha çok gerilmeli", "Lastik yere bırakılmalı", "Lastik suya batırılmalı", "Lastik hiç gerilmemeli"], dogru=0,
  aciklama=f"Esnek cisim ne kadar çok gerilirse o kadar çok enerji depolar {P3}.")

# --- Konu 4: Enerji Dönüşümleri ve Korunum
a("u2k4", "Düşen Top", "secim", soru="Yukarıdan serbest bırakılan top düşerken enerjisi nasıl değişir?",
  secenekler=["Potansiyel enerji artar, kinetik enerji azalır.", "İkisi de artar.", "Potansiyel enerji azalır, kinetik enerji artar.", "İkisi de değişmez."], dogru=2,
  aciklama=f"Top düşerken yükseklik azalır, hız artar. PE kinetiğe dönüşür {P4}.")
a("u2k4", "Sarkaç ve Salıncak", "dytablo", soru="Salıncakla ilgili ifadeler için D ya da Y seç.", ifadeler=[
  {"s": "En yüksek noktada potansiyel enerji en fazladır.", "d": True},
  {"s": "En alt noktada kinetik enerji en fazladır.", "d": True},
  {"s": "Yukarı çıkarken salıncak hızlanır.", "d": False},
  {"s": "Aşağı inerken potansiyel enerji kinetik enerjiye dönüşür.", "d": True}],
  aciklama=f"Tepede PE, dipte KE en fazladır. Yukarı çıkarken salıncak yavaşlar {P4}.")
a("u2k4", "Enerjinin Korunumu", "secim", soru="Enerjinin korunumu kanunu aşağıdakilerden hangisini anlatır?",
  secenekler=["Enerji kullanıldıkça yok olur.", "Enerji yoktan var olabilir.", "Enerji yalnızca kinetik olabilir.", "Enerji yok olmaz, başka bir türe dönüşür."], dogru=3,
  aciklama=f"Enerji yoktan var olmaz, yok da olmaz. Yalnızca tür değiştirir {P4}.")
a("u2k4", "Sürtünme ve Enerji", "secim", soru="Düz yolda itilen kutu bir süre sonra duruyor. Kutunun kinetik enerjisine ne olmuştur?",
  secenekler=["Yok olmuştur.", "Sürtünmeyle ısı ve ses enerjisine dönüşmüştür.", "Esneklik enerjisine dönüşmüştür.", "Artmıştır."], dogru=1,
  aciklama=f"Sürtünme kinetik enerjiyi ısı ve sese dönüştürür. Enerji kaybolmaz {P4}.")
a("u2k4", "Sıkışan Yay", "bosluk", havuz=["ışık", "çekim"], cumleler=[
  {"c": "Sıkıştırılan yay ___ potansiyel enerjisi depolar.", "cevap": "esneklik"},
  {"c": "Yay serbest kalınca bu enerji arabanın ___ enerjisine dönüşür.", "cevap": "kinetik"},
  {"c": "Yay ne kadar çok sıkışırsa o kadar ___ enerji depolar.", "cevap": "çok"}],
  aciklama=f"Sıkışan yayın enerjisi, bırakılınca hareket enerjisine dönüşür {P4}.")
a("u2k4", "Enerji Dönüşümü", "dy", ifade="Pistte yukarı çıkan topun kinetik enerjisi artar.", dogru=False,
  duzeltme="Yukarı çıkan topun kinetik enerjisi azalır, potansiyel enerjisi artar.",
  aciklama=f"Yukarı çıkarken top yavaşlar. KE azalır, PE artar {P4}.")
a("u2k4", "Eğik Düzlem", "secim", soru="Eğik düzlemin tepesinden bırakılan oyuncak arabanın kinetik enerjisi nerede en fazladır?",
  secenekler=["En üst noktada", "Orta noktada", "En alt noktada", "Her yerde eşittir"], dogru=2,
  aciklama=f"Araba indikçe hızlanır. En altta kinetik enerjisi en fazladır {P4}.")
H.yaz()
