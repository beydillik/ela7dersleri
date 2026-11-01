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
    baslik="1. Dönem 1. Yazılı", ders="Fen Bilimleri", senaryo="Senaryo 4", sure=40, tarih="2026-11-03",
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
def KH(kazanim, tur, soru, kuark, dogruSik, yanlis1, yanlis2, ipucu, aciklama, once, ornek, sonra, k, havuz):
    """tur: eksik (Kuark'ın cevabı doğru ama yarım) | yanilgi (Hatırla kartlarındaki klasik hatalar; yalnız bunlar).
    Ela önce eksiği/hatayı seçer, sonra tam cevabın boşluğunu (once ___ sonra) kendisi yazar: son yaptığı şey doğru cevap olur."""
    Y.kuark(kazanim=kazanim, tur=tur, soru=soru, kuark=kuark, secenekler=[dogruSik, yanlis1, yanlis2], dogru=0, ipucu=ipucu, aciklama=aciklama,
            dogruCevap=f"{once} {ornek} {sonra}".replace(" .", ".").replace(" ;", ";").strip(), tamamla={"once": once, "ornek": ornek, "sonra": sonra, "k": k, "havuz": havuz})

# Eksik cevap (8): Ela'nın gerçek hatası, bilgiyi biliyor ama yarım yazıyor
KH("FB.7.2.1", "eksik", "Sandığı iterek hareket ettiren kişi iş yapmış mıdır? Açıklayınız.", "Evet.",
   "Eksik: “çünkü” yok; kuvvet ile hareketin aynı doğrultuda olduğu yazılmalı.", "Yanlış: sandığı iten iş yapmaz.", "Tam, eksik yok.",
   "“Açıklayınız” ne istiyor?", "Gerekçesiz cevap yazılıda tam puan almaz. (s. 61)",
   "Evet, çünkü kuvvet ile hareket", "aynı doğrultuda", ".", ["aynı doğrultu", "aynı yön", "doğrultusunda"], ["dik", "zıt yönde"])
KH("FB.7.1.4", "eksik", "Yıldızların yaşam süresini ne belirler? Açıklayınız.", "Kütlesi.",
   "Eksik: nasıl belirlediği yok; kütle büyükse yaşam kısa olur.", "Yanlış: yaşam süresini renk belirler.", "Tam, eksik yok.",
   "Kütle büyüyünce yaşam ne olur?", "Kütle ne kadar büyükse yaşam o kadar kısa olur. (s. 42)",
   "Kütlesi. Kütle büyükse yaşam", "kısa", "olur.", ["kısa"], ["uzun", "sonsuz"])
KH("FB.7.1.4", "eksik", "Kırmızı süperdev evresinden sonra yıldızın yaşamı nasıl sona erer?", "Patlar.",
   "Eksik: patlamanın adı (süpernova) ve geriye ne kaldığı yazılmamış.", "Yanlış: süperdev beyaz cüce olur.", "Tam, eksik yok.",
   "Patlamanın bir adı var.", "Süperdev süpernova ile patlar; geriye nötron yıldızı ya da kara delik kalır. (s. 42)",
   "Süpernova ile patlar; geriye nötron yıldızı ya da", "kara delik", "kalır.", ["kara delik", "karadelik"], ["beyaz cüce", "bulutsu"])
KH("FB.7.1.5", "eksik", "Evren, galaksi ve yıldızı büyükten küçüğe sıralayınız.", "Evren en büyüktür.",
   "Eksik: yalnız en büyüğü yazılmış; tam sıra yazılmalı.", "Yanlış: en büyük galaksidir.", "Tam, eksik yok.",
   "“Sıralayınız” üçünü de istiyor.", "Evren galaksileri, galaksi yıldızları içine alır. (s. 46, 48)",
   "Evren →", "Galaksi", "→ Yıldız", ["galaksi", "gök ada", "gökada"], ["Dünya", "Güneş sistemi"])
KH("FB.7.1.5", "eksik", "Galaksi nedir?", "Çok büyük bir yapıdır.",
   "Eksik: neyden oluştuğu yazılmamış (yıldız, gezegen, bulutsu…).", "Yanlış: galaksi tek bir yıldızdır.", "Tam, eksik yok.",
   "Galaksinin içinde neler var?", "Galaksi; yıldız, gezegen, bulutsu gibi gök cisimlerinden oluşur. (s. 48)",
   "Yıldız, gezegen, bulutsu gibi", "gök cisimlerinden", "oluşan yapıdır.", ["gök cisim", "cisim"], ["sulardan", "taşlardan"])
KH("FB.7.2.2", "eksik", "Kinetik enerji hangi iki özelliğe bağlıdır?", "Kütleye bağlıdır.",
   "Eksik: ikinci özellik (hız) yazılmamış.", "Yanlış: kinetik enerji kütleye bağlı değildir.", "Tam, eksik yok.",
   "Soru “iki özellik” diyor.", "Kinetik enerji kütle ve hızla doğru orantılıdır. (s. 67)",
   "Kütleye ve", "hıza", "bağlıdır.", ["hız", "sürat"], ["yüksekliğe", "renge"])
