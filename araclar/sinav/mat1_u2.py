import sys, os; sys.path.insert(0, os.path.dirname(__file__))
KOK = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")); sys.path.insert(0, KOK)
from ortak import Havuz
from gen_mat1 import (sec_svg, ust_alt_svg, gorunum_cizimi, yapi_cizimi, svg_yapi, svg_kare_ag, prizma_ag, numarali_hac, gor,
                      Y_L, Y_KOSE, Y_SAKLI, svg_dolu, kutu)
H = Havuz("mat1", 2, "m2"); a = H.add
S1, S2, S3, S4, S5 = "(s. 118–124)", "(s. 125–128)", "(s. 129–133)", "(s. 134–138)", "(s. 138–143)"
C4 = ["1. çizim", "2. çizim", "3. çizim", "4. çizim"]

# --- Konu 1: Cisimlerin farklı yönlerden görünümleri
on_L, ust_L, sag_L, arka_L = gor(Y_L, "on"), gor(Y_L, "ust"), gor(Y_L, "sag"), gor(Y_L, "arka")
assert len({on_L, ust_L, sag_L, arka_L}) == 4
a("u2k1", "Görünümü Çizme", "secim", soru="Görseldeki yapının önden görünümü hangisidir?", secenekler=C4, dogru=2,
  svg=ust_alt_svg(yapi_cizimi(Y_L, 22, True), [gorunum_cizimi(g, 18) for g in (ust_L, arka_L, on_L, sag_L)]),
  aciklama=f"Önden 3 sütun var: soldaki 2, diğerleri 1 kare yüksekliğinde {S1}.")
a("u2k1", "Karşılıklı Görünümler Simetrik", "dy", ifade="Eş küplerden yapılmış bir yapının önden ve arkadan görünümleri dikey bir doğruya göre simetriktir.", dogru=True,
  aciklama=f"Ön-arka ve sağ-sol dikey, üst-alt yatay bir doğruya göre simetriktir {S1}.")
a("u2k1", "Saklanan Küpler", "kisa", soru="Görseldeki yapı en az kaç küpten oluşur?", yanit=str(len(Y_SAKLI)), sayi=True, svg=svg_yapi(Y_SAKLI),
  aciklama=f"4 küp görünüyor. Üstteki küpün altında saklı bir küp var: 4 + 1 = 5 {S1}.")
a("u2k1", "Altı Yön", "dytablo", soru="Her ifade için Doğru ya da Yanlış seç.", ifadeler=[
  {"s": "Bir yapıya altı yönden bakılabilir.", "d": True},
  {"s": "Üstten görünümde yapının ön tarafı yukarıda kalır.", "d": False},
  {"s": "Arka arkaya dizilmiş küpler önden bakınca tek kare görünür.", "d": True}],
  aciklama=f"Üstten görünümde ön taraf aşağıda kalır. Öndeki küp arkadakini saklar {S1}.")
sag_K, sol_K = gor(Y_KOSE, "sag"), gor(Y_KOSE, "sol")
ters_K = frozenset((c, 1 - r) for c, r in sag_K); duz = frozenset({(0, 0), (1, 0)})
assert len({sag_K, sol_K, ters_K, duz}) == 4
a("u2k1", "Karşılıklı Görünümler Simetrik", "secim", soru="Sağdan görünümü görseldeki gibi olan bir yapının soldan görünümü hangisidir?", secenekler=C4, dogru=3,
  svg=ust_alt_svg(gorunum_cizimi(sag_K, 22), [gorunum_cizimi(g, 18) for g in (sag_K, ters_K, duz, sol_K)], baslik="Sağdan görünüm"),
  aciklama=f"Soldan görünüm, sağdan görünümün ayna görüntüsüdür: yüksek sütun öbür tarafa geçer {S1}.")
