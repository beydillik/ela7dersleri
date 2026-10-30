"""Teknoloji ve Tasarım 7 · 1. Dönem 1. Yazılı — Yazılıya Hazırlık verisi.
OYYS senaryosu YOK: öğretmen 15 soruluk çalışma kâğıdı gönderdi, yazılıda bunlardan 10'unu soracak (Kemal, 30 Ekim 2026).
Yeni soru yazılmaz: "Öğretmenin Soruları" = kâğıttaki 15 soru (ikiz yok); Fikri'nin Hatası aynı sorulara yanlış cevaplar;
4 prova = 15 sorudan 10'ar soru (konu dağılımı 3+3+3+1 varsayımdır), her soru 10 puan.
Cevaplar ders kitabından (Karaca 2022, sayfa atıflı). Kitapta tam karşılığı olmayanlar (kaynak URL'leri kaynakNotu'nda):
  mucit (TDK), dokunun tasarıma etkileri (Ankara Üniv. açık ders, Görsel Tasarım Öge ve İlkeleri),
  valör, form, zıtlık (MEB Görsel Sanatlar programı; sitedeki u2k1–u2k3 kartlarıyla aynı).
Çalıştır: python3 araclar/yazili/bil1_d1y1.py"""
import os, sys, copy
sys.path.insert(0, os.path.dirname(__file__))
from yazili import Yazili
import cizim_bil as Z


def A(ad, *k): return {"ad": ad, "k": list(k)}
def SIRA(ad, *g): return {"ad": ad, "sira": [list(x) if isinstance(x, (list, tuple)) else [x] for x in g]}
def M(harf, soru, cevap, an, formul=None, iskele=None):
    m = {"harf": harf, "soru": soru}
    if formul: m["formul"] = formul
    if iskele: m["iskele"] = iskele
    m["cevap"] = cevap; m["anahtarlar"] = an
    return m

ELEMAN = ["nokta", "çizgi", "renk", "doku", "biçim", "form", "şekil", "yön", "aralık", "ışık", "gölge", "oran", "yazı", "valör", "değer", "mekân", "mekan"]
KESIF = ["ateş", "yer çekimi", "yerçekimi", "kaldırma kuvveti", "kıta", "gezegen", "amerika"]

Y = Yazili("bil1", "d1y1",
    baslik="1. Dönem 1. Yazılı", ders="Teknoloji ve Tasarım", senaryo="Öğretmenin çalışma kâğıdı", sure=40, tarih="2026-11-02",
    dagilim={"Ü1·A": 3, "Ü1·B": 3, "Ü2·A": 3, "Ü2·B": 1},
    soruBaslik="Öğretmenin Soruları", soruEtiket="Soru", kazanimAd="konu", ikizsiz=True,
    soruGiris="Bunlar öğretmeninin gönderdiği <b>15 soru</b>. Yazılıda bunlardan <b>10'u</b> çıkacak. Bazılarında önce kısa bir ısınma var; sonra cevabı <b>yazarak</b> ver. Eksik kalan parçalar Yanlış Defterim'e gider.",
    giris="Öğretmeninin gönderdiği çalışma kâğıdında <b>15 soru</b> var; yazılıda bunlardan <b>10'u</b> sorulacak. Hepsi 1. ve 2. üniteden. Önce 4 konu kartına bak, sonra 15 soruyu yazarak çöz, en sonda 10 soruluk prova yap.",
    kapsamDisi=["3. Ünite ve sonrası (tasarım süreci, teknik resim, ergonomi…)", "Endüstri devrimlerinin ayrıntıları (1.0–5.0)", "Ülkelerin teknoloji karşılaştırması, Ar-Ge, yeni teknolojiler",
                "Analoji ve ürünü yeniden yorumlama", "Denge, ritim, harmoni gibi diğer ilkelerin ayrıntısı"],
    puanNotu="Puanlar tahminidir: 10 soru, her biri 10 puan sayıldı. Öğretmen puanları farklı dağıtabilir.",
    kaynakNotu=("Sorular öğretmenin çalışma kâğıdından (15 soru). Cevaplar Teknoloji ve Tasarım 7 ders kitabından (Karaca, 2022). Kitap dışı: "
                "mucit, TDK tanımı (Habertürk'ün aktarımı): https://www.haberturk.com/ne-demek/mucit-ne-anlama-gelir · "
                "dokunun tasarıma etkileri: Ankara Üniversitesi Açık Ders, Görsel Tasarım Öge ve İlkeleri (Doku): https://acikders.ankara.edu.tr/mod/resource/view.php?id=101429 · "
                "valör, form, zıtlık: MEB Görsel Sanatlar Dersi Öğretim Programı (2018): https://mufredat.meb.gov.tr/Dosyalar/2018121111026326-GORSEL%20SANATLAR.pdf ve "
                "TT programı 2. ünite: https://tymm.meb.gov.tr/teknoloji-tasarim-dersi/unite/1438"))

