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
    soruGiris="Bunlar öğretmeninin kâğıdındaki <b>8 soru</b>. Yazılıda <b>aynısı</b> çıkacak. İlk çözüşte önce kısa bir ısınma var, sonra cevabı <b>yazarak</b> ver. İkinci çözüşte ısınma yok: doğrudan aklından yaz.",
    giris="Öğretmeninin kâğıdındaki <b>8 soru</b> yazılıda <b>aynen</b> çıkacak. Önce 4 konu kartını oku ve boşlukları doldur. Sonra 8 soruyu sırayla çöz. En sonda Kısa Cevap Kartları ile her cevabı bir kez daha hatırla.",
    kapsamDisi=["Kâğıtta olmayan her şey: öğretmen bu 8 sorunun aynısını soracak", "Own It ünitelerindeki diğer konular (present perfect, used to…)"],
    puanNotu="Kâğıtta yalnız 1. ve 7. sorunun puanı yazıyor (20'şer puan). Diğerlerinin puanı belli değil.",
    kaynakNotu=("Sorular öğretmenin çalışma kâğıdından. Cevaplar: Own it! 3 Workbook s. 86 (sıklık zarfları, past simple), WB s. 9 "
                "(in 1992); İngilizce 7 ders kitabı (MEB) s. 10–16 (görünüş, kişilik, karşılaştırma). Karşılaştırma yazım kuralları "
                "(hotter, funnier, more expensive) ve düzensiz fiiller genel İngilizce kurallarıdır."),
    sozluk={"categorize": "grupla, sınıflandır", "appearance": "görünüş", "personality": "kişilik", "punctual": "dakik",
            "stubborn": "inatçı", "thoughtful": "düşünceli", "overweight": "kilolu", "adjectives": "sıfatlar", "generous": "cömert",
            "polite": "kibar", "lazy": "tembel", "comparatives": "karşılaştırma hâli (-er / more)", "circle": "daire içine al",
            "in words": "yazıyla", "fill in the blanks": "boşlukları doldur", "meanings": "anlamları", "past forms": "geçmiş hâlleri (V2)",
            "once a week": "haftada bir", "according to": "-e göre"})

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
# ÖĞRETMENİN SORULARI (kâğıttaki sırayla)
# =====================================================================
Q = {}
def S(no, kazanim, maddeler, metin, svg=None):
    q = {"id": f"m{no}", "no": no, "kazanim": kazanim, "metin": metin, "maddeler": maddeler}
    if svg: q["svg"] = svg
    Q[no] = Y.meb(**q)

GOR = ["handsome", "slim", "overweight", "tall", "brown eyes"]
KIS = ["punctual", "stubborn", "thoughtful", "honest", "friendly"]
S(1, K1, [
    M("a", "Write the Appearance words. (Appearance kutusuna gelen 5 kelimeyi yaz.)", "handsome, slim, overweight, tall, brown eyes",
      [A(w, w if w != "brown eyes" else "brown eye") for w in GOR],
      {"tur": "dytablo", "soru": "Önce ısınalım: Bu kelime GÖRÜNÜŞ (Appearance) mü? Görünüşse D, kişilikse Y seç.",
       "ifadeler": [{"s": "handsome", "d": True}, {"s": "punctual", "d": False}, {"s": "stubborn", "d": False}, {"s": "slim", "d": True},
                    {"s": "thoughtful", "d": False}, {"s": "overweight", "d": True}, {"s": "tall", "d": True}, {"s": "honest", "d": False},
                    {"s": "friendly", "d": False}, {"s": "brown eyes", "d": True}],
       "aciklama": "Fotoğrafta görünenler Appearance: handsome, slim, overweight, tall, brown eyes."},
      tetik=["Appearance"], notu="Fotoğrafta görünür mü? Görünürse Appearance, davranışsa Personality.", formul="grup"),
    M("b", "Write the Personality words. (Personality kutusuna gelen 5 kelimeyi yaz.)", "punctual, stubborn, thoughtful, honest, friendly",
      [A(w, w) for w in KIS],
      {"tur": "eslestir", "soru": "Önce ısınalım: Kişilik sıfatlarını Türkçesiyle eşleştir.",
       "ciftler": [{"sol": "punctual", "sag": "dakik"}, {"sol": "stubborn", "sag": "inatçı"}, {"sol": "thoughtful", "sag": "düşünceli"},
                   {"sol": "honest", "sag": "dürüst"}, {"sol": "friendly", "sag": "arkadaş canlısı"}],
       "aciklama": "Bunlar davranış anlatır, fotoğrafta görünmez → Personality."},
      tetik=["Personality"], formul="grup")],
  metin=["Categorize the words. (Kelimeleri grupla.) Appearance / Personality",
         "A. handsome · B. punctual · C. stubborn · D. slim · E. thoughtful · F. overweight · G. tall · H. honest · I. friendly · J. brown eyes"])

