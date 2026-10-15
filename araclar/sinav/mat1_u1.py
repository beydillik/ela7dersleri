import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from ortak import Havuz, ONC
H = Havuz("mat1", 1, "m1"); a = H.add
S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12 = ("(s. 15–24)", "(s. 25–34)", "(s. 35–40)", "(s. 41–49)", "(s. 50–61)", "(s. 62–72)",
  "(s. 73–81)", "(s. 82–87)", "(s. 88–95)", "(s. 96–101)", "(s. 102–107)", "(s. 108–116)")

# --- Konu 1: Tam sayılar ve sayı doğrusu
a("u1k1", "Negatif Tam Sayılar", "kisa", soru="Bir denizaltı deniz seviyesinin 35 metre altında. Konumunu tam sayıyla yaz.", yanit="-35", sayi=True,
  aciklama=f"Deniz seviyesi 0'dır. Altı eksidir: −35 {S1}.")
a("u1k1", "Kelimeden Sayıya", "secim", soru="Aşağıdakilerden hangisi negatif bir tam sayıyla anlatılır?",
  secenekler=["50 TL kâr", "Deniz seviyesinin 20 m üstü", "200 TL borç", "Binanın 3. katı"], dogru=2,
  aciklama=f"Borç, gider, zarar, altı → eksi {S1}.")
a("u1k1", "Tam Sayılar Ailesi", "secim", soru="Sıfır ile ilgili aşağıdaki ifadeler verilmiştir.",
  onculler=["Sıfır pozitif bir tam sayıdır.", "Sıfır negatif bir tam sayıdır.", "Sıfırın işareti yoktur."],
  kok="Bu ifadelerden hangileri doğrudur?", secenekler=["Yalnız I", "Yalnız II", "Yalnız III", "I ve II"], dogru=2,
  aciklama=f"Sıfır ne pozitif ne negatiftir; işareti yoktur {S1}.")
a("u1k1", "İki Sayı Arasındaki Uzaklık", "kisa", soru="Bir binada otopark −2. katta, Elif +5. katta oturuyor. Otoparktan Elif'in katına kaç kat çıkılır?", yanit="7", sayi=True,
  aciklama=f"−2'den 0'a 2 kat, 0'dan 5'e 5 kat: 2 + 5 = 7 {S1}.")
a("u1k1", "Sayı Doğrusu", "dytablo", soru="Her ifade için Doğru ya da Yanlış seç.", ifadeler=[
  {"s": "Negatif sayılar sayı doğrusunda 0'ın solundadır.", "d": True},
  {"s": "+4 ile 4 aynı sayıdır.", "d": True},
  {"s": "Sayı doğrusunda sola gittikçe sayılar büyür.", "d": False}],
  aciklama=f"Sol eksi, sağ artı. Sağa gittikçe sayılar büyür {S1}.")

# --- Konu 2: Rasyonel sayılar
a("u1k2", "Payda Sıfır Olamaz", "secim", soru="Aşağıdakilerden hangisi tanımsızdır?",
  secenekler=["[[0/8]]", "[[8/0]]", "[[8/1]]", "[[-8/2]]"], dogru=1,
  aciklama=f"Paydası 0 olan kesir tanımsızdır. 0 ile çarpılınca 8 eden sayı yok {S2}.")
a("u1k2", "Aradaki Sayılar", "kisa", soru="Sayı doğrusunda 0 ile 1 arasında kaç tam sayı vardır?", yanit="0", sayi=True,
  aciklama=f"0 ile 1 arasında tam sayı yoktur ama rasyonel sayılar vardır {S2}.")
a("u1k2", "Eksi Bütüne Aittir", "secim", soru="[[-1 2/3]] sayısının bileşik kesir hâli hangisidir?",
  secenekler=["[[-5/3]]", "[[-1/3]]", "[[5/3]]", "[[-2/3]]"], dogru=0,
  aciklama=f"Eksiyi kenara koy: 1 tam 2/3 = 5/3. Eksiyi geri ekle: −5/3 {S2}.")
a("u1k2", "Sayı Aileleri", "dy", ifade="Her tam sayı bir rasyonel sayıdır.", dogru=True,
  aciklama=f"Her tam sayı paydası 1 olan kesir gibi yazılır: 5 = 5/1 {S2}.")
a("u1k2", "Eksinin Yeri", "secim", soru="Aşağıdakilerden hangisi diğerlerinden farklı bir sayıdır?",
  secenekler=["[[-9/3]]", "[[9/-3]]", "−3", "[[9/3]]"], dogru=3,
  aciklama=f"Eksi payda, paydada ya da önde olabilir; değer −3'tür. 9/3 ise +3 {S2}.")