# =====================================================================
# KONU KARTLARI (Hatırla)
# =====================================================================
Y.kazanim(kod="Ü1·A", ad="Teknoloji kavramını açıklar; buluş, keşif ve icatı ayırt eder.", kisa="Teknoloji, Keşif ve İcat", soru=3,
    soruNot="Kâğıtta 4 soru: 1, 4, 8, 9", renk="#1d6fa3", konular=["u1k1"], sayfa="s. 11", svg=Z.bulus_icat(),
    maddeler=["<b>Teknoloji:</b> Araç-gereç yapabilmek için gereken <b>bilgi ve yetenek</b>tir. Bir işi daha iyi, daha hızlı, daha kolay, daha ekonomik ve daha verimli yapma girişimidir. (s. 11)",
              "Teknolojinin amacı insan hayatının kalitesini artırmaktır. (s. 11)",
              "<b>Keşif (buluş):</b> Daha önce <b>var olan</b> ama bilinmeyen bir şeyin bulunmasıdır. Örnek: ateşin, yer çekiminin, suyun kaldırma kuvvetinin fark edilmesi; bilinmeyen bir kıtanın ya da gezegenin bulunması. (s. 11)",
              "<b>İcat:</b> Var olan teknolojilerin çaba ve araştırmayla <b>yeni ve benzersiz</b> biçimde bir araya getirilmesidir. Örnek: kibrit, araba, daktilo. (s. 11)",
              "Fark: keşifte var olan <b>bulunur</b>, icatta daha önce olmayan bir şey <b>yapılır</b>. (s. 11)",
              "İcat yapan kişiye <b>mucit</b> denir. (kitap dışı: TDK)"],
    kelimeler=["bilgi ve yetenek", "araç-gereç", "daha iyi, hızlı, kolay", "var olan ama bilinmeyen", "yeni ve benzersiz", "bir araya getirmek", "mucit"],
    hatalar=[{"yanlis": "Keşif ve icat aynı şeydir.", "dogru": "Keşif: var olanı bulmak. İcat: var olanları birleştirip yeni bir şey yapmak."},
             {"yanlis": "Keşif örneği olarak kibrit, araba yazmak.", "dogru": "Kibrit ve araba icattır. Keşif: yer çekiminin fark edilmesi, yeni bir kıtanın bulunması."},
             {"yanlis": "“Teknoloji telefon ve bilgisayardır.”", "dogru": "Bunlar teknoloji ürünü. Teknoloji, araç-gereç yapmak için gereken bilgi ve yetenektir."}])

Y.kazanim(kod="Ü1·B", ad="Tasarım kavramını açıklar; endüstri ve tasarım dallarını tanır.", kisa="Tasarım, Endüstri ve Tasarım Dalları", soru=3,
    soruNot="Kâğıtta 5 soru: 2, 3, 6, 7, 10", renk="#9b3fa6", konular=["u1k2", "u1k3"], sayfa="s. 12–14", svg=Z.tasarim_dallari(),
    maddeler=["<b>Tasarım:</b> Bir fikrin <b>zihinde canlandırılıp planlanmasıdır</b>. En önemli özelliği <b>planlama</b>dır. Bir fikrin kâğıt üzerine çizilmiş şekli de tasarımdır. (s. 13)",
              "<b>Endüstri (sanayi):</b> Makine ve benzeri araçlarla <b>toplu üretim</b> yapılan faaliyet dalıdır. Ham maddeleri kullanıma hazır hâle getirir. (s. 12)",
              "<b>Endüstriyel tasarım:</b> <b>Seri üretime</b> uygun ürün tasarlama işidir. <b>Üç boyutlu</b> nesnelerle ilgilenir: makineler, araç-gereçler, mutfak malzemeleri. (s. 13)",
              "<b>Çevre tasarımı:</b> <b>Bina, peyzaj ve iç mekân</b> tasarımıdır. Programda “mimari-çevre tasarımı” diye geçer. (s. 14)",
              "<b>Grafik tasarım:</b> <b>Okunan ve izlenen</b> görüntülerin tasarımıdır: afiş, broşür, kitap, dergi, ambalaj. (s. 14)"],
    kelimeler=["zihinde canlandırma", "planlama", "makineyle toplu üretim", "seri üretim", "üç boyutlu ürün", "bina, peyzaj, iç mekân", "okunan ve izlenen görüntü"],
    hatalar=[{"yanlis": "Afiş ve broşür endüstriyel tasarımdır.", "dogru": "Afiş, broşür, kitap: grafik tasarım (okunan ve izlenen görüntüler)."},
             {"yanlis": "Bina ve iç mekân grafik tasarımdır.", "dogru": "Bina, peyzaj ve iç mekân: çevre tasarımı."},
             {"yanlis": "Endüstri: elle tek tek eşya yapmak.", "dogru": "Endüstri: makine ve araçlarla toplu üretim."}])