a("u2k1", "Görünüm Kare Gösterir", "secim", soru="Eş küplerden yapılmış yapılarla ilgili aşağıdaki ifadeler verilmiştir.",
  onculler=["Üstten ve alttan görünümler yatay bir doğruya göre simetriktir.", "Tek yönden bakarak bir yapıdaki küp sayısı her zaman bulunur.",
            "Görünümdeki her kare, bir küpün bir yüzüdür."],
  kok="Bu ifadelerden hangileri doğrudur?", secenekler=["Yalnız I", "I ve II", "I ve III", "II ve III"], dogru=2,
  aciklama=f"Öndeki küp arkadakini saklar; tek yönden küp sayısı her zaman bulunmaz {S1}.")

# --- Konu 2: Prizma ve açınımı
a("u2k2", "Yüz, Ayrıt, Köşe", "kisa", soru="Dikdörtgenler prizmasının kaç ayrıtı vardır?", yanit="12", sayi=True,
  aciklama="Önde 4, arkada 4, önü arkaya bağlayan 4: 12 ayrıt.")
a("u2k2", "Açınım Kapanır mı?", "secim", soru="Görseldeki açınımlardan hangisi kapanınca bir dikdörtgenler prizması olur?", secenekler=C4, dogru=2,
  svg=sec_svg([prizma_ag("bes"), prizma_ag("cakisan"), prizma_ag("dogru"), prizma_ag("cakisan_sol")], h=160),
  aciklama=f"6 yüzü olan ve eş yüzleri karşılıklı gelen açınım kapanır {S2}.")
a("u2k2", "Birden Fazla Açınım", "dy", ifade="Bir dikdörtgenler prizmasının yalnızca bir açınımı vardır.", dogru=False,
  duzeltme="Bir dikdörtgenler prizmasının birden fazla açınımı vardır.", aciklama=f"Farklı ayrıtlardan kesilince farklı açınımlar elde edilir {S2}.")
a("u2k2", "Açınım Kapanır mı?", "secim", soru="Görseldeki açınım kapatılınca 1 numaralı yüzün karşısına hangi yüz gelir?",
  secenekler=["2", "3", "5", "6"], dogru=1, svg=svg_kare_ag(numarali_hac()),
  aciklama=f"Dik sırada 1 ile 3 arasında yalnızca 2 var: 1 ile 3 karşılıklı {S2}.")
a("u2k2", "Karşılıklı Yüzler Eştir", "dytablo", soru="Her ifade için Doğru ya da Yanlış seç.", ifadeler=[
  {"s": "Dikdörtgenler prizmasının 6 yüzü vardır.", "d": True},
  {"s": "Dikdörtgenler prizmasının 8 köşesi vardır.", "d": True},
  {"s": "Dikdörtgenler prizmasında karşılıklı yüzler farklı büyüklüktedir.", "d": False}],
  aciklama=f"6 yüz, 12 ayrıt, 8 köşe. Karşılıklı yüzler eştir {S2}.")
a("u2k2", "Yüz, Ayrıt, Köşe", "bosluk", soru="Cümlelerdeki boşlukları kelime havuzundan uygun olanla doldur.", cumleler=[
  {"c": "Prizmanın düz yüzeylerinin her birine ___ denir.", "cevap": "yüz"},
  {"c": "İki yüzün birleştiği çizgiye ___ denir.", "cevap": "ayrıt"},
  {"c": "Ayrıtların buluştuğu noktaya ___ denir.", "cevap": "köşe"}],
  havuz=["taban", "açınım"], aciklama="Yüz düz yüzey, ayrıt birleşme çizgisi, köşe buluşma noktasıdır.")

# --- Konu 3: Yüzey alanı
a("u2k3", "Yüzey Alanı Formülü", "kisa", soru="Ayrıtları 2 cm, 4 cm ve 5 cm olan dikdörtgenler prizmasının yüzey alanı kaç cm²'dir?", yanit="76", sayi=True,
  aciklama=f"Yüzler 8, 10, 20. 2 · (8 + 10 + 20) = 76 cm² {S3}.")
