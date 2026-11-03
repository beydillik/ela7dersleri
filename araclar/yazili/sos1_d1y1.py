"""Sosyal Bilgiler 7 · 1. Dönem 1. Yazılı — Yazılıya Hazırlık verisi.
Kapsam: MEB senaryo tablosu, Senaryo 5 (okulun seçtiği): SB.7.1.1 (1), SB.7.1.2 (2), SB.7.1.3 (2), SB.7.2.1 (1) = 6 soru.
Kaynaklar: MEB "Yazılıya Hazırlanıyorum 7. Sınıf Sosyal Bilgiler 1. Dönem 1. Yazılı" (5 soru, çözümleriyle; bütün senaryoları kapsıyor),
ders kitabı (sayfa atıflı; kaynaklar/sos1/unite1.md, unite2.md), yazilihocam.com 7. sınıf Sosyal 1. dönem 1. yazılı örnekleri (siyah, mavi, kırmızı;
benzer soru ve provalarda, kimi birebir).
Öncelik (Kemal, 4 Kasım 2026: banko soruya daha çok emek): m1, m2, m3, m5 ★★★ Banko (kalıpla yazılır); m4 ★★ Puan topla.
Çalıştır: python3 araclar/yazili/sos1_d1y1.py"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from yazili import Yazili
import cizim_sos as Z


def A(ad, *k): return {"ad": ad, "k": list(k)}
def M(harf, soru, cevap=None, an=None, formul=None, puan=None):
    m = {"harf": harf, "soru": soru}
    if formul: m["formul"] = formul
    if cevap: m["cevap"] = cevap; m["anahtarlar"] = an or []
    if puan is not None: m["puan"] = puan
    return m
def P(bas, ornek, havuz, k=None, hepsi=None):
    d = {"bas": bas, "ornek": ornek, "havuz": havuz}
    if k: d["k"] = k
    if hepsi: d["hepsi"] = hepsi
    return d
def B(kisa, eksik, yanlis, ipucu, aciklama, *parcalar):
    return {"kisaCevap": kisa, "basamak": {"sec": {"secenekler": [kisa, eksik, yanlis], "dogru": 0, "ipucu": ipucu, "aciklama": aciklama}, "parcalar": list(parcalar)}}
def IK(kisa, tetik, notu, *parcalar): return {"kisaCevap": kisa, "tetik": tetik, "kalipNot": notu, "basamak": {"parcalar": list(parcalar)}}
def Q(madde, tetik, notu, b):
    madde.update(b); madde["tetik"], madde["kalipNot"] = tetik, notu; return madde

K1, K2, K3, K4 = "SB.7.1.1", "SB.7.1.2", "SB.7.1.3", "SB.7.2.1"

Y = Yazili("sos1", "d1y1",
    baslik="1. Dönem 1. Yazılı", ders="Sosyal Bilgiler", senaryo="Senaryo 5", sure=40, tarih="2026-11-06",
    dagilim={K1: 1, K2: 2, K3: 2, K4: 1},
    giris="Okulun seçtiği senaryoda <b>6 soru</b> var: İletişimden 1, Özel gereksinimli bireylerden 2, Millî meselelerden 2, Küreselleşmeden 1. "
          "Önce <b>★★★ Banko</b> soruları sağlamla: kalıbını bilirsen puan kesin. Millî Mücadele sorusu için üç kelime yeter: <b>yenilgi – Mondros – işgal</b>.",
    kapsamDisi=["Komşularımız ve Türk dünyası, barış ve ara buluculuk, göç, iklim krizi ve insani yardım (2. öğrenme alanının küreselleşme dışındaki konuları)",
                "3. öğrenme alanı: Ortak Mirasımız (Osmanlı tarihi)"],
    puanNotu="Puanlar tahminidir: okul soruların puanını farklı dağıtabilir. Toplam 100. Provalarda senaryodaki gibi 6 soru var; hangi alt konudan geleceği tahmindir.",
    kaynakNotu="Sorular MEB'in yayımladığı 'Yazılıya Hazırlanıyorum 7. Sınıf Sosyal Bilgiler 1. Dönem 1. Yazılı' örneklerine, ders kitabına ve yazilihocam.com yazılı örneklerine dayanır.",
    soruGiris="Bunlar MEB'in örnek soruları; yazılıda <b>benzerleri</b> çıkacak. <b>★★★ Banko</b> olanlarla başla. Cevabı kısa ve kalıba uygun yaz.",
    kazanimAd="konu")

# =====================================================================
# KONULAR (Hatırla kartları + Hatırla ve Tekrarla boşlukları)
# =====================================================================
Y.kazanim(kod=K1, ad="Dâhil olduğu gruplarda ve sosyal hayatta etkili iletişimin önemini sorgulayabilme", kisa="Etkili İletişim", soru=1, renk="#1971c2",
    konular=["u1k1", "u1k2", "u1k3"], sayfa="s. 17–22", svg=Z.h_iletisim(),
    maddeler=["<b>Empati</b>: kendini karşındakinin yerine koyup onun duygu ve düşüncelerini anlamaya çalışmak ve bunu ona yansıtmak. (s. 18)",
              "Empati cümlesi: <b>duygusunu söyle + öneri sun</b>. Kitaptaki örnek: “Canın sıkılmış olmalı Emine. İstersen derslerim bittikten sonra birlikte oyun oynayalım.” (s. 18)",
              "<b>Ben dili</b>: duygunu karşındakini suçlamadan söylemek. Örnek: “Eşyalarımın izinsiz kullanılmasından rahatsız oluyorum.” (s. 19)",
              "Ben dili kalıbı: <b>“… olduğunda (durum) kendimi … hissediyorum / … oluyorum.”</b> Kişiyi değil davranışı anlat. (s. 19)",
              "<b>Sen dili</b>: kişiyi suçlar, yargılar: “Odanı hiç toplamıyorsun.” Yanlış anlaşılmaya ve tartışmaya yol açar. (s. 22)",
              "<b>Etkin dinleme</b>: göz teması kur, sözünü kesme, “Seni anlıyorum.” de. Yüzdeki ifade <b>mimik</b>; el, kol, baş hareketi <b>jest</b>. (s. 20)"],
    kelimeler=["seni anlıyorum", "istersen …", "… olduğunda kendimi … hissediyorum", "suçlama yok", "göz teması", "mimik = yüz, jest = el"],
    hatalar=[{"yanlis": "Ben dilinde yine suçlamak: “Sen hep geç kalıyorsun, üzülüyorum.”", "dogru": "Davranışı ve duyguyu söyle: “Geç kaldığında üzülüyorum.”"},
             {"yanlis": "Empati yerine öğüt vermek: “Abartma, sinema çok güzel.”", "dogru": "Önce duygusunu anla: “Seni anlıyorum, yüksek ses seni rahatsız ediyor.”"},
             {"yanlis": "Kaş kaldırmak jesttir.", "dogru": "Yüzdeki ifade mimiktir; el, kol, baş hareketi jesttir."}],
    tekrar=[{"c": "Kendini karşındakinin yerine koyup onun duygularını anlamaya {empati|sen dili|öğüt} denir.", "s": "s. 18"},
            {"c": "Empati kuran Gizem kardeşine “{Canın sıkılmış olmalı|Sen de hep oyun istiyorsun}. İstersen birlikte oyun oynayalım.” der.", "s": "s. 18"},
            {"c": "Ben dili, duyguyu karşındakini {suçlamadan|suçlayarak} söylemektir.", "s": "s. 19"},
            {"c": "Ben dili cümlesi: “Geç kaldığında kendimi {değersiz hissediyorum|haklı görüyorum}.”", "s": "MEB örnek sorusu"},
            {"c": "Sen dili kişiyi {suçlar ve yargılar|anlar ve destekler}, tartışmaya yol açar.", "s": "s. 22"},
            {"c": "Etkin dinlemede konuşanla {göz teması kurulur|telefona bakılır} ve sözü {kesilmez|kesilir}.", "s": "s. 20"},
            {"c": "Yüzdeki ifadelere {mimik|jest}, el ve kol hareketlerine {jest|mimik} denir.", "s": "s. 20"}])

Y.kazanim(kod=K2, ad="Özel gereksinimli bireyler için fırsat eşitliğini sürdürmeye yönelik fikir üretebilme", kisa="Özel Gereksinimli Bireyler ve Fırsat Eşitliği", soru=2, renk="#2f9e44",
    konular=["u1k4"], sayfa="s. 33–37", svg=Z.h_firsat(),
    maddeler=["<b>Özel gereksinimli birey</b>: görme, işitme, bedensel ya da öğrenme alanında farklı ihtiyacı olan, ek desteğe ihtiyaç duyan kişi. (s. 33)",
              "<b>Fırsat eşitliği</b>: kim olursa olsun herkesin aynı haklara sahip olması. Okulda <b>rampa, asansör</b> ve özel eğitim desteği buna örnektir. (s. 33)",
              "Düzenleme örnekleri: kaldırımda <b>takip şeridi</b> (görme), <b>rampa ve asansör</b> (tekerlekli sandalye), kamu binası ve ulaşımda erişilebilirlik, engelsiz plaj. (s. 33–36)",
              "Fırsat eşitliği bireye ne kazandırır? <b>Bağımsız yaşar, öz güveni artar</b>, kendini değerli hisseder; toplumda adalet ve barış olur. (s. 33, 35)",
              "<b>Slogan</b>: kısa, akılda kalan, <b>olumlu</b> bir söz; içinde <b>herkes / birlikte / engel yok</b> olsun. Örnek: “Engelleri oyunla aşalım.” (MEB örnek sorusu)",
              "Fikir / öneri kalıbı: <b>Kim? → Neye ihtiyacı var? → Ne yapılmalı?</b> Tekerlekli sandalye kullanan çocuk → parka girmek → rampa yapılmalı. (s. 37)"],
    kelimeler=["herkes aynı haklara sahip", "rampa, asansör", "takip şeridi", "bağımsız yaşam", "öz güven", "kısa ve olumlu slogan", "… yapılmalı"],
    hatalar=[{"yanlis": "Olumsuz slogan: “Parkları bozanlar utansın!”", "dogru": "Olumlu ve herkesi kapsayan yaz: “Parklar herkesin, engel yok!”"},
             {"yanlis": "Herkese aynı şeyi yapmak (yalnız merdiven) fırsat eşitliğidir.", "dogru": "İhtiyaca göre düzenleme gerekir: merdivenin yanına rampa."},
             {"yanlis": "Öneriyi genel bırakmak: “Yardım edilmeli.”", "dogru": "Somut yaz: “Parka rampa yapılmalı.”"}],
    tekrar=[{"c": "Fırsat eşitliği, herkesin {aynı haklara sahip olmasıdır|aynı işi yapmasıdır}.", "s": "s. 33"},
            {"c": "Okullardaki {rampa ve asansör|zil ve tahta} fırsat eşitliğinin bir parçasıdır.", "s": "s. 33"},
            {"c": "Kaldırımlardaki takip şeritleri {görme|işitme} yetersizliği olan bireylerin güvenle yürümesini sağlar.", "s": "s. 33"},
            {"c": "Fırsat eşitliği bireyin öz güvenini {artırır|azaltır}.", "s": "s. 33"},
            {"c": "Toplum açısından fırsat eşitliği {adalet ve barış|kavga ve yalnızlık} ortamı oluşturur.", "s": "s. 33"},
            {"c": "İyi bir slogan {kısa ve olumludur|uzun ve suçlayıcıdır}.", "s": "MEB örnek sorusu"},
            {"c": "Öneri yazarken önce kişinin {ihtiyacını|adını} söyle, sonra {ne yapılmalı|kim suçlu} yaz.", "s": "cevap kalıbı"}])

Y.kazanim(kod=K3, ad="Türk toplumunun millî meseleler karşısında gösterdiği tutum ve davranışlara ilişkin çıkarım yapabilme", kisa="Millî Meseleler ve Türk Toplumu", soru=2, renk="#c92a2a",
    konular=["u1k5", "u1k6"], sayfa="s. 42–46", svg=Z.h_milli(),
    maddeler=["<b>Millî mesele</b>: bütün milleti ilgilendiren önemli gelişme (bağımsızlık, vatan bütünlüğü, güvenlik…). Örnek: Çanakkale Savaşları, Millî Mücadele, Kıbrıs Barış Harekâtı. (s. 44)",
              "Samsun'a çıkışın nedenleri: Osmanlı Devleti <b>Birinci Dünya Savaşı'nda yenildi</b>, <b>Mondros Ateşkes Antlaşması</b>'nı imzaladı, <b>Anadolu işgal edildi</b>. (s. 45)",
              "Mustafa Kemal <b>19 Mayıs 1919</b>'da Samsun'a çıktı; milletin bağımsızlık duygusunu canlandırıp halkı mücadele etrafında birleştirmek istedi. (s. 45)",
              "Halkın tutumu: tüm imkânsızlıklara rağmen <b>birlik oldu</b>; <b>Tekâlif-i Millîye</b> ile yiyecek, giyecek, araç ve gereçlerini <b>orduyla paylaştı</b> (fedakârlık, dayanışma). (s. 45)",
              "<b>15 Temmuz 2016</b> darbe girişimi: millet devletinin yanında durdu, <b>demokrasiye ve millî iradeye sahip çıktı</b>, girişim başarısız oldu. (s. 42, 45)",
              "<b>6 Şubat 2023</b> depremi: tüm Türkiye <b>tek yürek</b> oldu. Millî başarılar (Defne Kurt, Aziz Sancar) gurur ve birlik duygusu verir. (s. 43, 46)"],
    kelimeler=["yenilgi → Mondros → işgal", "19 Mayıs 1919", "birlik oldu", "orduyla paylaştı", "demokrasiye sahip çıktı", "tek yürek"],
    hatalar=[{"yanlis": "Neden olarak yalnız “savaş vardı” yazmak.", "dogru": "Üç olayı yaz: savaşta yenilgi, Mondros, Anadolu'nun işgali."},
             {"yanlis": "“Halk korktu ve mücadeleye katılmadı.”", "dogru": "Halk birlik oldu, elindeki imkânları orduyla paylaştı."},
             {"yanlis": "Mondros'u Samsun'a çıkıştan sonra yazmak.", "dogru": "Sıra: savaşta yenilgi → Mondros → işgal → 19 Mayıs 1919 Samsun."}],
    tekrar=[{"c": "Osmanlı Devleti {Birinci Dünya Savaşı'nda|Kurtuluş Savaşı'nda} yenildi.", "s": "s. 45"},
            {"c": "Yenilen Osmanlı Devleti {Mondros Ateşkes Antlaşması'nı|Kıbrıs Barış Harekâtı'nı} imzalamak zorunda kaldı.", "s": "s. 45"},
            {"c": "Antlaşmadan sonra Anadolu'nun birçok bölgesi {işgal edildi|kurtuldu}.", "s": "s. 45"},
            {"c": "Mustafa Kemal {19 Mayıs 1919|29 Ekim 1923}'da Samsun'a çıktı.", "s": "s. 45"},
            {"c": "Halk tüm imkânsızlıklara rağmen {birlik oldu|dağıldı} ve elindeki imkânları orduyla {paylaştı|sakladı}.", "s": "s. 45"},
            {"c": "15 Temmuz 2016'da Türk milleti demokrasiye {sahip çıktı|sırtını döndü}.", "s": "s. 45"},
            {"c": "6 Şubat 2023 depreminden sonra tüm Türkiye {tek yürek oldu|ilgisiz kaldı}.", "s": "s. 43"}])

Y.kazanim(kod=K4, ad="Küreselleşmenin insan ve toplum hayatında meydana getirdiği değişimi yorumlayabilme", kisa="Küreselleşme", soru=1, renk="#7048e8",
    konular=["u2k1", "u2k2"], sayfa="s. 58–63", svg=Z.h_kuresel(),
    maddeler=["<b>Küreselleşme</b>: dünyanın ekonomik, kültürel ve siyasi olarak birbirine daha bağlı hâle gelmesi. Alanları: ekonomi, ulaşım, iletişim, kültür, sağlık, çevre. (s. 60)",
              "<b>İletişim</b>: genel ağ ve mobil cihazlar sayesinde bilgiye kolay ulaşılır; dünyanın öbür ucundaki arkadaşına <b>saniyeler içinde</b> “Merhaba” dersin. (s. 58, 62)",
              "Örnek kalıbı: <b>Eskiden …; şimdi … sayesinde …</b> “Eskiden mektup günler sonra ulaşırdı; şimdi telefonla anında haberleşiyoruz.” (MEB örnek sorusu)",
              "<b>Ulaşım</b>: aylar süren yolculuklar gelişmiş ulaşım araçlarıyla birkaç saate indi. <b>Ekonomi</b>: e-ticaretle evden çıkmadan başka ülkelerden alışveriş. (s. 58, 62)",
              "<b>Kültür</b>: farklı kültürleri tanırız (olumlu) ama yerel kültürler zayıflayabilir (olumsuz); millî kültüre sahip çıkmak önemlidir. (s. 62)",
              "<b>Sağlık ve çevre</b>: teşhis ve tedavi kolaylaştı (olumlu); salgın hastalıklar hızla yayıldı, çevre kirliliği arttı (olumsuz). (s. 63)"],
    kelimeler=["genel ağ", "anında / saniyeler içinde", "eskiden … şimdi …", "olumlu – olumsuz", "farklı kültürleri tanıma", "millî kültüre sahip çıkma"],
    hatalar=[{"yanlis": "Örnek yerine tanım yazmak: “Küreselleşme dünyanın birbirine bağlanmasıdır.”", "dogru": "Günlük yaşamdan örnek ver: “Yurt dışındaki teyzemle görüntülü konuşuyorum.”"},
             {"yanlis": "Yalnız “telefon” yazıp bırakmak.", "dogru": "Değişimi anlat: eskiden mektup günler sürerdi, şimdi telefonla anında."},
             {"yanlis": "Küreselleşmenin hiç olumsuz etkisi yoktur.", "dogru": "Yerel kültür zayıflayabilir, salgın ve çevre sorunları yayılabilir."}],
    tekrar=[{"c": "Küreselleşme, dünyanın birbirine daha {bağlı|uzak} hâle gelmesi sürecidir.", "s": "s. 60"},
            {"c": "Genel ağ ve mobil cihazlar sayesinde insanlar birbirleriyle {anında|aylar sonra} haberleşir.", "s": "s. 58, 62"},
            {"c": "Eskiden mektuplar sahiplerine {günler sonra|saniyeler içinde} ulaşırdı.", "s": "MEB örnek sorusu"},
            {"c": "Eskiden aylar süren yolculuklar gelişmiş ulaşım araçlarıyla {birkaç saate|birkaç yıla} indi.", "s": "s. 58"},
            {"c": "E-ticaret sayesinde {evden çıkmadan başka ülkelerle|yalnız mahalle bakkalından} alışveriş yapılabilir.", "s": "s. 62"},
            {"c": "Küreselleşmeyle farklı kültürleri tanırız ama yerel kültürler {zayıflayabilir|hiç değişmez}.", "s": "s. 62"},
            {"c": "“Örnek veriniz” sorusunda {eskiden … şimdi …|yalnız tanım} kalıbıyla yaz.", "s": "cevap kalıbı"}])

# =====================================================================
# CEVAP KALIPLARI (Özet'te liste; sorunun içinde tek satır kalıp notu)
# =====================================================================
Y.formul(id="empati", ad="Empati cümlesi", kalip="Seni anlıyorum + duygusu + İstersen … (öneri)", ne="“Empati kurduğunu gösteren konuşma yazınız” sorularında", ornek="Seni anlıyorum, yüksek ses seni rahatsız ediyor. İstersen parka gidelim.")
Y.formul(id="bendili", ad="Ben diline çevir", kalip="… olduğunda (durum) + kendimi … hissediyorum / … oluyorum", ne="“Ben diline çeviriniz” sorularında", ornek="Geç kaldığında kendimi değersiz hissediyorum.")
Y.formul(id="kavram", ad="Kavram + çünkü", kalip="Kavramın adı + çünkü …", ne="“Hangi unsura örnektir? Neden?” sorularında", ornek="Empati, çünkü kendini arkadaşının yerine koymuş.")
Y.formul(id="slogan", ad="Slogan", kalip="Kısa + olumlu + herkes / birlikte / engel yok", ne="“Slogan yazınız” sorularında", ornek="Parklar herkesin, engel yok!")
Y.formul(id="oneri", ad="Fikir / öneri / etki", kalip="Kim? → Neye ihtiyacı var? → Ne yapılmalı? (etki: bağımsız olur, öz güveni artar)", ne="“Öneri yazınız”, “olumlu etkisini açıklayınız” sorularında", ornek="Tekerlekli sandalye kullananlar için parka rampa yapılmalı.")
Y.formul(id="neden", ad="Neden (tarih)", kalip="Yenilgi → Mondros → işgal", ne="“Hangi tarihsel gelişmeler etkili olmuştur?” sorularında", ornek="Osmanlı Birinci Dünya Savaşı'nda yenildi, Mondros'u imzaladı, Anadolu işgal edildi.")
Y.formul(id="tutum", ad="Halkın tutumu", kalip="Halk ne yaptı? + hangi değer (birlik, dayanışma, fedakârlık)", ne="“Yaklaşımı nasıl olmuştur?”, “hangi özelliğini gösterir?” sorularında", ornek="Halk birlik oldu, imkânlarını orduyla paylaştı; bu dayanışmadır.")
Y.formul(id="ornek", ad="Eskiden – şimdi", kalip="Eskiden …; şimdi … sayesinde …", ne="“Günlük yaşamdan örnek veriniz” sorularında", ornek="Eskiden mektup günler sürerdi; şimdi genel ağ sayesinde anında haberleşiyoruz.")
Y.formul(id="olumlu", ad="Olumlu – olumsuz", kalip="Olumlu: … · Olumsuz: …", ne="“Olumlu ve olumsuz etkisini yazınız” sorularında", ornek="Olumlu: farklı kültürleri tanırız. Olumsuz: yerel kültür zayıflar.")

# ortak anahtar kökleri
ANLA = ["anlıyorum", "anladım", "yerinde olsa", "ben de"]
DUYGU_BEN = ["hissediyorum", "oluyorum", "üzülüyorum", "kırılıyorum", "değersiz", "rahatsız", "huzursuz", "zorlanıyorum", "endişe"]
KAPSA = ["herkes", "birlikte", "eşit", "engel yok", "engelsiz", "hep beraber", "aşalım", "hepimiz"]
YAP = ["yapılmalı", "kurulmalı", "konulmalı", "konmalı", "verilmeli", "eklenmeli", "olmalı"]

# =====================================================================
# MEB SORULARI (5 soru) — öncelik: 3 banko, 2 puan topla
# =====================================================================
Y.meb(id="m1", no=1, kazanim=K1, oncelik=3,
    metin=["Selim, sınıf arkadaşı Ezel ile sinemaya gitmek istemiştir. Ezel ise yüksek sesten rahatsız olduğu için sinemaya gitmek istemediğini belirtmiştir. Bunun üzerine Selim, Ezel'e şunları söylemiştir:"],
    maddeler=[Q(M("a", "Aşağıda boş bırakılan alana Selim'in Ezel ile empati kurduğunu gösteren bir konuşma metni yazınız.",
        "Seni anlıyorum Ezel, yüksek ses seni rahatsız ediyor. Ben de rahatsız olduğum bir yerde eğlenemezdim. İstersen sinema yerine birlikte parkta dolaşalım.",
        [A("Onu anladığını söyler", *ANLA), A("Duygusunu fark eder", "rahatsız", "hoşlanm", "sevm"), A("Başka bir şey önerir", "gidelim", "yapalım", "oynayalım", "izleyelim", "dolaş", "birlikte")], "empati"),
        ["empati kurduğunu", "konuşma metni"], "Empati → “Seni anlıyorum” + duygusu + “İstersen …” önerisi.",
        B("Seni anlıyorum, yüksek ses seni rahatsız ediyor. İstersen parka gidelim.", "Seni anlıyorum.", "Abartma Ezel, sinema çok güzel, hadi gel.",
          "Empati kuran kişi karşısındakinin duygusunu anlar ve bunu ona söyler.", "Empati: kendini karşındakinin yerine koyup duygusunu anlamak ve bunu ona yansıtmak. Bir öneri eklemek cevabı tamamlar. (s. 18)",
          P("Selim: “Ezel,", "seni anlıyorum", ["sen çok abartıyorsun", "sinema çok eğlenceli"], k=ANLA),
          P("Yüksek ses seni", "rahatsız ediyor", ["çok mutlu ediyor", "hiç etkilemiyor"], k=["rahatsız", "hoşlanm", "sevm"]),
          P("İstersen", "birlikte parka gidelim", ["sen evde otur", "ben yalnız giderim"], k=["gidelim", "yapalım", "oynayalım", "izleyelim", "dolaş", "birlikte"])))],
    ikizler=[
        {"metin": ["Ayşe, okulun voleybol takımına seçilemediği için çok üzülmüştür. Teneffüste yalnız başına oturan Ayşe'nin yanına arkadaşı Elif gelmiştir."],
         "maddeler": [M("a", "Elif'in Ayşe ile empati kurduğunu gösteren bir konuşma metni yazınız.",
            "Seni anlıyorum Ayşe, çok emek verdiğin için üzülmen çok doğal. Ben de senin yerinde olsam üzülürdüm. İstersen birlikte çalışalım, gelecek yıl yine deneriz.",
            [A("Onu anladığını söyler", *ANLA), A("Duygusunu fark eder", "üzül", "kırgın", "moral"), A("Öneri ya da destek", "istersen", "birlikte", "çalışalım", "deneriz", "yardım")], "empati")]},
        {"metin": ["Elif, yarışmada derece alamadığı için üzgün olan arkadaşına “Senin yerinde olsaydım ben de üzülürdüm. Bunun için çok emek verdiğini biliyorum.” der."],
         "maddeler": [M("a", "Elif'in bu davranışı hangi etkili iletişim unsuruna örnektir? Neden?",
            "Empatiye örnektir. Çünkü Elif kendini arkadaşının yerine koyarak onun duygularını anlamaya çalışmıştır.",
            [A("Empati", "empati"), A("Kendini onun yerine koydu", "yerine koy", "duygu", "anla")], "kavram")]}])

Y.meb(id="m2", no=2, kazanim=K1, oncelik=3,
    metin=["Aşağıda “sen dili” ile kurulan cümleler yer almaktadır. Bu cümleleri “ben dili”ne çevirerek altlarındaki noktalı alanlara yazınız."],
    maddeler=[
        Q(M("a", "“Sürekli geç kalmandan bıktım!” cümlesini “ben dili”ne çeviriniz.",
            "Geç kaldığında beklemek zorunda kalıyorum ve kendimi değersiz hissediyorum. Zamanında gelmeni isterim.",
            [A("Durumu anlatır (geç kalma)", "kaldığında", "kalındığında", "kalınca"), A("Kendi duygusunu söyler", *DUYGU_BEN)], "bendili"),
          ["“ben dili”ne çeviriniz"], "Ben dili → “… olduğunda kendimi … hissediyorum.” Suçlama yok.",
          B("Geç kaldığında kendimi değersiz hissediyorum.", "Kendimi değersiz hissediyorum.", "Sen hep geç kalıyorsun, bundan bıktım!",
            "Ben dilinde kişi suçlanmaz; durum ve senin duygun söylenir.", "Ben dili: duyguyu karşındakini suçlamadan söylemek. Kalıp: … olduğunda kendimi … hissediyorum. (s. 19)",
            P("Ne olduğunda?", "geç kaldığında", ["sen hep geç kalıyorsun", "hiç gelmiyorsun"], k=["kaldığında", "kalındığında", "kalınca"]),
            P("Duygum: kendimi", "değersiz hissediyorum", ["çok haklı görüyorum", "senden bıktım"], k=["hissediyorum", "üzülüyorum", "kırılıyorum", "değersiz"]))),
        Q(M("b", "“Salonu dağınık bırakıyorsun.” cümlesini “ben dili”ne çeviriniz.",
            "Salon dağınık kaldığında aradığımı bulamıyorum ve bu beni rahatsız ediyor.",
            [A("Durumu anlatır (dağınık salon)", "dağınık"), A("Kendi duygusunu söyler", *DUYGU_BEN)], "bendili"),
          ["“ben dili”ne çeviriniz"], "Ben dili → “… olduğunda kendimi … hissediyorum.” Suçlama yok.",
          B("Salon dağınık olduğunda rahatsız oluyorum.", "Rahatsız oluyorum.", "Hiç toplamıyorsun, çok dağınıksın!",
            "Ben dilinde hem durum hem duygu söylenir; “sen” ile suçlanmaz.", "Kitaptaki örnek: “Odanın dağınık olmasından rahatsız oluyorum.” Kişi suçlanmıyor, duygu söyleniyor. (s. 19)",
            P("Ne olduğunda? Salon", "dağınık olduğunda", ["hep dağıtıyorsun", "temiz olduğunda"], k=["dağınık"]),
            P("Duygum:", "rahatsız oluyorum", ["sen çok tembelsin", "beni hiç dinlemiyorsun"], k=DUYGU_BEN)))],
    ikizler=[
        {"metin": ["Aşağıda “sen dili” ile kurulmuş cümleler verilmiştir."],
         "maddeler": [M("a", "“Kitabımı yine izinsiz almışsın. Eşyalarıma hiç saygı göstermiyorsun.” cümlesini “ben dili”ne çeviriniz.",
                        "Kitabım bana sorulmadan alındığında rahatsız oluyorum. Eşyalarımı kullanmadan önce izin istemeni isterim.",
                        [A("Durumu anlatır", "sorulmadan", "izinsiz", "izin"), A("Kendi duygusunu söyler", *DUYGU_BEN)], "bendili"),
                      M("b", "“Konuşurken sürekli sözümü kesiyorsun. Beni hiç dinlemiyorsun.” cümlesini “ben dili”ne çeviriniz.",
                        "Konuşurken sözüm kesildiğinde kendimi dinlenmiyormuş gibi hissediyorum. Sözümü tamamlamama fırsat vermeni isterim.",
                        [A("Durumu anlatır", "kesildiğinde", "kesilince", "sözüm kesil"), A("Kendi duygusunu söyler", *DUYGU_BEN)], "bendili")]},
        {"metin": ["Bir öğrenci arkadaşına “Sen zaten hiçbir zaman beni dinlemiyorsun, çok düşüncesizsin.” der."],
         "maddeler": [M("a", "Bu cümle hangi iletişim biçimiyle kurulmuştur? İletişimi nasıl olumsuz etkileyebilir? Açıklayınız.",
            "Sen dili ile kurulmuştur. Kişiyi suçlayıp yargıladığı için karşıdaki kişi savunmaya geçer, tartışma çıkar ve iletişim bozulur.",
            [A("Sen dili", "sen dil"), A("Suçlar, yargılar", "suçla", "yargıla"), A("Tartışmaya yol açar", "tartışma", "kavga", "kırıl", "bozul", "savunma", "uzaklaş")], "kavram")]}])

Y.meb(id="m3", no=3, kazanim=K2, oncelik=3,
    metin=["Mahallenizdeki oyun parklarının özel gereksinimli çocukların ihtiyaçlarına uygun şekilde düzenlenmesini ve bu konuda kamuoyu oluşturulmasını istediğinizi düşününüz."],
    maddeler=[Q(M("a", "Amacınıza uygun bir slogan yazınız.", "Engelleri oyunla aşalım, parklar herkes için!",
        [A("Konuya uygun (park, oyun)", "park", "oyun", "salıncak", "kayd"), A("Herkesi kapsayan olumlu söz", *KAPSA)], "slogan"),
        ["slogan"], "Slogan → kısa + olumlu + “herkes / birlikte / engel yok”.",
        B("Parklar herkesin, engel yok!", "Parklar güzeldir.", "Parkları bozanlar utansın!",
          "MEB amaca uygun ve olumsuz ifade içermeyen her sloganı kabul ediyor. Amaç: herkesin oynayabileceği park.",
          "Slogan kısa, olumlu ve amaca uygun olmalı: özel gereksinimli çocukların da oynayabileceği parklar. (MEB örnek sorusu; s. 33)",
          P("Nerede?", "Parklar", ["Arabalar", "Dersler"], k=["park", "oyun"]),
          P("Kimin için?", "herkesin", ["kimsenin", "yalnız benim"], k=["herkes", "birlikte", "eşit"]),
          P("Olumlu son:", "engel yok!", ["git buradan!", "yasak!"], k=["engel yok", "engelsiz", "aşalım", "hep beraber"])))],
    ikizler=[
        {"metin": ["Okulunuzdaki kütüphanenin ve laboratuvarın tekerlekli sandalye kullanan öğrencilerin de rahatça girebileceği şekilde düzenlenmesini istiyorsunuz. Okul panosuna bir afiş asacaksınız."],
         "maddeler": [M("a", "Afişiniz için amacınıza uygun bir slogan yazınız.", "Okulumuz herkesin, rampayla engel yok!",
            [A("Konuya uygun (okul, kütüphane)", "okul", "kütüphane", "sınıf", "laboratuvar", "ders", "kitap"), A("Herkesi kapsayan olumlu söz", *KAPSA)], "slogan")]},
        {"metin": ["Bir okulda asansör ve rampa yapılmasının ardından bedensel yetersizliği olan öğrenciler sınıflara ve laboratuvarlara başkasının yardımına ihtiyaç duymadan ulaşmaya başlamıştır."],
         "maddeler": [M("a", "Bu değişikliğin öğrenciler üzerindeki iki olumlu etkisini açıklayınız.",
            "Öğrenciler başkasına ihtiyaç duymadan bağımsız hareket eder. Kendilerini değerli hisseder, öz güvenleri artar ve derslere eşit şekilde katılırlar.",
            [A("1. etki: bağımsız hareket eder", "bağımsız", "kendi başına", "yardımsız"), A("2. etki: öz güveni artar, eşit katılır", "öz güven", "özgüven", "değerli", "eşit", "katıl", "mutlu")], "oneri")]}])

Y.meb(id="m4", no=4, kazanim=K3, oncelik=2,
    metin=["Mustafa Kemal Paşa, 19 Mayıs 1919'da Samsun'a çıkarak Millî Mücadele'yi başlatmıştır."],
    maddeler=[
        Q(M("a", "Mustafa Kemal Paşa'nın bu adımı atmasında hangi tarihsel gelişmeler etkili olmuştur?",
            "Osmanlı Devleti'nin Birinci Dünya Savaşı'nda yenilmesi, Mondros Ateşkes Antlaşması'nı imzalaması ve Anadolu'nun işgale uğraması.",
            [A("Birinci Dünya Savaşı'nda yenilgi", "yenil", "mağlup"), A("Mondros Ateşkes Antlaşması", "mondros"), A("Anadolu'nun işgali", "işgal")], "neden"),
          ["hangi tarihsel gelişmeler"], "Neden → üç olay sırayla: yenilgi → Mondros → işgal.",
          B("Savaşta yenilgi, Mondros, Anadolu'nun işgali.", "Anadolu işgal edilmişti.", "Türkiye Cumhuriyeti kurulmuştu.",
            "Kitap üç olay sayıyor: bir savaş, bir antlaşma, bir işgal.", "Osmanlı Birinci Dünya Savaşı'nda yenildi, Mondros Ateşkes Antlaşması'nı imzaladı, ardından Anadolu işgal edildi. (s. 45)",
            P("1. Osmanlı Devleti Birinci Dünya Savaşı'nda", "yenildi", ["kazandı", "hiç savaşmadı"], k=["yenil", "mağlup"]),
            P("2. İmzaladığı antlaşma:", "Mondros Ateşkes Antlaşması", ["Barış Harekâtı", "Tekâlif-i Millîye"], k=["mondros"]),
            P("3. Antlaşmadan sonra Anadolu", "işgal edildi", ["kalkındı", "bayram yaptı"], k=["işgal"]))),
        Q(M("b", "Anadolu halkının, Mustafa Kemal Paşa'nın başlattığı bu mücadeleye yaklaşımı nasıl olmuştur?",
            "Anadolu halkı, tüm imkânsızlıklara rağmen yurdunu savunmak için seferber olmuş, birlik içinde hareket etmiş ve elindeki yiyecek, giyecek, araç ve gereçleri ordusuyla paylaşmıştır.",
            [A("Destek verdi, birlik oldu", "birlik", "seferber", "destek"), A("İmkânlarını orduyla paylaştı", "paylaş", "yardım")], "tutum"),
          ["yaklaşımı nasıl olmuştur"], "Tutum → halk ne yaptı? “Birlik oldu + orduyla paylaştı.”",
          B("Halk birlik oldu, elindeki imkânları orduyla paylaştı.", "Halk destek verdi.", "Halk savaştan korktu ve mücadeleye katılmadı.",
            "İki şey yaz: halk nasıl davrandı, elindekilerle ne yaptı?", "Halk tüm imkânsızlıklara rağmen birlik içinde hareket etti; Tekâlif-i Millîye ile yiyecek, giyecek, araç ve gereçlerini orduyla paylaştı. (s. 45)",
            P("Halk tüm imkânsızlıklara rağmen", "birlik oldu", ["kaçtı", "mücadeleye karşı çıktı"], k=["birlik", "seferber", "destek"]),
            P("Elindeki yiyecek ve giyeceği", "orduyla paylaştı", ["sakladı", "sattı"], k=["paylaş", "yardım"])))],
    ikizler=[
        {"metin": ["Millî Mücadele yıllarında Anadolu'nun farklı bölgelerinde yaşayan kadınlar, vatanın bağımsızlığı için yürütülen çalışmalara çeşitli şekillerde destek olmuştur. "
                   "Kimi cephe gerisinde yaralıların bakımına yardım etmiş, kimi yiyecek ve giyecek hazırlamış, kimi de ordunun ihtiyaç duyduğu malzemelerin taşınmasına katkı sağlamıştır. "
                   "Zorlu hava koşulları, yoksulluk ve imkânsızlıklar bu kadınları mücadeleden vazgeçirmemiştir."],
         "maddeler": [M("a", "Millî Mücadele başlamadan önce Osmanlı Devleti ve Anadolu hangi zor durumdaydı?",
                        "Osmanlı Devleti Birinci Dünya Savaşı'nda yenilmiş, Mondros Ateşkes Antlaşması'nı imzalamak zorunda kalmış ve Anadolu'nun birçok bölgesi işgal edilmişti.",
                        [A("Savaşta yenilgi", "yenil", "mağlup"), A("Mondros", "mondros"), A("İşgal", "işgal")], "neden"),
                      M("b", "Kadınların karşılaştıkları güçlüklere rağmen mücadeleye destek vermeleri, Türk toplumunun millî meseleler karşısındaki hangi özelliklerini göstermektedir? Açıklayınız.",
                        "Birlik, dayanışma, yardımlaşma, fedakârlık ve vatanseverlik özelliklerini gösterir. Türk toplumu zor zamanlarda ayrım yapmadan birlik olmuş, elindeki imkânları mücadeleye vermiştir.",
                        [A("Birlik, dayanışma", "birlik", "dayanışma", "yardımlaş", "beraber"), A("Fedakârlık, vatanseverlik", "fedakâr", "vatansever", "vatan sevgisi", "sorumluluk")], "tutum")]},
        {"metin": ["15 Temmuz 2016 gecesi Türkiye, demokratik düzeni ortadan kaldırmaya yönelik bir girişimle karşı karşıya kalmıştır. Darbeciler Türkiye Büyük Millet Meclisi'ni bombalamıştır."],
         "maddeler": [M("a", "Bu girişimin adı nedir? Neyi hedef almıştır?", "Darbe girişimidir. Demokrasiyi ve milletin seçtiği yönetimi hedef almıştır.",
                        [A("Darbe girişimi", "darbe"), A("Demokrasiyi hedef aldı", "demokrasi", "seçtiği", "millî irade", "halkın")], "kavram"),
                      M("b", "Türk milletinin bu girişim karşısındaki tutumu nasıl olmuştur?",
                        "Türk milleti devletinin yanında yer almış, canı pahasına demokrasiye ve millî iradeye sahip çıkmış, birlik olarak girişimi başarısızlığa uğratmıştır.",
                        [A("Demokrasiye sahip çıktı", "sahip çık", "savun", "millî irade"), A("Birlik oldu, girişim başarısız oldu", "birlik", "başarısız", "engelle", "durdur")], "tutum")]}])

Y.meb(id="m5", no=5, kazanim=K4, oncelik=3,
    metin=["Küreselleşme, insan ve toplum yaşamının birçok alanında olduğu gibi iletişim alanında da önemli değişimlere yol açmıştır."],
    maddeler=[Q(M("a", "Bu değişime günlük yaşamdan bir örnek veriniz.",
        "Eskiden mektuplar, ulaşım araçlarıyla günler sonra sahiplerine ulaştırılırdı. Günümüzde ise genel ağ ve cep telefonları sayesinde insanlar birbirleriyle anında haberleşebiliyor.",
        [A("İletişim aracı (genel ağ, telefon)", "genel ağ", "internet", "telefon", "mesaj", "görüntülü", "sosyal medya", "bilgisayar"), A("Hız: anında, hızlı", "anında", "hızlı", "saniye", "hemen", "kolay")], "ornek"),
        ["günlük yaşamdan bir örnek"], "Örnek ver → “Eskiden …; şimdi … sayesinde anında …”",
        B("Eskiden mektup günler sürerdi; şimdi telefonla anında konuşuyoruz.", "Telefon kullanıyoruz.", "Küreselleşme, dünyanın birbirine bağlanmasıdır.",
          "Soru tanım değil örnek istiyor: eskiden ve şimdi nasıl haberleşiyoruz?", "Genel ağ ve mobil cihazlar sayesinde iletişim çok hızlandı; uzaktakilerle canlı görüşebiliyoruz. (s. 62)",
          P("Eskiden", "mektup günler sonra ulaşırdı", ["görüntülü konuşurduk", "hiç haberleşilmezdi"], k=["mektup", "günler", "haftalar"]),
          P("Şimdi", "genel ağ ve telefon sayesinde", ["posta güvercini ile", "at arabasıyla"], k=["genel ağ", "internet", "telefon", "mesaj", "görüntülü", "bilgisayar"]),
          P("Böylece", "anında haberleşiyoruz", ["aylarca bekliyoruz", "hiç konuşmuyoruz"], k=["anında", "hızlı", "saniye", "hemen"])))],
    ikizler=[
        {"metin": ["Mersin'de yaşayan Deniz, çevrim içi bir oyun sayesinde Japonya'da yaşayan bir öğrenciyle tanışır. İkisi birkaç saniye içinde mesajlaşıp okul yaşamları hakkında bilgi paylaşır."],
         "maddeler": [M("a", "Bu olay küreselleşmenin hangi yönünü göstermektedir? Açıklayınız.",
            "İletişim alanındaki etkisini gösterir. Genel ağ sayesinde dünyanın farklı yerlerindeki insanlar saniyeler içinde haberleşebilmektedir.",
            [A("İletişim", "iletişim", "haberleş"), A("Hız: anında", "saniye", "anında", "hızlı")], "kavram")]},
        {"metin": ["Küreselleşme, ulaşım alanında da önemli değişimlere yol açmıştır."],
         "maddeler": [M("a", "Bu değişime günlük yaşamdan bir örnek veriniz.",
            "Eskiden başka bir ülkeye gitmek gemiyle aylar sürerdi. Günümüzde uçak sayesinde birkaç saatte başka bir ülkeye gidebiliyoruz.",
            [A("Ulaşım aracı", "uçak", "tren", "gemi", "otobüs"), A("Hız: birkaç saat, kısa sürede", "saat", "hızlı", "kısa sürede", "çabuk")], "ornek")]}])

# =====================================================================
# BENZER SORULAR (Konu Tekrarı): kısa cevap, tetik, kalıp notu, parçalar (sec YOK → doğrudan sınavdaki gibi yazma)
# =====================================================================
IKIZ = {
 ("m1i1", "a"): IK("Seni anlıyorum, üzülmen çok doğal. İstersen birlikte çalışalım.", ["empati kurduğunu", "konuşma metni"], "Empati → “Seni anlıyorum” + duygusu + “İstersen …” önerisi.",
    P("Elif: “Ayşe,", "seni anlıyorum", ["bunu dert etme", "sen zaten iyi oynamıyorsun"], k=ANLA),
    P("Seçilemediğin için", "üzülmen çok doğal", ["hiç önemli değil", "boşuna ağlıyorsun"], k=["üzül", "kırgın", "moral"]),
    P("Bir önerim var:", "istersen birlikte çalışalım", ["bir daha deneme", "takımı unut"], k=["istersen", "birlikte", "çalışalım", "deneriz", "yardım"])),
 ("m1i2", "a"): IK("Empati; çünkü kendini arkadaşının yerine koydu.", ["hangi etkili iletişim unsuruna", "Neden"], "Kavramın adı + “çünkü …” gerekçesi.",
    P("Unsurun adı:", "empati", ["sen dili", "jest"], k=["empati"]),
    P("Çünkü Elif kendini arkadaşının", "yerine koydu", ["sözünü kesti", "suçladı"], k=["yerine koy", "duygu", "anla"])),
 ("m2i1", "a"): IK("Kitabım izinsiz alındığında rahatsız oluyorum.", ["“ben dili”ne çeviriniz"], "Ben dili → “… olduğunda kendimi … hissediyorum.” Suçlama yok.",
    P("Ne olduğunda? Kitabım", "izinsiz alındığında", ["hep sen alıyorsun", "sen saygısızsın"], k=["sorulmadan", "izinsiz", "izin"]),
    P("Duygum:", "rahatsız oluyorum", ["sen hiç saygı duymuyorsun", "bir daha alma"], k=DUYGU_BEN)),
 ("m2i1", "b"): IK("Sözüm kesildiğinde kendimi dinlenmiyormuş gibi hissediyorum.", ["“ben dili”ne çeviriniz"], "Ben dili → “… olduğunda kendimi … hissediyorum.” Suçlama yok.",
    P("Ne olduğunda?", "sözüm kesildiğinde", ["sen hep sözümü kesiyorsun", "hiç susmuyorsun"], k=["kesildiğinde", "kesilince", "sözüm kesil"]),
    P("Duygum: kendimi", "dinlenmiyormuş gibi hissediyorum", ["çok haklı görüyorum", "senden bıktım"], k=["hissediyorum", "üzülüyorum", "kırılıyorum", "rahatsız"])),
 ("m2i2", "a"): IK("Sen dili; kişiyi suçladığı için tartışma çıkar.", ["hangi iletişim biçimiyle", "olumsuz etkileyebilir"], "Biçimin adı + “çünkü suçlar” + sonucu (tartışma).",
    P("İletişim biçimi:", "sen dili", ["ben dili", "empati"], k=["sen dil"]),
    P("Çünkü kişiyi", "suçlar ve yargılar", ["anlar", "över"], k=["suçla", "yargıla"]),
    P("Sonuç:", "tartışma çıkar", ["dostluk güçlenir", "iletişim güzelleşir"], k=["tartışma", "kavga", "kırıl", "bozul", "savunma", "uzaklaş"])),
 ("m3i1", "a"): IK("Okul herkesin, engel yok!", ["slogan"], "Slogan → kısa + olumlu + “herkes / birlikte / engel yok”.",
    P("Nerede?", "Okulumuz", ["Sokaklar", "Arabalar"], k=["okul", "kütüphane", "sınıf", "laboratuvar"]),
    P("Kimin için?", "herkesin", ["kimsenin", "birkaç kişinin"], k=["herkes", "birlikte", "eşit"]),
    P("Olumlu son:", "engel yok!", ["giremezsin!", "yasak!"], k=["engel yok", "engelsiz", "aşalım", "hep beraber"])),
 ("m3i2", "a"): IK("Bağımsız hareket ederler ve öz güvenleri artar.", ["iki olumlu etkisini"], "İki etki yaz → “1) bağımsız olur, 2) öz güveni artar.”",
    P("1. etki: Öğrenciler", "bağımsız hareket eder", ["hep yardım bekler", "okula gelmez"], k=["bağımsız", "kendi başına", "yardımsız"]),
    P("2. etki: Öğrencilerin", "öz güveni artar", ["öz güveni azalır", "dersleri azalır"], k=["güveni art", "güvenleri art", "değerli", "eşit", "mutlu"])),
 ("m4i1", "a"): IK("Savaşta yenilgi, Mondros, Anadolu'nun işgali.", ["hangi zor durumdaydı"], "Neden → üç olay sırayla: yenilgi → Mondros → işgal.",
    P("1. Birinci Dünya Savaşı'nda", "yenildi", ["kazandı", "hiç savaşmadı"], k=["yenil", "mağlup"]),
    P("2. İmzaladığı antlaşma:", "Mondros", ["Kıbrıs", "Tekâlif-i Millîye"], k=["mondros"]),
    P("3. Anadolu", "işgal edildi", ["kalkındı", "bayram yaptı"], k=["işgal"])),
 ("m4i1", "b"): IK("Birlik, dayanışma ve fedakârlık.", ["hangi özelliklerini"], "Özellik → değer adları: “birlik, dayanışma, fedakârlık”.",
    P("Toplum zor zamanda", "birlik ve dayanışma gösterir", ["dağılır", "kavga eder"], k=["birlik", "dayanışma", "yardımlaş", "beraber"]),
    P("Kendi sıkıntısını bırakıp", "fedakârlık yapar", ["yalnız kendini düşünür", "vazgeçer"], k=["fedakâr", "vatansever", "vatan sevgisi", "sorumluluk"])),
 ("m4i2", "a"): IK("Darbe girişimi; demokrasiyi hedef aldı.", ["girişimin adı", "Neyi hedef almıştır"], "Kavramın adı + neyi hedef aldı: “darbe → demokrasi”.",
    P("Girişimin adı:", "darbe girişimi", ["deprem", "seçim"], k=["darbe"]),
    P("Hedef aldığı:", "demokrasi", ["spor", "ticaret"], k=["demokrasi", "seçtiği", "millî irade", "halkın"])),
 ("m4i2", "b"): IK("Demokrasiye sahip çıktı, birlik olup girişimi başarısız kıldı.", ["tutumu nasıl olmuştur"], "Tutum → millet ne yaptı? “sahip çıktı + birlik oldu”.",
    P("Millet demokrasiye", "sahip çıktı", ["sırtını döndü", "karşı çıktı"], k=["sahip çık", "savun"]),
    P("Sonuç: girişim", "başarısız oldu", ["başarılı oldu", "destek buldu"], k=["başarısız", "engelle", "durdur"])),
 ("m5i1", "a"): IK("İletişim; genel ağ sayesinde uzaktakiyle anında konuşulur.", ["hangi yönünü"], "Alanın adı + nasıl değişti: “iletişim → anında”.",
    P("Alan:", "iletişim", ["sağlık", "çevre"], k=["iletişim", "haberleş"]),
    P("Genel ağ sayesinde başka ülkedeki biriyle", "anında konuşulur", ["hiç konuşulmaz", "aylar sonra yazışılır"], k=["saniye", "anında", "hızlı"])),
 ("m5i2", "a"): IK("Eskiden yolculuk aylar sürerdi; şimdi uçakla birkaç saatte gidiyoruz.", ["günlük yaşamdan bir örnek"], "Örnek ver → “Eskiden …; şimdi … sayesinde anında …”",
    P("Eskiden", "yolculuk aylar sürerdi", ["uçakla bir saat sürerdi", "hiç yolculuk yoktu"], k=["aylar", "günler", "uzun"]),
    P("Şimdi", "uçak sayesinde", ["yürüyerek", "at sırtında"], k=["uçak", "tren", "gemi", "otobüs"]),
    P("Böylece", "birkaç saatte gidiyoruz", ["yıllarca yoldayız", "hiç gidemiyoruz"], k=["saat", "hızlı", "kısa sürede", "çabuk"])),
}
for q in Y.d["mebSorular"]:
    for i, z in enumerate(q.get("ikizler", [])):
        zid = z.get("id") or f"{q['id']}i{i + 1}"
        for m in z["maddeler"]:
            b = IKIZ.get((zid, m["harf"]))
            if b: m.update(b)
            else: raise SystemExit(f"ikiz verisi eksik: {zid} {m['harf']}")

# =====================================================================
# PUSULA'NIN CEVABINI DÜZELT: 8 eksik (yarım cevap) + 3 yanılgı (yalnız Hatırla'daki sık hatalardan)
# =====================================================================
def KH(kazanim, tur, soru, kuark, dogruSik, yanlis1, yanlis2, ipucu, aciklama, once, ornek, sonra, k, havuz):
    Y.kuark(kazanim=kazanim, tur=tur, soru=soru, kuark=kuark, secenekler=[dogruSik, yanlis1, yanlis2], dogru=0, ipucu=ipucu, aciklama=aciklama,
            dogruCevap=f"{once} {ornek} {sonra}".replace(" .", ".").replace(" !", "!").strip(), tamamla={"once": once, "ornek": ornek, "sonra": sonra, "k": k, "havuz": havuz})

TAM, DOGRU_ = "Tam, eksik yok.", "Doğru, hata yok."
KH(K1, "eksik", "Selim'in Ezel ile empati kurduğunu gösteren bir konuşma yazınız.", "Seni anlıyorum.",
   "Eksik: duygusu ve öneri yok; “İstersen …” ile bir öneri eklenmeli.", "Yanlış: “Sinemaya gel.” demeli.", TAM,
   "Empati cümlesinin üç parçası var: anlıyorum + duygusu + öneri.", "Empati kuran kişi duyguyu anlar ve bunu yansıtır; öneri cevabı tamamlar. (s. 18)",
   "Seni anlıyorum, yüksek ses seni rahatsız ediyor. İstersen", "parka gidelim", ".", ["gidelim", "yapalım", "birlikte", "dolaş", "oynayalım"], ["sen de gel artık", "sinema çok güzel"])
KH(K1, "eksik", "“Salonu dağınık bırakıyorsun.” cümlesini ben diline çeviriniz.", "Rahatsız oluyorum.",
   "Eksik: neden rahatsız olduğu (dağınık salon) yazılmamış.", "Yanlış: “Sen çok dağınıksın.” olmalı.", TAM,
   "Ben dili: durum + duygu.", "Ben dilinde hem durum hem duygu söylenir: “Salon dağınık olduğunda rahatsız oluyorum.” (s. 19)",
   "Salon", "dağınık olduğunda", "rahatsız oluyorum.", ["dağınık"], ["hep dağıtıyorsun", "temiz olduğunda"])
KH(K1, "eksik", "Arkadaşının “Senin yerinde olsaydım ben de üzülürdüm.” demesi hangi iletişim unsuruna örnektir? Neden?", "Empati.",
   "Eksik: “çünkü” ile gerekçe yazılmamış.", "Yanlış: ben dili olmalı.", TAM,
   "Soru “Neden?” de diyor.", "Empati: kendini karşındakinin yerine koyup duygusunu anlamak. (s. 18)",
   "Empati, çünkü kendini arkadaşının", "yerine koymuş", ".", ["yerine koy"], ["sözünü kesmiş", "onu suçlamış"])
KH(K2, "eksik", "Okullarda rampa ve asansör yapılması öğrencilere ne kazandırır? İki etki yazınız.", "Bağımsız olurlar.",
   "Eksik: iki etki istenmiş, biri yazılmış.", "Yanlış: başkasına bağımlı olurlar.", TAM,
   "Soru kaç şey istiyor?", "Fırsat eşitliği bireyin öz güvenini artırır, kendini değerli hissettirir. (s. 33)",
   "Bağımsız olurlar ve", "öz güvenleri artar", ".", ["güvenleri art", "güveni art", "değerli", "eşit"], ["yalnız kalırlar", "derse gelmezler"])
KH(K2, "eksik", "Parkların özel gereksinimli çocuklar için düzenlenmesine yönelik bir öneri yazınız.", "Yardım edilmeli.",
   "Eksik: öneri genel kalmış; ne yapılacağı somut yazılmalı.", "Yanlış: öneri değil slogan yazılmalı.", TAM,
   "Kim? Neye ihtiyacı var? Ne yapılmalı?", "Sosyal alanlarda uygun düzenlemeler (rampa, asansör gibi) yapılmalıdır. (s. 33)",
   "Tekerlekli sandalye kullanan çocuklar için parka", "rampa yapılmalı", ".", ["rampa", "asansör", "engelsiz"], ["çiçek dikilmeli", "kapı kilitlenmeli"])
KH(K3, "eksik", "Mustafa Kemal'in Samsun'a çıkmasında hangi gelişmeler etkili olmuştur?", "Anadolu işgal edildi.",
   "Eksik: savaştaki yenilgi ve Mondros yazılmamış.", "Yanlış: Cumhuriyet kurulduğu için çıktı.", TAM,
   "Kitap üç olay sayıyor.", "Birinci Dünya Savaşı'nda yenilgi → Mondros Ateşkes Antlaşması → işgal. (s. 45)",
   "Osmanlı Birinci Dünya Savaşı'nda yenildi,", "Mondros Ateşkes Antlaşması'nı imzaladı", "ve Anadolu işgal edildi.", ["mondros"], ["Tekâlif-i Millîye'yi yayımladı", "Kıbrıs Barış Harekâtı'nı yaptı"])
KH(K3, "eksik", "Anadolu halkının Millî Mücadele'ye yaklaşımı nasıl olmuştur?", "Halk destek verdi.",
   "Eksik: nasıl destek verdiği (imkânlarını orduyla paylaştı) yazılmamış.", "Yanlış: halk mücadeleye karşı çıktı.", TAM,
   "“Nasıl” sorusu ayrıntı ister.", "Halk birlik oldu; yiyecek, giyecek, araç ve gereçlerini orduyla paylaştı. (s. 45)",
   "Halk birlik oldu ve elindeki imkânları", "orduyla paylaştı", ".", ["paylaş"], ["sakladı", "sattı"])
KH(K4, "eksik", "Küreselleşmenin iletişime etkisine günlük yaşamdan bir örnek veriniz.", "Telefon.",
   "Eksik: değişim anlatılmamış; eskiden ve şimdi karşılaştırılmalı.", "Yanlış: örnek olarak mektup yazılmalı.", TAM,
   "Örnekte değişim görünmeli: eskiden … şimdi …", "Genel ağ ve mobil cihazlarla iletişim çok hızlandı. (s. 62)",
   "Eskiden mektup günler sürerdi; şimdi telefonla", "anında haberleşiyoruz", ".", ["anında", "hızlı", "saniye", "hemen"], ["hiç haberleşmiyoruz", "aylarca bekliyoruz"])
KH(K1, "yanilgi", "“Sürekli geç kalmandan bıktım!” cümlesini ben diline çeviriniz.", "Sen hep geç kalıyorsun, ben de üzülüyorum.",
   "Yanlış: hâlâ “sen” ile suçluyor; durum ve duygu söylenmeli.", "Yanlış: “bıktım” kelimesi eklenmeli.", DOGRU_,
   "Ben dilinde kişi suçlanır mı?", "Ben dili karşındakini suçlamadan duyguyu söyler. (s. 19)",
   "Suçlamadan söyle:", "geç kaldığında", "kendimi değersiz hissediyorum.", ["kaldığında", "kalındığında", "kalınca"], ["sen hep geç kalıyorsun", "hiç gelmiyorsun"])
KH(K2, "yanilgi", "Bir binada herkesin yalnız merdivenle girmesi fırsat eşitliği midir?", "Evet, çünkü herkese aynı şey yapılıyor.",
   "Yanlış: tekerlekli sandalye kullanan giremez; ihtiyaca göre rampa gerekir.", "Yanlış: kimse binaya girmemeli.", DOGRU_,
   "Tekerlekli sandalye kullanan biri girebilir mi?", "Fırsat eşitliği için binalarda rampa, asansör gibi uygun düzenlemeler yapılmalıdır. (s. 33)",
   "Hayır, çünkü tekerlekli sandalye kullanan giremez; binaya", "rampa", "yapılmalı.", ["rampa", "asansör"], ["çiçek", "merdiven"])
KH(K4, "yanilgi", "Küreselleşmenin iletişim alanındaki değişimine günlük yaşamdan bir örnek veriniz.", "Küreselleşme, dünyanın birbirine bağlanmasıdır.",
   "Yanlış: tanım yazılmış; soru günlük yaşamdan örnek istiyor.", "Yanlış: küreselleşmenin iletişimle ilgisi yoktur.", DOGRU_,
   "Soru tanım mı, örnek mi istiyor?", "Örnek: genel ağ sayesinde dünyanın öbür ucundaki arkadaşına saniyeler içinde “Merhaba” diyebilmek. (s. 58)",
   "Örnek: Yurt dışındaki teyzemle", "görüntülü konuşuyorum", ".", ["görüntülü", "telefon", "mesaj", "internet", "genel ağ"], ["mektup bekliyorum", "hiç konuşamıyorum"])

# =====================================================================
# PROVA YAZILILARI (2 deneme; Senaryo 5 dağılımı: 1 + 2 + 2 + 1 soru, toplam 100; puanlar tahmini). Bağlamlar MEB ve benzerlerinden farklı.
# =====================================================================
Y.prova(id="p1", ad="Prova 1", sorular=[
    {"kazanim": K1, "puan": 16, "benzer": "m2", "metin": ["Aşağıdaki cümleler “sen dili” ile kurulmuştur."],
     "maddeler": [M("a", "“Odamı hep dağıtıyorsun, hiç dikkat etmiyorsun!” cümlesini “ben dili”ne çeviriniz.", "Odam dağınık kaldığında rahatsız oluyorum. Eşyalarımı yerinde bulmak istiyorum.",
                    [A("Durumu anlatır", "dağınık", "dağıldığında"), A("Duygusunu söyler", *DUYGU_BEN)], "bendili", puan=8),
                  M("b", "“Müziğin sesini sürekli açıyorsun, çok bencilsin!” cümlesini “ben dili”ne çeviriniz.", "Müziğin sesi yüksek olduğunda dersime odaklanmakta zorlanıyorum.",
                    [A("Durumu anlatır", "yüksek", "ses"), A("Duygusunu söyler", *DUYGU_BEN)], "bendili", puan=8)]},
    {"kazanim": K2, "puan": 16, "benzer": "m3", "metin": ["Belediye, otobüs duraklarında ve kaldırımlarda görme ve bedensel yetersizliği olan bireyler için düzenlemeler yapmak istiyor. Halkı bilinçlendirmek için bir kampanya hazırlanacak."],
     "maddeler": [M("a", "Kampanya için amacınıza uygun bir slogan yazınız.", "Yollar herkesin, engelsiz şehir hepimizin!",
                    [A("Konuya uygun (yol, şehir, durak)", "yol", "şehir", "durak", "ulaşım", "kaldırım", "otobüs"), A("Herkesi kapsayan olumlu söz", *KAPSA)], "slogan", puan=16)]},
    {"kazanim": K2, "puan": 16, "benzer": "m3", "metin": ["Görme yetersizliği olan Cem, kaldırım üzerindeki kabartmalı sarı şeridi bastonuyla takip ederek durağa güvenli biçimde ulaşır."],
     "maddeler": [M("a", "Bu düzenleme Cem'in yaşamında hangi amaca hizmet etmektedir?", "Cem'in kimseye ihtiyaç duymadan bağımsız ve güvenli şekilde hareket etmesini sağlar; günlük yaşamını kolaylaştırır.",
                    [A("Bağımsız, güvenli hareket", "bağımsız", "güvenli", "güvenle", "kendi başına"), A("Günlük yaşamı kolaylaştırır, fırsat eşitliği", "kolaylaş", "fırsat eşitliği", "eşit")], "oneri", puan=8),
                  M("b", "Özel gereksinimli bireyler için fırsat eşitliğini sağlamaya yönelik bir öneri daha yazınız.", "Otobüslere rampa yapılmalı ve duraklarda sesli anons sistemi kurulmalıdır.",
                    [A("Somut düzenleme", "rampa", "asansör", "sesli", "işaret dili", "şerit", "engelsiz", "kabartma"), A("Ne yapılmalı", *YAP)], "oneri", puan=8)]},
    {"kazanim": K3, "puan": 18, "benzer": "m4", "metin": ["Millî Mücadele yıllarında Anadolu halkı, Tekâlif-i Millîye Emirleri kapsamında ordunun ihtiyaçlarını karşılamak için büyük bir çaba göstermiştir."],
     "maddeler": [M("a", "Halk orduya hangi yollarla destek olmuştur?", "Elindeki yiyecek, giyecek, araç ve gereçleri orduyla paylaşmıştır.",
                    [A("Yiyecek, giyecek", "yiyecek", "giyecek", "erzak"), A("Araç gereç paylaştı", "araç", "paylaş")], "tutum", puan=9),
                  M("b", "Bu davranış Türk toplumunun hangi özelliğini gösterir?", "Fedakârlık, dayanışma ve birlik özelliğini gösterir.",
                    [A("Fedakârlık", "fedakâr", "vatansever"), A("Dayanışma, birlik", "dayanışma", "birlik", "yardımlaş")], "tutum", puan=9)]},
    {"kazanim": K3, "puan": 18, "benzer": "m4", "metin": ["6 Şubat 2023'te Kahramanmaraş merkezli büyük depremler meydana gelmiştir. Ülkenin birçok yerinden bölgeye gıda, su ve giysi gönderilmiş; kamu kurumları, sivil toplum kuruluşları ve vatandaşlar birlikte çalışmıştır."],
     "maddeler": [M("a", "Depremden sonra yapılan iki yardım çalışmasını yazınız.", "Arama-kurtarma ekipleri gönderildi; çadır kentler ve konteyner kentler kuruldu.",
                    [A("Arama-kurtarma, sağlık", "arama", "kurtarma", "sağlık", "sahra"), A("Barınma, gıda", "çadır", "konteyner", "gıda", "giysi")], "tutum", puan=8),
                  M("b", "Bu olay Türk toplumunun millî meseleler karşısındaki hangi tutumunu gösterir?", "Tüm Türkiye tek yürek olmuş; yardımlaşma ve dayanışma göstermiştir.",
                    [A("Tek yürek, birlik", "tek yürek", "birlik", "kenetlen"), A("Yardımlaşma, dayanışma", "yardımlaş", "dayanışma")], "tutum", puan=10)]},
    {"kazanim": K4, "puan": 16, "benzer": "m5", "metin": ["Küreselleşme, alışveriş ve ticaret alanında da önemli değişimlere yol açmıştır."],
     "maddeler": [M("a", "Bu değişime günlük yaşamdan bir örnek veriniz.", "Eskiden başka ülkenin ürününü almak çok zordu. Şimdi e-ticaret sayesinde evden çıkmadan başka ülkelerden alışveriş yapabiliyoruz.",
                    [A("E-ticaret, genel ağ", "e-ticaret", "internet", "genel ağ", "çevrim içi", "online", "uygulama"), A("Kolaylık: evden, başka ülkeden", "evden", "başka ülke", "kolay", "hızlı", "yurt dışı")], "ornek", puan=16)]}])

Y.prova(id="p2", ad="Prova 2", sorular=[
    {"kazanim": K1, "puan": 16, "benzer": "m1", "metin": ["Yağmur, sınıf gezisine katılmak istemiştir. Arkadaşı Mert ise otobüste midesi bulandığı için geziye gelmek istemediğini söylemiştir."],
     "maddeler": [M("a", "Yağmur'un Mert ile empati kurduğunu gösteren bir konuşma metni yazınız.", "Seni anlıyorum Mert, otobüste kendini kötü hissediyorsun. İstersen öğretmenimizle konuşalım, ön koltukta birlikte otururuz.",
                    [A("Onu anladığını söyler", *ANLA), A("Duygusunu fark eder", "kötü", "rahatsız", "bulan"), A("Öneri sunar", "istersen", "konuşalım", "otururuz", "birlikte", "yapalım")], "empati", puan=16)]},
    {"kazanim": K2, "puan": 16, "benzer": "m3", "metin": ["Okulunuzda “Herkes İçin Spor” adlı bir şenlik düzenlenecek. Şenliğe özel gereksinimli öğrencilerin de katılması isteniyor."],
     "maddeler": [M("a", "Şenlik afişi için amacınıza uygun bir slogan yazınız.", "Spor herkesin, engelleri birlikte aşalım!",
                    [A("Konuya uygun (spor, şenlik)", "spor", "şenlik", "oyun", "koş", "maç", "yarış"), A("Herkesi kapsayan olumlu söz", *KAPSA)], "slogan", puan=16)]},
    {"kazanim": K2, "puan": 16, "benzer": "m3", "metin": ["Bir belediye, hizmet binasında yalnızca merdiven kullanmakta ve “Herkes aynı kapıdan girecek.” demektedir."],
     "maddeler": [M("a", "Bu durum tekerlekli sandalye kullanan bir vatandaşı nasıl etkiler?", "Binaya giremez, hizmetten yararlanamaz; fırsat eşitliği sağlanmamış olur.",
                    [A("Giremez, yararlanamaz", "giremez", "yararlanamaz", "ulaşamaz", "çıkamaz"), A("Fırsat eşitliği yok", "fırsat eşitliği", "eşit değil", "haksız")], "oneri", puan=8),
                  M("b", "Bu sorunun çözümü için bir öneri yazınız.", "Binaya rampa ve asansör yapılmalıdır.",
                    [A("Somut düzenleme", "rampa", "asansör"), A("Ne yapılmalı", *YAP)], "oneri", puan=8)]},
    {"kazanim": K3, "puan": 18, "benzer": "m4", "metin": ["1919 yılında Anadolu'nun çeşitli bölgeleri işgal altındayken Mustafa Kemal Samsun'a çıkarak halkın bağımsızlık umudunu güçlendirmeye ve milleti ortak bir mücadele etrafında toplamaya başlamıştır."],
     "maddeler": [M("a", "Mustafa Kemal'in Samsun'a çıkış tarihini yazınız. Bu gelişmenin Türk tarihi açısından önemi nedir?", "19 Mayıs 1919. Millî Mücadele başlamış, Türk milletine umut olmuştur; mücadelenin sonunda Türkiye Cumhuriyeti kurulmuştur.",
                    [A("19 Mayıs 1919", "19 mayıs", "1919"), A("Millî Mücadele başladı, umut oldu", "millî mücadele", "umut", "başla")], "neden", puan=9),
                  M("b", "Anadolu'nun işgal edilmesine yol açan antlaşmanın adı nedir? Bu antlaşma hangi savaştan sonra imzalanmıştır?", "Mondros Ateşkes Antlaşması; Birinci Dünya Savaşı'ndan sonra imzalanmıştır.",
                    [A("Mondros", "mondros"), A("Birinci Dünya Savaşı", "birinci dünya", "1. dünya", "i. dünya")], "neden", puan=9)]},
    {"kazanim": K3, "puan": 18, "benzer": "m4", "metin": ["Millî yüzücü Defne Kurt, 2025 yılında Dünya Para Yüzme Şampiyonası'nda 5 altın madalya kazanarak Türk spor tarihine geçmiştir."],
     "maddeler": [M("a", "Bu başarı toplumda hangi ortak duyguları güçlendirir?", "Gurur, sevinç, birlik ve millî aidiyet duygularını güçlendirir.",
                    [A("Gurur, sevinç", "gurur", "sevinç", "mutlu"), A("Birlik, aidiyet", "birlik", "aidiyet", "beraber", "vatan sevgisi")], "tutum", puan=9),
                  M("b", "Bilim alanındaki bir millî başarıya örnek veriniz.", "Aziz Sancar'ın DNA onarımı çalışmalarıyla Nobel Kimya Ödülü kazanması ya da Alper Gezeravcı'nın uzaya gitmesi.",
                    [A("Bilimde millî başarı", "aziz sancar", "nobel", "gezeravcı", "uzay")], "tutum", puan=9)]},
    {"kazanim": K4, "puan": 16, "benzer": "m5", "metin": ["Bir kasabada gençler genel ağ sayesinde dünyanın farklı yerlerindeki müzikleri, yemekleri ve giyim tarzlarını yakından takip etmeye başlar. Zamanla kasabanın bazı geleneksel ürünlerine ve yerel etkinliklerine ilgi azalır."],
     "maddeler": [M("a", "Bu hikâyeden hareketle küreselleşmenin kültür alanındaki bir olumlu ve bir olumsuz etkisini yazınız.",
                    "Olumlu: Farklı kültürleri tanırlar, kültürel etkileşim artar. Olumsuz: Yerel kültür ve geleneklere ilgi azalır, yerel kültür zayıflar.",
                    [A("Olumlu: farklı kültürleri tanıma", "tanı", "etkileşim", "öğren"), A("Olumsuz: yerel kültür zayıflar", "yerel", "gelenek", "zayıfla", "azal", "unutul")], "olumlu", puan=16)]}])

Y.yaz()