Y.kazanim(kod="Ü2·A", ad="Sanat/tasarım elemanlarını açıklar.", kisa="Tasarım Elemanları", soru=3,
    soruNot="Kâğıtta 4 soru: 5, 11, 12, 13", renk="#d9480f", konular=["u2k1", "u2k2"], sayfa="s. 24 + program", svg=Z.elemanlar(),
    maddeler=["Elemanlar: <b>nokta, çizgi, renk, doku, biçim-form</b>, şekil, valör (değer), yön, aralık, ışık-gölge, oran, yazı, mekân. (s. 24, program)",
              "<b>Nokta:</b> Görsel anlatımın en küçük, temel elemanıdır; yer belirten işarettir. <b>Çizgi:</b> Hareket eden bir noktanın izidir (noktanın bir doğrultuda uzaması). (s. 24)",
              "<b>Renk:</b> Işığın cisimlere çarpıp <b>yansıyarak</b> gözümüzde bıraktığı etkidir. <b>Sıcak renkler uyarıcı</b>, <b>soğuk renkler gevşetici ve dinlendiricidir</b>. Renkle dikkat çekilir (vurgu). (s. 24, 27)",
              "<b>Valör (değer):</b> Bir rengin <b>açıklık ve koyuluk</b> derecesidir. <b>Form:</b> Şeklin <b>üç boyut</b> ve hacim kazanmış hâlidir. (program)",
              "<b>Doku:</b> Nesnenin <b>dış yüzeyinin yapısıdır</b> (pürüzlü, kaygan, yumuşak). Gözle görülür, elle hissedilir. (s. 24)",
              "Dokunun etkileri: tasarımı <b>zenginleştirir</b>, <b>dikkati çeker</b>, nesneyi <b>gerçek gibi hissettirir</b>, düz resme <b>derinlik</b> verir. (kitap dışı: açık ders)"],
    kelimeler=["ışığın yansıması", "sıcak = uyarıcı", "soğuk = dinlendirici", "açıklık-koyuluk = valör", "üç boyut = form", "dış yüzeyin yapısı", "zenginleştirir, dikkat çeker"],
    hatalar=[{"yanlis": "Vurgu, denge, ritim tasarım elemanıdır.", "dogru": "Bunlar tasarım İLKESİ. Eleman: nokta, çizgi, renk, doku, form…"},
             {"yanlis": "Soğuk renkler uyarır, sıcak renkler dinlendirir.", "dogru": "Sıcak renkler (kırmızı, turuncu) uyarır; soğuk renkler (mavi, yeşil) dinlendirir."},
             {"yanlis": "Rengin açıklık-koyuluğu: renk. Üç boyutlu hâl: şekil.", "dogru": "Açıklık-koyuluk: valör (değer). Üç boyut ve hacim: form."}])

Y.kazanim(kod="Ü2·B", ad="Tasarım ilkelerini bir ürün üzerinde göstererek açıklar.", kisa="Tasarım İlkeleri: Vurgu ve Zıtlık", soru=1,
    soruNot="Kâğıtta 2 soru: 14, 15", renk="#2b8a3e", konular=["u2k3"], sayfa="s. 27 + program", svg=Z.ilkeler(),
    maddeler=["<b>Vurgu:</b> Tasarımda <b>göz alıcı olan odak noktası</b>dır. (s. 27)",
              "Vurgu <b>renk, şekil, form, boyut, yerleşim</b> ya da çizgiyle sağlanır; vurgulanan kısım daha etkili görünür. (s. 27)",
              "Vurgu örneği: düz bir kıyafetin üstüne takılan <b>kolye</b>, bir metindeki <b>koyu yazılmış</b> bölüm dikkati oraya çeker. (s. 27)",
              "<b>Zıtlık (kontrast):</b> Zıt özelliklerin yan yana getirilmesiyle oluşan <b>güçlü görsel etki</b>dir: açık-koyu, büyük-küçük, sıcak-soğuk. (program)",
              "Karıştırma: <b>denge</b> parçaların eşit dağılması, <b>ritim</b> uyumlu tekrardır. (s. 27)"],
    kelimeler=["göz alıcı", "odak noktası", "dikkati çeker", "kolye, koyu yazı", "zıtlık = kontrast", "açık-koyu yan yana"],
    hatalar=[{"yanlis": "Vurgu: parçaların eşit dağılması.", "dogru": "Bu denge. Vurgu: göz alıcı odak noktası."},
             {"yanlis": "Zıt özellikleri yan yana getirmek: ritim.", "dogru": "Bu zıtlık (kontrast). Ritim: uyumlu tekrar."},
             {"yanlis": "Vurguyu açıklarken örnek vermemek.", "dogru": "Tanım + nasıl sağlanır + örnek (kolye, koyu yazı)."}])

# =====================================================================
# CEVAP KALIPLARI
# =====================================================================
Y.formul(id="tanim", ad="Tanım", kalip="X, … dır. (Örneğin …)", ne="“… nedir? Açıklayınız.” sorularında",
         ornek="Teknoloji, araç-gereç yapabilmek için gereken bilgi ve yetenektir.")
Y.formul(id="alan", ad="Adını bul + Çünkü", kalip="Bu …'dır, çünkü …", ne="“Tanımı verilen alan / ilke / eleman hangisidir?” sorularında",
         ornek="Bu grafik tasarımdır, çünkü okunan ve izlenen görüntülerin tasarımıdır.")
Y.formul(id="karsilastir", ad="Karşılaştır", kalip="X … dır, Y ise … dır.", ne="“Arasındaki fark nedir?” sorularında",
         ornek="Sıcak renkler uyarıcıdır, soğuk renkler ise dinlendiricidir.")
Y.formul(id="ornek", ad="Örnek ver", kalip="1. …  2. …", ne="“İki örnek yazınız”, “5 tane yazınız” sorularında: istenen sayıda, numaralı yaz",
         ornek="İki icat örneği: 1. Kibrit  2. Daktilo")
Y.formul(id="etki", ad="Tanım + Etki", kalip="X, … dır. Tasarıma etkisi: … ve …", ne="“Kavramı açıklayınız. Etkileri nelerdir?” sorularında: iki parçayı da yaz",
         ornek="Işık-gölge: her ışık kaynağı bir gölge yaratır. Tasarıma etkisi: resmi canlı ve hareketli yapar. (s. 24)")

# =====================================================================
# ÖĞRETMENİN SORULARI (çalışma kâğıdı, 15 soru; numaralar kâğıttaki gibi)
# =====================================================================
Q = {}
def S(no, kazanim, maddeler, metin=None, svg=None):
    q = {"id": f"m{no}", "no": no, "kazanim": kazanim, "maddeler": maddeler}
    if metin: q["metin"] = metin
    if svg: q["svg"] = svg
    Q[no] = Y.meb(**q)