a("u2k3", "Küp", "kisa", soru="Bir ayrıtı 3 cm olan küpün yüzey alanı kaç cm²'dir?", yanit="54", sayi=True,
  aciklama=f"Bir yüz 3 · 3 = 9 cm². 6 · 9 = 54 cm² {S3}.")
a("u2k3", "Yüzey Alanı Formülü", "secim", soru="Ayrıtları a, b ve c olan dikdörtgenler prizmasının yüzey alanı hangisidir?",
  secenekler=["a · b · c", "2 · (a · b + a · c + b · c)", "a + b + c", "6 · a · b"], dogru=1,
  aciklama=f"Üç farklı yüzün alanını topla, 2 ile çarp {S3}.")
a("u2k3", "Kare Prizma", "dy", ifade="Taban kenarı a, yüksekliği b olan kare prizmanın yüzey alanı 2 · a[[u:2]] + 4 · a · b'dir.", dogru=True,
  aciklama=f"İki kare yüz (2 · a²) ve dört eş dikdörtgen yüz (4 · a · b) {S3}.")
a("u2k3", "Hangi Yüzler Kaplanacak?", "secim", soru="Tabanı 5 cm × 5 cm, yüksekliği 4 cm olan kapaksız bir kutunun dışı boyanacak. Kaç cm² boyanır?",
  secenekler=["105", "130", "100", "125"], dogru=0,
  aciklama=f"Kapak yok: taban 25 + dört yan yüz 4 · 20 = 80. 25 + 80 = 105 cm² {S3}.")
a("u2k3", "Küp", "secim", soru="Prizmalarla ilgili aşağıdaki ifadeler verilmiştir.",
  onculler=["Küp, dikdörtgenler prizmasının özel bir durumudur.", "Yüzey alanı cm³ birimiyle yazılır.", "Bir küpün yüzey alanı 6 · a[[u:2]] ile bulunur."],
  kok="Bu ifadelerden hangileri doğrudur?", secenekler=["I ve III", "Yalnız I", "Yalnız III", "I, II ve III"], dogru=0,
  aciklama=f"Yüzey alanı bir alandır; cm² ile yazılır. I ve III doğru {S3}.")

# --- Konu 4: Hacim ve birim küp
a("u2k4", "Hacim", "secim", soru="Bir cismin uzayda kapladığı yere ne denir?", secenekler=["Yüzey alanı", "Hacim", "Açınım", "Ayrıt"], dogru=1,
  aciklama=f"Cismin kapladığı yer hacimdir; yüzey alanı yüzlerin alanları toplamıdır {S4}.")
a("u2k4", "Eş Nesnelerle Ölçme", "dy", ifade="İki kutunun hacmini karşılaştırmak için birini bilyeyle, diğerini küple doldurup sayıları karşılaştırabiliriz.", dogru=False,
  duzeltme="İki kutu da aynı eş nesnelerle doldurulmalıdır.", aciklama=f"Farklı nesnelerle sayılan sonuçlar karşılaştırılamaz {S4}.")
a("u2k4", "Birim Küp Cinsinden Hacim", "kisa", soru="Görseldeki prizma birim küplerle dolu. Hacmi kaç br³?", yanit="12", sayi=True, svg=svg_dolu(kutu(3, 2, 2), s=34),
  aciklama=f"Alt katta 3 + 3 = 6 küp, iki kat: 12 br³ {S4}.")
a("u2k4", "Kaplamak mı, Doldurmak mı?", "eslestir", soru="Her durumu, bulunması gereken ölçüyle eşleştir.", ciftler=[
  {"sol": "Kutuyu paket kâğıdıyla kaplamak", "sag": "Yüzey alanı"},
  {"sol": "Kutuya kaç küp sığacağını bulmak", "sag": "Hacim"},
  {"sol": "Kutunun bir kenarını ölçmek", "sag": "Uzunluk"}],
  aciklama="Kaplamak yüzey alanı, doldurmak hacimdir.")
