"""Fen Bilimleri 7 · 1. Dönem 1. Yazılı — Yazılıya Hazırlık verisi.
Kapsam: MEB senaryo tablosu, Senaryo 4 (okulun seçtiği): FB.7.1.3 (1), FB.7.1.4 (1), FB.7.1.5 (1), FB.7.2.1 (2), FB.7.2.2 (1) = 6 soru.
FB.7.1.1 ve FB.7.1.2 bu sınavda YOK: uzay araçları karşılaştırması, teleskoplar, Türkiye'nin uyduları, takımyıldızlar sorulmaz.
Kaynaklar: MEB "Yazılıya Hazırlanıyorum" örnek soruları (yalnız senaryoya giren 3–9. sorular), kitap (sayfa atıflı),
okul yazılısı örneklerinden senaryoya uyan soru kalıpları (yeniden yazıldı). Çalıştır: python3 araclar/yazili/fen1_d1y1.py"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from yazili import Yazili
import cizim as Z


def A(ad, *k): return {"ad": ad, "k": list(k)}
def SIRA(ad, *g): return {"ad": ad, "sira": [list(x) if isinstance(x, (list, tuple)) else [x] for x in g]}
def M(harf, soru, cevap=None, an=None, formul=None, iskele=None, puan=None):
    m = {"harf": harf, "soru": soru}
    if formul: m["formul"] = formul
    if iskele: m["iskele"] = iskele
    if cevap: m["cevap"] = cevap; m["anahtarlar"] = an or []
    if puan is not None: m["puan"] = puan
    return m

# Sık kullanılan anahtarlar
EVET_IS = A("Evet, iş yapılmıştır", "evet", "yapılmış", "yapmış", "yapar", "yapılır")
HAYIR_IS = A("Hayır, iş yapılmamıştır", "hayır", "yapılmamış", "yapmamış", "yapmaz", "yapılmaz", "sıfır")
KIRLILIK = A("Problemin adı: uzay kirliliği (uzay çöpü)", "kirlili", "çöp")
NEDEN_COP = A("Nedeni: görevi biten uydu ve roket parçaları yörüngede kalıyor", "görevi", "görevini", "işlevini", "eski uydu", "parça", "kalıntı", "tamamla", "bitmiş", "biten", "bitince")
ZARAR = A("Sonucu: çarpışma, uzay araçlarına zarar", "çarp", "zarar", "hasar")
TEKNOLOJI = A("Günlük hayattan bir teknoloji: TV, GPS, telefon, internet, hava durumu…", "televizyon", "tv", "gps", "navigasyon", "telefon", "internet", "hava durumu", "haberleşme", "iletişim", "yayın")
KUTLE_K = A("Küçük kütleli yıldız", "küçük kütle", "kütlesi küçük", "küçük")
KUTLE_B = A("Büyük kütleli yıldız", "büyük kütle", "kütlesi büyük", "büyük")
BEYAZ = A("Beyaz cüce", "beyaz cüce")
BASLANGIC_KUTLE = A("Belirleyen özellik: başlangıç kütlesi", "kütle")
AYNI_DOGRULTU = A("Kuvvet ile hareket aynı doğrultuda", "aynı doğrultu", "aynı yön", "doğrultusunda", "paralel")
DIK = A("Kuvvet yukarı, hareket yatay (dik / farklı doğrultu)", "dik", "farklı doğrultu", "farklı yön", "yatay")
YER_DEG_YOK = A("Cisim yer değiştirmiyor (hareket yok)", "hareket etm", "yer değiştirm", "sabit", "yol alm", "kıpırda", "duruyor", "durduğu", "hareketsiz")
POTANSIYEL = A("Çekim potansiyel enerjisi", "potansiyel")
KINETIK = A("Kinetik enerji", "kinetik", "hareket enerjisi")
KUTLE = A("Kütle (ağırlık)", "kütle", "ağırlı")
YUKSEKLIK = A("Yükseklik", "yüksek")
HIZ = A("Hız (sürat)", "hız", "sürat")

Y = Yazili("fen1", "d1y1",
    baslik="1. Dönem 1. Yazılı", ders="Fen Bilimleri", senaryo="Senaryo 4", sure=40, tarih=None,
    dagilim={"FB.7.1.3": 1, "FB.7.1.4": 1, "FB.7.1.5": 1, "FB.7.2.1": 2, "FB.7.2.2": 1},
    giris="Okulun seçtiği senaryoda <b>6 açık uçlu soru</b> var. Hepsi 5 kazanımdan geliyor. Önce hatırla, sonra MEB'in sorularını çöz, en sonda gerçek yazılı gibi prova yap. Uzay araçları, teleskoplar ve takımyıldızlar bu yazılıda yok; onlara çalışma.",
    kapsamDisi=["Uzay araçlarını karşılaştırma (FB.7.1.1)", "Teleskoplar ve gözlem araçları (FB.7.1.2)", "Türkiye'nin uyduları", "Takımyıldızlar", "Enerji dönüşümü ve sürtünme"],
    puanNotu="Puanlar tahminidir: okul soruların puanını farklı dağıtabilir. Toplam 100.",
    kaynakNotu="Sorular MEB'in yayımladığı 'Yazılıya Hazırlanıyorum 7. Sınıf Fen Bilimleri 1. Dönem 1. Yazılı' örneklerine ve ders kitabına dayanır.")

# =====================================================================
# KAZANIMLAR (Hatırla kartları)
# =====================================================================
Y.kazanim(kod="FB.7.1.3", ad="Uzay araştırmalarının yol açabileceği problemleri çözebilme", kisa="Uzay Kirliliği", soru=1, renk="#1f9e8f",
    konular=["u1k4"], sayfa="s. 30, 32", svg=Z.uzay_copu(),
    maddeler=["Görevini bitirmiş uydular, roket parçaları ve yakıt tankları Dünya'nın çevresinde kontrolsüz dolanır. Buna <b>uzay kirliliği</b> denir. (s. 30)",
              "<b>Nedeni:</b> İşlevini yitiren uzay araçları ve parçaları yörüngede kalır. (s. 30, 32)",
              "<b>Sonucu:</b> Parçalar çok hızlıdır; küçük bir parça bile uzay aracına büyük zarar verir. (s. 32)",
              "Önlem alınmazsa uzay araştırmaları, haberleşme, ulaşım (GPS) ve güvenlik aksar. (s. 32)",
              "<b>Çözüm:</b> Çöpleri yakalayıp Dünya'ya getirmek, görevi biten uyduları kontrollü olarak yörüngeden çıkarmak, çevreci teknolojiler. (s. 32)"],
    kelimeler=["uzay kirliliği", "görevi biten uydu", "yörünge", "çarpışma", "çok hızlı", "haberleşme / GPS aksar", "toplayıp Dünya'ya getirmek"],
    hatalar=[{"yanlis": "Uzay kirliliği atmosferdeki hava kirliliğidir.", "dogru": "Uzay kirliliği, Dünya'nın çevresinde dolanan işlevsiz uydu ve roket parçalarıdır."},
             {"yanlis": "Çözüm sorusunda yalnızca yöntemi yazmak.", "dogru": "Yöntemi yaz + çünkü ile neden işe yarayacağını (ya da eksik yanını) yaz."},
             {"yanlis": "“Küçük parça zarar vermez.”", "dogru": "Parçalar çok hızlı olduğu için küçük parça bile büyük zarar verir."}])

Y.kazanim(kod="FB.7.1.4", ad="Yıldızların yaşamını açıklayarak yapılandırabilme", kisa="Yıldızların Yaşamı", soru=1, renk="#d9480f",
    konular=["u1k5"], sayfa="s. 40–42", svg=Z.dongu(),
    maddeler=["Yıldızlar <b>bulutsu (nebula)</b> denen gaz ve toz bulutlarında doğar. (s. 41)",
              "Gaz ve toz bulutu kütle çekimiyle çöker, ısınır: <b>ön yıldız</b> oluşur. Merkezinde tepkimeler başlayınca yıldız olur. (s. 42)",
              "Yıldızın yaşamını <b>kütlesi</b> belirler. Kütle büyükse yaşam <b>kısa</b> olur. (s. 42)",
              "<b>Küçük kütleli</b> (Güneş'in yaklaşık 8 katından az): kırmızı dev → gezegenimsi bulutsu → <b>beyaz cüce</b>. (s. 42)",
              "<b>Büyük kütleli</b> (8 Güneş kütlesinden fazla): kırmızı süperdev → <b>süpernova</b> patlaması → nötron yıldızı veya <b>kara delik</b>. (s. 42)",
              "Güneş orta büyüklükte, küçük kütleli bir yıldızdır: sonu beyaz cüce olur, kara delik olmaz. (s. 40, 42)"],
    kelimeler=["bulutsu (nebula)", "başlangıç kütlesi", "kırmızı dev", "beyaz cüce", "kırmızı süperdev", "süpernova", "nötron yıldızı", "kara delik"],
    hatalar=[{"yanlis": "Güneş kara delik olacak.", "dogru": "Güneş küçük kütleli; beyaz cüce olarak sona erecek."},
             {"yanlis": "Kırmızı dev ile kırmızı süperdevi karıştırmak.", "dogru": "Dev → küçük kütleli yol. Süperdev → büyük kütleli yol."},
             {"yanlis": "Kütlesi büyük yıldız daha uzun yaşar.", "dogru": "Kütle büyükse yaşam daha kısa olur."}])

Y.kazanim(kod="FB.7.1.5", ad="Yıldız, galaksi ve evren kavramlarını açıklayarak yapılandırabilme", kisa="Yıldız, Galaksi, Evren", soru=1, renk="#6741d9",
    konular=["u1k7"], sayfa="s. 46, 48", svg=Z.kapsama(),
    maddeler=["<b>Galaksi (gök ada):</b> Yıldız, gezegen, bulutsu, gök taşı gibi gök cisimlerinden oluşan yapı. (s. 48)",
              "<b>Evren:</b> Dünya, yıldızlar, gezegenler, galaksiler gibi tüm gök cisimlerini içine alan boşluk. (s. 48)",
              "Bu kavramlar birbirini kapsar. Büyükten küçüğe: <b>Evren → Galaksi → (Güneş sistemi) → Yıldız</b>. (s. 46)",
              "Güneş sistemi, sarmal kollu <b>Samanyolu</b> galaksisindedir. En yakın galaksi <b>Andromeda</b>'dır. (s. 48)",
              "Yıldız: ısı ve ışık yayan, büyük gaz küresi şeklindeki gök cismi. (MEB örnek sorusu)",
              "Akılda tutmak için adres gibi düşün: ülke içinde il, il içinde ilçe, ilçe içinde mahalle. (s. 46)"],
    kelimeler=["birbirini kapsar", "evren en büyük", "galaksi = gök ada", "Samanyolu (sarmal)", "Andromeda", "tüm gök cisimlerini içine alan boşluk"],
    hatalar=[{"yanlis": "Galaksi → Evren → Yıldız diye sıralamak.", "dogru": "En büyük evren: Evren → Galaksi → Yıldız."},
             {"yanlis": "Güneş sistemi ile galaksiyi aynı şey sanmak.", "dogru": "Güneş sistemi, Samanyolu galaksisinin küçük bir parçasıdır."},
             {"yanlis": "Güneş sistemi Andromeda'dadır.", "dogru": "Güneş sistemi Samanyolu'nda. Andromeda en yakın komşu galaksi."}])

Y.kazanim(kod="FB.7.2.1", ad="Fiziksel anlamda yapılan işin bağlı olduğu faktörlere ilişkin bilimsel çıkarım yapabilme", kisa="Fiziksel Anlamda İş", soru=2, renk="#1971c2",
    konular=["u2k1"], sayfa="s. 61–62", svg=Z.iki_kosul(),
    maddeler=["İş için <b>iki koşul</b>: 1) Cisme kuvvet uygulanmalı. 2) Cisim, kuvvetle <b>aynı doğrultuda</b> hareket etmeli (yer değiştirmeli). (s. 61–62)",
              "Kuvvet var ama cisim hareket etmiyorsa iş <b>yok</b>: duvarı itmek, halteri havada tutmak. (s. 62)",
              "Kuvvet ile hareket <b>dik</b> ise o kuvvet iş yapmaz: poşeti yukarı tutup düz yolda yürümek. (s. 62)",
              "İş; kuvvet ve kuvvet doğrultusunda alınan yol ile <b>doğru orantılıdır</b>. Kuvvet ya da yol artarsa iş artar. (s. 62)",
              "Kuvvet newton (N), yol metre (m) olursa işin birimi <b>joule (J)</b> olur. (s. 62)",
              "Fizikteki iş, günlük hayattaki işten farklıdır: yorulmak iş yapıldığını göstermez. (s. 62)"],
    kelimeler=["kuvvet uygulanmalı", "aynı doğrultuda", "yer değiştirme / yol alma", "dik → iş yok", "doğru orantılı", "joule (J)"],
    hatalar=[{"yanlis": "“Çok yoruldu, demek ki iş yaptı.”", "dogru": "Yorulmak değil; kuvvet doğrultusunda yer değiştirme önemlidir."},
             {"yanlis": "Poşetleri taşıyarak yürüyen kişi poşetlere iş yapar.", "dogru": "Kuvvet yukarı, hareket yatay: doğrultular dik, iş yok."},
             {"yanlis": "Sadece “evet” ya da “hayır” yazmak.", "dogru": "Evet/hayır + çünkü: kuvvet ve hareketin doğrultusunu yaz."}])

Y.kazanim(kod="FB.7.2.2", ad="Enerji çeşitlerinden kinetik ve potansiyel enerjiyi karşılaştırabilme", kisa="Kinetik ve Potansiyel Enerji", soru=1, renk="#e8590c",
    konular=["u2k2", "u2k3"], sayfa="s. 64, 66–68", svg=Z.enerji_iki(),
    maddeler=["<b>Enerji</b>, iş yapabilme yeteneğidir. Birimi joule'dür. (s. 64)",
              "<b>Kinetik enerji:</b> Cismin hareketinden dolayı sahip olduğu enerji. <b>Kütle</b> ve <b>hız (sürat)</b> ile doğru orantılı. (s. 66–67)",
              "<b>Çekim potansiyel enerjisi:</b> Cismin yüksekliğinden dolayı sahip olduğu enerji. <b>Ağırlık (kütle)</b> ve <b>yükseklik</b>e bağlı. (s. 68)",
              "<b>Esneklik potansiyel enerjisi:</b> Gerilen yay, paket lastiği gibi esnek cisimlerde depolanan enerji. (s. 68)",
              "<b>Fark:</b> Kinetik enerji için cisim hareket etmeli. Potansiyel enerji için yükseklik (konum) ya da esneklik gerekir. Duran cismin kinetik enerjisi yoktur. (s. 66, 68)",
              "<b>Benzerlik:</b> İkisi de enerjidir, birimleri joule, ikisi de kütleye bağlıdır. (s. 64, 67–68)"],
    kelimeler=["kinetik = hareket", "kütle + hız", "potansiyel = yükseklik / konum", "kütle (ağırlık) + yükseklik", "esneklik", "duran cisim → kinetik yok"],
    hatalar=[{"yanlis": "Kinetik enerji yüksekliğe bağlıdır.", "dogru": "Kinetik: kütle + hız. Çekim potansiyel: kütle + yükseklik. (s. 69)"},
             {"yanlis": "Dalda duran elmanın kinetik enerjisi vardır.", "dogru": "Duruyorsa kinetik enerji yok; yüksekte olduğu için çekim potansiyel enerjisi var."},
             {"yanlis": "Karşılaştırma sorusunda yalnız birini anlatmak.", "dogru": "İkisini de yaz: “Kinetik …, potansiyel ise …”"}])

# =====================================================================
# CEVAP KALIPLARI
# =====================================================================
Y.formul(id="cunku", ad="Cevap + Çünkü", kalip="… dır, çünkü …", ne="“Açıklayınız”, “neden”, “değerlendiriniz” sorularında",
         ornek="Hayır, iş yapılmamıştır, çünkü halter yer değiştirmemiştir.")
Y.formul(id="karsilastir", ad="Karşılaştır", kalip="X … , Y ise … . İkisi de …", ne="“Karşılaştırınız”, “fark nedir” sorularında",
         ornek="Kinetik enerji için cisim hareket etmelidir, çekim potansiyel enerjisi için ise yüksekte olmalıdır.")
Y.formul(id="sira", ad="Sırala", kalip="A → B → C (büyükten küçüğe)", ne="“Sıralayınız”, “evreleri yazınız” sorularında",
         ornek="Evren → Galaksi → Yıldız")
Y.formul(id="problem", ad="Problem · Neden · Sonuç", kalip="Problem … dır. Nedeni … . Sonucu …", ne="“Problem nedir, nedenleri ve sonuçları” sorularında",
         ornek="Problem uzay kirliliğidir. Nedeni görevi biten uyduların yörüngede kalmasıdır. Sonucu uzay araçlarına çarpıp zarar vermesidir.")
Y.formul(id="tahmin", ad="Tahmin + Gerekçe", kalip="Bence … olur, çünkü …", ne="“Tahmininizi yazınız”, “sizce hangisi” sorularında",
         ornek="Bence GPS bozulabilir, çünkü çöpler çalışan uydulara çarpabilir.")

# =====================================================================
# MEB SORULARI (senaryoya giren 3–9) + ikizleri
# =====================================================================
Y.meb(id="m3", no=3, kazanim="FB.7.1.3",
    metin=["İnsanlık, son 60 yılda uzaya binlerce uydu fırlattı. Görevini tamamlamış uydular, roketten kopan parçalar ve boya parçaları bile Dünya yörüngesinde saatte binlerce kilometre hızla dolanmaktadır. Bilim insanları, bu durumun gelecekteki uzay yolculuklarını imkânsız hâle getirebileceğinden endişe ediyor."],
    maddeler=[
        M("a", "Uzay araştırmaları esnasında yaşanan bu problem nedir? Bu durumun nedenlerini ve sonuçlarını kısaca yazınız.",
          "Bu problem uzay kirliliğidir. Nedeni, görevini tamamlamış uyduların ve roket parçalarının yörüngede kalmasıdır. Sonucu, bu çok hızlı parçaların yeni uzay araçlarına çarpıp zarar verebilmesidir.",
          [KIRLILIK, NEDEN_COP, ZARAR], "problem",
          {"tur": "kisa", "soru": "Önce ısınalım: Metinde anlatılan problemin adı nedir?", "yanit": "uzay kirliliği", "kabul": ["uzay çöpü", "uzay kirliliği problemi", "uzay çöpleri"], "aciklama": "Yörüngede dolanan işlevsiz araç ve parçalar uzay kirliliği oluşturur. (s. 30)"}),
        M("b", "Eğer bu sorun çözülmezse gelecekte, günlük hayatımızı etkileyen teknolojilerde ne gibi aksaklıklar yaşanabilir? Tahmininizi kısaca yazınız.",
          "Yörüngedeki çöpler çalışan uydulara çarpabilir. Bu yüzden televizyon yayınları kesilebilir, GPS (navigasyon) bozulabilir, hava durumu tahminleri yapılamayabilir.",
          [A("Çöpler çalışan uydulara zarar verir", "uydu"), TEKNOLOJI], "tahmin",
          {"tur": "dytablo", "soru": "Önce ısınalım: Uzay kirliliği çözülmezse hangileri olabilir? D ya da Y seç.", "ifadeler": [
              {"s": "GPS (navigasyon) bozulabilir.", "d": True}, {"s": "Televizyon yayınları kesilebilir.", "d": True},
              {"s": "Hava durumu tahminleri zorlaşabilir.", "d": True}, {"s": "Yağmurlar tamamen durur.", "d": False}],
           "aciklama": "Çöpler uydulara çarparsa haberleşme ve ulaşım (GPS) aksar. (s. 32)"}),
        M("c", "Bu problemi çözmek için iki öneri var: 1. Eski uyduları Dünya atmosferine çekerek yanmalarını sağlamak. 2. Uzaydaki çöpleri dev ağlar veya mıknatıslar yardımıyla toplayıp temizlemek. Sizce bu çözüm yollarından hangisi daha uygulanabilir? Seçtiğiniz yöntemin neden daha iyi olduğunu veya eksik yanlarını açıklayınız.",
          "Örnek: 2. yöntem daha uygulanabilir, çünkü bazı uydular çok yüksekte olduğu için onları atmosfere çekmek zordur; ağla toplamak daha kesin bir çözümdür. (1. yöntemi seçip “atmosferde yanan uydu tamamen ortadan kalkar” diye açıklamak da doğrudur.)",
          [A("Bir yöntem seçmek (1. ya da 2.)", "1.", "2.", "birinci", "ikinci", "atmosfer", "ağ", "mıknatıs"), A("Gerekçe: çünkü … (neden daha iyi ya da eksik yanı)", "çünkü", "için", "zor", "kolay", "kesin", "tamamen")], "cunku")],
    ikizler=[
        {"metin": ["Bir haber sitesinde şu bilgi yer alıyor: “Görevini tamamlamış bir hava durumu uydusu kontrolden çıktı ve Dünya'nın çevresinde dolanmaya devam ediyor. Bu uydu, aynı yörüngedeki bir haberleşme uydusuna çok yaklaştı.”"],
         "maddeler": [
            M("a", "Haberde anlatılan durum hangi probleme örnektir? Bu problemin bir nedenini yazınız.",
              "Bu durum uzay kirliliğine örnektir. Nedeni, görevini tamamlamış uyduların yörüngede kalıp dolanmaya devam etmesidir.", [KIRLILIK, NEDEN_COP], "problem"),
            M("b", "İki uydu çarpışırsa Dünya'daki insanların günlük hayatı nasıl etkilenebilir? Tahmininizi yazınız.",
              "Haberleşme uydusu zarar görürse telefon, televizyon ya da internet bağlantıları kesilebilir.", [A("Çalışan uydu zarar görür", "uydu", "zarar"), TEKNOLOJI], "tahmin"),
            M("c", "Bu tür problemleri önlemek için bir çözüm önerisi yazınız ve önerinizin neden işe yarayacağını açıklayınız.",
              "Görevi biten uydular kontrollü olarak yörüngeden çıkarılmalıdır. Böylece yörüngede dolanan çöp azalır ve çarpışma riski düşer.",
              [A("Çözüm: yörüngeden çıkarmak, toplamak, yakalayıp Dünya'ya getirmek…", "yörüngeden çıkar", "topla", "yakala", "getir", "atmosfer", "temizle"), A("Gerekçe: çöp azalır / çarpışma riski düşer", "azal", "risk", "düş", "önle", "çünkü")], "cunku")]},
        {"metin": ["Bir uzay ajansı, yörüngedeki çöpler için iki proje hazırladı. 1. Proje: Çöpleri robot kollu bir uzay aracıyla tek tek yakalayıp Dünya'ya getirmek. 2. Proje: Yeni fırlatılan her uyduya, görevi bitince kendini yörüngeden çıkaracak bir sistem eklemek."],
         "maddeler": [
            M("a", "Bu projeler hangi problemi çözmek için hazırlanmıştır? Problemin bir sonucunu yazınız.",
              "Uzay kirliliği problemini çözmek için hazırlanmıştır. Sonucu: çok hızlı hareket eden çöpler uzay araçlarına çarpıp zarar verebilir.", [KIRLILIK, ZARAR], "problem"),
            M("b", "Sizce hangi proje gelecekte daha etkili olur? Nedenini açıklayınız.",
              "Örnek: 2. proje daha etkili olur, çünkü yeni uydular görevleri bitince kendiliğinden yörüngeden çıkar ve yeni çöp oluşmaz. (1. projeyi seçip “var olan çöpleri temizler” demek de doğrudur.)",
              [A("Bir proje seçmek", "1.", "2.", "birinci", "ikinci"), A("Gerekçe: çünkü …", "çünkü", "için")], "cunku"),
            M("c", "Uzay çöpü küçük bir boya parçası kadar küçük olsa bile tehlikelidir. Bunun nedenini açıklayınız.",
              "Uzay çöpleri çok yüksek hızla hareket eder. Bu yüzden küçük bir parça bile uzay aracına çarptığında büyük zarar verir.",
              [A("Çok hızlı hareket ederler", "hız", "hızlı", "sürat"), ZARAR], "cunku")]}])

Y.meb(id="m4", no=4, kazanim="FB.7.1.4", svg=Z.dongu(),
    metin=["Aşağıda yıldızların doğumundan ölümüne kadar izlediği iki farklı yaşam döngüsü şematize edilmiştir."],
    maddeler=[
        M("a", "Şemaya göre tüm yıldızların ortak doğum yeri olan yapıya ne ad verilir? Bu yapıdan çıkan bir yıldızın “süpernova patlaması” ile ömrünü tamamlaması için başlangıçta nasıl bir kütleye sahip olması gerekir?",
          "Bu yapıya bulutsu (nebula) denir. Süpernova patlaması için yıldızın başlangıçta büyük kütleli olması gerekir.",
          [A("Bulutsu (nebula)", "bulutsu", "nebula"), KUTLE_B], None,
          {"tur": "bosluk", "soru": "Önce ısınalım: Boşlukları doldur.", "cumleler": [
              {"c": "Bütün yıldızlar ___ adı verilen gaz ve toz bulutlarında doğar.", "cevap": "bulutsu"},
              {"c": "Süpernova patlaması ___ kütleli yıldızlarda görülür.", "cevap": "büyük"}],
           "havuz": ["küçük", "kara delik"], "aciklama": "Yıldızlar bulutsuda doğar; süpernova büyük kütleli yıldızların sonudur. (s. 41–42)"}),
        M("b", "Güneş, orta büyüklükte (küçük kütleli) bir yıldızdır. Güneş'in yaşam döngüsünün sonunda bir “kara delik”e dönüşmesi beklenebilir mi? Şemadaki verilere dayanarak kısaca açıklayınız.",
          "Hayır, beklenemez. Çünkü Güneş küçük kütleli bir yıldızdır. Kara delik yalnızca büyük kütleli yıldızların süpernova patlamasından sonra oluşur. Güneş ömrünü beyaz cüce olarak tamamlar.",
          [A("Hayır", "hayır", "beklenemez", "dönüşmez", "olmaz", "olamaz", "beklenmez"), KUTLE_K, A("Kara delik büyük kütleli yıldızdan (süpernovadan sonra) oluşur", "büyük kütle", "büyük", "süpernova"), BEYAZ], "cunku",
          {"tur": "dy", "ifade": "Güneş'in ömrünü kara delik olarak tamamlaması beklenir.", "dogru": False, "duzeltme": "Güneş küçük kütleli bir yıldızdır; beyaz cüce olarak sona erer.", "aciklama": "Kara delik büyük kütleli yıldızlardan oluşur. (s. 42)"})],
    ikizler=[
        {"metin": ["Kütlesi Güneş'in yaklaşık 20 katı olan A yıldızı ile kütlesi Güneş kadar olan B yıldızı aynı bulutsuda doğuyor."],
         "maddeler": [
            M("a", "Hangi yıldız ömrünü süpernova patlamasıyla tamamlar? Nedenini yazınız.",
              "A yıldızı süpernova patlamasıyla ömrünü tamamlar, çünkü kütlesi Güneş'in 8 katından fazladır, yani büyük kütleli bir yıldızdır.",
              [A("A yıldızı", "a yıldızı", "a'"), KUTLE_B], "cunku"),
            M("b", "B yıldızının yaşamının son evresi ne olur? Bu evreye gelmeden önce hangi evreden geçer?",
              "B yıldızı beyaz cüce olarak sona erer. Önce kırmızı dev, sonra gezegenimsi bulutsu evresinden geçer.",
              [BEYAZ, A("Kırmızı dev (ve gezegenimsi bulutsu)", "kırmızı dev", "gezegenimsi")], "sira"),
            M("c", "Hangi yıldızın yaşamı daha kısa sürer? Açıklayınız.",
              "A yıldızının yaşamı daha kısa sürer, çünkü yıldızın kütlesi ne kadar büyükse yaşamı o kadar kısa olur.",
              [A("A yıldızı", "a yıldızı", "a'"), A("Kütle büyükse yaşam kısa", "kütle")], "cunku")]},
        {"metin": ["Bir öğrenci, büyük kütleli bir yıldızın yaşam evrelerini karışık olarak yazmış: kırmızı süperdev, bulutsu, kara delik, süpernova, büyük kütleli yıldız."],
         "maddeler": [
            M("a", "Bu evreleri doğumdan ölüme doğru sıralayınız.",
              "Bulutsu → Büyük kütleli yıldız → Kırmızı süperdev → Süpernova → Kara delik",
              [SIRA("Doğru sıra: bulutsu → büyük kütleli yıldız → kırmızı süperdev → süpernova → kara delik", "bulutsu", ["büyük kütle"], "süperdev", "süpernova", ["kara delik", "karadelik"])], "sira",
              {"tur": "secim", "soru": "Önce ısınalım: Doğru sıralama hangisidir?", "secenekler": [
                  "Bulutsu → Büyük kütleli yıldız → Kırmızı süperdev → Süpernova → Kara delik",
                  "Bulutsu → Kırmızı süperdev → Büyük kütleli yıldız → Kara delik → Süpernova",
                  "Büyük kütleli yıldız → Bulutsu → Süpernova → Kırmızı süperdev → Kara delik",
                  "Bulutsu → Büyük kütleli yıldız → Kırmızı dev → Beyaz cüce → Kara delik"], "dogru": 0,
               "aciklama": "Büyük kütleli yıldız süperdev olur, süpernova ile patlar, geriye kara delik ya da nötron yıldızı kalır. (s. 42)"}),
            M("b", "Bu yıldızın yaşamı süpernova yerine beyaz cüce ile bitseydi, başlangıç kütlesi hakkında ne söylenebilirdi?",
              "Yıldız küçük kütleli olurdu; yani başlangıç kütlesi Güneş'in yaklaşık 8 katından az olurdu.", [KUTLE_K], "cunku")]}])

Y.meb(id="m5", no=5, kazanim="FB.7.1.4",
    metin=["Aşağıda, uzayda yaşamının farklı evrelerinde bulunan üç farklı gök cisminin kendi ağzından anlattığı bilgiler yer almaktadır.",
           "X Cismi: “Ben büyük bir gaz ve toz bulutuyum. İçimde kütle çekimi sayesinde sıkışan maddeler yeni yıldızların doğmasına imkân sağlar.”",
           "Y Cismi: “Ben çok büyük kütleli bir yıldızdım. Ömrümün sonunda muazzam bir patlama geçirdim ve şimdi ışığın bile kaçamadığı çok güçlü bir çekim merkezine dönüştüm.”",
           "Z Cismi: “Ben orta büyüklükte bir yıldızım. Milyarlarca yıldır ısı ve ışık yayıyorum. Enerjim bittiğinde önce şişip kızıl bir deve dönüşeceğim. En sonunda beyaz bir cüce olarak sessizce veda edeceğim.”"],
    maddeler=[
        M("a", "Yukarıda kendisini tanıtan X, Y ve Z cisimlerinin bilimsel adlarını yazınız.",
          "X: Bulutsu (nebula). Y: Kara delik. Z: Küçük kütleli yıldız (Güneş gibi).",
          [A("X: bulutsu (nebula)", "bulutsu", "nebula"), A("Y: kara delik", "kara delik", "karadelik"), A("Z: küçük kütleli yıldız", "küçük kütle", "güneş")], None,
          {"tur": "eslestir", "soru": "Önce ısınalım: Cisimleri adlarıyla eşleştir.", "ciftler": [
              {"sol": "X: Gaz ve toz bulutu, içinde yıldızlar doğar.", "sag": "Bulutsu (nebula)"},
              {"sol": "Y: Patlamadan sonra ışığın kaçamadığı çekim merkezi oldu.", "sag": "Kara delik"},
              {"sol": "Z: Kırmızı dev, sonra beyaz cüce olacak.", "sag": "Küçük kütleli yıldız"}],
           "aciklama": "Yıldız bulutsuda doğar; büyük kütleli kara delik, küçük kütleli beyaz cüce olur. (s. 41–42)"}),
        M("b", "Metindeki Y cismi ile Z cisminin yaşamlarının “son evrelerinin” neden birbirinden farklı olduğunu, yıldızların başlangıçtaki hangi temel özelliğiyle açıklarsınız?",
          "Bu farkın nedeni yıldızların başlangıçtaki kütleleridir. Büyük kütleli yıldız (Y) süpernova patlamasıyla kara delik ya da nötron yıldızı olur. Küçük kütleli yıldız (Z) patlamadan beyaz cüce olur.",
          [BASLANGIC_KUTLE, A("Büyük kütleli → süpernova → kara delik / nötron yıldızı", "süpernova", "nötron", "büyük kütle"), A("Küçük kütleli → beyaz cüce", "beyaz cüce", "küçük kütle")], "karsilastir",
          {"tur": "secim", "soru": "Önce ısınalım: Y ve Z'nin son evrelerini farklı yapan özellik hangisidir?", "secenekler": ["Başlangıçtaki kütleleri", "Renkleri", "Dünya'ya uzaklıkları", "Parlaklıkları"], "dogru": 0,
           "aciklama": "Yıldızların yaşam sürecini kütleleri belirler. (s. 42)"})],
    ikizler=[
        {"metin": ["K: “Ben donuk kırmızı bir yapıyım. Gaz ve toz bulutu çöküp ısınınca oluştum. Merkezimde tepkimeler başlayınca yıldız olacağım.”",
                   "L: “Ben büyük kütleli bir yıldızın ömrünün sonundaki dev patlamayım. Benden sonra geriye nötron yıldızı ya da kara delik kalır.”",
                   "M: “Ben küçük kütleli bir yıldızdan geriye kalan demir ve karbon yığınıyım.”"],
         "maddeler": [
            M("a", "K, L ve M cisimlerinin bilimsel adlarını yazınız.", "K: Ön yıldız. L: Süpernova. M: Beyaz cüce.",
              [A("K: ön yıldız", "ön yıldız", "önyıldız"), A("L: süpernova", "süpernova"), A("M: beyaz cüce", "beyaz cüce")]),
            M("b", "L ve M'nin oluştuğu yıldızları kütleleri bakımından karşılaştırınız.",
              "L büyük kütleli bir yıldızın sonunda oluşur. M ise küçük kütleli bir yıldızdan geriye kalır.", [KUTLE_B, KUTLE_K], "karsilastir")]},
        {"metin": ["N: “Ben Güneş'ten çok daha büyük, şişmiş bir yıldızım. Başlangıçta büyük kütleli bir yıldızdım. Yakında dev bir patlama yaşayacağım.”",
                   "P: “Ben de şişmiş bir yıldızım ama başlangıç kütlem küçüktü. Bir sonraki evrede gezegenimsi bulutsu olacağım.”"],
         "maddeler": [
            M("a", "N ve P yıldızları şu an hangi evrededir? Adlarını yazınız.", "N: Kırmızı süperdev. P: Kırmızı dev.",
              [A("N: kırmızı süperdev", "süperdev"), A("P: kırmızı dev", "kırmızı dev")]),
            M("b", "N ve P yıldızlarının yaşamları nasıl sona erecek? Bu farkın nedeni nedir?",
              "N süpernova patlamasıyla sona erer, geriye nötron yıldızı ya da kara delik kalır. P beyaz cüce olur. Farkın nedeni başlangıç kütleleridir.",
              [A("N: süpernova → nötron yıldızı / kara delik", "süpernova", "nötron", "kara delik"), BEYAZ, BASLANGIC_KUTLE], "karsilastir")]}])

Y.meb(id="m6", no=6, kazanim="FB.7.1.5",
    metin=["Bir gök bilimci, keşfettiği yeni bir gök cisminin yerini tarif ederken şu ifadeleri kullanmaktadır:",
           "“Keşfettiğim bu gök cismi, çevresine ısı ve ışık yayan büyük bir gaz küresidir. Bu parlak cisim; milyarlarca benzerinin, gaz ve toz bulutlarının bir araya gelerek oluşturduğu çok büyük bir sistemin içindedir. Bu sistem ise her şeyi içine alan ve sınırı tam olarak bilinmeyen sonsuz boşluğun küçük bir parçasıdır.”"],
    maddeler=[
        M("a", "Yukarıdaki açıklamaya göre hangi kavramlardan bahsedilmiştir? İsimlerini yazınız. Bu kavramları kapsam alanı en geniş olandan en dar olana (büyükten küçüğe) doğru sıralayınız.",
          "Yıldız, galaksi ve evren. Sıralama: Evren → Galaksi → Yıldız.",
          [A("Yıldız", "yıldız"), A("Galaksi", "galaksi", "gök ada", "gökada"), A("Evren", "evren"), SIRA("Sıra: evren → galaksi → yıldız", "evren", ["galaksi", "gök ada", "gökada"], "yıldız")], "sira",
          {"tur": "secim", "soru": "Önce ısınalım: Kavramların büyükten küçüğe sıralaması hangisidir?", "secenekler": ["Evren → Galaksi → Yıldız", "Galaksi → Evren → Yıldız", "Yıldız → Galaksi → Evren", "Evren → Yıldız → Galaksi"], "dogru": 0,
           "aciklama": "Evren galaksileri, galaksi yıldızları içine alır. (s. 46, 48)"}),
        M("b", "Aşağıdaki cümlelerde boş bırakılan yerleri kavramlar arasındaki ilişkiye uygun şekilde tamamlayınız.", None, None, None,
          {"tur": "bosluk", "cumleler": [
              {"c": "Dünya'nın da içinde bulunduğu sarmal yapıda olan galaksimizin adı ___ galaksisidir.", "cevap": "Samanyolu"},
              {"c": "Milyarlarca galaksiyi ve aralarındaki boşlukları kapsayan en büyük yapıya ___ denir.", "cevap": "evren"},
              {"c": "Galaksilerin ana bileşenlerinden olup ısı ve ışık kaynağı olan küresel gök cisimlerine ___ denir.", "cevap": "yıldız"}],
           "havuz": ["Andromeda", "bulutsu"], "aciklama": "Samanyolu bizim galaksimiz; evren en büyük yapı; yıldız ısı ve ışık kaynağı. (s. 48)"})],
    ikizler=[
        {"metin": ["Bir öğrenci evinin adresini yazdıktan sonra “Benim evrendeki adresim de böyle!” diyor ve şu kavramları kullanıyor: Güneş sistemi, Evren, Samanyolu galaksisi, Dünya."],
         "maddeler": [
            M("a", "Bu kavramları büyükten küçüğe doğru sıralayınız.", "Evren → Samanyolu galaksisi → Güneş sistemi → Dünya",
              [SIRA("Sıra: evren → Samanyolu galaksisi → Güneş sistemi → Dünya", "evren", ["samanyolu", "galaksi"], ["güneş sistemi", "sistem"], "dünya")], "sira"),
            M("b", "Galaksi ve evren kavramlarını kendi cümlelerinizle tanımlayınız.",
              "Galaksi, yıldız, gezegen, bulutsu gibi gök cisimlerinden oluşan büyük yapıdır. Evren ise bütün gök cisimlerini ve galaksileri içine alan boşluktur.",
              [A("Galaksi: gök cisimlerinden (yıldız, gezegen, bulutsu…) oluşan yapı", "gök cisim", "yıldız", "gezegen", "bulutsu"), A("Evren: hepsini içine alan boşluk", "içine alan", "kapsayan", "tüm", "bütün", "hepsini")])]},
        {"metin": ["Uzay istasyonundaki bir astronot şöyle düşünüyor: “Gördüğüm her parlak nokta ısı ve ışık yayan dev bir gaz küresi. Bunlardan milyarlarcası, sarmal kolları olan büyük bir yapının içinde. Bu yapının yakınında, çapı onun yaklaşık iki katı olan komşu bir yapı daha var.”"],
         "maddeler": [
            M("a", "Astronotun “parlak noktalar” ve “sarmal kolları olan büyük yapı” dediği kavramlar nelerdir?", "Parlak noktalar yıldızdır. Sarmal kolları olan büyük yapı galaksidir (Samanyolu galaksisi).",
              [A("Yıldız", "yıldız"), A("Galaksi (Samanyolu)", "galaksi", "samanyolu", "gök ada")]),
            M("b", "Komşu yapının adı nedir?", "Andromeda galaksisi.", [A("Andromeda", "andromeda")]),
            M("c", "Bu yapıların hepsini içine alan kavram hangisidir? Tanımını yazınız.", "Evren. Evren, bütün gök cisimlerini ve galaksileri içine alan boşluktur.",
              [A("Evren", "evren"), A("Tanım: hepsini içine alan boşluk", "içine alan", "kapsayan", "boşluk")])]}])

Y.meb(id="m7", no=7, kazanim="FB.7.2.1", svg=Z.itme_tasima(),
    metin=["Fen bilimleri dersinde bir eylemin “fiziksel anlamda iş” sayılabilmesi için belirli şartlar gerekir. Görsellerde yer alan kişilerin durumlarını inceleyerek soruları cevaplayınız.",
           "Görsel 1: Sandığı iterek hareket ettiren kişi. Görsel 2: Poşetleri sallamadan yatayda taşıyan kişi."],
    maddeler=[
        M("a", "Görseldeki kişilerden hangisi fiziksel anlamda iş yapmıştır?",
          "Sandığı iten kişi iş yapmıştır. Poşetleri taşıyan kişi poşetlere yukarı doğru kuvvet uygular ama poşetler yatayda hareket eder. Kuvvet ile hareket yönü dik olduğu için iş yapılmaz.",
          [A("Sandığı iten kişi (Görsel 1)", "sandı", "iten", "görsel 1", "1. görsel", "birinci"), DIK], "cunku",
          {"tur": "dytablo", "soru": "Önce ısınalım: D ya da Y seç.", "ifadeler": [
              {"s": "Sandığı iten kişi fiziksel anlamda iş yapmıştır.", "d": True},
              {"s": "Poşetleri taşıyan kişi poşetlere fiziksel anlamda iş yapmıştır.", "d": False}],
           "aciklama": "Poşette kuvvet yukarı, hareket yatay: doğrultular farklı, iş yok. (s. 62)"}),
        M("b", "Bir eylemin “fiziksel anlamda iş” sayılabilmesi için uygulanan kuvvet ile hareket yönü arasında nasıl bir ilişki olması gerektiğini açıklayınız.",
          "Uygulanan kuvvet ile hareket yönü aynı doğrultuda olmalıdır. Yani cisim, uygulanan kuvvetin doğrultusunda yer değiştirmelidir.",
          [AYNI_DOGRULTU, A("Cisim yer değiştirmeli (hareket etmeli)", "yer değiştir", "hareket", "yol al")], "cunku",
          {"tur": "secim", "soru": "Önce ısınalım: İş için kuvvet ile hareket arasındaki ilişki nasıl olmalıdır?", "secenekler": [
              "Aynı doğrultuda olmalıdır.", "Birbirine dik olmalıdır.", "Kuvvet hareketten büyük olmalıdır.", "İlişki önemli değildir."], "dogru": 0,
           "aciklama": "Cisim, uygulanan kuvvetle aynı doğrultuda yer değiştirmelidir. (s. 61)"})],
    ikizler=[
        {"metin": ["I. Elif yerdeki oyuncak kutusunu sağa doğru itiyor ve kutu sağa doğru ilerliyor.", "II. Kerem ağır bir dolabı itiyor ancak dolap hiç hareket etmiyor.",
                   "III. Duru çantasını elinde tutarak düz bir koridorda ileri doğru yürüyor.", "IV. Bir öğrenci yerdeki topu eğilip yukarı doğru kaldırıyor."],
         "maddeler": [
            M("a", "Hangi durumlarda fiziksel anlamda iş yapılmıştır?", "I ve IV numaralı durumlarda fiziksel anlamda iş yapılmıştır.",
              [A("I. durum", "i ", "i.", "elif"), A("IV. durum", "iv", "kaldır")], None,
              {"tur": "dytablo", "soru": "Önce ısınalım: Her durum için iş yapıldı mı? (D: yapıldı, Y: yapılmadı)", "ifadeler": [
                  {"s": "I. Elif kutuyu itiyor, kutu ilerliyor.", "d": True}, {"s": "II. Kerem dolabı itiyor, dolap kıpırdamıyor.", "d": False},
                  {"s": "III. Duru çantayı tutarak düz yolda yürüyor.", "d": False}, {"s": "IV. Öğrenci topu yukarı kaldırıyor.", "d": True}],
               "aciklama": "İş için kuvvet ve aynı doğrultuda yer değiştirme birlikte gerekir. (s. 61–62)"}),
            M("b", "II ve III numaralı durumlarda neden iş yapılmadığını ayrı ayrı açıklayınız.",
              "II'de kuvvet uygulanmasına rağmen dolap yer değiştirmemiştir. III'te kuvvet yukarı doğru, hareket ise yatay olduğu için doğrultular dik, iş yapılmaz.",
              [YER_DEG_YOK, DIK], "cunku")]},
        {"metin": ["Selim aynı kutuyu, aynı büyüklükteki kuvvetle itiyor. 1. durumda kutu 2 metre, 2. durumda 6 metre ilerliyor."],
         "maddeler": [
            M("a", "Hangi durumda daha fazla iş yapılmıştır? Nedenini açıklayınız.",
              "2. durumda daha fazla iş yapılmıştır, çünkü kuvvet aynı ama kuvvet doğrultusunda alınan yol daha fazladır. İş, alınan yol ile doğru orantılıdır.",
              [A("2. durum", "2.", "ikinci", "6"), A("Yol fazla → iş fazla (doğru orantı)", "yol", "mesafe", "doğru orantı", "metre")], "cunku"),
            M("b", "Selim 1. durumda kuvvetini artırsaydı ve kutu yine 2 metre ilerleseydi yapılan iş nasıl değişirdi? Açıklayınız.",
              "Yapılan iş artardı, çünkü iş, uygulanan kuvvet ile doğru orantılıdır.",
              [A("İş artar", "artar", "artardı", "fazla", "çoğal"), A("İş kuvvetle doğru orantılı", "kuvvet", "doğru orantı")], "cunku")]}])

Y.meb(id="m8", no=8, kazanim="FB.7.2.1", svg=Z.halter(),
    metin=["Görseldeki haltercinin durumlarını inceleyerek soruları cevaplayınız. Durum 1: Kaldırma anı. Durum 2: Sabit tutma anı."],
    maddeler=[
        M("a", "Haltercinin, halteri yerden yukarı doğru kaldırdığı 1. durumu “fiziksel anlamda iş” kavramı açısından değerlendiriniz. Bu durumda iş yapılmış mıdır? Kısaca açıklayınız.",
          "Evet, iş yapılmıştır. Çünkü halterci yukarı yönde kuvvet uygulamış ve halter bu kuvvetle aynı doğrultuda yukarı hareket etmiştir.",
          [EVET_IS, A("Kuvvet yukarı, halter yukarı hareket ediyor (aynı doğrultu)", "aynı doğrultu", "aynı yön", "yukarı", "yer değiştir")], "cunku",
          {"tur": "dy", "ifade": "Halterci halteri yerden yukarı kaldırırken fiziksel anlamda iş yapar.", "dogru": True, "aciklama": "Kuvvet yukarı, halter de yukarı hareket ediyor. (s. 61)"}),
        M("b", "Haltercinin, ağırlığı başının üzerinde sabit tuttuğu 2. durumu “fiziksel anlamda iş” kavramı açısından değerlendiriniz. Bu durumda iş yapılmış mıdır? Kısaca açıklayınız.",
          "Hayır, iş yapılmamıştır. Çünkü halter sabit duruyor, yer değiştirmiyor. Kuvvet olsa da yol alınmadığı için iş sıfırdır.",
          [HAYIR_IS, YER_DEG_YOK], "cunku",
          {"tur": "dy", "ifade": "Halterci halteri başının üzerinde sabit tutarken çok yorulduğu için iş yapar.", "dogru": False, "duzeltme": "Halter yer değiştirmediği için iş yapılmaz; yorulmak iş demek değildir.", "aciklama": "Kuvvet var ama hareket yoksa iş yoktur. (s. 62)"})],
    ikizler=[
        {"metin": ["Ayşe kitap dolu bir kutuyu yerden kaldırıp rafa koyuyor (Durum 1). Sonra başka bir kutuyu iki elinde 10 saniye hareketsiz tutuyor (Durum 2)."],
         "maddeler": [
            M("a", "Durum 1'de Ayşe fiziksel anlamda iş yapmış mıdır? Açıklayınız.", "Evet, iş yapmıştır. Çünkü kutuya yukarı doğru kuvvet uygulamış ve kutu bu kuvvetle aynı doğrultuda yukarı hareket etmiştir.",
              [EVET_IS, A("Kuvvet ve hareket aynı doğrultuda (yukarı)", "aynı doğrultu", "aynı yön", "yukarı", "yer değiştir")], "cunku"),
            M("b", "Durum 2'de Ayşe fiziksel anlamda iş yapmış mıdır? Açıklayınız.", "Hayır, iş yapmamıştır. Çünkü kutu hareketsiz duruyor, yer değiştirmiyor.",
              [HAYIR_IS, YER_DEG_YOK], "cunku")]},
        {"metin": ["Bir garson boş tepsiyi masadan yukarı kaldırıyor (Durum 1). Sonra tepsiyi yere paralel tutarak düz yolda başka masaya yürüyor (Durum 2)."],
         "maddeler": [
            M("a", "Durum 1'de garson tepsiye fiziksel anlamda iş yapmış mıdır? Açıklayınız.", "Evet, iş yapmıştır. Çünkü tepsiye yukarı kuvvet uygulamış ve tepsi aynı doğrultuda yukarı hareket etmiştir.",
              [EVET_IS, A("Kuvvet ve hareket aynı doğrultuda", "aynı doğrultu", "aynı yön", "yukarı")], "cunku"),
            M("b", "Durum 2'de garson tepsiye fiziksel anlamda iş yapmış mıdır? Açıklayınız.", "Hayır, iş yapmamıştır. Çünkü tepsiye uyguladığı kuvvet yukarı doğru, tepsinin hareketi ise yataydır; doğrultular diktir.",
              [HAYIR_IS, DIK], "cunku")]}])

Y.meb(id="m9", no=9, kazanim="FB.7.2.2", svg=Z.elma(),
    metin=["Bir bahçedeki elma ağacını inceleyen öğrenci, daldaki elmanın ve yere düşmekte olan elmanın enerjilerini karşılaştırmak istiyor."],
    maddeler=[
        M("a", "Dalda duran elmanın sahip olduğu enerji çeşidi nedir? Bu enerji, elmanın hangi özelliklerine bağlıdır?",
          "Dalda duran elmanın çekim potansiyel enerjisi vardır. Bu enerji elmanın kütlesine (ağırlığına) ve yerden yüksekliğine bağlıdır.",
          [POTANSIYEL, KUTLE, YUKSEKLIK], None,
          {"tur": "secim", "soru": "Önce ısınalım: Dalda duran elmanın enerjisi hangisidir?", "secenekler": ["Çekim potansiyel enerjisi", "Kinetik enerji", "Esneklik potansiyel enerjisi", "Elektrik enerjisi"], "dogru": 0,
           "aciklama": "Yüksekte duran cismin çekim potansiyel enerjisi vardır. (s. 68)"}),
        M("b", "Elmanın daldan koptuktan sonraki hareketinden dolayı kazandığı enerji çeşidi nedir?", "Kinetik enerji.", [KINETIK]),
        M("c", "Bu iki enerji türü arasındaki en temel farklılığı, enerjinin ortaya çıkması için gereken şartlar bakımından karşılaştırarak açıklayınız.",
          "Kinetik enerji için cismin hareket etmesi (hızının olması) gerekir. Çekim potansiyel enerjisi için ise cismin bir yükseklikte (konumda) bulunması gerekir.",
          [A("Kinetik → hareket / hız gerekir", "hareket", "hız", "sürat"), A("Potansiyel → yükseklik / konum gerekir", "yüksek", "konum")], "karsilastir")],
    ikizler=[
        {"svg": Z.kaydirak(), "metin": ["Bir çocuk kaydırağın tepesinde hareketsiz oturuyor. Sonra kaydıraktan aşağı kayıyor."],
         "maddeler": [
            M("a", "Tepede hareketsiz oturan çocuğun hangi enerjisi vardır? Bu enerji hangi özelliklere bağlıdır?",
              "Çekim potansiyel enerjisi vardır. Bu enerji çocuğun kütlesine (ağırlığına) ve yüksekliğine bağlıdır.", [POTANSIYEL, KUTLE, YUKSEKLIK]),
            M("b", "Kayarken çocuğun hareketinden dolayı sahip olduğu enerji nedir? Bu enerji hangi özelliklere bağlıdır?",
              "Kinetik enerji. Kinetik enerji çocuğun kütlesine ve hızına bağlıdır.", [KINETIK, KUTLE, HIZ]),
            M("c", "Tepede hareketsiz oturan çocuğun kinetik enerjisi var mıdır? Nedenini yazınız.", "Hayır, yoktur. Çünkü çocuk hareket etmiyor; kinetik enerji için hareket gerekir.",
              [A("Hayır, yoktur", "hayır", "yok"), A("Hareket etmiyor", "hareket etm", "hareketsiz", "duruyor", "hareket gerek")], "cunku")]},
        {"svg": Z.yay_ok(), "metin": ["Bir okçu yayını geriyor ve oku fırlatıyor."],
         "maddeler": [
            M("a", "Gerilmiş yayda hangi enerji depolanmıştır?", "Gerilmiş yayda esneklik potansiyel enerjisi depolanmıştır.", [A("Esneklik potansiyel enerjisi", "esneklik")]),
            M("b", "Havada giden okun hareketinden dolayı sahip olduğu enerji nedir?", "Kinetik enerji.", [KINETIK]),
            M("c", "Bu iki enerjiyi, ortaya çıkmaları için gereken şartlar bakımından karşılaştırınız.",
              "Esneklik potansiyel enerjisi için esnek bir cismin (yayın) şeklinin değişmesi, gerilmesi gerekir. Kinetik enerji için ise cismin hareket etmesi gerekir.",
              [A("Esneklik: esnek cismin şekli değişmeli (gerilmeli)", "esnek", "geril", "şekl"), A("Kinetik: hareket gerekir", "hareket", "hız")], "karsilastir")]}])

# =====================================================================
# KUARK'IN HATASI
# =====================================================================
def KH(kazanim, soru, kuark, dogruSik, yanlis1, yanlis2, ipucu, aciklama, dogruCevap):
    Y.kuark(kazanim=kazanim, soru=soru, kuark=kuark, secenekler=[dogruSik, yanlis1, yanlis2], dogru=0, ipucu=ipucu, aciklama=aciklama, dogruCevap=dogruCevap)

KH("FB.7.2.1", "Halteri başının üzerinde sabit tutan halterci iş yapar mı?", "Evet, iş yapar. Çünkü çok yoruluyor ve halteri tutmak için kuvvet uyguluyor.",
   "Yorulmak iş yapıldığını göstermez; halter yer değiştirmediği için iş yapılmaz.", "Halterci halteri tutarken hiç kuvvet uygulamaz.", "Kuark haklı, cevapta hata yok.",
   "İş için iki koşulu hatırla: kuvvet + o doğrultuda yer değiştirme.", "Kuvvet var ama yer değiştirme yok: iş sıfır. (s. 62)",
   "Hayır, iş yapmaz. Çünkü halter sabit duruyor, yer değiştirmiyor.")
KH("FB.7.2.1", "Poşetleri elinde taşıyarak düz yolda yürüyen kişi poşetlere iş yapar mı?", "Evet, iş yapar. Çünkü poşetler kişiyle birlikte yer değiştiriyor.",
   "Poşetler yer değiştiriyor ama kuvvet yukarı, hareket yatay; doğrultular dik olduğu için iş yok.", "Poşetler hiç yer değiştirmiyor.", "Poşetler hafif olduğu için iş yapılmaz.",
   "Kuvvetin yönüne ve hareketin yönüne ayrı ayrı bak.", "Kuvvet ile hareket aynı doğrultuda değilse o kuvvet iş yapmaz. (s. 62)",
   "Hayır, iş yapmaz. Çünkü poşete uygulanan kuvvet yukarı, poşetin hareketi yataydır.")
KH("FB.7.2.1", "Görsel 1'deki kişi sandığı itiyor ve sandık ilerliyor. İş yapılmış mıdır?", "Evet.",
   "Cevap doğru ama “çünkü” kısmı eksik: kuvvet ile hareket aynı doğrultuda olduğu yazılmalı.", "Cevap yanlış; sandığı itmek iş değildir.", "Hata yok, yazılıda tek kelime yeterli.",
   "Açık uçlu soruda puanı ne getirir?", "Yazılıda gerekçesiz cevap tam puan almaz.",
   "Evet, iş yapılmıştır. Çünkü kişi sandığa kuvvet uygulamış ve sandık bu kuvvetle aynı doğrultuda hareket etmiştir.")
KH("FB.7.1.4", "Güneş'in ömrünün sonunda ne olacak?", "Güneş süpernova olarak patlayacak ve kara deliğe dönüşecek.",
   "Güneş küçük kütleli bir yıldızdır; kırmızı dev olup beyaz cüce olarak sona erer.", "Güneş önce nötron yıldızı, sonra beyaz cüce olur.", "Güneş'in yaşamı hiç bitmez.",
   "Güneş küçük kütleli mi, büyük kütleli mi?", "Süpernova ve kara delik büyük kütleli yıldızlara aittir. (s. 42)",
   "Güneş küçük kütleli bir yıldızdır. Kırmızı dev, gezegenimsi bulutsu ve en sonunda beyaz cüce olur.")
KH("FB.7.1.4", "Yıldızların yaşam süresini ne belirler?", "Kütlesi büyük olan yıldız daha uzun yaşar.",
   "Ters söylemiş: kütle büyükse yaşam daha kısa olur.", "Yaşam süresini kütle değil, rengi belirler.", "Yaşam süresini Dünya'ya uzaklığı belirler.",
   "Kütle büyüyünce yaşam uzar mı, kısalır mı?", "Kütle ne kadar büyükse yaşam o kadar kısa olur. (s. 42)",
   "Yıldızın yaşamını kütlesi belirler. Kütle büyükse yaşam kısa olur.")
KH("FB.7.1.4", "Kırmızı süperdev evresinden sonra yıldızın yaşamı nasıl sona erer?", "Kırmızı süperdev sonunda beyaz cüce olur.",
   "Dev ile süperdevi karıştırmış: süperdev süpernova ile patlar, nötron yıldızı ya da kara delik olur.", "Kırmızı süperdev yeniden bulutsuya dönüşür.", "Kuark haklı, hata yok.",
   "Süperdev hangi yolda: küçük mü büyük kütleli mi?", "Kırmızı dev → beyaz cüce; kırmızı süperdev → süpernova. (s. 42)",
   "Kırmızı süperdev süpernova ile patlar; geriye nötron yıldızı ya da kara delik kalır.")
KH("FB.7.1.5", "Evren, galaksi ve yıldızı büyükten küçüğe sıralayınız.", "Galaksi → Evren → Yıldız",
   "Evren en büyüktür ve galaksileri içine alır: Evren → Galaksi → Yıldız.", "Yıldız en büyüktür: Yıldız → Galaksi → Evren.", "Sıralama doğru, hata yok.",
   "Hangisi her şeyi içine alır?", "Evren tüm gök cisimlerini ve galaksileri içine alır. (s. 48)", "Evren → Galaksi → Yıldız")
KH("FB.7.1.5", "Galaksi nedir?", "Galaksi, Güneş ve etrafındaki gezegenlerdir.",
   "Bu Güneş sistemi; galaksi, yıldız ve gezegen gibi pek çok gök cisminden oluşan çok daha büyük bir yapıdır.", "Galaksi, tek bir büyük yıldızdır.", "Tanım doğru, hata yok.",
   "Güneş sistemi galaksinin neresinde?", "Güneş sistemi Samanyolu galaksisinin küçük bir parçasıdır. (s. 48)",
   "Galaksi; yıldız, gezegen, bulutsu, gök taşı gibi gök cisimlerinden oluşan yapıdır.")
KH("FB.7.2.2", "Dalda duran elmanın enerjisi nedir?", "Elmanın kinetik enerjisi vardır, çünkü yüksekte duruyor.",
   "Yüksekte duran cismin çekim potansiyel enerjisi vardır; kinetik enerji için hareket gerekir.", "Elmanın hiç enerjisi yoktur.", "Elmanın esneklik potansiyel enerjisi vardır.",
   "Elma hareket ediyor mu?", "Kinetik = hareket; çekim potansiyel = yükseklik. (s. 66, 68)",
   "Dalda duran elmanın çekim potansiyel enerjisi vardır. Kütlesine ve yüksekliğine bağlıdır.")
KH("FB.7.2.2", "Kinetik enerji hangi özelliklere bağlıdır?", "Kütleye ve yüksekliğe bağlıdır.",
   "Yükseklik potansiyel enerjiyi etkiler; kinetik enerji kütleye ve hıza bağlıdır.", "Kinetik enerji kütleye bağlı değildir.", "Kuark haklı, hata yok.",
   "Kinetik enerji hareketle ilgili; hareketi ne anlatır?", "Kinetik enerji kütle ve hızla doğru orantılıdır. (s. 67)", "Kinetik enerji kütleye ve hıza bağlıdır.")
KH("FB.7.1.3", "Uzay kirliliği nedir?", "Fabrika dumanlarının atmosferi kirletmesidir.",
   "Bu hava kirliliği; uzay kirliliği, Dünya'nın çevresinde dolanan işlevsiz uydu ve roket parçalarıdır.", "Uzay kirliliği, yıldız patlamalarından kalan tozlardır.", "Cevap doğru, hata yok.",
   "Uzay kirliliği nerede oluyor ve neyden oluşuyor?", "Görevi biten uydular ve roket parçaları uzay kirliliği oluşturur. (s. 30)",
   "Uzay kirliliği, görevini bitirmiş uyduların ve roket parçalarının Dünya'nın çevresinde kontrolsüz dolanmasıdır.")
KH("FB.7.1.3", "Uzay kirliliğine bir çözüm önerisi yazınız.", "Uzaya daha çok uydu gönderilmeli.",
   "Bu öneri çöpü artırır; görevi biten uyduları yörüngeden çıkarmak ya da çöpleri toplamak gerekir.", "Öneri doğru ama gerekçe yazılmamış.", "Uydular hiç kullanılmamalı, öneri tamamdır.",
   "Daha çok uydu, daha çok ne demek?", "Çözüm: çöpleri yakalayıp Dünya'ya getirmek, kontrollü yörüngeden çıkarmak. (s. 32)",
   "Görevi biten uydular kontrollü olarak yörüngeden çıkarılmalı ya da çöpler yakalanıp Dünya'ya getirilmelidir.")

# =====================================================================
# PROVA YAZILILARI (Senaryo 4: 6 soru, toplam 100; puanlar tahmini)
# =====================================================================
P1 = Y.prova(id="p1", ad="Prova 1", sorular=[
    {"kazanim": "FB.7.1.3", "puan": 20, "metin": ["Uzay Gözetim Ağı'nın raporlarına göre Dünya'nın çevresinde, farklı büyüklüklerde 130 milyondan fazla parça uzay çöpü olarak dolaşıyor."],
     "maddeler": [
        M("a", "Haberde anlatılan problem nedir? Bu problemin oluşma nedenini yazınız.", "Problem uzay kirliliğidir. Görevini tamamlamış uyduların, roket parçalarının ve yakıt tanklarının yörüngede kalmasıyla oluşur.", [KIRLILIK, NEDEN_COP], "problem", puan=8),
        M("b", "Bu durumun iki olumsuz sonucunu yazınız.", "1. Çok hızlı hareket eden çöpler uzay araçlarına çarpıp zarar verebilir. 2. Çalışan uydular zarar görürse haberleşme ve GPS gibi hizmetler aksayabilir.",
          [ZARAR, TEKNOLOJI], puan=12)]},
    {"kazanim": "FB.7.1.4", "puan": 20, "svg": Z.dongu({"k2": "1", "k4": "2", "b2": "3"}), "metin": ["Aşağıdaki şemada yıldızların yaşam süreci verilmiştir. Bazı evreler numaralarla gösterilmiştir."],
     "maddeler": [
        M("a", "1, 2 ve 3 numaralı evrelerin adlarını yazınız.", "1: Kırmızı dev. 2: Beyaz cüce. 3: Kırmızı süperdev.",
          [A("1: kırmızı dev", "kırmızı dev"), A("2: beyaz cüce", "beyaz cüce"), A("3: kırmızı süperdev", "süperdev")], puan=12),
        M("b", "Bir yıldızın şemadaki hangi yoldan gideceğini belirleyen özellik nedir? Açıklayınız.", "Yıldızın başlangıç kütlesi belirler. Kütlesi Güneş'in yaklaşık 8 katından az olan yıldız üst yoldan, fazla olan alt yoldan gider.",
          [BASLANGIC_KUTLE, A("Küçük kütle üst yol, büyük kütle alt yol (8 Güneş kütlesi)", "küçük", "büyük", "8", "sekiz")], "cunku", puan=8)]},
    {"kazanim": "FB.7.1.5", "puan": 15, "metin": ["Güneş sistemi, Galaksi, Evren, Dünya"],
     "maddeler": [
        M("a", "Yukarıdaki kavramları büyükten küçüğe doğru sıralayınız.", "Evren → Galaksi → Güneş sistemi → Dünya",
          [SIRA("Sıra: evren → galaksi → Güneş sistemi → Dünya", "evren", ["galaksi", "gök ada"], ["güneş sistemi", "sistem"], "dünya")], "sira", puan=8),
        M("b", "Galaksi nedir? Tanımlayınız ve içinde bulunduğumuz galaksinin adını yazınız.", "Galaksi; yıldız, gezegen, bulutsu, gök taşı gibi gök cisimlerinden oluşan yapıdır. İçinde bulunduğumuz galaksi Samanyolu'dur.",
          [A("Tanım: gök cisimlerinden oluşan yapı", "gök cisim", "yıldız", "gezegen"), A("Samanyolu", "samanyolu")], puan=7)]},
    {"kazanim": "FB.7.2.1", "puan": 15, "metin": ["Can, 20 N'luk kuvvetle bir kutuyu 3 metre; Ece aynı kuvvetle aynı kutuyu 5 metre itiyor."],
     "maddeler": [
        M("a", "Hangisi daha fazla iş yapmıştır? Nedenini açıklayınız.", "Ece daha fazla iş yapmıştır, çünkü kuvvetler aynı ama Ece kutuyu daha uzun yol itmiştir. İş, kuvvet doğrultusunda alınan yol ile doğru orantılıdır.",
          [A("Ece", "ece"), A("Yol fazla → iş fazla", "yol", "mesafe", "metre", "doğru orantı")], "cunku", puan=8),
        M("b", "Can kuvvetini artırsaydı ve kutuyu yine 3 metre itseydi yaptığı iş nasıl değişirdi?", "Yaptığı iş artardı, çünkü iş, uygulanan kuvvet ile doğru orantılıdır.",
          [A("İş artar", "artar", "artardı", "fazla"), A("Kuvvetle doğru orantılı", "kuvvet", "doğru orantı")], "cunku", puan=7)]},
    {"kazanim": "FB.7.2.1", "puan": 15, "metin": ["Mert sırt çantasını sırtında taşıyarak düz yolda okula yürüyor. Okula gelince çantayı yerden kaldırıp sırasının üstüne koyuyor."],
     "maddeler": [
        M("a", "Mert düz yolda yürürken çantaya fiziksel anlamda iş yapar mı? Açıklayınız.", "Hayır, iş yapmaz. Çünkü çantaya uyguladığı kuvvet yukarı doğru, çantanın hareketi ise yataydır; doğrultular diktir.",
          [HAYIR_IS, DIK], "cunku", puan=8),
        M("b", "Mert çantayı yerden sıranın üstüne kaldırırken iş yapar mı? Açıklayınız.", "Evet, iş yapar. Çünkü çantaya yukarı doğru kuvvet uygular ve çanta aynı doğrultuda yukarı hareket eder.",
          [EVET_IS, A("Kuvvet ve hareket aynı doğrultuda (yukarı)", "aynı doğrultu", "aynı yön", "yukarı")], "cunku", puan=7)]},
    {"kazanim": "FB.7.2.2", "puan": 15, "svg": Z.kaykay(), "metin": ["Sürtünmenin önemsenmediği bir kaykay parkurunda K noktası en yüksek, L noktası orta yükseklikte, M noktası en alçak noktadır. Öğrenci K noktasında bir an hareketsiz duruyor, sonra parkurdan aşağı kayıyor."],
     "maddeler": [
        M("a", "Öğrencinin çekim potansiyel enerjisinin en fazla olduğu nokta hangisidir? Nedenini yazınız.", "K noktasıdır, çünkü K en yüksek noktadır. Çekim potansiyel enerjisi yükseklikle artar.",
          [A("K noktası", "k nokta", "k'", "k "), A("En yüksek nokta (yükseklik)", "yüksek")], "cunku", puan=8),
        M("b", "Öğrenci K noktasında hareketsiz durduğu anda kinetik enerjisi var mıdır? Açıklayınız.", "Hayır, yoktur. Çünkü kinetik enerji için hareket gerekir; öğrenci o an hareket etmiyor.",
          [A("Hayır, yoktur", "hayır", "yok"), A("Hareket etmiyor", "hareket etm", "hareketsiz", "duruyor", "hareket gerek")], "cunku", puan=7)]}])

Y.prova(id="p2", ad="Prova 2", sorular=[
    {"kazanim": "FB.7.1.3", "puan": 20, "metin": ["Bir uzay ajansı, görevini tamamlamış uyduların ve roket parçalarının, çalışan uydular için çarpışma riski oluşturduğunu açıkladı."],
     "maddeler": [
        M("a", "Bu problemin adını yazınız. Problemin uzay araştırmalarıyla ilişkisini açıklayınız.", "Problemin adı uzay kirliliğidir. Uzay araştırmaları için gönderilen araçlar görevleri bitince yörüngede kalır ve çöp oluşturur.",
          [KIRLILIK, NEDEN_COP], "problem", puan=8),
        M("b", "Bu problemin azaltılması için iki çözüm önerisi geliştiriniz.", "1. Görevi biten uydular kontrollü olarak yörüngeden çıkarılabilir. 2. Uzay çöpleri özel sistemlerle yakalanıp Dünya'ya getirilebilir.",
          [A("1. öneri: yörüngeden çıkarmak / atmosferde yakmak", "yörüngeden", "atmosfer", "yak"), A("2. öneri: yakalamak, toplamak, Dünya'ya getirmek", "yakala", "topla", "getir", "ağ", "temizle")], puan=12)]},
    {"kazanim": "FB.7.1.4", "puan": 20, "metin": ["A: “Ben gaz ve toz bulutunun çöküp ısınmasıyla oluşan donuk kırmızı bir yapıyım.”", "B: “Ben büyük kütleli bir yıldızın ömrünün sonundaki dev patlamayım.”", "C: “Ben bir yıldızın ömrü bitince geriye kalan, ışığın bile kaçamadığı çok güçlü bir çekim merkeziyim.”"],
     "maddeler": [
        M("a", "A, B ve C'nin bilimsel adlarını yazınız.", "A: Ön yıldız. B: Süpernova. C: Kara delik.",
          [A("A: ön yıldız", "ön yıldız", "önyıldız"), A("B: süpernova", "süpernova"), A("C: kara delik", "kara delik", "karadelik")], puan=9),
        M("b", "Güneş'in yaşamında B ve C evreleri görülür mü? Nedenini açıklayınız.", "Hayır, görülmez. Çünkü Güneş küçük kütleli bir yıldızdır. Süpernova ve kara delik büyük kütleli yıldızlarda görülür. Güneş beyaz cüce olur.",
          [A("Hayır", "hayır", "görülmez", "olmaz"), KUTLE_K, A("B ve C büyük kütleli yıldızlarda görülür", "büyük"), BEYAZ], "cunku", puan=11)]},
    {"kazanim": "FB.7.1.5", "puan": 15, "svg": Z.kapsama(("1", "2", "3"), "İç içe üç çember: 1 en dışta, 3 en içte"), "metin": ["Aşağıdaki iç içe çemberlerde en dıştan içe doğru üç kavram 1, 2 ve 3 numaralarıyla gösterilmiştir."],
     "maddeler": [
        M("a", "1, 2 ve 3 numaralı yerlere yıldız, galaksi ve evren kavramlarından hangilerini yazarsınız?", "1: Evren. 2: Galaksi. 3: Yıldız.",
          [SIRA("1 evren, 2 galaksi, 3 yıldız", "evren", ["galaksi", "gök ada"], "yıldız")], "sira", puan=9),
        M("b", "Evren kavramını tanımlayınız.", "Evren; Dünya, yıldızlar, gezegenler ve galaksiler gibi tüm gök cisimlerini içine alan boşluktur.",
          [A("Tüm gök cisimlerini içine alan", "tüm", "bütün", "hepsini", "içine alan", "kapsayan"), A("boşluk", "boşluk")], puan=6)]},
    {"kazanim": "FB.7.2.1", "puan": 15, "metin": ["Bir öğrenci ağır bir kutuyu 40 N'luk kuvvetle yatay yönde itiyor ve kutu uygulanan kuvvet yönünde 3 metre ilerliyor."],
     "maddeler": [
        M("a", "Bu durumda fiziksel anlamda iş yapılmış mıdır? Sebebiyle birlikte açıklayınız.", "Evet, iş yapılmıştır. Çünkü kutuya kuvvet uygulanmış ve kutu kuvvetle aynı doğrultuda 3 metre yer değiştirmiştir.",
          [EVET_IS, AYNI_DOGRULTU], "cunku", puan=7),
        M("b", "Ertesi gün öğrenci kutuyu aynı kuvvetle itmesine rağmen kutu yerinden kıpırdamıyor. Bu durumda iş yapılır mı? Açıklayınız.", "Hayır, iş yapılmaz. Çünkü kuvvet uygulanmasına rağmen kutu yer değiştirmemiştir.",
          [HAYIR_IS, YER_DEG_YOK], "cunku", puan=8)]},
    {"kazanim": "FB.7.2.1", "puan": 15, "metin": ["Bir öğrenci: “Bir cisme kuvvet uygulanıyorsa mutlaka fiziksel anlamda iş yapılır.” diyor."],
     "maddeler": [
        M("a", "Bu ifadeyi değerlendiriniz ve bir örnekle açıklayınız.", "Bu ifade yanlıştır. Örneğin duvarı itersek kuvvet uygularız ama duvar yer değiştirmediği için iş yapılmaz.",
          [A("İfade yanlış", "yanlış", "doğru değil", "her zaman değil", "mutlaka değil"), A("Örnek: kuvvet var ama hareket yok (duvar, halter…) ya da dik", "duvar", "halter", "hareket etm", "yer değiştirm", "dik", "poşet")], "cunku", puan=8),
        M("b", "Fiziksel anlamda iş yapılması için gerekli iki koşulu yazınız.", "1. Cisme kuvvet uygulanmalıdır. 2. Cisim uygulanan kuvvetle aynı doğrultuda hareket etmelidir (yer değiştirmelidir).",
          [A("1. koşul: kuvvet uygulanmalı", "kuvvet uygul"), A("2. koşul: aynı doğrultuda yer değiştirme", "aynı doğrultu", "doğrultusunda", "yer değiştir")], puan=7)]},
    {"kazanim": "FB.7.2.2", "puan": 15, "svg": Z.kizak(), "metin": ["Bir dağın zirvesinde hareketsiz duran bir kızak ve dağdan aşağı doğru kayan başka bir kızak var."],
     "maddeler": [
        M("a", "Zirvede duran kızağın hangi enerjisi vardır? Bu enerji hangi özelliklere bağlıdır?", "Çekim potansiyel enerjisi vardır. Kızağın kütlesine (ağırlığına) ve yüksekliğine bağlıdır.",
          [POTANSIYEL, KUTLE, YUKSEKLIK], puan=8),
        M("b", "Kayan kızağın hareketinden dolayı sahip olduğu enerji türünü ve bu enerjinin bağlı olduğu iki özelliği yazınız.", "Kinetik enerji. Kızağın kütlesine ve hızına bağlıdır.",
          [KINETIK, KUTLE, HIZ], puan=7)]}])

Y.prova(id="p3", ad="Prova 3", sorular=[
    {"kazanim": "FB.7.1.3", "puan": 20, "metin": ["Uzay çöpü sorununa iki öneri getirildi.", "1. Öneri: Yeni uydular, görevleri bitince atmosfere girip yanacak şekilde tasarlansın.", "2. Öneri: Yörüngedeki çöpler, robot kollu bir temizlik aracıyla yakalanıp Dünya'ya getirilsin."],
     "maddeler": [
        M("a", "Uzay çöpleri çok küçük olsalar bile neden tehlikelidir? Açıklayınız.", "Uzay çöpleri çok yüksek hızla hareket eder. Bu yüzden küçük bir parça bile uzay aracına çarptığında büyük zarar verir.",
          [A("Çok hızlı hareket ederler", "hız", "sürat"), ZARAR], "cunku", puan=8),
        M("b", "Sizce hangi öneri daha uygulanabilir? Seçtiğiniz önerinin neden daha iyi olduğunu ya da diğer önerinin eksik yanını açıklayınız.", "Örnek: 1. öneri daha uygulanabilir, çünkü yeni çöp oluşmasını baştan önler. 2. öneri ise yalnızca var olan çöpleri tek tek toplar ve çok zaman alır.",
          [A("Bir öneri seçmek", "1.", "2.", "birinci", "ikinci"), A("Gerekçe: çünkü … / eksik yanı", "çünkü", "için", "eksik", "zor", "önler")], "cunku", puan=12)]},
    {"kazanim": "FB.7.1.4", "puan": 20, "metin": ["Kütlesi Güneş'in yaklaşık 3 katı olan K yıldızı ile kütlesi Güneş'in yaklaşık 15 katı olan L yıldızı bulunuyor."],
     "maddeler": [
        M("a", "K ve L yıldızlarının yaşamlarının nasıl sona ereceğini yazınız.", "K yıldızı küçük kütleli olduğu için beyaz cüce olarak sona erer. L yıldızı büyük kütleli olduğu için süpernova patlamasıyla sona erer; geriye nötron yıldızı ya da kara delik kalır.",
          [A("K: beyaz cüce", "beyaz cüce"), A("L: süpernova → nötron yıldızı / kara delik", "süpernova", "nötron", "kara delik")], puan=10),
        M("b", "Hangi yıldızın yaşamı daha uzun sürer? Nedenini açıklayınız.", "K yıldızının yaşamı daha uzun sürer, çünkü kütlesi daha küçüktür. Kütle büyüdükçe yaşam kısalır.",
          [A("K yıldızı", "k yıldızı", "k'"), A("Kütle küçük → yaşam uzun", "kütle")], "cunku", puan=10)]},
    {"kazanim": "FB.7.1.5", "puan": 15, "metin": ["Bir öğrenci defterine şu notları almış:", "I. Samanyolu, evrendeki galaksilerden biridir.", "II. Güneş sistemi, Andromeda galaksisinde yer alır.", "III. Evren, bütün gök cisimlerini içine alan boşluktur."],
     "maddeler": [
        M("a", "Notlardan hangisi yanlıştır? Doğrusunu yazınız.", "II. not yanlıştır. Doğrusu: Güneş sistemi Samanyolu galaksisinde yer alır.",
          [A("II. not yanlış", "ii"), A("Doğrusu: Samanyolu", "samanyolu")], puan=9),
        M("b", "Samanyolu galaksisinin şeklini ve ona en yakın galaksinin adını yazınız.", "Samanyolu sarmal şekillidir. En yakın galaksi Andromeda'dır.",
          [A("Sarmal", "sarmal"), A("Andromeda", "andromeda")], puan=6)]},
    {"kazanim": "FB.7.2.1", "puan": 15, "metin": ["I. Ali yerdeki topa vuruyor, top ileri gidiyor.", "II. Zeynep evin duvarını tüm gücüyle itiyor.", "III. Bir işçi tuğlaları yerden kaldırıp kamyona yüklüyor."],
     "maddeler": [
        M("a", "Her durum için fiziksel anlamda iş yapılıp yapılmadığını yazınız.", "I: İş yapılmıştır. II: İş yapılmamıştır. III: İş yapılmıştır.",
          [SIRA("I yapıldı, II yapılmadı, III yapıldı (sırayla)", ["yapılmış", "yapıldı", "evet", "var"], ["yapılmamış", "yapılmadı", "hayır", "yok"], ["yapılmış", "yapıldı", "evet", "var"])], puan=9),
        M("b", "İş yapılmayan durumun nedenini açıklayınız.", "II. durumda Zeynep duvara kuvvet uygular ama duvar yer değiştirmez. Hareket olmadığı için iş yapılmaz.",
          [A("II. durum (duvar)", "duvar", "ii"), YER_DEG_YOK], "cunku", puan=6)]},
    {"kazanim": "FB.7.2.1", "puan": 15, "metin": ["Göktuğ 300 N'luk halteri yerden başının üzerine kaldırıyor ve 5 saniye o şekilde tutuyor. Göktuğ çok yoruluyor."],
     "maddeler": [
        M("a", "Göktuğ halteri kaldırırken fiziksel anlamda iş yapar mı? Açıklayınız.", "Evet, iş yapar. Çünkü halter, uygulanan yukarı yönlü kuvvetle aynı doğrultuda yukarı hareket eder.",
          [EVET_IS, A("Aynı doğrultuda yukarı hareket", "aynı doğrultu", "aynı yön", "yukarı")], "cunku", puan=7),
        M("b", "Göktuğ halteri başının üzerinde tutarken iş yapar mı? Çok yorulduğu hâlde cevabınızın nedenini açıklayınız.", "Hayır, iş yapmaz. Çünkü halter sabit duruyor, yer değiştirmiyor. Yorulmak fiziksel anlamda iş yapıldığını göstermez.",
          [HAYIR_IS, YER_DEG_YOK, A("Yorulmak iş demek değil", "yorul")], "cunku", puan=8)]},
    {"kazanim": "FB.7.2.2", "puan": 15, "svg": Z.grafik(), "metin": ["Grafikte bir cismin çekim potansiyel enerjisinin “a” harfiyle gösterilen bir büyüklüğe bağlı değişimi verilmiştir: a arttıkça enerji de artıyor."],
     "maddeler": [
        M("a", "“a” yerine yazılabilecek iki farklı büyüklüğü yazınız.", "Cismin kütlesi (ağırlığı) ve yerden yüksekliği.", [KUTLE, YUKSEKLIK], puan=8),
        M("b", "Aynı grafik kinetik enerji için çizilseydi “a” yerine hangi iki büyüklük yazılabilirdi?", "Cismin kütlesi ve hızı.", [KUTLE, HIZ], puan=7)]}])

Y.prova(id="p4", ad="Prova 4", sorular=[
    {"kazanim": "FB.7.1.3", "puan": 20, "metin": ["Ece televizyon izlerken görüntü birden kesiliyor. Haberlerde, yayını sağlayan haberleşme uydusuna küçük bir uzay çöpünün çarptığı söyleniyor."],
     "maddeler": [
        M("a", "Bu olay hangi probleme bağlıdır? Problemin nedenini yazınız.", "Bu olay uzay kirliliğine bağlıdır. Nedeni, görevi biten uyduların ve roket parçalarının Dünya'nın çevresinde dolanmaya devam etmesidir.",
          [KIRLILIK, NEDEN_COP], "problem", puan=10),
        M("b", "Bu problem çözülmezse günlük hayatta başka hangi aksaklıklar yaşanabilir? İki örnek yazınız.", "GPS (navigasyon) sistemleri bozulabilir. Hava durumu tahminleri yapılamayabilir. Telefon ve internet bağlantıları kesilebilir.",
          [A("1. örnek", "gps", "navigasyon", "hava durumu", "telefon", "internet", "iletişim", "haberleşme"), A("2. farklı bir örnek (ikinci bir teknoloji)", "hava durumu", "telefon", "internet", "ulaşım", "güvenlik", "gps")], "tahmin", puan=10)]},
    {"kazanim": "FB.7.1.4", "puan": 20, "svg": Z.dongu({"k1": "?", "k4": "?", "b1": "?", "b3": "?"}), "metin": ["Öğretmen tahtaya yıldızların yaşam sürecini çizmiş ama bazı evreleri soru işaretiyle bırakmış."],
     "maddeler": [
        M("a", "Üst yoldaki ve alt yoldaki soru işaretli yerlere gelmesi gereken evreleri yazınız.", "Üst yol: küçük kütleli yıldız ve beyaz cüce. Alt yol: büyük kütleli yıldız ve süpernova.",
          [KUTLE_K, BEYAZ, KUTLE_B, A("Süpernova", "süpernova")], puan=12),
        M("b", "Nötron yıldızı ya da kara delik hangi olaydan sonra oluşur? Bu olay hangi yıldızlarda görülür?", "Süpernova patlamasından sonra oluşur. Süpernova büyük kütleli yıldızlarda görülür.",
          [A("Süpernova patlaması", "süpernova", "patlama"), KUTLE_B], puan=8)]},
    {"kazanim": "FB.7.1.5", "puan": 15, "metin": ["Bir belgeselde şöyle anlatılıyor: “Gökyüzündeki Güneş, ısı ve ışık yayan bir gaz küresidir. Güneş sistemi, sarmal kolları olan dev bir yapının Avcı kolunda bulunur. Bu dev yapı ise içinde milyarlarca benzerinin bulunduğu, her şeyi içine alan bir bütünün parçasıdır.”"],
     "maddeler": [
        M("a", "Belgeselde Güneş, “sarmal kolları olan dev yapı” ve “her şeyi içine alan bütün” için hangi kavramlar kullanılmalıdır?", "Güneş: yıldız. Sarmal kolları olan dev yapı: Samanyolu galaksisi. Her şeyi içine alan bütün: evren.",
          [A("Güneş: yıldız", "yıldız"), A("Dev yapı: Samanyolu galaksisi", "galaksi", "samanyolu"), A("Bütün: evren", "evren")], puan=9),
        M("b", "Bu üç kavram arasındaki ilişkiyi bir cümleyle açıklayınız.", "Bu kavramlar birbirini kapsar: evren galaksileri, galaksi de yıldızları içine alır.",
          [A("Birbirini kapsar / içine alır", "kapsa", "içine al", "içinde", "içerir")], puan=6)]},
    {"kazanim": "FB.7.2.1", "puan": 15, "metin": ["Bir kargo görevlisi koliyi A noktasında yerden kaldırıyor. A ile B arasında koliyi sallamadan düz yolda taşıyor. B noktasında koliyi masanın üstüne kaldırıyor."],
     "maddeler": [
        M("a", "Görevli A noktasında, A–B arasında ve B noktasında koliye fiziksel anlamda iş yapar mı? Sırasıyla yazınız.", "A noktasında iş yapar. A–B arasında iş yapmaz. B noktasında iş yapar.",
          [SIRA("A yapar, A–B yapmaz, B yapar (sırayla)", ["yapar", "yapılır", "evet", "var"], ["yapmaz", "yapılmaz", "hayır", "yok"], ["yapar", "yapılır", "evet", "var"])], puan=9),
        M("b", "A–B arasında neden iş yapılmadığını açıklayınız.", "Çünkü görevli koliye yukarı doğru kuvvet uygular ama koli yatay hareket eder. Kuvvet ile hareket doğrultusu dik olduğu için iş yapılmaz.",
          [DIK], "cunku", puan=6)]},
    {"kazanim": "FB.7.2.1", "puan": 15, "metin": ["Ali ve Veli aynı kutuyu 4 metre itiyor. Ali 50 N, Veli 100 N kuvvet uyguluyor."],
     "maddeler": [
        M("a", "Hangisi daha çok iş yapar? Nedenini açıklayınız.", "Veli daha çok iş yapar, çünkü yol aynı ama Veli daha büyük kuvvet uygulamıştır. İş, kuvvetle doğru orantılıdır.",
          [A("Veli", "veli"), A("Kuvvet büyük → iş fazla", "kuvvet", "doğru orantı")], "cunku", puan=8),
        M("b", "Fiziksel anlamda yapılan işin bağlı olduğu iki etkeni yazınız.", "Uygulanan kuvvet ve cismin kuvvet doğrultusunda aldığı yol.",
          [A("Kuvvet", "kuvvet"), A("Kuvvet doğrultusunda alınan yol", "yol", "mesafe", "yer değiştirme")], puan=7)]},
    {"kazanim": "FB.7.2.2", "puan": 15, "metin": ["Ağırlıkları eşit olan K ve L cisimlerinden K yerden h, L ise 2h yükseklikte hareketsiz tutuluyor."],
     "maddeler": [
        M("a", "Cisimlerin çekim potansiyel enerjilerini karşılaştırınız. Nedenini yazınız.", "L'nin çekim potansiyel enerjisi K'den fazladır, çünkü ağırlıkları eşit ama L daha yüksektedir.",
          [A("L'nin enerjisi daha fazla", "l'nin", "l daha", "l cism"), A("Neden: L daha yüksekte (ağırlıklar eşit)", "yüksek")], "karsilastir", puan=8),
        M("b", "K ve L cisimlerinin kinetik enerjileri hakkında ne söylenebilir? Açıklayınız.", "İkisinin de kinetik enerjisi yoktur, çünkü ikisi de hareketsiz tutuluyor; kinetik enerji için hareket gerekir.",
          [A("İkisinde de kinetik enerji yok", "yok", "sıfır"), A("Hareket etmiyorlar", "hareketsiz", "hareket etm", "hareket gerek", "duruyor")], "cunku", puan=7)]}])

Y.yaz()
