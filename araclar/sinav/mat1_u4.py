# -*- coding: utf-8 -*-
"""Matematik 4. Tema (Dönüşüm) Sınav Provası havuzu: python3 araclar/sinav/mat1_u4.py"""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from ortak import Havuz, ONC
KOK = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")); sys.path.insert(0, KOK)
from gen_mat1 import gs_tek_nokta, gs_nokta_aday, gs_gizli, gs_kaymis, gs_orta_dikme, gs_aciortay
H = Havuz("mat1", 4, "m4")
a = H.add
S1, S2, S3, S4 = "(s. 202–205, 210)", "(s. 205–209)", "(s. 211–213)", "(s. 213–215)"

# --- Konu 1: Yansıma dönüşümü
a("u4k1", "Eşit Uzaklık", "kisa", soru="Görselde A noktasının görüntüsü A′, simetri doğrusunun kaç kare sağındadır?", yanit="4", sayi=True,
  svg=gs_tek_nokta(4), aciklama=f"A doğruya 4 kare uzakta; görüntüsü de öbür yanda 4 kare uzakta {S1}.")
a("u4k1", "Dik Ortalar", "secim", soru="Görselde A noktasının görüntüsü hangi numaralı noktadır?", svg=gs_nokta_aday("d"),
  secenekler=["1", "2", "3", "Hiçbiri"], dogru=0, aciklama=f"Görüntü doğruya eşit uzak ve A ile aynı hizada olmalı: 1 {S1}.")
a("u4k1", "Şekil ve Görüntü Eştir", "dytablo", soru="Her ifade için Doğru ya da Yanlış seç.", ifadeler=[
  {"s": "Bir şekil ile görüntüsü eştir.", "d": True},
  {"s": "Görüntü, şeklin iki katı büyüklüğündedir.", "d": False},
  {"s": "Nokta ile görüntüsü simetri doğrusuna eşit uzaklıktadır.", "d": True},
  {"s": "Yansımada şeklin yönü hiç değişmez.", "d": False}],
  aciklama=f"Görüntü şekle eştir ama yönü ters döner {S1}.")
a("u4k1", "Yansıma Dönüşümü", "bosluk", cumleler=[
  {"c": "Bir noktanın bir doğruya göre simetrisine, yansıma dönüşümü altındaki ___ denir.", "cevap": "görüntüsü"},
  {"c": "Simetri doğrusu, nokta ile görüntüsünü birleştiren parçayı ___ ortalar.", "cevap": "dik"},
  {"c": "Çizdiğimiz görüntüyü simetri ___ ile kontrol edebiliriz.", "cevap": "aynası"}],
  havuz=["paralel", "köşesi"], aciklama=f"Görüntü, dik ortalama ve simetri aynası {S1}.")
a("u4k1", "Şekil ve Görüntü Eştir", "secim", soru="Yansıma dönüşümüyle ilgili aşağıdaki ifadeler verilmiştir.",
  onculler=["Bir şekil ile görüntüsü eştir.", "Görüntü her zaman şekilden büyüktür.", "Yansımada şeklin yönü değişmez."],
  kok="Bu ifadelerden hangileri doğrudur?", secenekler=ONC, dogru=0,
  aciklama=f"Görüntü şekle eştir, büyümez; yönü ters döner {S1}.")
a("u4k1", "Köşe Köşe Yansıt", "kisa", soru="Bir dörtgenin görüntüsünü çizmek için en az kaç köşenin görüntüsünü bulmalıyız?", yanit="4", sayi=True,
  aciklama=f"Dörtgenin 4 köşesi var; hepsinin görüntüsü bulunup birleştirilir {S1}.")
a("u4k1", "Simetri Aynası ve Asetat", "dy", ifade="Asetat kâğıdıyla kontrol yaparken kâğıt simetri doğrusunun öbür yanına çevrilir.", dogru=True,
  aciklama=f"Şekil asetata çizilir, kâğıt doğrunun öbür yanına çevrilir {S1}.")

# --- Konu 2: Simetri doğrularını bulma
a("u4k2", "Birden Çok Simetri Doğrusu", "eslestir", soru="Her şekli simetri doğrusu sayısıyla eşleştir.", ciftler=[
  {"sol": "Kare", "sag": "4 simetri doğrusu"},
  {"sol": "Dikdörtgen", "sag": "2 simetri doğrusu"},
  {"sol": "Eşkenar üçgen", "sag": "3 simetri doğrusu"},
  {"sol": "Paralelkenar", "sag": "Simetri doğrusu yok"}],
  aciklama=f"Kare 4, dikdörtgen 2, eşkenar üçgen 3; paralelkenarın yok {S2}.")