a("u2k4", "Birim Küp", "bosluk", cumleler=[
  {"c": "Ayrıtlarının her biri 1 birim olan küpe ___ denir.", "cevap": "birim küp"},
  {"c": "Bir cismin uzayda kapladığı yere ___ denir.", "cevap": "hacim"},
  {"c": "Bir kutuyu kâğıtla kaplamak için ___ buluruz.", "cevap": "yüzey alanı"}],
  havuz=["ayrıt", "açınım"], aciklama=f"Birim küp, hacim ve yüzey alanı tanımları {S4}.")
a("u2k4", "Daha Uygun Birim", "secim", soru="Kutuların hacmini ölçmekle ilgili aşağıdaki ifadeler verilmiştir.",
  onculler=["Pinpon toplarıyla doldurunca aralarında boşluk kalır.", "Hacmi ölçmek için en uygun birim eş küplerdir.", "Farklı nesnelerle ölçülen sonuçlar her zaman aynıdır."],
  kok="Bu ifadelerden hangileri doğrudur?", secenekler=["Yalnız I", "I ve II", "II ve III", "I, II ve III"], dogru=1,
  aciklama=f"Farklı nesneler farklı sonuç verir; küpler boşluksuz doldurur {S4}.")

# --- Konu 5: Dikdörtgenler prizmasının hacmi
a("u2k5", "Hacim Formülü", "kisa", soru="Ayrıtları 4 br, 3 br ve 5 br olan dikdörtgenler prizmasının hacmi kaç br³?", yanit="60", sayi=True,
  aciklama=f"Taban alanı 4 · 3 = 12, 12 · 5 = 60 br³ {S5}.")
a("u2k5", "Kare Prizma ve Küp", "secim", soru="Bir ayrıtı 3 br olan küpün hacmi kaç br³'tür?", secenekler=["9", "18", "27", "12"], dogru=2,
  aciklama=f"3 · 3 · 3 = 3[[u:3]] = 27 br³ {S5}.")
a("u2k5", "Ayrıt Değişince Hacim", "dytablo", soru="Her ifade için Doğru ya da Yanlış seç.", ifadeler=[
  {"s": "Bir prizmanın yüksekliği 2 katına çıkarsa hacmi de 2 katına çıkar.", "d": True},
  {"s": "Bir küpün her ayrıtı 3 katına çıkarsa hacmi de 3 katına çıkar.", "d": False},
  {"s": "Bir prizmanın bütün ayrıtları 2 katına çıkarsa hacmi 8 katına çıkar.", "d": True}],
  aciklama=f"Küpün ayrıtı 3 katı olursa hacmi 3 · 3 · 3 = 27 katı olur {S5}.")
a("u2k5", "Aynı Hacim, Farklı Prizma", "secim", soru="Hangisi 18 eş birim küpten yapılmış bir dikdörtgenler prizmasının ayrıtları olamaz?",
  secenekler=["1 br, 2 br, 9 br", "1 br, 3 br, 6 br", "2 br, 3 br, 3 br", "2 br, 2 br, 5 br"], dogru=3,
  aciklama=f"2 · 2 · 5 = 20; öbürlerinin çarpımı 18 {S5}.")
a("u2k5", "Katman", "kisa", soru="Bir prizmanın taban katmanında 6 birim küp var ve prizma 5 katmandan oluşuyor. Hacmi kaç br³?", yanit="30", sayi=True,
  aciklama=f"Bir katman × katman sayısı: 6 · 5 = 30 br³ {S5}.")
a("u2k5", "Hacim Birimi br³", "dy", ifade="Hacim br² birimiyle yazılır.", dogru=False, duzeltme="Hacim br³ ile yazılır; br² alan birimidir.",
  aciklama=f"Üç ayrıt çarpılır: br · br · br = br³ {S5}.")

H.yaz()
