"""Din Kültürü 7 · 1. Dönem 1. Yazılı — Yazılıya Hazırlık verisi.
Kapsam: MEB senaryo tablosu, Senaryo 5 (okulun seçtiği): DKAB.7.1.1 (1), DKAB.7.1.2 (2), DKAB.7.1.3 (3) = 6 soru. Sınav 13 Kasım 2026 Cuma.
Kaynaklar: MEB TEGM "Yazılıya Hazırlanıyorum 7. Sınıf Din Kültürü ve Ahlak Bilgisi 1. Dönem 1. Yazılı" (9 soru, çözümleriyle).
  MEB "öğrenme çıktısı – soru no": 7.1.1 → 1-2-3 · 7.1.2 → 4-5-6 · 7.1.3 → 7-8 · 7.1.4 → 9. Senaryo 5'e girenler: 1–8; hariç: 9.
  Ders kitabı s. 16, 19, 25–29, 32, 34–35. yazilihocam.com 1. yazılı örnekleri (siyah 1,3,4,7,8,9,11; kırmızı 1-II,2,3,4,5,7,9,10): benzer soru ve provalarda.
Öncelik (Kemal: banko soruya çok, zor soruya az emek): m2, m3, m4, m7 ★★★ · m1, m5, m8 ★★ · m6 ★.
Kararlar (Kemal onayı, 10 Kasım 2026): MEB 2–3–4 isim/terim soruları kısa akış (eşleştir/boşluk → yaz; 4 basamak yok, motor değişmedi);
  7.1.3 için 5 Hazır Cümle; MEB 5b anahtarındaki Kıyamet (metinde “Kıyametten sonra” geçiyor) iki maddede de zorunlu sayılmaz.
Çalıştır: python3 araclar/yazili/din1_d1y1.py"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from yazili import Yazili
import cizim_din as Z


def A(ad, *k): return {"ad": ad, "k": list(k)}
def AS(ad, *sira): return {"ad": ad, "sira": [list(x) for x in sira]}
def M(harf, soru, cevap=None, an=None, formul=None, puan=None):
    m = {"harf": harf, "soru": soru}
    if formul: m["formul"] = formul
    if cevap: m["cevap"] = cevap; m["anahtarlar"] = an or []
    if puan is not None: m["puan"] = puan
    return m
def P(bas, ornek, havuz, k=None, hepsi=None, sira=None):
    d = {"bas": bas, "ornek": ornek, "havuz": havuz}
    if k: d["k"] = k
    if hepsi: d["hepsi"] = hepsi
    if sira: d["sira"] = sira
    return d
def B(kisa, eksik, yanlis, ipucu, aciklama, *parcalar):
    return {"kisaCevap": kisa, "basamak": {"sec": {"secenekler": [kisa, eksik, yanlis], "dogru": 0, "ipucu": ipucu, "aciklama": aciklama}, "parcalar": list(parcalar)}}
def Q(madde, tetik, notu, b):
    madde.update(b); madde["tetik"], madde["kalipNot"] = tetik, notu; return madde
def KA(madde, iskele, kisa, tetik, notu=None):
    """Kısa akış (isim/terim): iskele (eşleştir, boşluk) → aklından yaz. Notu olmayan madde 'soruyu oku' adımı açmaz."""
    madde.update({"iskele": iskele, "kisaCevap": kisa, "tetik": tetik})
    if notu: madde["kalipNot"] = notu
    return madde
def IK(madde, tetik, notu, kisa, *parcalar):
    """Benzer soru maddesi: sec yok, doğrudan sınavdaki gibi yazma + ipucu."""
    madde.update({"kisaCevap": kisa, "tetik": tetik, "kalipNot": notu, "basamak": {"parcalar": list(parcalar)}}); return madde


K1, K2, K3 = "DKAB.7.1.1", "DKAB.7.1.2", "DKAB.7.1.3"

Y = Yazili("din1", "d1y1",
    baslik="1. Dönem 1. Yazılı", ders="Din Kültürü ve Ahlak Bilgisi", senaryo="Senaryo 5", sure=40, tarih="2026-11-13",
    dagilim={K1: 1, K2: 2, K3: 3},
    mebToplam=9,
    mebHaric=[{"no": 9, "kazanim": "DKAB.7.1.4", "ad": "Nâs suresini ve bu surenin anlamını okuyarak yorumlayabilme"}],
    giris="Okulun seçtiği senaryoda <b>6 soru</b> var: melekler 1, ahiret hayatının aşamaları 2, melek ve ahiret inancının kazandırdıkları 3. "
          "Önce <b>★★★ Banko</b> soruları sağlamla: <b>altı meleğin adı ve görevi</b>, <b>ayetten ahiret aşamasını bulma</b>, metinden <b>davranış yazma</b>. "
          "Soruların yarısı inancın kazandırdıklarından: <b>5 Hazır Cümle</b> üç soruya da yeter.",
    kapsamDisi=["Nâs suresi (okunuşu, anlamı, mesajı) — MEB örneğinin 9. sorusu",
                "Hac, umre ve kurban — 2. ünite bu yazılıda yok"],
    puanNotu="Puanlar tahminidir: okul soruların puanını farklı dağıtabilir. Toplam 100. Provalarda senaryodaki gibi 6 soru var (melekler 1, aşamalar 2, kazandırdıkları 3).",
    kaynakNotu="Sorular MEB'in yayımladığı 'Yazılıya Hazırlanıyorum 7. Sınıf Din Kültürü ve Ahlak Bilgisi 1. Dönem 1. Yazılı' örneklerine, ders kitabına ve yazilihocam.com yazılı örneklerine dayanır. "
               "Ayet ve hadisler MEB dokümanı ve ders kitabındaki mealle verilmiştir. MEB'in 5. soru cevabında Kıyamet 'metinde yok' listesinde; oysa metinde 'Kıyametten sonra' geçiyor, bu yüzden burada zorunlu sayılmadı.",
    soruGiris="Bunlar MEB'in örnek soruları; yazılıda <b>benzerleri</b> çıkacak. <b>★★★ Banko</b> olanlarla başla. Cevabı kısa ve kalıba uygun yaz.",
    kazanimAd="konu")

# =====================================================================
# KONULAR (Hatırla kartları + Hatırla ve Tekrarla boşlukları)
# =====================================================================
Y.kazanim(kod=K1, ad="Melekleri sınıflandırabilme", kisa="Melekler: Özellikleri ve Görevleri", soru=1, renk="#1a7f86",
    konular=["u1k1", "u1k2"], sayfa="s. 16, 19", svg=Z.h_melek(),
    maddeler=["Melekleri <b>gözle göremeyiz</b>; onları ancak <b>Allah'ın haber vermesiyle</b> biliriz. (s. 16; MEB örnek sorusu)",
              "Özellikleri: <b>nurdan yaratılmışlar</b>, <b>iradeleri yok</b>, <b>Allah'ın emrine karşı gelmezler</b>, hızlı ve güçlüler; <b>yemez, içmez, uyumazlar</b>. (s. 19)",
              "Dört büyük melek: <b>Cebrail</b> vahiy getirir · <b>Azrail</b> can alır · <b>Mikâil</b> tabiat olayları ve rızık · <b>İsrafil</b> sûra üfler. (s. 19)",
              "<b>Kiramen Kâtibin</b> (yazıcı melekler): sevap ve günahları amel defterine yazar. (s. 19)",
              "<b>Münker ve Nekir</b> (sorgu melekleri): kabirde insanları sorguya çeker. (s. 19; MEB örnek sorusu)",
              "Ayette ipucu ara: “canını alırlar” → <b>Azrail</b>; “değerli yazıcılar” → <b>Kiramen Kâtibin</b>."],
    kelimeler=["nurdan", "iradeleri yok", "vahiy: Cebrail", "can: Azrail", "tabiat: Mikâil", "sûr: İsrafil", "yazar: Kiramen Kâtibin", "sorgu: Münker ve Nekir"],
    hatalar=[{"yanlis": "“Vahyi Mikâil getirir.”", "dogru": "Vahyi Cebrail getirir; Mikâil tabiat olaylarıyla görevlidir."},
             {"yanlis": "“Sûra Azrail üfler.”", "dogru": "Sûra İsrafil üfler; Azrail can alır."},
             {"yanlis": "“Kiramen Kâtibin kabirde sorgular.”", "dogru": "Sorguyu Münker ve Nekir yapar; Kiramen Kâtibin yazar."}],
    tekrar=[{"c": "Melekleri Allah'ın {haber vermesiyle|gözlerimizle bakarak} biliriz.", "s": "s. 16"},
            {"c": "Melekler {nurdan|topraktan|ateşten} yaratılmıştır.", "s": "s. 19"},
            {"c": "Meleklerin {iradeleri yoktur|istedikleri gibi davranma güçleri vardır}.", "s": "s. 19"},
            {"c": "Vahiy getiren melek: {Cebrail|Mikâil|Azrail}", "s": "s. 19"},
            {"c": "Can almakla görevli melek: {Azrail|İsrafil|Cebrail}", "s": "s. 19"},
            {"c": "Tabiat olaylarıyla görevli melek: {Mikâil|Cebrail|İsrafil}", "s": "s. 19"},
            {"c": "Sûra iki kez üfleyen melek: {İsrafil|Azrail|Mikâil}", "s": "s. 19"},
            {"c": "Sevap ve günahları yazan melekler: {Kiramen Kâtibin|Münker ve Nekir}", "s": "s. 19"},
            {"c": "İnsanları sorguya çeken melekler: {Münker ve Nekir|Kiramen Kâtibin}", "s": "s. 19"}])

Y.kazanim(kod=K2, ad="Ahiret hayatının aşamalarını çözümleyebilme", kisa="Ahiret Hayatının Aşamaları", soru=2, renk="#7048e8",
    konular=["u1k3", "u1k4"], sayfa="s. 25–29", svg=Z.h_asama(),
    maddeler=["Sıra: <b>Ölüm → Kıyamet → Baas → Mahşer → Mizan → Cennet / Cehennem</b>. (s. 26, 29)",
              "<b>Kıyamet</b>: İsrafil sûra <b>ilk</b> üfleyince her şey son bulur. <b>Baas</b>: sûra <b>ikinci</b> üfleyince insanlar yeniden dirilir. (s. 26–27)",
              "<b>Mahşer</b>: insanların hesap vermek için <b>toplanacakları yer</b>. Amel defterleri burada verilir. (s. 27)",
              "<b>Mizan</b>: sevap ve günahların tartılacağı <b>manevi adalet terazisi</b>. (s. 27)",
              "Hesaptan sonra: <b>Cennet</b> mükâfat yeri, <b>Cehennem</b> ceza yeri. (s. 28–29)",
              "Ayetten bul: diriltme, kabirden çıkma → <b>Baas</b> · toplanma → <b>Mahşer</b> · terazi, tartı → <b>Mizan</b> · mükâfat, ırmaklar → <b>Cennet</b> · sûr → <b>Kıyamet</b>.",
              "<b>Ömür</b> yaşam süresi, <b>ecel</b> ölüm vakti, <b>amel defteri</b> yapılanların yazıldığı defterdir. (s. 25)"],
    kelimeler=["ölüm", "kıyamet", "baas: diriliş", "mahşer: toplanma", "mizan: terazi", "cennet / cehennem", "ömür, ecel, amel defteri"],
    hatalar=[{"yanlis": "“Mahşer, sevap ve günahların tartıldığı terazidir.”", "dogru": "Tartılan yer mizan; mahşer toplanma yeridir."},
             {"yanlis": "“Sûra ikinci kez üflenince kıyamet kopar.”", "dogru": "İlk üfleyiş kıyamet, ikinci üfleyiş baastır."},
             {"yanlis": "“Metinde yer verilen” sorusuna metinde geçmeyeni yazmak.", "dogru": "Önce kelime metinde geçiyor mu diye bak."}],
    tekrar=[{"c": "Ahiret aşamalarının ilki {ölümdür|mahşerdir}.", "s": "s. 26"},
            {"c": "İsrafil sûra ilk üfleyince {kıyamet|baas} gerçekleşir.", "s": "s. 26"},
            {"c": "Sûra ikinci kez üflenince yeniden diriliş olur; buna {baas|mizan} denir.", "s": "s. 27"},
            {"c": "İnsanların hesap vermek için toplanacakları yer: {mahşer|mizan}", "s": "s. 27"},
            {"c": "Sevap ve günahların tartıldığı manevi terazi: {mizan|mahşer}", "s": "s. 27"},
            {"c": "Mizandan sonra insanlar {cennete ya da cehenneme|yeniden dünyaya} gönderilir.", "s": "s. 28"},
            {"c": "Ayette “terazi” geçiyorsa aşama {mizan|baas} olur.", "s": "cevap kalıbı"},
            {"c": "Ayette “diriltileceksiniz” geçiyorsa aşama {baas|cennet} olur.", "s": "cevap kalıbı"}])

Y.kazanim(kod=K3, ad="Melek ve ahiret inancının insana kazandırdıkları konusunda analitik düşünebilme", kisa="İnancın İnsana Kazandırdıkları", soru=3, renk="#c2410c",
    konular=["u1k5"], sayfa="s. 32, 34–35", svg=Z.h_kazanc(),
    maddeler=["<b>5 Hazır Cümle 1:</b> Yaptıklarımın yazıldığını bilirim, <b>sorumlu davranırım</b>. (s. 34; MEB örnek sorusu)",
              "<b>5 Hazır Cümle 2:</b> Ahirette hesap vereceğimi bilirim, <b>kötülükten uzak dururum</b>. (s. 34–35)",
              "<b>5 Hazır Cümle 3:</b> Kimse görmese de haksızlık yapmam, <b>vicdanlı davranırım</b>. (MEB örnek sorusu)",
              "<b>5 Hazır Cümle 4:</b> Dünyanın imtihan olduğunu bilirim, <b>zorlukta pes etmem, sabrederim</b>. (s. 34)",
              "<b>5 Hazır Cümle 5:</b> Güzel davranışların karşılığını ahirette göreceğimi bilirim, <b>iyilik yaparım</b>. (s. 34)",
              "Davranış örnekleri: <b>komşusuna eziyet etmez, misafirine ikram eder, güzel söz söyler</b>, yardım eder, sözünü tutar. (s. 32, 34; MEB örnek sorusu)"],
    kelimeler=["yazılıyor → sorumlu", "hesap → kötülükten uzak", "kimse görmese de → vicdanlı", "imtihan → pes etmem", "karşılığı var → iyilik yaparım", "çünkü …"],
    hatalar=[{"yanlis": "Yalnız “Sorumlu olur.” yazıp gerekçeyi unutmak.", "dogru": "Gerekçesini ekle: “Sorumlu olur, çünkü yaptıklarının yazıldığını bilir.”"},
             {"yanlis": "“Üç davranış” isteyen soruya tek davranış yazmak.", "dogru": "Metindeki her öğüdü ayrı ayrı yaz: komşu, misafir, güzel söz."},
             {"yanlis": "“Güzel şeyler kazandırır.” gibi belirsiz cevap yazmak.", "dogru": "Kazancın adını yaz: sorumluluk, sabır, vicdan, iyilik."}],
    tekrar=[{"c": "Yaptıklarının {kaydedildiğini|unutulduğunu} bilen insan sorumlu davranır.", "s": "s. 34"},
            {"c": "Ahirete inanan, yaptıklarının {hesabını vereceğini|karşılıksız kalacağını} bilir.", "s": "s. 35"},
            {"c": "Kimse görmese de haksızlık yapmayan kişi {vicdanlı|ilgisiz} davranır.", "s": "MEB örnek sorusu"},
            {"c": "Dünyanın bir {imtihan|oyun} yeri olduğunu bilen, zorlukta sabreder.", "s": "s. 34"},
            {"c": "Ahirete inanan, güzel davranışlarının karşılığını {ahirette|hiçbir zaman} göreceğini bilir.", "s": "s. 34"},
            {"c": "Allah'a ve ahiret gününe inanan kişi komşusunu {rahatsız etmez|rahatsız eder}.", "s": "s. 32"},
            {"c": "Allah'a ve ahiret gününe inanan kişi misafirine {ikram eder|kapıyı açmaz}.", "s": "s. 32"},
            {"c": "Cevapta kazancı yazdıktan sonra {çünkü|belki} ile gerekçesini ekle.", "s": "cevap kalıbı"}])

# =====================================================================
# CEVAP KALIPLARI
# =====================================================================
Y.formul(id="ozellik", ad="Meleklerin özellikleri", kalip="Görülmezler + emre karşı gelmezler + iradeleri yok (+ nurdan, yemezler)", ne="“Meleklerin özellikleri nelerdir?” sorularında", ornek="Gözle görülmezler, emre karşı gelmezler, iradeleri yoktur.")
Y.formul(id="isim", ad="Görevden melek adı", kalip="Görevi oku → meleğin adını yaz (Cebrail, Azrail, Mikâil, İsrafil, Kiramen Kâtibin, Münker ve Nekir)", ne="“Meleklerin isimlerini yazınız” sorularında", ornek="Vahiy getirir: Cebrail.")
Y.formul(id="asama", ad="Ayetten aşama", kalip="Kilit kelime → aşama: dirilme = baas, toplanma = mahşer, terazi = mizan, mükâfat = cennet, sûr = kıyamet", ne="“Hangi aşamadan bahsedilmektedir?” sorularında", ornek="“Adalet terazileri” → Mizan.")
Y.formul(id="metinde", ad="Metinde olan / olmayan", kalip="Kelime metinde geçiyor mu? Geçenler a), geçmeyenler b)", ne="“Metinde yer verilen / verilmeyen aşamalar” sorularında", ornek="Metinde: baas, mizan. Metinde yok: mahşer, cennet, cehennem.")
Y.formul(id="iliski", ad="Aşamalar arası ilişki", kalip="Önce … (dirilme), sonra … (tartılma), sonunda … (karşılık)", ne="“Aşamalar arasındaki ilişkiyi açıklayınız” sorularında", ornek="Önce baas olur, sonra mizanda tartılır, sonunda cennet ya da cehennemde karşılığını görür.")
Y.formul(id="davranis", ad="Davranış yazma", kalip="Metindeki öğütleri tek tek “yapar / yapmaz” diye yaz", ne="“Üç davranış yazınız” sorularında", ornek="Komşusuna eziyet etmez. Misafirine ikram eder. Güzel söz söyler.")
Y.formul(id="etki", ad="İnancın etkisi", kalip="Bilir + bilir + bu yüzden davranış", ne="“Etkisini üç cümleyle açıklayınız” sorularında", ornek="Yaptıklarının yazıldığını bilir. Hesap vereceğini bilir. Bu yüzden kötülükten uzak durur.")
Y.formul(id="kazanc", ad="Kazandırdıkları", kalip="Kazanç + çünkü + gerekçe (5 Hazır Cümle)", ne="“Kazandırdıklarını gerekçeleriyle yazınız” sorularında", ornek="Sorumlu olur, çünkü yaptıklarının yazıldığını bilir.")

# ortak anahtar kökleri
GORUL = ["görülmez", "görünmez", "görülemez", "algılan", "haber", "vahiy"]
KARSI = ["karşı gelmez", "itaat", "emre uy", "emirlere uy", "emirlerine uy"]
IRADE = ["irade"]
NUR = ["nur"]
YEMEZ = ["yemez", "içmez", "uyumaz", "ihtiyaç"]
K_OZ = "Özellik → melekleri ayıran yönleri yaz: görülmezler, emre karşı gelmezler, iradeleri yok."
K_AD = "İsim → görevi oku, o görevi yapan meleğin adını yaz."
K_TAB = "Tablo → satırın adını oku, o gruptaki meleklerin isimlerini yaz."
K_AS = "Ayetten aşama → kilit kelimeye bak: dirilme = baas, toplanma = mahşer, terazi = mizan."
K_VAR = "Metinde olan → metinde kelimesi geçen kavramları yaz."
K_YOK = "Metinde olmayan → aşamaları tek tek düşün, metinde geçmeyenleri yaz."
K_IL = "İlişki → “önce …, sonra …, sonunda …” diye sıraya göre anlat."
K_DAV = "Davranış → metindeki her öğüdü ayrı bir “yapar / yapmaz” cümlesi yap."
K_ET = "Etki → “… bilir” iki cümle + “bu yüzden …” bir cümle."
K_KZ = "Kazandırdıkları → kazancı yaz, “çünkü” ile gerekçesini ekle."

# =====================================================================
# MEB SORULARI (8 soru) — öncelik: 4 banko, 3 puan topla, 1 bir adım
# =====================================================================
Y.meb(id="m1", no=1, kazanim=K1, oncelik=2,
    metin=["Ahmet, “Gezegenimizdeki Canlılar” belgeselini izledikten sonra “Kâinatta farklı özelliklere sahip ne kadar çok varlık yaratılmış.” diye düşündü. Bu konuyla ilgili öğretmeninin tavsiye ettiği kaynaklardan yaptığı araştırmada; güneş, ay, yıldızlar, dağlar, denizler, bitkiler ve hayvanlar gibi görülebilen varlıkların yanı sıra melek, cin şeytan gibi gözle görülemeyen varlıkların olduğunu da öğrendi. Sadece vahiyle bilgi sahibi olunabilecek varlıklardan olan meleklerin hangi özelliklere sahip olduğuyla ilgili şu ayetlere ulaştı:",
           "“Hamd, gökleri ve yeri yoktan var eden, melekleri ikişer, üçer, dörder kanatlı elçiler kılan Allah'a mahsustur.” (Fatır suresi 1. ayet)",
           "“… Allah'ın kendilerine verdiği emirlere karşı gelmeyen ve kendilerine emredilen şeyi yapan melekler vardır.” (Tahrim suresi 6. ayet)"],
    maddeler=[Q(M("a", "Buna göre melekleri diğer varlıklardan ayıran özellikler nelerdir? Yazınız.",
        "Melekler duyu organlarıyla algılanamayan, sadece Allah'ın haber vermesiyle bilgi sahibi olunabilen varlıklardır. Allah'ın emir ve buyruklarına asla karşı gelmezler. Allah'ın buyurduğu şeyleri eksiksiz yerine getirirler. İradeleri yoktur ve kanatlı varlıklardır.",
        [A("Gözle görülmez, Allah'ın haberiyle bilinir", *GORUL), A("Emre karşı gelmez, buyrulanı eksiksiz yapar", *KARSI, "eksiksiz", "yerine getir", "emredileni yapar"), A("İradeleri yok, kanatlı", "irade", "kanat")], "ozellik"),
        ["melekleri diğer varlıklardan ayıran özellikler"], K_OZ,
        B("Gözle görülmezler, emre karşı gelmezler, iradeleri yoktur.", "Gözle görülmezler.", "İnsanlar gibi yer içerler, istediklerini yaparlar.",
          "Ayetler “emirlere karşı gelmeyen” diyor; metin “gözle görülemeyen” diyor. İkisini de kullan.",
          "Melekler görülmez, emre karşı gelmez, iradeleri yoktur; MEB'in cevabı da bunlardır. (s. 19; MEB örnek sorusu)",
          P("Görünme:", "gözle görülmezler", ["her yerde görünürler", "yemek yerler"], k=GORUL),
          P("Allah'ın buyrukları:", "emre karşı gelmezler", ["bazen karşı gelirler", "kendi bildiğini yaparlar"], k=KARSI),
          P("Seçme gücü:", "iradeleri yoktur", ["kendileri seçerler", "istedikleri gibi davranırlar"], k=IRADE)))],
    ikizler=[
        {"metin": ["Yüce Allah tarafından özel görevler verilerek yaratılan, görünmeyen ancak varlıklarına inanılması iman esaslarından biri olan varlıklar vardır. Kur'an-ı Kerim'de bu varlıklardan sıkça söz edilir."],
         "maddeler": [IK(M("a", "Bu varlıkların adını yazınız ve onlara ait üç özelliği belirtiniz.", "Melekler. Nurdan yaratılmışlardır, iradeleri yoktur, yeme içme uyuma gibi ihtiyaçları yoktur.",
                        [A("Adı: melekler", "melek"), A("Nurdan yaratılmış", *NUR), A("İradeleri yok", *IRADE), A("Yemez, içmez, uyumaz", "yeme", "içme", "uyuma", "uyumaz", "hızlı")], "ozellik"),
                      ["adını", "üç özelliği"], "Ad + üç özellik → önce adı, sonra üç kısa özellik.",
                      "Melekler. Nurdan yaratılmışlardır, iradeleri yoktur, yemezler.",
                      P("Varlıkların adı:", "melekler", ["cinler", "insanlar"], k=["melek"]),
                      P("1. özellik:", "nurdan yaratılmışlardır", ["ateşten yaratılmışlardır", "topraktan yaratılmışlardır"], k=NUR),
                      P("2. özellik:", "iradeleri yoktur", ["istedikleri gibi davranırlar", "emirlere karşı gelirler"], k=IRADE),
                      P("3. özellik:", "yemezler, içmezler, uyumazlar", ["akşamları yemek yerler", "yorulup dinlenirler"], k=YEMEZ))]},
        {"metin": ["Melekler, Allah'ın yarattığı varlıklardandır ve onların diğer varlıklardan farklı özellikleri vardır."],
         "maddeler": [IK(M("a", "Meleklerin özelliklerinden beş tanesini yazınız.", "Nurdan yaratılmışlardır. İradeleri yoktur. Allah'ın emirlerine karşı gelmezler. Yemezler, içmezler, uyumazlar. Hızlı ve güçlüdürler.",
                        [A("Nurdan yaratılmış", *NUR), A("İradeleri yok", *IRADE), A("Emre karşı gelmez", *KARSI), A("Yemez, içmez, uyumaz", "yemez", "içmez", "uyumaz"), A("Hızlı ve güçlü", "hızlı", "güçlü", "cinsiyet")], "ozellik"),
                      ["özelliklerinden beş tanesini"], "Beş özellik → kısa kısa yaz: nur, irade, emir, yemez, hızlı.",
                      "Nurdan yaratılmışlardır, iradeleri yoktur, emre karşı gelmezler, yemezler, hızlı ve güçlüdürler.",
                      P("Nereden yaratıldılar:", "nurdan yaratılmışlardır", ["ateşten yaratılmışlardır", "topraktan yaratılmışlardır"], k=NUR),
                      P("Seçme gücü:", "iradeleri yoktur", ["kendileri seçerler", "istedikleri gibi yaşarlar"], k=IRADE),
                      P("Allah'ın buyrukları:", "emre karşı gelmezler", ["bazen karşı gelirler", "kendi bildiğini yaparlar"], k=KARSI),
                      P("İhtiyaçları:", "yemezler, içmezler, uyumazlar", ["akşamları yemek yerler", "yorulup dinlenirler"], k=["yemez", "içmez", "uyumaz"]),
                      P("Hareketleri:", "hızlı ve güçlüdürler", ["çok yavaştırlar", "zayıftırlar"], k=["hızlı", "güçlü"]))]}])

Y.meb(id="m2", no=2, kazanim=K1, oncelik=3,
    metin=["Aşağıdaki tabloyu belirtilen meleklerin isimlerini yazarak doldurunuz."], svg=Z.tablo_gruplar(),
    maddeler=[
        KA(M("a", "“Dört Büyük Melek” satırına gelecek isimleri yazınız.", "Cebrail, Mikâil, Azrail, İsrafil",
             [A("Cebrail", "cebrail"), A("Mikâil", "mikail"), A("Azrail", "azrail"), A("İsrafil", "israfil")], "isim"),
           {"tur": "eslestir", "soru": "Dört büyük meleği görevleriyle eşleştir.",
            "ciftler": [{"sol": "Vahiy getirir", "sag": "Cebrail"}, {"sol": "Can alır", "sag": "Azrail"}, {"sol": "Tabiat olayları, rızık", "sag": "Mikâil"}, {"sol": "Sûra üfler", "sag": "İsrafil"}],
            "aciklama": "Dört büyük melek: Cebrail, Azrail, Mikâil ve İsrafil. (s. 19)"},
           "Cebrail, Azrail, Mikâil, İsrafil", ["isimleri"], K_TAB),
        KA(M("b", "“Yazıcı Melekler” ve “Sorgu Melekleri” satırlarına gelecek isimleri yazınız.", "Yazıcı melekler: Kiramen Kâtibin. Sorgu melekleri: Münker ve Nekir.",
             [A("Kiramen Kâtibin", "kiramen", "katibin"), A("Münker ve Nekir", "münker", "nekir")], "isim"),
           {"tur": "bosluk", "cumleler": [{"c": "Yazıcı melekler: ___", "cevap": "Kiramen Kâtibin"}, {"c": "Sorgu melekleri: ___", "cevap": "Münker ve Nekir"}],
            "havuz": ["Mikâil", "Azrail"], "aciklama": "Kiramen Kâtibin yazar, Münker ve Nekir sorgular. (s. 19)"},
           "Kiramen Kâtibin; Münker ve Nekir", ["isimleri"])],
    ikizler=[
        {"metin": ["Kur'an-ı Kerim ve hadislerde en çok bilinen melekler dört büyük melek olarak adlandırılır."],
         "maddeler": [IK(M("a", "Dört büyük meleğin isimlerini ve görevlerini yazınız.", "Cebrail: vahiy getirir. Azrail: can alır. Mikâil: tabiat olaylarıyla görevlidir. İsrafil: sûra üfler.",
                        [AS("Cebrail: vahiy", ["cebrail"], ["vahiy"]), AS("Azrail: can alma", ["azrail"], ["can al", "canını"]), AS("Mikâil: tabiat olayları", ["mikail"], ["tabiat", "rızı", "yağmur"]), AS("İsrafil: sûra üfleme", ["israfil"], ["üfle", "sûr", "sur"])], "isim"),
                      ["isimlerini ve görevlerini"], "İsim + görev → her satıra bir melek: “Adı: görevi”.",
                      "Cebrail: vahiy getirir. Azrail: can alır. Mikâil: tabiat olayları. İsrafil: sûra üfler.",
                      P("1. melek ve görevi:", "Cebrail: vahiy getirir", ["Cebrail: can alır", "Mikâil: vahiy getirir"], hepsi=[["cebrail"], ["vahiy"]]),
                      P("2. melek ve görevi:", "Azrail: can alır", ["Azrail: sûra üfler", "İsrafil: can alır"], hepsi=[["azrail"], ["can al", "canını"]]),
                      P("3. melek ve görevi:", "Mikâil: tabiat olayları", ["Mikâil: vahiy getirir", "Azrail: tabiat olayları"], hepsi=[["mikail"], ["tabiat", "rızı", "yağmur"]]),
                      P("4. melek ve görevi:", "İsrafil: sûra üfler", ["İsrafil: can alır", "Cebrail: sûra üfler"], hepsi=[["israfil"], ["üfle"]]))]},
        {"metin": ["Dört büyük meleğin dışında kitabımızda adı geçen başka melekler de vardır."],
         "maddeler": [IK(M("a", "Yazıcı meleklerin adını ve görevini yazınız.", "Kiramen Kâtibin. Görevleri kişinin sevap ve günahlarını amel defterine yazmaktır.",
                        [A("Kiramen Kâtibin", "kiramen", "katibin"), A("Sevap ve günahı yazar", "yazar", "yazmak", "kayded")], "isim"),
                      ["adını ve görevini"], "Ad + görev → “Adı: görevi” diye yaz.",
                      "Kiramen Kâtibin: sevap ve günahları yazar.",
                      P("Adı:", "Kiramen Kâtibin", ["Münker ve Nekir", "Azrail"], k=["kiramen", "katibin"]),
                      P("Görevi:", "sevap ve günahları yazar", ["vahiy getirir", "sûra üfler"], k=["yazar", "yazmak", "kayded"])),
                      IK(M("b", "Sorgu meleklerinin adını ve görevini yazınız.", "Münker ve Nekir. Görevleri insanları sorguya çekmektir.",
                        [A("Münker ve Nekir", "münker", "nekir"), A("Sorguya çeker", "sorgu", "hesaba çek")], "isim"),
                      ["adını ve görevini"], "Ad + görev → “Adı: görevi” diye yaz.",
                      "Münker ve Nekir: insanları sorguya çeker.",
                      P("Adı:", "Münker ve Nekir", ["Kiramen Kâtibin", "Mikâil"], k=["münker", "nekir"]),
                      P("Görevi:", "insanları sorguya çeker", ["yağmur yağdırır", "can alır"], k=["sorgu", "hesaba çek"]))]}])

Y.meb(id="m3", no=3, kazanim=K1, oncelik=3,
    metin=["Aşağıda görevleri verilen meleklerin isimlerini yazınız.",
           "1. Allah'ın (cc) emirlerini peygamberlere iletmekle görevlidir.", "2. Yaşam süresini tamamlayanların canını almakla görevlidir.", "3. Kabirde insanları hesaba çekmekle görevlidir.",
           "4. İnsanların yaptıkları iyilik ve kötülükleri kaydetmekle görevlidir.", "5. Tabiat olaylarıyla görevlidir.", "6. Kıyamet günü sûra üflemekle görevlidir."],
    maddeler=[
        KA(M("a", "1, 2 ve 3 numaralı görevleri yapan meleklerin isimlerini sırayla yazınız.", "1. Cebrail 2. Azrail 3. Münker ve Nekir",
             [A("1: Cebrail", "cebrail"), A("2: Azrail", "azrail"), A("3: Münker ve Nekir", "münker", "nekir")], "isim"),
           {"tur": "eslestir", "soru": "Görevi meleğin adıyla eşleştir.",
            "ciftler": [{"sol": "1. Emirleri peygamberlere iletir", "sag": "Cebrail"}, {"sol": "2. Canını alır", "sag": "Azrail"}, {"sol": "3. Kabirde hesaba çeker", "sag": "Münker ve Nekir"}],
            "aciklama": "Vahiy Cebrail, can Azrail, kabirde sorgu Münker ve Nekir. (s. 19)"},
           "1 Cebrail, 2 Azrail, 3 Münker ve Nekir", ["meleklerin isimlerini"], K_AD),
        KA(M("b", "4, 5 ve 6 numaralı görevleri yapan meleklerin isimlerini sırayla yazınız.", "4. Kiramen Kâtibin 5. Mikâil 6. İsrafil",
             [A("4: Kiramen Kâtibin", "kiramen", "katibin"), A("5: Mikâil", "mikail"), A("6: İsrafil", "israfil")], "isim"),
           {"tur": "eslestir", "soru": "Görevi meleğin adıyla eşleştir.",
            "ciftler": [{"sol": "4. İyilik ve kötülükleri kaydeder", "sag": "Kiramen Kâtibin"}, {"sol": "5. Tabiat olaylarıyla görevli", "sag": "Mikâil"}, {"sol": "6. Kıyamet günü sûra üfler", "sag": "İsrafil"}],
            "aciklama": "Yazan Kiramen Kâtibin, tabiat olayları Mikâil, sûr İsrafil. (s. 19)"},
           "4 Kiramen Kâtibin, 5 Mikâil, 6 İsrafil", ["meleklerin isimlerini"])],
    ikizler=[
        {"metin": ["I. “O, kullarının üstünde yegâne kudret ve tasarruf sahibidir. Size koruyucular gönderir. Nihayet birinize ölüm geldi mi elçilerimiz (görevli melekler) onun canını alırlar. Onlar vazifede kusur etmezler.” (En'am suresi 61. ayet)",
                   "II. “Şunu iyi bilin ki üzerinizde bekçiler, değerli yazıcılar vardır; onlar, yapmakta olduklarınızı bilir.” (İnfitâr suresi, 10-12. ayetler)"],
         "maddeler": [IK(M("a", "I. ayette hangi melekten bahsedilmiştir?", "Azrail", [A("Azrail", "azrail")], "isim"),
                      ["hangi melekten"], "Ayetten melek → görevi anlatan kelimeyi bul: “canını alırlar”.", "Azrail",
                      P("Canı alan melek:", "Azrail", ["Mikâil", "İsrafil"], k=["azrail"])),
                      IK(M("b", "II. ayette özellikleri bildirilen meleklerin adını yazınız.", "Kiramen Kâtibin", [A("Kiramen Kâtibin", "kiramen", "katibin")], "isim"),
                      ["meleklerin adını"], "Ayetten melek → görevi anlatan kelimeyi bul: “değerli yazıcılar”.", "Kiramen Kâtibin",
                      P("Yazıcı melekler:", "Kiramen Kâtibin", ["Münker ve Nekir", "Cebrail"], k=["kiramen", "katibin"]))]},
        {"metin": ["Aşağıda görevleri verilen meleklerin isimlerini yazınız.", "1. Rızıkların dağıtılması, yağmurların yağması ile görevlidir.", "2. Allah'ın emir ve yasaklarını peygamberlerine bildirir.", "3. Kıyametin kopması ve ölümden sonra diriliş sırasında sûra üfler.", "4. İnsanları sorguya çeker."],
         "maddeler": [IK(M("a", "Görevleri verilen meleklerin isimlerini sırayla yazınız.", "1. Mikâil 2. Cebrail 3. İsrafil 4. Münker ve Nekir",
                        [A("1: Mikâil", "mikail"), A("2: Cebrail", "cebrail"), A("3: İsrafil", "israfil"), A("4: Münker ve Nekir", "münker", "nekir")], "isim"),
                      ["meleklerin isimlerini"], K_AD, "1 Mikâil, 2 Cebrail, 3 İsrafil, 4 Münker ve Nekir",
                      P("1:", "Mikâil", ["Azrail", "Cebrail"], k=["mikail"]),
                      P("2:", "Cebrail", ["İsrafil", "Azrail"], k=["cebrail"]),
                      P("3:", "İsrafil", ["Azrail", "Mikâil"], k=["israfil"]),
                      P("4:", "Münker ve Nekir", ["Kiramen Kâtibin", "Cebrail"], k=["münker", "nekir"]))]}])

Y.meb(id="m4", no=4, kazanim=K2, oncelik=3,
    metin=["Ayetlerde altı çizili yerlerde ahiret hayatının hangi aşamasından bahsedildiğini tespit ederek bu kavramları kutucuk içerisindeki boş bırakılan alanlara yazınız."], svg=Z.tablo_ayetler(),
    maddeler=[KA(M("a", "1'den 5'e kadar kutucuklara gelecek kavramları sırayla yazınız.", "1. Baas 2. Mizan 3. Haşir veya Mahşer 4. Cennet 5. Kıyamet",
        [A("1: Baas", "baas", "ba's"), A("2: Mizan", "mizan"), A("3: Mahşer", "mahşer", "haşir", "haşr"), A("4: Cennet", "cennet"), A("5: Kıyamet", "kıyamet")], "asama"),
        {"tur": "eslestir", "soru": "Altı çizili ifadeyi ahiret aşamasıyla eşleştir.",
         "ciftler": [{"sol": "diriltileceksiniz", "sag": "Baas"}, {"sol": "adalet terazileri", "sag": "Mizan"}, {"sol": "O'nun huzurunda toplanacaksınız", "sag": "Mahşer"}, {"sol": "mükâfat verir", "sag": "Cennet"}, {"sol": "sûra üflenecek", "sag": "Kıyamet"}],
         "aciklama": "Dirilme baas, terazi mizan, toplanma mahşer, mükâfat cennet, sûr kıyamet. (s. 26–28)"},
        "1 Baas, 2 Mizan, 3 Mahşer, 4 Cennet, 5 Kıyamet", ["kutucuklara gelecek kavramları"], K_AS)],
    ikizler=[
        {"metin": ["I. “Allah onları topladığı vakit, sanki (dünyada) sadece günün bir saatinde, aralarında tanışacak kadar kısa bir süre kaldıklarını düşünürler…” (Yunus suresi 45. ayet)",
                   "II. “Biz, kıyamet günü için adalet terazileri kurarız; artık kimseye hiçbir şekilde haksızlık edilmez. Yapılan, bir hardal tanesi kadar dahi olsa onu getirir ortaya koyarız…” (Enbiyâ suresi, 47. ayet)"],
         "maddeler": [IK(M("a", "I. ayette ahiret hayatının aşamalarının hangisinden bahsedildiğini yazınız.", "Mahşer (haşir)", [A("Mahşer", "mahşer", "haşir", "haşr")], "asama"),
                      ["hangisinden bahsedildiğini"], K_AS, "Mahşer",
                      P("“Topladığı vakit”:", "mahşer", ["mizan", "baas"], k=["mahşer", "haşir", "haşr"])),
                      IK(M("b", "II. ayetteki “adalet terazileri” ifadesinin ahiret hayatının hangi aşamasıyla ilgili olduğunu yazınız.", "Mizan", [A("Mizan", "mizan")], "asama"),
                      ["hangi aşamasıyla"], K_AS, "Mizan",
                      P("Terazi:", "mizan", ["mahşer", "kıyamet"], k=["mizan"])),
                      IK(M("c", "İnsanların dünya hayatında yaptıklarıyla ilgili hesap vermek için toplanacakları yerin adını yazınız.", "Mahşer", [A("Mahşer", "mahşer")], "asama"),
                      ["toplanacakları yerin adını"], "Yerin adı → toplanılan yer: mahşer.", "Mahşer",
                      P("Toplanma yeri:", "mahşer", ["mizan", "cennet"], k=["mahşer"]))]},
        {"metin": ["I. “Kâfirler: ‘Allah, ölen kimseyi bir daha diriltmez!’ diye var güçleriyle yemin ediyorlar. Hayır, elbette diriltecek! Bu, O'nun gerçekleşmesini üzerine aldığı kesin bir sözüdür…” (Nahl suresi 38. ayet)",
                   "II. “O gün sûra üflenecek, ardından Allah'ın diledikleri dışında göklerde ve yerde bulunanların hepsi ölecek; sonra sûra yeniden üflenecek ve onlar birden ayağa kalkmış, etrafa bakıyor olacaklar.” (Zümer suresi, 68. ayet)"],
         "maddeler": [IK(M("a", "I. ayette ahiret hayatının aşamalarının hangisinden bahsedildiğini yazınız.", "Baas", [A("Baas", "baas", "ba's", "diriliş")], "asama"),
                      ["hangisinden bahsedildiğini"], K_AS, "Baas",
                      P("“Elbette diriltecek”:", "baas", ["mizan", "cennet"], k=["baas", "ba's"])),
                      IK(M("b", "II. ayetin ahiret hayatının aşamalarından hangileri ile ilgili olduğunu yazınız.", "Kıyamet ve baas", [A("Kıyamet", "kıyamet"), A("Baas", "baas", "ba's", "diriliş")], "asama"),
                      ["hangileri ile ilgili"], "Hangileri → iki üfleyişe bak: ilki kıyamet, ikincisi baas.", "Kıyamet ve baas",
                      P("İlk üfleyiş:", "kıyamet", ["mizan", "mahşer"], k=["kıyamet"]),
                      P("Yeniden üfleyiş:", "baas", ["cennet", "cehennem"], k=["baas", "ba's"]))]}])

ORNEK5 = "Dünya hayatında, hiçbir canlının yaşam süresi sonsuz değildir. Her canlı için Allah (cc) tarafından belirlenmiş bir yaşam süresi vardır. Bu sürenin dolmasıyla gerçekleşen durum, insanoğlu için bir yok oluş değil sonsuz bir hayatın başlangıcıdır. Kıyametten sonra ahiret hayatında yeniden diriliş bir hakikattir. Bu durum Kur'an-ı Kerim'de “O … yeryüzünü ölümünün ardından canlandırıyor. İşte siz de böyle (diriltilip) çıkarılacaksınız.” (Rum suresi 19. ayet) ayetiyle insanın yeniden dirilişi doğanın baharda yeniden canlanmasına benzetilmiştir. İnsanın dünya hayatında yaptıklarını içeren kayıtların ilahi bir terazide değerlendirileceği ahiret hayatının aşamaları bunlarla sınırlı değildir."
Y.meb(id="m5", no=5, kazanim=K2, oncelik=2, metin=[ORNEK5],
    maddeler=[
        Q(M("a", "Metinde ahiret hayatının aşamalarıyla ilgili yer verilen kavramları yazınız.", "Ömür, ecel, baas, amel defteri, mizan.",
            [A("Ömür (yaşam süresi)", "ömür", "yaşam süresi"), A("Ecel (sürenin dolması)", "ecel", "ölüm"), A("Baas (yeniden diriliş)", "baas", "ba's", "diriliş"), A("Amel defteri (kayıtlar)", "amel", "kayıt"), A("Mizan (ilahi terazi)", "mizan", "terazi")], "metinde"),
          ["yer verilen kavramları"], K_VAR,
          B("Ömür, ecel, baas, amel defteri, mizan.", "Baas, mizan.", "Mahşer, cennet, cehennem.",
            "Metindeki ifadeleri kavrama çevir: yaşam süresi, sürenin dolması, yeniden diriliş, kayıtlar, terazi.",
            "MEB'in cevabı: ömür, ecel, baas, amel defteri, mizan. (s. 25, 27; MEB örnek sorusu)",
            P("“Belirlenmiş süre”:", "ömür", ["mahşer", "cennet"], k=["ömür"]),
            P("“Sürenin dolması”:", "ecel", ["mahşer", "cehennem"], k=["ecel"]),
            P("“Canlanma” sözü:", "baas", ["cehennem", "mahşer"], k=["baas", "ba's"]),
            P("“İçinde yaptıkları yazan”:", "amel defteri", ["mizan", "cennet"], k=["amel"]),
            P("“İlahi tartı”:", "mizan", ["baas", "mahşer"], k=["mizan"]))),
        Q(M("b", "Metinde yer verilmeyen ahiret hayatının aşamalarını tespit ederek yazınız.", "Mahşer, cennet, cehennem.",
            [A("Mahşer", "mahşer"), A("Cennet", "cennet"), A("Cehennem", "cehennem")], "metinde"),
          ["yer verilmeyen"], K_YOK,
          B("Mahşer, cennet, cehennem.", "Mahşer.", "Baas, mizan, amel defteri.",
            "Aşamaların sırasını aklından geçir: metinde olmayanları seç.",
            "Metinde mahşer, cennet ve cehennem yok. (MEB'in cevabında kıyamet de var ama metinde “Kıyametten sonra” geçiyor; yazmak şart değil.) (s. 26–28; MEB örnek sorusu)",
            P("Toplanma yeri:", "mahşer", ["mizan", "baas"], k=["mahşer"]),
            P("Mükâfat yeri:", "cennet", ["mizan", "mahşer"], k=["cennet"]),
            P("Ceza yeri:", "cehennem", ["baas", "mizan"], k=["cehennem"])))],
    ikizler=[
        {"metin": ["Belirlenen süre dolunca her insan ölümü tadar. Dünya için takdir edilen süre bitince İsrafil sûra üfler ve kıyamet kopar. Sonra insanlar yaptıklarının hesabını vermek üzere mahşerde toplanır."],
         "maddeler": [IK(M("a", "Metinde ahiret hayatının aşamalarıyla ilgili yer verilen kavramları yazınız.", "Ölüm, kıyamet, mahşer.",
                        [A("Ölüm", "ölüm"), A("Kıyamet", "kıyamet"), A("Mahşer", "mahşer")], "metinde"),
                      ["yer verilen kavramları"], K_VAR, "Ölüm, kıyamet, mahşer.",
                      P("Birinci aşama:", "ölüm", ["cennet", "mizan"], k=["ölüm"]),
                      P("Sûra üflenince:", "kıyamet", ["mizan", "cennet"], k=["kıyamet"]),
                      P("Toplanma:", "mahşer", ["mizan", "cehennem"], k=["mahşer"])),
                      IK(M("b", "Metinde yer verilmeyen ahiret hayatının aşamalarını yazınız.", "Baas, mizan, cennet, cehennem.",
                        [A("Baas", "baas", "ba's"), A("Mizan", "mizan"), A("Cennet", "cennet"), A("Cehennem", "cehennem")], "metinde"),
                      ["yer verilmeyen"], K_YOK, "Baas, mizan, cennet, cehennem.",
                      P("Diriliş:", "baas", ["ölüm", "kıyamet"], k=["baas", "ba's"]),
                      P("Terazi:", "mizan", ["mahşer", "ölüm"], k=["mizan"]),
                      P("Sonuç yerleri:", "cennet, cehennem", ["kıyamet, ölüm", "mahşer, ölüm"], hepsi=[["cennet"], ["cehennem"]]))]},
        {"metin": ["İsrafil sûra ikinci kez üflediğinde insanlar yeniden diriltilir. İnsanların sevap ve günahları manevi bir terazide tartılır. Sevabı ağır gelen kişi sonsuz mükâfat yerine gider."],
         "maddeler": [IK(M("a", "Metinde ahiret hayatının aşamalarıyla ilgili yer verilen kavramları yazınız.", "Baas, mizan, cennet.",
                        [A("Baas", "baas", "ba's", "diriliş", "diriltil"), A("Mizan", "mizan", "terazi"), A("Cennet", "cennet", "mükâfat")], "metinde"),
                      ["yer verilen kavramları"], K_VAR, "Baas, mizan, cennet.",
                      P("Yeniden canlanma:", "baas", ["ölüm", "mahşer"], k=["baas", "ba's"]),
                      P("Tartılma:", "mizan", ["mahşer", "ölüm"], k=["mizan"]),
                      P("Sonsuz ödül yeri:", "cennet", ["cehennem", "ölüm"], k=["cennet"])),
                      IK(M("b", "Metinde yer verilmeyen ahiret hayatının aşamalarını yazınız.", "Ölüm, kıyamet, mahşer, cehennem.",
                        [A("Ölüm", "ölüm"), A("Kıyamet", "kıyamet"), A("Mahşer", "mahşer"), A("Cehennem", "cehennem")], "metinde"),
                      ["yer verilmeyen"], K_YOK, "Ölüm, kıyamet, mahşer, cehennem.",
                      P("Dünya hayatının bitişi:", "ölüm", ["baas", "mizan"], k=["ölüm"]),
                      P("İlk üfleyiş:", "kıyamet", ["baas", "mizan"], k=["kıyamet"]),
                      P("Toplanma:", "mahşer", ["mizan", "cennet"], k=["mahşer"]),
                      P("Ceza yeri:", "cehennem", ["cennet", "mizan"], k=["cehennem"]))]}])

BAAS = ["baas", "ba's", "dirilir", "dirilme", "diriliş"]
MIZAN = ["mizan", "tartıl", "terazi"]
KARS = ["cennet", "cehennem", "karşılığ"]
Y.meb(id="m6", no=6, kazanim=K2, oncelik=1,
    metin=["Kur'an-ı Kerim'de “O gün insanlar amellerinin kendilerine gösterilmesi için bölük bölük kabirlerinden çıkacaklardır. Artık kim zerre ağırlığınca bir hayır işlerse onun mükafatını görecektir. Kim de zerre ağırlığınca bir kötülük işlerse onun cezasını görecektir.” (Zilzal suresi 6-8. ayetler) buyurulmaktadır."],
    maddeler=[Q(M("a", "Ahiret hayatının yukarıdaki ayetlerde bahsedilen aşamaları arasındaki ilişkiyi açıklayınız.",
        "İnsanların bölük bölük kabirlerinden çıkması yeniden dirilişi (baası) temsil eder. Baastan sonra kurulacak mizanda insanların yaptıkları tartılır; en küçük iyilik ve kötülük bile karşılıksız kalmaz. Mizandaki sonuca göre iyilikleri ağır gelenler cennetle ödüllendirilir, kötülükleri fazla olanlar cehennemle karşılaşır.",
        [A("Baas: kabirlerden çıkma, dirilme", *BAAS), A("Mizan: yapılanların tartılması", *MIZAN), A("Karşılık: cennet ya da cehennem", *KARS)], "iliski"),
        ["aşamaları arasındaki ilişkiyi"], K_IL,
        B("Önce baas olur, insanlar dirilir. Sonra mizanda yaptıkları tartılır. Sonunda cennet ya da cehennemde karşılığını görür.", "Önce baas olur, insanlar dirilir.", "Önce cennete girilir, sonra kıyamet kopar.",
          "Ayette üç şey var: kabirden çıkma, zerre ağırlığınca tartılma, karşılığını görme. Sırayla yaz.",
          "Kabirden çıkma baas; ardından mizanda tartılma; sonra cennet ya da cehennem. (s. 27–28; MEB örnek sorusu)",
          P("Önce", "baas olur, insanlar dirilir", ["okul biter", "herkes uyur"], k=BAAS),
          P("Sonra", "mizanda yaptıkları tartılır", ["hiçbir şey sorulmaz", "herkes unutulur"], k=MIZAN),
          P("Sonunda", "cennet ya da cehennemde karşılığını görür", ["hiçbir şey olmaz", "her şey unutulur"], k=KARS)))],
    ikizler=[
        {"metin": ["Ahiret hayatı aşamalardan oluşur."],
         "maddeler": [IK(M("a", "Ahiret hayatının aşamalarını sırasına göre yazınız.", "Ölüm, kıyamet, baas, mahşer, mizan, cennet ve cehennem.",
                        [AS("Doğru sıra", ["ölüm"], ["kıyamet"], ["baas", "ba's", "diriliş"], ["mahşer", "haşir"], ["mizan"], ["cennet", "cehennem"])], "iliski"),
                      ["sırasına göre"], "Sıra → Ölüm, kıyamet, baas, mahşer, mizan, cennet-cehennem.",
                      "Ölüm, kıyamet, baas, mahşer, mizan, cennet-cehennem.",
                      P("İlk üç:", "ölüm, kıyamet, baas", ["baas, ölüm, kıyamet", "kıyamet, ölüm, baas"], sira=[["ölüm"], ["kıyamet"], ["baas", "ba's"]]),
                      P("Son üç:", "mahşer, mizan, cennet-cehennem", ["cennet-cehennem, mizan, mahşer", "mizan, mahşer, cennet-cehennem"], sira=[["mahşer"], ["mizan"], ["cennet", "cehennem"]]))]},
        {"metin": ["Ahiret gününde insanların dünyada yaptıkları davranışlar değerlendirilecektir."],
         "maddeler": [IK(M("a", "Mizanın ne zaman kurulacağını ve bu sırada ne olacağını kısaca açıklayınız.", "Mizan, mahşerde amel defterleri verildikten sonra kurulur. Bu sırada sevap ve günahlar tartılır; sevabı ağır gelenler mükâfatlandırılır, günahı ağır gelenler cezalandırılır.",
                        [A("Ne zaman: amel defterleri verildikten sonra", "amel defter", "mahşer", "hesap"), A("Ne olur: sevap ve günahlar tartılır", "tartıl", "tartı"), A("Sonuç: mükâfat ya da ceza", "mükâfat", "ceza", "cennet", "cehennem")], "iliski"),
                      ["ne zaman kurulacağını", "ne olacağını"], "İki soru → “Ne zaman: … Ne olur: …”",
                      "Amel defterleri verildikten sonra kurulur. Sevap ve günahlar tartılır, karşılığı cennet ya da cehennemdir.",
                      P("Ne zaman:", "amel defterleri verildikten sonra", ["dünya hayatında", "ölmeden önce"], k=["amel defter", "mahşer", "hesap"]),
                      P("Ne olur:", "sevap ve günahlar tartılır", ["herkes uyur", "kimse sorulmaz"], k=["tartıl", "tartı"]),
                      P("Sonuç:", "mükâfat ya da ceza verilir", ["kimseye bir şey olmaz", "hepsi unutulur"], k=["mükâfat", "ceza"]))]}])

Y.meb(id="m7", no=7, kazanim=K3, oncelik=3,
    metin=["Din kültürü ve ahlak bilgisi dersinde “Melek ve ahiret inancının insana kazandırdıkları” konusunu işleyen öğretmen, tahtaya şu ayeti ve hadisi yazdı:",
           "“…Asıl erdemli kişi Allah'a, âhiret gününe, meleklere, kitaba ve peygamberlere iman eden; sevdiği maldan yakınlara, yetimlere, yoksullara, yolda kalmışlara, yardım isteyenlere ve özgürlüğünü kaybetmiş olanlara harcayan; namazı kılıp zekâtı verendir. Böyleleri anlaşma yaptıklarında sözlerini tutarlar; darlıkta, hastalıkta ve savaş zamanında sabrederler. İşte doğru olanlar bunlardır ve işte takva sahipleri bunlardır.” (Bakara suresi 177. ayet)",
           "“Allah'a ve ahiret gününe iman eden kimse, komşusuna eziyet etmesin! Allah'a ve ahiret gününe iman eden kimse, misafirine ikramda bulunsun! Allah'a ve ahiret gününe iman eden kimse, ya hayır söylesin ya da sussun!” (Buhari, “Edeb”, 31.)"],
    maddeler=[
        Q(M("a", "Yukarıdaki ayet ve hadisi ilke edinen bireyin günlük yaşamında göstermesi beklenen üç davranışı yazınız.",
            "Komşularıyla iyi geçinir, karşılıklı saygıya dayalı ilişkiler kurar. Evine gelen misafirleri güler yüzle karşılayıp ikramda bulunur. Faydalı ve güzel konuşmaya özen gösterir. Yardımsever olur.",
            [A("Komşusuna eziyet etmez", "komşu"), A("Misafirine ikram eder", "misafir", "ikram"), A("Üçüncü davranış: güzel söz, yardım, sözünü tutma", "güzel söz", "hayır söyle", "güzel konuş", "faydalı", "sus", "yardım", "sözünü tut", "sabr")], "davranis"),
          ["üç davranışı"], K_DAV,
          B("Komşusuna eziyet etmez. Misafirine ikram eder. Güzel söz söyler.", "Komşusuna eziyet etmez.", "Çok çalışır. Erken uyur. Ödevini yapar.",
            "Üç davranış istiyor: hadiste üç öğüt var, sırayla yaz.",
            "Hadisteki üç öğüt: komşuya eziyet etmemek, misafire ikram, hayır söylemek ya da susmak. Ayetteki yardım ve sözünde durma da olur. (s. 32, 34; MEB örnek sorusu)",
            P("1. davranış:", "komşusuna eziyet etmez", ["çok televizyon izler", "geç uyur"], k=["komşu"]),
            P("2. davranış:", "misafirine ikram eder", ["kapıyı kapatır", "evden çıkmaz"], k=["misafir", "ikram"]),
            P("3. davranış:", "güzel söz söyler", ["kötü söz söyler", "bağırır"], k=["güzel söz", "hayır söyle", "güzel konuş"]))),
        Q(M("b", "Ayet ve hadiste bahsedilen davranışların ortaya çıkmasında melek ve ahiret inancının etkisini üç cümleyle açıklayınız.",
            "Meleklerin ve ahiret hayatının varlığına inanan bir insan, yaptığı her davranışın görüldüğünü ve kaydedildiğini bilir. Ahirette bu davranışların hesabını vereceğini bildiği için sorumluluk bilinciyle hareket eder. Bu inanç sayesinde doğru davranışlar yapmaya yönelir ve kötülüklerden uzak durur.",
            [A("Yapılanlar görülür, yazılır", "kaydedil", "görül", "yazıl"), A("Hesap verecek, sorumlu", "hesab", "hesap", "sorumlu"), A("Kötülükten uzak durur, iyiye yönelir", "kötü", "iyi", "doğru davran")], "etki"),
          ["etkisini üç cümleyle"], K_ET,
          B("Yaptıklarının yazıldığını bilir. Ahirette hesap vereceğini bilir. Bu yüzden kötülükten uzak durur.", "Yaptıklarının yazıldığını bilir.", "Meleklerin kanatları olduğunu bilir ve çok sevinir.",
            "Üç cümle istiyor: yazılıyor, hesap var, bu yüzden davranış.",
            "Yapılanların kaydedildiğini ve hesabının verileceğini bilen insan sorumlu davranır, kötülükten uzak durur. (s. 34–35; MEB örnek sorusu)",
            P("1. cümle:", "yaptıklarının yazıldığını bilir", ["bugün havanın güzel olduğunu bilir", "hiçbir şey bilmez"], k=["yazıl", "kaydedil", "görül"]),
            P("2. cümle:", "ahirette hesap vereceğini bilir", ["ahiretin olmadığını düşünür", "yarın tatil olduğunu bilir"], k=["hesab", "hesap", "sorumlu"]),
            P("3. cümle:", "bu yüzden kötülükten uzak durur", ["bu yüzden dilediğini yapar", "bu yüzden umursamaz"], k=["uzak dur", "kaçın", "iyiliğe yönel"])))],
    ikizler=[
        {"metin": ["Ahiret inancına sahip bireylerin davranışları, yaptıklarının hesabını vereceklerini bildikleri için günlük hayata yansır."],
         "maddeler": [IK(M("a", "Ahiret inancına sahip bireyler hangi davranışlarda bulunurlar? Üç örnek yazınız.", "Sorumluluk sahibi olurlar. İyilik yaparlar. İhtiyaç sahiplerine yardım ederler, adaleti savunurlar.",
                        [A("Sorumlu olur", "sorumlu"), A("İyilik yapar", "iyilik", "yardım"), A("Adaletli, komşusuyla iyi geçinir", "adalet", "komşu", "dürüst", "doğru")], "davranis"),
                      ["Üç örnek"], K_DAV, "Sorumlu olurlar. İyilik yaparlar. Adaletli davranırlar.",
                      P("1. örnek:", "sorumlu olurlar", ["ödevini unuturlar", "her şeyi ertelerler"], k=["sorumlu"]),
                      P("2. örnek:", "iyilik yaparlar", ["kavga ederler", "kimseye bakmazlar"], k=["iyilik", "yardım"]),
                      P("3. örnek:", "adaletli davranırlar", ["haksızlık yaparlar", "yalan söylerler"], k=["adalet", "dürüst", "doğru"]))]},
        {"metin": ["H.E., boşalttığı bir evin dolabında para dolu bir çanta buldu. Kimsenin görmediği bu anda parayı almadı; sahibinin ailesine ulaştırıp teslim etti."],
         "maddeler": [IK(M("a", "Bu kişinin davranışında melek ve ahiret inancının etkisini iki cümleyle açıklayınız.", "Yaptıklarının melekler tarafından kaydedildiğini bilir. Ahirette hesap vereceğini bildiği için haksızlıktan uzak durur.",
                        [A("Yapılanlar yazılır", "kaydedil", "yazıl", "görül"), A("Hesap verecek, haksızlıktan uzak durur", "hesab", "hesap", "haksız", "uzak dur")], "etki"),
                      ["etkisini iki cümleyle"], "Etki iki cümle → “… yazıldığını bilir.” + “Hesap vereceği için … uzak durur.”",
                      "Yaptıklarının yazıldığını bilir. Hesap vereceği için haksızlıktan uzak durur.",
                      P("1. cümle:", "yaptıklarının yazıldığını bilir", ["parayı çok sevdiğini bilir", "kimsenin görmediğini bilir"], k=["yazıl", "kaydedil"]),
                      P("2. cümle: Bu yüzden", "hesap vereceği için haksızlıktan uzak durur", ["parayı saklar", "eve götürür"], k=["hesab", "hesap", "haksız"])),
                      IK(M("b", "Bu davranışta görülen iki ahlaki değeri yazınız.", "Doğruluk ve dürüstlük; merhamet.",
                        [A("Doğruluk, dürüstlük", "doğru", "dürüst"), A("İkinci değer: emanet, merhamet, yardımseverlik", "merhamet", "yardım", "emanet", "güven")], "davranis"),
                      ["iki ahlaki değeri"], "Değer → davranışın adını yaz: doğruluk, merhamet, yardımseverlik.",
                      "Doğruluk ve merhamet.",
                      P("1. değer:", "doğruluk", ["kıskançlık", "cimrilik"], k=["doğru", "dürüst"]),
                      P("2. değer:", "merhamet", ["bencillik", "acımasızlık"], k=["merhamet", "yardım", "emanet"]))]}])

Y.meb(id="m8", no=8, kazanim=K3, oncelik=2,
    metin=["Bir kulüp etkinliğinde Eren ve Selma, “İnanç ve İnsan Davranışı” konulu bir söyleşiden çıktıktan sonra okul bahçesinde sohbet ederler. Aralarında şöyle bir konuşma geçer:",
           "Eren: “Söyleşideki konuşmacı, melek ve ahiret inancının davranışlarımızı doğrudan olumlu etkilediğini söyledi. Bir insan, kendisini koruyan ve amellerini kaydeden meleklerin varlığını bilirse hayata çok daha farklı bakar. Nitekim ayette, ‘Halbuki üzerinizde muhakkak bekçiler, değerli yazıcılar vardır.’ buyruluyor. Bu bilinçle ve her şeyin ahirette adaletle tartılacağına inanarak yaşayan birisi, zorluklar karşısında pes etmez. Bu inanç insana bir iç pusula verir ve onu sorumluluk sahibi yapar.”",
           "Selma: “Çok doğru Eren. Bence de bu inancın asıl gücü, insanı sadece ‘ödül ve ceza’ mantığından kurtarıp gerçek bir vicdan sahibi yapmasında gizli. Bir kişi, kimsenin görmediği anlarda bile haksızlık yapmıyorsa gerçek ahlaka ulaşmıştır. Çünkü bilir ki dünyada yapılan hiçbir şey karşılıksız kalmaz. Başka bir ayette dendiği gibi: ‘Artık kim zerre ağırlığınca bir hayır işlerse onun mükâfatını görecektir. Kim de zerre ağırlığınca bir kötülük işlerse onun cezasını görecektir.’ İşte karşılık beklemeden iyilik yapma isteği de tam olarak bu bilinçten doğar.”"],
    maddeler=[Q(M("a", "Selma ve Eren'in yukarıdaki konuşmalarından hareketle melek ve ahiret inancının insana kazandırdıklarını gerekçeleriyle anlatan dört cümle yazınız.",
        "Meleklerin varlığına inanmak, insana sorumluluk bilinci kazandırır. Ahirete inanmak, insanın zorluklar karşısında pes etmesini engeller. Her davranışın karşılığı olacağını bilen kişi, gizlide dahi kötülükten uzak durur. Ahirete inanan kişi, kimse görmese bile vicdanıyla hareket edip haksızlıktan kaçınır.",
        [A("Sorumluluk kazandırır", "sorumlu"), A("Zorlukta pes etmez", "pes etme", "sabr", "vazgeçme"), A("Her davranışın karşılığı var, kötülükten uzak durur", "kötülükten", "gizli"), A("Kimse görmese de vicdanlı", "vicdan", "haksızlık yapma", "haksızlıktan")], "kazanc"),
        ["kazandırdıklarını gerekçeleriyle", "dört cümle"], K_KZ,
        B("Meleklere inanan sorumlu olur, çünkü yaptıkları yazılır. Ahirete inanan pes etmez. Karşılık olduğunu bilen kötülükten uzak durur. Kimse görmese de vicdanlı davranır.", "Meleklere inanan sorumlu olur.", "Meleklerin kanatları vardır. Eren ile Selma arkadaştır.",
          "Dört cümle: Eren'den iki kazanç (sorumluluk, pes etmemek), Selma'dan iki kazanç (kötülükten uzak durmak, vicdan).",
          "Eren sorumluluk ve pes etmemeyi, Selma vicdanı ve kimse görmese de haksızlık yapmamayı söylüyor. (s. 34–35; MEB örnek sorusu)",
          P("1. Meleklere inanan", "sorumlu olur, çünkü yaptıkları yazılır", ["tembel olur", "kimseyi sevmez"], k=["sorumlu"]),
          P("2. Ahirete inanan", "zorlukta pes etmez", ["hemen bırakır", "üzülüp oturur"], k=["pes etme", "vazgeçme", "sabr"]),
          P("3. Karşılık olduğunu bilen", "kötülükten uzak durur", ["dilediğini yapar", "umursamaz"], k=["kötülükten", "gizli"]),
          P("4. Kimse görmese de", "vicdanlı davranır", ["haksızlık yapar", "kopya çeker"], k=["vicdan", "haksızlıktan"])))],
    ikizler=[
        {"metin": ["Ayşe: “Sınavda kimse görmese de kopya çekmem, çünkü meleklerin yaptıklarımı yazdığını biliyorum.”",
                   "Mert: “Çok zor bir dönem geçirdim ama pes etmedim. Dünyanın bir imtihan olduğunu ve emeğimin karşılıksız kalmayacağını biliyorum.”"],
         "maddeler": [IK(M("a", "Ayşe ve Mert'in konuşmalarından hareketle melek ve ahiret inancının insana kazandırdıklarını gerekçeleriyle anlatan iki cümle yazınız.",
                        "Meleklere inanan kişi, kimse görmese de haksızlık yapmaz; çünkü yaptıklarının yazıldığını bilir. Ahirete inanan kişi zorlukta pes etmez; çünkü dünyanın bir imtihan olduğunu bilir.",
                        [A("Kimse görmese de haksızlık yapmaz (yazıldığını bilir)", "haksızlık yapma", "kopya çekme", "yazıl", "vicdan"), A("Zorlukta pes etmez (imtihan)", "pes etme", "sabr", "imtihan")], "kazanc"),
                      ["kazandırdıklarını gerekçeleriyle", "iki cümle"], K_KZ,
                      "Yaptıklarının yazıldığını bilen haksızlık yapmaz. Dünyanın imtihan olduğunu bilen pes etmez.",
                      P("1. cümle:", "yaptıklarının yazıldığını bilen haksızlık yapmaz", ["sınavda kopya çeker", "melekleri görür"], k=["haksızlık yapma", "yazıl", "vicdan"]),
                      P("2. cümle:", "dünyanın imtihan olduğunu bilen pes etmez", ["dünyayı sevmez", "bir an önce bırakır"], k=["pes etme", "imtihan", "sabr"]))]},
        {"metin": ["Ders kitabındaki “İnanıyorum Çünkü” etkinliğindeki cümleleri tamamlayınız."],
         "maddeler": [IK(M("a", "Ahiret inancı bana sorumluluk ve hesap verme bilinci kazandırır. Çünkü …", "Çünkü yaptıklarımın hesabını vereceğimi biliyorum.",
                        [A("Yaptıklarının hesabını verir", "hesab", "hesap")], "kazanc"),
                      ["Çünkü"], "Çünkü → cümleyi gerekçeyle tamamla.", "Çünkü yaptıklarımın hesabını vereceğimi biliyorum.",
                      P("Çünkü yaptıklarımın", "hesabını vereceğimi biliyorum", ["hiç sorulmayacağını biliyorum", "unutulacağını sanıyorum"], k=["hesab", "hesap"])),
                      IK(M("b", "Ahiret inancı hayatıma anlam katar. Çünkü …", "Çünkü hayatın ölümle bitmediğini ve her şeyin bir yaratılış amacı olduğunu biliyorum.",
                        [A("Hayat ölümle bitmez, amaç var", "ölümle", "amaç", "sonsuz")], "kazanc"),
                      ["Çünkü"], "Çünkü → hayatın ölümle bitmediğini yaz.", "Çünkü hayatın ölümle bitmediğini biliyorum.",
                      P("Çünkü hayatın", "ölümle bitmediğini biliyorum", ["çok kısa olduğunu biliyorum", "boşa geçtiğini düşünüyorum"], k=["ölümle", "amaç", "sonsuz"])),
                      IK(M("c", "Meleklerin varlığına inanmak davranışlarımı düzeltmemde motivasyon sağlar. Çünkü …", "Çünkü davranışlarımın melekler tarafından kaydedildiğini biliyorum.",
                        [A("Davranışları kaydedilir", "kaydedil", "yazıl")], "kazanc"),
                      ["Çünkü"], "Çünkü → yaptıklarının yazıldığını yaz.", "Çünkü davranışlarımın kaydedildiğini biliyorum.",
                      P("Çünkü davranışlarımın", "kaydedildiğini biliyorum", ["kimse bilmeyeceğini düşünüyorum", "önemsiz olduğunu düşünüyorum"], k=["kaydedil", "yazıl"]))]}])

# =====================================================================
# LEKLE'NİN CEVABINI DÜZELT: 8 eksik (yarım cevap) + 3 yanılgı (yalnız Hatırla'daki sık hatalardan)
# =====================================================================
def KH(kazanim, tur, soru, kuark, dogruSik, yanlis1, yanlis2, ipucu, aciklama, once, ornek, sonra, k, havuz):
    Y.kuark(kazanim=kazanim, tur=tur, soru=soru, kuark=kuark, secenekler=[dogruSik, yanlis1, yanlis2], dogru=0, ipucu=ipucu, aciklama=aciklama,
            dogruCevap=f"{once} {ornek} {sonra}".replace(" .", ".").replace(" !", "!").replace(" ;", ";").strip(), tamamla={"once": once, "ornek": ornek, "sonra": sonra, "k": k, "havuz": havuz})

TAM, DOGRU_ = "Tam, eksik yok.", "Doğru, hata yok."
KH(K1, "eksik", "Dört büyük meleğin isimlerini yazınız.", "Cebrail, Azrail, Mikâil.",
   "Eksik: dördüncü melek (İsrafil) yazılmamış.", "Yanlış: yalnız Cebrail yazmalı.", TAM,
   "Dört melek istenmiş, kaç tane yazılmış?", "Dört büyük melek: Cebrail, Azrail, Mikâil ve İsrafil. (s. 19)",
   "Cebrail, Azrail, Mikâil ve", "İsrafil", ".", ["israfil"], ["Kiramen Kâtibin", "Münker"])
KH(K1, "eksik", "Sorgu meleklerinin adını yazınız.", "Münker.",
   "Eksik: iki melek var; Nekir de yazılmalı.", "Yanlış: Kiramen Kâtibin yazmalı.", TAM,
   "Sorgu melekleri kaç tane?", "Sorgu melekleri Münker ve Nekir'dir. (s. 19)",
   "Münker ve", "Nekir", ".", ["nekir"], ["Mikâil", "Azrail"])
KH(K1, "eksik", "Melekleri diğer varlıklardan ayıran özellikler nelerdir?", "Melekler gözle görülmez.",
   "Eksik: yalnız bir özellik var; başka özellikler de yazılmalı.", "Yanlış: melekler görülür.", TAM,
   "Soru “özellikler” diyor; birden çok yaz.", "Melekler görülmez, iradeleri yoktur, emre karşı gelmez. (s. 19)",
   "Melekler gözle görülmez,", "iradeleri yoktur", ".", ["irade"], ["yemek yerler", "çok yavaştırlar"])
KH(K2, "eksik", "Ahiret hayatının aşamalarını sırasına göre yazınız.", "Ölüm, kıyamet, baas.",
   "Eksik: mahşer, mizan, cennet-cehennem yazılmamış.", "Yanlış: sıra karışık.", TAM,
   "Aşamaların yarısı nerede kaldı?", "Sıra: ölüm, kıyamet, baas, mahşer, mizan, cennet-cehennem. (s. 26, 29)",
   "Ölüm, kıyamet, baas,", "mahşer, mizan, cennet-cehennem", ".", ["mahşer"], ["uyku, oyun, tatil", "okul, ders, sınav"])
KH(K2, "eksik", "Mizan nedir? Yazınız.", "Bir terazidir.",
   "Eksik: ne tartıldığı yazılmamış.", "Yanlış: mizan toplanma yeridir.", TAM,
   "Bu terazide ne tartılır?", "Mizan, sevap ve günahların tartıldığı manevi terazidir. (s. 27)",
   "Mizan,", "sevap ve günahların tartıldığı", "manevi terazidir.", ["sevap", "günah"], ["yağmurun ölçüldüğü", "suyun tartıldığı"])
KH(K3, "eksik", "Ayet ve hadisi ilke edinen bireyin göstermesi beklenen üç davranışı yazınız.", "Komşusuna eziyet etmez.",
   "Eksik: üç davranış istenmiş, bir tane yazılmış.", "Yanlış: komşu ile ilgili değil.", TAM,
   "Hadiste kaç öğüt var?", "Hadiste üç öğüt var: komşu, misafir, güzel söz. (s. 32; MEB örnek sorusu)",
   "Komşusuna eziyet etmez,", "misafirine ikram eder, güzel söz söyler", ".", ["misafir"], ["evden çıkmaz, bağırır", "geç uyur, çok yer"])
KH(K3, "eksik", "Melek ve ahiret inancının insana kazandırdıklarını gerekçesiyle yazınız.", "Sorumlu olur.",
   "Eksik: gerekçe (çünkü) yazılmamış.", "Yanlış: sorumlu olmaz.", TAM,
   "Soru “gerekçeleriyle” diyor.", "Yaptıklarının yazıldığını bilen sorumlu olur. (s. 34)",
   "Sorumlu olur, çünkü", "yaptıklarının yazıldığını bilir", ".", ["yazıl", "kaydedil", "hesap", "hesab"], ["yemek yediğini bilir", "çok yorulduğunu bilir"])
KH(K3, "eksik", "Ahirete inanmak insana ne kazandırır? Yazınız.", "Güzel şeyler kazandırır.",
   "Eksik: belirsiz; kazancın adı yazılmalı.", "Yanlış: hiçbir şey kazandırmaz.", TAM,
   "“Güzel şeyler” ne demek? Adını söyle.", "Ahirete inanan sorumlu olur, sabreder, kötülükten uzak durur. (s. 34–35)",
   "Sorumluluk ve", "sabır", "kazandırır.", ["sabır", "sabr", "pes etme", "vicdan", "huzur"], ["uyku", "yorgunluk"])
KH(K1, "yanilgi", "Vahyi peygamberlere getiren melek hangisidir?", "Mikâil.",
   "Yanlış: vahyi Cebrail getirir; Mikâil tabiat olaylarıyla görevlidir.", "Yanlış: Azrail getirir.", DOGRU_,
   "Mikâil'in görevi neydi?", "Vahiy meleği Cebrail'dir; Mikâil tabiat olaylarıyla görevlidir. (s. 19)",
   "Vahyi", "Cebrail", "getirir.", ["cebrail"], ["Azrail", "İsrafil"])
KH(K2, "yanilgi", "Mahşer nedir? Yazınız.", "Sevap ve günahların tartıldığı terazidir.",
   "Yanlış: bu mizandır; mahşer toplanma yeridir.", "Yanlış: mahşer cennetin adıdır.", DOGRU_,
   "Terazi hangi kelimeyle anılır?", "Mahşer, insanların hesap vermek için toplanacakları yerdir. (s. 25, 27)",
   "Mahşer, insanların hesap vermek için", "toplanacakları yerdir", ".", ["toplan"], ["tartılacağı terazidir", "dinleneceği yerdir"])
KH(K2, "yanilgi", "İsrafil sûra ikinci kez üfleyince ne olur?", "Kıyamet kopar.",
   "Yanlış: ilk üfleyiş kıyamet; ikinci üfleyişte baas olur, insanlar dirilir.", "Yanlış: hiçbir şey olmaz.", DOGRU_,
   "İki üfleyişi karıştırma.", "İlk üfleyiş kıyamet, ikinci üfleyiş baastır. (s. 26–27)",
   "İkinci üfleyişte", "baas olur, insanlar dirilir", ".", ["baas", "dirilir"], ["kıyamet kopar", "dünya başlar"])

# =====================================================================
# PROVA YAZILILARI (2 deneme; Senaryo 5: 1 + 2 + 3 soru, toplam 100; puanlar tahmini). Bağlamlar MEB ve benzerlerinden farklı.
# =====================================================================
Y.prova(id="p1", ad="Prova 1", sorular=[
    {"kazanim": K1, "puan": 15, "benzer": "m3",
     "maddeler": [M("a", "Ölüm vakti gelenlerin canını almakla görevli melek hangisidir?", "Azrail", [A("Azrail", "azrail")], "isim", puan=5),
                  M("b", "İnsanın sağında ve solunda bulunup sevap ve günahlarını yazan melekler hangileridir?", "Kiramen Kâtibin", [A("Kiramen Kâtibin", "kiramen", "katibin")], "isim", puan=5),
                  M("c", "Melekleri insanlardan ayıran iki özelliği yazınız.", "Nurdan yaratılmışlardır. İradeleri yoktur.", [A("Birinci özellik", *NUR, *IRADE, *GORUL), A("İkinci özellik", *IRADE, *KARSI, *YEMEZ, "hızlı")], "ozellik", puan=5)]},
    {"kazanim": K2, "puan": 15, "benzer": "m4",
     "metin": ["Aşağıdaki ayet meallerinde ahiret hayatının hangi aşamasından bahsedildiğini yazınız.",
               "I. “Her nefis ölümü tadacaktır...”", "II. “İşte o vakit, kimin tartıları ağır gelmişse, artık o, hoşnut olacağı bir hayat içinde olacaktır.”",
               "III. “O gün onların ağızlarını mühürleriz; yapmış olduklarını elleri bize anlatır, ayakları da tanıklık eder.”", "IV. “…içinden ırmaklar akan cennetler…”"],
     "maddeler": [M("a", "I, II, III ve IV numaralı ayetlerde bahsedilen aşamaları sırayla yazınız.", "I. Ölüm II. Mizan III. Mahşer IV. Cennet",
                    [A("I: Ölüm", "ölüm"), A("II: Mizan", "mizan"), A("III: Mahşer", "mahşer", "haşir"), A("IV: Cennet", "cennet")], "asama", puan=15)]},
    {"kazanim": K2, "puan": 15, "benzer": "m5",
     "metin": ["Ölüm, insan için bir yok oluş değil, yeni ve sonsuz bir hayatın başlangıcıdır. Allah'ın emriyle İsrafil sûra üfleyince kıyamet kopar. Sûra ikinci defa üflenince gerçekleşen baas ile insanlar yeniden dirilir."],
     "maddeler": [M("a", "Metinde ahiret hayatının aşamalarıyla ilgili yer verilen kavramları yazınız.", "Ölüm, kıyamet, baas.",
                    [A("Ölüm", "ölüm"), A("Kıyamet", "kıyamet"), A("Baas", "baas", "ba's")], "metinde", puan=7),
                  M("b", "Metinde yer verilmeyen ahiret hayatının aşamalarını yazınız.", "Mahşer, mizan, cennet, cehennem.",
                    [A("Mahşer", "mahşer"), A("Mizan", "mizan"), A("Cennet", "cennet"), A("Cehennem", "cehennem")], "metinde", puan=8)]},
    {"kazanim": K3, "puan": 20, "benzer": "m7",
     "metin": ["“… İyi ve yararlı işleri en güzel şekilde yapın. Şüphesiz, Allah iyi ve yararlı işleri en güzel şekilde yapanları sever.” (Bakara suresi 195. ayet)",
               "“Ey iman edenler! Allah için hakkı titizlikle ayakta tutan, adalet ile şahitlik eden kimseler olun…” (Maide suresi 8. ayet)"],
     "maddeler": [M("a", "Bu ayetleri ilke edinen bir kişinin günlük hayatında göstereceği iki davranışı yazınız.", "İyi ve yararlı işler yapar. Adaletli davranır, doğruyu söyler.",
                    [A("İyi ve yararlı işler yapar", "iyi", "yararlı", "yardım"), A("Adaletli davranır, doğruyu söyler", "adalet", "doğru", "haksız")], "davranis", puan=10),
                  M("b", "Bu davranışlarda melek ve ahiret inancının etkisini iki cümleyle açıklayınız.", "Yaptıklarının melekler tarafından yazıldığını bilir. Ahirette hesap vereceğini bildiği için kötülükten uzak durur.",
                    [A("Yapılanlar yazılır", "yazıl", "kaydedil", "görül"), A("Hesap verir, kötülükten uzak durur", "hesab", "hesap", "kötülük", "sorumlu")], "etki", puan=10)]},
    {"kazanim": K3, "puan": 20, "benzer": "m8",
     "metin": ["Can: “Okulun bahçesinde kimse görmese de çöp atmıyorum, çünkü yaptığım her şeyin kaydedildiğini biliyorum.”",
               "Deniz: “Ben de kaybettiğim maçtan sonra hemen vazgeçmedim. Dünyanın bir imtihan olduğunu biliyorum. Bir de arkadaşlarıma yardım edince karşılığını ahirette göreceğime inanıyorum.”"],
     "maddeler": [M("a", "Can ve Deniz'in konuşmalarından hareketle melek ve ahiret inancının insana kazandırdıklarını gerekçeleriyle anlatan üç cümle yazınız.",
                    "Yaptıklarının kaydedildiğini bilen kişi sorumlu olur. Dünyanın imtihan olduğunu bilen zorlukta pes etmez. Karşılığını ahirette göreceğini bilen iyilik yapar.",
                    [A("Sorumluluk", "sorumlu", "vicdan", "yazıl", "kaydedil"), A("Pes etmemek, sabır", "pes etme", "sabr", "imtihan", "vazgeçme"), A("İyilik, yardım", "iyilik", "yardım")], "kazanc", puan=20)]},
    {"kazanim": K3, "puan": 15, "benzer": "m7",
     "metin": ["Meleklerin varlığına inanmak, insanın davranışlarını etkiler."],
     "maddeler": [M("a", "Meleklerin varlığına inanmanın insana kazandırdıklarından iki tanesini yazınız.", "İnsanın kötülükten kaçınmasını ve iyiliğe yönelmesini sağlar. İnsanı manevi olarak güçlü kılar.",
                    [A("Kötülükten kaçınır, iyiliğe yönelir", "kötülük", "iyilik", "sorumlu", "haksız", "yalan"), A("Manevi güç, güzel ahlak", "manevi", "güçlü", "doğru", "merhamet", "yardım", "sevgi")], "kazanc", puan=15)]}])

Y.prova(id="p2", ad="Prova 2", sorular=[
    {"kazanim": K1, "puan": 15, "benzer": "m2",
     "metin": ["Aşağıda bazı meleklerin görevleri verilmiştir.", "I. Vahiy getirmek", "II. Yağmurların yağması, bitkilerin gelişmesi gibi tabiat olayları", "III. Kıyamet ve diriliş sırasında sûra üflemek"],
     "maddeler": [M("a", "I, II ve III numaralı görevleri yapan melekleri sırayla yazınız.", "I. Cebrail II. Mikâil III. İsrafil",
                    [A("I: Cebrail", "cebrail"), A("II: Mikâil", "mikail"), A("III: İsrafil", "israfil")], "isim", puan=9),
                  M("b", "“Melekler nurdan yaratılmıştır.” Meleklerin başka iki özelliğini yazınız.", "İradeleri yoktur. Yemezler, içmezler, uyumazlar.",
                    [A("Birinci özellik", *IRADE, *KARSI, *GORUL), A("İkinci özellik", *YEMEZ, "hızlı", "güçlü", "cinsiyet", *IRADE)], "ozellik", puan=6)]},
    {"kazanim": K2, "puan": 15, "benzer": "m6",
     "metin": ["Ahiret hayatı belirli aşamalardan oluşur."],
     "maddeler": [M("a", "Ahiret hayatının aşamalarını sırasına göre yazınız.", "Ölüm, kıyamet, baas, mahşer, mizan, cennet ve cehennem.",
                    [AS("Doğru sıra", ["ölüm"], ["kıyamet"], ["baas", "ba's"], ["mahşer", "haşir"], ["mizan"], ["cennet", "cehennem"])], "iliski", puan=8),
                  M("b", "Mahşer ile mizan arasındaki farkı yazınız.", "Mahşer insanların toplanacağı yerdir; mizan ise sevap ve günahların tartıldığı manevi terazidir.",
                    [A("Mahşer: toplanma yeri", "toplan"), A("Mizan: tartılma, terazi", "tartıl", "terazi")], "iliski", puan=7)]},
    {"kazanim": K2, "puan": 15, "benzer": "m4",
     "metin": ["Aşağıdaki ayet meallerinde ahiret hayatının hangi aşamasından bahsedildiğini yazınız.",
               "I. “Gök yarıldığı, yıldızlar saçıldığı, denizler kaynayıp fışkırtıldığı…”", "II. “Onlar, ‘Allah, ölen bir kimseyi diriltmez.’ diye Allah adını anarak en kuvvetli yeminlerini ettiler. Hayır, diriltecek!…”", "III. “…O, kızgın bir ateştir.”"],
     "maddeler": [M("a", "I, II ve III numaralı ayetlerde bahsedilen aşamaları sırayla yazınız.", "I. Kıyamet II. Baas III. Cehennem",
                    [A("I: Kıyamet", "kıyamet"), A("II: Baas", "baas", "ba's"), A("III: Cehennem", "cehennem")], "asama", puan=15)]},
    {"kazanim": K3, "puan": 20, "benzer": "m8",
     "metin": ["Elif: “Komşumuzun poşetlerini taşıdım, kimse görmedi ama iyilik yapmak için görülmeye gerek yok. Her davranışımın kaydedildiğini biliyorum.”",
               "Ali: “Ben de hastalandığımda çok zorlandım ama sabrettim. Hayatın ölümle bitmediğini ve ahirette sevdiklerimizle birlikte olacağımızı bilmek bana huzur veriyor.”"],
     "maddeler": [M("a", "Elif ve Ali'nin konuşmalarından hareketle melek ve ahiret inancının insana kazandırdıklarını gerekçeleriyle anlatan üç cümle yazınız.",
                    "Davranışlarının kaydedildiğini bilen kişi kimse görmese de iyilik yapar. Dünyanın imtihan olduğunu bilen zorlukta sabreder. Hayatın ölümle bitmediğini bilen huzur bulur.",
                    [A("Kimse görmese de iyilik yapar", "iyilik", "kaydedil", "yazıl", "vicdan"), A("Zorlukta sabreder", "sabr", "sabır", "pes etme"), A("Huzur bulur", "huzur", "ölümle")], "kazanc", puan=20)]},
    {"kazanim": K3, "puan": 20, "benzer": "m7",
     "metin": ["Melek ve ahiret inancına sahip bir kişi aşağıdaki durumlarda nasıl davranır? Birer cümleyle yazınız."],
     "maddeler": [M("a", "Sokakta yere düşmüş bir cüzdan bulduğunda:", "Cüzdanı sahibine ulaştırır.", [A("Sahibine verir", "sahib", "teslim", "götür", "polis")], "davranis", puan=7),
                  M("b", "Bir arkadaşı hakkında kötü konuşulduğunda:", "Kötü konuşmaz, ya hayır söyler ya da susar.", [A("Kötü konuşmaz, hayır söyler ya da susar", "sus", "kötü konuşma", "hayır söyle", "savun", "katılma", "güzel söz")], "davranis", puan=7),
                  M("c", "Eve misafir geldiğinde:", "Misafirini güler yüzle karşılar, ikram eder.", [A("İkram eder, güler yüzlü olur", "ikram", "güler yüz")], "davranis", puan=6)]},
    {"kazanim": K3, "puan": 15, "benzer": "m8",
     "maddeler": [M("a", "Ahiret inancının insana kazandırdıklarından iki tanesini gerekçesiyle yazınız.", "Sorumlu olur, çünkü yaptıklarının hesabını vereceğini bilir. Zorlukta sabreder, çünkü dünyanın bir imtihan olduğunu bilir.",
                    [A("Birinci kazanç ve gerekçe", "sorumlu", "hesab", "kötülük"), A("İkinci kazanç ve gerekçe", "sabr", "imtihan", "pes etme", "huzur", "anlam", "iyilik")], "kazanc", puan=15)]}])

Y.yaz()