KH("FB.7.1.3", "eksik", "Uzay kirliliği problemini nedeni ve sonucuyla açıklayınız.", "Uzay kirliliği.",
   "Eksik: nedeni ve sonucu yazılmamış.", "Yanlış: bu hava kirliliğidir.", "Tam, eksik yok.",
   "Soru üç şey istiyor: problem, neden, sonuç.", "Neden: eski uydular yörüngede kalır; sonuç: araçlara çarpar. (s. 30, 32)",
   "Uzay kirliliği. Nedeni: eski uydular yörüngede kalır. Sonucu: uzay araçlarına", "çarpar", ".", ["çarp", "zarar"], ["yağar", "ısınır"])
KH("FB.7.1.3", "eksik", "Uzay kirliliğine bir çözüm önerisi yazınız ve nedenini açıklayınız.", "Çöpleri toplamak.",
   "Eksik: “çünkü” ile neden işe yarayacağı yazılmamış.", "Yanlış: çöp toplamak çözüm değildir.", "Tam, eksik yok.",
   "Öneri + çünkü.", "Çözüm önerisinde gerekçe de puan getirir. (s. 32)",
   "Çöpleri toplamak, çünkü çarpışma riski", "azalır", ".", ["azal", "düş", "önlen"], ["artar", "değişmez"])
# Yanılgı (4): yalnız Hatırla kartlarının "sık yapılan hatalar"ında zaten geçen klasikler
KH("FB.7.2.1", "yanilgi", "Halteri başının üzerinde sabit tutan halterci iş yapar mı?", "Evet, çünkü çok yoruluyor.",
   "Yanlış: halter yer değiştirmiyor; yorulmak iş demek değil.", "Yanlış: halterci hiç kuvvet uygulamıyor.", "Doğru, hata yok.",
   "Halter hareket ediyor mu?", "Kuvvet var ama yer değiştirme yok: iş yok. (s. 62)",
   "Hayır, iş yapmaz, çünkü halter", "hareket etmiyor", ".", ["hareket etm", "sabit", "yer değiştirm", "duruyor", "hareketsiz"], ["yukarı çıkıyor", "çok ağır"])
KH("FB.7.2.1", "yanilgi", "Poşetleri elinde taşıyarak düz yolda yürüyen kişi poşetlere iş yapar mı?", "Evet, çünkü poşetler onunla birlikte yer değiştiriyor.",
   "Yanlış: kuvvet yukarı, hareket yatay; doğrultular dik olduğu için iş yok.", "Yanlış: poşetler hiç yer değiştirmiyor.", "Doğru, hata yok.",
   "Kuvvetin yönüne ve hareketin yönüne ayrı ayrı bak.", "Kuvvet ile hareket aynı doğrultuda değilse iş yok. (s. 62)",
   "Hayır, çünkü kuvvet yukarı, hareket", "yatay", "; doğrultular dik.", ["yatay", "ileri", "düz"], ["yukarı", "aşağı"])
KH("FB.7.1.4", "yanilgi", "Güneş'in ömrünün sonunda ne olacak?", "Süpernova olarak patlayıp kara deliğe dönüşecek.",
   "Yanlış: Güneş küçük kütleli; beyaz cüce olacak.", "Yanlış: Güneş nötron yıldızı olacak.", "Doğru, hata yok.",
   "Güneş küçük kütleli mi, büyük kütleli mi?", "Süpernova ve kara delik büyük kütleli yıldızlara aittir. (s. 42)",
   "Güneş küçük kütleli olduğu için", "beyaz cüce", "olacak.", ["beyaz cüce"], ["kara delik", "süpernova"])
KH("FB.7.2.2", "yanilgi", "Dalda duran elmanın enerjisi nedir?", "Kinetik enerji, çünkü yüksekte duruyor.",
   "Yanlış: yüksekte duran cismin çekim potansiyel enerjisi var; kinetik için hareket gerekir.", "Yanlış: elmanın hiç enerjisi yoktur.", "Doğru, hata yok.",
   "Elma hareket ediyor mu?", "Kinetik = hareket; çekim potansiyel = yükseklik. (s. 66, 68)",
   "Dalda duran elmanın", "çekim potansiyel", "enerjisi vardır.", ["potansiyel"], ["kinetik", "ışık"])

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


# =====================================================================
# BASAMAKLAR (MEB soruları): 1 tam cevabı tanı → 2 parça parça kur → 3 kalıpla yaz → 4 sınavdaki hâli.
# kisaCevap: puanın büyük kısmını (%70+) getiren en kısa cevap; Ela'nın hedefi bu (Kemal'in kararı, 1 Kasım 2026).
# Parça: bas (hazır cümle başı; anahtar köklerini İÇERMEZ), ornek, k (kabul kökleri) | hepsi | sira | serbest, havuz (2 çeldirici).
# =====================================================================
def B(kisa, dogru, eksik, yanlis, ipucu, aciklama, *parcalar):
    return {"kisaCevap": kisa, "basamak": {"sec": {"secenekler": [dogru, eksik, yanlis], "dogru": 0, "ipucu": ipucu, "aciklama": aciklama}, "parcalar": list(parcalar)}}
def P(bas, ornek, havuz, k=None, hepsi=None, sira=None, serbest=False):
    d = {"bas": bas, "ornek": ornek, "havuz": havuz}
    if k: d["k"] = k
    if hepsi: d["hepsi"] = hepsi
    if sira: d["sira"] = sira
    if serbest: d["serbest"] = True
    return d