S(1, "Ü1·A", [M("a", "Teknoloji nedir? Açıklayınız.",
    "Teknoloji, araç-gereç yapabilmek için gereken bilgi ve yetenektir. Bir işi daha iyi, daha hızlı, daha kolay, daha ekonomik ve daha verimli yapma girişimidir. Amacı insan hayatının kalitesini artırmaktır.",
    [A("Araç-gereç yapmak için gereken bilgi ve yetenek", "araç", "gereç", "yetenek"),
     A("Bir işi daha iyi, hızlı, kolay, verimli yapma", "daha iyi", "hızlı", "kolay", "verimli", "ekonomik"),
     A("Amacı: hayat kalitesini artırmak", "kalite", "hayatı", "hayatımızı", "yaşam")], "tanim",
    {"tur": "secim", "soru": "Önce ısınalım: Hangisi teknolojinin tanımıdır?",
     "secenekler": ["Araç-gereç yapabilmek için gereken bilgi ve yetenek", "Var olan ama bilinmeyen bir şeyin bulunması", "Makinelerle toplu üretim yapılan faaliyet dalı", "Okunan ve izlenen görüntülerin tasarımı"],
     "dogru": 0, "aciklama": "Teknoloji: araç-gereç yapmak için bilgi ve yetenek. Diğerleri keşif, endüstri ve grafik tasarım. (s. 11)"})])

S(2, "Ü1·B", [M("a", "Yukarıda tanımı verilen tasarım alanı hangi tasarım alanıdır?",
    "Grafik tasarımdır. Grafik tasarım, okunan ve izlenen görüntülerin tasarımıdır.",
    [A("Grafik tasarım", "grafik")], "alan")],
  metin=["Broşür, afiş, kitap, dergi vb. okunan ve izlenen görüntülerin tasarımını yapmaktır."])

S(3, "Ü1·B", [M("a", "Tasarım nedir? Açıklayınız.",
    "Tasarım, bir fikrin zihinde canlandırılıp planlanmasıdır. En önemli özelliği planlamadır. Bir fikrin kâğıt üzerine çizilmiş şekli de tasarımdır.",
    [A("Zihinde canlandırma", "zihin", "canlandır", "hayal"), A("Planlama", "plan"), A("Fikrin kâğıda çizilmesi", "kâğıt", "kağıt", "çiz")], "tanim",
    {"tur": "secim", "soru": "Önce ısınalım: Kitaba göre tasarımın en önemli özelliği hangisidir?",
     "secenekler": ["Planlama", "Seri üretim", "Süsleme", "Satış"], "dogru": 0,
     "aciklama": "Planlamanın olduğu her yerde tasarımdan söz edilebilir. (s. 13)"})])

S(4, "Ü1·A", [M("a", "İcat yapan kişilere ne isim verilir?",
    "İcat yapan kişilere mucit denir.", [A("Mucit", "mucit")], "alan")])

S(5, "Ü2·A", [M("a", "5 adet tasarım elemanı yazınız.",
    "1. Nokta 2. Çizgi 3. Renk 4. Doku 5. Biçim (form)",
    [SIRA(f"{i}. eleman doğru", *[ELEMAN] * i) for i in range(1, 6)], "ornek",
    {"tur": "dytablo", "soru": "Önce ısınalım: Hangileri tasarım ELEMANIdır? Doğru (D) ya da Yanlış (Y) seç.", "ifadeler": [
        {"s": "Nokta", "d": True}, {"s": "Doku", "d": True}, {"s": "Renk", "d": True}, {"s": "Vurgu", "d": False}, {"s": "Denge", "d": False}],
     "aciklama": "Vurgu ve denge tasarım İLKESİdir. Nokta, doku, renk elemandır. (s. 24, 27)"})])

S(6, "Ü1·B", [M("a", "Endüstri nedir? Açıklayınız.",
    "Endüstri (sanayi), makine ve benzeri araçlar kullanılarak toplu üretim yapılan faaliyet dalıdır. Ham maddeleri ve yarı işlenmiş maddeleri kullanıma hazır hâle getirir.",
    [A("Makine ve araçlarla", "makine"), A("Toplu üretim", "toplu", "seri"), A("Ham maddeyi kullanıma hazır hâle getirir", "ham madde", "hammadde", "kullanıma hazır", "yarı işlen")], "tanim",
    {"tur": "secim", "soru": "Önce ısınalım: Endüstrinin bir diğer adı nedir?", "secenekler": ["Sanayi", "Teknik", "İnovasyon", "Tasarım"], "dogru": 0,
     "aciklama": "Kitapta “Sanayi ya da endüstri” diye geçer. (s. 12)"})])

S(7, "Ü1·B", [M("a", "Endüstriyel tasarım nedir? Açıklayınız.",
    "Endüstriyel tasarım, seri üretime uygun ürün tasarlama işidir. Üç boyutlu nesnelerin tasarlanması ve geliştirilmesiyle ilgilidir. Örneğin makineler, araç-gereçler ve mutfak malzemeleri.",
    [A("Seri üretime uygun ürün tasarlama", "seri üretim", "seri"), A("Üç boyutlu nesneler", "üç boyut", "3 boyut", "3b"),
     A("Örnek: makine, araç-gereç, mutfak malzemesi", "makine", "araç", "mutfak", "tencere", "sandalye", "araba", "otomobil", "telefon")], "tanim",
    {"tur": "secim", "soru": "Önce ısınalım: Hangisi endüstriyel tasarımın konusudur?", "secenekler": ["Mutfak malzemesi", "Afiş", "Park ve bahçe", "Kitap kapağı"], "dogru": 0,
     "aciklama": "Makineler, araç-gereçler, mutfak malzemeleri endüstri tasarımına girer. (s. 13)"})])