S2 = [("My brother doesn't tell lies. He is ___.", "honest", "doesn't tell lies"),
      ("Selin has got a lot of money and she helps poor people. She is ___.", "generous", "helps poor people"),
      ("My sister always says “thank you”. She is a ___ person.", "polite", "says “thank you”"),
      ("Sevda teacher is never late. She is very ___.", "punctual", "never late"),
      ("My daughter never does his homework. She is ___.", "lazy", "never does his homework")]
S(2, K1, [M("abcde"[i], s, c, [A(c, c)],
            {"tur": "eslestir", "soru": "Önce ısınalım: Davranışı sıfatla eşleştir.",
             "ciftler": [{"sol": "doesn't tell lies", "sag": "honest"}, {"sol": "helps poor people", "sag": "generous"},
                         {"sol": "always says “thank you”", "sag": "polite"}, {"sol": "is never late", "sag": "punctual"},
                         {"sol": "never does homework", "sag": "lazy"}],
             "aciklama": "Yalan söylemeyen dürüst (honest), yardım eden cömert (generous), teşekkür eden kibar (polite), geç kalmayan dakik (punctual), ödev yapmayan tembel (lazy)."} if i == 0 else None,
            tetik=[t], notu="Cümledeki davranışı bul → kutudan sıfat: never late → punctual." if i == 0 else None, formul="sifat")
          for i, (s, c, t) in enumerate(S2)],
  metin=["Complete the sentences with adjectives in the box. (Kutudaki sıfatlarla cümleleri tamamla.)", "Box: honest · punctual · lazy · generous · polite"])

S3 = [("Antalya is ___ (hot) than Ağrı.", "hotter", ["hotter"], ["hotter", "hoter", "more hot", "hottest"], "Kısa sıfat, son harf iki kez: hot → hotter."),
      ("A computer is ___ (expensive) than radio.", "more expensive", ["more expensive"], ["more expensive", "expensiver", "most expensive", "expensivest"], "Uzun sıfat: more + expensive."),
      ("Milk is ___ (good) than coffee.", "better", ["better"], ["better", "gooder", "more good", "best"], "Düzensiz: good → better."),
      ("My cousin is ___ (slim) than my sister.", "slimmer", ["slimmer"], ["slimmer", "slimer", "more slim", "slimmest"], "Kısa sıfat, son harf iki kez: slim → slimmer."),
      ("Ünal teacher is ___ (funny) than me.", "funnier", ["funnier"], ["funnier", "funnyer", "more funny", "funniest"], "-y düşer, -ier gelir: funny → funnier."),
      ("My sister is ___ (selfish) than my brother.", "more selfish", ["more selfish"], ["more selfish", "selfisher", "selfishest", "most selfish"], "Uzun sıfat: more + selfish.")]