# --- Konu 3: Mutlak değer
a("u1k3", "Mutlak Değer", "kisa", soru="|−8| kaçtır?", yanit="8", sayi=True,
  aciklama=f"Mutlak değer 0'a uzaklıktır. İşareti sil, sayı kalır: 8 {S3}.")
a("u1k3", "Mutlak Değeri Verilen Sayı", "secim", soru="Mutlak değeri 5 olan sayılar hangileridir?",
  secenekler=["Yalnız 5", "Yalnız −5", "5 ve −5", "0 ve 5"], dogru=2,
  aciklama=f"0'a 5 birim uzakta iki sayı var: sağda 5, solda −5 {S3}.")
a("u1k3", "Mutlak Değer Eksi Olmaz", "dy", ifade="Bir sayının mutlak değeri negatif olabilir.", dogru=False,
  duzeltme="Uzaklık eksi olmaz. Mutlak değer ya 0 ya da pozitiftir.",
  aciklama=f"Mutlak değer uzaklıktır, hiç eksi olmaz {S3}.")
a("u1k3", "Eksik ya da Fazla", "kisa", soru="Bir çay fabrikasında hedef 500 gram. Bir paket 496 gram geldi. Hata miktarı kaç gramdır?", yanit="4", sayi=True,
  aciklama=f"500'e uzaklık: 500 − 496 = 4 gram {S3}.")
a("u1k3", "Eksi de Artı da Aynı", "secim", soru="Mutlak değeri 3'ten küçük olan tam sayılar hangileridir?",
  secenekler=["1, 2", "−2, −1, 0, 1, 2", "−3, 3", "0, 1, 2, 3"], dogru=1,
  aciklama=f"0'a uzaklığı 3'ten az olanlar: −2, −1, 0, 1, 2 {S3}.")

# --- Konu 4: Farklı gösterimler
a("u1k4", "Paydayı 10, 100, 1000 Yap", "kisa", soru="[[9/25]] kesrinin ondalık gösterimini yaz.", yanit="0,36", sayi=True,
  aciklama=f"9/25 = 36/100 = 0,36 {S4}.")
a("u1k4", "Sonlu mu, Devirli mi?", "secim", soru="Hangisinin ondalık gösterimi devirlidir?",
  secenekler=["[[1/4]]", "[[3/5]]", "[[2/3]]", "[[7/10]]"], dogru=2,
  aciklama=f"Paydada 2 ve 5'ten başka asal çarpan varsa devirli olur. 3 var {S4}.")
a("u1k4", "Ondalıktan Kesre", "secim", soru="0,7 sayısının kesir hâli hangisidir?",
  secenekler=["[[7/100]]", "[[7/10]]", "[[1/7]]", "[[70/10]]"], dogru=1,
  aciklama=f"Virgülden sonra 1 basamak var: paydaya 10 yazılır {S4}.")
a("u1k4", "Devirliden Kesre", "secim", soru="0,[[d:3]] hangi kesre eşittir?",
  secenekler=["[[3/10]]", "[[3/100]]", "[[3/9]]", "[[1/30]]"], dogru=2,
  aciklama=f"Devreden 1 basamak için paydaya bir 9 yazılır: 3/9 {S4}.")
a("u1k4", "Kesir Çizgisi Bölmedir", "dy", ifade="[[1/5]] kesri 1 ÷ 5 demektir ve 0,2'ye eşittir.", dogru=True,
  aciklama=f"Kesir çizgisi bölmedir: 1 ÷ 5 = 0,2 {S4}.")

# --- Konu 5: Karşılaştırma ve sıralama
a("u1k5", "Negatiflerde Uzak Olan Küçük", "secim", soru="Hangisi en küçüktür?",
  secenekler=["−2", "−9", "0", "−5"], dogru=1,
  aciklama=f"Negatiflerde 0'a en uzak olan en küçüktür: −9 {S5}.")
a("u1k5", "Sağdaki Büyüktür", "secim", soru="Mars'ın sıcaklığı −65 °C, Neptün'ün −200 °C. Hangisi doğrudur?",
  secenekler=["Neptün daha sıcaktır.", "Mars daha sıcaktır.", "İkisi eşittir.", "Karşılaştırılamaz."], dogru=1,
  aciklama=f"−65, −200'ün sağındadır, yani daha büyüktür {S5}.")