S(8, "Ü1·A", [M("a", "Keşif ve icat arasındaki fark nedir? Açıklayınız.",
    "Keşif, daha önce var olan ama bilinmeyen bir şeyin bulunmasıdır; örneğin yer çekiminin fark edilmesi. İcat ise var olan teknolojilerin bir araya getirilerek yeni ve benzersiz bir şeyin yapılmasıdır; örneğin kibrit. Yani keşifte var olan bulunur, icatta yeni bir şey yapılır.",
    [A("Keşif: var olan ama bilinmeyen bir şeyi bulmak", "var olan", "bilinmeyen", "fark ed"), A("İcat: var olanları birleştirip yeni bir şey yapmak", "yeni", "bir araya", "birleştir", "benzersiz"),
     A("Her birine örnek (yer çekimi, kıta / kibrit, araba…)", *KESIF, "kibrit", "araba", "daktilo")], "karsilastir",
    {"tur": "secim", "soru": "Önce ısınalım: Hangisi doğrudur?",
     "secenekler": ["Keşifte var olan bulunur, icatta yeni bir şey yapılır.", "Keşifte yeni bir şey yapılır, icatta var olan bulunur.", "Keşif ve icat aynı anlama gelir.", "Keşif yalnızca makinelerle yapılır."],
     "dogru": 0, "aciklama": "Keşif: var olan ama bilinmeyenin bulunması. İcat: var olanların yeni biçimde bir araya getirilmesi. (s. 11)"})])

S(9, "Ü1·A", [M("a", "İki adet keşif örneği yazınız.",
    "1. Yer çekiminin fark edilmesi 2. Bilinmeyen bir kıtanın bulunması",
    [SIRA("1. keşif örneği doğru", KESIF), SIRA("2. keşif örneği doğru", KESIF, KESIF)], "ornek",
    {"tur": "dytablo", "soru": "Önce ısınalım: Hangileri KEŞİF örneğidir? D ya da Y seç.", "ifadeler": [
        {"s": "Yer çekiminin fark edilmesi", "d": True}, {"s": "Bilinmeyen bir kıtanın bulunması", "d": True}, {"s": "Kibrit", "d": False}, {"s": "Araba", "d": False}],
     "aciklama": "Kibrit ve araba icattır; yer çekimi ve yeni bir kıta var olan ama bilinmeyen şeylerdir. (s. 11)"})])

S(10, "Ü1·B", [M("a", "Yukarıda tanımı verilen tasarım alanı hangi tasarım alanıdır?",
    "Çevre tasarımıdır (mimari-çevre tasarımı). Çevre tasarımı bina, peyzaj ve iç mekân tasarımını kapsar.",
    [A("Çevre tasarımı (mimari-çevre)", "çevre", "mimari")], "alan")],
  metin=["Bina, peyzaj ve iç mekân tasarımını kapsayan oldukça geniş bir çalışma alanıdır."])

S(11, "Ü2·A", [
    M("a", "Tasarım elemanlarından biri olan doku kavramını açıklayınız.",
      "Doku, nesnelerin dış yüzeyinin yapısıdır; pürüzlü, kaygan, yumuşak, sert gibi. Doku gözle görülür, elle dokunarak hissedilir.",
      [A("Nesnenin dış yüzeyinin (dış yapısının) özelliği", "dış yapı", "yüzey", "dış görünüş"), A("Örnek: pürüzlü, kaygan, yumuşak, sert…", "pürüzlü", "kaygan", "yumuşak", "sert", "pürüzsüz", "ağaç kabuğu", "kumaş", "dokun", "hissed")], "tanim"),
    M("b", "Dokunun tasarıma kattığı etkiler nelerdir?",
      "Doku tasarımı zenginleştirir ve çeşitlendirir. Dikkati nesneye çeker. Nesneyi gerçek gibi hissettirir ve düz bir resme derinlik (üç boyut) etkisi verir.",
      [A("Tasarımı zenginleştirir, çeşitlendirir", "zengin", "çeşit"), A("Dikkat çeker, ilgi uyandırır", "dikkat", "ilgi"), A("Gerçek gibi hissettirir, derinlik verir", "gerçek", "derinlik", "üç boyut", "hissettir")], "etki")])

S(12, "Ü2·A", [
    M("a", "Tasarım elemanlarından biri olan renk kavramını açıklayınız.",
      "Renk, ışığın cisimlere çarptıktan sonra yansıyarak gözümüzde bıraktığı etkidir.",
      [A("Işık", "ışı"), A("Cisimlerden yansıma", "yansı"), A("Gözde bıraktığı etki", "göz", "görme")], "tanim",
      {"tur": "secim", "soru": "Önce ısınalım: Renk nasıl oluşur?",
       "secenekler": ["Işığın cisimlerden yansıyıp gözümüzde bıraktığı etkiyle", "Noktanın bir doğrultuda uzamasıyla", "Nesnenin dış yüzeyinin yapısıyla", "Şeklin üç boyut kazanmasıyla"],
       "dogru": 0, "aciklama": "Renk: ışığın cisimlere çarpıp yansıyarak görme duyumuzda bıraktığı etki. (s. 24)"}),
    M("b", "Rengin tasarım üzerindeki etkileri nelerdir?",
      "Renk insanları etkiler. Sıcak renkler (kırmızı, turuncu) uyarıcıdır, soğuk renkler (mavi, yeşil) gevşetici ve dinlendiricidir. Renkle tasarımda dikkat çekilir, vurgu yapılır.",
      [A("Sıcak renkler uyarıcı", "sıcak", "uyar"), A("Soğuk renkler gevşetici, dinlendirici", "soğuk", "dinlendir", "gevşe", "sakin"), A("Dikkat çeker, vurgu yapar", "dikkat", "vurgu", "odak")], "etki")])