S(3, K2, [M("abcdef"[i], s, c, [A(c, *k)], SEC("Önce ısınalım: Hangisi doğru yazım?", sec, ac), tetik=[s[s.index("("):s.index(")") + 1]],
            notu="Parantezdeki sıfata bak: kısa → -er · uzun → more … · good → better." if i == 0 else None, formul="comp")
          for i, (s, c, k, sec, ac) in enumerate(S3)],
  metin=["Write the comparatives of the adjectives. (Sıfatların karşılaştırma hâlini yaz.)"])

S4 = [("Timmy (wasn't / weren't) at party last night.", "wasn't", ["wasn't", f"wasn{AP}t", "wasnt", "was not"], "Timmy"),
      ("Alex and Tom (was / were) in the school garden ten minutes ago.", "were", ["were"], "Alex and Tom"),
      ("(Was / Were) you in Antalya five years ago?", "Were", ["were"], "you"),
      ("I (was / were) born in Ağrı in 2001.", "was", ["was"], "I (was"),
      ("We (was / were) at the theatre yesterday.", "were", ["were"], "We")]
S(4, K3, [M("abcde"[i], s, c, [A(c, *k)],
            {"tur": "dytablo", "soru": "Önce ısınalım: Özne–fiil eşleşmesi doğru mu? D ya da Y seç.",
             "ifadeler": [{"s": "I → was", "d": True}, {"s": "Timmy → weren't", "d": False}, {"s": "Alex and Tom → were", "d": True},
                          {"s": "We → was", "d": False}, {"s": "you → were", "d": True}],
             "aciklama": "I / he / she / Timmy → was · we / you / they / Alex and Tom → were."} if i == 0 else None,
            kisa=f"{c} ({t.replace(' (was', '')} → {c.lower()})", tetik=[t],
            notu="Özneye bak: I / he / she / Timmy → was · we / you / they → were." if i == 0 else None, formul="waswere")
          for i, (s, c, k, t) in enumerate(S4)],
  metin=["Circle the correct word. (Doğru kelimeyi daire içine al.)"])

S(5, K3, [
    M("a", "1992:", "nineteen ninety-two", [A("nineteen", "nineteen"), A("ninety-two", "ninety-two", "ninety two", "ninetytwo")],
      SEC("Önce ısınalım: 1992 nasıl yazılır?", ["nineteen ninety-two", "nine nine two", "nineteen ninety-twelve", "ninety nineteen-two"], "İkişer ikişer: 19 | 92 → nineteen ninety-two."),
      tetik=["1992"], notu="Yılı ikişer ikişer oku: 19 | 92 → nineteen ninety-two.", formul="yil"),
    M("b", "2019:", "twenty nineteen", [A("twenty / two thousand (and)", "twenty", "two thousand"), A("nineteen", "nineteen")],
      SEC("Önce ısınalım: 2019 nasıl yazılır?", ["twenty nineteen", "two nineteen", "twelve nineteen", "twenty ninety"], "İkişer ikişer: 20 | 19 → twenty nineteen. (two thousand and nineteen da doğru)"),
      tetik=["2019"], formul="yil"),
    M("c", "2000:", "two thousand", [A("two thousand", "two thousand")],
      SEC("Önce ısınalım: 2000 nasıl yazılır?", ["two thousand", "twenty hundred", "two hundred", "twenty zero"], "2000 → two thousand (iki bin)."),
      tetik=["2000"], formul="yil")],
  metin=["Write the years in words. (Yılları yazıyla yaz.)"])

