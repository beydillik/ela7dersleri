"""İngilizce (Own It) 7 · Seçmeli İngilizce Sınavı — Yazılıya Hazırlık 2 (#yazili2).
Öğretmen kâğıdı (11 Kasım 2026): Comparing Students (tablo), Part B ve Part C okuma (tam cümle), Part D sporlar, Part E rutin cümleleri.
Kemal: her şey 1. hazırlıkla aynı (kâğıt biçimi, "ne istiyor" adımı yok, okuma beklemesi yok, prova yok); sınav tarihi bilinmiyor.
Cevaplar Gemini'nin anahtarından, Claude düzeltmeleriyle: B2'de metin "tall" demiyor ("a little taller than me", well-built, curly blond
hair, green eyes) → "He is well-built with curly blond hair and green eyes."; tablo ve "older/shorter" cevapları "than …" ile tam cümle;
Part D'de kâğıttaki tablo 5 satırlı olduğu için 11 kelimenin hepsi gruplanır (soru 2+2 istiyor; kısa cevapta 2+2).
Rosa (C5) için metin "kind" demiyor, "Thank you / Sorry" diyor (kibar); beklenen cevap "Yes, they are." kabul edildi.
Çalıştır: python3 araclar/yazili/own1_d1y2.py"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from yazili import Yazili
import cizim_ing as ZI

K1, K2, K3, K4, K5 = "Tablo", "Sam ve Harry", "Ellie, Jenny, Jeremy, Rosa", "Sporlar", "Rutinler"

METIN_B = ("Hi, my name is Sam. I am fourteen years old. I am short and plump with dark, wavy hair and brown eyes. I like wearing colorful glasses. "
           "This is my young brother, Harry. He is younger than me. We don't look alike at all. He is a little taller than me, with curly blond hair "
           "and green eyes. He is well-built because he likes doing sports. Our personalities are very different as well. He has a lot of friends, "
           "and he gets along well with new people. I am usually shyer and more nervous than him. I have a few close friends. I am always on time; "
           "I don't like being late to meetings, but he is usually not punctual. We are both generous and kind people. We always share what we have "
           "and support each other. I love my brother.")
METIN_C = ("These are my friends: Ellie, Jenny, and Jeremy. We met in elementary school, so we know each other very well. Ellie doesn't change her "
           "mind easily. She is very stubborn but respectful and kind to others, so we don't mind that much. Jenny is more open-minded than Ellie, "
           "and she always tells the truth. She hates telling lies. Jeremy studies hard and always gets high marks. He loves learning new things. "
           "Me? I am Rosa. Unfortunately, I always drop and break things by accident. I always say “Thank you” and “Sorry” when I need to.")

Y = Yazili("own1", "d1y2",
    baslik="Seçmeli İngilizce Sınavı", ders="İngilizce (Own It)", senaryo="Öğretmenin çalışma kâğıdı", sure=40, tarih=None,
    dagilim={K1: 1, K2: 1, K3: 1, K4: 1, K5: 1},
    soruBaslik="Öğretmenin Soruları", soruEtiket="Soru", kazanimAd="konu", ikizsiz=True, beklemesiz=True,
    soruGiris="Bunlar öğretmeninin kâğıdındaki sorular, kâğıttaki sırayla. Kâğıtta ne yapacaksan burada da onu yap: metni oku, <b>tam cümleyle</b> yaz, kelimeleri kutulara yerleştir.",
    giris="Öğretmeninin kâğıdındaki <b>5 bölüm</b> sınavda çıkacak. Önce 5 konu kartını oku ve boşlukları doldur. Sonra soruları sırayla çöz. En sonda Kısa Cevap Kartları ile her cevabı bir kez daha hatırla. Cevapları hep <b>tam cümleyle</b> yaz: “Sam.” değil, “Sam is older than Jane.”",
    kapsamDisi=["Kâğıtta olmayan her şey"],
    puanNotu="Kâğıttaki puanlar: Part B 24, Part C 20, Part D 20, Part E 21. Tablo sorusunun puanı yazmıyor.",
    kaynakNotu="Sorular öğretmenin kâğıdından. Cevaplar metinlerden ve tablodan; tam cümle kalıpları ve sıklık zarfları Own it! 3 WB s. 86 (adverbs of frequency).",
    sozluk={"plump": "tombul", "wavy": "dalgalı", "curly": "kıvırcık", "blond": "sarı (saç)", "well-built": "yapılı, iri", "look alike": "birbirine benzemek",
            "gets along well": "iyi geçinir", "shyer": "daha utangaç", "nervous": "gergin, sinirli", "on time": "zamanında", "punctual": "dakik",
            "generous": "cömert", "share": "paylaşmak", "support": "desteklemek", "stubborn": "inatçı", "respectful": "saygılı",
            "open-minded": "açık fikirli", "tells the truth": "doğruyu söyler", "lies": "yalanlar", "high marks": "yüksek notlar",
            "by accident": "kazara", "change her mind": "fikrini değiştirmek", "elementary school": "ilkokul"})

# =====================================================================
# KONU KARTLARI
# =====================================================================
Y.kazanim(kod=K1, ad="Tablodaki bilgileri karşılaştırma sıfatlarıyla tam cümle yazar.", kisa="Tablo: older / taller / heavier", soru=1,
    soruNot="Kâğıtta: Comparing Students (tablo)", renk="#d9480f", konular=["u1k1"], sayfa="Kâğıt + genel kural", svg=ZI.h_karsilastir(),
    maddeler=["Tablo: <b>Jane</b> 12 yaş, 58 kg, 1.52 m · <b>Sam</b> 13 yaş, 62 kg, 1.65 m.",
              "Age (yaş) büyük → <b>older</b> · Height (boy) büyük → <b>taller</b> · Weight (kilo) büyük → <b>heavier</b>.",
              "Cevap kalıbı: <b>İsim + is + sıfat-er + than + diğeri.</b>",
              "1. <b>Sam is older than Jane.</b> 2. <b>Sam is taller than Jane.</b> 3. <b>Sam is heavier than Jane.</b>",
              "heavy → y düşer, <b>-ier</b>: heavier. Tersi: younger, shorter, lighter."],
    kelimeler=["age = yaş", "weight = kilo", "height = boy", "older", "taller", "heavier"],
    hatalar=[{"yanlis": "Sam.", "dogru": "Sam is older than Jane. (tam cümle)"},
             {"yanlis": "heavyer", "dogru": "heavier"},
             {"yanlis": "Jane is taller.", "dogru": "1.65 > 1.52 → Sam is taller than Jane."}],
    tekrar=[{"c": "“Look at the table and answer the questions.” = Tabloya bak ve {soruları cevapla|tabloyu çiz}.", "s": "sınav yönergesi"},
            {"c": "“Who is older, Jane or Sam?” = Jane mi Sam mi daha {yaşlı (büyük)|uzun|kilolu}?", "s": "sınav yönergesi"},
            {"c": "Sam 13, Jane 12 → {Sam|Jane} is older than {Jane|Sam}.", "s": "tablo"},
            {"c": "1.65 m > 1.52 m → Sam is {taller|shorter} than Jane.", "s": "tablo"},
            {"c": "62 kg > 58 kg → Sam is {heavier|heavyer|lighter} than Jane.", "s": "tablo"},
            {"c": "Tam cümle: {Sam is older than Jane.|Sam.|Older.}", "s": "cevap kalıbı"}])

Y.kazanim(kod=K2, ad="Okuduğu metindeki kişilerin görünüşünü ve kişiliğini tam cümleyle anlatır.", kisa="Part B: Sam ve Harry", soru=1,
    soruNot="Kâğıtta: Part B (6 soru, 24 puan)", renk="#7a5ce0", konular=["u1k1", "u1k2"], sayfa="Kâğıt, Part B",
    maddeler=["Soru kalıpları: <b>Who is …?</b> → “<b>Harry is …</b>” · <b>Is Sam …?</b> → “<b>Yes, he is.</b> / <b>No, he isn't.</b>”",
              "<b>What does Harry look like?</b> = görünüşü (saç, göz, boy) · <b>What is Sam like?</b> = kişiliği (nasıl biri).",
              "<b>Sam</b> (anlatan): short, plump, dark wavy hair, brown eyes · <b>shy, nervous, punctual, generous, kind</b> · always on time.",
              "<b>Harry</b> (kardeşi): younger, a little taller, <b>curly blond hair, green eyes, well-built</b> · lots of friends → <b>outgoing and social</b> · not punctual.",
              "Cevaplar: 1 <b>Sam is shorter than Harry.</b> 2 <b>He is well-built with curly blond hair and green eyes.</b> 3 <b>Harry is outgoing and social.</b>",
              "4 <b>Yes, he is.</b> 5 <b>He is shy, nervous, punctual, generous and kind.</b> 6 <b>Sam is older than Harry.</b>"],
    kelimeler=["plump = tombul", "wavy = dalgalı", "curly = kıvırcık", "blond = sarı saç", "well-built = yapılı", "shy = utangaç", "nervous = gergin", "outgoing = dışa dönük"],
    hatalar=[{"yanlis": "What is Sam like? → He is short and plump.", "dogru": "“like” = kişilik → He is shy, nervous, punctual, generous and kind."},
             {"yanlis": "Who is shorter? → Harry is shorter.", "dogru": "Harry is a little taller than me (Sam) → Sam is shorter than Harry."},
             {"yanlis": "Is Sam a punctual person? → Yes.", "dogru": "Tam cümle: Yes, he is."}],
    tekrar=[{"c": "“Read the text and answer the questions in full sentences.” = Metni oku, soruları {tam cümlelerle|tek kelimeyle} cevapla.", "s": "sınav yönergesi"},
            {"c": "“What does Harry look like?” = Harry'nin {görünüşü nasıl|kişiliği nasıl}? “What is Sam like?” = Sam {nasıl biri (kişilik)|neye benziyor}?", "s": "sınav yönergesi"},
            {"c": "“He is a little taller than me.” (Harry) → {Sam|Harry} is shorter. “He is younger than me.” → {Sam|Harry} is older.", "s": "Part B"},
            {"c": "Harry: {curly blond|dark wavy} hair, {green|brown} eyes, {well-built|plump}.", "s": "Part B"},
            {"c": "Harry has a lot of friends → Harry is {outgoing and social|shy and nervous}.", "s": "Part B"},
            {"c": "Sam: “I am always on time.” → Is Sam a punctual person? {Yes, he is.|No, he isn't.}", "s": "Part B"},
            {"c": "What is Sam like? → He is shy, nervous, {punctual|plump}, generous and {kind|tall}.", "s": "Part B"}])

Y.kazanim(kod=K3, ad="Okuduğu metindeki kişilerin kişiliğini tam cümleyle anlatır.", kisa="Part C: Ellie, Jenny, Jeremy, Rosa", soru=1,
    soruNot="Kâğıtta: Part C (5 soru, 20 puan)", renk="#1d6fa3", konular=["u1k2"], sayfa="Kâğıt, Part C",
    maddeler=["<b>Ellie</b>: fikrini kolay değiştirmez → <b>stubborn</b>; ama <b>respectful and kind</b>.",
              "<b>Jenny</b>: open-minded, always tells the truth, hates lies → <b>honest</b>.",
              "<b>Jeremy</b>: studies hard, high marks → çalışkan (hardworking), <b>lazy değil</b>.",
              "<b>Rosa</b> = metni anlatan (“Me? I am Rosa.”): eşyaları düşürüp kırar → <b>clumsy</b> (sakar); “Thank you / Sorry” der → kibar.",
              "Cevaplar: 1 <b>She is stubborn, respectful and kind.</b> 2 <b>Jenny is honest and never tells lies.</b> 3 <b>No, he isn't.</b>",
              "4 <b>Rosa is clumsy.</b> 5 <b>Yes, they are.</b> (iki kişi → they)"],
    kelimeler=["stubborn = inatçı", "respectful = saygılı", "open-minded = açık fikirli", "honest = dürüst", "hardworking = çalışkan", "lazy = tembel", "clumsy = sakar", "by accident = kazara"],
    hatalar=[{"yanlis": "Who is clumsy? → Jeremy is clumsy.", "dogru": "Rosa (anlatan) eşyaları düşürüp kırıyor → Rosa is clumsy."},
             {"yanlis": "Is Jeremy a lazy person? → Yes, he is.", "dogru": "Jeremy studies hard → No, he isn't."},
             {"yanlis": "Are Ellie and Rosa kind people? → Yes, she is.", "dogru": "İki kişi → Yes, they are."}],
    tekrar=[{"c": "“Read the text and answer the questions in full sentences.” = Metni oku, soruları {tam cümlelerle|kısaca} cevapla.", "s": "sınav yönergesi"},
            {"c": "“Is Jeremy a lazy person?” = Jeremy {tembel biri mi|çalışkan biri mi}?", "s": "sınav yönergesi"},
            {"c": "Ellie doesn't change her mind easily → She is {stubborn|honest|clumsy}, respectful and kind.", "s": "Part C"},
            {"c": "Jenny always tells the truth → {Jenny|Ellie} is honest and never tells lies.", "s": "Part C"},
            {"c": "Jeremy studies hard → Is Jeremy lazy? {No, he isn't.|Yes, he is.}", "s": "Part C"},
            {"c": "“Me? I am Rosa. I always drop and break things.” → {Rosa|Jeremy} is clumsy.", "s": "Part C"},
            {"c": "Are Ellie and Rosa kind people? → Yes, {they are|she is|he is}.", "s": "Part C"}])

BIREY = ["running", "archery", "golf", "karate", "swimming", "wrestling"]
TAKIM = ["football", "basketball", "handball", "ice-hockey", "baseball"]
Y.kazanim(kod=K4, ad="Sporları bireysel ve takım sporları olarak gruplar.", kisa="Part D: Sporlar", soru=1,
    soruNot="Kâğıtta: Part D (20 puan)", renk="#2b8a3e", konular=["u0k2"], sayfa="Kâğıt, Part D",
    maddeler=["<b>Individual sports</b> (tek başına): <b>running, archery, golf, karate, swimming, wrestling</b>.",
              "<b>Team sports</b> (takımla): <b>football, basketball, handball, ice-hockey, baseball</b>.",
              "Ayırma yolu: <b>Takım arkadaşın var mı?</b> Varsa team, yoksa individual.",
              "Soru 2 + 2 istiyor; en kolayları: <b>swimming, running</b> · <b>football, basketball</b>.",
              "archery = okçuluk · wrestling = güreş · ice-hockey = buz hokeyi."],
    kelimeler=["individual = bireysel", "team = takım", "archery = okçuluk", "wrestling = güreş", "swimming = yüzme", "handball = hentbol"],
    hatalar=[{"yanlis": "golf → Team", "dogru": "golf tek başına oynanır → Individual"},
             {"yanlis": "karate → Team", "dogru": "karate → Individual"},
             {"yanlis": "baseball → Individual", "dogru": "baseball takımla oynanır → Team"}],
    tekrar=[{"c": "“Write the names of two individual sports and two team sports.” = İki {bireysel|kış} ve iki takım sporunun adını yaz.", "s": "sınav yönergesi"},
            {"c": "“Individual Sports / Team Sports” = {Bireysel / Takım|Kapalı / Açık} sporlar", "s": "sınav yönergesi"},
            {"c": "running, swimming, archery → {Individual|Team}", "s": "Part D"},
            {"c": "golf, karate, wrestling → {Individual|Team}", "s": "Part D"},
            {"c": "football, basketball, handball → {Team|Individual}", "s": "Part D"},
            {"c": "ice-hockey, baseball → {Team|Individual}", "s": "Part D"}])

Y.kazanim(kod=K5, ad="Günlük rutinlerini sıklık zarflarıyla yazar.", kisa="Part E: Rutin cümleleri", soru=1,
    soruNot="Kâğıtta: Part E (21 puan)", renk="#c2255c", konular=["u0k2"], sayfa="WB s. 86",
    maddeler=["Sıklık zarfları: <b>always</b> (her zaman) · <b>usually</b> (genellikle) · <b>sometimes</b> (bazen) · <b>never</b> (asla).",
              "Kalıp: <b>I + zarf + fiil + …</b> Zarf fiilden önce gelir. (WB s. 86: before the main verb)",
              "Ezber cümle 1: <b>I usually do my homework after school.</b>",
              "Ezber cümle 2: <b>I never go to bed late.</b>",
              "Kâğıttaki örneği (I always watch TV after school) kopyalama; kendi iki cümleni yaz."],
    kelimeler=["always = her zaman", "usually = genellikle", "sometimes = bazen", "never = asla", "do my homework", "go to bed"],
    hatalar=[{"yanlis": "I do usually my homework.", "dogru": "I usually do my homework. (zarf fiilden önce)"},
             {"yanlis": "I never goes to bed late.", "dogru": "I never go to bed late. (I ile -s yok)"},
             {"yanlis": "Usually homework.", "dogru": "Tam cümle: I usually do my homework after school."}],
    tekrar=[{"c": "“Write two sentences about your daily routines.” = Günlük {rutinlerin|tatilin} hakkında iki cümle yaz.", "s": "sınav yönergesi"},
            {"c": "“using frequency adverbs” = {sıklık zarflarını|renkleri} kullanarak", "s": "sınav yönergesi"},
            {"c": "I {usually|usual} do my homework after school.", "s": "WB s. 86"},
            {"c": "I never {go|goes} to bed late.", "s": "WB s. 86"},
            {"c": "Zarf nerede? {I usually do|I do usually} my homework.", "s": "WB s. 86"},
            {"c": "never = {asla|her zaman}, always = {her zaman|bazen}", "s": "WB s. 86"}])

Y.formul(id="tam", ad="Tam cümle", kalip="İsim + is + sıfat (+ than …)", ne="“Who is …?” sorularında", ornek="Sam is older than Jane.")
Y.formul(id="evet", ad="Kısa cevap", kalip="Yes, he/she is. · No, he/she isn't. · Yes, they are.", ne="“Is … ? / Are … ?” sorularında", ornek="Yes, he is.")
Y.formul(id="rutin", ad="Rutin cümlesi", kalip="I + zarf + fiil", ne="Part E", ornek="I never go to bed late.")

# =====================================================================
# ÖĞRETMENİN SORULARI (kâğıt biçimi)
# =====================================================================
def B(cevap, hepsi=None, k=None):
    b = {"cevap": cevap, "genis": True}
    if hepsi: b["hepsi"] = hepsi
    if k: b["k"] = k
    return b
def TAM(harf, soru, cevap, hepsi=None, k=None, ipucu="Metne bak, tam cümleyle yaz."):
    return {"harf": harf, "soru": soru, "kisaCevap": cevap,
            "iskele": {"tur": "doldur", "soru": ipucu, "cumleler": [{"c": "___", "b": [B(cevap, hepsi, k)]}], "aciklama": f"Tam cümle: {cevap}"}}

Y.meb(id="m1", no=1, kazanim=K1, metin=["Comparing Students (Table) — Look at the table and answer the questions."],
      svg=ZI.tablo_svg(["Student", "Age", "Weight", "Height"], [["Jane", "12", "58 kg", "1.52 m"], ["Sam", "13", "62 kg", "1.65 m"]], [86, 70, 92, 92],
                       etiket="Tablo: Jane 12 yaş 58 kg 1.52 m, Sam 13 yaş 62 kg 1.65 m"),
      maddeler=[TAM("a", "1. Who is older, Jane or Sam?", "Sam is older than Jane.", ["sam is older"], ipucu="Tabloya bak, tam cümleyle yaz."),
                TAM("b", "2. Who is taller?", "Sam is taller than Jane.", ["sam is taller"], ipucu="Tabloya bak, tam cümleyle yaz."),
                TAM("c", "3. Who is heavier?", "Sam is heavier than Jane.", ["sam is heavier"], ipucu="Tabloya bak, tam cümleyle yaz.")])

Y.meb(id="m2", no=2, kazanim=K2, metin=["Part B. Read the text and answer the questions in full sentences. (24 points)", METIN_B],
      maddeler=[TAM("a", "1. Who is shorter?", "Sam is shorter than Harry.", ["sam is shorter"]),
                TAM("b", "2. What does Harry look like?", "He is well-built with curly blond hair and green eyes.", ["curly", "blond", "green"]),
                TAM("c", "3. Who is outgoing and social?", "Harry is outgoing and social.", ["harry is"]),
                TAM("d", "4. Is Sam a punctual person?", "Yes, he is.", ["yes", "he is"]),
                TAM("e", "5. What is Sam like?", "He is shy, nervous, punctual, generous and kind.", ["shy", "nervous", "punctual", "generous", "kind"]),
                TAM("f", "6. Who is older?", "Sam is older than Harry.", ["sam is older"])])

Y.meb(id="m3", no=3, kazanim=K3, metin=["Part C. Read the text and answer the questions in full sentences. (20 Points)", METIN_C],
      maddeler=[TAM("a", "1. What is Ellie like?", "She is stubborn, respectful and kind.", ["stubborn", "respectful", "kind"]),
                TAM("b", "2. Who is honest and never tells lies?", "Jenny is honest and never tells lies.", ["jenny"]),
                TAM("c", "3. Is Jeremy a lazy person?", "No, he isn't.", k=["no, he isn't", "no he isn't", "no, he is not", "no he is not", "no, he isnt", "no he isnt"]),
                TAM("d", "4. Who is clumsy?", "Rosa is clumsy.", ["rosa"]),
                TAM("e", "5. Are Ellie and Rosa kind people?", "Yes, they are.", ["yes", "they are"])])

Y.meb(id="m4", no=4, kazanim=K4, metin=["Part D. Sports & Vocabulary (Spor Kelimeleri) (20 points)",
                                         "Kutudaki kelimeler: running, archery, football, golf, karate, swimming, basketball, handball, ice-hockey, baseball, wrestling"],
      maddeler=[{"harf": "a", "soru": "Write the names of two individual sports and two team sports.",
                 "iskele": {"tur": "grupla", "soru": "Kâğıttaki tablo gibi: her sporu doğru sütuna koy.",
                            "kelimeler": ["running", "archery", "football", "golf", "karate", "swimming", "basketball", "handball", "ice-hockey", "baseball", "wrestling"],
                            "kutular": [{"etiket": "Individual Sports", "uyeler": BIREY}, {"etiket": "Team Sports", "uyeler": TAKIM}],
                            "aciklama": "Tek başına yapılanlar individual: running, archery, golf, karate, swimming, wrestling. Takımla oynananlar team: football, basketball, handball, ice-hockey, baseball."},
                 "kisaCevap": "Individual: swimming, running (archery, golf, karate, wrestling) · Team: football, basketball (handball, ice-hockey, baseball)"}])

ZARF = ["always", "usually", "sometimes", "never", "often"]
Y.meb(id="m5", no=5, kazanim=K5, metin=["Part E. (21 points) Soru 4: Writing about Routines (Frequency Adverbs)",
                                         "Write two sentences about your daily routines using frequency adverbs (always, usually, sometimes, never).",
                                         "Example: I always watch TV after school. / I always wake up early on weekdays."],
      maddeler=[{"harf": "a", "soru": "Write two sentences about your daily routines.",
                 "iskele": {"tur": "doldur", "soru": "İki cümle yaz: I + zarf + fiil. (Ezber: I usually do my homework after school. / I never go to bed late.)",
                            "cumleler": [{"c": "___", "b": [B("I usually do my homework after school.", ["i "], ZARF)]},
                                         {"c": "___", "b": [B("I never go to bed late.", ["i "], ZARF)]}],
                            "aciklama": "I ile başlayıp bir sıklık zarfı (always, usually, sometimes, never) içeren anlamlı cümle doğru sayılır. Zarf fiilden önce gelir."},
                 "kisaCevap": "I usually do my homework after school. / I never go to bed late."}])

# =====================================================================
# HOOT'UN HATASI
# =====================================================================
def KH(kazanim, soru, kuark, dogruSik, yanlis1, yanlis2, ipucu, aciklama, dogruCevap):
    Y.kuark(kazanim=kazanim, soru=soru, kuark=kuark, secenekler=[dogruSik, yanlis1, yanlis2], dogru=0, ipucu=ipucu, aciklama=aciklama, dogruCevap=dogruCevap)

KH(K1, "Who is older, Jane or Sam?", "Sam.", "Tam cümle olmalı: Sam is older than Jane.", "Hoot haklı, tek kelime yeter.", "Jane is older than Sam. olmalı.",
   "Yönerge “in full sentences” diyor.", "Tam cümle: İsim + is + older + than + diğeri.", "Sam is older than Jane.")
KH(K1, "Who is heavier?", "Sam is heavyer than Jane.", "heavy → heavier (y düşer, -ier).", "Hoot haklı.", "more heavy olmalı.",
   "heavy -y ile bitiyor.", "heavy → heavier.", "Sam is heavier than Jane.")
KH(K2, "What is Sam like?", "He is short and plump.", "“What is … like?” kişiliği sorar: He is shy, nervous, punctual, generous and kind.", "Hoot haklı.", "He has got brown eyes. olmalı.",
   "“look like” görünüş, “like” kişilik.", "Kişilik: shy, nervous, punctual, generous, kind.", "He is shy, nervous, punctual, generous and kind.")
KH(K2, "Who is shorter?", "Harry is shorter.", "Harry is a little taller than Sam → Sam is shorter than Harry.", "Hoot haklı.", "Both are short. olmalı.",
   "“He is a little taller than me.” cümlesindeki “me” kim?", "Anlatan Sam; Harry ondan uzun.", "Sam is shorter than Harry.")
KH(K3, "Who is clumsy?", "Jeremy is clumsy.", "Eşyaları düşürüp kıran Rosa (anlatan): Rosa is clumsy.", "Hoot haklı.", "Ellie is clumsy. olmalı.",
   "“Me? I am Rosa.” sonrasındaki cümleye bak.", "drop and break things by accident = sakar (clumsy).", "Rosa is clumsy.")
KH(K3, "Are Ellie and Rosa kind people?", "Yes, she is.", "İki kişi → Yes, they are.", "Hoot haklı.", "No, they aren't. olmalı.",
   "Ellie ve Rosa = they.", "Are … ? sorusuna: Yes, they are.", "Yes, they are.")
KH(K4, "Individual or team? golf", "Team", "golf tek başına oynanır → Individual.", "Hoot haklı.", "Hiçbiri.",
   "Golfte takım arkadaşın var mı?", "Individual: running, archery, golf, karate, swimming, wrestling.", "Individual")
KH(K5, "Write a sentence with a frequency adverb.", "I do usually my homework.", "Zarf fiilden önce: I usually do my homework.", "Hoot haklı.", "I usually does my homework. olmalı.",
   "Zarf nerede durur?", "I + zarf + fiil (WB s. 86).", "I usually do my homework after school.")

Y.yaz()
