"""İngilizce (Own It) 7 · 1. Dönem 1. Yazılı — Yazılıya Hazırlık verisi.
OYYS senaryosu YOK: öğretmen 8 soruluk "Seçmeli Studying Paper" gönderdi (10 Kasım 2026), yazılıda AYNI sorular sorulacak; sınav 11 Kasım 2026.
Kemal'in kararı (10 Kasım 2026): yeni soru, benzer soru, prova yok; yalnız bu 8 soru kitaba ve genel İngilizce kurallarına göre cevaplanır,
aşama aşama ezberletilir. Soru 6'daki yonca simgeleri taramada silik: Patty-golf 3 dolu yaprak (usually), Patty-cycling 0 (never) Kemal'in
kâğıttan doğrulaması; diğer kutular taramadan okundu.
Kaynaklar: öğretmenin kâğıdı; Own it! 3 WB s. 86 (adverbs of frequency, past simple), WB s. 9 (Derek Rabelo … in 1992);
İngilizce 7 (MEB, Bilim Kültür) s. 10–14 (görünüş/kişilik sıfatları), s. 16 (younger than, more hardworking than).
Çalıştır: python3 araclar/yazili/own1_d1y1.py"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from yazili import Yazili
import cizim_ing as ZI
import cizim_own as Z


def A(ad, *k): return {"ad": ad, "k": list(k)}
def AS(ad, *sira): return {"ad": ad, "sira": [list(x) for x in sira]}
def M(harf, soru, cevap, an, iskele=None, kisa=None, tetik=None, notu=None, formul=None):
    m = {"harf": harf, "soru": soru}
    if formul: m["formul"] = formul
    if iskele: m["iskele"] = iskele
    m["cevap"] = cevap; m["anahtarlar"] = an
    m["kisaCevap"] = kisa or cevap
    if tetik: m["tetik"] = tetik
    if notu: m["kalipNot"] = notu
    return m
def SEC(soru, secenekler, aciklama, dogru=0): return {"tur": "secim", "soru": soru, "secenekler": secenekler, "dogru": dogru, "aciklama": aciklama}

K1, K2, K3, K4 = "Sıfatlar", "Karşılaştırma", "Geçmiş zaman", "Sıklık"
AP = "’"

Y = Yazili("own1", "d1y1",
    baslik="1. Dönem 1. Yazılı", ders="İngilizce (Own It)", senaryo="Öğretmenin çalışma kâğıdı", sure=40, tarih="2026-11-11",
    dagilim={K1: 2, K2: 2, K3: 3, K4: 1},
    soruBaslik="Öğretmenin Soruları", soruEtiket="Soru", kazanimAd="konu", ikizsiz=True,
    soruGiris="Bunlar öğretmeninin kâğıdındaki <b>8 soru</b>, kâğıttaki gibi. Yazılıda <b>aynısı</b> çıkacak. Kâğıtta ne yapacaksan burada da onu yap: kutulara yerleştir, boşluğa yaz, doğru kelimeyi seç.",
    giris="Öğretmeninin kâğıdındaki <b>8 soru</b> yazılıda <b>aynen</b> çıkacak. Önce 4 konu kartını oku ve boşlukları doldur. Sonra 8 soruyu sırayla çöz. En sonda Kısa Cevap Kartları ile her cevabı bir kez daha hatırla.",
    kapsamDisi=["Kâğıtta olmayan her şey: öğretmen bu 8 sorunun aynısını soracak", "Own It ünitelerindeki diğer konular (present perfect, used to…)"],
    puanNotu="Kâğıtta yalnız 1. ve 7. sorunun puanı yazıyor (20'şer puan). Diğerlerinin puanı belli değil.",
    kaynakNotu=("Sorular öğretmenin çalışma kâğıdından. Cevaplar: Own it! 3 Workbook s. 86 (sıklık zarfları, past simple), WB s. 9 "
                "(in 1992); İngilizce 7 ders kitabı (MEB) s. 10–16 (görünüş, kişilik, karşılaştırma). Karşılaştırma yazım kuralları "
                "(hotter, funnier, more expensive) ve düzensiz fiiller genel İngilizce kurallarıdır."),
    beklemesiz=True)

# =====================================================================
# KONU KARTLARI (Hatırla ve Tekrarla)
# =====================================================================
Y.kazanim(kod=K1, ad="Kişileri görünüş ve kişilik sıfatlarıyla anlatır.", kisa="Görünüş ve Kişilik", soru=2,
    soruNot="Kâğıtta 2 soru: 1, 2", renk="#7a5ce0", konular=["u1k1", "u1k2"], sayfa="MEB kitabı s. 10–14", svg=ZI.h_gorunus(),
    maddeler=["<b>Appearance</b> (görünüş) = gözle görülen: <b>handsome</b> (yakışıklı), <b>slim</b> (ince), <b>overweight</b> (kilolu), <b>tall</b> (uzun boylu), <b>brown eyes</b> (kahverengi gözler).",
              "<b>Personality</b> (kişilik) = davranış: <b>punctual</b> (dakik), <b>stubborn</b> (inatçı), <b>thoughtful</b> (düşünceli), <b>honest</b> (dürüst), <b>friendly</b> (arkadaş canlısı).",
              "Ayırma yolu: <b>Fotoğrafta görünür mü?</b> Görünürse Appearance, görünmezse Personality.",
              "Soru 2: doesn't tell lies → <b>honest</b> · helps poor people → <b>generous</b> · says “thank you” → <b>polite</b>.",
              "Soru 2: never late → <b>punctual</b> · never does homework → <b>lazy</b>. (MEB kitabı s. 10, 14)"],
    kelimeler=["görünür = Appearance", "davranış = Personality", "honest = dürüst", "generous = cömert", "polite = kibar", "punctual = dakik", "lazy = tembel"],
    hatalar=[{"yanlis": "tall → Personality", "dogru": "tall fotoğrafta görünür → Appearance"},
             {"yanlis": "punctual → Appearance", "dogru": "punctual (dakik) bir davranış → Personality"},
             {"yanlis": "says “thank you” → generous", "dogru": "“thank you” diyen kibar → polite; fakirlere yardım eden → generous"}],
    tekrar=[{"c": "“Categorize the words.” = Kelimeleri {grupla|çevir|ezberle}.", "s": "sınav yönergesi"},
            {"c": "“Complete the sentences with adjectives in the box.” = Kutudaki {sıfatlarla|fiillerle} cümleleri tamamla.", "s": "sınav yönergesi"},
            {"c": "handsome, slim, overweight, tall, brown eyes → {Appearance|Personality}", "s": "Soru 1"},
            {"c": "punctual, stubborn, thoughtful, honest, friendly → {Personality|Appearance}", "s": "Soru 1"},
            {"c": "My brother doesn't tell lies. He is {honest|lazy|polite}.", "s": "Soru 2"},
            {"c": "Selin helps poor people. She is {generous|punctual|lazy}.", "s": "Soru 2"},
            {"c": "My sister always says “thank you”. She is a {polite|generous|lazy} person.", "s": "Soru 2"},
            {"c": "Sevda teacher is never late: {punctual|polite|honest}. My daughter never does her homework: {lazy|generous|honest}.", "s": "Soru 2"}])

Y.kazanim(kod=K2, ad="İki şeyi sıfatların karşılaştırma hâliyle karşılaştırır.", kisa="Karşılaştırma (-er / more)", soru=2,
    soruNot="Kâğıtta 2 soru: 3, 8", renk="#d9480f", konular=["u1k1"], sayfa="MEB kitabı s. 16 + genel kural", svg=ZI.h_karsilastir(),
    maddeler=["Kısa sıfat + <b>-er than</b>. Sonu sessiz-sesli-sessiz ise son harf iki kez: <b>hot → hotter</b>, <b>slim → slimmer</b>.",
              "Sonu <b>-y</b> ise y düşer, <b>-ier</b> gelir: <b>funny → funnier</b>.",
              "Uzun sıfat: <b>more … than</b>: <b>more expensive</b>, <b>more selfish</b>. (MEB s. 16: more hardworking than)",
              "Düzensiz: <b>good → better</b>.",
              "Soru 8: tabloda büyük sayı daha sıcak (<b>hotter</b>), küçük sayı daha soğuk (<b>colder</b>). Yesterday → <b>was</b>, today → <b>is</b>.",
              "Soru 8: Antalya dün 29, Ağrı dün 11 → doğru şık <b>D) Antalya was hotter than Ağrı yesterday.</b>"],
    kelimeler=["hot → hotter", "slim → slimmer", "funny → funnier", "good → better", "more expensive", "more selfish", "büyük sayı = hotter"],
    hatalar=[{"yanlis": "hoter, slimer", "dogru": "hotter, slimmer (son harf iki kez)"},
             {"yanlis": "more good, gooder", "dogru": "better"},
             {"yanlis": "expensiver, selfisher", "dogru": "more expensive, more selfish"}],
    tekrar=[{"c": "“Write the comparatives of the adjectives.” = Sıfatların {karşılaştırma hâlini|geçmiş hâlini} yaz.", "s": "sınav yönergesi"},
            {"c": "“Which one is TRUE?” = Hangisi {doğru|yanlış}?", "s": "sınav yönergesi"},
            {"c": "Antalya is {hotter|hoter|more hot} than Ağrı.", "s": "Soru 3"},
            {"c": "A computer is {more expensive|expensiver} than radio.", "s": "Soru 3"},
            {"c": "Milk is {better|gooder|more good} than coffee.", "s": "Soru 3"},
            {"c": "My cousin is {slimmer|slimer} than my sister. Ünal teacher is {funnier|funnyer} than me.", "s": "Soru 3"},
            {"c": "My sister is {more selfish|selfisher} than my brother.", "s": "Soru 3"},
            {"c": "Yesterday: Antalya 29, Ağrı 11 → Antalya {was hotter|was colder} than Ağrı yesterday.", "s": "Soru 8"}])

V2 = [("go", "went", "gitmek"), ("swim", "swam", "yüzmek"), ("give", "gave", "vermek"), ("do", "did", "yapmak"), ("become", "became", "olmak"),
      ("hear", "heard", "duymak"), ("leave", "left", "ayrılmak"), ("know", "knew", "bilmek"), ("see", "saw", "görmek"), ("understand", "understood", "anlamak")]
Y.kazanim(kod=K3, ad="Geçmişi was/were ve fiillerin geçmiş hâliyle anlatır; yılları okur.", kisa="Was/Were, Yıllar, V2", soru=3,
    soruNot="Kâğıtta 3 soru: 4, 5, 7", renk="#1d6fa3", konular=["u0k2", "u1k3"], sayfa="WB s. 86, 9",
    svg=ZI.tablo_svg(["V1", "V2", "Anlam"], [list(x) for x in V2], [96, 110, 110], sat_h=25, bas_h=28, boy=13, etiket="On fiilin geçmiş hâli ve anlamı"),
    maddeler=["<b>I / he / she / it / Timmy → was</b>. <b>we / you / they / Alex and Tom → were</b>. Olumsuz: wasn't, weren't.",
              "Soru 4: a <b>wasn't</b> · b <b>were</b> · c <b>Were</b> · d <b>was</b> · e <b>were</b>.",
              "Yıllar ikişer ikişer okunur: 19 | 92 → <b>nineteen ninety-two</b>. 20 | 19 → <b>twenty nineteen</b>. 2000 → <b>two thousand</b>. (WB s. 9: born in 1992)",
              "Düzensiz fiiller (V2) ezberlenir: <b>go → went</b>, <b>swim → swam</b>, <b>give → gave</b>, <b>do → did</b>, <b>become → became</b>.",
              "<b>hear → heard</b>, <b>leave → left</b>, <b>know → knew</b>, <b>see → saw</b>, <b>understand → understood</b>. (WB s. 86: Many common verbs are irregular)"],
    kelimeler=["I / he / she → was", "we / you / they → were", "nineteen ninety-two", "twenty nineteen", "two thousand", "go → went", "see → saw"],
    hatalar=[{"yanlis": "Alex and Tom was …", "dogru": "Alex and Tom were … (iki kişi → were)"},
             {"yanlis": "goed, swimmed, knowed", "dogru": "went, swam, knew (düzensiz)"},
             {"yanlis": "1992 → one nine nine two", "dogru": "nineteen ninety-two (ikişer ikişer)"}],
    tekrar=[{"c": "“Circle the correct word.” = Doğru kelimeyi {daire içine al|çiz|yaz}.", "s": "sınav yönergesi"},
            {"c": "“Write the meanings and past forms of the verbs.” = Fiillerin {anlamlarını ve geçmiş hâllerini|resimlerini} yaz.", "s": "sınav yönergesi"},
            {"c": "Timmy {wasn't|weren't} at party last night. Alex and Tom {were|was} in the school garden.", "s": "Soru 4"},
            {"c": "I {was|were} born in Ağrı in 2001. We {were|was} at the theatre yesterday.", "s": "Soru 4"},
            {"c": "1992 = {nineteen ninety-two|nine nine two}. 2000 = {two thousand|twenty hundred}.", "s": "Soru 5"},
            {"c": "go → {went|goed}, swim → {swam|swimmed}, give → {gave|gived}, do → {did|doed}, become → {became|becomed}", "s": "Soru 7"},
            {"c": "hear → {heard|heared}, leave → {left|leaved}, know → {knew|knowed}, see → {saw|seed}, understand → {understood|understanded}", "s": "Soru 7"}])

Y.kazanim(kod=K4, ad="Sıklık zarflarıyla ne kadar sık yapıldığını anlatır.", kisa="Sıklık Zarfları", soru=1,
    soruNot="Kâğıtta 1 soru: 6 (ve 8'in sağ kutusu)", renk="#2b8a3e", konular=["u0k2"], sayfa="WB s. 86", svg=Z.lejant(),
    maddeler=["Dolu yaprak sayısı: <b>4 always</b> · <b>3 usually</b> · <b>2 often</b> · <b>1 sometimes</b> · 0 dolu = <b>rarely</b> · yalnız çizgi = <b>never</b>.",
              "Zarf fiilden <b>önce</b> gelir; Amanda/Patty/Stephen için fiile <b>-s</b>: <b>always plays</b>, <b>often goes</b>, <b>usually does</b>. (WB s. 86: before the main verb)",
              "play tennis/golf → <b>plays</b> · go cycling → <b>goes</b> · do powerlifting → <b>does</b>.",
              "Soru 6: b <b>often goes cycling</b> · c <b>usually does powerlifting</b> · d <b>usually plays golf</b>.",
              "Soru 6: e <b>never goes cycling</b> · f <b>sometimes plays tennis</b> · g <b>always plays golf</b>.",
              "Soru 8 sağ: “<b>Once a week</b>” (haftada bir) cevabının sorusu <b>How often</b> → <b>C) How often do you train?</b> (WB s. 86: once a week)"],
    kelimeler=["4 yaprak = always", "3 = usually", "2 = often", "1 = sometimes", "yalnız çizgi = never", "goes / plays / does", "How often"],
    hatalar=[{"yanlis": "Amanda goes often cycling.", "dogru": "Amanda often goes cycling. (zarf fiilden önce)"},
             {"yanlis": "Patty never go cycling.", "dogru": "Patty never goes cycling. (-s unutma)"},
             {"yanlis": "Once a week → Why do you play football?", "dogru": "Once a week → How often do you train?"}],
    tekrar=[{"c": "“Look at the table and fill in the blanks.” = Tabloya bak, {boşlukları doldur|resmi boya}.", "s": "sınav yönergesi"},
            {"c": "“What is the best question according to the answer?” = Cevaba göre en iyi {soru|cevap} hangisi?", "s": "sınav yönergesi"},
            {"c": "4 dolu yaprak = {always|often}, 3 = {usually|sometimes}, 2 = {often|never}, 1 = {sometimes|always}", "s": "Soru 6"},
            {"c": "Yalnız çizgi, hiç yaprak yok = {never|usually}", "s": "Soru 6"},
            {"c": "Amanda often {goes|go|going} cycling. Amanda usually {does|do} powerlifting.", "s": "WB s. 86"},
            {"c": "Patty usually {plays|play} golf. Patty {never|always} goes cycling.", "s": "Soru 6"},
            {"c": "Stephen {sometimes|usually} plays tennis. Stephen {always|never} plays golf.", "s": "Soru 6"},
            {"c": "Jack: Once a week. → Emma: {How often|Why|Where} do you train?", "s": "WB s. 86"}])

# =====================================================================
# CEVAP KALIPLARI (Özet'te)
# =====================================================================
Y.formul(id="grup", ad="Grupla", kalip="Appearance: … · Personality: …", ne="“Categorize the words” sorusunda", ornek="Appearance: tall · Personality: honest")
Y.formul(id="sifat", ad="Davranış → sıfat", kalip="davranış → kutudaki sıfat", ne="“Complete the sentences with adjectives” sorusunda", ornek="never late → punctual")
Y.formul(id="comp", ad="Karşılaştırma", kalip="kısa: -er · uzun: more … · good → better", ne="“Write the comparatives” sorusunda", ornek="hot → hotter, expensive → more expensive")
Y.formul(id="waswere", ad="Was / Were", kalip="I/he/she/it → was · we/you/they → were", ne="“Circle the correct word” sorusunda", ornek="Alex and Tom were …")
Y.formul(id="yil", ad="Yılı yazıyla", kalip="ikişer ikişer: 19 | 92", ne="“Write the years in words” sorusunda", ornek="1992 → nineteen ninety-two")
Y.formul(id="siklik", ad="Sıklık cümlesi", kalip="Kim + zarf + fiil-s", ne="“Look at the table and fill in the blanks” sorusunda", ornek="Amanda often goes cycling.")
Y.formul(id="v2", ad="V2 + anlam", kalip="V1 → V2 (anlam)", ne="“Write the meanings and past forms” sorusunda", ornek="go → went (gitmek)")

# =====================================================================
# ÖĞRETMENİN SORULARI — kâğıttaki biçimle (Kemal, 10 Kasım 2026 akşamı: "Ela yarın görünce şaşırmasın")
# Her soru tek ekran, tek madde; iskele = kâğıttaki iş (grupla: sürükle-bırak, doldur: boşluğa yaz / daire içine al, secim: şık).
# "Bu soru senden ne istiyor?" adımı yok (kalipNot yazılmadı); yanlıştan sonra okuma beklemesi yok (beklemesiz).
# =====================================================================
def S(no, kazanim, soru, iskele, kisa, metin=None, svg=None, harf="a", ek=None):
    m = {"harf": harf, "soru": soru, "iskele": iskele, "kisaCevap": kisa}
    q = {"id": f"m{no}", "no": no, "kazanim": kazanim, "maddeler": [m] + (ek or [])}
    if metin: q["metin"] = metin
    if svg: q["svg"] = svg
    return Y.meb(**q)
def B(cevap, *kabul, k=None, sec=None):
    b = {"cevap": cevap}
    if kabul: b["kabul"] = list(kabul)
    if k: b["k"] = k
    if sec: b["secenekler"] = sec
    return b

GOR = ["handsome", "slim", "overweight", "tall", "brown eyes"]
KIS = ["punctual", "stubborn", "thoughtful", "honest", "friendly"]
HARF10 = "ABCDEFGHIJ"
KEL = ["handsome", "punctual", "stubborn", "slim", "thoughtful", "overweight", "tall", "honest", "friendly", "brown eyes"]
S(1, K1, "1. Categorize the words. (Kelimeleri grupla.)",
  {"tur": "grupla", "soru": "Her kelimeyi doğru kutuya koy: Appearance (görünüş) ya da Personality (kişilik).",
   "kelimeler": KEL, "kutular": [{"etiket": "Appearance", "uyeler": GOR}, {"etiket": "Personality", "uyeler": KIS}],
   "aciklama": "Fotoğrafta görünenler Appearance: handsome, slim, overweight, tall, brown eyes. Davranış anlatanlar Personality: punctual, stubborn, thoughtful, honest, friendly."},
  "Appearance: handsome, slim, overweight, tall, brown eyes · Personality: punctual, stubborn, thoughtful, honest, friendly",
  metin=["Kâğıtta: " + " · ".join(f"{HARF10[i]}. {w}" for i, w in enumerate(KEL))])

S(2, K1, "2. Complete the sentences with adjectives in the box. (Kutudaki sıfatlarla cümleleri tamamla.)",
  {"tur": "doldur", "soru": "Kutudaki kelimelerden uygun olanı boşluğa yaz.", "kutu": ["honest", "punctual", "lazy", "generous", "polite"],
   "cumleler": [{"c": "My brother doesn't tell lies. He is ___.", "b": [B("honest")]},
                {"c": "Selin has got a lot of money and she helps poor people. She is ___.", "b": [B("generous")]},
                {"c": "My sister always says “thank you”. She is a ___ person.", "b": [B("polite")]},
                {"c": "Sevda teacher is never late. She is very ___.", "b": [B("punctual")]},
                {"c": "My daughter never does his homework. She is ___.", "b": [B("lazy")]}],
   "aciklama": "Yalan söylemeyen dürüst (honest), yardım eden cömert (generous), teşekkür eden kibar (polite), geç kalmayan dakik (punctual), ödev yapmayan tembel (lazy)."},
  "honest · generous · polite · punctual · lazy")

S(3, K2, "3. Write the comparatives of the adjectives. (Sıfatların karşılaştırma hâlini yaz.)",
  {"tur": "doldur", "soru": "Parantezdeki sıfatın karşılaştırma hâlini boşluğa yaz.",
   "cumleler": [{"c": "Antalya is ___ (hot) than Ağrı.", "b": [B("hotter")]},
                {"c": "A computer is ___ (expensive) than radio.", "b": [B("more expensive")]},
                {"c": "Milk is ___ (good) than coffee.", "b": [B("better")]},
                {"c": "My cousin is ___ (slim) than my sister.", "b": [B("slimmer")]},
                {"c": "Ünal teacher is ___ (funny) than me.", "b": [B("funnier")]},
                {"c": "My sister is ___ (selfish) than my brother.", "b": [B("more selfish")]}],
   "aciklama": "Kısa sıfat -er (hot → hotter, slim → slimmer: son harf iki kez), -y → -ier (funnier), uzun sıfat more … (more expensive, more selfish), good → better."},
  "hotter · more expensive · better · slimmer · funnier · more selfish")

S(4, K3, "4. Circle the correct word. (Doğru kelimeyi daire içine al.)",
  {"tur": "doldur", "soru": "Doğru kelimeye dokun (kâğıtta onu daire içine alacaksın).", "harfler": True,
   "cumleler": [{"c": "Timmy ___ at party last night.", "b": [B("wasn't", sec=["wasn't", "weren't"])]},
                {"c": "Alex and Tom ___ in the school garden ten minutes ago.", "b": [B("were", sec=["was", "were"])]},
                {"c": "___ you in Antalya five years ago?", "b": [B("Were", sec=["Was", "Were"])]},
                {"c": "I ___ born in Ağrı in 2001.", "b": [B("was", sec=["was", "were"])]},
                {"c": "We ___ at the theatre yesterday.", "b": [B("were", sec=["was", "were"])]}],
   "aciklama": "I / he / she / Timmy → was · we / you / they / Alex and Tom → were."},
  "a wasn't · b were · c Were · d was · e were")

S(5, K3, "5. Write the years in words. (Yılları yazıyla yaz.)",
  {"tur": "doldur", "soru": "Yılı İngilizce kelimelerle yaz.",
   "cumleler": [{"c": "1992: ___", "b": [B("nineteen ninety-two", "nineteen ninety two")]},
                {"c": "2019: ___", "b": [B("twenty nineteen", "twenty-nineteen", "two thousand and nineteen", "two thousand nineteen")]},
                {"c": "2000: ___", "b": [B("two thousand")]}],
   "aciklama": "Yıllar ikişer ikişer okunur: 19 | 92 → nineteen ninety-two, 20 | 19 → twenty nineteen. 2000 → two thousand."},
  "nineteen ninety-two · twenty nineteen · two thousand")

S6C = [("Amanda ___ . (go cycling)", "often goes cycling"), ("Amanda ___ . (do powerlifting)", "usually does powerlifting"),
       ("Patty ___ . (play golf)", "usually plays golf"), ("Patty ___ . (go cycling)", "never goes cycling"),
       ("Stephen ___ . (play tennis)", "sometimes plays tennis"), ("Stephen ___ . (play golf)", "always plays golf")]
S(6, K4, "6. Look at the table and fill in the blanks. (Tabloya bak, boşlukları doldur.)",
  {"tur": "doldur", "soru": "Yaprakları say, zarf + fiil-s yaz. (a kâğıtta örnek: Amanda always plays tennis.)", "harfler": True, "harfBas": 2,
   "cumleler": [{"c": c, "b": [B(v)]} for c, v in S6C],
   "aciklama": "4 dolu yaprak always, 3 usually, 2 often, 1 sometimes, 0 dolu rarely, yalnız çizgi never. Zarf fiilden önce, fiile -s: goes, does, plays."},
  "b often goes cycling · c usually does powerlifting · d usually plays golf · e never goes cycling · f sometimes plays tennis · g always plays golf",
  metin=["Yonca: 4 dolu yaprak always · 3 usually · 2 often · 1 sometimes · 0 dolu rarely · yalnız çizgi never",
         "a. Amanda always plays tennis. (kâğıtta örnek olarak yazılı)"], svg=Z.tablo6())

KOK_TR = {"gitmek": ["git"], "yüzmek": ["yüz"], "vermek": ["ver"], "yapmak": ["yap", "et"], "olmak": ["ol"], "duymak": ["duy", "işit"],
          "ayrılmak": ["ayrıl", "terk", "bırak", "çık"], "bilmek": ["bil"], "görmek": ["gör"], "anlamak": ["anla"]}
S(7, K3, "7. Write the meanings and past forms of the verbs below. (Fiillerin geçmiş hâlini ve anlamını yaz.)",
  {"tur": "doldur", "soru": "Her fiilin PAST (V2) hâlini ve Türkçe ANLAM'ını yaz.",
   "cumleler": [{"c": f"{v1.capitalize()} → PAST (V2): ___ ANLAM: ___", "b": [B(v2), B(tr, k=KOK_TR[tr])]} for v1, v2, tr in V2],
   "aciklama": "go-went (gitmek), swim-swam (yüzmek), give-gave (vermek), do-did (yapmak), become-became (olmak), hear-heard (duymak), leave-left (ayrılmak), know-knew (bilmek), see-saw (görmek), understand-understood (anlamak)."},
  "went, swam, gave, did, became, heard, left, knew, saw, understood")

S(8, K2, "8. Choose the correct options. Which one is TRUE? (Tabloya göre hangisi DOĞRU?)",
  {"tur": "secim", "sabit": True, "soru": "Tablodaki sayılara bak. Hangisi DOĞRU?",
   "secenekler": ["Antalya is colder than İstanbul today.", "Ağrı was hotter than İstanbul yesterday.", "İstanbul is colder than Ağrı today.", "Antalya was hotter than Ağrı yesterday."],
   "dogru": 3, "aciklama": "Dün Antalya 29, Ağrı 11 → D doğru. A: bugün 34 > 20, B: dün 11 < 24, C: bugün 20 > 15 olduğu için yanlış."},
  "D) Antalya was hotter than Ağrı yesterday.", svg=Z.tablo8(),
  ek=[{"harf": "b", "soru": "Emma: ______? Jack: Once a week. What is the best question according to the answer?",
       "iskele": {"tur": "secim", "sabit": True, "soru": "“Once a week” (haftada bir) cevabına en uygun soru hangisi?",
                  "secenekler": ["Do you like indoor sports?", "Why do you play football?", "How often do you train?", "Where do you play volleyball?"],
                  "dogru": 2, "aciklama": "Once a week bir sıklık; sıklık “How often” ile sorulur. Why → Because, Where → yer, Do you …? → Yes/No."},
       "kisaCevap": "C) How often do you train?"}])

# =====================================================================
# HOOT'UN HATASI (aynı sorulara Ela'nın yapabileceği hatalar; eski biçim)
# =====================================================================
def KH(kazanim, soru, kuark, dogruSik, yanlis1, yanlis2, ipucu, aciklama, dogruCevap):
    Y.kuark(kazanim=kazanim, soru=soru, kuark=kuark, secenekler=[dogruSik, yanlis1, yanlis2], dogru=0, ipucu=ipucu, aciklama=aciklama, dogruCevap=dogruCevap)

KH(K1, "Categorize: tall → ?", "Personality", "tall fotoğrafta görünür → Appearance olmalı.", "Hoot haklı, tall bir davranış.", "tall hiçbir gruba girmez.",
   "Uzun boyu fotoğrafta görebilir misin?", "Görünüş (Appearance): handsome, slim, overweight, tall, brown eyes.", "Appearance")
KH(K1, "My sister always says “thank you”. She is a ___ person.", "generous", "“thank you” diyen kişi kibardır → polite.", "Hoot haklı, generous doğru.", "lazy olmalı.",
   "Teşekkür etmek cömertlik mi, kibarlık mı?", "polite = kibar, generous = cömert (fakirlere yardım eder).", "polite")
KH(K2, "Antalya is ___ (hot) than Ağrı.", "hoter", "Son harf iki kez yazılır → hotter.", "Hoot haklı, hoter doğru.", "more hot olmalı.",
   "hot: sessiz-sesli-sessiz… son harfe ne olur?", "hot → hotter, slim → slimmer.", "hotter")
KH(K2, "Milk is ___ (good) than coffee.", "more good", "good düzensizdir → better.", "Hoot haklı.", "gooder olmalı.",
   "good kurala uymayan sıfattı.", "good → better.", "better")
KH(K3, "Alex and Tom (was / were) in the school garden.", "was", "İki kişi (they) → were.", "Hoot haklı, was doğru.", "weren't olmalı.",
   "Alex and Tom = they. They ile hangisi?", "we / you / they → were.", "were")
KH(K3, "Write the past form: know → ?", "knowed", "know düzensizdir → knew.", "Hoot haklı.", "known olmalı.",
   "Düzensiz fiiller -ed almaz.", "know → knew (bilmek).", "knew")
KH(K4, "Patty ___ . (go cycling) — yalnız çizgi", "Patty never go cycling.", "-s eksik: Patty never goes cycling.", "Hoot haklı, cümle doğru.", "Patty goes never cycling. olmalı.",
   "Patty = she. Fiile ne eklenir?", "Zarf fiilden önce, fiile -s: never goes.", "never goes cycling")
KH(K4, "Amanda ___ . (go cycling) — 2 dolu yaprak", "Amanda goes often cycling.", "Zarf fiilden önce gelir: Amanda often goes cycling.", "Hoot haklı.", "Amanda always goes cycling. olmalı.",
   "Zarf nerede durur: fiilden önce mi, sonra mı?", "2 dolu → often; zarf fiilden önce (WB s. 86).", "often goes cycling")

Y.yaz()