a("u4k2", "Birden Çok Simetri Doğrusu", "kisa", soru="Düzgün altıgenin kaç simetri doğrusu vardır?", yanit="6", sayi=True,
  aciklama="Düzgün çokgende simetri doğrusu sayısı kenar sayısına eşittir: 6.")
a("u4k2", "Simetri Doğrusu Olmayan Şekiller", "secim", soru="Aşağıdaki şekillerden hangisinin simetri doğrusu yoktur?",
  secenekler=["Çeşitkenar üçgen", "İkizkenar üçgen", "Kare", "Yarım daire"], dogru=0,
  aciklama=f"Çeşitkenar üçgenin hiçbir kenarı eş değil; simetrik değildir {S2}.")
a("u4k2", "Gizli Simetri Doğrusu", "secim", soru="Görseldeki iki eş üçgen için hangisi doğrudur?", svg=gs_gizli(3),
  secenekler=["Bir doğruya göre simetriktir.", "Renkleri farklı olduğu için simetrik değildir.", "Aralarında boşluk olduğu için simetrik değildir.", "Eş değildir."], dogru=0,
  aciklama=f"Parçalar paralel ve orta noktaları tek doğruda: simetriktir {S2}.")
a("u4k2", "Gizli Simetri Doğrusu", "secim", soru="Görseldeki eş üçgenler bir doğruya göre simetrik midir?", svg=gs_kaymis(),
  secenekler=["Hayır; orta noktalar aynı doğru üzerinde değil.", "Evet; parçalar paralel.", "Evet; üçgenler eş.", "Evet; yönleri aynı."], dogru=0,
  aciklama=f"Üçgen yalnızca kaydırılmış; orta noktalar tek doğruda değil {S2}.")
a("u4k2", "Kenara Göre Yansıtma", "secim", soru="İkizkenar dik üçgen uzun kenarına göre yansıtılırsa üçgen ile görüntüsü hangi şekli oluşturur?",
  secenekler=["Kare", "Dikdörtgen", "Eşkenar üçgen", "Paralelkenar"], dogru=0,
  aciklama=f"Dört kenar eş, dört açı dik olur: kare {S2}.")
a("u4k2", "Simetri Doğrusu Olmayan Şekiller", "dy", ifade="Paralelkenarı köşegeninden kesince iki eş parça oluştuğu için köşegen bir simetri doğrusudur.", dogru=False,
  duzeltme="İki parça eş olur ama katlayınca üst üste gelmez; köşegen simetri doğrusu değildir.",
  aciklama=f"Simetri için parçalar katlayınca çakışmalı {S2}.")
a("u4k2", "Hayatta Simetri", "dy", ifade="Kelebek kanatları ve kar taneleri simetrik örüntülere sahiptir.", dogru=True,
  aciklama=f"Doğada kelebek, kar tanesi ve çiçeklerde simetri vardır {S2}.")

# --- Konu 3: Orta dikme
a("u4k3", "Orta Dikme İnşası", "secim", soru="Görseldeki orta dikme inşasında sıradaki adım hangisidir?", svg=gs_orta_dikme(3),
  secenekler=["K ile L'yi ölçüsüz cetvelle birleştirmek", "A ile K'yi birleştirmek", "Pergeli küçültüp yeni yay çizmek", "AB'yi cetvelle ölçmek"], dogru=0,
  aciklama=f"Yay, yay, kesişim, birleştir: sırada K ile L var {S3}.")
a("u4k3", "Orta Dikme", "kisa", soru="AB = 18 cm. Orta dikme AB'yi iki parçaya ayırıyor. Parçalardan biri kaç cm?", yanit="9", sayi=True,
  aciklama=f"Orta dikme iki eş parça oluşturur: 18 ÷ 2 = 9 cm {S3}.")
a("u4k3", "Eş Çemberler", "secim", soru="AB = 8 cm. Orta dikme inşasında pergel açıklığı hangi uzunluktan uzun olmalıdır?",
  secenekler=["4 cm", "8 cm", "2 cm", "16 cm"], dogru=0,
  aciklama=f"Açıklık AB'nin yarısından (4 cm) uzun olmalı {S3}.")
a("u4k3", "Orta Dikme", "bosluk", cumleler=[
  {"c": "Bir doğru parçasını dik kesen ve iki eş parçaya ayıran doğruya ___ denir.", "cevap": "orta dikme"},
  {"c": "İnşada yalnızca pergel ve ___ cetvel kullanılır.", "cevap": "ölçüsüz"},
  {"c": "Yayların kesiştiği nokta, doğru parçasının iki ucuna ___ uzaklıktadır.", "cevap": "eşit"}],
  havuz=["açıortay", "farklı"], aciklama=f"Orta dikme, ölçüsüz cetvel ve eşit uzaklık {S3}.")