a("u1k5", "Paydaları ya da Payları Eşitle", "secim", soru="Hangisi doğrudur?",
  secenekler=["[[2/3]] < [[2/5]]", "[[3/7]] > [[5/7]]", "[[2/3]] > [[2/5]]", "[[1/5]] > [[1/2]]"], dogru=2,
  aciklama=f"Paylar eşitse paydası küçük olan büyüktür {S5}.")
a("u1k5", "Negatif, Sıfır, Pozitif", "dy", ifade="Her pozitif sayı, her negatif sayıdan büyüktür.", dogru=True,
  aciklama=f"Negatif < 0 < pozitif {S5}.")
a("u1k5", "Arada Hep Bir Sayı Var", "kisa", soru="[[-7/3]] sayısından küçük olan en büyük tam sayı kaçtır?", yanit="-3", sayi=True,
  aciklama=f"−7/3 = −2 tam 1/3. Ondan küçük ilk tam sayı −3'tür {S5}.")

# --- Konu 6: Tam sayılarla toplama ve çıkarma
a("u1k6", "Aynı İşaret: Topla, İşareti Koru", "kisa", soru="(−6) + (−5) + (−12) kaçtır?", yanit="-23", sayi=True,
  aciklama=f"Aynı işaret: 6 + 5 + 12 = 23, eksi kalır {S6}.")
a("u1k6", "Farklı İşaret: Çıkar, Büyüğün İşareti", "secim", soru="Esma Hanım'ın hesabında −100 TL var. Hesabına 75 TL yatırdı. Yeni bakiyesi kaç TL'dir?",
  secenekler=["−175", "−25", "25", "175"], dogru=1,
  aciklama=f"(−100) + 75: 100 − 75 = 25, büyük olan eksi: −25 {S6}.")
a("u1k6", "Çıkarma = Tersiyle Toplama", "kisa", soru="(+10) − (−8) kaçtır?", yanit="18", sayi=True,
  aciklama=f"Çıkarmayı çevir, topla: 10 + 8 = 18 {S6}.")
a("u1k6", "Aradaki Eksi Çıkarmadır", "secim", soru="−3 − 4 − 5 kaçtır?",
  secenekler=["−12", "−4", "4", "12"], dogru=0,
  aciklama=f"(−3) + (−4) + (−5) = −12 {S6}.")
a("u1k6", "Ters İşaretliler Toplanınca 0", "secim", soru="Hangisinin sonucu 0'dır?",
  secenekler=["(+10) + (+10)", "(−10) − (+10)", "(+10) + (−10)", "(−10) + (−10)"], dogru=2,
  aciklama=f"Bir sayı ile ters işaretlisinin toplamı 0'dır {S6}.")

# --- Konu 7: Çarpma ve bölme
a("u1k7", "Aynı İşaret: Çarpım Artı", "kisa", soru="(−10) · (−10) kaçtır?", yanit="100", sayi=True,
  aciklama=f"Aynı işaret → artı: 100 {S7}.")
a("u1k7", "Çok Çarpanda Eksileri Say", "secim", soru="(−3) · (−5) · (−6) çarpımının sonucu hangisidir?",
  secenekler=["90", "−90", "−14", "14"], dogru=1,
  aciklama=f"Üç eksi var, tek: sonuç eksi. 3 · 5 · 6 = 90 → −90 {S7}.")
a("u1k7", "Bölmede Aynı Kural", "kisa", soru="(−144) ÷ (−12) kaçtır?", yanit="12", sayi=True,
  aciklama=f"Aynı işaret → artı: 144 ÷ 12 = 12 {S7}.")
a("u1k7", "Çarpma = Tekrarlı Toplama", "secim", soru="Klimanın mavi tuşuna her basışta sıcaklık 2 °C azalıyor. Tuşa 3 kez basılırsa sıcaklık nasıl değişir?",
  secenekler=["+6 °C", "−5 °C", "−6 °C", "+5 °C"], dogru=2,
  aciklama=f"3 · (−2) = −6. Sıcaklık 6 derece düşer {S7}.")
a("u1k7", "Bölmenin Farklı Yazılışları", "secim", soru="Hangisi −4'e eşit değildir?",
  secenekler=["(−12) ÷ 3", "[[-12/3]]", "12 : (−3)", "(−12) : (−3)"], dogru=3,
  aciklama=f"(−12) : (−3) aynı işaret, sonuç +4 {S7}.")

# --- Konu 8: Rasyonel sayılarla toplama ve çıkarma
a("u1k8", "Payda Aynıysa Payları Topla", "secim", soru="[[3/7]] + ([[-5/7]]) kaçtır?",
  secenekler=["[[8/7]]", "[[-2/7]]", "[[2/7]]", "[[-8/14]]"], dogru=1,
  aciklama=f"Payda aynı: 3 + (−5) = −2. Sonuç −2/7 {S8}.")