S6 = [("a", "Amanda ___ . (play tennis)", "always plays tennis", "always", "plays tennis", "play tennis",
       {"tur": "eslestir", "soru": "Önce ısınalım: Dolu yaprak sayısını sıklık zarfıyla eşleştir.",
        "ciftler": [{"sol": "4 dolu yaprak", "sag": "always"}, {"sol": "3 dolu yaprak", "sag": "usually"}, {"sol": "2 dolu yaprak", "sag": "often"},
                    {"sol": "1 dolu yaprak", "sag": "sometimes"}, {"sol": "yalnız çizgi", "sag": "never"}],
        "aciklama": "4 always, 3 usually, 2 often, 1 sometimes, 0 dolu rarely, yalnız çizgi never. Amanda–tennis: 4 dolu → always (kâğıtta örnek)."}),
      ("b", "Amanda ___ . (go cycling)", "often goes cycling", "often", "goes cycling", "go cycling",
       SEC("Önce ısınalım: Amanda–cycling 2 dolu yaprak. Hangisi doğru?", ["often goes cycling", "goes often cycling", "often go cycling", "sometimes goes cycling"], "2 dolu → often; zarf fiilden önce, go → goes.")),
      ("c", "Amanda ___ . (do powerlifting)", "usually does powerlifting", "usually", "does powerlifting", "do powerlifting",
       SEC("Önce ısınalım: Amanda–powerlifting 3 dolu yaprak. Hangisi doğru?", ["usually does powerlifting", "does usually powerlifting", "usually do powerlifting", "usually doing powerlifting"], "3 dolu → usually; zarf fiilden önce, fiile -s: does.")),
      ("d", "Patty ___ . (play golf)", "usually plays golf", "usually", "plays golf", "play golf",
       SEC("Önce ısınalım: Patty–golf 3 dolu yaprak. Hangisi doğru?", ["usually plays golf", "usually play golf", "plays usually golf", "always plays golf"], "3 dolu → usually; play → plays.")),
      ("e", "Patty ___ . (go cycling)", "never goes cycling", "never", "goes cycling", "go cycling",
       SEC("Önce ısınalım: Patty–cycling yalnız çizgi, hiç dolu yaprak yok. Hangisi doğru?", ["never goes cycling", "never go cycling", "goes never cycling", "rarely goes cycling"], "Yalnız çizgi → never; go → goes.")),
      ("f", "Stephen ___ . (play tennis)", "sometimes plays tennis", "sometimes", "plays tennis", "play tennis", None),
      ("g", "Stephen ___ . (play golf)", "always plays golf", "always", "plays golf", "play golf", None)]
S(6, K4, [M(h, s, c, [A(z, z), AS(f"{fiil} (zarftan sonra, -s ile)", [z], [fiil])], isk, tetik=[f"({t})"],
            notu="Yaprakları say → zarf + fiil-s: Amanda often goes cycling." if i == 0 else None, formul="siklik")
          for i, (h, s, c, z, fiil, t, isk) in enumerate(S6)],
  metin=["Look at the table and fill in the blanks. (Tabloya bak, boşlukları doldur.)",
         "Yonca: 4 dolu yaprak always · 3 usually · 2 often · 1 sometimes · 0 dolu rarely · yalnız çizgi never",
         "a şıkkı kâğıtta örnek olarak çözülü: Amanda always plays tennis. Tabloda yalnız sorulan kutular var."],
  svg=Z.tablo6())

V2M = [V2[0:2], V2[2:4], V2[4:6], V2[6:8], V2[8:10]]
YAN = {"went": "goed", "swam": "swimmed", "gave": "gived", "did": "doed", "became": "becomed", "heard": "heared", "left": "leaved",
       "knew": "knowed", "saw": "seed", "understood": "understanded"}
KOK_TR = {"gitmek": ["git"], "yüzmek": ["yüz"], "vermek": ["ver"], "yapmak": ["yap"], "olmak": ["ol"], "duymak": ["duy", "işit"],
          "ayrılmak": ["ayrıl", "terk", "bırak", "çık"], "bilmek": ["bil"], "görmek": ["gör"], "anlamak": ["anla"]}