TANIM13 = ["Hareket eden bir noktanın izidir.", "Işığın nesnelerden yansıyarak gözümüzde oluşturduğu etkidir.", "Bir rengin açıklık ve koyuluk derecesidir.",
           "Görsel anlatımın en küçük ve en temel elemanıdır.", "Şeklin üç boyut ve hacim kazanmış hâlidir."]
S(13, "Ü2·A", [
    M("a", f"“{TANIM13[0]}” Bu tanım hangi tasarım elemanına aittir?", "Çizgi", [A("Çizgi", "çizgi")], None,
      {"tur": "eslestir", "soru": "Önce ısınalım: Tanımları tasarım elemanlarıyla eşleştir.", "ciftler": [
          {"sol": TANIM13[0], "sag": "Çizgi"}, {"sol": TANIM13[1], "sag": "Renk"}, {"sol": TANIM13[2], "sag": "Valör (değer)"},
          {"sol": TANIM13[3], "sag": "Nokta"}, {"sol": TANIM13[4], "sag": "Form"}],
       "aciklama": "Çizgi: noktanın uzaması. Renk: ışığın yansıması. Valör: açıklık-koyuluk. Nokta: en temel eleman. Form: üç boyut. (s. 24, program)"}),
    M("b", f"“{TANIM13[1]}” Bu tanım hangi tasarım elemanına aittir?", "Renk", [A("Renk", "renk")]),
    M("c", f"“{TANIM13[2]}” Bu tanım hangi tasarım elemanına aittir?", "Valör (değer)", [A("Valör (değer)", "valör", "valor", "değer")]),
    M("d", f"“{TANIM13[3]}” Bu tanım hangi tasarım elemanına aittir?", "Nokta", [A("Nokta", "nokta")]),
    M("e", f"“{TANIM13[4]}” Bu tanım hangi tasarım elemanına aittir?", "Form (biçim-form)", [A("Form (biçim-form)", "form", "biçim")])],
  metin=["Aşağıda verilen tanımların hangi tasarım elemanına ait olduğunu yazınız."])

S(14, "Ü2·B", [M("a", "Vurgu tasarım ilkesini açıklayınız.",
    "Vurgu, tasarımda göz alıcı olan odak noktasıdır. Renk, şekil, form, boyut ya da yerleşimle sağlanır. Örneğin düz bir kıyafetin üstüne takılan kolye ya da metindeki koyu yazılmış bölüm dikkati oraya çeker.",
    [A("Göz alıcı odak noktası, dikkati çeker", "odak", "göz alıcı", "dikkat"), A("Renk, şekil, boyut gibi elemanlarla sağlanır", "renk", "şekil", "boyut", "form", "yerleşim", "çizgi"),
     A("Örnek: kolye, koyu yazılmış bölüm", "kolye", "koyu", "kalın")], "tanim",
    {"tur": "secim", "soru": "Önce ısınalım: Vurgu nedir?",
     "secenekler": ["Tasarımda göz alıcı olan odak noktası", "Parçaların bütün içinde eşit dağılması", "Elemanların uyumlu tekrarı", "Zıt özelliklerin yan yana getirilmesi"],
     "dogru": 0, "aciklama": "Vurgu odak noktasıdır. Diğerleri denge, ritim ve zıtlık. (s. 27)"})])

S(15, "Ü2·B", [M("a", "Yukarıda tanımı verilen tasarım ilkesi hangisidir?",
    "Zıtlıktır (kontrast). Açık-koyu, büyük-küçük gibi zıt özellikler yan yana gelince güçlü bir görsel etki oluşur.",
    [A("Zıtlık (kontrast)", "zıt", "kontrast")], "alan")],
  metin=["Zıt özelliklerin yan yana getirilmesiyle oluşan güçlü görsel etkidir."])

# =====================================================================
# FİKRİ'NİN HATASI (aynı 15 soruya yanlış ya da eksik cevaplar; veri alanı kuarkHata)
# =====================================================================
def KH(kazanim, soru, kuark, dogruSik, yanlis1, yanlis2, ipucu, aciklama, dogruCevap):
    Y.kuark(kazanim=kazanim, soru=soru, kuark=kuark, secenekler=[dogruSik, yanlis1, yanlis2], dogru=0, ipucu=ipucu, aciklama=aciklama, dogruCevap=dogruCevap)

KH("Ü1·A", "Teknoloji nedir? Açıklayınız.", "Teknoloji, telefon ve bilgisayardır.",
   "Telefon ve bilgisayar teknoloji ürünüdür; teknoloji, araç-gereç yapmak için gereken bilgi ve yetenektir.", "Teknoloji, bilinmeyen bir kıtanın bulunmasıdır.", "Fikri haklı, cevapta hata yok.",
   "Ürün mü sordu, kavram mı?", "Teknoloji: araç-gereç yapabilmek için gerekli bilgi ve yetenek. (s. 11)",
   "Teknoloji, araç-gereç yapabilmek için gereken bilgi ve yetenektir. Bir işi daha iyi, hızlı ve kolay yapma girişimidir.")
KH("Ü1·A", "İcat yapan kişilere ne isim verilir?", "Tasarımcı.",
   "İcat yapan kişiye mucit denir.", "İcat yapan kişiye teknisyen denir.", "Fikri haklı, icat yapan herkes tasarımcıdır.",
   "İcat → mu…", "Mucit: yeni bir buluş ortaya koyan, icat eden kimse (TDK).", "İcat yapan kişilere mucit denir.")