a("u1k8", "Önce Paydaları Eşitle", "secim", soru="([[-1/6]]) + ([[-1/3]]) kaçtır?",
  secenekler=["[[-2/9]]", "[[-1/2]]", "[[1/2]]", "[[-1/9]]"], dogru=1,
  aciklama=f"−1/3 = −2/6. −1/6 + (−2/6) = −3/6 = −1/2 {S8}.")
a("u1k8", "Çıkarma = Tersini Ekle", "kisa", soru="([[-5/6]]) − ([[-1/6]]) kaçtır? En sade hâliyle yaz.", yanit="-2/3", kabul=["-4/6"], sayi=True,
  aciklama=f"Çevir, topla: −5/6 + 1/6 = −4/6 = −2/3 {S8}.")
a("u1k8", "Toplamanın Özellikleri", "dy", ifade="([[-2/9]]) + [[2/9]] = 0 işleminde toplamanın ters eleman özelliği kullanılmıştır.", dogru=True,
  aciklama=f"Toplamları 0 olan iki sayı birbirinin tersidir {S8}.")
a("u1k8", "Problemde Toplama ve Çıkarma", "secim", soru="Termometre [[1/2]] °C gösteriyor. Sıcaklık [[3/2]] °C düştü. Yeni sıcaklık kaç °C'tur?",
  secenekler=["2", "1", "−1", "−2"], dogru=2,
  aciklama=f"1/2 − 3/2 = −2/2 = −1 {S8}.")

# --- Konu 9: Rasyonel sayılarla çarpma
a("u1k9", "Pay Paya, Payda Paydaya", "secim", soru="[[3/5]] · [[2/7]] kaçtır?",
  secenekler=["[[5/12]]", "[[6/35]]", "[[6/12]]", "[[21/10]]"], dogru=1,
  aciklama=f"Pay paya: 3 · 2 = 6, payda paydaya: 5 · 7 = 35 {S9}.")
a("u1k9", "İşaret Tam Sayılardaki Gibi", "kisa", soru="([[-2/3]]) · ([[-3/4]]) kaçtır? En sade hâliyle yaz.", yanit="1/2", kabul=["6/12", "0,5"], sayi=True,
  aciklama=f"Aynı işaret → artı. 2 · 3 / 3 · 4 = 6/12 = 1/2 {S9}.")
a("u1k9", "Bir Sayının Kesrini Bulma", "kisa", soru="Yiğit 600 TL harçlığının [[1/4]]'ünü harcadı. Parası kaç TL azaldı?", yanit="150", sayi=True,
  aciklama=f"600 · 1/4 = 150 TL {S9}.")
a("u1k9", "Çarpmanın Özellikleri", "secim", soru="Hangisinde çarpmanın yutan eleman özelliği vardır?",
  secenekler=["[[2/7]] · [[7/2]] = 1", "[[3/5]] · 1 = [[3/5]]", "([[-4/9]]) · 0 = 0", "[[1/2]] · [[1/3]] = [[1/3]] · [[1/2]]"], dogru=2,
  aciklama=f"0 ile çarpınca sonuç 0 olur: 0 yutar {S9}.")
a("u1k9", "Tam Sayılı Kesri Önce Çevir", "secim", soru="([[-1 1/3]]) · [[3/8]] kaçtır?",
  secenekler=["[[-1/2]]", "[[1/2]]", "[[-3/8]]", "[[-1 1/8]]"], dogru=0,
  aciklama=f"−1 tam 1/3 = −4/3. −4/3 · 3/8 = −12/24 = −1/2 {S9}.")

# --- Konu 10: Üslü ifadeler
a("u1k10", "Tekrarlı Çarpımı Kısalt", "secim", soru="7 · 7 · 7 · 7 · 7 çarpımının üslü gösterimi hangisidir?",
  secenekler=["5[[u:7]]", "7 · 5", "7[[u:5]]", "35"], dogru=2,
  aciklama=f"7 beş kez çarpılmış: taban 7, üs 5 {S10}.")
a("u1k10", "Taban, Üs ve Değer", "kisa", soru="4[[u:3]] kaçtır?", yanit="64", sayi=True,
  aciklama=f"4 · 4 · 4 = 64. 4 · 3 değil! {S10}.")
a("u1k10", "Parantez Fark Yaratır", "secim", soru="−2[[u:4]] kaçtır?",
  secenekler=["16", "−16", "−8", "8"], dogru=1,
  aciklama=f"Parantez yok: önce 2[[u:4]] = 16, sonra eksi: −16 {S10}.")