BASAMAK = {
 ("m3", "a"): B("Uzay kirliliği. Nedeni: eski uydular ve roket parçaları yörüngede kalır. Sonucu: uzay araçlarına çarpar.",
    "Uzay kirliliği. Nedeni: eski uydular ve roket parçaları yörüngede kalır. Sonucu: uzay araçlarına çarpar.",
    "Uzay kirliliği.", "Hava kirliliği. Fabrikaların dumanı atmosferi kirletir.",
    "Soru üç şey istiyor: problem, neden, sonuç.", "Tam puan için adı, nedeni ve sonucu birlikte yazılır. (s. 30, 32)",
    P("Problem:", "uzay kirliliği", ["hava kirliliği", "ışık kirliliği"], k=["uzay kirlili", "uzay çöp", "uzay copu"]),
    P("Nedeni:", "eski uydular yörüngede kalır", ["fabrikalar duman çıkarır", "yıldızlar patlar"], k=["eski uydu", "görevi", "parça", "kalır", "kalıyor", "bitmiş", "biten"]),
    P("Sonucu:", "uzay araçlarına çarpar", ["yağmur yağmaz", "Güneş söner"], k=["çarp", "zarar", "hasar"])),
 ("m3", "b"): B("Çöpler uydulara çarpar; GPS ve televizyon bozulur.",
    "Çöpler uydulara çarpar; GPS ve televizyon bozulur.", "Uzay yolculukları zorlaşır.", "Yağmurlar durur, hava kirlenir.",
    "Günlük hayatta kullandığın bir teknoloji yaz.", "Uydular zarar görürse GPS, TV, telefon aksar. (s. 32)",
    P("Çöpler neye çarpar?", "çalışan uydulara", ["uçaklara", "dağlara"], k=["uydu"]),
    P("Bozulabilecek bir teknoloji:", "GPS / televizyon", ["buzdolabı", "bisiklet"], k=["televizyon", "tv", "gps", "navigasyon", "telefon", "internet", "hava durumu", "haberleşme", "iletişim", "yayın"])),
 ("m3", "c"): B("2. yöntem, çünkü uydular çok yüksekte; atmosfere çekmek zor.",
    "2. yöntem, çünkü uydular çok yüksekte; atmosfere çekmek zor.", "2. yöntem.", "Hiçbiri; uzaya hiç uydu gönderilmemeli.",
    "Bir yöntem seç ve “çünkü” ile nedenini yaz.", "Hangi yöntemi seçtiğin değil, gerekçe yazman puan getirir.",
    P("Seçtiğim yöntem:", "2. yöntem (ağla toplamak)", ["hiçbiri", "uydu göndermemek"], k=["1", "2", "birinci", "ikinci", "ağ", "atmosfer", "mıknatıs"]),
    P("Nedeni:", "uydular yüksekte, atmosfere çekmek zor", ["bilmiyorum", "çünkü"], serbest=True)),
 ("m4", "a"): B("Bulutsu. Büyük kütleli olmalı.",
    "Bulutsu. Büyük kütleli olmalı.", "Bulutsu.", "Kara delik. Küçük kütleli olmalı.",
    "Soru iki şey soruyor: doğum yeri ve kütle.", "Yıldızlar bulutsuda doğar; süpernova büyük kütleli yıldızlarda olur. (s. 41–42)",
    P("Doğum yeri:", "bulutsu", ["kara delik", "beyaz cüce"], k=["bulutsu", "nebula"]),
    P("Süpernova için kütle:", "büyük", ["küçük", "orta"], k=["büyük"])),
 ("m4", "b"): B("Hayır, çünkü Güneş küçük kütleli; beyaz cüce olur.",
    "Hayır, çünkü Güneş küçük kütleli; beyaz cüce olur.", "Hayır.", "Evet, çünkü Güneş çok büyük bir yıldızdır.",
    "Evet/hayır tek başına puan getirmez.", "Güneş küçük kütleli, sonu beyaz cüce; kara delik büyük kütleli yıldızdan olur. (s. 42)",
    P("Cevap:", "hayır", ["evet", "belki"], k=["hayır", "beklenemez", "olmaz", "dönüşmez"]),
    P("Güneş'in kütlesi:", "küçük", ["büyük", "çok büyük"], k=["küçük"]),
    P("Güneş'in sonu:", "beyaz cüce", ["kara delik", "süpernova"], k=["beyaz cüce"])),
 ("m5", "a"): B("X: bulutsu, Y: kara delik, Z: küçük kütleli yıldız",
    "X: bulutsu, Y: kara delik, Z: küçük kütleli yıldız", "X: bulutsu, Y: süpernova, Z: beyaz cüce", "X: galaksi, Y: kara delik, Z: büyük kütleli yıldız",
    "Her cismin anlattığı son cümleye dikkat et.", "X gaz-toz bulutu, Y ışığın kaçamadığı merkez, Z beyaz cüce olacak yıldız. (s. 41–42)",
    P("X:", "bulutsu", ["galaksi", "süpernova"], k=["bulutsu", "nebula"]),
    P("Y:", "kara delik", ["süpernova", "nötron yıldızı"], k=["kara delik", "karadelik"]),
    P("Z:", "küçük kütleli yıldız", ["büyük kütleli yıldız", "kırmızı süperdev"], k=["küçük kütle", "güneş"])),
 ("m5", "b"): B("Başlangıç kütlesi: Y büyük kütleli → süpernova; Z küçük kütleli → beyaz cüce.",
    "Başlangıç kütlesi: Y büyük kütleli → süpernova; Z küçük kütleli → beyaz cüce.", "Başlangıç kütlesi.", "Renkleri farklı olduğu için.",
    "Yıldızın yaşamını belirleyen özellik neydi?", "Yaşam sürecini başlangıç kütlesi belirler. (s. 42)",
    P("Belirleyen özellik:", "başlangıç kütlesi", ["renk", "uzaklık"], k=["kütle"]),
    P("Y'nin sonu:", "süpernova → kara delik", ["beyaz cüce", "kırmızı dev"], k=["süpernova", "nötron", "kara delik"]),
    P("Z'nin sonu:", "beyaz cüce", ["kara delik", "süpernova"], k=["beyaz cüce"])),
 ("m6", "a"): B("Yıldız, galaksi, evren. Evren → Galaksi → Yıldız.",
    "Yıldız, galaksi, evren. Evren → Galaksi → Yıldız.", "Galaksi → Evren → Yıldız", "Güneş sistemi → Dünya → Ay",
    "En büyük kavram her şeyi içine alır.", "Evren galaksileri, galaksi yıldızları içine alır. (s. 46, 48)",
    P("Kavramlar:", "yıldız, galaksi, evren", ["Dünya, Ay", "gezegen, uydu"], hepsi=[["yıldız"], ["galaksi", "gök ada"], ["evren"]]),
    P("Büyükten küçüğe:", "evren → galaksi → yıldız", ["galaksi → evren → yıldız", "yıldız → galaksi → evren"], sira=[["evren"], ["galaksi", "gök ada"], ["yıldız"]])),
 ("m7", "a"): B("Sandığı iten. Poşette kuvvet yukarı, hareket yatay; iş yok.",
    "Sandığı iten. Poşette kuvvet yukarı, hareket yatay; iş yok.", "Sandığı iten kişi.", "İkisi de iş yapar, ikisi de yoruluyor.",
    "Kuvvetin ve hareketin yönüne bak.", "Poşette kuvvet ile hareket diktir, iş yapılmaz. (s. 62)",
    P("İş yapan:", "sandığı iten", ["poşet taşıyan", "ikisi de"], k=["sandı", "iten", "görsel 1", "birinci"]),
    P("Poşet taşıyanın kuvveti ve hareketi:", "kuvvet yukarı, hareket yatay (dik)", ["ikisi de ileri", "kuvvet çok büyük"], k=["dik", "yatay", "farklı doğrultu", "farklı yön"])),
 ("m7", "b"): B("Aynı doğrultuda olmalı; cisim yer değiştirmeli.",
    "Aynı doğrultuda olmalı; cisim yer değiştirmeli.", "Kuvvet büyük olmalı.", "Birbirine dik olmalı.",
    "İki koşulu hatırla.", "Cisim, uygulanan kuvvetle aynı doğrultuda yer değiştirmeli. (s. 61)",
    P("Kuvvet ile cismin yolu:", "aynı doğrultuda olmalı", ["dik olmalı", "zıt olmalı"], k=["aynı doğrultu", "aynı yön", "doğrultusunda", "paralel"]),
    P("Cisim ne yapmalı?", "yer değiştirmeli", ["durmalı", "ısınmalı"], k=["yer değiştir", "hareket", "yol al"])),
 ("m8", "a"): B("Evet. Kuvvet de halter de yukarı (aynı doğrultu).",
    "Evet. Kuvvet de halter de yukarı (aynı doğrultu).", "Evet.", "Hayır, çünkü halter çok ağır.",
    "Evet/hayır + kuvvet ve hareketin yönü.", "Kuvvet yukarı, halter de yukarı hareket ediyor: iş var. (s. 61)",
    P("Cevap:", "evet, iş var", ["hayır", "bilinmez"], k=["evet", "yapılmış", "yapmış", "yapar", "var"]),
    P("Kuvvet ve halter hangi yöne?", "ikisi de yukarı (aynı doğrultu)", ["ikisi de aşağı", "farklı yönlere"], k=["aynı doğrultu", "aynı yön", "yukarı"])),
 ("m8", "b"): B("Hayır. Halter hareket etmiyor.",
    "Hayır. Halter hareket etmiyor.", "Hayır.", "Evet, çünkü çok yoruluyor.",
    "Halter yer değiştiriyor mu?", "Kuvvet var ama hareket yok: iş yapılmaz. (s. 62)",
    P("Cevap:", "hayır, iş yok", ["evet", "biraz"], k=["hayır", "yapılmamış", "yapmamış", "yapmaz", "yok", "sıfır"]),
    P("Halter ne durumda?", "hareket etmiyor (sabit)", ["yukarı çıkıyor", "düşüyor"], k=["hareket etm", "sabit", "duruyor", "hareketsiz", "yer değiştirm"])),
 ("m9", "a"): B("Çekim potansiyel enerjisi; kütle ve yükseklik.",
    "Çekim potansiyel enerjisi; kütle ve yükseklik.", "Potansiyel enerji.", "Kinetik enerji; hız ve kütle.",
    "Elma duruyor ama yüksekte.", "Yüksekte duran cismin çekim potansiyel enerjisi var; kütle ve yüksekliğe bağlı. (s. 68)",
    P("Enerjinin adı:", "çekim potansiyel enerjisi", ["kinetik enerji", "ısı enerjisi"], k=["potansiyel"]),
    P("Bağlı olduğu iki şey:", "kütle ve yükseklik", ["hız ve renk", "sıcaklık"], hepsi=[["kütle", "ağırlı"], ["yüksek"]])),
 ("m9", "b"): B("Kinetik enerji.",
    "Kinetik enerji.", "Potansiyel enerji.", "Esneklik potansiyel enerjisi.",
    "Elma artık hareket ediyor.", "Hareketten dolayı sahip olunan enerji kinetik enerjidir. (s. 66)",
    P("Enerjinin adı:", "kinetik enerji", ["potansiyel enerji", "ışık enerjisi"], k=["kinetik", "hareket enerjisi"])),
 ("m9", "c"): B("Kinetik için hareket, potansiyel için yükseklik gerekir.",
    "Kinetik için hareket, potansiyel için yükseklik gerekir.", "Kinetik enerji hareket enerjisidir.", "İkisi de yüksekliğe bağlıdır.",
    "Karşılaştırmada iki tarafı da yaz.", "Kinetik: hareket; çekim potansiyel: yükseklik. (s. 66, 68)",
    P("Kinetik için gereken:", "hareket", ["yükseklik", "renk"], k=["hareket", "hız", "sürat"]),
    P("Potansiyel için gereken:", "yükseklik", ["hız", "ses"], k=["yüksek", "konum"])),
}

