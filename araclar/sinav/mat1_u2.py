import sys, os; sys.path.insert(0, os.path.dirname(__file__))
KOK = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")); sys.path.insert(0, KOK)
from ortak import Havuz
from gen_mat1 import (sec_svg, ust_alt_svg, gorunum_cizimi, yapi_cizimi, svg_yapi, svg_kare_ag, prizma_ag, numarali_hac, gor,
                      Y_L, Y_KOSE, Y_SAKLI)
H = Havuz("mat1", 2, "m2"); a = H.add
S1, S2, S3 = "(s. 118–124)", "(s. 125–128)", "(s. 129–133)"
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

H.yaz()