S(7, K3, [M("abcde"[i], f"{a[0].capitalize()} ve {b[0].capitalize()}: geçmiş hâlini (V2) ve anlamını yaz.",
            f"{a[0]} → {a[1]} ({a[2]}), {b[0]} → {b[1]} ({b[2]})",
            [A(f"{a[1]}", a[1]), A(f"{a[2]}", *KOK_TR[a[2]]), A(f"{b[1]}", b[1]), A(f"{b[2]}", *KOK_TR[b[2]])],
            {"tur": "bosluk", "soru": "Önce ısınalım: Geçmiş hâlini (V2) seç.", "cumleler": [{"c": f"{a[0]} → ___", "cevap": a[1]}, {"c": f"{b[0]} → ___", "cevap": b[1]}],
             "havuz": [YAN[a[1]], YAN[b[1]]], "aciklama": f"Düzensiz fiiller: {a[0]} → {a[1]}, {b[0]} → {b[1]}. (-ed almaz)"},
            kisa=f"{a[1]} ({a[2]}), {b[1]} ({b[2]})", tetik=["geçmiş hâlini (V2) ve anlamını"],
            notu="V1 → V2 + Türkçe anlam: go → went (gitmek)." if i == 0 else None, formul="v2")
          for i, (a, b) in enumerate(V2M)],
  metin=["Write the meanings and past forms of the verbs below. (Fiillerin anlamlarını ve geçmiş hâllerini yaz.)",
         "1. Go · 2. Swim · 3. Give · 4. Do · 5. Become · 6. Hear · 7. Leave · 8. Know · 9. See · 10. Understand"])

S(8, K2, [
    M("a", "Which one is TRUE? (Tabloya göre hangisi DOĞRU? Şıkkın harfini ve cümlesini yaz.)", "D) Antalya was hotter than Ağrı yesterday.",
      [A("D şıkkı: Antalya was hotter than Ağrı", "antalya was hotter", "d)")],
      {"tur": "dytablo", "soru": "Önce ısınalım: Tablodaki sayılara bak. Her cümle Doğru (D) mu, Yanlış (Y) mı?",
       "ifadeler": [{"s": "A) Antalya is colder than İstanbul today.", "d": False}, {"s": "B) Ağrı was hotter than İstanbul yesterday.", "d": False},
                    {"s": "C) İstanbul is colder than Ağrı today.", "d": False}, {"s": "D) Antalya was hotter than Ağrı yesterday.", "d": True}],
       "aciklama": "A: bugün 34 > 20, Antalya daha sıcak. B: dün 11 < 24, Ağrı daha soğuk. C: bugün 20 > 15, İstanbul daha sıcak. D: dün 29 > 11 → doğru."},
      kisa="D) Antalya was hotter than Ağrı yesterday.", tetik=["TRUE"],
      notu="Sayıları karşılaştır: dün → was, bugün → is; “Once a week” → How often.", formul="comp"),
    M("b", "Emma: ______? Jack: Once a week. What is the best question according to the answer? (Şıkkın harfini ve soruyu yaz.)", "C) How often do you train?",
      [A("C şıkkı: How often", "how often")],
      {"tur": "dytablo", "soru": "Önce ısınalım: “Once a week” (haftada bir) cevabına uyan soru hangisi? Uyan D, uymayan Y.",
       "ifadeler": [{"s": "A) Do you like indoor sports?", "d": False}, {"s": "B) Why do you play football?", "d": False},
                    {"s": "C) How often do you train?", "d": True}, {"s": "D) Where do you play volleyball?", "d": False}],
       "aciklama": "Once a week bir sıklık; sıklık “How often” ile sorulur. Why → Because, Where → yer, Do you …? → Yes/No."},
      kisa="C) How often do you train?", tetik=["Once a week"], formul="siklik")],
  metin=["Choose the correct options. (Doğru seçenekleri seç.)", "Sol kutu: tablo (City · Yesterday · Today). Which one is TRUE?", "Sağ kutu: Emma: ______? Jack: Once a week. What is the best question according to the answer?"],
  svg=Z.tablo8())

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