# Soru kelimesi → cevap kalıbı: soru metnindeki tetikleyici ifadeler vurgulanır, altında tek satır kalıp notu (Kemal'in kararı: kalıplar ayrı sayfada değil, sorunun içinde)
TETIK = {
 ("m3", "a"): (["nedenlerini ve sonuçlarını"], "Problem · Neden · Sonuç: üç parça yaz."),
 ("m3", "b"): (["Tahmininizi"], "Tahmin + gerekçe: “… bozulabilir, çünkü …”"),
 ("m3", "c"): (["hangisi daha uygulanabilir", "neden daha iyi olduğunu"], "Seçim + çünkü: “… yöntem, çünkü …”"),
 ("m4", "a"): (["ne ad verilir", "nasıl bir kütleye"], "İki soru var: adı yaz + kütleyi yaz."),
 ("m4", "b"): (["beklenebilir mi", "açıklayınız"], "Evet/Hayır + çünkü."),
 ("m5", "a"): (["bilimsel adlarını"], "Üç ad yaz: X: … Y: … Z: …"),
 ("m5", "b"): (["neden birbirinden farklı", "hangi temel özelliğiyle"], "Özellik + iki tarafın sonu: “Y … , Z ise …”"),
 ("m6", "a"): (["İsimlerini yazınız", "sıralayınız"], "Önce adlar, sonra sıra: A → B → C"),
 ("m7", "a"): (["hangisi fiziksel anlamda iş yapmıştır"], "Kişiyi yaz + çünkü (kuvvetin ve hareketin yönü)."),
 ("m7", "b"): (["nasıl bir ilişki"], "İlişkiyi yaz: “… doğrultuda olmalı”."),
 ("m8", "a"): (["iş yapılmış mıdır", "açıklayınız"], "Evet/Hayır + çünkü."),
 ("m8", "b"): (["iş yapılmış mıdır", "açıklayınız"], "Evet/Hayır + çünkü."),
 ("m9", "a"): (["enerji çeşidi nedir", "hangi özelliklerine bağlıdır"], "Enerjinin adı + bağlı olduğu iki şey."),
 ("m9", "b"): (["enerji çeşidi nedir"], "Yalnız enerjinin adı yeter."),
 ("m9", "c"): (["karşılaştırarak"], "Karşılaştır: “Kinetik için … , potansiyel için …”"),
}
for q in Y.d["mebSorular"]:
    for m in q["maddeler"]:
        t = TETIK.get((q["id"], m["harf"]))
        if t: m["tetik"], m["kalipNot"] = t
        b = BASAMAK.get((q["id"], m["harf"]))
        if b:
            m.update(b); m.pop("iskele", None)   # basamaklı maddede ısınma yerine basamak 1–2