KH("Ü1·A", "Keşif ve icat arasındaki fark nedir? Açıklayınız.", "Keşif ve icat aynı şeydir; ikisi de yeni bir şey yapmaktır.",
   "Keşifte var olan ama bilinmeyen bir şey bulunur; icatta var olanlar birleştirilip yeni bir şey yapılır.", "Ters söylemeliydi: keşif yeni şey yapmak, icat var olanı bulmaktır.", "Fikri haklı, hata yok.",
   "Yer çekimi Newton'dan önce de var mıydı?", "Keşif: var olanın bulunması. İcat: yeni ve benzersiz bir araya getirme. (s. 11)",
   "Keşif, var olan ama bilinmeyen bir şeyin bulunmasıdır. İcat ise var olanların bir araya getirilip yeni bir şey yapılmasıdır.")
KH("Ü1·A", "Keşif ve icat arasındaki fark nedir? Açıklayınız.", "Farklıdır.",
   "Cevap eksik: keşfin ve icatın ne olduğu ayrı ayrı yazılmalı.", "Cevap yanlış; keşif ve icat aynıdır.", "Hata yok, tek kelime yeterli.",
   "“Açıklayınız” diyen soruda puanı ne getirir?", "Karşılaştırma sorusunda ikisini de anlat: “Keşif …, icat ise …”.",
   "Keşif, var olan ama bilinmeyen bir şeyin bulunmasıdır. İcat ise var olanların bir araya getirilip yeni bir şey yapılmasıdır.")
KH("Ü1·A", "İki adet keşif örneği yazınız.", "1. Kibrit 2. Araba",
   "Kibrit ve araba icattır; keşif örneği yer çekiminin fark edilmesi ya da yeni bir kıtanın bulunması olabilir.", "Kibrit keşif, araba icattır.", "Fikri haklı, ikisi de keşiftir.",
   "Kibrit doğada hazır var mıydı?", "Kibrit, araba, daktilo icat örnekleridir. (s. 11)",
   "1. Yer çekiminin fark edilmesi 2. Bilinmeyen bir kıtanın bulunması")
KH("Ü1·B", "Broşür, afiş, kitap, dergi vb. okunan ve izlenen görüntülerin tasarımı hangi tasarım alanıdır?", "Endüstriyel tasarım.",
   "Okunan ve izlenen görüntüler grafik tasarımın alanıdır.", "Bu çevre tasarımıdır.", "Fikri haklı, hata yok.",
   "Afiş ve kitap seri üretilen üç boyutlu eşya mı, okunan görüntü mü?", "Grafik tasarım: okunan ve izlenen görüntülerin tasarımı. (s. 14)", "Grafik tasarımdır.")
KH("Ü1·B", "Bina, peyzaj ve iç mekân tasarımını kapsayan alan hangi tasarım alanıdır?", "Grafik tasarım.",
   "Bina, peyzaj ve iç mekân çevre tasarımının alanıdır.", "Bu endüstriyel tasarımdır.", "Fikri haklı, hata yok.",
   "Bina ve bahçe nerede durur: kâğıtta mı, çevremizde mi?", "Çevre tasarımı: bina, peyzaj ve iç mekân. (s. 14)", "Çevre tasarımıdır (mimari-çevre tasarımı).")
KH("Ü1·B", "Endüstriyel tasarım nedir? Açıklayınız.", "Endüstriyel tasarım, bina ve bahçe tasarlamaktır.",
   "Bina ve bahçe çevre tasarımıdır; endüstriyel tasarım seri üretime uygun, üç boyutlu ürün tasarlamaktır.", "Endüstriyel tasarım, afiş ve broşür tasarlamaktır.", "Fikri haklı, hata yok.",
   "Endüstri = toplu üretim. Ne üretilir?", "Endüstriyel tasarım: seri üretime uygun ürün tasarlama işi. (s. 13)",
   "Endüstriyel tasarım, seri üretime uygun ürün tasarlama işidir. Üç boyutlu nesnelerle ilgilenir.")
KH("Ü1·B", "Endüstri nedir? Açıklayınız.", "Endüstri, eşyaları elle tek tek yapmaktır.",
   "Endüstri, makine ve araçlarla toplu üretim yapılan faaliyet dalıdır.", "Endüstri, yeni bir kıtanın bulunmasıdır.", "Fikri haklı, hata yok.",
   "Fabrikada eşyalar elle mi, makineyle mi yapılır?", "Endüstri: makine ve benzeri araçlarla toplu üretim. (s. 12)",
   "Endüstri, makine ve benzeri araçlarla toplu üretim yapılan faaliyet dalıdır.")
KH("Ü1·B", "Tasarım nedir? Açıklayınız.", "Tasarım, bir ürünü satmaktır.",
   "Tasarım, bir fikri zihinde canlandırıp planlamaktır; en önemli özelliği planlamadır.", "Tasarım, ürünü makineyle çok sayıda üretmektir.", "Fikri haklı, hata yok.",
   "Tasarımın en önemli özelliği neydi?", "Tasarımın en önemli özelliği planlamadır. (s. 13)",
   "Tasarım, bir fikrin zihinde canlandırılıp planlanmasıdır. En önemli özelliği planlamadır.")