a("u1k10", "Eksi Taban: Çift Artı, Tek Eksi", "dytablo", soru="Her eşitlik için Doğru ya da Yanlış seç.", ifadeler=[
  {"s": "(−2)[[u:3]] = −8", "d": True},
  {"s": "(−2)[[u:4]] = −16", "d": False},
  {"s": "(−1)[[u:5]] = −1", "d": True},
  {"s": "1[[u:2025]] = 2025", "d": False}],
  aciklama=f"Eksi tabanda çift üs artı, tek üs eksi. 1'in her kuvveti 1'dir {S10}.")
a("u1k10", "Kesrin Kuvveti", "secim", soru="([[2/3]])[[u:2]] kaçtır?",
  secenekler=["[[4/6]]", "[[4/9]]", "[[2/9]]", "[[4/3]]"], dogru=1,
  aciklama=f"Pay da payda da kuvvetlenir: 2 · 2 / 3 · 3 = 4/9 {S10}.")

# --- Konu 11: Rasyonel sayılarla bölme
a("u1k11", "Böl = Tersiyle Çarp", "secim", soru="[[2/3]] ÷ [[3/4]] kaçtır?",
  secenekler=["[[1/2]]", "[[8/9]]", "[[6/12]]", "[[9/8]]"], dogru=1,
  aciklama=f"Koru, çevir, ters çevir: 2/3 · 4/3 = 8/9 {S11}.")
a("u1k11", "Kaç Tane Sığar?", "kisa", soru="[[3/4]] m kablo [[1/8]] m'lik parçalara ayrılıyor. Kaç parça olur?", yanit="6", sayi=True,
  aciklama=f"3/4 ÷ 1/8 = 3/4 · 8 = 6 {S11}.")
a("u1k11", "Ters Çevir", "secim", soru="Hangi sayının çarpma işlemine göre tersi yoktur?",
  secenekler=["1", "−1", "0", "[[1/2]]"], dogru=2,
  aciklama=f"0'ın tersi yoktur; 0 ile çarpınca 1 elde edilmez {S11}.")
a("u1k11", "Tam Sayılı Kesir ve İşaret", "kisa", soru="(−8) ÷ ([[-4/3]]) kaçtır?", yanit="6", sayi=True,
  aciklama=f"Aynı işaret → artı. 8 · 3/4 = 6 {S11}.")
a("u1k11", "Kesir Çizgisi de Bölmedir", "dy", ifade="Bölmede sayıların yeri değişirse sonuç değişmez.", dogru=False,
  duzeltme="Bölmenin değişme özelliği yoktur; yer değişirse sonuç değişir.",
  aciklama=f"6 ÷ 2 = 3 ama 2 ÷ 6 = 1/3. Bölmede yer önemlidir {S11}.")

# --- Konu 12: Çok adımlı işlemler
a("u1k12", "İşlem Sırası", "kisa", soru="2 + 3 · 4 kaçtır?", yanit="14", sayi=True,
  aciklama=f"Önce çarpma: 3 · 4 = 12, sonra 2 + 12 = 14 {S12}.")
a("u1k12", "Aynı Öncelikte Soldan Sağa", "secim", soru="20 ÷ 4 · 5 kaçtır?",
  secenekler=["1", "25", "4", "100"], dogru=1,
  aciklama=f"Kardeş işlemler soldan sağa: 20 ÷ 4 = 5, 5 · 5 = 25 {S12}.")
a("u1k12", "Önce Parantez", "secim", soru="(2 + 1)[[u:2]] kaçtır?",
  secenekler=["3", "5", "9", "6"], dogru=2,
  aciklama=f"Önce parantezin içi: 3, sonra kuvvet: 3[[u:2]] = 9 {S12}.")
a("u1k12", "Kesir Çizgisi Ayırır", "kisa", soru="Kesir çizgisinin üstünde 3 · 8, altında 10 − 4 yazıyor. Sonuç kaçtır?", yanit="4", sayi=True,
  aciklama=f"Üst 24, alt 6. En son 24 ÷ 6 = 4 {S12}.")
a("u1k12", "Problemi İşleme Çevir", "secim", soru="Valiz boşken 5 kg. İçine her biri 2 kg olan 4 eşya konuyor. Valizin kütlesi hangi işlemle bulunur?",
  secenekler=["(5 + 2) · 4", "5 + 2 · 4", "5 · 2 + 4", "5 + 2 + 4"], dogru=1,
  aciklama=f"Eşyalar 2 · 4 = 8 kg. Valizle 5 + 8 = 13 kg {S12}.")
H.yaz()