a("u4k3", "Simetri Doğrusu = Orta Dikme", "dytablo", soru="Her ifade için Doğru ya da Yanlış seç.", ifadeler=[
  {"s": "Orta dikme doğru parçasını 90°'lik açıyla keser.", "d": True},
  {"s": "A ve B merkezli yaylar farklı açıklıklarla çizilir.", "d": False},
  {"s": "Bir doğru parçasının simetri doğrusu, orta dikmesidir.", "d": True},
  {"s": "İnşada cetvelle uzunluk ölçülür.", "d": False}],
  aciklama=f"Yaylar eş çizilir; inşada ölçü alınmaz {S3}.")
a("u4k3", "İki Uca Eşit Uzak", "kisa", soru="Orta dikme inşasında pergel 7 cm açıldı. AKBL dörtgeninin çevresi kaç cm?", yanit="28", sayi=True,
  aciklama=f"Dört kenarın hepsi 7 cm: 4 · 7 = 28 cm {S3}.")
a("u4k3", "Orta Dikme", "secim", soru="Orta dikmeyle ilgili aşağıdaki ifadeler verilmiştir.",
  onculler=["Doğru parçasını dik keser.", "Doğru parçasını iki eş parçaya ayırır.", "Üzerindeki her nokta doğru parçasının iki ucuna eşit uzaklıktadır."],
  kok="Bu ifadelerden hangileri doğrudur?", secenekler=ONC, dogru=3,
  aciklama=f"Üç ifade de orta dikmenin özelliğidir {S3}.")

# --- Konu 4: Açıortay
a("u4k4", "İki Eş Açı", "kisa", soru="130°'lik bir açının açıortayı oluşturduğu açılardan biri kaç derecedir?", yanit="65", sayi=True,
  aciklama=f"Açıortay açıyı iki eş açıya ayırır: 130 ÷ 2 = 65° {S4}.")
a("u4k4", "İki Eş Açı", "kisa", soru="Açıortayın oluşturduğu açılardan biri 48°. Bütün açı kaç derecedir?", yanit="96", sayi=True,
  aciklama=f"İki eş açı: 48 + 48 = 96° {S4}.")
a("u4k4", "Açıortay İnşası", "secim", soru="Görseldeki açıortay inşasında sıradaki adım hangisidir?", svg=gs_aciortay(3),
  secenekler=["A ile E'yi birleştirmek", "K ile L'yi birleştirmek", "K ile E'yi birleştirmek", "Köşe merkezli yeni bir yay çizmek"], dogru=0,
  aciklama=f"E bulundu; köşe A ile E birleştirilir {S4}.")
a("u4k4", "Orta Dikme mi, Açıortay mı?", "secim", soru="Simetri doğrularıyla ilgili aşağıdaki ifadeler verilmiştir.",
  onculler=["Bir açının simetri doğrusu açıortayıdır.", "Bir doğru parçasının simetri doğrusu orta dikmesidir.", "Açıortay açıyı iki farklı açıya ayırır."],
  kok="Bu ifadelerden hangileri doğrudur?", secenekler=ONC, dogru=1,
  aciklama=f"Açıortay açıyı iki eş açıya ayırır; III yanlış {S4}.")
a("u4k4", "Orta Dikme mi, Açıortay mı?", "eslestir", soru="Her şekli simetri doğrusuyla eşleştir.", ciftler=[
  {"sol": "Doğru parçası", "sag": "Orta dikme"},
  {"sol": "Açı", "sag": "Açıortay"},
  {"sol": "Daire dilimi", "sag": "İki yarıçapın arasındaki açının açıortayı"}],
  aciklama=f"Parça → orta dikme, açı → açıortay {S4}.")
a("u4k4", "Köşeden Eşit Uzak İki Nokta", "dy", ifade="Açıortay inşasının ilk adımında pergelin sivri ucu açının köşesine konur.", dogru=True,
  aciklama=f"Köşe merkezli yay kolları K ve L'de keser {S4}.")
a("u4k4", "Açıortay İnşası", "secim", soru="K ve L merkezli eş yaylar çizmek, hangi parçanın orta dikmesini çizmek demektir?",
  secenekler=["KL", "AK", "AL", "AE"], dogru=0,
  aciklama=f"K ve L merkezli eş yaylar KL'nin orta dikmesini verir; bu da açıortaydır {S4}.")

H.yaz()
