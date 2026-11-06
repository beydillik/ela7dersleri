"""Türkçe 7 · 1. Dönem 1. Yazılı — Yazılıya Hazırlık verisi.
Kapsam: MEB senaryo tablosu, Senaryo 5 (okulun seçtiği): T.O.7.4 (1), T.O.7.5 (2), T.O.7.21 (1), T.Y.7.3 (1), T.Y.7.21 (1) = 6 soru.
Kaynaklar: MEB TEGM "Yazılıya Hazırlanıyorum 7. Sınıf Türkçe 1. Dönem 1. Yazılı" (10 soru, çözümleriyle; bütün senaryoları kapsıyor).
  MEB "öğrenme çıktısı – soru no": 7.21 → 1 · 7.5 → 2 · 7.7 → 3 · Y.7.18 → 4 · 7.8 → 5 · 7.4 → 6 · 7.14 → 7 · 7.15 → 8 · Y.7.21 → 9 · Y.7.3 → 10.
  Senaryo 5'e girenler: 1, 2, 6, 9, 10. Hariç: 3, 4 (sınırda), 5, 7 (sınırda), 8 (Kemal onayı, 6 Kasım 2026).
  T.O.7.5'in senaryodaki 2. sorusu için MEB'de soru yok: benzer sorular ve provalarda ana düşünce / metindeki bilgiyi bulma.
Ders kitabı ve defter konuları (sayfa atıflı): u1k1 (s. 12, 32), u1k3 (s. 17, 22), u1k4 (s. 49), u1k5 (s. 34–35), u3k3 (s. 167).
yazilihocam.com 7. sınıf Türkçe 1. dönem 1. yazılı örnekleri (siyah, kırmızı, mavi): benzer soru ve provalarda, kimi birebir.
Öncelik (Kemal: banko soruya daha çok emek): m9, m2 ★★★ Banko; m1, m6 ★★ Puan topla; m10 ★ Bir adım yaz.
Çalıştır: python3 araclar/yazili/tr1_d1y1.py"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from yazili import Yazili
import cizim_tr as Z


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

K1, K2, K3, K4, K5 = "T.O.7.21", "T.O.7.5", "T.O.7.4", "T.Y.7.21", "T.Y.7.3"

Y = Yazili("tr1", "d1y1",
    baslik="1. Dönem 1. Yazılı", ders="Türkçe", senaryo="Senaryo 5", sure=40, tarih="2026-11-10",
    dagilim={K1: 1, K2: 2, K3: 1, K4: 1, K5: 1},
    mebToplam=10,
    mebHaric=[{"no": 3, "kazanim": "T.O.7.7", "ad": "Metnin derin anlamını belirlemeye yönelik basit çıkarımlar yapabilme"},
              {"no": 4, "kazanim": "T.Y.7.18", "ad": "Yazısını zenginleştirecek biçimde söz varlığını kullanabilme", "sinir": True},
              {"no": 5, "kazanim": "T.O.7.8", "ad": "Metnin derin anlamını belirlemeye yönelik üst düzey çıkarımlar yapabilme"},
              {"no": 7, "kazanim": "T.O.7.14", "ad": "Bilgilendirici metinlerde metin yapılarından hareketle önemli bilgileri belirleme", "sinir": True},
              {"no": 8, "kazanim": "T.O.7.15", "ad": "Bilgilendirici metinde anahtar kelimeleri belirleme"}],
    giris="Okulun seçtiği senaryoda <b>6 soru</b> var: kelimenin anlamı 2, metnin konusu ve ana düşüncesi 2, yazım-noktalama 1, taslak ve metin yazma 1. "
          "Önce <b>★★★ Banko</b> soruları sağlamla: <b>ikilemeler ayrı ve çizgisiz</b>, noktalı virgülün ve üç noktanın <b>amacı</b>, konunun <b>kısa</b> yazılışı. "
          "Kelime sorularında <b>tahmin + metinden gerekçe</b> yeter; metin yazma sorusunda en azından <b>Giriş – Gelişme – Sonuç</b> taslağını yaz.",
    kapsamDisi=["Metinden çıkarım yapma (gizli anlam, örtük mesaj) — MEB örneğinin 3. ve 5. soruları",
                "Verilen ifadelerle metni tamamlama ve benzetme kullanma — MEB 4. soru",
                "Metin yapısından önemli bilgiyi bulma ve anahtar kelime — MEB 7. ve 8. sorular"],
    puanNotu="Puanlar tahminidir: okul soruların puanını farklı dağıtabilir. Toplam 100. Provalarda senaryodaki gibi 6 soru var; "
             "T.O.7.5'in ikinci sorusu MEB örneğinde yok, ana düşünce ya da metindeki bilgiyi bulma olacağını tahmin ediyoruz.",
    kaynakNotu="Sorular MEB'in yayımladığı 'Yazılıya Hazırlanıyorum 7. Sınıf Türkçe 1. Dönem 1. Yazılı' örneklerine, ders kitabına ve yazilihocam.com yazılı örneklerine dayanır. "
               "“Forsa” parçası MEB dokümanındaki Ömer Seyfettin alıntısıdır.",
    soruGiris="Bunlar MEB'in örnek soruları; yazılıda <b>benzerleri</b> çıkacak. <b>★★★ Banko</b> olanlarla başla. Cevabı kısa ve kalıba uygun yaz.",
    kazanimAd="konu")

# =====================================================================
# KONULAR (Hatırla kartları + Hatırla ve Tekrarla boşlukları)
# =====================================================================
Y.kazanim(kod=K1, ad="Metinden hareketle söz varlığını geliştirmeye yönelik çözümleme yapabilme", kisa="Kelimenin Anlamını Metinden Bulma", soru=1, renk="#1971c2",
    konular=["u1k1", "u2k1"], sayfa="s. 12, 16, 32", svg=Z.h_anlam(),
    maddeler=["<b>Bağlam</b>: bir kelimenin çevresindeki cümleler. Bilmediğin kelimenin anlamını çoğu zaman bağlam söyler. (s. 12)",
              "Önce <b>tahmin et</b>, sonra sözlükle kontrol et. Sınavda sözlük yok: tahminin de puan alır, <b>boş bırakma</b>. (s. 32)",
              "Bir kelimenin birden çok anlamı olabilir; <b>metindeki anlamını cümle seçer</b>: “ağır kutu” (kütlesi fazla) ≠ “ağır eleştiri” (kırıcı). (s. 16)",
              "Yol: kelimenin geçtiği cümleyi oku → yanındaki <b>ipucu kelimeleri</b> bul → anlamı <b>başka kelimelerle</b> yaz. HÜRKUŞ: “eğitim ve <b>keşif</b> görevleri” → keşif = bir yeri inceleyip bilgi toplama. (MEB örnek sorusu)",
              "Cevap kalıbı: <b>“kelime: … demek / … anlamında”</b>. Kelimeyi tekrar etme (“keşif: keşfetmek” olmaz).",
              "Ters soru da çıkar: <b>anlamı verilir, kelimeyi metinden bulursun</b>. Anlamı oku, metinde ona uyan kelimeyi ara, aynen yaz."],
    kelimeler=["bağlam", "ipucu kelime", "… demek", "başka kelimelerle açıkla", "metindeki anlam", "boş bırakma"],
    hatalar=[{"yanlis": "Kelimeyi tekrar etmek: “keşif: keşfetmek.”", "dogru": "Başka kelimelerle açıkla: “bir yeri inceleyip bilgi toplamak.”"},
             {"yanlis": "Metne bakmadan aklına gelen anlamı yazmak.", "dogru": "Kelimenin çevresindeki cümleye bak: “eğitim ve keşif görevleri.”"},
             {"yanlis": "Emin olmadığı maddeyi boş bırakmak.", "dogru": "Tahminini yaz; yakın bir anlam da puan getirir."}],
    tekrar=[{"c": "Bir kelimenin çevresindeki cümlelere {bağlam|ana fikir|başlık} denir.", "s": "s. 12"},
            {"c": "Bilmediğin kelimenin anlamını önce {bağlamdan tahmin et|hiç yazma}.", "s": "s. 32"},
            {"c": "Bir kelimenin metindeki anlamını {cümle|kelimenin uzunluğu} seçer.", "s": "s. 16"},
            {"c": "“İşçiler ağır kutuları taşıdı.” cümlesinde ağır, {kütlesi fazla|kırıcı} demektir.", "s": "yazilihocam örneği"},
            {"c": "HÜRKUŞ'taki “teçhizat”, görev için gereken {araç gereçlerdir|pilotun adıdır}.", "s": "MEB örnek sorusu"},
            {"c": "Anlamı yazarken kelimeyi {tekrar etme|aynen tekrar et}, başka kelimelerle açıkla.", "s": "cevap kalıbı"},
            {"c": "Emin olmasan da {tahminini yaz|maddeyi boş bırak}.", "s": "cevap kalıbı"}])

Y.kazanim(kod=K2, ad="Metnin yüzey anlamını belirleyebilme", kisa="Metnin Konusu ve Ana Düşüncesi", soru=2, renk="#e67700",
    konular=["u1k3"], sayfa="s. 17, 22", svg=Z.h_konu(),
    maddeler=["<b>Konu</b>: metinde <b>neyin anlatıldığı</b>. “Bu metin neyi anlatıyor?” sorusunun cevabı; <b>kısa</b> yazılır. (s. 22)",
              "Konuyu bulmak için ipuçları: <b>başlık</b> ve metinde <b>sık geçen kelimeler</b>. Arılar metninde “arı” her cümlede geçiyor. (s. 22)",
              "Konu kalıbı: <b>“… -ın/-in … önemi / … etkileri / … görevleri”</b>. Örnek: “Arıların doğadaki önemi.” (MEB örnek sorusu)",
              "<b>Ana düşünce</b>: yazarın asıl söylemek istediği; <b>bir cümle</b>dir, çoğu zaman ders verir: “Arıları korumalıyız.” (s. 17)",
              "Ana düşünce çoğu zaman metnin <b>sonunda</b>, “bu nedenle, bu yüzden, asıl önemli olan” sözlerinin ardındadır.",
              "Metinde yazan bilgi soruları (ne zaman, nerede, ne amaçla): cevap <b>metinde açıkça yazar</b>; o cümleyi bul, kısaca yaz."],
    kelimeler=["neyi anlatıyor?", "kısa: … önemi", "sık geçen kelime", "bir cümle", "-malıyız", "bu nedenle …"],
    hatalar=[{"yanlis": "Konu sorusuna uzun ders cümlesi yazmak: “Arıları korumalıyız.”", "dogru": "Konu kısa yazılır: “Arıların doğadaki önemi.”"},
             {"yanlis": "Konuya yalnız tek kelime yazmak: “Arılar.”", "dogru": "Arılar hakkında ne anlatılıyor? “Arıların doğadaki önemi.”"},
             {"yanlis": "Ana düşünce sorusuna konuyu yazmak: “Dil.”", "dogru": "Ana düşünce bir cümledir: “Dilimize sahip çıkmalıyız.”"}],
    tekrar=[{"c": "Konu, metinde {neyin anlatıldığıdır|yazarın adıdır}.", "s": "s. 22"},
            {"c": "Konu {kısa|çok uzun} yazılır: “Arıların doğadaki önemi.”", "s": "s. 22"},
            {"c": "Konuyu bulmak için metinde {sık geçen kelimelere|en uzun kelimeye} bakarız.", "s": "s. 22"},
            {"c": "Ana düşünce, yazarın {asıl söylemek istediği|ilk yazdığı} düşüncedir.", "s": "s. 17"},
            {"c": "Ana düşünce {bir cümledir|tek kelimedir}.", "s": "s. 17"},
            {"c": "“Arıları korumalıyız.” cümlesi {ana düşüncedir|konudur}.", "s": "MEB örnek sorusu"},
            {"c": "Ana düşünce çoğu zaman “{bu nedenle|bir varmış bir yokmuş}” gibi sözlerin ardındadır.", "s": "cevap kalıbı"}])

Y.kazanim(kod=K3, ad="Metinde geçen anlamını bilmediği söz varlığı unsurlarının anlamını tahmin edebilme", kisa="Anlam Tahmini ve Gerekçesi", soru=1, renk="#2f9e44",
    konular=["u1k1", "u3k2"], sayfa="s. 12, 32", svg=Z.h_tahmin(),
    maddeler=["Bu soru <b>iki parça</b> ister: 1) kelimenin anlamına dair <b>tahminin</b>, 2) seni bu tahmine götüren <b>metin içi gerekçe</b>. (MEB örnek sorusu)",
              "<b>Gerekçe = metindeki ipucu ifade.</b> Kendi fikrini değil, metinden bir parçayı <b>tırnak içinde</b> yaz: “kolları eski kuvvetini kaybetmiş”.",
              "İpucu çoğu zaman kelimenin <b>hemen yanındaki</b> cümlelerdedir: “bitap düşmüştü. Kolları eski kuvvetini kaybetmiş…” (MEB örnek sorusu; s. 12)",
              "Forsa: <b>bitap</b> = yorgun, güçsüz · <b>iştiyak</b> = özlem, çok isteme · <b>teselli</b> = avuntu, acıyı hafifleten şey. (MEB örnek sorusu)",
              "Deyim de sorulabilir: “burun kıvırmak” = beğenmemek, küçümsemek. Olaya bak: arkadaşları Ege'yi <b>tanımadan</b> yetersiz sanmış. (yazilihocam örneği)",
              "Cevap kalıbı: <b>“Anlamı: … Gerekçe: Metinde ‘…’ yazıyor.”</b>"],
    kelimeler=["tahminim", "gerekçem", "metinde ‘…’ yazıyor", "tırnak içinde", "yanındaki cümle", "kendi fikrin değil"],
    hatalar=[{"yanlis": "Gerekçeye kendi fikrini yazmak: “Bence yaşlılar yorulur.”", "dogru": "Metinden ipucu yaz: “kolları eski kuvvetini kaybetmiş.”"},
             {"yanlis": "Yalnız tahmini yazıp gerekçeyi unutmak.", "dogru": "İki parça yaz: tahmin + metinden gerekçe."},
             {"yanlis": "Kelimenin sözlükteki başka bir anlamını yazmak.", "dogru": "Metindeki anlamı yaz; anlamı cümle seçer."}],
    tekrar=[{"c": "Bu soru tahmin ve {gerekçe|başlık} ister.", "s": "MEB örnek sorusu"},
            {"c": "Gerekçe {metindeki ipucu ifadedir|kendi düşüncemdir}.", "s": "MEB örnek sorusu"},
            {"c": "Metinden aldığın gerekçeyi {tırnak içinde|soru işaretiyle} yaz.", "s": "cevap kalıbı"},
            {"c": "Forsa'da “bitap” kelimesi {yorgun, güçsüz|neşeli, güçlü} demektir.", "s": "MEB örnek sorusu"},
            {"c": "“İştiyakla yanıp tutuşurdu” sözündeki iştiyak {özlem|korku} anlamındadır.", "s": "MEB örnek sorusu"},
            {"c": "Dalga sesleri ona teselli verir, acısını {unuttururdu|artırırdı}.", "s": "MEB örnek sorusu"},
            {"c": "İpucu çoğu zaman kelimenin {hemen yanındaki cümlelerdedir|metnin başlığındadır}.", "s": "s. 12"}])

Y.kazanim(kod=K4, ad="Yazım kuralları ve noktalama işaretlerini uygulayabilme", kisa="İkilemeler, Noktalı Virgül, Üç Nokta", soru=1, renk="#c92a2a",
    konular=["u1k4", "u1k5"], sayfa="s. 34–35, 49", svg=Z.h_yazim(),
    maddeler=["<b>İkilemeler ayrı yazılır</b>, arasına <b>kısa çizgi ya da virgül konmaz</b>: apar topar, hızlı hızlı, teker teker, irili ufaklı. (s. 34)",
              "Noktalı virgül 1: ikiden fazla eş değer öge arasında virgül olan cümlede <b>özneden sonra</b> konabilir: “Genç şairimiz<b>;</b> Necip Fazıl, Nâzım Hikmet ve Attilâ İlhan…” (s. 49)",
              "Noktalı virgül 2: ögeleri arasında virgül bulunan <b>sıralı cümleleri ayırır</b>: “… güçlendirir, aktarır<b>;</b> … önem vermeyen toplumlar ise …” (s. 49)",
              "Noktalı virgül 3: virgüllerle ayrılmış <b>tür ve takımları</b> (grupları) ayırır: “Ece su, sandviç<b>;</b> Kerem şapka, gözlük aldı.” (s. 49)",
              "<b>Üç nokta</b>: tamamlanmamış cümlenin sonunda (sözün gerisi okura bırakılır), eksik bırakılan cevapta ve seslenmeyi pekiştirmede kullanılır. (s. 35)",
              "Cevap kalıbı: <b>işaret + amaç</b> → “Noktalı virgül; özneden sonra konur.” Yalnız işareti yazmak yarım puan getirir."],
    kelimeler=["ayrı, çizgisiz", "özneden sonra ;", "virgüllü sıralı cümleler ;", "virgüllü gruplar ;", "cümle yarım kaldı …", "işaret + amaç"],
    hatalar=[{"yanlis": "İkilemenin arasına kısa çizgi koymak: “teker-teker.”", "dogru": "Ayrı ve çizgisiz yaz: “teker teker.”"},
             {"yanlis": "İkilemeyi bitişik yazmak ya da araya virgül koymak: “koşakoşa”, “irili, ufaklı.”", "dogru": "“koşa koşa”, “irili ufaklı.”"},
             {"yanlis": "Yalnız işareti yazıp amacını yazmamak.", "dogru": "İşaret + amaç: “Noktalı virgül; özneden sonra konur.”"}],
    tekrar=[{"c": "İkilemeler {ayrı|bitişik} yazılır.", "s": "s. 34"},
            {"c": "İkilemelerin arasına {hiçbir işaret|kısa çizgi} konmaz: apar topar.", "s": "s. 34"},
            {"c": "“Genç şairimiz ( ) Necip Fazıl, Nâzım Hikmet…” cümlesinde boşluğa {noktalı virgül|üç nokta} gelir.", "s": "s. 49"},
            {"c": "Bu noktalı virgül {özneden sonra|cümle sonunda} konmuştur.", "s": "s. 49"},
            {"c": "Ögeleri arasında virgül bulunan {sıralı cümleleri|kelimenin hecelerini} noktalı virgül ayırır.", "s": "s. 49"},
            {"c": "Tamamlanmamış, yarım bırakılan cümlenin sonuna {üç nokta|noktalı virgül} konur.", "s": "s. 35"},
            {"c": "Noktalama sorusunda işaretin adını ve {amacını|rengini} yaz.", "s": "cevap kalıbı"}])

Y.kazanim(kod=K5, ad="Yazısında içerik ve yapıya yönelik seçimlerini yönetebilme", kisa="Taslak ve Bilgilendirici Metin", soru=1, renk="#7048e8",
    konular=["u3k3"], sayfa="s. 167", svg=Z.h_taslak(),
    maddeler=["Bilgilendirici metnin üç bölümü: <b>giriş, gelişme, sonuç</b>. (s. 167)",
              "<b>Giriş</b> konuyu tanıtır: “Doğa, nefes aldığımız hava ve içtiğimiz sudur.” <b>Gelişme</b> açıklar ve örnek verir. <b>Sonuç</b> toparlar, ana düşünceyi vurgular. (s. 167)",
              "<b>Taslak</b> = metni yazmadan önceki plan. Üç satır yeter: <b>“Giriş: … Gelişme: … Sonuç: …”</b> (MEB örnek sorusu)",
              "Doğa sevgisi taslağı: Giriş: doğanın hayatımızdaki önemi · Gelişme: doğayı korumak için yapılacaklar (geri dönüşüm, fidan) · Sonuç: doğayı korumak hepimizin görevi. (MEB örnek sorusu)",
              "Metni taslağa göre yaz: <b>her bölüme 1–2 cümle</b>. Sonucu “<b>Sonuç olarak …</b>” diye başlat. Örneği “<b>Örneğin …</b>” ile ver. (s. 167)",
              "Metin yapısı seçme sorusu da çıkabilir: iki şeyin benzer ve farklı yönleri anlatılacaksa <b>karşılaştırma-zıtlık</b> yapısı uygundur. (yazilihocam örneği)"],
    kelimeler=["Giriş: konuyu tanıt", "Gelişme: açıkla, örnek ver", "Sonuç: toparla", "Sonuç olarak …", "Örneğin …", "her bölüme 1–2 cümle"],
    hatalar=[{"yanlis": "Taslak istenince doğrudan uzun metin yazmak.", "dogru": "Önce üç satırlık taslak: Giriş: … Gelişme: … Sonuç: …"},
             {"yanlis": "Sonuç bölümünü unutmak.", "dogru": "“Sonuç olarak …” diye toparla."},
             {"yanlis": "Konudan çıkmak (doğa yerine tatil anısı yazmak).", "dogru": "Her bölüm verilen tema hakkında olsun."}],
    tekrar=[{"c": "Bilgilendirici metnin üç bölümü giriş, gelişme ve {sonuçtur|başlıktır}.", "s": "s. 167"},
            {"c": "Giriş bölümü {konuyu tanıtır|metni bitirir}.", "s": "s. 167"},
            {"c": "Gelişme bölümünde konu açıklanır ve {örnekler verilir|metin kapanır}.", "s": "s. 167"},
            {"c": "Sonuç bölümü anlatılanları {toparlar|ilk kez tanıtır}.", "s": "s. 167"},
            {"c": "Sonuç bölümü çoğu zaman “{Sonuç olarak|Bir gün}” diye başlar.", "s": "s. 167"},
            {"c": "Taslak, metni {yazmadan önceki plandır|bitirdikten sonraki puandır}.", "s": "MEB örnek sorusu"},
            {"c": "Metni yazarken taslaktaki her bölüme {1–2 cümle|tek kelime} yazarız.", "s": "cevap kalıbı"}])

# =====================================================================
# CEVAP KALIPLARI (Özet'te liste; sorunun içinde tek satır kalıp notu)
# =====================================================================
Y.formul(id="anlam", ad="Kelimenin anlamı", kalip="kelime: … demek (başka kelimelerle)", ne="“Anlamını metinden hareketle tahmin ediniz” sorularında", ornek="Keşif: bir yeri inceleyip bilgi toplamak.")
Y.formul(id="bul", ad="Anlamdan kelimeyi bul", kalip="Anlamı oku → metinde ona uyan kelimeyi aynen yaz", ne="“Anlamı verilen kelimeyi metinden bulunuz” sorularında", ornek="Yeryüzüne çıkan erimiş kaya: lav.")
Y.formul(id="gerekce", ad="Tahmin + gerekçe", kalip="Anlamı: … · Gerekçe: Metinde ‘…’ yazıyor.", ne="“Tahminlerinizi ve gerekçelerinizi yazınız” sorularında", ornek="Bitap: yorgun. Gerekçe: Metinde ‘kolları eski kuvvetini kaybetmiş’ yazıyor.")
Y.formul(id="konu", ad="Konu", kalip="Metin neyi anlatıyor? → kısa: “… -ın … önemi / etkileri”", ne="“Metnin konusunu yazınız” sorularında", ornek="Arıların doğadaki önemi.")
Y.formul(id="ana", ad="Ana düşünce", kalip="Yazar ne demek istiyor? → bir cümle: “… -malıyız / … önemlidir.”", ne="“Ana düşüncesini yazınız”, “asıl anlatılmak istenen” sorularında", ornek="Dilimize sahip çıkmalıyız, çünkü dil kimliğimizdir.")
Y.formul(id="bilgi", ad="Metinde yazan bilgi", kalip="Soru kelimesi (ne zaman, nerede, ne amaçla) → metindeki cümleyi bul, kısaca yaz", ne="Metinde açıkça yazan bilgiyi soran sorularda", ornek="6 Nisan Cumartesi günü açıldı.")
Y.formul(id="ikileme", ad="İkilemenin yazımı", kalip="İki kelime ayrı + arada çizgi ya da virgül yok", ne="“Yazım yanlışı yapılmış ikilemeleri düzeltiniz” sorularında", ornek="apar topar, hızlı hızlı")
Y.formul(id="isaret", ad="İşaret + amaç", kalip="İşaretin adı + amacı (özneden sonra / sıralı cümleleri ayırır / cümle yarım kaldı)", ne="“Uygun işareti getiriniz, kullanım amacını belirtiniz” sorularında", ornek="Noktalı virgül; özneden sonra konur.")
Y.formul(id="taslak", ad="Taslak", kalip="Giriş: … · Gelişme: … · Sonuç: …", ne="“Taslak hâlinde yazınız” sorularında", ornek="Giriş: doğanın önemi. Gelişme: korumak için yapılacaklar. Sonuç: hepimizin görevi.")
Y.formul(id="metin", ad="Taslağa uygun metin", kalip="Her bölüme 1–2 cümle; “Örneğin …”, “Sonuç olarak …”", ne="“Taslağa uygun bir metin yazınız” sorularında", ornek="Doğa hayatımız için önemlidir. Örneğin fidan dikebiliriz. Sonuç olarak doğayı korumak hepimizin görevidir.")
Y.formul(id="yapi", ad="Metin yapısı seçme", kalip="Benzer + farklı yön → karşılaştırma-zıtlık; olay sırası → sıralı-kronolojik", ne="“Amacınıza uygun metin yapısını belirleyiniz” sorularında", ornek="Karşılaştırma-zıtlık: ikisi de …; oysa biri …, diğeri …")

# ortak anahtar kökleri
KONU_DEGER = ["önem", "görev", "rol", "katkı", "fayda", "yarar"]
GIRIS = ["önem", "hayat", "yaşam", "nefes", "yuva", "değer"]
KORU = ["geri dönüşüm", "fidan", "ağaç", "çöp", "israf", "tasarruf", "temiz"]
SON = ["görev", "sorumlu", "hepimiz", "geleceğ"]
YARIM = ["tamamlanma", "eksik", "yarım", "okuyucu", "okura", "bitmemiş", "kesil", "bitirilmemiş"]
SIRALI = ["sıralı cümle", "cümleleri ayır", "iki cümle", "cümleler arasın"]

# =====================================================================
# MEB SORULARI (5 soru) — öncelik: 2 banko, 2 puan topla, 1 bir adım
# =====================================================================
HURKUS = ["Türkiye'nin yerli ve millî imkânlarla geliştirdiği HÜRKUŞ, eğitim ve keşif görevleri için tasarlanmış modern bir uçaktır. Güçlü motoru ve dayanıklı yapısı sayesinde güvenli uçuş imkânı sunar. Pilotların eğitim sürecinde ihtiyaç duyduğu birçok teçhizata sahip olan HÜRKUŞ, gelişmiş kontrol sistemleriyle kolay kullanım sağlar.",
          "Farklı hava koşullarında görev yapabilen bu uçak, yüksek manevra kabiliyeti sayesinde eğitim uçuşlarında önemli bir avantaj sağlar. Yerli mühendisler tarafından tasarlanan HÜRKUŞ, Türkiye'nin havacılık alanındaki gelişimini gösteren önemli projelerden biridir.",
          "Aşağıdaki kelimelerin anlamını metinden hareketle tahmin ediniz. Tahminlerinizi ilgili alanlara yazınız."]
KESIF = ["incele", "bilgi", "araştır", "keşfet", "öğren", "bilinmeyen"]
TECHIZAT = ["araç", "gereç", "donanım", "malzeme", "alet", "ekipman"]
MANEVRA = ["hareket", "yön", "dön", "kontrol", "yönlendir"]
AN1 = "Anlamı → kelimeyi tekrar etme, başka kelimelerle kısaca açıkla: “… demek”."
Y.meb(id="m1", no=1, kazanim=K1, oncelik=2, metin=HURKUS,
    maddeler=[
        Q(M("a", "keşif: Bu kelimenin metindeki anlamını tahmin edip yazınız.", "Keşif: Bilinmeyen bir yeri inceleyip bilgi toplama, araştırma.",
            [A("İnceleyip bilgi toplama", *KESIF)], "anlam"),
          ["anlamını tahmin edip yazınız"], AN1,
          B("Bir yeri inceleyip bilgi toplama.", "Uçakla yapılan şey.", "Çok hızlı uçmak.",
            "Kelimenin yanındaki “eğitim ve … görevleri” sözüne bak: uçak bir yeri neden gezer?", "Keşif uçağı bir yeri inceler ve bilgi toplar. MEB de “gizli olan bir şey hakkında bilgi edinme, bir yeri inceleme” cevabını kabul ediyor. (MEB örnek sorusu; s. 12)",
            P("Keşif:", "bir yeri inceleyip bilgi toplamak", ["uçağın rengi", "pilotun adı"], k=KESIF))),
        Q(M("b", "teçhizat: Bu kelimenin metindeki anlamını tahmin edip yazınız.", "Teçhizat: Bir görev için gerekli olan araç gereçlerin, donanımların tümü.",
            [A("Görev için araç gereç", *TECHIZAT)], "anlam"),
          ["anlamını tahmin edip yazınız"], AN1,
          B("Görev için gereken araç gereçler.", "Uçakta olan şeyler.", "Pilotun eğitim süresi.",
            "Cümle “pilotların eğitimde ihtiyaç duyduğu birçok …” diyor: ihtiyaç duyulan ne olabilir?", "Teçhizat, bir görev için gerekli araç gereç ve donanımlardır. (MEB örnek sorusu)",
            P("Teçhizat:", "görev için gereken araç gereçler", ["uçuşun saati", "havanın durumu"], k=TECHIZAT))),
        Q(M("c", "manevra: Bu kelimenin metindeki anlamını tahmin edip yazınız.", "Manevra: Bir araca istenilen hareketi yaptırma, aracı yönlendirip yön değiştirme.",
            [A("Araca hareket yaptırma, yön değiştirme", *MANEVRA)], "anlam"),
          ["anlamını tahmin edip yazınız"], AN1,
          B("Aracı istenen yöne hareket ettirme.", "Uçağın bir özelliği.", "Uçağı park etmek.",
            "Uçak havada dönerken, yön değiştirirken ne yapar?", "Manevra, bir araca istenilen hareketi yaptırmaktır; yön değiştirmek de manevradır. (MEB örnek sorusu)",
            P("Manevra:", "aracı istenen yöne hareket ettirmek", ["uçağı boyamak", "yakıt almak"], k=MANEVRA)))],
    ikizler=[
        {"metin": ["Okulun bahçesinde uzun süredir bakımsız kalan alanı düzenlemek için öğrenciler birlikte çalışmaya karar verdi. Bazı öğrenciler toprağı kazarken bazıları yeni fidanlar dikti. Ece, arkadaşlarının yorulduğunu fark edince onlara destek oldu ve kendi görevini bitirdikten sonra diğerlerine de yardım etti. Öğretmenleri, öğrencilerin çevreyi güzelleştirmek için gösterdiği gayreti takdir etti."],
         "maddeler": [M("a", "destek: Bu kelimenin metindeki anlamını tahmin edip yazınız.", "Destek: Birinin işini kolaylaştırmak için ona yardım etme, yanında olma.",
                        [A("Yardım etme, yanında olma", "yardım", "yanında", "kolaylaştır", "el uzat")], "anlam"),
                      M("b", "gayret: Bu kelimenin metindeki anlamını tahmin edip yazınız.", "Gayret: Bir işi başarmak için gösterilen çaba, emek.",
                        [A("Çaba, emek", "çaba", "emek", "uğraş", "çalışma")], "anlam")]},
        {"metin": ["Yer kabuğunun derinliklerinde bulunan erimiş kayaçlara magma adı verilir. Magma, yer kabuğundaki çatlaklardan yukarı doğru ilerleyerek yüzeye ulaşabilir. Yeryüzüne çıkan magma artık lav olarak adlandırılır ve çevreye yayılır. Volkanın tepesinde bulunan çanak biçimindeki krater, lav ve gazların dışarı çıktığı bölümdür. Patlama sırasında çok küçük kaya ve mineral parçalarından oluşan kül de havaya karışabilir.",
                    "Aşağıda metinde geçen bazı kelimelerin anlamları verilmiştir. Bu kelimeleri metinden bularak yazınız."],
         "maddeler": [M("a", "Yer kabuğunun altında bulunan erimiş kayaç maddesi: Bu anlama gelen kelimeyi metinden bulunuz.", "Magma", [A("magma", "magma")], "bul"),
                      M("b", "Yeryüzüne çıktıktan sonra akış hâlinde bulunan erimiş kaya: Bu anlama gelen kelimeyi metinden bulunuz.", "Lav", [A("lav", "lav")], "bul"),
                      M("c", "Volkanın tepesinde bulunan çanak biçimindeki açıklık: Bu anlama gelen kelimeyi metinden bulunuz.", "Krater", [A("krater", "krater")], "bul")]}])

Y.meb(id="m2", no=2, kazanim=K2, oncelik=3,
    metin=["Arılar doğada önemli bir role sahiptir. Çiçeklerden topladıkları nektarı kovanlarına taşıyarak bal üretirler ancak arıların görevi sadece bal yapmak değildir. Çiçekler arasında dolaşırken bitkilerin tozlaşmasına da yardımcı olurlar. Bu sayede birçok bitki çoğalabilir ve doğadaki yaşam dengesi korunur. Son yıllarda yapılan araştırmalar, arıların sayısının azalmasının bitki çeşitliliğini ve tarımı olumsuz etkileyebileceğini göstermektedir. Bu nedenle arıların korunması doğa için büyük önem taşımaktadır."],
    maddeler=[Q(M("a", "Metnin konusunu yazınız.", "Metnin konusu, arıların doğadaki önemi ve bitkilerin çoğalmasındaki rolüdür.",
        [A("Kimi anlatıyor: arılar", "arı"), A("Ne anlatıyor: doğadaki önemi, görevi", *KONU_DEGER)], "konu"),
        ["konusunu"], "Konu → “Metin neyi anlatıyor?” Kısa öbek: “… -ın … önemi”.",
        B("Arıların doğadaki önemi.", "Arılar.", "Arıları korumalıyız, yoksa doğa bozulur.",
          "Konu kısa yazılır ama yalnız “Arılar” yetmez: arılar hakkında ne anlatılıyor?", "Konu, metinde neyin anlatıldığıdır; kısa bir öbekle yazılır. “Arıları korumalıyız” bir ders cümlesidir, yani ana düşüncedir. (s. 22; MEB örnek sorusu)",
          P("Hangi canlı?", "arıların", ["çiçeklerin renklerini", "balın fiyatını"], k=["arı"]),
          P("Neyini anlatıyor?", "doğadaki önemini", ["kanat sayısını", "uyku saatlerini"], k=KONU_DEGER)))],
    ikizler=[
        {"metin": ["Her şehrin ana caddelerine bir çıkın ve tabelaları inceleyin. Türkiye'de olmadığınızı düşünebilirsiniz. Bir dil bu kadar özentiye kurban edilir mi? Kendi dilimizi zorla yabancı kelimelerin boyunduruğu altına sokuyoruz ve bunu bir marifetmiş gibi tabelalarımızda, tişörtlerimizde taşıyoruz. Dilimiz bizim öz kimliğimizdir ve dilimizi kaybedersek kendimize ait tüm kültürümüzü kaybederiz. Bu nedenle kendi kelimelerimize sahip çıkmak vatanımıza sahip çıkmak kadar önemlidir."],
         "maddeler": [M("a", "Metnin konusunu yazınız.", "Dilimizde yabancı kelimelerin kullanılması ve Türkçeye sahip çıkmanın önemi.",
                        [A("Dil, Türkçe", "dil", "türkçe", "kelime"), A("Yabancı kelime / sahip çıkma", "yabancı", "sahip çık", "önem")], "konu"),
                      M("b", "Metnin ana düşüncesini yazınız.", "Dil, kimliğimizin ve kültürümüzün parçasıdır; bu nedenle yabancı kelimeler yerine Türkçe kelimeler kullanıp dilimize sahip çıkmalıyız.",
                        [A("Dilimize sahip çıkmalıyız", "sahip çık", "korumalı", "kullanmalı"), A("Çünkü dil kimliğimiz, kültürümüz", "kimli", "kültür")], "ana")]},
        {"metin": ["Günümüzde başarı çoğu zaman hiç hata yapmamakla ilişkilendiriliyor. Oysa insan yeni bir şey öğrenirken yanılabilir, eksik kalabilir ve bazen yeniden başlamak zorunda kalabilir. Hatalar doğru değerlendirildiğinde kişiye neyi değiştirmesi gerektiğini gösteren önemli birer işarettir. Bu nedenle başarısızlıktan kaçmak yerine ondan ders çıkarmak, gelişmenin en sağlam yollarından biridir. Asıl önemli olan hiç düşmemek değil, her denemeden yeni bir şey öğrenerek yoluna devam edebilmektir."],
         "maddeler": [M("a", "Metnin konusunu yazınız.", "Hataların insanın gelişmesindeki önemi.",
                        [A("Hatalar, başarısızlık", "hata", "başarısız", "yanıl"), A("Gelişmedeki önemi, yararı", "önem", "geliş", "yarar", "fayda", "ders")], "konu"),
                      M("b", "Bu metinde asıl anlatılmak istenen düşünceyi kendi cümlelerinizle yazınız.", "Hatalar doğru değerlendirildiğinde insanı geliştirir; bu yüzden hatadan korkmamalı, ondan ders çıkarmalıyız.",
                        [A("Hatalardan ders çıkarmalıyız", "ders çıkar", "öğren", "korkmamalı", "kaçmamalı"), A("Hatalar insanı geliştirir", "geliş", "başarı", "ilerle")], "ana")]}])

FORSA = ["Kırk yıllık bir esaret! Yıllarca kadırgalarda kürek çekmiş, Malta'nın karanlık zindanlarında yatmıştı. Şimdi yaşı altmışı geçmişti. İhtiyarlamış, çok bitap düşmüştü. Kolları eski kuvvetini kaybetmiş, o heybetli vücudu âdeta erimiş, bir kemik torbasına dönmüştü. Ama yıllar onun sadece bedenini yormuş, ruhundaki memleket ateşini söndürememişti. Geceleri rüyasında hep o sevgili yurdunu; yurdunun serin pınarlarını, ulu dağlarını görürdü. Gündüzleri ise engin denizlere bakarak ufukta belirecek bir Türk yelkenlisi görmenin iştiyakıyla yanıp tutuşurdu. Gözleri ufukta, kalbi memleket hasretiyle atarken rüzgârın getirdiği dalga sesleri ona ufak bir teselli verir, vatanından ayrı kalmanın acısını bir an olsun unuttururdu.",
         "Ömer Seyfettin'in “Forsa” adlı hikâyesinden alınan metindeki kelimelerin anlamlarını metnin bağlamından yararlanarak tahmin ediniz. Tahminlerinizi ve gerekçelerinizi yazınız."]
BITAP_T = ["yorgun", "güçsüz", "bitkin", "halsiz", "hâlsiz", "dermansız", "takatsiz"]
BITAP_G = ["kuvvet", "kemik", "erimiş", "ihtiyarla"]
ISTIYAK_T = ["özlem", "özle", "istek", "arzu", "çok iste", "hasret"]
ISTIYAK_G = ["yanıp tutuş", "rüyasında", "kalbi memleket"]
TESELLI_T = ["avun", "hafiflet", "moral", "rahatla", "azalt", "iyi gel"]
TESELLI_G = ["unuttur"]
GR = "Tahmin + gerekçe → “Anlamı: … Gerekçe: Metinde ‘…’ yazıyor.”"
Y.meb(id="m6", no=6, kazanim=K3, oncelik=2, metin=FORSA,
    maddeler=[
        Q(M("a", "bitap: Kelimenin anlamına dair tahmininizi ve sizi bu tahmine götüren metin içi gerekçeleri yazınız.",
            "Tahminim: yorgun, güçsüz, bitkin. Gerekçem: Metinde “kolları eski kuvvetini kaybetmiş”, “bir kemik torbasına dönmüştü” ve “ihtiyarlamış” yazıyor.",
            [A("Tahmin: yorgun, güçsüz", *BITAP_T), A("Gerekçe: metindeki ipucu", *BITAP_G)], "gerekce"),
          ["tahmininizi", "metin içi gerekçeleri"], GR,
          B("Yorgun, güçsüz; çünkü metinde “kolları eski kuvvetini kaybetmiş” yazıyor.", "Yorgun, güçsüz.", "Mutlu; çünkü bence yaşlılar hep mutludur.",
            "Soru iki şey istiyor: anlam tahmini ve metinden gerekçe. Gerekçe senin fikrin değil, metindeki ipucu.", "Bitap: yorgun, güçsüz. Ardından gelen “kolları eski kuvvetini kaybetmiş, bir kemik torbasına dönmüştü” ifadeleri bunu gösterir. (MEB örnek sorusu)",
            P("Tahminim:", "yorgun, güçsüz", ["neşeli, güçlü", "zengin, varlıklı"], k=BITAP_T),
            P("Gerekçem: Metinde", "“kolları eski kuvvetini kaybetmiş”", ["“serin pınarlarını”", "“engin denizlere”"], k=BITAP_G))),
        Q(M("b", "iştiyak: Kelimenin anlamına dair tahmininizi ve sizi bu tahmine götüren metin içi gerekçeleri yazınız.",
            "Tahminim: özlem, çok isteme. Gerekçem: Metinde “yanıp tutuşurdu”, “kalbi memleket hasretiyle atarken” ve “rüyasında hep o sevgili yurdunu görürdü” yazıyor.",
            [A("Tahmin: özlem, çok isteme", *ISTIYAK_T), A("Gerekçe: metindeki ipucu", *ISTIYAK_G)], "gerekce"),
          ["tahmininizi", "metin içi gerekçeleri"], GR,
          B("Özlem; çünkü metinde “yanıp tutuşurdu” yazıyor.", "Özlem.", "Korku; çünkü denizler tehlikelidir.",
            "Kelimenin hemen arkasındaki “… yanıp tutuşurdu” sözüne bak.", "İştiyak: özlem, çok isteme. “Yanıp tutuşurdu” ve “kalbi memleket hasretiyle atarken” ifadeleri büyük bir özlemi gösterir. (MEB örnek sorusu)",
            P("Tahminim:", "özlem, çok isteme", ["korku, kaçma", "uyku, dinlenme"], k=ISTIYAK_T),
            P("Gerekçem: Metinde", "“yanıp tutuşurdu”", ["“kürek çekmiş”", "“ulu dağlarını”"], k=ISTIYAK_G))),
        Q(M("c", "teselli: Kelimenin anlamına dair tahmininizi ve sizi bu tahmine götüren metin içi gerekçeleri yazınız.",
            "Tahminim: avuntu, acıyı hafifleten şey. Gerekçem: Kelimenin hemen ardında “acısını bir an olsun unuttururdu” yazıyor.",
            [A("Tahmin: avuntu, acıyı hafifletme", *TESELLI_T), A("Gerekçe: metindeki ipucu", *TESELLI_G)], "gerekce"),
          ["tahmininizi", "metin içi gerekçeleri"], GR,
          B("Avuntu, rahatlama; çünkü metinde “bir an olsun unuttururdu” yazıyor.", "Avuntu, rahatlama.", "Rüzgâr; çünkü dalga sesini rüzgâr getirir.",
            "Teselli verdikten sonra dalga sesleri ona ne yapıyor? Cümlenin sonunu oku.", "Teselli: avuntu, acıyı hafifleten şey. Hemen ardındaki “acısını bir an olsun unuttururdu” bunu gösterir. (MEB örnek sorusu)",
            P("Tahminim:", "avuntu, rahatlama", ["kızgınlık, öfke", "yorgunluk, uyku"], k=TESELLI_T),
            P("Gerekçem: Metinde", "“bir an olsun unuttururdu”", ["“yaşı altmışı geçmişti”", "“karanlık zindanlarında”"], k=TESELLI_G)))],
    ikizler=[
        {"metin": ["Okul takımına yeni katılan Ege, ilk antrenmanlarda birkaç kez pas hatası yaptı. Bazı arkadaşları onun takıma katkı sağlayamayacağını düşünmeye başladı. Ancak Ege sonraki günlerde düzenli çalıştı, kısa sürede oyuna uyum sağladı ve önemli maçlarda takımına büyük katkı sundu. Arkadaşları, başlangıçta Ege'yi yeterince tanımadan “burun kıvırdıklarını” anladı."],
         "maddeler": [M("a", "“Burun kıvırmak” söz grubunun anlamını tahmin ediniz ve sizi bu tahmine götüren metin içi gerekçeyi yazınız.",
            "Tahminim: beğenmemek, küçümsemek, yeterli görmemek. Gerekçem: Metinde arkadaşlarının “onun takıma katkı sağlayamayacağını düşünmeye başladı” ve onu “yeterince tanımadan” yargıladıkları yazıyor.",
            [A("Tahmin: beğenmemek, küçümsemek", "beğenme", "küçümse", "yeterli görme", "önemseme", "hor gör"), A("Gerekçe: metindeki ipucu", "katkı sağlayamayacağını", "tanımadan")], "gerekce")]},
        {"metin": ["Dağın zirvesine ulaşan Selin nefes nefese kalmıştı. Dizleri titriyor, bir adım daha atacak dermanı kalmamıştı. Yine de karşısındaki manzarayı görünce bütün yorgunluğunu unuttu. Gökyüzü masmavi, vadiler yemyeşildi; uzaklarda karlı tepeler parlıyordu. Bu ihtişam karşısında ağzı açık kaldı, uzun süre konuşamadı."],
         "maddeler": [M("a", "derman: Kelimenin anlamına dair tahmininizi ve sizi bu tahmine götüren metin içi gerekçeyi yazınız.",
                        "Tahminim: güç, kuvvet. Gerekçem: Metinde “nefes nefese kalmıştı”, “dizleri titriyor” ve “yorgunluğunu” yazıyor.",
                        [A("Tahmin: güç, kuvvet", "güç", "kuvvet", "takat", "enerji"), A("Gerekçe: metindeki ipucu", "nefes nefese", "dizleri titri", "yorgun")], "gerekce"),
                      M("b", "ihtişam: Kelimenin anlamına dair tahmininizi ve sizi bu tahmine götüren metin içi gerekçeyi yazınız.",
                        "Tahminim: görkem, büyüklük, göz alıcı güzellik. Gerekçem: Metinde “ağzı açık kaldı”, “gökyüzü masmavi, vadiler yemyeşildi” yazıyor.",
                        [A("Tahmin: görkem, büyük güzellik", "görkem", "güzellik", "büyüklük", "muhteşem", "göz alıcı"), A("Gerekçe: metindeki ipucu", "ağzı açık", "masmavi", "yemyeşil", "parlıyor")], "gerekce")]}])

Y.meb(id="m9", no=9, kazanim=K4, oncelik=3,
    metin=["Aşağıda yer alan yazım ve noktalama ile ilgili soruları cevaplayınız."],
    maddeler=[
        Q(M("a", "“Sınav kâğıtlarını apar-topar toplayıp hızlıhızlı sınıftan çıktı ancak dışarıda yağmur yağıyordu.” cümlesinde yazım yanlışı yapılmış ikilemeleri bulunuz ve cümlenin doğru hâlini yazınız.",
            "Sınav kâğıtlarını apar topar toplayıp hızlı hızlı sınıftan çıktı ancak dışarıda yağmur yağıyordu. (İkilemeler ayrı yazılır, arasına kısa çizgi konmaz.)",
            [A("apar topar (çizgisiz)", "apar topar"), A("hızlı hızlı (ayrı)", "hızlı hızlı")], "ikileme"),
          ["yazım yanlışı yapılmış ikilemeleri", "doğru hâlini"], "İkileme yazımı → iki kelime ayrı, arada çizgi ya da virgül yok; cümleyi baştan yaz.",
          B("Sınav kâğıtlarını apar topar toplayıp hızlı hızlı sınıftan çıktı…", "Sınav kâğıtlarını apar topar toplayıp hızlıhızlı sınıftan çıktı…", "Sınav kâğıtlarını apar-topar toplayıp hızlı-hızlı sınıftan çıktı…",
            "Cümlede iki ikileme var; ikisinin de yazımına bak.", "İkilemeler ayrı yazılır ve arasına kısa çizgi konmaz: apar topar, hızlı hızlı. (s. 34; MEB örnek sorusu)",
            P("1. ikileme:", "apar topar", ["apar-topar", "apartopar"], k=["apar topar"]),
            P("2. ikileme:", "hızlı hızlı", ["hızlıhızlı", "hızlı-hızlı"], k=["hızlı hızlı"]))),
        Q(M("b", "“Genç şairimiz ( ) Necip Fazıl, Nâzım Hikmet ve Attilâ İlhan gibi isimlerden ilham alıyordu.” Boşluğa uygun işareti (noktalı virgül ya da üç nokta) getiriniz ve kullanım amacını belirtiniz.",
            "Noktalı virgül (;). Amacı: İkiden fazla eş değer öge (şair isimleri) arasında virgül bulunan cümlede özneyi (Genç şairimiz) diğer ögelerden ayırmak için özneden sonra konur.",
            [A("İşaret: noktalı virgül", "noktalı virgül"), A("Amaç: özneden sonra konur", "özne")], "isaret"),
          ["uygun işareti", "kullanım amacını"], "İşaret + amaç → “Noktalı virgül / Üç nokta; çünkü …” İkisini de yaz.",
          B("Noktalı virgül; özneden sonra konur.", "Noktalı virgül.", "Üç nokta; cümle yarım kaldı.",
            "Boşluktan sonra virgülle sıralanan isimler var. Boşluktan önce kim var?", "İkiden fazla eş değer öge arasında virgül bulunan cümlelerde özneden sonra noktalı virgül konabilir. (s. 49; MEB örnek sorusu)",
            P("İşaret:", "noktalı virgül", ["üç nokta", "ünlem işareti"], k=["noktalı virgül"]),
            P("Amacı: isimler sıralanmadan önce", "özneyi ayırmak", ["cümleyi bitirmek", "soru sormak"], k=["özne"]))),
        Q(M("c", "“Bahçemizde meyve ağaçları, rengârenk çiçekler, taze ot kokuları ( ) İçimiz huzurla doldu.” Boşluğa uygun işareti (noktalı virgül ya da üç nokta) getiriniz ve kullanım amacını belirtiniz.",
            "Üç nokta (...). Amacı: Anlatımı tamamlanmamış, yarım bırakılan cümlenin sonuna konur; sözün gerisi okuyucuya bırakılmıştır.",
            [A("İşaret: üç nokta", "üç nokta", "..."), A("Amaç: cümle tamamlanmamış", *YARIM)], "isaret"),
          ["uygun işareti", "kullanım amacını"], "İşaret + amaç → “Noktalı virgül / Üç nokta; çünkü …” İkisini de yaz.",
          B("Üç nokta; cümle tamamlanmamış, yarım kalmış.", "Üç nokta.", "Noktalı virgül; özneden sonra konur.",
            "Boşluktan önceki cümlenin yüklemi var mı? Cümle bitmiş mi?", "Üç nokta, sözün bir yerde kesilip gerisinin okuyucuya bırakıldığını gösterir; MEB'in cevabı: anlatımı tamamlanmamış cümlenin sonuna konur. (s. 35; MEB örnek sorusu)",
            P("İşaret:", "üç nokta", ["noktalı virgül", "iki nokta"], k=["üç nokta"]),
            P("Amacı: cümle", "tamamlanmamış, yarım kalmış", ["soru soruyor", "özneyle başlıyor"], k=YARIM))),
        Q(M("d", "“Tarihî eserleri koruyan toplumlar geçmişleriyle bağlarını güçlendirir, kültürel miraslarını gelecek nesillere aktarır ( ) bu eserlere yeterince önem vermeyen toplumlar ise zamanla tarihî değerlerini kaybeder, kültürel kimliklerinden uzaklaşır.” Boşluğa uygun işareti getiriniz ve kullanım amacını belirtiniz.",
            "Noktalı virgül (;). Amacı: Ögeleri arasında virgül bulunan sıralı cümleleri birbirinden ayırmak için kullanılmıştır.",
            [A("İşaret: noktalı virgül", "noktalı virgül"), A("Amaç: sıralı cümleleri ayırır", *SIRALI)], "isaret"),
          ["uygun işareti", "kullanım amacını"], "İşaret + amaç → “Noktalı virgül / Üç nokta; çünkü …” İkisini de yaz.",
          B("Noktalı virgül; virgüllü sıralı cümleleri ayırır.", "Noktalı virgül.", "Üç nokta; söz okura bırakıldı.",
            "Boşluğun iki yanında ayrı yüklemli iki cümle var ve ikisinin içinde de virgül var.", "Ögeleri arasında virgül bulunan sıralı cümleleri ayırmak için noktalı virgül konur. (s. 49; MEB örnek sorusu)",
            P("İşaret:", "noktalı virgül", ["üç nokta", "soru işareti"], k=["noktalı virgül"]),
            P("Amacı: içinde virgül olan", "sıralı cümleleri ayırmak", ["özneyi ayırmak", "sözü okura bırakmak"], k=SIRALI)))],
    ikizler=[
        {"metin": ["Bir öğrenci aşağıdaki cümleleri yazarken yazım ve noktalama hataları yapmıştır."],
         "maddeler": [M("a", "“Yarışmacılar sahneye teker-teker çağrıldı.” cümlesinde yanlış yazılan ikilemeyi bulup cümlenin doğru hâlini yazınız.",
                        "Yarışmacılar sahneye teker teker çağrıldı.", [A("teker teker", "teker teker")], "ikileme"),
                      M("b", "“Yağmur başlayınca insanlar koşakoşa durağa yöneldi.” cümlesinde yanlış yazılan ikilemeyi bulup cümlenin doğru hâlini yazınız.",
                        "Yağmur başlayınca insanlar koşa koşa durağa yöneldi.", [A("koşa koşa", "koşa koşa")], "ikileme"),
                      M("c", "“Bahçedeki çocuklar irili, ufaklı taşları bir kutuda topladı.” cümlesinde yanlış yazılan ikilemeyi bulup cümlenin doğru hâlini yazınız.",
                        "Bahçedeki çocuklar irili ufaklı taşları bir kutuda topladı.", [A("irili ufaklı (virgülsüz)", "irili ufaklı")], "ikileme"),
                      M("d", "“Gezi için Ece su, sandviç, meyve hazırladı ( ) Kerem şapka, güneş kremi, gözlük aldı.” Boşluğa gelmesi gereken işareti ve kullanım amacını yazınız.",
                        "Noktalı virgül (;). Amacı: Ögeleri arasında virgül bulunan sıralı cümleleri birbirinden ayırmak.",
                        [A("noktalı virgül", "noktalı virgül"), A("Amaç: sıralı cümleleri ayırır", *SIRALI)], "isaret")]},
        {"metin": ["Aşağıda yer alan yazım ve noktalama ile ilgili soruları cevaplayınız."],
         "maddeler": [M("a", "“Çocuklar bahçede koşa-koşa oynarken annem mutfakta ağırağır çay demledi.” cümlesinde yazım yanlışı yapılmış ikilemeleri bulunuz ve cümlenin doğru hâlini yazınız.",
                        "Çocuklar bahçede koşa koşa oynarken annem mutfakta ağır ağır çay demledi.", [A("koşa koşa", "koşa koşa"), A("ağır ağır", "ağır ağır")], "ikileme"),
                      M("b", "“Öğretmenimiz ( ) Ali, Ayşe ve Can'ı tebrik etti.” Boşluğa uygun işareti getiriniz ve kullanım amacını belirtiniz.",
                        "Noktalı virgül (;). Amacı: Sıralanan isimler arasında virgül olduğu için özneyi diğer ögelerden ayırmak üzere özneden sonra konur.",
                        [A("noktalı virgül", "noktalı virgül"), A("Amaç: özneden sonra", "özne")], "isaret"),
                      M("c", "“Sınıfta yeni kitaplar, defterler, renkli kalemler ( ) Her şey yeni döneme hazırdı.” Boşluğa uygun işareti getiriniz ve kullanım amacını belirtiniz.",
                        "Üç nokta (...). Amacı: Cümle tamamlanmamış, yarım bırakılmış; sözün gerisi okuyucuya bırakılmıştır.",
                        [A("üç nokta", "üç nokta", "..."), A("Amaç: cümle tamamlanmamış", *YARIM)], "isaret")]}])

Y.meb(id="m10", no=10, kazanim=K5, oncelik=1,
    metin=["“Doğa sevgisi” temalı bilgilendirici bir metin yazmayı planladığınızı düşününüz."],
    maddeler=[
        Q(M("a", "Bu metnin giriş, gelişme ve sonuç bölümlerinde hangi içeriklere yer vereceğinizi taslak hâlinde yazınız.",
            "Giriş: Doğanın insan hayatındaki önemi belirtilerek konuya giriş yapılır. Gelişme: Doğayı korumak için yapılması gerekenler (geri dönüşüm, ağaçlandırma) örneklerle açıklanır. Sonuç: Doğayı korumanın hepimizin görevi olduğu vurgulanır.",
            [A("Giriş: doğanın önemi", *GIRIS), A("Gelişme: korumak için yapılacaklar, örnek", *KORU), A("Sonuç: hepimizin görevi", *SON)], "taslak"),
          ["taslak hâlinde"], "Taslak → 3 satır: “Giriş: … Gelişme: … Sonuç: …”",
          B("Giriş: doğanın hayatımızdaki önemi. Gelişme: geri dönüşüm, fidan dikmek. Sonuç: doğayı korumak hepimizin görevi.",
            "Giriş: doğanın önemi. Gelişme: geri dönüşüm, fidan dikmek.", "Geçen yaz ailemle denize gittik, çok eğlendik.",
            "Taslakta üç bölüm olmalı; her birine bir satır.", "Giriş konuyu tanıtır, gelişme açıklar ve örnek verir, sonuç toparlar. (s. 167; MEB örnek sorusu)",
            P("Giriş (konuyu tanıt):", "doğanın hayatımızdaki önemi", ["en sevdiğim renk", "bugünkü hava durumu"], k=GIRIS),
            P("Gelişme (açıkla, örnek ver):", "geri dönüşüm, fidan dikmek", ["televizyon izlemek", "alışverişe gitmek"], k=KORU),
            P("Sonuç (toparla):", "doğayı korumak hepimizin görevi", ["ben bilmem", "doğa çok uzakta"], k=SON))),
        Q(M("b", "Taslağınıza uygun bir metin yazınız.",
            "Doğa; nefes aldığımız hava, içtiğimiz su ve bizi doyuran topraktır, yani hayatımız için çok önemlidir. Ancak ormanlar yok ediliyor, denizler kirleniyor. Doğayı sevmek eylem ister: Örneğin çöplerimizi geri dönüşüme atabilir, suyu israf etmeyebilir, fidan dikebiliriz. Sonuç olarak doğayı korumak hepimizin görevidir; doğayı korumak aslında kendi geleceğimizi korumaktır.",
            [A("Giriş: doğanın önemi", *GIRIS), A("Gelişme: yapılacaklar ve örnek", *KORU), A("Sonuç: hepimizin görevi", *SON)], "metin"),
          ["Taslağınıza uygun bir metin"], "Metin → her bölüme 1–2 cümle; örneği “Örneğin …”, sonucu “Sonuç olarak …” ile yaz.",
          B("Doğa hayatımız için çok önemlidir. Örneğin fidan dikebilir, çöpleri geri dönüşüme atabiliriz. Sonuç olarak doğayı korumak hepimizin görevidir.",
            "Doğa hayatımız için çok önemlidir. Örneğin fidan dikebiliriz.", "Doğa. Ağaç. Deniz. Çiçek.",
            "Taslaktaki üç satırı üç kısa cümleye çevir.", "Metin taslağa uymalı: giriş, gelişme, sonuç; her bölüme 1–2 cümle yeter. (s. 167; MEB örnek sorusu)",
            P("Giriş: Doğa", "hayatımız için çok önemlidir", ["bazen sıkıcıdır", "bir resimdir"], k=GIRIS),
            P("Gelişme: Örneğin", "fidan dikebilir, çöpleri geri dönüşüme atabiliriz", ["oyun oynayabiliriz", "uyuyabiliriz"], k=KORU),
            P("Sonuç olarak doğayı korumak", "hepimizin görevidir", ["zor bir iştir", "gereksizdir"], k=SON)))],
    ikizler=[
        {"metin": ["“Kitap okumanın faydaları” temalı bilgilendirici bir metin yazmayı planladığınızı düşününüz."],
         "maddeler": [M("a", "Bu metnin giriş, gelişme ve sonuç bölümlerinde hangi içeriklere yer vereceğinizi taslak hâlinde yazınız.",
                        "Giriş: Kitap okumanın hayatımızdaki yeri ve önemi. Gelişme: Okumanın faydaları; kelime hazinesi gelişir, hayal gücü artar, örneğin her gün 20 sayfa okumak. Sonuç: Kitap okumayı alışkanlık hâline getirmeliyiz.",
                        [A("Giriş: okumanın önemi", "önem", "hayat", "yeri"), A("Gelişme: faydalar", "kelime", "hayal", "bilgi"), A("Sonuç: alışkanlık edinmeliyiz", "alışkanlık", "okumalıyız", "edinmeli")], "taslak"),
                      M("b", "Taslağınıza uygun bir metin yazınız.",
                        "Kitaplar bize yeni dünyaların kapısını açar; bu yüzden okumak hayatımızda çok önemlidir. Kitap okuyan kişinin kelime hazinesi gelişir, hayal gücü artar. Örneğin her gün yirmi sayfa okuyan biri yılda birçok kitap bitirir. Sonuç olarak kitap okumayı alışkanlık hâline getirmeliyiz.",
                        [A("Giriş: okumanın önemi", "önem", "hayat"), A("Gelişme: faydalar ve örnek", "kelime", "hayal", "örne"), A("Sonuç: alışkanlık", "alışkanlık", "okumalıyız")], "metin")]},
        {"metin": ["Bir öğrenci, sınava hazırlanırken önemli bilgileri küçük kartlara yazarak gün içinde tekrar ediyor. Başka bir öğrenci ise aynı konuları renkli kavram haritaları oluşturarak çalışıyor. Okulun bültende bu iki çalışma biçiminin ortak yönlerini ve birbirinden ayrılan özelliklerini açıklamanız isteniyor."],
         "maddeler": [M("a", "Karşılaştırma-zıtlık, tanıtıcı ve sıralı-kronolojik metin yapılarından amacınıza en uygun olanı belirleyip adını yazınız.",
                        "Karşılaştırma-zıtlık metin yapısı; çünkü iki yöntemin benzer ve farklı yönleri anlatılacak.",
                        [A("Karşılaştırma-zıtlık", "karşılaştırma"), A("Çünkü benzer ve farklı yönler", "benzer", "farklı", "ortak")], "yapi"),
                      M("b", "Seçtiğiniz yapıya uygun, iki çalışma yönteminin benzer ve farklı yönlerini ele alan kısa bir bilgilendirici metin yazınız.",
                        "Her iki öğrenci de bilgileri kalıcı hâle getirmek için çalışıyor. Bilgi kartları kısa tekrar yapmayı kolaylaştırır; kavram haritaları ise bilgiler arasındaki ilişkiyi gösterir. Sonuç olarak iki yöntem de öğrenmeyi destekler ama biri tekrara, diğeri ilişki kurmaya yardım eder.",
                        [A("Benzer yön: ikisi de", "ikisi de", "her iki", "ikisinde de"), A("Farklı yön: oysa / ise", "oysa", " ise", "ilişki"), A("Sonuç", "sonuç olarak", "kısacası")], "yapi")]}])

# =====================================================================
# BENZER SORULAR (Konu Tekrarı): kısa cevap, tetik, kalıp notu, parçalar (sec YOK → doğrudan sınavdaki gibi yazma)
# =====================================================================
IKIZ = {
 ("m1i1", "a"): IK("Yardım etme, yanında olma.", ["anlamını tahmin edip yazınız"], AN1,
    P("Destek:", "yardım etmek, yanında olmak", ["kızmak", "uzaklaşmak"], k=["yardım", "yanında", "kolaylaştır"])),
 ("m1i1", "b"): IK("Çaba, emek.", ["anlamını tahmin edip yazınız"], AN1,
    P("Gayret:", "çaba, emek", ["tembellik", "uyku"], k=["çaba", "emek", "uğraş", "çalışma"])),
 ("m1i2", "a"): IK("Magma", ["kelimeyi metinden bulunuz"], "Anlamdan kelimeye → anlamı oku, metinde ona uyan kelimeyi bul, aynen yaz.",
    P("Kelime:", "magma", ["krater", "kül"], k=["magma"])),
 ("m1i2", "b"): IK("Lav", ["kelimeyi metinden bulunuz"], "Anlamdan kelimeye → anlamı oku, metinde ona uyan kelimeyi bul, aynen yaz.",
    P("Kelime:", "lav", ["magma", "krater"], k=["lav"])),
 ("m1i2", "c"): IK("Krater", ["kelimeyi metinden bulunuz"], "Anlamdan kelimeye → anlamı oku, metinde ona uyan kelimeyi bul, aynen yaz.",
    P("Kelime:", "krater", ["magma", "kül"], k=["krater"])),
 ("m2i1", "a"): IK("Türkçeye sahip çıkmanın önemi.", ["konusunu"], "Konu → “Metin neyi anlatıyor?” Kısa öbek: “… -ın … önemi”.",
    P("Metin neyi anlatıyor?", "Türkçemizin", ["tişört modasını", "şehir trafiğini"], k=["dil", "türkçe", "kelime"]),
    P("Onun hakkında ne?", "sahip çıkmanın önemi", ["renkleri", "fiyatları"], k=["yabancı", "sahip çık", "önem"])),
 ("m2i1", "b"): IK("Dilimize sahip çıkmalıyız, çünkü dil kimliğimizdir.", ["ana düşüncesini"], "Ana düşünce → yazar ne demek istiyor? Bir cümle: “… -malıyız, çünkü …”.",
    P("Ne yapmalıyız?", "dilimize sahip çıkmalıyız", ["tabelaları sökmeliyiz", "tişört almalıyız"], k=["sahip çık", "korumalı", "kullanmalı"]),
    P("Çünkü dil", "kimliğimizdir", ["çok zordur", "yabancıdır"], k=["kimli", "kültür"])),
 ("m2i2", "a"): IK("Hataların gelişmemizdeki önemi.", ["konusunu"], "Konu → “Metin neyi anlatıyor?” Kısa öbek: “… -ın … önemi”.",
    P("Metin neyi anlatıyor?", "hataların", ["sınav sonuçlarının", "okul kurallarının"], k=["hata", "başarısız", "yanıl"]),
    P("Onların neyini?", "gelişmemizdeki önemini", ["sayısını", "rengini"], k=["önem", "geliş", "yarar", "fayda"])),
 ("m2i2", "b"): IK("Hatalardan ders çıkarmalıyız, çünkü hatalar bizi geliştirir.", ["asıl anlatılmak istenen düşünceyi"], "Ana düşünce → yazar ne demek istiyor? Bir cümle: “… -malıyız, çünkü …”.",
    P("Ne yapmalıyız?", "hatalardan ders çıkarmalıyız", ["hiç denememeliyiz", "hatayı saklamalıyız"], k=["ders çıkar", "öğren", "korkmamalı", "kaçmamalı"]),
    P("Çünkü hatalar bizi", "geliştirir", ["üzer", "durdurur"], k=["geliş", "başarı", "ilerle"])),
 ("m6i1", "a"): IK("Küçümsemek; çünkü metinde “katkı sağlayamayacağını düşünmeye başladı” yazıyor.", ["anlamını tahmin ediniz", "metin içi gerekçeyi"], GR,
    P("Tahminim:", "beğenmemek, küçümsemek", ["sevinmek, alkışlamak", "hapşırmak, üşümek"], k=["beğenme", "küçümse", "yeterli görme", "önemseme", "hor gör"]),
    P("Gerekçem: Metinde", "“katkı sağlayamayacağını düşünmeye başladı”", ["“düzenli çalıştı”", "“önemli maçlarda”"], k=["katkı sağlayamayacağını", "tanımadan"])),
 ("m6i2", "a"): IK("Güç, kuvvet; çünkü metinde “dizleri titriyor” yazıyor.", ["tahmininizi", "metin içi gerekçeyi"], GR,
    P("Tahminim:", "güç, kuvvet", ["manzara", "neşe"], k=["güç", "kuvvet", "takat", "enerji"]),
    P("Gerekçem: Metinde", "“dizleri titriyor”", ["“gökyüzü masmavi”", "“karlı tepeler”"], k=["nefes nefese", "dizleri titri", "yorgun"])),
 ("m6i2", "b"): IK("Görkem, büyük güzellik; çünkü metinde “ağzı açık kaldı” yazıyor.", ["tahmininizi", "metin içi gerekçeyi"], GR,
    P("Tahminim:", "görkem, büyük güzellik", ["yorgunluk", "korku"], k=["görkem", "güzellik", "büyüklük", "muhteşem"]),
    P("Gerekçem: Metinde", "“ağzı açık kaldı”", ["“dizleri titriyor”", "“nefes nefese”"], k=["ağzı açık", "masmavi", "yemyeşil", "parlıyor"])),
 ("m9i1", "a"): IK("Yarışmacılar sahneye teker teker çağrıldı.", ["yanlış yazılan ikilemeyi", "doğru hâlini"], "İkileme yazımı → iki kelime ayrı, arada çizgi ya da virgül yok; cümleyi baştan yaz.",
    P("Doğrusu:", "teker teker", ["teker-teker", "tekerteker"], k=["teker teker"])),
 ("m9i1", "b"): IK("İnsanlar koşa koşa durağa yöneldi.", ["yanlış yazılan ikilemeyi", "doğru hâlini"], "İkileme yazımı → iki kelime ayrı, arada çizgi ya da virgül yok; cümleyi baştan yaz.",
    P("Doğrusu:", "koşa koşa", ["koşakoşa", "koşa-koşa"], k=["koşa koşa"])),
 ("m9i1", "c"): IK("Çocuklar irili ufaklı taşları topladı.", ["yanlış yazılan ikilemeyi", "doğru hâlini"], "İkileme yazımı → iki kelime ayrı, arada çizgi ya da virgül yok; cümleyi baştan yaz.",
    P("Doğrusu:", "irili ufaklı", ["irili, ufaklı", "iriliufaklı"], k=["irili ufaklı"])),
 ("m9i1", "d"): IK("Noktalı virgül; virgüllü sıralı cümleleri ayırır.", ["gelmesi gereken işareti", "kullanım amacını"], "İşaret + amaç → “Noktalı virgül / Üç nokta; çünkü …” İkisini de yaz.",
    P("İşaret:", "noktalı virgül", ["üç nokta", "ünlem"], k=["noktalı virgül"]),
    P("Amacı: içinde virgül olan", "sıralı cümleleri ayırmak", ["özneyi ayırmak", "cümleyi bitirmek"], k=SIRALI)),
 ("m9i2", "a"): IK("koşa koşa … ağır ağır", ["yazım yanlışı yapılmış ikilemeleri", "doğru hâlini"], "İkileme yazımı → iki kelime ayrı, arada çizgi ya da virgül yok; cümleyi baştan yaz.",
    P("1. ikileme:", "koşa koşa", ["koşa-koşa", "koşakoşa"], k=["koşa koşa"]),
    P("2. ikileme:", "ağır ağır", ["ağırağır", "ağır-ağır"], k=["ağır ağır"])),
 ("m9i2", "b"): IK("Noktalı virgül; özneden sonra konur.", ["uygun işareti", "kullanım amacını"], "İşaret + amaç → “Noktalı virgül / Üç nokta; çünkü …” İkisini de yaz.",
    P("İşaret:", "noktalı virgül", ["üç nokta", "soru işareti"], k=["noktalı virgül"]),
    P("Amacı: isimler sıralanmadan önce", "özneyi ayırmak", ["cümleyi bitirmek", "sözü okura bırakmak"], k=["özne"])),
 ("m9i2", "c"): IK("Üç nokta; cümle tamamlanmamış.", ["uygun işareti", "kullanım amacını"], "İşaret + amaç → “Noktalı virgül / Üç nokta; çünkü …” İkisini de yaz.",
    P("İşaret:", "üç nokta", ["noktalı virgül", "iki nokta"], k=["üç nokta"]),
    P("Amacı: cümle", "tamamlanmamış, yarım kalmış", ["soru soruyor", "özneyle başlıyor"], k=YARIM)),
 ("m10i1", "a"): IK("Giriş: okumanın hayatımızdaki önemi. Gelişme: kelime ve hayal gücü gelişir, örnek. Sonuç: okumayı alışkanlık edinmeliyiz.", ["taslak hâlinde"], "Taslak → 3 satır: “Giriş: … Gelişme: … Sonuç: …”",
    P("Giriş (konuyu tanıt):", "okumanın hayatımızdaki önemi", ["en sevdiğim yemek", "dünkü maç"], k=["önem", "hayat", "yeri"]),
    P("Gelişme (açıkla, örnek ver):", "kelime hazinesi ve hayal gücü gelişir", ["televizyon çok güzel", "oyun oynarım"], k=["kelime", "hayal", "bilgi"]),
    P("Sonuç (toparla):", "okumayı alışkanlık hâline getirmeliyiz", ["kitaplar ağırdır", "yarın tatil"], k=["alışkanlık", "okumalıyız", "edinmeli"])),
 ("m10i1", "b"): IK("Okumak hayatımızda çok önemlidir. Kelime hazinemiz ve hayal gücümüz gelişir. Sonuç olarak okumayı alışkanlık hâline getirmeliyiz.", ["Taslağınıza uygun bir metin"], "Metin → her bölüme 1–2 cümle; örneği “Örneğin …”, sonucu “Sonuç olarak …” ile yaz.",
    P("Giriş: Okumak", "hayatımızda çok önemlidir", ["bazen sıkıcıdır", "pahalıdır"], k=["önem", "hayat"]),
    P("Gelişme: Okuyan kişinin", "kelime hazinesi ve hayal gücü gelişir", ["gözleri yorulur", "çantası ağırlaşır"], k=["kelime", "hayal", "örne"]),
    P("Sonuç olarak", "okumayı alışkanlık hâline getirmeliyiz", ["kitapları kaldırmalıyız", "hiç açmamalıyız"], k=["alışkanlık", "okumalıyız"])),
 ("m10i2", "a"): IK("Karşılaştırma-zıtlık; çünkü benzer ve farklı yönler anlatılacak.", ["amacınıza en uygun olanı"], "Yapı seç → benzer + farklı yön anlatılacaksa “karşılaştırma-zıtlık” + çünkü.",
    P("Yapı:", "karşılaştırma-zıtlık", ["sıralı-kronolojik", "tanıtıcı"], k=["karşılaştırma"]),
    P("Çünkü iki yöntemin", "benzer ve farklı yönleri anlatılacak", ["olay sırası anlatılacak", "yalnız biri tanıtılacak"], k=["benzer", "farklı", "ortak"])),
 ("m10i2", "b"): IK("İkisi de öğrenmeyi kolaylaştırır. Kartlar tekrara, kavram haritası ise ilişki kurmaya yardım eder. Sonuç olarak ikisi de işe yarar.", ["benzer ve farklı yönlerini"], "Karşılaştırma metni → “İkisi de …” + “oysa / ise …” + “Sonuç olarak …”.",
    P("Benzer yön:", "ikisi de öğrenmeyi kolaylaştırır", ["kartlar kırmızıdır", "harita çok büyüktür"], k=["ikisi de", "her iki", "ikisinde de"]),
    P("Farklı yön:", "kartlar tekrara, kavram haritası ise ilişki kurmaya yardım eder", ["ikisi aynı renktedir", "ikisi de kâğıttır"], k=["oysa", " ise", "ilişki"]),
    P("Toparla:", "sonuç olarak ikisi de işe yarar", ["kartlar kayboldu", "harita yırtıldı"], k=["sonuç olarak", "kısacası"])),
}
for q in Y.d["mebSorular"]:
    for i, z in enumerate(q.get("ikizler", [])):
        zid = z.get("id") or f"{q['id']}i{i + 1}"
        for m in z["maddeler"]:
            b = IKIZ.get((zid, m["harf"]))
            if b: m.update(b)
            else: raise SystemExit(f"ikiz verisi eksik: {zid} {m['harf']}")

# =====================================================================
# HECE'NİN CEVABINI DÜZELT: 8 eksik (yarım cevap) + 3 yanılgı (yalnız Hatırla'daki sık hatalardan)
# =====================================================================
def KH(kazanim, tur, soru, kuark, dogruSik, yanlis1, yanlis2, ipucu, aciklama, once, ornek, sonra, k, havuz):
    Y.kuark(kazanim=kazanim, tur=tur, soru=soru, kuark=kuark, secenekler=[dogruSik, yanlis1, yanlis2], dogru=0, ipucu=ipucu, aciklama=aciklama,
            dogruCevap=f"{once} {ornek} {sonra}".replace(" .", ".").replace(" !", "!").replace(" ;", ";").strip(), tamamla={"once": once, "ornek": ornek, "sonra": sonra, "k": k, "havuz": havuz})

TAM, DOGRU_ = "Tam, eksik yok.", "Doğru, hata yok."
KH(K1, "eksik", "HÜRKUŞ metnindeki “teçhizat” kelimesinin anlamını tahmin ediniz.", "Uçakta olan şeyler.",
   "Eksik: anlam belirsiz; ne tür şeyler olduğu (araç gereç) yazılmalı.", "Yanlış: “teçhizat: teçhizatlı olmak” yazmalı.", TAM,
   "Cümle “pilotların ihtiyaç duyduğu birçok teçhizat” diyor.", "Teçhizat, bir görev için gereken araç gereç ve donanımlardır. (MEB örnek sorusu)",
   "Bir görev için gereken", "araç gereçler", ".", TECHIZAT, ["uçuş saatleri", "pilot isimleri"])
KH(K2, "eksik", "Arılar metninin konusunu yazınız.", "Arılar.",
   "Eksik: arılar hakkında ne anlatıldığı yazılmamış.", "Yanlış: konu bir ders cümlesi olmalı.", TAM,
   "Arıların neyi anlatılıyor?", "Konu kısa yazılır ama neyin anlatıldığını söyler: “Arıların doğadaki önemi.” (s. 22)",
   "Arıların", "doğadaki önemi", ".", KONU_DEGER, ["kanat rengi", "uyku saati"])
KH(K2, "eksik", "Tabelalar metninin ana düşüncesini yazınız.", "Dil.",
   "Eksik: ana düşünce bir cümledir; yazarın ne demek istediği yazılmalı.", "Yanlış: konu “tabelalar” olmalı.", TAM,
   "Ana düşünce tek kelime mi, cümle mi?", "Ana düşünce yazarın asıl söylemek istediği, bir cümledir. (s. 17)",
   "Dilimize sahip çıkmalıyız, çünkü dil", "kimliğimizdir", ".", ["kimli", "kültür"], ["çok zordur", "yabancıdır"])
KH(K3, "eksik", "Forsa metnindeki “bitap” kelimesinin anlamını tahmin edip gerekçesini yazınız.", "Yorgun.",
   "Eksik: gerekçe yok; metinden ipucu yazılmalı.", "Yanlış: tahmin “neşeli” olmalı.", TAM,
   "Soru kaç şey istiyor?", "Tahmin + metin içi gerekçe: “kolları eski kuvvetini kaybetmiş.” (MEB örnek sorusu)",
   "Yorgun; çünkü metinde", "“kolları eski kuvvetini kaybetmiş”", "yazıyor.", BITAP_G, ["“ufukta bir yelkenli”", "“serin pınarlar”"])
KH(K3, "eksik", "Forsa metnindeki “iştiyak” kelimesinin anlamını tahmin edip gerekçesini yazınız.", "Çünkü metinde “yanıp tutuşurdu” yazıyor.",
   "Eksik: gerekçe var ama tahmin (anlam) yazılmamış.", "Yanlış: gerekçeye kendi fikrini yazmalı.", TAM,
   "Kelimenin anlamı nerede?", "İştiyak: özlem, çok isteme. (MEB örnek sorusu)",
   "Anlamı", "özlem, çok isteme", "; çünkü “yanıp tutuşurdu” yazıyor.", ["özlem", "istek", "arzu", "hasret", "çok iste"], ["korku, kaçma", "uyku, dinlenme"])
KH(K4, "eksik", "“apar-topar … hızlıhızlı” ikilemelerini doğru yazınız.", "apar topar",
   "Eksik: ikinci ikileme (hızlı hızlı) düzeltilmemiş.", "Yanlış: “apar-topar” doğrudur.", TAM,
   "Cümlede kaç ikileme vardı?", "İkilemeler ayrı ve çizgisiz yazılır: apar topar, hızlı hızlı. (s. 34)",
   "apar topar ve", "hızlı hızlı", "", ["hızlı hızlı"], ["hızlıhızlı", "hızlı-hızlı"])
KH(K4, "eksik", "“Genç şairimiz ( ) Necip Fazıl, Nâzım Hikmet…” Boşluğa gelen işareti ve amacını yazınız.", "Noktalı virgül.",
   "Eksik: amacı yazılmamış.", "Yanlış: buraya üç nokta gelir.", TAM,
   "Soru “kullanım amacını” da istiyor.", "Özneden sonra noktalı virgül konabilir. (s. 49)",
   "Noktalı virgül; çünkü", "özneden sonra konur", ".", ["özne"], ["cümle bitti", "soru soruluyor"])
KH(K5, "eksik", "“Doğa sevgisi” metninin taslağını yazınız.", "Giriş: doğanın önemi. Gelişme: geri dönüşüm, fidan dikmek.",
   "Eksik: sonuç bölümü yok.", "Yanlış: taslakta yalnız giriş olur.", TAM,
   "Taslakta kaç bölüm olmalı?", "Bilgilendirici metin: giriş, gelişme, sonuç. (s. 167)",
   "Sonuç:", "doğayı korumak hepimizin görevi", ".", SON, ["bugün hava güzel", "doğa resmi çizdim"])
KH(K4, "yanilgi", "“Yarışmacılar sahneye teker-teker çağrıldı.” cümlesini düzeltiniz.", "Doğru yazılmış; ikilemelerin arasına kısa çizgi konur.",
   "Yanlış: ikilemelerin arasına kısa çizgi konmaz; “teker teker” yazılır.", "Yanlış: bitişik “tekerteker” yazılır.", DOGRU_,
   "İkilemelerin arasına işaret konur mu?", "İkilemeler ayrı yazılır, arasına kısa çizgi ya da virgül konmaz. (s. 34)",
   "Ayrı ve çizgisiz:", "teker teker", "çağrıldı.", ["teker teker"], ["teker-teker", "tekerteker"])
KH(K2, "yanilgi", "Arılar metninin konusunu yazınız.", "Arıları korumalıyız, çünkü doğa için önemlidirler.",
   "Yanlış: bu ana düşünce; konu kısa yazılır: “Arıların doğadaki önemi.”", "Yanlış: konu “bal” olmalı.", DOGRU_,
   "Konu kısa mı, ders veren cümle mi?", "Konu, metinde neyin anlatıldığıdır; kısa yazılır. Ders veren cümle ana düşüncedir. (s. 17, 22)",
   "Konu kısa yazılır: arıların", "doğadaki önemi", ".", ["önem", "görev", "rol"], ["korunması gerektiği", "balı çok tatlıdır"])
KH(K3, "yanilgi", "Forsa metnindeki “bitap” kelimesinin gerekçesini yazınız.", "Gerekçe: Bence yaşlı insanlar hep yorgun olur.",
   "Yanlış: gerekçe kendi fikrin değil, metindeki ipucudur.", "Yanlış: gerekçe yazmaya gerek yok.", DOGRU_,
   "Gerekçe nereden alınır?", "Gerekçe metin içi ipucudur: “bir kemik torbasına dönmüştü.” (MEB örnek sorusu)",
   "Gerekçe metinden alınır:", "“bir kemik torbasına dönmüştü”", "", BITAP_G, ["“bence yaşlılar yorulur”", "“dedem de yorgundur”"])

# =====================================================================
# PROVA YAZILILARI (2 deneme; Senaryo 5 dağılımı: 1 + 2 + 1 + 1 + 1 soru, toplam 100; puanlar tahmini). Bağlamlar MEB ve benzerlerinden farklı.
# =====================================================================
Y.prova(id="p1", ad="Prova 1", sorular=[
    {"kazanim": K1, "puan": 15, "benzer": "m1",
     "metin": ["İşçiler, depoya getirilen ağır kutuları birlikte taşıdı.", "Toplantıda herkes müdürün yaptığı ağır eleştiriler karşısında sessiz kaldı.",
               "Yukarıdaki cümlelerde “ağır” sözcüğü farklı anlamlarda kullanılmıştır."],
     "maddeler": [M("a", "1. cümlede “ağır” sözcüğünün anlamını yazınız.", "Kütlesi fazla olan, taşınması güç.",
                    [A("Kütlesi fazla, taşınması güç", "kütle", "taşınması güç", "zor taşın", "kilo", "hafif olmayan")], "anlam", puan=7),
                  M("b", "2. cümlede “ağır” sözcüğünün anlamını yazınız.", "Sert, kırıcı, etkisi güçlü.",
                    [A("Sert, kırıcı", "sert", "kırıcı", "incit", "üzücü", "etkisi güçlü")], "anlam", puan=8)]},
    {"kazanim": K2, "puan": 15, "benzer": "m2",
     "metin": ["İlçenin yakınındaki yıllardır kullanılmayan taş değirmen, belediye tarafından onarılarak Doğa Tanıtım Merkezi hâline getirildi. Merkez, 6 Nisan Cumartesi günü ziyaretçilere açıldı. Alt katta bölgedeki bitki ve hayvanları tanıtan fotoğraflar sergilenirken üst katta çocukların inceleme yapabileceği küçük bir gözlem bölümü oluşturuldu. Bahçeye ise farklı kuş türlerinin yararlanması için ahşap yuvalar yerleştirildi. Merkez, pazartesi günleri dışında 10.00-17.00 saatleri arasında ziyaret edilebilecek."],
     "maddeler": [M("a", "Doğa Tanıtım Merkezi hangi gün ziyaretçilere açılmıştır?", "6 Nisan Cumartesi günü açılmıştır.", [A("6 Nisan Cumartesi", "6 nisan", "cumartesi")], "bilgi", puan=5),
                  M("b", "Bitki ve hayvanları tanıtan fotoğraflar binanın hangi bölümünde sergilenmektedir?", "Binanın alt katında sergilenmektedir.", [A("Alt kat", "alt kat")], "bilgi", puan=5),
                  M("c", "Merkez haftanın hangi günü ziyaret edilemeyecektir?", "Pazartesi günü ziyaret edilemeyecektir.", [A("Pazartesi", "pazartesi")], "bilgi", puan=5)]},
    {"kazanim": K2, "puan": 15, "benzer": "m2",
     "metin": ["Bir iyiliğin değerini, onu kaç kişinin gördüğü değil hangi niyetle yapıldığı belirler. Bazı insanlar yardım ettiklerini sürekli anlatır, yaptıkları küçük bir iyiliğin bile herkes tarafından bilinmesini ister. Oysa gerçekten yardımsever olan kişi, karşılık ya da övgü beklemeden başkasının ihtiyacını gidermeye çalışır. İyilik, gösterişe dönüştüğünde samimiyetini kaybedebilir."],
     "maddeler": [M("a", "Bu metnin ana düşüncesini kendi cümlelerinizle yazınız.", "Gerçek iyilik, övgü ve karşılık beklemeden samimi bir niyetle yapılır; gösteriş için yapılan iyilik değerini kaybeder.",
                    [A("Karşılık beklemeden, samimi niyetle", "karşılık", "övgü", "samimi", "niyet"), A("Gösteriş iyiliğin değerini düşürür", "gösteriş", "değerini kaybed", "değer")], "ana", puan=15)]},
    {"kazanim": K3, "puan": 15, "benzer": "m6",
     "metin": ["Okul korosunda solo söyleyecek olan Elif, sahneye çıkmadan önce çok heyecanlandı. Ancak şarkısını başarıyla tamamlayıp salondan büyük alkış alınca öğretmeninin yüzü güldü. Elif'in gösterdiği başarı öğretmenini çok sevindirmişti."],
     "maddeler": [M("a", "“Yüzü gülmek” deyiminin anlamını tahmin ediniz ve sizi bu tahmine götüren metin içi gerekçeyi yazınız.",
                    "Tahminim: sevinmek, mutlu olmak. Gerekçem: Metinde “Elif'in gösterdiği başarı öğretmenini çok sevindirmişti” yazıyor.",
                    [A("Tahmin: sevinmek, mutlu olmak", "sevin", "mutlu", "memnun"), A("Gerekçe: metindeki ipucu", "sevindirmişti", "başarı", "alkış")], "gerekce", puan=15)]},
    {"kazanim": K4, "puan": 20, "benzer": "m9", "metin": ["Aşağıda yer alan yazım ve noktalama ile ilgili soruları cevaplayınız."],
     "maddeler": [M("a", "“Rüzgâr esince yapraklar yavaş-yavaş, sallanasallana yere düştü.” cümlesindeki yanlış yazılmış ikilemeleri düzelterek cümleyi yeniden yazınız.",
                    "Rüzgâr esince yapraklar yavaş yavaş, sallana sallana yere düştü.", [A("yavaş yavaş", "yavaş yavaş"), A("sallana sallana", "sallana sallana")], "ikileme", puan=8),
                  M("b", "“Kardeşim ( ) kalemini, silgisini ve defterini çantasına koydu.” Boşluğa uygun işareti getiriniz ve kullanım amacını belirtiniz.",
                    "Noktalı virgül (;). Amacı: Sıralanan ögeler arasında virgül olduğu için özneden sonra konur.", [A("noktalı virgül", "noktalı virgül"), A("Amaç: özneden sonra", "özne")], "isaret", puan=6),
                  M("c", "“— Ödevini bitirdin mi? — Şey ( )” Boşluğa uygun işareti getiriniz ve kullanım amacını belirtiniz.",
                    "Üç nokta (...). Amacı: Karşılıklı konuşmada yeterli olmayan, eksik bırakılan cevabı göstermek.", [A("üç nokta", "üç nokta", "..."), A("Amaç: eksik bırakılan cevap", "eksik", "yarım", "cevap", "tamamlanma")], "isaret", puan=6)]},
    {"kazanim": K5, "puan": 20, "benzer": "m10", "metin": ["“Spor yapmanın faydaları” temalı bilgilendirici bir metin yazmayı planladığınızı düşününüz."],
     "maddeler": [M("a", "Bu metnin giriş, gelişme ve sonuç bölümlerinde hangi içeriklere yer vereceğinizi taslak hâlinde yazınız.",
                    "Giriş: Sporun hayatımızdaki önemi. Gelişme: Sporun faydaları; kaslar güçlenir, uyku düzelir, örneğin her gün yürüyüş yapmak. Sonuç: Sporu her gün yapılan bir alışkanlık hâline getirmeliyiz.",
                    [A("Giriş: sporun önemi", "önem", "hayat"), A("Gelişme: faydalar ve örnek", "güçlen", "sağlık", "uyku", "örne", "fayda"), A("Sonuç: alışkanlık", "alışkanlık", "yapmalıyız", "getirmeliyiz")], "taslak", puan=10),
                  M("b", "Taslağınıza uygun bir metin yazınız.",
                    "Spor, sağlıklı bir hayatın en önemli parçalarından biridir. Düzenli spor yapan kişinin kasları güçlenir, uykusu düzelir ve kendini daha mutlu hisseder. Örneğin her gün yarım saat yürümek bile vücudumuza iyi gelir. Sonuç olarak sporu alışkanlık hâline getirmeliyiz.",
                    [A("Giriş: sporun önemi", "önem", "hayat"), A("Gelişme: faydalar ve örnek", "güçlen", "sağlık", "uyku", "örne"), A("Sonuç", "sonuç olarak", "alışkanlık")], "metin", puan=10)]}])

Y.prova(id="p2", ad="Prova 2", sorular=[
    {"kazanim": K1, "puan": 15, "benzer": "m1",
     "metin": ["Köyün girişindeki eski taş köprü yıllarca bakımsız kalmış, harap bir hâle gelmişti. Taşları yerinden oynamış, korkulukları kırılmıştı. Belediye köprüyü onarınca köprü yeniden sağlam ve güzel görünmeye başladı.",
               "Aşağıdaki kelimelerin anlamını metinden hareketle tahmin ediniz."],
     "maddeler": [M("a", "harap: Bu kelimenin metindeki anlamını tahmin edip yazınız.", "Harap: Yıkık dökük, çok kötü durumda, bakımsız.",
                    [A("Yıkık dökük, kötü durumda", "yıkık", "kötü durum", "bakımsız", "bozuk", "eskimiş", "yıpran")], "anlam", puan=8),
                  M("b", "onarmak: Bu kelimenin metindeki anlamını tahmin edip yazınız.", "Onarmak: Bozulmuş bir şeyi tamir etmek, düzeltmek.",
                    [A("Tamir etmek, düzeltmek", "tamir", "düzelt", "yenile", "sağlamlaştır")], "anlam", puan=7)]},
    {"kazanim": K2, "puan": 15, "benzer": "m2",
     "metin": ["Mahalle kütüphanesine kitap ödünç alma işlemlerini hızlandırmak için otomatik işlem cihazları yerleştirildi. Okurlar artık kitaplarını birkaç dakika içinde alıp çıkabiliyordu. Bir süre sonra kütüphaneci, eskiden ziyaretçilerin kendisine kitap önerisi sorduğunu ve okudukları eserler hakkında sohbet ettiğini; şimdi ise çoğu kişinin cihazdan işlemini yapıp hemen ayrıldığını fark etti. Bir gün çalışma arkadaşına, “Kitaplar daha hızlı el değiştiriyor ama sohbetler raflarda kaldı.” dedi."],
     "maddeler": [M("a", "Metnin konusunu yazınız.", "Teknolojinin kütüphanede insanlar arasındaki sohbeti azaltması.",
                    [A("Teknoloji, cihazlar", "teknoloji", "cihaz", "otomatik", "makine"), A("Sohbetin, iletişimin azalması", "sohbet", "iletişim", "konuşma")], "konu", puan=15)]},
    {"kazanim": K2, "puan": 15, "benzer": "m2",
     "metin": ["Dünyadaki suyun çok küçük bir bölümü içilebilir tatlı sudur. Üstelik nüfus arttıkça bu suya duyulan ihtiyaç da her geçen gün büyüyor. Dişlerimizi fırçalarken musluğu açık bırakmak, bulaşıkları akan suyun altında yıkamak gibi küçük alışkanlıklar her gün litrelerce suyun boşa gitmesine yol açıyor. Bu nedenle suyu dikkatli kullanmak, gelecek nesillere karşı hepimizin sorumluluğudur."],
     "maddeler": [M("a", "Bu metnin ana düşüncesini kendi cümlelerinizle yazınız.", "Tatlı su azdır; bu yüzden suyu israf etmeden, dikkatli kullanmalıyız.",
                    [A("Suyu dikkatli kullanmalıyız", "dikkatli kullan", "israf", "boşa harca", "tasarruf", "korumalı"), A("Çünkü tatlı su az, gelecek için sorumluluk", "azdır", "sınırlı", "sorumlu", "gelecek")], "ana", puan=15)]},
    {"kazanim": K3, "puan": 15, "benzer": "m6",
     "metin": ["Zil çalınca öğrenciler büyük bir telaşla çantalarını toplayıp kapıya koştu. Birkaç dakika sonra koridorlar boşaldı ve okulda derin bir sükûnet başladı; yalnızca duvardaki saatin tik takları duyuluyordu."],
     "maddeler": [M("a", "sükûnet: Kelimenin anlamına dair tahmininizi ve sizi bu tahmine götüren metin içi gerekçeyi yazınız.",
                    "Tahminim: sessizlik, sakinlik. Gerekçem: Metinde “koridorlar boşaldı” ve “yalnızca duvardaki saatin tik takları duyuluyordu” yazıyor.",
                    [A("Tahmin: sessizlik, sakinlik", "sessiz", "sakin", "huzur"), A("Gerekçe: metindeki ipucu", "boşaldı", "tik tak", "yalnızca")], "gerekce", puan=15)]},
    {"kazanim": K4, "puan": 20, "benzer": "m9", "metin": ["Aşağıda yer alan yazım ve noktalama ile ilgili soruları cevaplayınız."],
     "maddeler": [M("a", "“Bayramda herkes güle-güle sohbet etti, çocuklar da ikişerikişer bahçeye çıktı.” cümlesindeki yanlış yazılmış ikilemeleri düzelterek cümleyi yeniden yazınız.",
                    "Bayramda herkes güle güle sohbet etti, çocuklar da ikişer ikişer bahçeye çıktı.", [A("güle güle", "güle güle"), A("ikişer ikişer", "ikişer ikişer")], "ikileme", puan=8),
                  M("b", "“Annem pazardan elma, armut aldı ( ) babam fırından ekmek, simit getirdi.” Boşluğa uygun işareti getiriniz ve kullanım amacını belirtiniz.",
                    "Noktalı virgül (;). Amacı: Ögeleri arasında virgül bulunan sıralı cümleleri birbirinden ayırmak.", [A("noktalı virgül", "noktalı virgül"), A("Amaç: sıralı cümleleri ayırır", *SIRALI)], "isaret", puan=6),
                  M("c", "“Masada sıcak çorba, taze ekmek, mis kokulu börekler ( ) Herkes sofraya koştu.” Boşluğa uygun işareti getiriniz ve kullanım amacını belirtiniz.",
                    "Üç nokta (...). Amacı: Cümle tamamlanmamış, yarım bırakılmış; sözün gerisi okuyucuya bırakılmıştır.", [A("üç nokta", "üç nokta", "..."), A("Amaç: cümle tamamlanmamış", *YARIM)], "isaret", puan=6)]},
    {"kazanim": K5, "puan": 20, "benzer": "m10", "metin": ["“Teknolojiyi bilinçli kullanmak” temalı bilgilendirici bir metin yazmayı planladığınızı düşününüz."],
     "maddeler": [M("a", "Bu metnin giriş, gelişme ve sonuç bölümlerinde hangi içeriklere yer vereceğinizi taslak hâlinde yazınız.",
                    "Giriş: Teknolojinin hayatımızdaki yeri ve önemi. Gelişme: Bilinçli kullanım yolları; ekran süresini sınırlamak, kişisel bilgileri paylaşmamak, örneğin akşamları telefonu bırakmak. Sonuç: Teknolojiyi kontrollü kullanmak hepimizin sorumluluğudur.",
                    [A("Giriş: teknolojinin önemi", "önem", "hayat", "yeri"), A("Gelişme: bilinçli kullanım yolları, örnek", "süre", "sınırla", "paylaşma", "örne"), A("Sonuç: hepimizin sorumluluğu", "sorumlu", "görev", "hepimiz", "kullanmalıyız")], "taslak", puan=10),
                  M("b", "Taslağınıza uygun bir metin yazınız.",
                    "Teknoloji, hayatımızı kolaylaştıran önemli bir araçtır. Ancak onu bilinçli kullanmazsak zarar görebiliriz. Ekran süremizi sınırlamalı ve kişisel bilgilerimizi paylaşmamalıyız. Örneğin akşam yemeğinde telefonu bırakıp ailemizle sohbet edebiliriz. Sonuç olarak teknolojiyi kontrollü kullanmak hepimizin sorumluluğudur.",
                    [A("Giriş: teknolojinin önemi", "önem", "hayat"), A("Gelişme: yollar ve örnek", "sınırla", "paylaşma", "örne"), A("Sonuç", "sonuç olarak", "sorumlu")], "metin", puan=10)]}])

Y.yaz()