KH("Ü2·A", "5 adet tasarım elemanı yazınız.", "Nokta, çizgi, renk, vurgu, denge.",
   "Vurgu ve denge tasarım ilkesidir; yerine doku, biçim-form gibi elemanlar yazılmalı.", "Nokta ve çizgi eleman değildir.", "Fikri haklı, hepsi eleman.",
   "Eleman mı, ilke mi? Vurgu hangi listedeydi?", "Elemanlar s. 24'te, ilkeler s. 27'de.",
   "Nokta, çizgi, renk, doku, biçim (form).")
KH("Ü2·A", "Rengin tasarım üzerindeki etkileri nelerdir?", "Soğuk renkler insanı uyarır, sıcak renkler dinlendirir.",
   "Ters söylemiş: sıcak renkler uyarıcı, soğuk renkler gevşetici ve dinlendiricidir.", "Renklerin insan üzerinde hiçbir etkisi yoktur.", "Fikri haklı, hata yok.",
   "Kırmızı mı daha heyecanlı, mavi mi?", "Sıcak renkler uyarıcı, soğuk renkler gevşetici ve dinlendirici etki uyandırır. (s. 24)",
   "Sıcak renkler uyarıcı, soğuk renkler gevşetici ve dinlendiricidir. Renkle dikkat çekilir.")
KH("Ü2·A", "Doku kavramını açıklayınız.", "Doku, bir nesnenin rengidir.",
   "Doku, nesnenin dış yüzeyinin yapısıdır (pürüzlü, kaygan gibi); renk ayrı bir elemandır.", "Doku, noktanın bir doğrultuda uzamasıdır.", "Fikri haklı, hata yok.",
   "Gözünü kapatıp ağaç kabuğuna dokunsan ne hissedersin?", "Doku: nesnelerin dış yapı özellikleri. (s. 24)",
   "Doku, nesnelerin dış yüzeyinin yapısıdır: pürüzlü, kaygan, yumuşak gibi.")
KH("Ü2·A", "“Bir rengin açıklık ve koyuluk derecesidir.” Hangi tasarım elemanıdır?", "Renk.",
   "Bu valördür (değer); renk, ışığın yansımasıyla gözümüzde oluşan etkidir.", "Bu dokudur.", "Fikri haklı, hata yok.",
   "Aynı rengin açığı ve koyusu… bunun özel bir adı vardı.", "Valör (değer): bir rengin açıklık-koyuluk derecesi (program).", "Valör (değer)")
KH("Ü2·A", "“Şeklin üç boyut ve hacim kazanmış hâlidir.” Hangi tasarım elemanıdır?", "Şekil.",
   "Bu formdur; şekil düz, iki boyutludur.", "Bu noktadır.", "Fikri haklı, hata yok.",
   "Kare düzdür; küp üç boyutludur. Küpe ne denir?", "Form: eni, boyu ve derinliği olan üç boyutlu biçim (program).", "Form (biçim-form)")
KH("Ü2·B", "Vurgu tasarım ilkesini açıklayınız.", "Vurgu, tasarımdaki parçaların eşit dağılmasıdır.",
   "Bu dengenin tanımı; vurgu, tasarımda göz alıcı olan odak noktasıdır.", "Vurgu, elemanların uyumlu tekrarıdır.", "Fikri haklı, hata yok.",
   "Düz kıyafetteki kolyeyi düşün: gözün nereye gider?", "Vurgu: göz alıcı odak noktası. (s. 27)",
   "Vurgu, tasarımda göz alıcı olan odak noktasıdır. Renk, şekil, boyutla sağlanır; örneğin düz kıyafetteki kolye.")
KH("Ü2·B", "“Zıt özelliklerin yan yana getirilmesiyle oluşan güçlü görsel etkidir.” Hangi tasarım ilkesidir?", "Ritim.",
   "Bu zıtlıktır (kontrast); ritim uyumlu tekrardır.", "Bu dengedir.", "Fikri haklı, hata yok.",
   "Tanımda hangi kelime ilkenin adını veriyor?", "Zıtlık (kontrast): karşıt elemanlar yan yana (program). Ritim: uyumlu tekrar (s. 27).", "Zıtlık (kontrast)")

# =====================================================================
# PROVA YAZILILARI: 15 sorudan 10'ar (dağılım 3+3+3+1), her soru 10 puan
# =====================================================================
def prova_sorusu(no):
    q = copy.deepcopy(Q[no]); q.pop("id"); q.pop("no")
    n = len(q["maddeler"]); pay = 10 // n
    for m in q["maddeler"]:
        m.pop("iskele", None); m["puan"] = pay
    q["puan"] = 10
    return q

for pid, ad, nolar in [("p1", "Prova 1", [1, 2, 5, 6, 7, 8, 9, 12, 13, 14]), ("p2", "Prova 2", [1, 3, 4, 7, 8, 10, 11, 12, 13, 15]),
                       ("p3", "Prova 3", [2, 3, 4, 5, 6, 8, 9, 11, 13, 14]), ("p4", "Prova 4", [1, 4, 5, 6, 7, 9, 10, 11, 12, 15])]:
    Y.prova(id=pid, ad=ad, sorular=[prova_sorusu(n) for n in nolar])

# Her soru 4 provada en az 2 kez geçsin
say = {n: sum(n in p for p in [[1, 2, 5, 6, 7, 8, 9, 12, 13, 14], [1, 3, 4, 7, 8, 10, 11, 12, 13, 15], [2, 3, 4, 5, 6, 8, 9, 11, 13, 14], [1, 4, 5, 6, 7, 9, 10, 11, 12, 15]]) for n in Q}
assert min(say.values()) >= 2, say
print("Provalarda soru tekrarları:", say)
Y.yaz()