# =====================================================================
# BENZER SORULAR (Konu Tekrarı): basamaksız, doğrudan sınavdaki gibi yazma + ipucu (cümle başları, kelime havuzu, "Anladım").
# Her maddede kisaCevap, tetik, kalipNot ve parçalar (basamak.sec YOK → motor doğrudan 4. basamaktan başlatır). (Kemal, 1 Kasım 2026)
# =====================================================================
def IK(kisa, tetik, notu, *parcalar): return {"kisaCevap": kisa, "tetik": tetik, "kalipNot": notu, "basamak": {"parcalar": list(parcalar)}}
PROB = P("Problem:", "uzay kirliliği", ["hava kirliliği", "ışık kirliliği"], k=["uzay kirlili", "uzay çöp", "uzay copu"])
EVET = P("Cevap:", "evet, iş var", ["hayır", "bilinmez"], k=["evet", "yapılmış", "yapmış", "yapar", "var"])
HAYIR = P("Cevap:", "hayır, iş yok", ["evet", "biraz"], k=["hayır", "yapılmamış", "yapmamış", "yapmaz", "yok", "sıfır"])
DURUYOR = ["hareket etm", "yer değiştirm", "kıpırda", "duruyor", "hareketsiz", "sabit"]
IKIZ = {
 ("m3i1", "a"): IK("Uzay kirliliği. Nedeni: eski uydular yörüngede kalır.", ["hangi probleme örnektir", "bir nedenini"], "Problem + neden.",
    PROB, P("Nedeni:", "eski uydular yörüngede kalır", ["fabrikalar duman çıkarır", "yıldızlar patlar"], k=["eski uydu", "görevi", "parça", "kalır", "kalıyor", "bitmiş", "biten"])),
 ("m3i1", "b"): IK("Uydu zarar görür; telefon ve TV kesilir.", ["Tahmininizi"], "Tahmin: “… kesilebilir, çünkü …”",
    P("Neye çarpar?", "haberleşme uydusuna", ["Dünya'ya", "Ay'a"], k=["uydu"]),
    P("Kesilebilecek teknoloji:", "telefon / televizyon", ["buzdolabı", "bisiklet"], k=["televizyon", "tv", "telefon", "internet", "gps", "yayın", "haberleşme", "iletişim"])),
 ("m3i1", "c"): IK("Eski uyduları yörüngeden çıkarmak; çarpışma riski azalır.", ["bir çözüm önerisi", "neden işe yarayacağını"], "Öneri + çünkü.",
    P("Önerim:", "eski uyduları yörüngeden çıkarmak", ["daha çok uydu göndermek", "uzaya hiç gitmemek"], k=["yörüngeden çıkar", "topla", "yakala", "getir", "atmosfer", "temizle"]),
    P("Bunun sonucu:", "çarpışma azalır", ["çarpışma artar", "hiçbir şey olmaz"], k=["azal", "düş", "önlen"])),
 ("m3i2", "a"): IK("Uzay kirliliği. Sonucu: araçlara çarpar.", ["hangi problemi", "bir sonucunu"], "Problem + sonuç.",
    PROB, P("Sonucu:", "uzay araçlarına çarpar", ["yağmur yağmaz", "Güneş söner"], k=["çarp", "zarar", "hasar"])),
 ("m3i2", "b"): IK("2. proje, çünkü yeni çöp oluşmaz.", ["hangi proje", "Nedenini açıklayınız"], "Seçim + çünkü.",
    P("Seçtiğim proje:", "2. proje", ["hiçbiri", "ikisi de değil"], k=["1", "2", "birinci", "ikinci"]),
    P("Nedeni:", "yeni çöp oluşmaz", ["bilmiyorum", "çünkü"], serbest=True)),
 ("m3i2", "c"): IK("Çok hızlı hareket eder; küçük parça bile zarar verir.", ["Bunun nedenini açıklayınız"], "Neden + sonuç: “… hızlı, bu yüzden …”",
    P("Çöpler nasıl hareket eder?", "çok hızlı", ["çok yavaş", "hiç"], k=["hız", "sürat"]),
    P("Bir araca değerse:", "zarar verir", ["hiçbir şey olmaz", "yavaşlar"], k=["zarar", "hasar"])),
 ("m4i1", "a"): IK("A yıldızı, çünkü büyük kütleli.", ["Hangi yıldız", "Nedenini yazınız"], "Yıldız + çünkü.",
    P("Yıldız:", "A yıldızı", ["B yıldızı", "ikisi de"], k=["a yıldızı", "a'"]),
    P("Çünkü kütlesi:", "büyük", ["küçük", "sıfır"], k=["büyük"])),
 ("m4i1", "b"): IK("Beyaz cüce; önce kırmızı dev.", ["son evresi ne olur", "hangi evreden geçer"], "İki şey: son evre + ondan önceki evre.",
    P("Son evre:", "beyaz cüce", ["kara delik", "süpernova"], k=["beyaz cüce"]),
    P("Önceki evre:", "kırmızı dev", ["kırmızı süperdev", "bulutsu"], k=["kırmızı dev"])),
 ("m4i1", "c"): IK("A yıldızı; kütle büyükse yaşam kısa.", ["daha kısa sürer", "Açıklayınız"], "Yıldız + çünkü.",
    P("Yıldız:", "A yıldızı", ["B yıldızı", "ikisi de"], k=["a yıldızı", "a'"]),
    P("Kural:", "kütle büyükse yaşam kısa", ["kütle büyükse yaşam uzun", "kütle önemsiz"], k=["kısa"])),
 ("m4i2", "a"): IK("Bulutsu → büyük kütleli yıldız → süperdev → süpernova → kara delik", ["sıralayınız"], "Sırala: A → B → C …",
    P("İlk iki evre:", "bulutsu → büyük kütleli yıldız", ["kırmızı dev → beyaz cüce", "büyük kütleli yıldız → bulutsu"], sira=[["bulutsu"], ["büyük kütle"]]),
    P("Son üç evre:", "süperdev → süpernova → kara delik", ["kırmızı dev → beyaz cüce → bulutsu", "süpernova → süperdev → kara delik"], sira=[["süperdev"], ["süpernova"], ["kara delik", "karadelik"]])),
 ("m4i2", "b"): IK("Küçük kütleli olurdu.", ["başlangıç kütlesi hakkında"], "Kütle: küçük mü, büyük mü?",
    P("Kütlesi:", "küçük", ["büyük", "çok büyük"], k=["küçük"])),
 ("m5i1", "a"): IK("K: Ön yıldız. L: Süpernova. M: Beyaz cüce.", ["bilimsel adlarını"], "Üç ad yaz.",
    P("K:", "ön yıldız", ["bulutsu", "kara delik"], k=["ön yıldız", "önyıldız"]), P("L:", "süpernova", ["beyaz cüce", "kırmızı dev"], k=["süpernova"]),
    P("M:", "beyaz cüce", ["kara delik", "nötron yıldızı"], k=["beyaz cüce"])),
 ("m5i1", "b"): IK("L büyük kütleli yıldızdan, M küçük kütleli yıldızdan.", ["karşılaştırınız"], "Karşılaştır: “L … , M ise …”",
    P("L'nin yıldızı:", "büyük kütleli", ["küçük kütleli", "Güneş"], k=["büyük"]), P("M'nin yıldızı:", "küçük kütleli", ["büyük kütleli", "kara delik"], k=["küçük"])),
 ("m5i2", "a"): IK("N: kırmızı süperdev, P: kırmızı dev", ["hangi evrededir"], "İki ad yaz.",
    P("N:", "kırmızı süperdev", ["kırmızı dev", "beyaz cüce"], k=["süperdev"]), P("P:", "kırmızı dev", ["kırmızı süperdev", "süpernova"], k=["kırmızı dev"])),
 ("m5i2", "b"): IK("N süpernova → kara delik; P beyaz cüce. Neden: başlangıç kütlesi.", ["nasıl sona erecek", "farkın nedeni"], "İki sonu yaz + nedeni.",
    P("N'nin sonu:", "süpernova", ["beyaz cüce", "bulutsu"], k=["süpernova", "nötron", "kara delik"]), P("P'nin sonu:", "beyaz cüce", ["kara delik", "süpernova"], k=["beyaz cüce"]),
    P("Farkın nedeni:", "başlangıç kütlesi", ["renk", "uzaklık"], k=["kütle"])),
 ("m6i1", "a"): IK("Evren → Samanyolu → Güneş sistemi → Dünya", ["büyükten küçüğe"], "Sırala: A → B → C → D",
    P("En büyük iki:", "evren → Samanyolu", ["Dünya → Güneş sistemi", "Samanyolu → evren"], sira=[["evren"], ["samanyolu", "galaksi"]]),
    P("En küçük iki:", "Güneş sistemi → Dünya", ["Dünya → Güneş sistemi", "evren → Dünya"], sira=[["güneş sistemi", "sistem"], ["dünya"]])),
 ("m6i1", "b"): IK("Galaksi: yıldız ve gezegenlerden oluşan yapı. Evren: hepsini içine alan boşluk.", ["kendi cümlelerinizle tanımlayınız"], "İki tanım: “Galaksi … , evren …”",
    P("Galaksi neyden oluşur?", "yıldız, gezegen, bulutsu", ["sudan", "taşlardan"], k=["yıldız", "gezegen", "bulutsu", "gök cisim"]),
    P("Evren nedir?", "hepsini içine alan boşluk", ["tek bir yıldız", "Güneş sistemi"], k=["içine alan", "kapsayan", "tüm", "bütün", "hepsini"])),
 ("m6i2", "a"): IK("Yıldız ve galaksi (Samanyolu).", ["kavramlar nelerdir"], "İki kavram adı.",
    P("Parlak noktalar:", "yıldız", ["gezegen", "uydu"], k=["yıldız"]), P("Sarmal yapı:", "galaksi (Samanyolu)", ["evren", "Güneş sistemi"], k=["galaksi", "samanyolu", "gök ada"])),
 ("m6i2", "b"): IK("Andromeda.", ["Komşu yapının adı"], "Yalnız adı yeter.", P("Adı:", "Andromeda", ["Samanyolu", "Güneş"], k=["andromeda"])),
 ("m6i2", "c"): IK("Evren: bütün gök cisimlerini içine alan boşluk.", ["hepsini içine alan kavram", "Tanımını yazınız"], "Ad + tanım.",
    P("Kavram:", "evren", ["galaksi", "yıldız"], k=["evren"]), P("Tanımı:", "her şeyi içine alan boşluk", ["en büyük yıldız", "bir gezegen"], k=["içine alan", "kapsayan", "boşluk"])),
 ("m7i1", "a"): IK("I ve IV.", ["Hangi durumlarda"], "Durum numaralarını yaz.",
    P("İş yapılan durumlar:", "I ve IV", ["II ve III", "yalnız II"], hepsi=[["i ve", "i,", "i."], ["iv"]])),
 ("m7i1", "b"): IK("II: dolap hareket etmiyor. III: kuvvet yukarı, hareket yatay.", ["neden iş yapılmadığını"], "İkisini ayrı yaz: “II … , III …”",
    P("II'de dolap:", "hareket etmiyor", ["hızla ilerliyor", "yukarı çıkıyor"], k=DURUYOR),
    P("III'te kuvvet ve hareket:", "kuvvet yukarı, hareket yatay", ["ikisi de ileri", "ikisi de yukarı"], k=["yatay", "dik", "farklı"])),
 ("m7i2", "a"): IK("2. durum, çünkü yol daha fazla.", ["Hangi durumda", "Nedenini açıklayınız"], "Durum + çünkü.",
    P("Durum:", "2. durum", ["1. durum", "ikisi eşit"], k=["2", "ikinci", "6"]), P("Çünkü:", "yol daha fazla", ["daha az", "aynı"], k=["fazla", "uzun", "çok"])),
 ("m7i2", "b"): IK("İş artar, çünkü iş kuvvetle doğru orantılı.", ["nasıl değişirdi"], "Artar mı, azalır mı + çünkü.",
    P("İş:", "artar", ["azalır", "değişmez"], k=["artar", "artardı", "fazla", "çoğal"]), P("Çünkü iş neye bağlı?", "kuvvete", ["renge", "zamana"], k=["kuvvet"])),
 ("m8i1", "a"): IK("Evet. Kuvvet de kutu da yukarı (aynı doğrultu).", ["iş yapmış mıdır", "Açıklayınız"], "Evet/Hayır + çünkü.",
    EVET, P("Kuvvet ve kutu hangi yöne?", "ikisi de yukarı (aynı doğrultu)", ["ikisi de aşağı", "farklı yönlere"], k=["aynı doğrultu", "aynı yön", "yukarı"])),
 ("m8i1", "b"): IK("Hayır. Kutu hareket etmiyor.", ["iş yapmış mıdır", "Açıklayınız"], "Evet/Hayır + çünkü.",
    HAYIR, P("Kutu ne durumda?", "hareket etmiyor", ["yukarı çıkıyor", "düşüyor"], k=DURUYOR)),
 ("m8i2", "a"): IK("Evet. Kuvvet de tepsi de yukarı (aynı doğrultu).", ["iş yapmış mıdır", "Açıklayınız"], "Evet/Hayır + çünkü.",
    EVET, P("Kuvvet ve tepsi hangi yöne?", "ikisi de yukarı (aynı doğrultu)", ["ikisi de aşağı", "farklı yönlere"], k=["aynı doğrultu", "aynı yön", "yukarı"])),
 ("m8i2", "b"): IK("Hayır. Kuvvet yukarı, hareket yatay.", ["iş yapmış mıdır", "Açıklayınız"], "Evet/Hayır + çünkü.",
    HAYIR, P("Kuvvetin ve hareketin yönü:", "kuvvet yukarı, hareket yatay", ["ikisi de ileri", "ikisi de yukarı"], k=["yatay", "dik", "farklı"])),
 ("m9i1", "a"): IK("Çekim potansiyel enerjisi; kütle ve yükseklik.", ["hangi enerjisi vardır", "hangi özelliklere bağlıdır"], "Enerjinin adı + bağlı olduğu iki şey.",
    P("Enerjinin adı:", "çekim potansiyel enerjisi", ["kinetik enerji", "ısı enerjisi"], k=["potansiyel"]),
    P("Bağlı olduğu iki şey:", "kütle ve yükseklik", ["hız ve renk", "sıcaklık"], hepsi=[["kütle", "ağırlı"], ["yüksek"]])),
 ("m9i1", "b"): IK("Kinetik enerji; kütle ve hız.", ["enerji nedir", "hangi özelliklere bağlıdır"], "Enerjinin adı + bağlı olduğu iki şey.",
    P("Enerjinin adı:", "kinetik enerji", ["potansiyel enerji", "ışık enerjisi"], k=["kinetik", "hareket enerjisi"]),
    P("Bağlı olduğu iki şey:", "kütle ve hız", ["yükseklik ve renk", "sıcaklık"], hepsi=[["kütle", "ağırlı"], ["hız", "sürat"]])),
 ("m9i1", "c"): IK("Hayır, çünkü hareket etmiyor.", ["kinetik enerjisi var mıdır", "Nedenini yazınız"], "Evet/Hayır + çünkü.",
    P("Cevap:", "hayır, yoktur", ["evet", "biraz vardır"], k=["hayır", "yok"]), P("Çünkü çocuk:", "hareket etmiyor", ["kayıyor", "koşuyor"], k=["hareket etm", "hareketsiz", "duruyor", "oturuyor"])),
 ("m9i2", "a"): IK("Esneklik potansiyel enerjisi.", ["hangi enerji depolanmıştır"], "Enerjinin adı yeter.",
    P("Enerjinin adı:", "esneklik potansiyel enerjisi", ["kinetik enerji", "ısı enerjisi"], k=["esneklik"])),
 ("m9i2", "b"): IK("Kinetik enerji.", ["enerji nedir"], "Enerjinin adı yeter.",
    P("Enerjinin adı:", "kinetik enerji", ["potansiyel enerji", "ışık enerjisi"], k=["kinetik", "hareket enerjisi"])),
 ("m9i2", "c"): IK("Esneklik için yay gerilmeli; kinetik için hareket gerekir.", ["karşılaştırınız"], "Karşılaştır: “Esneklik için … , kinetik için …”",
    P("Yay için gereken:", "gerilmesi (şeklinin değişmesi)", ["soğuması", "boyanması"], k=["geril", "şekl", "esne"]),
    P("Ok için gereken:", "hareket etmesi", ["durması", "boyanması"], k=["hareket", "hız"])),
}
for q in Y.d["mebSorular"]:
    for i, z in enumerate(q.get("ikizler", [])):
        zid = z.get("id") or f"{q['id']}i{i + 1}"
        for m in z["maddeler"]:
            b = IKIZ.get((zid, m["harf"]))
            if b: m.update(b); m.pop("iskele", None)

# Prova → benzediği MEB sorusu (provada "Hangi MEB sorusuna benziyor?" köprüsü)
BENZER = {"p1": ["m3", "m4", "m6", "m7", "m7", "m9"], "p2": ["m3", "m5", "m6", "m8", "m7", "m9"],
          "p3": ["m3", "m4", "m6", "m7", "m8", "m9"], "p4": ["m3", "m4", "m6", "m7", "m7", "m9"]}
for pv in Y.d["provalar"]:
    for q, b in zip(pv["sorular"], BENZER[pv["id"]]): q["benzer"] = b

Y.yaz()
