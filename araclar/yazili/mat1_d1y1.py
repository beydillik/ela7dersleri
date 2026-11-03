"""Matematik 7 · 1. Dönem 1. Yazılı — Yazılıya Hazırlık verisi.
Kapsam: MEB senaryo tablosu, Senaryo 4 (okulun seçtiği): MAT.7.1.1 (2), MAT.7.1.2 (2), MAT.7.1.3 (2) = 6 soru. MAT.7.1.4 (işlem problemleri) YOK.
Kaynaklar: MEB "Yazılıya Hazırlanıyorum 7. Sınıf Matematik 1. Dönem 1. Yazılı" (yalnız senaryoya giren 1–11. sorular, çözümleriyle),
ders kitabı (sayfa atıflı), yazilihocam.com 7. sınıf 1. dönem 1. yazılı örnekleri (siyah, mavi, pembe; senaryoya uyan sorular, rakamlar birebir).
Matematik uyarlaması (Kemal, 3 Kasım 2026): kazanımlar Hatırla/Konu Tekrarı için 6 alt konuya bölündü ("ust" = senaryodaki kazanım);
basamak 2 parçaları işlem adımları; ✓ tablolu sorularda satır satır yazma; MEB sorularında öncelik (3 banko, 2 puan topla, 1 bir adım yaz).
Çalıştır: python3 araclar/yazili/mat1_d1y1.py"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from yazili import Yazili
import cizim_mat as Z


def A(ad, *k): return {"ad": ad, "k": list(k)}
def SIRA(ad, *g): return {"ad": ad, "sira": [list(x) if isinstance(x, (list, tuple)) else [x] for x in g]}
def M(harf, soru, cevap=None, an=None, formul=None, iskele=None, puan=None):
    m = {"harf": harf, "soru": soru}
    if formul: m["formul"] = formul
    if iskele: m["iskele"] = iskele
    if cevap: m["cevap"] = cevap; m["anahtarlar"] = an or []
    if puan is not None: m["puan"] = puan
    return m
def P(bas, ornek, havuz, k=None, hepsi=None, sira=None, serbest=False):
    d = {"bas": bas, "ornek": ornek, "havuz": havuz}
    if k: d["k"] = k
    if hepsi: d["hepsi"] = hepsi
    if sira: d["sira"] = sira
    if serbest: d["serbest"] = True
    return d
def B(kisa, dogru, eksik, yanlis, ipucu, aciklama, *parcalar):
    return {"kisaCevap": kisa, "basamak": {"sec": {"secenekler": [dogru, eksik, yanlis], "dogru": 0, "ipucu": ipucu, "aciklama": aciklama}, "parcalar": list(parcalar)}}
def IK(kisa, tetik, notu, *parcalar): return {"kisaCevap": kisa, "tetik": tetik, "kalipNot": notu, "basamak": {"parcalar": list(parcalar)}}
def Q(madde, tetik, notu, b):
    """MEB maddesine tetik, kalıp notu ve basamak ekler."""
    madde.update(b); madde["tetik"], madde["kalipNot"] = tetik, notu; madde.pop("iskele", None); return madde

K11, K12, K13 = "MAT.7.1.1", "MAT.7.1.2", "MAT.7.1.3"
KA, KB, KC, KD, KE, KF = "MAT.7.1.1-A", "MAT.7.1.1-B", "MAT.7.1.1-C", "MAT.7.1.2-A", "MAT.7.1.2-B", "MAT.7.1.3-A"
AD11 = "Gerçek yaşam ya da matematiksel durumlarda doğal sayı, tam sayı ve rasyonel sayıları yorumlayabilme"
AD12 = "Gerçek yaşam durumlarında rasyonel sayıların ondalık gösterimlerini yansıtabilme"
AD13 = "Rasyonel sayıların karşılaştırma ve sıralama ilişkilerini yorumlayabilme"

Y = Yazili("mat1", "d1y1",
    baslik="1. Dönem 1. Yazılı", ders="Matematik", senaryo="Senaryo 4", sure=40, tarih="2026-11-05",
    dagilim={K11: 2, K12: 2, K13: 2},
    giris="Okulun seçtiği senaryoda <b>6 soru</b> var: üç kazanımın her birinden 2 soru. Önce <b>★★★ Banko</b> soruları sağlamla, bunlar kesin puan. <b>★</b> sorularda ilk adımı yazmak bile puan getirir. İşlem problemleri (toplama, çarpma, üslü ifadeler) bu yazılıda yok.",
    kapsamDisi=["Tam sayılarla ve rasyonel sayılarla dört işlem problemleri (MAT.7.1.4)", "Üslü ifadeler", "İşlem önceliği ve çok adımlı işlemler", "Toplama ve çarpma işleminin özellikleri"],
    puanNotu="Puanlar tahminidir: okul soruların puanını farklı dağıtabilir. Toplam 100. Provalarda her kazanımdan 2 soru var; hangi alt konudan geleceği tahmindir.",
    kaynakNotu="Sorular MEB'in yayımladığı 'Yazılıya Hazırlanıyorum 7. Sınıf Matematik 1. Dönem 1. Yazılı' örneklerine (senaryoya giren 1–11. sorular), ders kitabına ve yazilihocam.com yazılı örneklerine dayanır.",
    soruGiris="Bunlar MEB'in örnek soruları; yazılıda <b>benzerleri</b> çıkacak. <b>★★★ Banko</b> olanlarla başla. Cevabı <b>yazarak</b> ver: kesri 7/4, eksiyi - ile yazabilirsin.",
    kazanimAd="konu")

# =====================================================================
# KONULAR (Hatırla kartları + Hatırla ve Tekrarla boşlukları). "ust" = senaryodaki kazanım.
# =====================================================================
Y.kazanim(kod=KA, ust=K11, ad=AD11, kisa="Tam Sayılarla Gerçek Yaşam", soru=2, soruNot="MAT.7.1.1'den 2 soru (3 konudan)", renk="#d9480f",
    konular=["u1k1"], sayfa="s. 19–20, 51", svg=Z.h_altust(),
    maddeler=["<b>Üstü, yukarı, gelir, alacak, yatırılan</b> → pozitif (+). <b>Altı, aşağı, borç, kayıp</b> → negatif (−). (s. 20)",
              "Deniz seviyesi, zemin kat ve 0 °C <b>başlangıç (0)</b> kabul edilir. (s. 20)",
              "Örnek: deniz seviyesinin 10 935 m altı → <b>−10 935</b>; sıfırın 25 °C altı → <b>−25</b>; zeminden 369 m yukarı → <b>+369</b>. (MEB örnek sorusu)",
              "Doğal sayılar: 0, 1, 2, 3… <b>Tam sayılar</b>: negatif tam sayılar, sıfır ve pozitif tam sayılar. (s. 20)",
              "Sayı doğrusunda <b>soldaki sayı daha küçüktür</b>: −45 < −40, çünkü −45 daha solda (daha soğuk). (s. 51)",
              "Aralık sorusu: sıcaklık <b>en düşük ile en yüksek arasındaysa ✓</b>. Önce en düşüğe, sonra en yükseğe bak. (MEB örnek sorusu)"],
    kelimeler=["üstü → +", "altı → −", "0 = başlangıç", "en düşük ile en yüksek arası", "soldaki daha küçük"],
    hatalar=[{"yanlis": "−45, −40'tan büyüktür (45 büyük sayı).", "dogru": "−45 daha solda: −45 < −40, yani daha soğuk."},
             {"yanlis": "İşaretsiz yazmak: “10 935”.", "dogru": "Deniz seviyesinin altı olduğu için −10 935 yaz."},
             {"yanlis": "7 °C'yi kutup tilkisine işaretlemek.", "dogru": "Tilkide en yüksek +5 °C; 7 daha büyük, aralığın dışında."}],
    tekrar=[{"c": "Deniz seviyesinin {üstü|altı} pozitif, {altı|üstü} negatif tam sayıyla gösterilir.", "s": "s. 20"},
            {"c": "Hesaba para yatırmak {pozitif|negatif}, borç ya da kayıp {negatif|pozitif} sayıyla gösterilir.", "s": "s. 20"},
            {"c": "Deniz seviyesi, zemin kat ve 0 °C {başlangıç (0)|en büyük sayı|en küçük sayı} kabul edilir.", "s": "s. 20"},
            {"c": "Sayı doğrusunda {soldaki|sağdaki} sayı daha küçüktür: −45 {<|>} −40.", "s": "s. 51"},
            {"c": "Bir sıcaklık {en düşük ile en yüksek arasındaysa|en düşükten küçükse|en yüksekten büyükse} o aralıktadır, ✓ konur.", "s": "cevap kalıbı"},
            {"c": "En yüksek sıcaklığı +5 °C olan aralıkta 7 °C {yoktur|vardır}, çünkü 7 sayısı +5'ten {büyüktür|küçüktür}.", "s": "MEB örnek sorusu"},
            {"c": "−3 bir {tam sayıdır ama doğal sayı değildir|doğal sayıdır}.", "s": "s. 20"}])

Y.kazanim(kod=KB, ust=K11, ad=AD11, kisa="Mutlak Değer", soru=2, soruNot="MAT.7.1.1'den 2 soru (3 konudan)", renk="#1f9e8f",
    konular=["u1k3"], sayfa="s. 37", svg=Z.h_mutlak(),
    maddeler=["Bir sayının <b>0'a uzaklığına</b> mutlak değeri denir; |a| ile gösterilir. (s. 37)",
              "Mutlak değer <b>negatif olamaz</b>: |−3| = |+3| = 3, |0| = 0. (s. 37)",
              "Mutlak değeri 11 olan <b>iki</b> tam sayı vardır: −11 ve +11. (s. 37)",
              "İki sayı 0'ın iki yanındaysa aralarındaki uzaklık için <b>uzaklıkları topla</b>: −11 ile +11 arası 11 + 11 = 22 birim. (MEB örnek sorusu)",
              "<b>Hata miktarı</b> = |kütle − hedef|. Fark eksi çıkarsa paket eksik, artı çıkarsa fazla; hata miktarı her zaman pozitif. (MEB örnek sorusu)",
              "Hedefi bul: paket eksikse <b>ekle</b> (496 + 4 = 500), fazlaysa <b>çıkar</b> (254 − 4 = 250). (MEB örnek sorusu)"],
    kelimeler=["0'a uzaklık", "iki sayı: − ve +", "11 + 11 = 22", "hata = mutlak değer", "eksik → ekle", "fazla → çıkar"],
    hatalar=[{"yanlis": "|−7| = −7", "dogru": "Mutlak değer negatif olamaz: |−7| = 7."},
             {"yanlis": "Mutlak değeri 11 olan sayı yalnız 11'dir.", "dogru": "İki sayı var: −11 ve +11."},
             {"yanlis": "−11 ile +11 arası 0 birimdir (11 − 11).", "dogru": "0'ın iki yanında: 11 + 11 = 22 birim."}],
    tekrar=[{"c": "Bir sayının {0'a|1'e|en büyük sayıya} uzaklığına o sayının mutlak değeri denir.", "s": "s. 37"},
            {"c": "Mutlak değer {negatif olamaz|her zaman negatiftir}: |−3| = {3|−3}.", "s": "s. 37"},
            {"c": "Mutlak değeri 11 olan {iki|bir|üç} tam sayı vardır: −11 ve +11.", "s": "s. 37"},
            {"c": "−11 ile +11 arasındaki uzaklık 11 {+|−} 11 = {22|0} birimdir.", "s": "MEB örnek sorusu"},
            {"c": "Paket hedeften 4 g eksikse hedefi bulmak için 4 g {eklenir|çıkarılır}.", "s": "MEB örnek sorusu"},
            {"c": "Hata miktarı, kütle ile hedef arasındaki farkın {mutlak değeridir|kendisidir ve eksi olabilir}.", "s": "MEB örnek sorusu"},
            {"c": "En az hata, mutlak değeri {en küçük|en büyük} olandır; 1 g eksik ile 1 g fazla {eşit|farklı} hatadır.", "s": "MEB örnek sorusu"}])

Y.kazanim(kod=KC, ust=K11, ad=AD11, kisa="Rasyonel Sayılar ve Sayı Doğrusu", soru=2, soruNot="MAT.7.1.1'den 2 soru (3 konudan)", renk="#6741d9",
    konular=["u1k2"], sayfa="s. 27–32", svg=Z.h_kumeler(),
    maddeler=["a tam sayı, b sıfırdan farklı tam sayı olmak üzere <b>a/b</b> şeklinde yazılabilen sayılar rasyonel sayıdır. (s. 28)",
              "Paydası 0 olan ifade <b>tanımsızdır</b>: [[3/0]] rasyonel sayı değildir. (s. 28)",
              "Her tam sayı paydası 1 olan bir rasyonel sayıdır (−5 = [[-5/1]]). Her doğal sayı bir tam sayıdır: <b>doğal ⊂ tam ⊂ rasyonel</b>. (s. 20, 30)",
              "<b>Önce sadeleştir</b>: [[12/4]] = 3 → doğal, tam, rasyonel; [[-7/7]] = −1 → tam, rasyonel; −1,8 → yalnız rasyonel. (MEB örnek sorusu)",
              "Denk kesirler sayı doğrusunda <b>aynı noktadır</b>: [[-7/4]] = [[-14/8]] = [[-21/12]]. Sadeleştirince aynı sayı çıkar. (s. 27)",
              "Sayı doğrusunda göster: işaret → hangi iki tam sayı arası → aralığı payda kadar eş parçaya böl → tam kısımdan say. [[-7/4]] = [[-1 3/4]]: −2 ile −1 arasında. (s. 32)"],
    kelimeler=["a/b, b ≠ 0", "payda 0 → tanımsız", "doğal ⊂ tam ⊂ rasyonel", "önce sadeleştir", "denk kesir = aynı nokta", "tam sayılı kesir"],
    hatalar=[{"yanlis": "[[3/0]] = 0", "dogru": "Payda 0 olamaz: [[3/0]] tanımsız, hiçbir kümede değil."},
             {"yanlis": "−5 rasyonel sayı değildir.", "dogru": "−5 = [[-5/1]]; her tam sayı rasyoneldir."},
             {"yanlis": "[[-14/8]] ile [[-7/4]] farklı sayılardır.", "dogru": "2 ile sadeleştirince aynı: denk kesirler aynı noktadır."}],
    tekrar=[{"c": "a/b biçimindeki bir sayının rasyonel olması için b {sıfırdan farklı|sıfır|negatif} olmalıdır.", "s": "s. 28"},
            {"c": "Paydası 0 olan [[3/0]] ifadesi {tanımsızdır|sıfıra eşittir|bir doğal sayıdır}.", "s": "s. 28"},
            {"c": "Her tam sayı, paydası {1|0} olan bir rasyonel sayıdır: −5 = [[-5/1]].", "s": "s. 30"},
            {"c": "[[12/4]] sadeleşince {3|12|4} olur; bu yüzden doğal, tam ve rasyonel sayıdır.", "s": "MEB örnek sorusu"},
            {"c": "−1,8 tam sayı olmadığı için {yalnız rasyonel|doğal} sayıdır.", "s": "MEB örnek sorusu"},
            {"c": "[[-14/8]] ve [[-21/12]] sadeleşince [[-7/4]] olur; denk kesirler sayı doğrusunda {aynı noktadadır|farklı noktalardadır}.", "s": "s. 27"},
            {"c": "[[-7/4]] = [[-1 3/4]] sayısı −2 ile {−1|0|−3} arasındadır.", "s": "s. 32"}])

Y.kazanim(kod=KD, ust=K12, ad=AD12, kisa="Sonlu mu, Devirli mi?", soru=2, soruNot="MAT.7.1.2'den 2 soru (2 konudan)", renk="#1971c2",
    konular=["u1k4"], sayfa="s. 41–43", svg=Z.h_sonlu(),
    maddeler=["Her rasyonel sayının bir <b>ondalık gösterimi</b> vardır: ya sonlu (0,35) ya da devirli (0,1[[d:6]]). (s. 43)",
              "<b>1. adım: Sadeleştir.</b> [[15/24]] = [[5/8]]. Kural en sade hâle uygulanır. (s. 43)",
              "<b>2. adım: Paydayı asal çarpanlarına ayır.</b> 20 = 2 · 2 · 5; 18 = 2 · 3 · 3; 35 = 5 · 7. (s. 43)",
              "Paydada <b>yalnız 2 ve 5</b> varsa → <b>sonlu</b>. 2 ve 5 dışında asal çarpan (3, 7, 11…) varsa → <b>devirli</b>. (s. 43)",
              "?/35 sonlu olsun: 35 = 5 · 7 → 7 sadeleşip gitmeli → <b>? 7'nin katı</b> olmalı (7, 14, 21…). (MEB örnek sorusu)",
              "Paydası 10, 100, 1000 olan kesir doğrudan ondalık yazılır: [[9/10]] = 0,9; [[2375/1000]] = 2,375. (s. 41–42)"],
    kelimeler=["önce sadeleştir", "asal çarpan", "yalnız 2 ve 5 → sonlu", "3, 7, 11 → devirli", "7'nin katı", "gerekçe = paydanın çarpanları"],
    hatalar=[{"yanlis": "Sadeleştirmeden karar vermek: 24'te 3 var, [[15/24]] devirli.", "dogru": "Önce sadeleştir: [[5/8]], 8 = 2 · 2 · 2 → sonlu."},
             {"yanlis": "Payda çift sayıysa sonludur.", "dogru": "18 çift ama 3 çarpanı var → devirli."},
             {"yanlis": "Gerekçesiz cevap: “sonlu”.", "dogru": "Paydanın çarpanlarını yaz: 20 = 2 · 2 · 5 → sonlu."}],
    tekrar=[{"c": "Karar vermeden önce kesir {sadeleştirilir|genişletilir|ters çevrilir}.", "s": "s. 43"},
            {"c": "En sade hâlin paydasında yalnız 2 ve 5 varsa ondalık gösterim {sonlu|devirli} olur.", "s": "s. 43"},
            {"c": "Paydada 3, 7, 11 gibi bir asal çarpan varsa ondalık gösterim {devirli|sonlu} olur.", "s": "s. 43"},
            {"c": "20 = 2 · 2 · 5 olduğu için [[7/20]] {sonlu|devirli}; 18 = 2 · 3 · 3 olduğu için [[11/18]] {devirli|sonlu} olur.", "s": "MEB örnek sorusu"},
            {"c": "[[15/24]] sadeleşince [[5/8]] olur; 8 = 2 · 2 · 2 olduğu için ondalık gösterimi {sonlu|devirli}.", "s": "MEB örnek sorusu"},
            {"c": "?/35 sonlu olsun diye paydadaki 7 {sadeleşmeli|kalmalı}; ? sayısı {7'nin|5'in|2'nin} katı olmalı.", "s": "MEB örnek sorusu"}])

Y.kazanim(kod=KE, ust=K12, ad=AD12, kisa="Devirli Sayıyı Kesre Çevirme", soru=2, soruNot="MAT.7.1.2'den 2 soru (2 konudan)", renk="#e8590c",
    konular=["u1k4"], sayfa="s. 44–46", svg=Z.h_devir(),
    maddeler=["Devreden rakamların üstüne çizgi konur: 1,2333… = 1,2[[d:3]]. (s. 44)",
              "<b>Pay:</b> virgül ve çizgi yokmuş gibi sayının tamamı − devretmeyen kısım: 1,2[[d:3]] → 123 − 12 = 111. (s. 46)",
              "<b>Payda:</b> devreden basamak kadar 9, devretmeyen ondalık basamak kadar 0: 1,2[[d:3]] → 90. (s. 46)",
              "Sonra <b>en sade hâl</b>: [[111/90]] = [[37/30]] (3 ile). “En az” sorusunda en sade hâl kullanılır. (MEB örnek sorusu)",
              "Bölünen = pay, bölen = payda: [[37/30]] → 37 ÷ 30. En az toplam 37 + 30 = 67. (MEB örnek sorusu)",
              "Sonlu ondalık da kesre çevrilir: 2,75 = [[275/100]] = [[11/4]]. (s. 41–42)"],
    kelimeler=["tamamı − devretmeyen", "devreden kadar 9", "devretmeyen kadar 0", "en sade hâl", "bölünen = pay, bölen = payda"],
    hatalar=[{"yanlis": "1,2[[d:3]] = [[123/90]]", "dogru": "Paydan devretmeyen kısmı çıkar: 123 − 12 = 111 → [[111/90]]."},
             {"yanlis": "Sadeleştirmeden toplamak: 111 + 90 = 201.", "dogru": "“En az” dediği için önce sadeleştir: [[37/30]] → 67."},
             {"yanlis": "0,[[d:6]] = [[6/10]]", "dogru": "Devreden 1 basamak → payda 9: [[6/9]] = [[2/3]]."}],
    tekrar=[{"c": "Devirli sayıyı kesre çevirirken paya, sayının tamamından {devretmeyen kısım|devreden kısım|9} çıkarılarak yazılır.", "s": "s. 46"},
            {"c": "Paydaya devreden basamak kadar {9|0|1}, devretmeyen ondalık basamak kadar {0|9|1} yazılır.", "s": "s. 46"},
            {"c": "1,2333… için pay 123 − 12 = {111|135|123}, payda {90|99|100} olur.", "s": "MEB örnek sorusu"},
            {"c": "“En az” sorulduğunda kesrin {en sade hâli|genişletilmiş hâli} kullanılır: [[111/90]] = [[37/30]].", "s": "MEB örnek sorusu"},
            {"c": "Bölme işleminde bölünen kesrin {payı|paydası}, bölen kesrin {paydası|payı} olur.", "s": "MEB örnek sorusu"},
            {"c": "0,666… kesre çevrilince payda {9|10|100} olur.", "s": "s. 46"}])

Y.kazanim(kod=KF, ust=K13, ad=AD13, kisa="Karşılaştırma ve Sıralama", soru=2, soruNot="MAT.7.1.3'ten 2 soru", renk="#c2255c",
    konular=["u1k5"], sayfa="s. 51–57", svg=Z.h_sirala(),
    maddeler=["Sayı doğrusunda soldan sağa gidildikçe sayılar <b>büyür</b>; her pozitif sayı her negatif sayıdan büyüktür. (s. 53)",
              "Negatif sayılarda <b>0'dan uzaklaştıkça değer küçülür</b>: mutlak değeri büyük olan daha küçüktür. (s. 53)",
              "Paydaları eşitle, sonra payları karşılaştır: [[-2/3]] = [[-4/6]], [[-7/3]] = [[-14/6]]. (s. 55)",
              "Paydaları eşit negatiflerde <b>payı büyük olan küçüktür</b>: [[-14/6]] < [[-5/6]] < [[-4/6]]. (s. 53, 55)",
              "Tam kısma ayır: [[-45/44]] = [[-1 1/44]]. Tam kısımlar aynıysa kesir kısma bak; payları eşitse <b>paydası küçük olan büyüktür</b>: [[1/38]] > [[1/44]]. (s. 57)",
              "Hata bulma sorusu: <b>Doğru mu? → hatalı adım → çünkü → doğru sıra.</b> (MEB örnek sorusu)"],
    kelimeler=["soldaki küçük", "pozitif > negatif", "payda eşitle", "negatifte payı büyük olan küçük", "tam kısma ayır", "doğru sırayı yaz"],
    hatalar=[{"yanlis": "[[-4/6]] < [[-5/6]], çünkü 4 küçük.", "dogru": "Negatifte payı büyük olan küçük: [[-5/6]] < [[-4/6]]."},
             {"yanlis": "Yalnız “yanlış” yazmak.", "dogru": "Hatalı adımı, nedenini ve doğru sırayı da yaz."},
             {"yanlis": "[[-50/49]] en küçüktür, çünkü payı en büyük.", "dogru": "[[-50/49]] = [[-1 1/49]], −1'e en yakın olduğu için en büyüktür."}],
    tekrar=[{"c": "Sayı doğrusunda sağa gidildikçe sayılar {büyür|küçülür}.", "s": "s. 53"},
            {"c": "Her pozitif sayı her negatif sayıdan {büyüktür|küçüktür}.", "s": "s. 53"},
            {"c": "Negatif sayılarda mutlak değeri büyük olan {daha küçüktür|daha büyüktür}.", "s": "s. 53"},
            {"c": "Paydaları eşit iki negatif kesirden payı büyük olan {daha küçüktür|daha büyüktür}: [[-5/6]] {<|>} [[-4/6]].", "s": "s. 55"},
            {"c": "Karşılaştırmak için paydalar {eşitlenir|toplanır|silinir}: [[-2/3]] = [[-4/6]].", "s": "s. 55"},
            {"c": "Payları eşit kesirlerde paydası küçük olan {büyüktür|küçüktür}: [[1/38]] > [[1/44]].", "s": "s. 57"},
            {"c": "Hata sorusunda yalnız “yanlış” yazmak yetmez; {hatalı adımı ve doğru sırayı|yalnız sayıları} da yazmalısın.", "s": "cevap kalıbı"}])

# =====================================================================
# CEVAP KALIPLARI (Özet'te liste; sorunun içinde tek satır kalıp notu)
# =====================================================================
Y.formul(id="gercek", ad="Gerçek yaşam → tam sayı", kalip="üstü, gelir, yatırılan → + · altı, borç, kayıp → −", ne="“Tam sayılarla ifade ediniz” sorularında", ornek="Deniz seviyesinin 18 m altı → −18")
Y.formul(id="aralik", ad="Aralıkta mı?", kalip="en düşük ile en yüksek arasında → ✓", ne="Tablo ve ✓ sorularında", ornek="−10 °C, −40 ile +10 arasında → ✓")
Y.formul(id="islem", ad="Verilen · İşlem · Sonuç", kalip="İşlem: … = … Sonuç: … (birimiyle)", ne="“Bulunuz”, “kaçtır” sorularında", ornek="496 + 4 = 500 g")
Y.formul(id="gerekce", ad="Cevap + matematiksel gerekçe", kalip="… , çünkü (sayıyla neden)", ne="“Matematiksel gerekçeleriyle açıklayınız” sorularında", ornek="3. ve 5. makine, çünkü ikisinin de hatası 1 g, en küçük.")
Y.formul(id="sonlu", ad="Sonlu mu, devirli mi?", kalip="Sadeleştir → paydayı çarpanlara ayır → yalnız 2 ve 5 ise sonlu", ne="Ondalık gösterim sorularında", ornek="20 = 2 · 2 · 5 → [[7/20]] sonlu")
Y.formul(id="devir", ad="Devirli → kesir", kalip="(tamamı − devretmeyen) / (devreden kadar 9, devretmeyen kadar 0)", ne="Devirli sayı ve “en az” sorularında", ornek="1,2[[d:3]] = [[111/90]] = [[37/30]]")
Y.formul(id="hata", ad="Hatayı bul", kalip="Doğru mu? → hatalı adım → çünkü → doğru sıra", ne="“Doğru mudur?”, “hangi adımda” sorularında", ornek="Yanlış; 3. adımda, çünkü negatifte payı büyük olan küçüktür. Doğru sıra: …")

# =====================================================================
# MEB SORULARI (senaryoya giren 1–11) — öncelik: 3 banko, 2 puan topla, 1 bir adım yaz (Kemal, 3 Kasım 2026)
# =====================================================================
T1 = Z.iki_tablo((["Hayvan", "En düşük", "En yüksek"], [["Kutup tavşanı", "−40 °C", "+10 °C"], ["Kutup tilkisi", "−50 °C", "+5 °C"], ["Ren geyiği", "−35 °C", "+15 °C"]], [130, 95, 95], {"sat_h": 26}),
                 (["Sıcaklık (°C)", "Tavşan", "Tilki", "Geyik"], [["−45", "", "", ""], ["−30", "", "", ""], ["−10", "", "", ""], ["0", "", "", ""], ["+7", "", "", ""], ["+12", "", "", ""]], [95, 75, 75, 75], {"sat_h": 24}),
                 etiket="Hayvanların yaşadığı bölgelerin sıcaklık aralıkları ve işaretlenecek tablo")
TETIK_ARALIK = (["hangi hayvanların", "“✓” sembolü ile"], "Her sıcaklık için: en düşük ile en yüksek arasında mı? Arasındaysa ✓.")
Y.meb(id="m1", no=1, kazanim=KA, oncelik=3, svg=T1,
    metin=["Kutup tavşanı, kutup tilkisi ve ren geyiği soğuk iklimlerde yaşayabilen hayvanlardır. Bir araştırma etkinliğinde bu hayvanların yaşadığı bölgeler için aşağıdaki örnek sıcaklık aralıkları belirlenmiştir."],
    maddeler=[Q(M("a", "Aşağıdaki sıcaklıkların hangi hayvanların yaşadığı bölgelerde görülen sıcaklık aralıklarında olduğunu “✓” sembolü ile belirleyiniz. (Her sıcaklık için hayvanları yaz.)",
        "−45 °C: yalnız kutup tilkisi (−50 ile +5 arasında). −30, −10 ve 0 °C: üç hayvanın üçü de. +7 °C: kutup tavşanı ve ren geyiği (tilkide en yüksek +5). +12 °C: yalnız ren geyiği.",
        [A("−45 °C: yalnız kutup tilkisi", "tilki"), A("−30, −10, 0 °C: üçü de", "üçü", "hepsi", "üç hayvan"), A("+7 °C: tavşan ve geyik", "tavşan"), A("+12 °C: yalnız ren geyiği", "geyi")], "aralik"),
        *TETIK_ARALIK, B("−45: tilki · −30, −10, 0: üçü de · +7: tavşan, geyik · +12: geyik",
        "−45: tilki · −30, −10, 0: üçü de · +7: tavşan, geyik · +12: geyik", "−30, −10, 0: üçü de · +12: geyik", "−45: üçü de · +7: üçü de · +12: tavşan, geyik",
        "Altı sıcaklığın hepsine bakıldı mı? −45 en düşükten küçük mü?", "Sıcaklık bir hayvanın en düşük ile en yüksek sıcaklığı arasındaysa ✓ konur. −45, tavşanın −40'ından da küçüktür. (s. 51)",
        P("−45 °C:", "kutup tilkisi", ["kutup tavşanı", "ren geyiği"], k=["tilki"]),
        P("−30, −10 ve 0 °C:", "üçü de", ["yalnız kutup tilkisi", "hiçbiri"], k=["üçü", "hepsi", "üç hayvan"]),
        P("+7 °C:", "kutup tavşanı ve ren geyiği", ["yalnız kutup tilkisi", "üç hayvan birden"], hepsi=[["tavşan"], ["geyi"]]),
        P("+12 °C:", "ren geyiği", ["kutup tavşanı", "kutup tilkisi"], k=["geyi"])))],
    ikizler=[
        {"svg": Z.tablo_svg(["Ürün", "En düşük", "En yüksek"], [["Dondurma", "−25 °C", "−12 °C"], ["Balık", "−30 °C", "−18 °C"], ["Süt", "+2 °C", "+6 °C"]], [130, 95, 95], etiket="Ürünlerin saklama sıcaklıkları"),
         "metin": ["Bir markette üç ürünün saklanması gereken örnek sıcaklık aralıkları tabloda verilmiştir. Deponun sıcaklığı farklı zamanlarda −28 °C, −20 °C, −15 °C, 0 °C ve +4 °C ölçülmüştür."],
         "maddeler": [M("a", "Bu sıcaklıkların her biri hangi ürünün saklama aralığındadır? Hiçbirinin aralığında olmayan sıcaklık var mı?",
            "−28 °C: balık. −20 °C: dondurma ve balık. −15 °C: dondurma. 0 °C: hiçbiri (sütte en düşük +2). +4 °C: süt.",
            [A("−28 °C: balık", "balık"), A("−20 °C: dondurma ve balık", "dondurma"), A("0 °C: hiçbiri", "hiçbir"), A("+4 °C: süt", "süt")], "aralik")]},
        {"svg": Z.tablo_svg(["Bitki", "En düşük", "En yüksek"], [["Kaktüs", "−5 °C", "+45 °C"], ["Kardelen", "−20 °C", "+10 °C"], ["Muz", "+12 °C", "+35 °C"]], [130, 95, 95], etiket="Bitkilerin dayanabildiği sıcaklıklar"),
         "metin": ["Bir bahçe merkezi, üç bitkinin dayanabildiği örnek sıcaklık aralıklarını tabloda vermiştir."],
         "maddeler": [M("a", "−10 °C, 0 °C, +8 °C, +15 °C ve +40 °C sıcaklıklarının hangi bitkilerin dayanabildiği aralıkta olduğunu belirleyiniz.",
            "−10 °C: kardelen. 0 °C: kaktüs ve kardelen. +8 °C: kaktüs ve kardelen. +15 °C: kaktüs ve muz. +40 °C: yalnız kaktüs.",
            [A("−10 °C: yalnız kardelen", "kardelen"), A("+15 °C: kaktüs ve muz", "muz"), A("+40 °C: yalnız kaktüs", "kaktüs")], "aralik")]}])

Y.meb(id="m2", no=2, kazanim=KA, oncelik=3,
    metin=["1. Türkiye'nin en yüksek dağı olan Ağrı Dağı'nın zirvesi, deniz seviyesinin yaklaşık 5137 metre üzerindedir.",
           "2. Mariana Çukuru'ndaki Challenger Derinliği, deniz seviyesinin yaklaşık 10 935 metre altındadır.",
           "3. Erzurum'da bir kış günü hava sıcaklığı sıfırın altında 25 °C olarak ölçülmüştür.",
           "4. İstanbul'daki Çamlıca Kulesi'nin yüksekliği, bulunduğu zeminden itibaren 369 metredir."],
    maddeler=[Q(M("a", "Yukarıda verilen gerçek yaşam durumlarını uygun tam sayılarla ifade ediniz.",
        "1. +5137 (deniz seviyesinin üstü). 2. −10 935 (deniz seviyesinin altı). 3. −25 (sıfırın altı). 4. +369 (zeminden yukarı).",
        [A("1. +5137", "+5137"), A("2. −10 935", "-10 935", "-10935", "-10.935"), A("3. −25", "-25"), A("4. +369", "+369")], "gercek"),
        ["gerçek yaşam durumlarını", "uygun tam sayılarla"], "Üstü/yukarı → +, altı → −. Her duruma işaretli sayı yaz.",
        B("+5137 · −10 935 · −25 · +369", "+5137 · −10 935 · −25 · +369", "5137 · 10 935 · 25 · 369", "−5137 · +10 935 · +25 · −369",
        "Her durumda “üstü” mü, “altı” mı yazıyor?", "Deniz seviyesinin, sıfırın ya da zeminin üstü pozitif, altı negatif tam sayıyla gösterilir. (s. 20)",
        P("1. Ağrı Dağı, deniz seviyesinin üzeri:", "+5137", ["−5137", "−5,137"], k=["+5137"]),
        P("2. Challenger Derinliği, deniz seviyesinin altı:", "−10 935", ["+10 935", "10 935"], k=["-10 935", "-10935", "-10.935"]),
        P("3. Erzurum, sıfırın altı:", "−25", ["+25", "25"], k=["-25"]),
        P("4. Çamlıca Kulesi, zeminden yukarı:", "+369", ["−369", "−36"], k=["+369"])))],
    ikizler=[
        {"metin": ["Ece, gün içinde karşılaştığı bazı durumları defterine şöyle yazmıştır:", "1. Termometre sıfırın 6 °C altını gösterdi.", "2. Otoparkta araç zemin katın 3 kat üstüne çıktı.",
                   "3. Banka hesabına 450 TL para yatırıldı.", "4. Dalgıç, deniz seviyesinin 18 metre altına indi.", "5. Bir yarışmacı oyunda 20 puan kaybetti."],
         "maddeler": [M("a", "Bu durumların her birini uygun bir tam sayı ile gösteriniz.", "1. −6  2. +3  3. +450  4. −18  5. −20",
            [A("−6", "-6"), A("+3", "+3"), A("+450", "+450"), A("−18", "-18"), A("−20", "-20")], "gercek")]},
        {"metin": ["1. Bir maden ocağının tabanı, deniz seviyesinin 430 metre altındadır.", "2. Bir uçak, deniz seviyesinin 9000 metre üstünde uçuyor.",
                   "3. Bir dükkân bu ay 150 TL zarar etti.", "4. Ulaşım kartına 200 TL yüklendi."],
         "maddeler": [M("a", "Verilen durumları uygun tam sayılarla ifade ediniz.", "1. −430  2. +9000  3. −150  4. +200",
            [A("−430", "-430"), A("+9000", "+9000", "+9 000"), A("−150", "-150"), A("+200", "+200")], "gercek")]}])

Y.meb(id="m3", no=3, kazanim=KE, oncelik=1, svg=Z.hesap_makinesi("1,233333333333"),
    metin=["Fatih, hesap makinesinde bir doğal sayıyı sıfırdan farklı bir doğal sayıya bölmüştür. Sonucun devirli ondalık gösterimi hesap makinesinin ekranında görülmektedir."],
    maddeler=[Q(M("a", "Bu bölme işleminde kullanılabilecek bölünen ve bölen doğal sayıların toplamı en az kaçtır?",
        "Ekrandaki sayı 1,2[[d:3]]. Kesre çevirelim: (123 − 12) / 90 = [[111/90]]. En az değer istendiği için en sade hâl: [[111/90]] = [[37/30]] (3 ile sadeleşir). Bölünen 37, bölen 30. Toplam 37 + 30 = 67.",
        [A("Kesre çevirme: 111/90", "111/90"), A("En sade hâl: 37/30", "37/30"), A("Toplam: 67", "67")], "devir"),
        ["toplamı en az", "bölünen ve bölen"], "Devirli → kesir, en sade hâl, sonra pay + payda.",
        B("1,2[[d:3]] = [[111/90]] = [[37/30]] → 37 + 30 = 67", "1,2[[d:3]] = [[111/90]] = [[37/30]] → 37 + 30 = 67", "1,2[[d:3]] = [[111/90]] → 111 + 90 = 201", "1,2[[d:3]] = [[123/100]] → 123 + 100 = 223",
        "“En az” kelimesi kesirle ilgili ne istiyor?", "Devirli sayı (123 − 12) / 90 ile kesre çevrilir; “en az” için en sade hâl alınır: [[37/30]]. (s. 46)",
        P("Kesre çevir: (123 − 12) / 90 =", "111/90", ["123/90", "111/99"], k=["111/90"]),
        P("En sade hâli (3 ile sadeleştir):", "37/30", ["111/90", "37/33"], k=["37/30"]),
        P("Bölünen + bölen:", "67", ["201", "76"], k=["67"])))],
    ikizler=[
        {"metin": ["2,75 = △/□ eşitliğinde △ ve □ birer pozitif tam sayıdır."],
         "maddeler": [M("a", "Buna göre △ + □ işleminin sonucunun alabileceği en küçük değer kaçtır?",
            "2,75 = [[275/100]] = [[11/4]] (25 ile sadeleşir). En küçük değer için en sade hâl: △ = 11, □ = 4. △ + □ = 15.",
            [A("2,75 = 275/100", "275/100"), A("En sade: 11/4", "11/4"), A("Toplam: 15", "15")], "devir")]},
        {"metin": ["1,[[d:3]] = A/3 ve 2,[[d:7]] = B/9 eşitlikleri veriliyor."],
         "maddeler": [M("a", "Devirli sayıları kesre çevirerek A ve B değerlerini bulunuz.",
            "1,[[d:3]] = (13 − 1) / 9 = [[12/9]] = [[4/3]], yani A = 4. 2,[[d:7]] = (27 − 2) / 9 = [[25/9]], yani B = 25.",
            [A("12/9 = 4/3", "12/9", "4/3"), A("A = 4", "a = 4", "a=4"), A("25/9", "25/9"), A("B = 25", "b = 25", "b=25")], "devir"),
                      M("b", "Buna göre A + B toplamı kaçtır?", "A + B = 4 + 25 = 29.", [A("4 + 25", "4 + 25", "4+25"), A("29", "29")], "islem")]}])

T4 = Z.tablo_svg(["Makine", "Kütle", "Hedefe göre", "Hata miktarı"],
                 [["1. Makine", "496 g", "4 g eksik", "|−4| = 4"], ["2. Makine", "502 g", "", ""], ["3. Makine", "499 g", "", ""], ["4. Makine", "493 g", "", ""], ["5. Makine", "501 g", "", ""]],
                 [86, 66, 94, 86], etiket="Makinelere göre paketlerin hedef kütle ile karşılaştırılması")
Y.meb(id="m4", no=4, kazanim=KB, oncelik=3, svg=T4,
    metin=["Çay üretimi yapan bir fabrikada 5 adet çay paketleme makinesi vardır. Görevli, her makineden rastgele seçtiği bir çay paketini hassas terazi ile tartmış, paketlerin kütlelerini hedef kütle ile karşılaştırmış ve hata miktarlarını belirlemek için tabloyu hazırlamıştır."],
    maddeler=[
        Q(M("a", "Bir çay paketinin hedef kütlesini gram cinsinden bulunuz.", "1. makinenin paketi 496 g ve hedeften 4 g eksik. Eksik olanı ekleriz: 496 + 4 = 500 g.",
            [A("İşlem: 496 + 4", "496+4", "496 + 4", "4+496", "4 + 496"), A("Hedef: 500 g", "500")], "islem"),
          ["hedef kütlesini", "gram cinsinden"], "Eksikse ekle: kütle + eksik = hedef.",
          B("496 + 4 = 500 g", "496 + 4 = 500 g", "500", "496 − 4 = 492 g", "1. paket hedeften eksik mi, fazla mı?", "Paket hedeften eksikse eksik olan miktar eklenir. (MEB örnek sorusu)",
            P("Eksik olanı ekle:", "496 + 4", ["496 − 4", "500 + 4"], k=["496+4", "496 + 4", "4+496", "4 + 496"]),
            P("Hedef kütle:", "500 g", ["492 g", "504 g"], k=["500"]))),
        Q(M("b", "Tablodaki boşlukları örnekteki gibi doldurunuz.", "2. Makine: 2 g fazla, |+2| = 2. 3. Makine: 1 g eksik, |−1| = 1. 4. Makine: 7 g eksik, |−7| = 7. 5. Makine: 1 g fazla, |+1| = 1.",
            [A("2. makine: 2 g fazla, hata 2", "2 g fazla", "2g fazla", "2 gram fazla"), A("3. makine: 1 g eksik, hata 1", "1 g eksik", "1g eksik", "1 gram eksik"),
             A("4. makine: 7 g eksik, hata 7", "7 g eksik", "7g eksik", "7 gram eksik"), A("5. makine: 1 g fazla, hata 1", "1 g fazla", "1g fazla", "1 gram fazla")], "islem"),
          ["boşlukları", "örnekteki gibi"], "Kütle − 500: eksi çıkarsa eksik, artı çıkarsa fazla; hata = mutlak değer.",
          B("2 g fazla |+2| = 2 · 1 g eksik |−1| = 1 · 7 g eksik |−7| = 7 · 1 g fazla |+1| = 1",
            "2 g fazla |+2| = 2 · 1 g eksik |−1| = 1 · 7 g eksik |−7| = 7 · 1 g fazla |+1| = 1", "2 g fazla · 1 g eksik · 7 g eksik · 1 g fazla",
            "2 g fazla |+2| = 2 · 1 g eksik |−1| = −1 · 7 g eksik |−7| = −7 · 1 g fazla |+1| = 1",
            "Hata miktarı negatif olabilir mi?", "Hata miktarı hedefe olan uzaklıktır; mutlak değer olduğu için negatif olamaz. (s. 37)",
            P("2. Makine (502 g):", "2 g fazla, |+2| = 2", ["2 g eksik, |−2| = 2", "4 g fazla"], k=["2 g fazla", "2g fazla", "2 gram fazla"]),
            P("3. Makine (499 g):", "1 g eksik, |−1| = 1", ["1 g fazla", "9 g eksik"], k=["1 g eksik", "1g eksik", "1 gram eksik"]),
            P("4. Makine (493 g):", "7 g eksik, |−7| = 7", ["7 g fazla", "3 g eksik"], k=["7 g eksik", "7g eksik", "7 gram eksik"]),
            P("5. Makine (501 g):", "1 g fazla, |+1| = 1", ["1 g eksik", "5 g fazla"], k=["1 g fazla", "1g fazla", "1 gram fazla"]))),
        Q(M("c", "Bu kontrolün sonuçlarına göre hata miktarı en az olan makine veya makineleri belirleyiniz. Cevabınızı matematiksel gerekçeleriyle açıklayınız.",
            "3. ve 5. makineler. Hata miktarları 4, 2, 1, 7 ve 1 g; en küçüğü 1 g. 3. makinenin paketi 1 g eksik, 5. makinenin paketi 1 g fazla; yönleri farklı olsa da 500 g'a uzaklıkları aynı: |−1| = |+1| = 1.",
            [A("3. makine", "3."), A("5. makine", "5."), A("Hata 1 g, en küçük", "1 g", "1g", "en küçük", "en az"), A("Eksik/fazla farklı ama uzaklık eşit", "uzaklı", "mutlak", "aynı", "eşit")], "gerekce"),
          ["hata miktarı en az", "matematiksel gerekçeleriyle"], "Seçim + gerekçe: “… makine(ler), çünkü hata …”",
          B("3. ve 5. makineler; ikisinin hatası da 1 g, en küçük.", "3. ve 5. makineler; ikisinin hatası da 1 g, en küçük.", "3. makine.", "4. makine, çünkü kütlesi en az (493 g).",
            "“Makine veya makineleri” diyor; hata miktarı en küçük olan kaç makine var?", "Hata miktarı mutlak değerdir: 1 g eksik ile 1 g fazla aynı hatadır. (MEB örnek sorusu)",
            P("Makineler:", "3. ve 5.", ["yalnız 3.", "4."], hepsi=[["3."], ["5."]]),
            P("Gerekçe, hata miktarları:", "1 g, en küçük", ["7 g, en büyük", "eksik olduğu için"], k=["1 g", "1g", "en küçük", "en az"]),
            P("Biri eksik biri fazla ama 500 g'a", "uzaklıkları eşit", ["farklı", "biri daha az"], k=["eşit", "aynı"])))],
    ikizler=[
        {"svg": Z.tablo_svg(["Şişe", "Hacim", "Hedefe göre", "Hata"], [["1. şişe", "995 mL", "5 mL eksik", "|−5| = 5"], ["2. şişe", "1004 mL", "", ""], ["3. şişe", "990 mL", "", ""], ["4. şişe", "997 mL", "", ""], ["5. şişe", "1003 mL", "", ""]], [70, 76, 96, 82], etiket="Su şişeleri"),
         "metin": ["Bir su fabrikasında şişelerin hedef hacmi kontrol ediliyor. 1. şişe 995 mL ve hedeften 5 mL eksik."],
         "maddeler": [
            M("a", "Şişelerin hedef hacmini bulunuz.", "995 + 5 = 1000 mL.", [A("995 + 5", "995+5", "995 + 5"), A("1000 mL", "1000")], "islem"),
            M("b", "2., 3., 4. ve 5. şişelerin hedefe göre durumunu ve hata miktarını yazınız.", "2. şişe: 4 mL fazla, hata 4. 3. şişe: 10 mL eksik, hata 10. 4. şişe: 3 mL eksik, hata 3. 5. şişe: 3 mL fazla, hata 3.",
              [A("2. şişe: 4 mL fazla", "4 ml fazla", "4ml fazla"), A("3. şişe: 10 mL eksik", "10 ml eksik", "10ml eksik"), A("4. şişe: 3 mL eksik", "3 ml eksik", "3ml eksik"), A("5. şişe: 3 mL fazla", "3 ml fazla", "3ml fazla")], "islem"),
            M("c", "Hata miktarı en az olan şişe veya şişeler hangileridir? Gerekçesiyle açıklayınız.", "4. ve 5. şişeler. İkisinin de hata miktarı 3 mL, en küçük: |−3| = |+3| = 3.",
              [A("4. şişe", "4."), A("5. şişe", "5."), A("Hata 3 mL, en küçük", "3 ml", "3ml", "en küçük", "en az")], "gerekce")]},
        {"svg": Z.tablo_svg(["Ekmek", "Kütle", "Hedefe göre", "Hata"], [["1. ekmek", "254 g", "4 g fazla", "|+4| = 4"], ["2. ekmek", "247 g", "", ""], ["3. ekmek", "252 g", "", ""], ["4. ekmek", "245 g", "", ""], ["5. ekmek", "248 g", "", ""]], [76, 66, 96, 82], etiket="Ekmekler"),
         "metin": ["Bir fırında ekmeklerin kütlesi kontrol ediliyor. 1. ekmek 254 g ve hedef kütleden 4 g fazla."],
         "maddeler": [
            M("a", "Ekmeklerin hedef kütlesini bulunuz.", "Fazla olanı çıkarırız: 254 − 4 = 250 g.", [A("254 − 4", "254-4", "254 - 4"), A("250 g", "250")], "islem"),
            M("b", "2., 3., 4. ve 5. ekmeklerin hedefe göre durumunu ve hata miktarını yazınız.", "2. ekmek: 3 g eksik, hata 3. 3. ekmek: 2 g fazla, hata 2. 4. ekmek: 5 g eksik, hata 5. 5. ekmek: 2 g eksik, hata 2.",
              [A("2. ekmek: 3 g eksik", "3 g eksik", "3g eksik"), A("3. ekmek: 2 g fazla", "2 g fazla", "2g fazla"), A("4. ekmek: 5 g eksik", "5 g eksik", "5g eksik"), A("5. ekmek: 2 g eksik", "2 g eksik", "2g eksik")], "islem"),
            M("c", "Hata miktarı en az olan ekmek veya ekmekler hangileridir? Gerekçesiyle açıklayınız.", "3. ve 5. ekmekler. Biri 2 g fazla, biri 2 g eksik ama ikisinin de hata miktarı 2 g, en küçük.",
              [A("3. ekmek", "3."), A("5. ekmek", "5."), A("Hata 2 g, en küçük", "2 g", "2g", "en küçük", "en az")], "gerekce")]}])

Y.meb(id="m5", no=5, kazanim=KD, oncelik=2, svg=Z.tahta_kesir(["7/20", "−11/18", "15/24", "9/35"], "Dört farklı rasyonel sayı"),
    metin=["Tabloda dört farklı rasyonel sayı verilmiştir: [[7/20]], [[-11/18]], [[15/24]], [[9/35]]."],
    maddeler=[Q(M("a", "Bu sayıların en sade hâllerinin paydalarını inceleyerek ondalık gösterimlerinin sonlu mu yoksa devirli mi olduğunu matematiksel gerekçeleriyle açıklayınız.",
        "En sade hâlin paydasında 2 ve 5 dışında asal çarpan yoksa sonlu, varsa devirlidir. [[7/20]]: 20 = 2 · 2 · 5 → sonlu. [[-11/18]]: 18 = 2 · 3 · 3, 3 var → devirli. [[15/24]] = [[5/8]]: 8 = 2 · 2 · 2 → sonlu. [[9/35]]: 35 = 5 · 7, 7 var → devirli.",
        [A("Kural: paydada yalnız 2 ve 5 → sonlu", "2 ve 5", "2 veya 5", "2 ile 5"), A("7/20 ve 15/24 sonlu", "sonlu"), A("−11/18 ve 9/35 devirli", "devirli"), A("15/24 = 5/8 (önce sadeleştirme)", "5/8")], "sonlu"),
        ["en sade hâllerinin paydalarını", "sonlu mu yoksa devirli mi", "matematiksel gerekçeleriyle"], "Sadeleştir → paydayı çarpanlarına ayır → yalnız 2 ve 5 ise sonlu.",
        B("Paydada yalnız 2 ve 5 varsa sonlu. [[7/20]] sonlu · [[-11/18]] devirli (3) · [[15/24]] = [[5/8]] sonlu · [[9/35]] devirli (7)",
          "Paydada yalnız 2 ve 5 varsa sonlu. [[7/20]] sonlu · [[-11/18]] devirli (3) · [[15/24]] = [[5/8]] sonlu · [[9/35]] devirli (7)",
          "[[7/20]] ve [[15/24]] sonlu; [[-11/18]] ve [[9/35]] devirli.", "Payda çift sayıysa sonlu: [[7/20]], [[-11/18]], [[15/24]] sonlu; [[9/35]] devirli.",
          "Gerekçe nerede? Paydaların çarpanları yazılmış mı?", "Gerekçe = en sade hâlin paydasındaki asal çarpanlar. 18 çift olduğu hâlde 3 çarpanı yüzünden devirlidir. (s. 43)",
          P("Kural: paydada yalnız", "2 ve 5 varsa sonlu", ["3 ve 7 varsa sonlu", "çift sayı varsa sonlu"], k=["2 ve 5", "2 veya 5", "2 ile 5"]),
          P("[[7/20]] → payda 20 = 2 · 2 · 5 →", "sonlu", ["devirli", "tanımsız"], k=["sonlu"]),
          P("[[-11/18]] → payda 18 = 2 · 3 · 3 →", "devirli", ["sonlu", "tanımsız"], k=["devirli"]),
          P("[[15/24]] önce sadeleşir:", "5/8", ["3/8", "5/12"], k=["5/8"]),
          P("[[9/35]] → payda 35 = 5 · 7 →", "devirli", ["sonlu", "tanımsız"], k=["devirli"])))],
    ikizler=[
        {"metin": ["Aşağıda dört rasyonel sayı verilmiştir: [[3/8]], [[5/12]], [[21/30]], [[4/15]]."],
         "maddeler": [M("a", "Bu sayıların ondalık gösterimlerinin sonlu mu devirli mi olduğunu gerekçeleriyle yazınız.",
            "[[3/8]]: 8 = 2 · 2 · 2 → sonlu. [[5/12]]: 12 = 2 · 2 · 3, 3 var → devirli. [[21/30]] = [[7/10]]: 10 = 2 · 5 → sonlu. [[4/15]]: 15 = 3 · 5, 3 var → devirli.",
            [A("3/8 sonlu, 21/30 = 7/10 sonlu", "sonlu"), A("5/12 ve 4/15 devirli (3 çarpanı)", "devirli"), A("21/30'u sadeleştirme: 7/10", "7/10")], "sonlu")]},
        {"metin": ["Bir tarifte [[9/10]] kg elma kullanılmıştır. Bir yürüyüş parkurunun uzunluğu [[3 24/100]] km'dir. Bir sürahide [[2375/1000]] L meyve suyu vardır."],
         "maddeler": [
            M("a", "Verilen rasyonel sayıları ondalık gösterimle ifade ediniz.", "[[9/10]] = 0,9 kg. [[3 24/100]] = 3,24 km. [[2375/1000]] = 2,375 L.",
              [A("0,9", "0,9"), A("3,24", "3,24"), A("2,375", "2,375")], "islem"),
            M("b", "Bu sayıların ondalık gösterimleri neden sonludur? Paydalarına bakarak açıklayınız.", "Paydalar 10, 100 ve 1000; bunların asal çarpanları yalnız 2 ve 5 olduğu için ondalık gösterimler sonludur.",
              [A("Paydalar 10, 100, 1000", "10", "100"), A("Yalnız 2 ve 5 çarpanı", "2 ve 5", "2 ile 5")], "sonlu")]}])

T6 = Z.tablo_svg(["Sayı", "Doğal", "Tam", "Rasyonel"], [[x, "", "", ""] for x in ["21/4", "−5", "−1,8", "12/4", "0/9", "−7/7", "3/0"]],
                 [70, 80, 80, 90], etiket="Doğal sayı, tam sayı, rasyonel sayı tablosu", sat_h=34)
Y.meb(id="m6", no=6, kazanim=KC, oncelik=2, svg=T6,
    metin=["Tabloda yedi ifade var: [[21/4]], −5, −1,8, [[12/4]], [[0/9]], [[-7/7]], [[3/0]]."],
    maddeler=[Q(M("a", "Tablodaki ifadelerin doğal sayı, tam sayı veya rasyonel sayı belirtip belirtmediğini ilgili kutucukları “✓” ile işaretleyiniz. (Her satır için sayıları yaz.)",
        "Önce sadeleştir: [[12/4]] = 3, [[0/9]] = 0, [[-7/7]] = −1. Doğal sayı: [[12/4]] ve [[0/9]]. Tam sayı: −5, [[12/4]], [[0/9]], [[-7/7]]. Rasyonel sayı: [[3/0]] dışında hepsi. [[3/0]] paydası 0 olduğu için tanımsızdır, hiçbir satıra ✓ konmaz.",
        [A("Doğal: 12/4 ve 0/9", "0/9"), A("Tam: −5 ve −7/7 de", "-7/7"), A("Rasyonel: 3/0 dışında hepsi", "dışında", "hariç"), A("3/0 tanımsız", "tanımsız", "hiçbir")], "gerekce"),
        ["doğal sayı, tam sayı veya rasyonel sayı", "“✓” ile işaretleyiniz"], "Önce sadeleştir (12/4 = 3); her doğal tam, her tam rasyonel; payda 0 → tanımsız.",
        B("Doğal: [[12/4]], [[0/9]] · Tam: −5, [[12/4]], [[0/9]], [[-7/7]] · Rasyonel: [[3/0]] dışında hepsi · [[3/0]] tanımsız",
          "Doğal: [[12/4]], [[0/9]] · Tam: −5, [[12/4]], [[0/9]], [[-7/7]] · Rasyonel: [[3/0]] dışında hepsi · [[3/0]] tanımsız",
          "Rasyonel: [[3/0]] dışında hepsi.", "Doğal: [[12/4]], [[0/9]] · Tam: yalnız −5 · Rasyonel: yalnız kesirler, [[3/0]] de",
          "Her doğal sayı aynı zamanda tam sayı mıdır?", "Önce sadeleştirilir; her doğal sayı tam sayı, her tam sayı rasyonel sayıdır; paydası 0 olan ifade tanımsızdır. (s. 28, 30)",
          P("Doğal sayı:", "[[12/4]] ve [[0/9]]", ["−5 ve [[0/9]]", "[[21/4]] ve [[12/4]]"], hepsi=[["12/4"], ["0/9"]]),
          P("Tam sayı:", "−5, [[12/4]], [[0/9]], [[-7/7]]", ["[[12/4]], [[0/9]]", "−5, −1,8, [[12/4]]"], hepsi=[["-5"], ["12/4"], ["0/9"], ["7/7"]]),
          P("Rasyonel sayı:", "[[3/0]] dışında hepsi", ["hepsi, [[3/0]] de", "yalnız kesirler"], k=["dışında", "hariç"]),
          P("[[3/0]]:", "tanımsız (payda 0 olamaz)", ["0", "rasyonel"], k=["tanımsız", "hiçbir"])))],
    ikizler=[
        {"metin": ["Aşağıda dört farklı sayı hakkında bilgiler verilmiştir. Her açıklamaya uygun bir sayı örneği yazınız."],
         "maddeler": [
            M("a", "Rasyonel sayı olan fakat tam sayı olmayan negatif bir sayı ile tam sayı olan fakat doğal sayı olmayan bir sayı yazınız.",
              "Örnek: [[-1/2]] (rasyonel, tam değil, negatif) ve −3 (tam sayı ama negatif olduğu için doğal değil).",
              [A("Negatif kesir ya da ondalık (ör. −1/2, −0,5)", "/", "-0,", "-1,", "-2,"), A("Negatif tam sayı (ör. −3)", "-")], "gerekce"),
            M("b", "Doğal, tam ve rasyonel sayı kümelerinin üçünün de elemanı olan bir sayı ile a/b biçiminde yazılmış ancak rasyonel sayı belirtmeyen bir ifade yazınız.",
              "Örnek: 5 (doğal, tam ve rasyonel). [[7/0]] (paydası 0 olduğu için tanımsız, rasyonel değil).",
              [A("Doğal sayı (ör. 5, 0)", "5", "0", "1", "2", "3"), A("Paydası 0 olan ifade (ör. 7/0)", "/0")], "gerekce")]},
        {"metin": ["Sayılar: [[15/3]], −8, 2,5, [[0/4]], [[-12/6]], [[5/0]]"],
         "maddeler": [M("a", "Bu sayılardan doğal sayı, tam sayı ve rasyonel sayı olanları ayrı ayrı yazınız.",
            "Önce sadeleştir: [[15/3]] = 5, [[0/4]] = 0, [[-12/6]] = −2. Doğal: [[15/3]] ve [[0/4]]. Tam: [[15/3]], −8, [[0/4]], [[-12/6]]. Rasyonel: [[5/0]] dışında hepsi. [[5/0]] tanımsız.",
            [A("Doğal: 15/3 ve 0/4", "0/4"), A("Tam: −8 ve −12/6 de", "12/6"), A("Rasyonel: 5/0 dışında hepsi", "dışında", "hariç"), A("5/0 tanımsız", "tanımsız")], "gerekce")]}])

Y.meb(id="m7", no=7, kazanim=KD, oncelik=1, svg=Z.tahta_kesir(["?/35"], "Rasyonel sayı"),
    metin=["Tahtada ?/35 rasyonel sayısı yazılıdır."],
    maddeler=[Q(M("a", "Yukarıdaki rasyonel sayının sonlu ondalık gösterime sahip olması için ? yerine yazılabilecek tam sayıların ortak özelliğini matematiksel gerekçeleriyle açıklayınız.",
        "35 = 5 · 7. Sonlu ondalık gösterim için sadeleştirmeden sonra paydada 2 ve 5 dışında çarpan kalmamalı, yani 7 sadeleşip gitmeli. Bu yüzden ? yerine 7'nin katı olan bir tam sayı yazılmalıdır.",
        [A("35 = 5 · 7", "5 · 7", "5·7", "5.7", "5x7", "5 x 7", "5 ve 7", "7 · 5", "7x5"), A("Paydada 7 kalmamalı (sadeleşmeli)", "7 kalmamalı", "7 olmamalı", "sadeleş", "7 gitmeli", "kalmamalı"),
         A("? 7'nin katı olmalı", "7'nin kat", "7 nin kat", "7nin kat", "7’nin kat", "7 ile bölün")], "sonlu"),
        ["sonlu ondalık gösterime", "ortak özelliğini", "matematiksel gerekçeleriyle"], "Paydayı çarpanlara ayır; 2 ve 5 dışındaki çarpan payla sadeleşmeli.",
        B("35 = 5 · 7. Paydada 7 kalmamalı; ? 7'nin katı olmalı.", "35 = 5 · 7. Paydada 7 kalmamalı; ? 7'nin katı olmalı.", "? 7'nin katı olmalı.", "? 5'in katı olmalı, çünkü 35, 5 ile biter.",
          "Gerekçe = paydanın çarpanları ve hangisinin gitmesi gerektiği.", "Sonlu için en sade hâlin paydasında yalnız 2 ve 5 kalmalı; 7 ancak pay 7'nin katıysa sadeleşir. (s. 43)",
          P("35'in asal çarpanları:", "5 · 7", ["3 · 5", "5 · 5"], k=["5 · 7", "5·7", "5.7", "5x7", "5 x 7", "5 ve 7", "7 · 5", "7x5"]),
          P("Sonlu olması için paydada", "7 kalmamalı", ["5 kalmamalı", "2 kalmamalı"], k=["7 kalmamalı", "7 olmamalı", "7 sadeleş", "7 gitmeli"]),
          P("Bu yüzden ?", "7'nin katı olmalı", ["5'in katı olmalı", "çift sayı olmalı"], k=["7'nin kat", "7 nin kat", "7nin kat", "7’nin kat", "7 ile bölün"])))],
    ikizler=[
        {"metin": ["Bir kartta ?/24 rasyonel sayısı yazılıdır."],
         "maddeler": [M("a", "Bu sayının ondalık gösteriminin sonlu olması için ? yerine yazılabilecek tam sayıların ortak özelliğini gerekçesiyle açıklayınız.",
            "24 = 2 · 2 · 2 · 3. Paydada 3 kalmamalı, sadeleşip gitmeli. Bu yüzden ? 3'ün katı olmalıdır (3, 6, 9…).",
            [A("24 = 2 · 2 · 2 · 3", "2 · 3", "2·3", "2x3", "2 x 3", "3 var", "3 çarpan"), A("Paydada 3 kalmamalı", "3 kalmamalı", "3 olmamalı", "sadeleş", "3 gitmeli"), A("? 3'ün katı", "3'ün kat", "3 ün kat", "3ün kat", "3’ün kat")], "sonlu")]},
        {"metin": ["Bir kartta ?/30 rasyonel sayısı yazılıdır."],
         "maddeler": [M("a", "Bu sayının sonlu ondalık gösterime sahip olması için ? yerine hangi tam sayılar yazılabilir? Ortak özelliklerini gerekçesiyle yazınız.",
            "30 = 2 · 3 · 5. 2 ve 5 sorun değil; 3 sadeleşip gitmeli. Bu yüzden ? 3'ün katı olmalıdır (3, 6, 9…).",
            [A("30 = 2 · 3 · 5", "2 · 3 · 5", "2·3·5", "2x3x5", "2 x 3 x 5", "3 var", "3 çarpan"), A("3 sadeleşmeli", "3 kalmamalı", "sadeleş", "3 gitmeli", "3 olmamalı"), A("? 3'ün katı", "3'ün kat", "3 ün kat", "3ün kat", "3’ün kat")], "sonlu")]}])

Y.meb(id="m8", no=8, kazanim=KC, oncelik=2, svg=Z.sayi_dogrusu_svg(-2, -1, 4, (1, "A"), "−2 ile −1 arası dört eş parça, A birinci çizgide"),
    metin=["Sayı doğrusunda −2 ile −1 arası dört eş parçaya bölünmüştür. A noktasına karşılık gelen rasyonel sayıyı bulmaları istendiğinde üç öğrenci şu cevapları vermiştir:",
           "Kerem: [[-1 3/4]]   Zeynep: [[-14/8]]   Arda: [[-21/12]]"],
    maddeler=[Q(M("a", "Bu öğrencilerden hangisi ya da hangileri doğru cevap vermiştir? Öğrencilerin cevaplarının doğruluğunu matematiksel gerekçeleriyle açıklayınız.",
        "A noktası −2'den 1 parça sağda: [[-1 3/4]] = [[-7/4]]. Kerem: [[-1 3/4]] = [[-7/4]], doğru. Zeynep: [[-14/8]] 2 ile sadeleşince [[-7/4]], doğru. Arda: [[-21/12]] 3 ile sadeleşince [[-7/4]], doğru. Üçü de doğru; pay ve paydaları farklı olsa da bu kesirler denktir, aynı sayıyı gösterir.",
        [A("Üçü de doğru", "üçü", "hepsi", "üç öğrenci"), A("A = −7/4", "7/4"), A("Gerekçe: sadeleştirince aynı (denk)", "sadeleş", "denk", "2 ile", "3 ile")], "gerekce"),
        ["hangisi ya da hangileri", "matematiksel gerekçeleriyle"], "Kim doğru + her cevabı sadeleştirip aynı sayıya ulaş.",
        B("Üçü de doğru: hepsi sadeleşince [[-7/4]] olur.", "Üçü de doğru: hepsi sadeleşince [[-7/4]] olur.", "Üçü de doğru.", "Yalnız Kerem doğru, çünkü pay ve paydası farklı kesirler farklı sayılardır.",
          "Zeynep ile Arda'nın kesirlerini sadeleştir.", "Denk kesirler sayı doğrusunda aynı noktaya karşılık gelir. (s. 27)",
          P("A noktası:", "[[-7/4]] (−2'den 1 parça sağda)", ["[[-5/4]]", "[[-1/4]]"], k=["-7/4", "-1 3/4"]),
          P("Kerem: [[-1 3/4]] =", "[[-7/4]]", ["[[-3/4]]", "[[-4/4]]"], k=["7/4"]),
          P("Zeynep: [[-14/8]] ÷ 2 =", "[[-7/4]]", ["[[-7/8]]", "[[-14/4]]"], k=["7/4"]),
          P("Arda: [[-21/12]] ÷ 3 =", "[[-7/4]]", ["[[-7/12]]", "[[-21/4]]"], k=["7/4"]),
          P("Sonuç:", "üçü de doğru", ["yalnız Kerem", "Kerem ve Zeynep"], k=["üçü", "hepsi", "üç öğrenci"])))],
    ikizler=[
        {"metin": ["[[-23/5]] rasyonel sayısı veriliyor."],
         "maddeler": [
            M("a", "Bu rasyonel sayının sayı doğrusu üzerinde hangi ardışık iki tam sayı arasında bulunduğunu belirleyiniz.", "[[-23/5]] = [[-4 3/5]] olduğu için −5 ile −4 arasındadır.",
              [A("Tam sayılı kesir: −4 3/5", "4 3/5"), A("−5 ile −4 arası", "-5", "-4")], "gerekce"),
            M("b", "Bu sayıyı sayı doğrusunda göstermek için −5 ile −4 arası kaç eş parçaya bölünür? Sayı −4'ten kaç parça soldadır?", "Payda 5 olduğu için 5 eş parçaya bölünür. Sayı −4'ten 3 parça soldadır.",
              [A("5 eş parça", "5 eş", "5 parça"), A("3 parça sola", "3 parça", "3 sol")], "islem")]},
        {"svg": Z.sayi_dogrusu_svg(-3, -2, 3, (2, "B"), "−3 ile −2 arası üç eş parça, B ikinci çizgide"),
         "metin": ["Sayı doğrusunda −3 ile −2 arası üç eş parçaya bölünmüştür. B noktası için öğrenciler şu cevapları vermiştir:", "Ali: [[-2 1/3]]   Su: [[-14/6]]   Can: [[-7/6]]"],
         "maddeler": [M("a", "Hangi öğrenci ya da öğrenciler doğru cevap vermiştir? Gerekçesiyle açıklayınız.",
            "Ali ve Su doğru, Can yanlış. B noktası −3'ten 2 parça sağda: [[-2 1/3]] = [[-7/3]]. Ali doğru. Su: [[-14/6]] 2 ile sadeleşince [[-7/3]], doğru. Can: [[-7/6]] = [[-1 1/6]], −2 ile −1 arasında; yanlış.",
            [A("Ali ve Su doğru", "ali ve su", "su ve ali"), A("Can yanlış", "can yanlış", "can'ın", "can ın"), A("B = −7/3", "7/3"), A("Gerekçe: sadeleştirme", "sadeleş", "denk", "2 ile")], "gerekce")]}])

Y.meb(id="m9", no=9, kazanim=KB, oncelik=3,
    metin=["Elif, aklından tuttuğu bir tam sayının mutlak değerinin 11 olduğunu belirtmiştir."],
    maddeler=[
        Q(M("a", "Elif'in aklından tutmuş olabileceği tam sayıları yazınız.", "Mutlak değeri 11 olan iki tam sayı vardır: −11 ve +11. |−11| = 11, |+11| = 11.",
            [A("−11", "-11"), A("+11", "+11", "11 ve", "ve 11")], "islem"),
          ["tam sayıları yazınız"], "Mutlak değer = 0'a uzaklık: iki sayı var (biri −, biri +).",
          B("−11 ve +11", "−11 ve +11", "+11", "−22 ve +22", "0'a 11 birim uzaklıkta kaç sayı var?", "0'ın solunda ve sağında 11 birim uzaklıkta birer sayı vardır. (s. 37)",
            P("Sıfırın solunda:", "−11", ["−1", "−22"], k=["-11"]),
            P("Sıfırın sağında:", "+11", ["+1", "+22"], k=["+11", "11"]))),
        Q(M("b", "Bu sayıların sayı doğrusundaki konumlarını düşünerek bu sayılara karşılık gelen noktalar arasındaki uzaklığın kaç birim olduğunu bulunuz.",
            "−11, 0'a 11 birim; +11 de 0'a 11 birim uzaklıktadır. İkisi 0'ın iki yanında olduğu için uzaklık 11 + 11 = 22 birimdir.",
            [A("11 + 11", "11+11", "11 + 11"), A("22 birim", "22")], "islem"),
          ["noktalar arasındaki uzaklığın", "kaç birim"], "Uzaklık: 0'ın iki yanındaysa iki parçayı topla.",
          B("11 + 11 = 22 birim", "11 + 11 = 22 birim", "22", "11 − 11 = 0 birim", "İki sayı 0'ın aynı tarafında mı?", "0'ın iki yanındaki sayılar arası uzaklık, 0'a uzaklıkların toplamıdır. (MEB örnek sorusu)",
            P("−11'den 0'a, 0'dan +11'e:", "11 + 11", ["11 − 11", "11 + 0"], k=["11+11", "11 + 11"]),
            P("Uzaklık:", "22 birim", ["0 birim", "11 birim"], k=["22"])))],
    ikizler=[
        {"metin": ["Kerem, sayı doğrusunda 0'a 7 birim uzaklıktaki tam sayıları arıyor."],
         "maddeler": [
            M("a", "Kerem'in bulabileceği tam sayıları yazınız.", "−7 ve +7; ikisinin de mutlak değeri 7'dir.", [A("−7", "-7"), A("+7", "+7", "7 ve", "ve 7")], "islem"),
            M("b", "Bu iki sayı arasındaki uzaklık kaç birimdir?", "7 + 7 = 14 birim.", [A("7 + 7", "7+7", "7 + 7"), A("14 birim", "14")], "islem")]},
        {"metin": ["(−5) ile (+6) arasındaki tam sayılar inceleniyor."],
         "maddeler": [
            M("a", "(−5) ile (+6) arasındaki tam sayıları yazınız.", "−4, −3, −2, −1, 0, 1, 2, 3, 4, 5 (−5 ve +6 dahil değil).",
              [A("−4'ten başlar", "-4"), A("0 dahil", "0"), A("5'te biter", "5")], "islem"),
            M("b", "Bu sayılardan mutlak değeri 4 olanları yazınız.", "−4 ve 4; ikisi de 0'a 4 birim uzaklıktadır.", [A("−4", "-4"), A("+4", "+4", "4 ve", "ve 4", " 4")], "islem")]}])

Y.meb(id="m10", no=10, kazanim=KF, oncelik=2,
    metin=["Bir öğretmen, öğrencilerinden [[-2/3]], [[-5/6]], [[1/2]], [[-7/3]] rasyonel sayılarını küçükten büyüğe doğru sıralamalarını istemiştir. Efe şu adımları izlemiştir:",
           "1. Adım: Yalnızca [[1/2]] pozitif olduğu için bu sayının diğerlerinden büyük olduğunu belirlemiştir.",
           "2. Adım: Diğer sayıların paydalarını 6'da eşitlemiştir: [[-2/3]] = [[-4/6]], [[-5/6]] = [[-5/6]], [[-7/3]] = [[-14/6]].",
           "3. Adım: Paydaları eşit olan negatif sayıları paylarına göre karşılaştırarak [[-4/6]] < [[-5/6]] < [[-14/6]] sıralamasını yapmıştır.",
           "4. Adım: Sayıları küçükten büyüğe [[-2/3]] < [[-5/6]] < [[-7/3]] < [[1/2]] diye sıralamıştır."],
    maddeler=[Q(M("a", "Efe'nin yaptığı sıralama doğru mudur? Yanlış ise ilk hatayı hangi adımda yaptığını matematiksel gerekçelerle açıklayınız ve rasyonel sayıların doğru sıralamasını yazınız.",
        "Efe'nin sıralaması yanlıştır. İlk hata 3. adımdadır: paydaları eşit negatif sayılarda payı büyük olan (mutlak değeri büyük olan) daha küçüktür: [[-14/6]] < [[-5/6]] < [[-4/6]]. Doğru sıralama: [[-7/3]] < [[-5/6]] < [[-2/3]] < [[1/2]].",
        [A("Yanlış", "yanlış"), A("İlk hata 3. adımda", "3."), A("Gerekçe: negatifte payı büyük olan küçük", "büyük olan küçük", "büyük olan daha küçük", "mutlak değeri büyük"),
         SIRA("Doğru sıra: −7/3 < −5/6 < −2/3 < 1/2", ["-7/3", "-14/6"], "-5/6", ["-2/3", "-4/6"], "1/2")], "hata"),
        ["doğru mudur", "hangi adımda", "doğru sıralamasını yazınız"], "Doğru mu? + hatalı adım + çünkü + doğru sıra (4 parça).",
        B("Yanlış; ilk hata 3. adımda: negatifte payı büyük olan küçüktür. Doğru sıra: [[-7/3]] < [[-5/6]] < [[-2/3]] < [[1/2]]",
          "Yanlış; ilk hata 3. adımda: negatifte payı büyük olan küçüktür. Doğru sıra: [[-7/3]] < [[-5/6]] < [[-2/3]] < [[1/2]]",
          "Yanlış. Doğru sıra: [[-7/3]] < [[-5/6]] < [[-2/3]] < [[1/2]]", "Doğru, çünkü payı küçük olan küçüktür: [[-4/6]] < [[-5/6]] < [[-14/6]].",
          "Soru dört şey istiyor: doğru mu, hangi adım, neden, doğru sıra.", "Negatiflerde 0'dan uzaklaştıkça değer küçülür; [[-14/6]] en soldadır. (s. 53)",
          P("Cevap:", "yanlış", ["doğru", "bilinmez"], k=["yanlış"]),
          P("İlk hata:", "3. adım", ["1. adım", "2. adım"], k=["3."]),
          P("Çünkü negatiflerde", "payı büyük olan küçüktür", ["payı büyük olan büyüktür", "paydası büyük olan büyüktür"], k=["büyük olan küçük", "büyük olan daha küçük", "mutlak değeri büyük olan küçük"]),
          P("Doğru sıra:", "[[-7/3]] < [[-5/6]] < [[-2/3]] < [[1/2]]", ["[[-2/3]] < [[-5/6]] < [[-7/3]] < [[1/2]]", "[[1/2]] < [[-2/3]] < [[-5/6]] < [[-7/3]]"], sira=[["-7/3", "-14/6"], ["-5/6"], ["-2/3", "-4/6"], ["1/2"]])))],
    ikizler=[
        {"metin": ["a = [[-5/4]], b = [[-7/6]], c = [[2/3]] rasyonel sayıları veriliyor."],
         "maddeler": [M("a", "Bu rasyonel sayıları küçükten büyüğe doğru sıralayınız.",
            "c tek pozitif sayı, en büyük. Paydaları 12'de eşitle: [[-5/4]] = [[-15/12]], [[-7/6]] = [[-14/12]]. Negatifte payı büyük olan küçük: [[-15/12]] < [[-14/12]]. Sıra: a < b < c, yani [[-5/4]] < [[-7/6]] < [[2/3]].",
            [A("Paydaları eşitleme (12)", "12"), SIRA("Sıra: a < b < c", ["a", "-5/4", "-15/12"], ["b", "-7/6", "-14/12"], ["c", "2/3"])], "hata")]},
        {"metin": ["Deniz, [[-3/4]], [[-5/8]], [[1/4]], [[-3/2]] sayılarını küçükten büyüğe sıralarken şu adımları izlemiştir:",
                   "1. Adım: [[1/4]] tek pozitif sayı olduğu için en büyüktür.", "2. Adım: Paydaları 8'de eşitlemiştir: [[-6/8]], [[-5/8]], [[-12/8]].",
                   "3. Adım: Payı büyük olan büyüktür diyerek [[-5/8]] < [[-6/8]] < [[-12/8]] yazmıştır.", "4. Adım: Sıralamayı [[-5/8]] < [[-3/4]] < [[-3/2]] < [[1/4]] diye yazmıştır."],
         "maddeler": [M("a", "Deniz'in sıralaması doğru mudur? Yanlışsa ilk hatanın hangi adımda olduğunu gerekçesiyle açıklayınız ve doğru sıralamayı yazınız.",
            "Yanlış. İlk hata 3. adımda: negatiflerde payı büyük olan küçüktür: [[-12/8]] < [[-6/8]] < [[-5/8]]. Doğru sıra: [[-3/2]] < [[-3/4]] < [[-5/8]] < [[1/4]].",
            [A("Yanlış", "yanlış"), A("3. adım", "3."), A("Negatifte payı büyük olan küçük", "büyük olan küçük", "büyük olan daha küçük", "mutlak değeri büyük"),
             SIRA("Doğru sıra: −3/2 < −3/4 < −5/8 < 1/4", ["-3/2", "-12/8"], ["-3/4", "-6/8"], "-5/8", "1/4")], "hata")]}])

Y.meb(id="m11", no=11, kazanim=KF, oncelik=1, svg=Z.tahta_defter(["−45/44", "−39/38", "−50/49"], ["−50/49", "−45/44", "−39/38"]),
    metin=["Bir öğretmen, öğrencilerinden tahtadaki [[-45/44]], [[-39/38]], [[-50/49]] rasyonel sayılarını küçükten büyüğe sıralamalarını istemiştir. Bir öğrenci defterine [[-50/49]] < [[-45/44]] < [[-39/38]] yazmıştır."],
    maddeler=[Q(M("a", "Öğrencinin defterine yazdığı sıralama doğru mudur? Cevabınızı matematiksel gerekçelerle açıklayınız.",
        "Sıralama yanlıştır. Sayıları tam sayılı kesre çevirelim: [[-45/44]] = [[-1 1/44]], [[-39/38]] = [[-1 1/38]], [[-50/49]] = [[-1 1/49]]. Tam kısımlar aynı; payları eşit kesirlerde paydası küçük olan büyüktür: [[1/38]] > [[1/44]] > [[1/49]]. Sayılar negatif olduğu için mutlak değeri büyük olan küçüktür. Doğru sıra: [[-39/38]] < [[-45/44]] < [[-50/49]].",
        [A("Yanlış", "yanlış"), A("Tam sayılı kesir: −1 1/44, −1 1/38, −1 1/49", "1 1/"), A("Negatifte mutlak değeri büyük olan küçük", "mutlak değeri büyük", "büyük olan küçük"),
         SIRA("Doğru sıra: −39/38 < −45/44 < −50/49", "-39/38", "-45/44", "-50/49")], "hata"),
        ["doğru mudur", "matematiksel gerekçelerle"], "Doğru mu? + tam sayılı kesre çevir (−1 ve kesir) + doğru sıra.",
        B("Yanlış. [[-1 1/38]] < [[-1 1/44]] < [[-1 1/49]]; doğru sıra: [[-39/38]] < [[-45/44]] < [[-50/49]]",
          "Yanlış. [[-1 1/38]] < [[-1 1/44]] < [[-1 1/49]]; doğru sıra: [[-39/38]] < [[-45/44]] < [[-50/49]]",
          "Yanlış.", "Doğru, çünkü payı büyük olan negatif sayı en küçüktür: 50 > 45 > 39.",
          "Sayıları tam sayılı kesre çevirince ne görüyorsun?", "Hepsi [[-1]] ile bir kesir: [[1/38]] en büyük kesir olduğu için [[-1 1/38]] en küçük sayıdır. (s. 57)",
          P("Cevap:", "yanlış", ["doğru", "bilinmez"], k=["yanlış"]),
          P("Tam sayılı kesir hâlleri:", "[[-1 1/44]], [[-1 1/38]], [[-1 1/49]]", ["[[-45 1/44]], [[-39 1/38]]", "[[-1 45/44]]"], hepsi=[["1 1/44"], ["1 1/38"], ["1 1/49"]]),
          P("Negatifte kesir kısmı büyük olan", "daha küçüktür", ["daha büyüktür", "eşittir"], k=["küçük"]),
          P("Doğru sıra:", "[[-39/38]] < [[-45/44]] < [[-50/49]]", ["[[-50/49]] < [[-45/44]] < [[-39/38]]", "[[-45/44]] < [[-39/38]] < [[-50/49]]"], sira=[["-39/38"], ["-45/44"], ["-50/49"]])))],
    ikizler=[
        {"svg": Z.tahta_defter(["−13/12", "−17/16", "−21/20"], ["−21/20", "−17/16", "−13/12"]),
         "metin": ["Tahtadaki [[-13/12]], [[-17/16]], [[-21/20]] sayılarını bir öğrenci [[-21/20]] < [[-17/16]] < [[-13/12]] diye sıralamıştır."],
         "maddeler": [M("a", "Öğrencinin sıralaması doğru mudur? Gerekçesiyle açıklayınız.",
            "Yanlış. [[-13/12]] = [[-1 1/12]], [[-17/16]] = [[-1 1/16]], [[-21/20]] = [[-1 1/20]]. [[1/12]] en büyük kesir, bu yüzden [[-1 1/12]] en küçük. Doğru sıra: [[-13/12]] < [[-17/16]] < [[-21/20]].",
            [A("Yanlış", "yanlış"), A("Tam sayılı kesir", "1 1/"), SIRA("Doğru sıra: −13/12 < −17/16 < −21/20", "-13/12", "-17/16", "-21/20")], "hata")]},
        {"svg": Z.tahta_defter(["8/7", "10/9", "13/12"], ["13/12", "10/9", "8/7"]),
         "metin": ["Tahtadaki [[8/7]], [[10/9]], [[13/12]] sayılarını bir öğrenci [[13/12]] < [[10/9]] < [[8/7]] diye sıralamıştır."],
         "maddeler": [M("a", "Öğrencinin sıralaması doğru mudur? Gerekçesiyle açıklayınız.",
            "Doğru. [[8/7]] = [[1 1/7]], [[10/9]] = [[1 1/9]], [[13/12]] = [[1 1/12]]. Pozitiflerde kesir kısmı büyük olan büyüktür: [[1/12]] < [[1/9]] < [[1/7]]. Sıra: [[13/12]] < [[10/9]] < [[8/7]].",
            [A("Doğru", "doğru"), A("Tam sayılı kesir", "1 1/"), A("Pozitifte kesir kısmı büyük olan büyük", "büyük olan büyük", "paydası küçük olan büyük")], "hata")]}])

# =====================================================================
# BENZER SORULAR (Konu Tekrarı): kısa cevap, tetik, kalıp notu, parçalar (sec YOK → doğrudan sınavdaki gibi yazma)
# =====================================================================
IKIZ = {
 ("m1i1", "a"): IK("−28: balık · −20: dondurma, balık · −15: dondurma · 0: hiçbiri · +4: süt", ["hangi ürünün", "Hiçbirinin aralığında"], "Her sıcaklık için aralık kontrolü; hiçbir aralıkta yoksa “hiçbiri”.",
    P("−28 °C:", "balık", ["dondurma", "süt"], k=["balık"]), P("−20 °C:", "dondurma ve balık", ["yalnız süt", "hiçbiri"], hepsi=[["dondurma"]]),
    P("0 °C:", "hiçbiri", ["süt", "dondurma"], k=["hiçbir"]), P("+4 °C:", "süt", ["balık", "dondurma"], k=["süt"])),
 ("m1i2", "a"): IK("−10: kardelen · 0 ve +8: kaktüs, kardelen · +15: kaktüs, muz · +40: kaktüs", ["hangi bitkilerin", "aralıkta olduğunu"], "Her sıcaklık için aralık kontrolü: en düşük ile en yüksek arasında mı?",
    P("−10 °C:", "kardelen", ["muz", "üçü de"], k=["kardelen"]), P("+15 °C:", "kaktüs ve muz", ["yalnız kardelen", "hiçbiri"], k=["muz"]),
    P("+40 °C:", "yalnız kaktüs", ["muz", "kardelen"], k=["kaktüs"])),
 ("m2i1", "a"): IK("−6 · +3 · +450 · −18 · −20", ["uygun bir tam sayı ile"], "Üstü/yatırıldı → +, altı/kaybetti → −.",
    P("1. Sıfırın altı:", "−6", ["+6", "6"], k=["-6"]), P("2. Zemin katın üstü:", "+3", ["−3", "−33"], k=["+3"]), P("3. Para yatırıldı:", "+450", ["−450", "−45"], k=["+450"]),
    P("4. Deniz seviyesinin altı:", "−18", ["+18", "18"], k=["-18"]), P("5. Puan kaybetti:", "−20", ["+20", "20"], k=["-20"])),
 ("m2i2", "a"): IK("−430 · +9000 · −150 · +200", ["uygun tam sayılarla"], "Altı/zarar → −, üstü/yüklendi → +.",
    P("1. Deniz seviyesinin altı:", "−430", ["+430", "430"], k=["-430"]), P("2. Deniz seviyesinin üstü:", "+9000", ["−9000", "−900"], k=["+9000", "+9 000"]),
    P("3. Zarar:", "−150", ["+150", "150"], k=["-150"]), P("4. Yüklendi:", "+200", ["−200", "−20"], k=["+200"])),
 ("m3i1", "a"): IK("2,75 = [[275/100]] = [[11/4]] → 11 + 4 = 15", ["en küçük değer"], "Ondalık → kesir, en sade hâl, sonra pay + payda.",
    P("2,75 kesir olarak:", "275/100", ["275/10", "27/5"], k=["275/100"]), P("En sade hâli:", "11/4", ["55/20", "11/5"], k=["11/4"]), P("△ + □:", "15", ["375", "16"], k=["15"])),
 ("m3i2", "a"): IK("1,[[d:3]] = [[12/9]] = [[4/3]] → A = 4 · 2,[[d:7]] = [[25/9]] → B = 25", ["A ve B değerlerini"], "Devirli → kesir: (tamamı − devretmeyen) / 9.",
    P("1,3… = (13 − 1) / 9 =", "12/9 = 4/3", ["13/9", "13/10"], hepsi=[["12/9", "4/3"]]), P("Bu yüzden A =", "4", ["13", "12"], k=["4"]),
    P("2,7… = (27 − 2) / 9 =", "25/9", ["27/9", "27/10"], k=["25/9"]), P("Bu yüzden B =", "25", ["27", "9"], k=["25"])),
 ("m3i2", "b"): IK("4 + 25 = 29", ["A + B toplamı"], "Bulduğun A ve B'yi topla.", P("A + B =", "4 + 25", ["13 + 27", "4 + 27"], k=["4 + 25", "4+25"]), P("Sonuç:", "29", ["40", "31"], k=["29"])),
 ("m4i1", "a"): IK("995 + 5 = 1000 mL", ["hedef hacmini"], "Eksikse ekle: hacim + eksik = hedef.",
    P("Eksik olanı ekle:", "995 + 5", ["995 − 5", "1000 + 5"], k=["995+5", "995 + 5"]), P("Hedef:", "1000 mL", ["990 mL", "1005 mL"], k=["1000"])),
 ("m4i1", "b"): IK("4 mL fazla · 10 mL eksik · 3 mL eksik · 3 mL fazla", ["hedefe göre durumunu", "hata miktarını"], "Hacim − 1000: eksi → eksik, artı → fazla; hata = mutlak değer.",
    P("2. şişe (1004 mL):", "4 mL fazla", ["4 mL eksik", "6 mL fazla"], k=["4 ml fazla", "4ml fazla"]), P("3. şişe (990 mL):", "10 mL eksik", ["10 mL fazla", "90 mL eksik"], k=["10 ml eksik", "10ml eksik"]),
    P("4. şişe (997 mL):", "3 mL eksik", ["3 mL fazla", "7 mL eksik"], k=["3 ml eksik", "3ml eksik"]), P("5. şişe (1003 mL):", "3 mL fazla", ["3 mL eksik", "8 mL fazla"], k=["3 ml fazla", "3ml fazla"])),
 ("m4i1", "c"): IK("4. ve 5. şişeler; ikisinin hatası da 3 mL, en küçük.", ["en az olan", "Gerekçesiyle"], "Seçim + gerekçe: en küçük hata miktarı.",
    P("Şişeler:", "4. ve 5.", ["yalnız 4.", "3."], hepsi=[["4."], ["5."]]), P("Gerekçe, hata:", "3 mL, en küçük", ["10 mL, en büyük", "eksik olduğu için"], k=["3 ml", "3ml", "en küçük", "en az"])),
 ("m4i2", "a"): IK("254 − 4 = 250 g", ["hedef kütlesini"], "Fazlaysa çıkar: kütle − fazla = hedef.",
    P("Fazla olanı çıkar:", "254 − 4", ["254 + 4", "250 − 4"], k=["254-4", "254 - 4"]), P("Hedef:", "250 g", ["258 g", "246 g"], k=["250"])),
 ("m4i2", "b"): IK("3 g eksik · 2 g fazla · 5 g eksik · 2 g eksik", ["hedefe göre durumunu", "hata miktarını"], "Kütle − 250: eksi → eksik, artı → fazla; hata = mutlak değer.",
    P("2. ekmek (247 g):", "3 g eksik", ["3 g fazla", "7 g eksik"], k=["3 g eksik", "3g eksik"]), P("3. ekmek (252 g):", "2 g fazla", ["2 g eksik", "6 g fazla"], k=["2 g fazla", "2g fazla"]),
    P("4. ekmek (245 g):", "5 g eksik", ["5 g fazla", "4 g eksik"], k=["5 g eksik", "5g eksik"]), P("5. ekmek (248 g):", "2 g eksik", ["2 g fazla", "8 g eksik"], k=["2 g eksik", "2g eksik"])),
 ("m4i2", "c"): IK("3. ve 5. ekmekler; ikisinin hatası da 2 g, en küçük.", ["en az olan", "Gerekçesiyle"], "Seçim + gerekçe: en küçük hata miktarı (eksik ya da fazla fark etmez).",
    P("Ekmekler:", "3. ve 5.", ["yalnız 3.", "4."], hepsi=[["3."], ["5."]]), P("Gerekçe, hata:", "2 g, en küçük", ["5 g, en büyük", "fazla olduğu için"], k=["2 g", "2g", "en küçük", "en az"])),
 ("m5i1", "a"): IK("[[3/8]] sonlu · [[5/12]] devirli (3) · [[21/30]] = [[7/10]] sonlu · [[4/15]] devirli (3)", ["sonlu mu devirli mi", "gerekçeleriyle"], "Sadeleştir → paydanın çarpanları → yalnız 2 ve 5 ise sonlu.",
    P("[[3/8]] → 8 = 2 · 2 · 2 →", "sonlu", ["devirli", "tanımsız"], k=["sonlu"]), P("[[5/12]] → 12 = 2 · 2 · 3 →", "devirli", ["sonlu", "tanımsız"], k=["devirli"]),
    P("[[21/30]] önce sadeleşir:", "7/10", ["21/10", "7/3"], k=["7/10"]), P("[[4/15]] → 15 = 3 · 5 →", "devirli", ["sonlu", "tanımsız"], k=["devirli"])),
 ("m5i2", "a"): IK("0,9 · 3,24 · 2,375", ["ondalık gösterimle"], "Payda 10 → 1 basamak, 100 → 2, 1000 → 3 basamak.",
    P("[[9/10]] =", "0,9", ["0,09", "9,10"], k=["0,9"]), P("[[3 24/100]] =", "3,24", ["3,024", "32,4"], k=["3,24"]), P("[[2375/1000]] =", "2,375", ["23,75", "0,2375"], k=["2,375"])),
 ("m5i2", "b"): IK("Paydalar 10, 100, 1000; çarpanları yalnız 2 ve 5, bu yüzden sonlu.", ["neden sonludur"], "Paydanın çarpanları + kural.",
    P("Paydalar:", "10, 100, 1000", ["3, 7, 11", "9, 99"], k=["10"]), P("Çarpanları yalnız", "2 ve 5", ["3 ve 7", "2 ve 3"], k=["2 ve 5", "2 ile 5"])),
 ("m6i1", "a"): IK("[[-1/2]] ve −3", ["tam sayı olmayan negatif", "doğal sayı olmayan"], "Her açıklamaya bir örnek: kümeleri düşün.",
    P("Rasyonel ama tam değil, negatif:", "[[-1/2]]", ["−3", "2"], k=["/", ","]), P("Tam sayı ama doğal değil:", "−3", ["3", "0"], k=["-"])),
 ("m6i1", "b"): IK("5 ve [[7/0]]", ["üçünün de elemanı", "rasyonel sayı belirtmeyen"], "Doğal sayı her kümede; paydası 0 olan tanımsız.",
    P("Üç kümede de:", "5", ["−4", "[[1/2]]"], k=["5", "0", "3", "7", "9"]), P("Rasyonel olmayan a/b:", "[[7/0]]", ["[[0/7]]", "[[7/1]]"], k=["/0"])),
 ("m6i2", "a"): IK("Doğal: [[15/3]], [[0/4]] · Tam: [[15/3]], −8, [[0/4]], [[-12/6]] · Rasyonel: [[5/0]] dışında hepsi · [[5/0]] tanımsız", ["doğal sayı, tam sayı ve rasyonel sayı"], "Önce sadeleştir; doğal ⊂ tam ⊂ rasyonel; payda 0 → tanımsız.",
    P("Doğal sayı:", "[[15/3]] ve [[0/4]]", ["−8 ve [[0/4]]", "2,5 ve [[15/3]]"], hepsi=[["15/3"], ["0/4"]]),
    P("Tam sayı:", "[[15/3]], −8, [[0/4]], [[-12/6]]", ["yalnız −8", "−8, 2,5"], hepsi=[["15/3"], ["-8"], ["0/4"], ["12/6"]]),
    P("Rasyonel sayı:", "[[5/0]] dışında hepsi", ["hepsi", "yalnız 2,5"], k=["dışında", "hariç"]), P("[[5/0]]:", "tanımsız", ["0", "5"], k=["tanımsız"])),
 ("m7i1", "a"): IK("24 = 2 · 2 · 2 · 3. Paydada 3 kalmamalı; ? 3'ün katı olmalı.", ["ortak özelliğini", "sonlu olması için"], "Paydayı çarpanlara ayır; 2 ve 5 dışındaki çarpan sadeleşmeli.",
    P("24'ün asal çarpanları:", "2 · 2 · 2 · 3", ["2 · 2 · 5", "4 · 6"], k=["2 · 3", "2·3", "2x3", "2 x 3"]), P("Sonlu olması için paydada", "3 kalmamalı", ["2 kalmamalı", "5 kalmamalı"], k=["3 kalmamalı", "3 olmamalı", "3 gitmeli"]),
    P("Bu yüzden ?", "3'ün katı olmalı", ["2'nin katı olmalı", "tek sayı olmalı"], k=["3'ün kat", "3 ün kat", "3ün kat", "3’ün kat"])),
 ("m7i2", "a"): IK("30 = 2 · 3 · 5. 3 sadeleşmeli; ? 3'ün katı olmalı.", ["Ortak özelliklerini", "sonlu ondalık gösterime"], "Paydayı çarpanlara ayır; 2 ve 5 dışındaki çarpan sadeleşmeli.",
    P("30'un asal çarpanları:", "2 · 3 · 5", ["2 · 15", "5 · 6"], k=["2 · 3 · 5", "2·3·5", "2x3x5", "2 x 3 x 5"]), P("Gitmesi gereken çarpan:", "3", ["2", "5"], k=["3"]),
    P("Bu yüzden ?", "3'ün katı olmalı", ["5'in katı olmalı", "çift sayı olmalı"], k=["3'ün kat", "3 ün kat", "3ün kat", "3’ün kat"])),
 ("m8i1", "a"): IK("[[-23/5]] = [[-4 3/5]] → −5 ile −4 arasında", ["ardışık iki tam sayı arasında"], "Tam sayılı kesre çevir: tam kısım ile bir sonraki tam sayı arası.",
    P("Tam sayılı kesir:", "[[-4 3/5]]", ["[[-3 4/5]]", "[[-5 2/5]]"], k=["4 3/5"]), P("Arasında olduğu tam sayılar:", "−5 ile −4", ["−4 ile −3", "−23 ile −5"], hepsi=[["-5"], ["-4"]])),
 ("m8i1", "b"): IK("5 eş parça; −4'ten 3 parça sola", ["kaç eş parçaya", "kaç parça soldadır"], "Payda kadar parça; tam kısımdan pay kadar say.",
    P("Parça sayısı (payda):", "5 eş parça", ["3 eş parça", "23 eş parça"], k=["5"]), P("−4'ten sola:", "3 parça", ["5 parça", "2 parça"], k=["3"])),
 ("m8i2", "a"): IK("Ali ve Su doğru ([[-7/3]]); Can yanlış, [[-7/6]] −2 ile −1 arasında.", ["Hangi öğrenci ya da öğrenciler", "Gerekçesiyle"], "Kim doğru + her cevabı sadeleştir, B ile karşılaştır.",
    P("B noktası:", "[[-7/3]] (−3'ten 2 parça sağda)", ["[[-8/3]]", "[[-7/6]]"], k=["-7/3", "-2 1/3"]), P("Su: [[-14/6]] ÷ 2 =", "[[-7/3]]", ["[[-7/6]]", "[[-14/3]]"], k=["7/3"]),
    P("Can: [[-7/6]] =", "[[-1 1/6]]", ["[[-2 1/3]]", "[[-7/3]]"], k=["1 1/6"]), P("Sonuç:", "Ali ve Su doğru", ["üçü de doğru", "yalnız Can"], k=["ali ve su", "su ve ali"])),
 ("m9i1", "a"): IK("−7 ve +7", ["tam sayıları yazınız"], "0'a uzaklık 7: biri −, biri +.", P("Solda:", "−7", ["−1", "−14"], k=["-7"]), P("Sağda:", "+7", ["+1", "+14"], k=["+7", "7"])),
 ("m9i1", "b"): IK("7 + 7 = 14 birim", ["uzaklık kaç birimdir"], "0'ın iki yanındaysa uzaklıkları topla.", P("İşlem:", "7 + 7", ["7 − 7", "7 · 7"], k=["7+7", "7 + 7"]), P("Uzaklık:", "14 birim", ["0 birim", "7 birim"], k=["14"])),
 ("m9i2", "a"): IK("−4, −3, −2, −1, 0, 1, 2, 3, 4, 5", ["arasındaki tam sayıları"], "“Arasındaki”: uçlar dahil değil.",
    P("İlk sayı:", "−4", ["−5", "−6"], k=["-4"]), P("Ortada:", "−3, −2, −1, 0, 1, 2, 3, 4", ["1, 2, 3", "−1, 1"], k=["0"]), P("Son sayı:", "5", ["6", "7"], k=["5"])),
 ("m9i2", "b"): IK("−4 ve 4", ["mutlak değeri 4 olanları"], "0'a 4 birim uzaklıkta iki sayı.", P("Solda:", "−4", ["−3", "−5"], k=["-4"]), P("Sağda:", "+4", ["+5", "+3"], k=["+4", " 4"])),
 ("m10i1", "a"): IK("Paydalar 12: [[-5/4]] < [[-7/6]] < [[2/3]] (a < b < c)", ["küçükten büyüğe"], "Pozitif en büyük; negatiflerde paydaları eşitle, payı büyük olan küçük.",
    P("Ortak payda:", "12", ["10", "24 değil"], k=["12"]), P("Negatifler:", "[[-15/12]] < [[-14/12]]", ["[[-14/12]] < [[-15/12]]", "[[-14/12]] < [[-5/4]]"], sira=[["-15/12"], ["-14/12"]]),
    P("Sıra:", "a < b < c", ["b < a < c", "c < b < a"], sira=[["a", "-5/4"], ["b", "-7/6"], ["c", "2/3"]])),
 ("m10i2", "a"): IK("Yanlış; 3. adımda: negatifte payı büyük olan küçüktür. Doğru: [[-3/2]] < [[-3/4]] < [[-5/8]] < [[1/4]]", ["doğru mudur", "hangi adımda", "doğru sıralamayı yazınız"], "Doğru mu? + hatalı adım + çünkü + doğru sıra.",
    P("Cevap:", "yanlış", ["doğru", "bilinmez"], k=["yanlış"]), P("İlk hata:", "3. adım", ["2. adım", "4. adım"], k=["3."]),
    P("Çünkü negatiflerde", "payı büyük olan küçüktür", ["payı büyük olan büyüktür", "paydası küçük olan küçüktür"], k=["büyük olan küçük", "büyük olan daha küçük", "mutlak değeri büyük olan küçük"]),
    P("Doğru sıra:", "[[-3/2]] < [[-3/4]] < [[-5/8]] < [[1/4]]", ["[[-5/8]] < [[-3/4]] < [[-3/2]] < [[1/4]]", "[[1/4]] < [[-5/8]] < [[-3/4]] < [[-3/2]]"], sira=[["-3/2", "-12/8"], ["-3/4", "-6/8"], ["-5/8"], ["1/4"]])),
 ("m11i1", "a"): IK("Yanlış. [[-1 1/12]] < [[-1 1/16]] < [[-1 1/20]]; doğru: [[-13/12]] < [[-17/16]] < [[-21/20]]", ["doğru mudur", "Gerekçesiyle"], "Doğru mu? + tam sayılı kesre çevir + doğru sıra.",
    P("Cevap:", "yanlış", ["doğru", "bilinmez"], k=["yanlış"]), P("Tam sayılı hâller:", "[[-1 1/12]], [[-1 1/16]], [[-1 1/20]]", ["[[-13 1/12]]", "[[-1 13/12]]"], hepsi=[["1 1/12"], ["1 1/16"], ["1 1/20"]]),
    P("Doğru sıra:", "[[-13/12]] < [[-17/16]] < [[-21/20]]", ["[[-21/20]] < [[-17/16]] < [[-13/12]]", "[[-17/16]] < [[-13/12]] < [[-21/20]]"], sira=[["-13/12"], ["-17/16"], ["-21/20"]])),
 ("m11i2", "a"): IK("Doğru. [[1 1/12]] < [[1 1/9]] < [[1 1/7]]: pozitifte kesir kısmı büyük olan büyük.", ["doğru mudur", "Gerekçesiyle"], "Doğru mu? + tam sayılı kesre çevir + kural.",
    P("Cevap:", "doğru", ["yanlış", "bilinmez"], k=["doğru"]), P("Tam sayılı hâller:", "[[1 1/7]], [[1 1/9]], [[1 1/12]]", ["[[8 1/7]]", "[[1 8/7]]"], hepsi=[["1 1/7"], ["1 1/9"], ["1 1/12"]]),
    P("Pozitifte kesir kısmı büyük olan", "daha büyüktür", ["daha küçüktür", "eşittir"], k=["büyük olan büyük", "daha büyük"])),
}
for q in Y.d["mebSorular"]:
    for i, z in enumerate(q.get("ikizler", [])):
        zid = z.get("id") or f"{q['id']}i{i + 1}"
        for m in z["maddeler"]:
            b = IKIZ.get((zid, m["harf"]))
            if b: m.update(b); m.pop("iskele", None)
            else: raise SystemExit(f"ikiz verisi eksik: {zid} {m['harf']}")

# =====================================================================
# PİSİ'NİN CEVABINI DÜZELT: 8 eksik (Ela'nın gerçek hatası: işaretsiz, tek sayı, gerekçesiz, sadeleştirmeden) + 4 yanılgı (yalnız Hatırla'daki sık hatalardan)
# =====================================================================
def KH(kazanim, tur, soru, kuark, dogruSik, yanlis1, yanlis2, ipucu, aciklama, once, ornek, sonra, k, havuz):
    Y.kuark(kazanim=kazanim, tur=tur, soru=soru, kuark=kuark, secenekler=[dogruSik, yanlis1, yanlis2], dogru=0, ipucu=ipucu, aciklama=aciklama,
            dogruCevap=f"{once} {ornek} {sonra}".replace(" .", ".").strip(), tamamla={"once": once, "ornek": ornek, "sonra": sonra, "k": k, "havuz": havuz})

TAM, DOGRU_ = "Tam, eksik yok.", "Doğru, hata yok."
KH(KA, "eksik", "Dalgıcın deniz seviyesinin 18 metre altında olmasını tam sayıyla ifade ediniz.", "18",
   "Eksik: işaret yok; “altı” olduğu için eksi yazılmalı.", "Yanlış: +18 yazılmalı.", TAM, "“Altı” kelimesi hangi işareti ister?", "Deniz seviyesinin altı negatif tam sayıyla gösterilir. (s. 20)",
   "Deniz seviyesinin altı olduğu için", "−18", ".", ["-18"], ["+18", "18"])
KH(KB, "eksik", "Mutlak değeri 11 olan tam sayıları yazınız.", "11",
   "Eksik: yalnız bir sayı yazılmış; −11 de var.", "Yanlış: cevap 22 olmalı.", TAM, "Soru “sayıları” diyor: kaç sayı var?", "0'a 11 birim uzaklıkta iki sayı vardır. (s. 37)",
   "11 ve", "−11", ".", ["-11"], ["0", "22"])
KH(KB, "eksik", "Hedef kütle 500 g, paket 493 g. Paket hedefe göre nasıldır, hata miktarı kaçtır?", "7 g eksik.",
   "Eksik: hata miktarı (mutlak değer) yazılmamış.", "Yanlış: paket 7 g fazladır.", TAM, "Soru iki şey soruyor.", "Hata miktarı = |493 − 500| = |−7| = 7. (MEB örnek sorusu)",
   "7 g eksik; hata miktarı |−7| =", "7 g", ".", ["7 g", "7g", "7 gram"], ["493 g", "14 g"])
KH(KC, "eksik", "[[-14/8]] sayısı A = [[-7/4]] noktasına karşılık gelir mi? Gerekçesiyle açıklayınız.", "Evet.",
   "Eksik: gerekçe yok; sadeleştirince aynı sayı olduğu yazılmalı.", "Yanlış: −14/8 farklı bir noktadır.", TAM, "“Gerekçesiyle” ne istiyor?", "Denk kesirler aynı noktaya karşılık gelir. (s. 27)",
   "Evet, çünkü [[-14/8]] 2 ile sadeleşince", "−7/4", "olur.", ["7/4"], ["−7/8", "−14/4"])
KH(KD, "eksik", "[[9/35]] sayısının ondalık gösterimi sonlu mu, devirli mi? Gerekçesiyle yazınız.", "Devirli.",
   "Eksik: gerekçe yok; paydanın çarpanları yazılmalı.", "Yanlış: sonlu olmalı.", TAM, "Gerekçe = paydanın asal çarpanları.", "35 = 5 · 7; 7, 2 ve 5 dışında bir çarpan. (s. 43)",
   "Devirli, çünkü 35 = 5 · 7 ve paydada", "7", "var.", ["7"], ["2", "5"])
KH(KE, "eksik", "1,2333… sayısını kesre çevirip en sade hâlini yazınız.", "[[111/90]]",
   "Eksik: kesir sadeleştirilmemiş.", "Yanlış: cevap 123/90 olmalı.", TAM, "“En sade hâl” ne demek?", "111 ve 90, 3 ile bölünür: [[37/30]]. (MEB örnek sorusu)",
   "[[111/90]], 3 ile sadeleşince", "37/30", "olur.", ["37/30"], ["111/30", "37/90"])
KH(KF, "eksik", "Efe'nin sıralaması doğru mudur? Yanlışsa ilk hatayı hangi adımda yaptığını açıklayınız.", "Yanlış, 3. adımda.",
   "Eksik: “çünkü” yok; neden hatalı olduğu yazılmalı.", "Yanlış: hata 2. adımda.", TAM, "“Açıklayınız” gerekçe istiyor.", "Negatiflerde payı büyük olan küçüktür. (s. 53)",
   "Yanlış, 3. adımda; çünkü negatiflerde payı büyük olan", "küçüktür", ".", ["küçük"], ["büyüktür", "eşittir"])
KH(KF, "eksik", "[[-5/4]], [[-7/6]], [[2/3]] sayılarını küçükten büyüğe sıralayınız.", "[[2/3]] en büyüktür.",
   "Eksik: yalnız en büyük yazılmış; tam sıra yazılmalı.", "Yanlış: en büyük −5/4'tür.", TAM, "“Sıralayınız” üç sayıyı da istiyor.", "Paydalar 12: [[-15/12]] < [[-14/12]]. (s. 55)",
   "[[-5/4]] <", "−7/6", "< [[2/3]]", ["-7/6"], ["−5/4", "2/3"])
KH(KB, "yanilgi", "|−7| kaçtır?", "−7",
   "Yanlış: mutlak değer negatif olamaz.", "Yanlış: cevap 0 olmalı.", DOGRU_, "Mutlak değer neyi ölçer?", "Mutlak değer 0'a uzaklıktır, negatif olamaz. (s. 37)",
   "Mutlak değer negatif olamaz: |−7| =", "7", ".", ["7"], ["0", "14"])
KH(KF, "yanilgi", "[[-4/6]] ile [[-5/6]] sayılarını karşılaştırınız.", "[[-4/6]] < [[-5/6]], çünkü 4 küçüktür.",
   "Yanlış: negatiflerde payı büyük olan küçüktür.", "Yanlış: iki sayı eşittir.", DOGRU_, "Hangisi sayı doğrusunda daha solda?", "[[-5/6]], 0'a daha uzak olduğu için daha küçüktür. (s. 53)",
   "Negatifte payı büyük olan küçüktür:", "−5/6 < −4/6", ".", ["-5/6<-4/6", "-5/6 < -4/6", "-4/6>-5/6", "-4/6 > -5/6"], ["−4/6 < −5/6", "−5/6 = −4/6"])
KH(KC, "yanilgi", "[[3/0]] hangi sayı kümesindedir?", "Rasyonel sayıdır, [[3/0]] = 0.",
   "Yanlış: payda 0 olamaz; 3/0 tanımsızdır.", "Yanlış: 3/0 = 3'tür.", DOGRU_, "Paydaya bak.", "Paydası 0 olan ifade tanımsızdır. (s. 28)",
   "Payda 0 olamaz; [[3/0]]", "tanımsızdır", ".", ["tanımsız"], ["0'dır", "3'tür"])
KH(KD, "yanilgi", "[[15/24]] sayısının ondalık gösterimi sonlu mu, devirli mi?", "Devirli, çünkü 24'te 3 var.",
   "Yanlış: önce sadeleştirilmeli; 5/8 sonludur.", "Yanlış: 15/24 tanımsızdır.", DOGRU_, "Kural en sade hâle uygulanır.", "[[15/24]] = [[5/8]], 8 = 2 · 2 · 2. (s. 43)",
   "Önce sadeleştir: [[15/24]] = [[5/8]]; 8 = 2 · 2 · 2, yani", "sonlu", ".", ["sonlu"], ["devirli", "tanımsız"])

# =====================================================================
# PROVA YAZILILARI (2 deneme; her kazanımdan 2 soru, toplam 100; puanlar tahmini). Bağlamlar MEB ve benzerlerinden farklı.
# =====================================================================
Y.prova(id="p1", ad="Prova 1", sorular=[
    {"kazanim": KA, "puan": 15, "benzer": "m2", "metin": ["1. Bir denizaltı deniz seviyesinin 250 metre altındadır.", "2. Bir kuş deniz seviyesinin 120 metre üstünde uçuyor.", "3. Hesaptan 75 TL çekildi.", "4. Asansör zemin katın 2 kat altında duruyor."],
     "maddeler": [M("a", "Verilen durumları uygun tam sayılarla ifade ediniz.", "1. −250  2. +120  3. −75  4. −2 (zemin katın altı)",
        [A("−250", "-250"), A("+120", "+120"), A("−75", "-75"), A("−2", "-2 ")], "gercek", puan=15)]},
    {"kazanim": KB, "puan": 20, "benzer": "m4", "svg": Z.tablo_svg(["Paket", "Kütle", "Hedefe göre", "Hata"], [["1. paket", "197 g", "3 g eksik", "|−3| = 3"], ["2. paket", "203 g", "", ""], ["3. paket", "199 g", "", ""], ["4. paket", "201 g", "", ""]], [76, 66, 96, 82], etiket="Bisküvi paketleri"),
     "metin": ["Bir bisküvi fabrikasında paketlerin kütlesi kontrol ediliyor. 1. paket 197 g ve hedef kütleden 3 g eksik."],
     "maddeler": [M("a", "Hedef kütleyi bulunuz.", "197 + 3 = 200 g.", [A("197 + 3", "197+3", "197 + 3"), A("200 g", "200")], "islem", puan=6),
                  M("b", "2., 3. ve 4. paketlerin hedefe göre durumunu ve hata miktarını yazınız.", "2. paket: 3 g fazla, hata 3. 3. paket: 1 g eksik, hata 1. 4. paket: 1 g fazla, hata 1.",
                    [A("2. paket: 3 g fazla", "3 g fazla", "3g fazla"), A("3. paket: 1 g eksik", "1 g eksik", "1g eksik"), A("4. paket: 1 g fazla", "1 g fazla", "1g fazla")], "islem", puan=7),
                  M("c", "Hata miktarı en az olan paket veya paketleri gerekçesiyle belirleyiniz.", "3. ve 4. paketler; ikisinin de hata miktarı 1 g, en küçük.",
                    [A("3. paket", "3."), A("4. paket", "4."), A("Hata 1 g, en küçük", "1 g", "1g", "en küçük", "en az")], "gerekce", puan=7)]},
    {"kazanim": KD, "puan": 15, "benzer": "m5", "metin": ["Rasyonel sayılar: [[9/40]], [[7/12]], [[18/45]], [[13/22]]"],
     "maddeler": [M("a", "Bu sayıların ondalık gösterimlerinin sonlu mu devirli mi olduğunu matematiksel gerekçeleriyle açıklayınız.",
        "Paydada yalnız 2 ve 5 varsa sonlu. [[9/40]]: 40 = 2 · 2 · 2 · 5 → sonlu. [[7/12]]: 12 = 2 · 2 · 3 → devirli. [[18/45]] = [[2/5]] → sonlu. [[13/22]]: 22 = 2 · 11 → devirli.",
        [A("Kural: yalnız 2 ve 5 → sonlu", "2 ve 5", "2 veya 5", "2 ile 5"), A("9/40 ve 18/45 sonlu", "sonlu"), A("7/12 ve 13/22 devirli", "devirli"), A("18/45 = 2/5", "2/5")], "sonlu", puan=15)]},
    {"kazanim": KE, "puan": 15, "benzer": "m3", "metin": ["Bir matematik etkinliğinde kartlarda 0,[[d:6]] ve 1,2[[d:5]] devirli sayıları yazılıdır."],
     "maddeler": [M("a", "0,[[d:6]] sayısını kesre çevirip en sade hâlini yazınız.", "0,[[d:6]] = [[6/9]] = [[2/3]].", [A("6/9", "6/9"), A("En sade: 2/3", "2/3")], "devir", puan=7),
                  M("b", "1,2[[d:5]] sayısını kesre çeviriniz.", "1,2[[d:5]] = (125 − 12) / 90 = [[113/90]].", [A("125 − 12", "125-12", "125 - 12", "113"), A("113/90", "113/90")], "devir", puan=8)]},
    {"kazanim": KF, "puan": 20, "benzer": "m10", "metin": ["Aşağıdaki rasyonel sayı çiftleri karşılaştırılacaktır."],
     "maddeler": [M("a", "[[7/12]] ile [[5/8]] ve [[-3/10]] ile [[-2/5]] sayılarını karşılaştırınız; aralarına < ya da > yazınız.",
        "[[7/12]] = [[14/24]], [[5/8]] = [[15/24]] → [[7/12]] < [[5/8]]. [[-3/10]] = −0,3, [[-2/5]] = −0,4 → [[-3/10]] > [[-2/5]]. Sonuç: 7/12 < 5/8 ve −3/10 > −2/5.",
        [A("7/12 < 5/8", "7/12<5/8", "7/12 < 5/8", "5/8>7/12", "5/8 > 7/12"), A("−3/10 > −2/5", "-3/10>-2/5", "-3/10 > -2/5", "-2/5<-3/10", "-2/5 < -3/10")], "hata", puan=10),
                  M("b", "[[11/15]] ile [[7/10]] ve [[-5/6]] ile [[-13/18]] sayılarını karşılaştırınız; aralarına < ya da > yazınız.",
        "[[11/15]] = [[22/30]], [[7/10]] = [[21/30]] → [[11/15]] > [[7/10]]. [[-5/6]] = [[-15/18]] → [[-5/6]] < [[-13/18]]. Sonuç: 11/15 > 7/10 ve −5/6 < −13/18.",
        [A("11/15 > 7/10", "11/15>7/10", "11/15 > 7/10", "7/10<11/15", "7/10 < 11/15"), A("−5/6 < −13/18", "-5/6<-13/18", "-5/6 < -13/18", "-13/18>-5/6", "-13/18 > -5/6")], "hata", puan=10)]},
    {"kazanim": KF, "puan": 15, "benzer": "m11", "svg": Z.tahta_defter(["−29/28", "−36/35", "−22/21"], ["−22/21", "−29/28", "−36/35"]),
     "metin": ["Bir öğrenci [[-29/28]], [[-36/35]], [[-22/21]] sayılarını [[-22/21]] < [[-29/28]] < [[-36/35]] diye sıralamıştır."],
     "maddeler": [M("a", "Öğrencinin sıralaması doğru mudur? Matematiksel gerekçelerle açıklayınız.",
        "Doğru. [[-29/28]] = [[-1 1/28]], [[-36/35]] = [[-1 1/35]], [[-22/21]] = [[-1 1/21]]. [[1/21]] en büyük kesir olduğu için [[-1 1/21]] en küçük. Sıra: [[-22/21]] < [[-29/28]] < [[-36/35]].",
        [A("Doğru", "doğru"), A("Tam sayılı kesir", "1 1/"), A("Negatifte mutlak değeri büyük olan küçük", "mutlak değeri büyük", "büyük olan küçük", "en küçük")], "hata", puan=15)]}])

Y.prova(id="p2", ad="Prova 2", sorular=[
    {"kazanim": KC, "puan": 20, "benzer": "m6", "metin": ["Sayılar: [[18/6]], −9, 0,75, [[0/5]], [[-10/5]], [[4/0]]"],
     "maddeler": [M("a", "Bu sayılardan doğal sayı ve tam sayı olanları yazınız.", "Önce sadeleştir: [[18/6]] = 3, [[0/5]] = 0, [[-10/5]] = −2. Doğal: [[18/6]], [[0/5]]. Tam: [[18/6]], −9, [[0/5]], [[-10/5]].",
        [A("Doğal: 18/6 ve 0/5", "0/5"), A("Tam: −9 ve −10/5 de", "10/5")], "gerekce", puan=10),
                  M("b", "Rasyonel sayı olanları yazınız. Hangi ifade hiçbir kümeye girmez? Nedenini açıklayınız.", "[[4/0]] dışında hepsi rasyoneldir. [[4/0]] paydası 0 olduğu için tanımsızdır, hiçbir kümeye girmez.",
        [A("4/0 dışında hepsi", "dışında", "hariç"), A("4/0 tanımsız (payda 0)", "tanımsız", "payda 0", "paydası 0")], "gerekce", puan=10)]},
    {"kazanim": KB, "puan": 15, "benzer": "m9", "metin": ["Zeynep, aklından tuttuğu tam sayının mutlak değerinin 9 olduğunu söylüyor."],
     "maddeler": [M("a", "Zeynep'in aklından tutmuş olabileceği tam sayıları yazınız.", "−9 ve +9.", [A("−9", "-9"), A("+9", "+9", "9 ve", "ve 9")], "islem", puan=8),
                  M("b", "Bu sayılar arasındaki uzaklık kaç birimdir?", "9 + 9 = 18 birim.", [A("9 + 9", "9+9", "9 + 9"), A("18", "18")], "islem", puan=7)]},
    {"kazanim": KD, "puan": 15, "benzer": "m7", "metin": ["Tahtada ?/55 rasyonel sayısı yazılıdır."],
     "maddeler": [M("a", "Bu sayının sonlu ondalık gösterime sahip olması için ? yerine yazılabilecek tam sayıların ortak özelliğini matematiksel gerekçeleriyle açıklayınız.",
        "55 = 5 · 11. Paydada 11 kalmamalı, sadeleşip gitmeli. Bu yüzden ? 11'in katı olmalıdır.",
        [A("55 = 5 · 11", "5 · 11", "5·11", "5x11", "5 x 11", "5 ve 11"), A("11 kalmamalı", "11 kalmamalı", "sadeleş", "11 olmamalı"), A("11'in katı", "11'in kat", "11 in kat", "11in kat", "11’in kat")], "sonlu", puan=15)]},
    {"kazanim": KE, "puan": 20, "benzer": "m3", "metin": ["2,[[d:4]] = △/□ eşitliğinde △/□ en sade hâlde yazılmış bir kesirdir."],
     "maddeler": [M("a", "2,[[d:4]] sayısını kesre çeviriniz.", "2,[[d:4]] = (24 − 2) / 9 = [[22/9]].", [A("24 − 2", "24-2", "24 - 2", "22"), A("22/9", "22/9")], "devir", puan=10),
                  M("b", "△ + □ toplamı kaçtır?", "△ = 22, □ = 9. 22 + 9 = 31.", [A("22 + 9", "22+9", "22 + 9"), A("31", "31")], "islem", puan=10)]},
    {"kazanim": KF, "puan": 15, "benzer": "m10", "metin": ["Gizem [[-3/4]], [[-5/6]], [[1/3]], [[-1/2]] sayılarını [[-3/4]] < [[-5/6]] < [[-1/2]] < [[1/3]] diye sıralamıştır."],
     "maddeler": [M("a", "Gizem'in sıralaması doğru mudur? Yanlışsa gerekçesiyle açıklayıp doğru sıralamayı yazınız.",
        "Yanlış. Paydalar 12: [[-9/12]], [[-10/12]], [[-6/12]]. Negatifte payı büyük olan küçük: [[-10/12]] < [[-9/12]]. Doğru sıra: [[-5/6]] < [[-3/4]] < [[-1/2]] < [[1/3]].",
        [A("Yanlış", "yanlış"), A("Paydaları eşitleme (12)", "12"), SIRA("Doğru sıra: −5/6 < −3/4 < −1/2 < 1/3", ["-5/6", "-10/12"], ["-3/4", "-9/12"], ["-1/2", "-6/12"], "1/3")], "hata", puan=15)]},
    {"kazanim": KF, "puan": 15, "benzer": "m11", "svg": Z.tahta_defter(["−25/24", "−31/30", "−19/18"], ["−31/30", "−25/24", "−19/18"]),
     "metin": ["Bir öğrenci [[-25/24]], [[-31/30]], [[-19/18]] sayılarını [[-31/30]] < [[-25/24]] < [[-19/18]] diye sıralamıştır."],
     "maddeler": [M("a", "Öğrencinin sıralaması doğru mudur? Matematiksel gerekçelerle açıklayınız.",
        "Yanlış. [[-25/24]] = [[-1 1/24]], [[-31/30]] = [[-1 1/30]], [[-19/18]] = [[-1 1/18]]. [[1/18]] en büyük kesir olduğu için [[-1 1/18]] en küçük. Doğru sıra: [[-19/18]] < [[-25/24]] < [[-31/30]].",
        [A("Yanlış", "yanlış"), A("Tam sayılı kesir", "1 1/"), SIRA("Doğru sıra: −19/18 < −25/24 < −31/30", "-19/18", "-25/24", "-31/30")], "hata", puan=15)]}])

Y.yaz()
