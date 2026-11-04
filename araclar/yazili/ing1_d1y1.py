"""İngilizce (MEB) 7 · 1. Dönem 1. Yazılı — Yazılıya Hazırlık verisi.
Kapsam: MEB senaryo tablosu, Senaryo 1 (okulun seçtiği): E7.1.R1 (1), E7.1.W1 (1), E7.2.R1 (1), E7.2.W1 (1) = 4 soru.
Kaynaklar: MEB "Yazılıya Hazırlanıyorum 7. Sınıf İngilizce 1. Dönem 1. Yazılı" (10 soru, cevap anahtarıyla; bütün senaryoları kapsıyor,
Senaryo 1'in dört çıktısının hepsi bu 10 soruda), ders kitabı (Bilim Kültür Yayınları; sayfa atıflı; kaynaklar/ing1/unite1.md, unite2.md),
yazilihocam.com 7. sınıf İngilizce 1. dönem 1. yazılı örnekleri (siyah, mavi, kırmızı; benzer sorularda, kimi birebir).
Öncelik (Kemal, 4 Kasım 2026: banko soruya daha çok emek): tek kelimelik / kopyalanan cevaplar ★★★ (m1, m2, m3, m5, m7, m9, m10);
cümleyle cevaplanan m4, m6, m8 ★★ Puan topla.
Not: MEB'in sıklık grafiği (usually %90, often %70, sometimes %50, rarely %10) kitaptaki tablodan (s. 38: usually %80, sometimes %40, seldom %20) farklı;
MEB ölçeği öğretilir, "sorudaki grafiğe göre yaz" denir.
Çalıştır: python3 araclar/yazili/ing1_d1y1.py"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from yazili import Yazili
import cizim_ing as Z


def A(ad, *k): return {"ad": ad, "k": list(k)}
def AS(ad, *sira): return {"ad": ad, "sira": [list(x) for x in sira]}
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

K1, K2, K3, K4 = "E7.1.R1", "E7.1.W1", "E7.2.R1", "E7.2.W1"

# Kalıp notları ("Bu soru senden ne istiyor?" şıkları da bunlardan; birbirinden ayırt edilebilir olmalı)
N_SIFAT = "Davranış ipucu → kişilik sıfatı: “never late” → punctual."
N_ISIM = "Tarifteki ayrıntıyı bul (gözlük, kıvırcık, generous…) → kişinin adı."
N_TABLO1 = "APPEARANCE → boy, saç, göz · PERSONALITY → kişilik sıfatı (metinden kopyala)."
N_ER = "Tablodaki sayıya bak → kısa sıfat -er than, uzun sıfat more … than."
N_DUZELT = "Metinde doğrusunu bul → yalnız yanlış kelimeyi değiştir, cümleyi yeniden yaz."
N_WHAT = "What does … do (after school, on Sundays)? → She/He + fiil-s: “She plays …”"
N_HOWOFTEN = "How often → kaç kez: “twice a week”, “every day”."
N_DOES = "Does …? → “Yes, she does.” / “No, she doesn't.”"
N_WANT = "What does … want to win? → istediği şey: “a gold medal”."
N_SPOR = "Ekipman + yer → spor adı: racket → tennis, bow → archery."
N_WHERE = "Where → yer: “on a court”, “in the park”."
N_INOUT = "Indoor or outdoor? → metindeki kelimeyi seç: “an indoor sport”."
N_NEED = "need → iki ekipman yaz: “a ball and sports shoes”."
N_SIKLIK = "Yüzdeyi ya da gün sayısını bul → sıklık zarfı: %100 always … %0 never."
N_WHATTIME = "What time → “At + saat”: “At seven.”"
N_WHY = "Why → “Because …” ile başla."
N_WHEN = "When → zaman: “after breakfast”, “on Sundays”."
N_HOWLONG = "How long → süre: “four hours” (How often değil!)."
N_TABLO2 = "Sport · Equipment · Place · Frequency → diyalogdan kelimeleri kopyala."

Y = Yazili("ing1", "d1y1",
    baslik="1. Dönem 1. Yazılı", ders="İngilizce (MEB)", senaryo="Senaryo 1", sure=40, tarih="2026-11-12",
    dagilim={K1: 1, K2: 1, K3: 1, K4: 1},
    mebToplam=10, mebHaric=[],   # MEB dokümanının 10 sorusunun hepsi Senaryo 1'in çıktılarından (dosya başı notu)
    giris="Okulun seçtiği Senaryo 1'de <b>4 soru</b> var: her konudan 1 soru, her soruda 4–5 küçük madde. "
          "Önce <b>★★★ Banko</b> soruları sağlamla: cevap tek kelime ya da metinden kopyalanan bir parça. Kalıbını bilirsen puan kesin.",
    kapsamDisi=["Unit 3: Biographies, Unit 4: Wild Animals, Unit 5: Television", "Dinleme (Listening) ve konuşma (Speaking) etkinlikleri"],
    puanNotu="Puanlar tahminidir: 4 soru × 25 puan varsaydık; okul farklı dağıtabilir. Her konudan hangi MEB soru tipinin geleceği bilinmiyor; bu yüzden her konunun 2–3 tipine çalışıyoruz.",
    kaynakNotu="Sorular MEB'in yayımladığı 'Yazılıya Hazırlanıyorum 7. Sınıf İngilizce 1. Dönem 1. Yazılı' örneklerine, ders kitabına (Bilim Kültür Yayınları) ve yazilihocam.com yazılı örneklerine dayanır. Kişi çizimleri özgündür.",
    soruGiris="Bunlar MEB'in örnek soruları; yazılıda <b>benzerleri</b> çıkacak. <b>★★★ Banko</b> olanlarla başla. Cevabı kısa yaz: tek kelime ya da metinden kopyaladığın parça yeter.",
    kazanimAd="konu")

# =====================================================================
# KONULAR (Hatırla kartları + Hatırla ve Tekrarla boşlukları)
# =====================================================================
Y.kazanim(kod=K1, ad="Students will be able to understand a simple text about appearances, personalities, and comparisons including explanations and reasons.",
    kisa="Görünüş ve Kişilik (okuma)", soru=1, renk="#1971c2", konular=["u1k1", "u1k2"], sayfa="s. 10–23", svg=Z.h_gorunus(),
    maddeler=["Görünüş (<b>What does she look like?</b>): <b>tall / short</b>, <b>slim / thin / plump</b>, <b>beautiful / handsome / cute</b>, <b>young / old</b>. (s. 13, 14)",
              "Saç: uzunluk + şekil + renk + hair → <b>long / short</b> + <b>straight / wavy / curly</b> + <b>blonde, brown, dark, black</b>. “with blue eyes” = mavi gözlü. Kızıl saç: <b>ginger</b> (MEB örneği). (s. 14, 20)",
              "Kişilik (<b>What is he like?</b>): davranış → sıfat. always on time → <b>punctual</b> · never tells lies → <b>honest</b> · buys gifts, shares → <b>generous</b> · a lot of friends → <b>outgoing</b>. (s. 15)",
              "Diğerleri: doesn't like sharing → <b>selfish</b> (bencil) · never changes his mind → <b>stubborn</b> · studies hard → <b>hardworking</b>. (s. 10, 16)",
              "Tablo sorusu: <b>APPEARANCE</b> = görünüş (boy, kilo, saç, göz) · <b>PERSONALITY</b> = kişilik (sıfat). Kelimeleri diyalogdan <b>aynen kopyala</b>. (MEB örnek sorusu)",
              "Resimle eşleştirme: her kişinin <b>farklı olan</b> ayrıntısını bul: glasses (gözlük), curly (kıvırcık), plump (kilolu), ginger (kızıl). (MEB örnek sorusu)"],
    kelimeler=["tall – short", "slim – plump", "straight – wavy – curly", "punctual = zamanında gelen", "honest = dürüst", "generous = cömert", "selfish = bencil", "outgoing = sosyal"],
    hatalar=[{"yanlis": "Paylaşmayı sevmeyen kişi için “generous” yazmak.", "dogru": "Paylaşmayan kişi selfish (bencil); paylaşan kişi generous (cömert)."},
             {"yanlis": "“always on time” için “outgoing” yazmak.", "dogru": "Zamanında gelen kişi punctual; çok arkadaşı olan kişi outgoing."},
             {"yanlis": "APPEARANCE sütununa “serious, hardworking” yazmak.", "dogru": "Kişilik sıfatları PERSONALITY sütununa; APPEARANCE'a boy, saç, göz."}],
    tekrar=[{"c": "Tom is never late. He always arrives on time. He is {punctual|outgoing|selfish}.", "s": "s. 15"},
            {"c": "Mike never tells lies. He is {honest|stubborn|cute}.", "s": "s. 15"},
            {"c": "My brother doesn't like sharing his things. He is {selfish|generous|honest}.", "s": "s. 10"},
            {"c": "Helen likes meeting new people and she has a lot of friends. She is {outgoing|punctual|selfish}.", "s": "s. 15"},
            {"c": "Sally always studies hard for the exams. She is {hardworking|selfish|cute}.", "s": "s. 16"},
            {"c": "Kıvırcık saç İngilizcede {curly|straight} hair, düz saç {straight|curly} hair.", "s": "s. 14, 20"},
            {"c": "Tablodaki APPEARANCE sütununa {tall, slim, dark hair|serious, hardworking} yazılır.", "s": "cevap kalıbı"}])

Y.kazanim(kod=K2, ad="Students will be able to write simple pieces to compare people.",
    kisa="Karşılaştırma (yazma)", soru=1, renk="#e8590c", konular=["u1k3"], sayfa="s. 11–24", svg=Z.h_karsilastir(),
    maddeler=["Kısa sıfat + <b>-er than</b>: old → <b>older</b>, young → <b>younger</b>, tall → <b>taller</b>, short → <b>shorter</b>. “Jim is taller than Mike.” (s. 13, 21)",
              "Harf değişen sıfatlar: slim → <b>slimmer</b>, thin → thinner; -y → <b>-ier</b>: heavy → heavier, funny → funnier. (s. 21, 23, 24)",
              "Uzun sıfat: <b>more + sıfat + than</b>: more generous, more outgoing, more punctual, more hardworking. (s. 13, 16, 21)",
              "Düzensiz: good → <b>better</b> (He can play football better than everyone else.). (s. 11)",
              "Tablodan yazma: yaş büyükse <b>older</b>, küçükse <b>younger</b>; boy uzunsa <b>taller</b>, kısaysa <b>shorter</b>; kilo azsa <b>lighter / thinner</b>; yıldız çoksa <b>more …</b>. (MEB örnek sorusu)",
              "Yanlışı düzelt: metinde doğrusunu bul, <b>yalnız yanlış kelimeyi</b> değiştir, cümlenin geri kalanını aynen yaz. Bazen isimler yer değiştirir: “Emma is more outgoing than Amy.” (MEB örnek sorusu)"],
    kelimeler=["than = -den daha", "older – younger", "taller – shorter", "heavier – lighter", "more generous", "better", "yalnız yanlış kelimeyi değiştir"],
    hatalar=[{"yanlis": "generous → generouser", "dogru": "Uzun sıfat -er almaz: more generous."},
             {"yanlis": "Helen is more taller than Sally.", "dogru": "Kısa sıfatta more yok: taller."},
             {"yanlis": "Amy is older Emma. (than unutulmuş)", "dogru": "İki kişinin arasına than: Amy is older than Emma."}],
    tekrar=[{"c": "Helen is 17, Sally is 15. Helen is {older|younger} than Sally.", "s": "MEB örnek sorusu"},
            {"c": "Sally is 1.71 m, Helen is 1.65 m. Helen is {shorter|taller} than Sally.", "s": "MEB örnek sorusu"},
            {"c": "slim → {slimmer|slimer}", "s": "s. 21"},
            {"c": "generous → {more generous|generouser}", "s": "s. 21"},
            {"c": "good → {better|gooder}", "s": "s. 11"},
            {"c": "Karşılaştırmada iki kişinin arasına {than|that|then} yazılır.", "s": "s. 13"},
            {"c": "Yanlışı düzeltirken {yalnız yanlış kelimeyi değiştir|bütün cümleyi baştan uydur}.", "s": "cevap kalıbı"}])

Y.kazanim(kod=K3, ad="Students will be able to understand short and simple texts on sports.",
    kisa="Spor Metinlerini Anlama", soru=1, renk="#2f9e44", konular=["u2k1", "u2k2", "u2k3"], sayfa="s. 28–41", svg=Z.h_spor(),
    maddeler=["Ekipmandan spor: <b>racket + net</b> → tennis · <b>ball + basket</b> → basketball · <b>kick + goal</b> → football · <b>bow + arrows</b> → archery · <b>sneakers + mountains</b> → hiking. (s. 32, 34; archery MEB örneği)",
              "<b>team game</b> (basketball: 5 kişilik takım) – <b>individual sport</b> (swimming). <b>indoor</b> (gym, court) – <b>outdoor</b> (park, mountains, sea). (s. 29, 32)",
              "Soru kelimesi: <b>What … do?</b> → ne yapıyor (fiil) · <b>How often?</b> → kaç kez (twice a week) · <b>Does …?</b> → Yes, she does. / No, she doesn't. (s. 30, 31)",
              "Cevabı metinde bul: sorudaki zaman ifadesini (<b>after school, on Sundays</b>) metinde ara, o cümleyi kopyala. (cevap kalıbı)",
              "I → she / he olunca fiile <b>-s</b>: I play → she <b>plays</b> · I go → she <b>goes</b> · I ride → she <b>rides</b>. (s. 30: He goes jogging twice a week.)",
              "Günleri say: <b>Tuesdays and Thursdays</b> = haftada 2 gün = <b>twice a week</b>. (MEB örnek sorusu)"],
    kelimeler=["racket → tennis", "basket → basketball", "bow → archery", "How often → twice a week", "Does … ? → Yes, she does.", "she plays / goes / rides"],
    hatalar=[{"yanlis": "She play volleyball.", "dogru": "she / he ile fiil -s alır: She plays volleyball."},
             {"yanlis": "How often does she go hiking? → In the mountains.", "dogru": "How often kaç kez diye sorar: Twice a week."},
             {"yanlis": "Does she go to bed early? → Yes, she is.", "dogru": "Does ile sorulursa does ile cevapla: Yes, she does."}],
    tekrar=[{"c": "You need a racket and a ball. You hit the ball over the net. → {tennis|football|swimming}", "s": "s. 32"},
            {"c": "You kick the ball into the goal. There are 11 players in each team. → {football|basketball|archery}", "s": "MEB örnek sorusu"},
            {"c": "You need a bow and some arrows. → {archery|hiking|cycling}", "s": "MEB örnek sorusu"},
            {"c": "How often does she go hiking? → {Twice a week.|In the mountains.|Yes, she does.}", "s": "s. 30"},
            {"c": "Does she go to bed early? → {Yes, she does.|Yes, she is.}", "s": "cevap kalıbı"},
            {"c": "I play volleyball. → She {plays|play} volleyball.", "s": "s. 30"},
            {"c": "Swimming is an {individual|team} sport.", "s": "s. 32"}])

Y.kazanim(kod=K4, ad="Students will be able to write pieces about routines/daily activities by using frequency adverbs.",
    kisa="Rutinler ve Sıklık Zarfları (yazma)", soru=1, renk="#7048e8", konular=["u2k3"], sayfa="s. 29–41", svg=Z.h_siklik(),
    maddeler=["MEB grafiği: <b>always %100 · usually %90 · often %70 · sometimes %50 · rarely %10 · never %0</b>. (MEB örnek sorusu)",
              "Kitaptaki tabloda yüzdeler biraz farklı (usually %80, sometimes %40, seldom %20). Sınavda <b>sorudaki grafiğe göre</b> yaz. (s. 38)",
              "Zarfın yeri: özneden sonra, fiilden önce: I <b>always</b> get up early. She <b>never</b> eats junk food. (s. 31, 36)",
              "How often? → <b>every day</b>, <b>once a week</b>, <b>twice a week</b>, <b>three / four times a week</b>. (s. 30, 31, 39)",
              "Spor tablosu: <b>Sport</b> (spor), <b>Equipment</b> (ekipman: racket, ball), <b>Place</b> (yer: court, gym), <b>Frequency</b> (kaç kez: twice a week). Diyalogdan kopyala. (MEB örnek sorusu)",
              "<b>Why?</b> → Because … · <b>What time?</b> → At seven. · <b>How long?</b> → four hours (süre). (s. 41; MEB örnek sorusu)"],
    kelimeler=["always %100", "usually %90", "often %70", "sometimes %50", "never %0", "twice a week", "Because …", "At seven."],
    hatalar=[{"yanlis": "%50 → usually", "dogru": "%50 sometimes; usually %90."},
             {"yanlis": "I eat never junk food.", "dogru": "Zarf fiilden önce: I never eat junk food."},
             {"yanlis": "Frequency sütununa “tennis court” yazmak.", "dogru": "Frequency = kaç kez: twice a week. Yer Place sütununa."}],
    tekrar=[{"c": "%100 → {always|usually|never}", "s": "MEB örnek sorusu"},
            {"c": "%0 → {never|sometimes|always}", "s": "MEB örnek sorusu"},
            {"c": "%50 → {sometimes|usually|often}", "s": "MEB örnek sorusu"},
            {"c": "%90 → {usually|rarely|sometimes}", "s": "MEB örnek sorusu"},
            {"c": "%70 → {often|never|always}", "s": "MEB örnek sorusu"},
            {"c": "Haftada iki kez = {twice a week|two weeks}", "s": "s. 30"},
            {"c": "Why sorusunun cevabı {Because|So|And} ile başlar.", "s": "cevap kalıbı"}])

# =====================================================================
# CEVAP KALIPLARI (Özet'te liste; sorunun içinde tek satır kalıp notu)
# =====================================================================
Y.formul(id="sifat", ad="Davranıştan kişilik sıfatı", kalip="İpucu cümlesi → sıfat (never late → punctual)", ne="“Complete the sentences with the correct words” sorularında", ornek="Mike never tells lies. He is honest.")
Y.formul(id="isim", ad="Tariften isim", kalip="Resimdeki ayrıntıyı cümlede bul → isim", ne="“Write the correct names”, “Who …?” sorularında", ornek="Gözlüklü, kıvırcık saçlı → Zack")
Y.formul(id="tablo1", ad="Görünüş / kişilik tablosu", kalip="APPEARANCE: boy, saç, göz · PERSONALITY: kişilik sıfatı", ne="“Complete the table according to the dialogue” sorularında", ornek="Sam → tall, slim, dark hair · serious, hardworking")
Y.formul(id="er", ad="Karşılaştırma", kalip="Kısa sıfat + -er than · uzun sıfat: more … than", ne="“Look at the table and complete the sentences” sorularında", ornek="Helen is older than Sally. Sally is more generous than Helen.")
Y.formul(id="duzelt", ad="Yanlışı düzelt", kalip="Metinde doğrusunu bul + yalnız yanlış kelimeyi değiştir", ne="“Correct the mistakes. Rewrite the sentences.” sorularında", ornek="Amy is younger than Emma. → Amy is older than Emma.")
Y.formul(id="soru", ad="Soru kelimesi → cevap", kalip="What … do? → She plays … · How often? → twice a week · Does …? → Yes, she does.", ne="“Answer the questions according to the text” sorularında", ornek="How often does she go hiking? → Twice a week.")
Y.formul(id="spor", ad="Ekipmandan spor", kalip="Ekipman + yer → spor adı", ne="“Write the correct sports” sorularında", ornek="racket + net → tennis")
Y.formul(id="siklik", ad="Sıklık zarfı", kalip="always %100 · usually %90 · often %70 · sometimes %50 · rarely %10 · never %0", ne="“Fill in the blanks according to the chart” sorularında", ornek="I never eat junk food. (0%)")
Y.formul(id="tablo2", ad="Spor tablosu", kalip="Sport · Equipment · Place · Frequency → diyalogdan kopyala", ne="Spor diyaloglu tablo sorularında", ornek="tennis · racket and ball · tennis court · twice a week")
Y.formul(id="neden", ad="Why / What time / How long", kalip="Why → Because … · What time → At seven. · How long → four hours", ne="“Why …?”, “What time …?” sorularında", ornek="Because he wants to be a successful football player.")

# =====================================================================
# MEB SORULARI (10 soru) — öncelik: 7 banko, 3 puan topla
# =====================================================================
Y.meb(id="m1", no=1, kazanim=K1, oncelik=3,
    metin=["Complete the sentences with the correct words. (Cümleleri doğru kelimelerle tamamla.)",
           "1. Sally always does her homework and studies hard for the exams. She is ______.",
           "2. Tom is never late for school. He always arrives on time. He is ______.",
           "3. My brother doesn't like sharing his things. He is ______.",
           "4. Helen likes meeting new people and she has a lot of friends. She is ______.",
           "5. Mike never tells lies. He always tells the truth. He is ______."],
    maddeler=[Q(M("a", "Complete the sentences 1–5 with the correct words.",
        "1. She is hardworking. 2. He is punctual. 3. He is selfish. 4. She is outgoing. 5. He is honest.",
        [A("1. hardworking", "hardworking", "hard-working"), A("2. punctual", "punctual"), A("3. selfish", "selfish"), A("4. outgoing", "outgoing"), A("5. honest", "honest")], "sifat"),
        ["correct words"], N_SIFAT,
        B("hardworking, punctual, selfish, outgoing, honest", "hardworking, punctual, selfish", "hardworking, outgoing, generous, punctual, honest",
          "Her cümledeki davranışa bak: zamanında gelmek, paylaşmamak, çok arkadaş, yalan söylememek.",
          "Davranıştan sıfat: studies hard → hardworking, on time → punctual, doesn't share → selfish, a lot of friends → outgoing, never tells lies → honest. (s. 10, 15, 16)",
          P("1. studies hard → She is", "hardworking", ["lazy", "stubborn"], k=["hardworking", "hard-working"]),
          P("2. never late → He is", "punctual", ["outgoing", "selfish"], k=["punctual"]),
          P("3. doesn't like sharing → He is", "selfish", ["generous", "honest"], k=["selfish"]),
          P("4. a lot of friends → She is", "outgoing", ["punctual", "stubborn"], k=["outgoing"]),
          P("5. never tells lies → He is", "honest", ["selfish", "cute"], k=["honest"])))],
    ikizler=[
        {"metin": ["Read the clues and write the correct personality adjective. (İpuçlarını oku, doğru kişilik sıfatını yaz.)",
                   "Word bank: patient – helpful – punctual – generous – hardworking – selfish",
                   "1. Mert waits calmly when something takes a long time. Mert is ______.",
                   "2. Elif helps her classmates when they have difficulty with their homework. Elif is ______.",
                   "3. Can always comes to school before the bell rings. Can is ______.",
                   "4. Zeynep enjoys giving presents and sharing her things with others. Zeynep is ______.",
                   "5. Arda studies regularly and never leaves his schoolwork unfinished. Arda is ______."],
         "maddeler": [M("a", "Write the correct personality adjective for 1–5.", "1. Mert is patient. 2. Elif is helpful. 3. Can is punctual. 4. Zeynep is generous. 5. Arda is hardworking.",
                        [A("1. patient", "patient"), A("2. helpful", "helpful"), A("3. punctual", "punctual"), A("4. generous", "generous"), A("5. hardworking", "hardworking", "hard-working")], "sifat")]},
        {"metin": ["Read the classroom notes and answer the questions. (Sınıf notlarını oku, soruları cevapla.)",
                   "Our teacher gives us a group project. Ece always shares her materials with her friends and helps them. Kerem never arrives late for group meetings. Mert loves meeting new people and he has a lot of friends."],
         "maddeler": [M("a", "Who is generous? Who is punctual? Who is outgoing?", "Ece is generous. Kerem is punctual. Mert is outgoing.",
                        [A("generous → Ece", "ece"), A("punctual → Kerem", "kerem"), A("outgoing → Mert", "mert")], "isim")]}])

Y.meb(id="m2", no=2, kazanim=K1, oncelik=3,
    metin=["Read the sentences and fill in the table with the correct names. (Cümleleri oku, resimlerin altına doğru isimleri yaz.)",
           "Sarah is a beautiful girl with blue eyes and blonde hair.",
           "Zack has curly brown hair. He wears glasses.",
           "Tom has short wavy hair. He is thin.",
           "Daisy has brown eyes. She is cute with wavy ginger hair.",
           "Jack is plump with short brown hair. He has brown eyes."],
    svg=Z.kisiler([dict(sac="ginger", stil="uzun_dalgali", goz="brown", tisort="#ae3ec9"), dict(sac="brown", stil="dalgali", beden="ince", tisort="#e03131"),
                   dict(sac="brown", stil="kisa", goz="brown", beden="kilolu", tisort="#f08c00"), dict(sac="blonde", stil="uzun_duz", goz="blue", tisort="#1c7ed6"),
                   dict(sac="brown", stil="kivircik", gozluk=True, tisort="#495057")], "Beş kişinin resmi: 1, 2, 3, 4, 5"),
    maddeler=[Q(M("a", "Write the correct names for pictures 1–5.", "1. Daisy 2. Tom 3. Jack 4. Sarah 5. Zack",
        [A("1. resim → Daisy (kızıl dalgalı saç)", "daisy"), A("2. resim → Tom (kısa dalgalı saç, ince)", "tom"), A("3. resim → Jack (kilolu)", "jack"),
         A("4. resim → Sarah (sarı saç, mavi göz)", "sarah"), A("5. resim → Zack (gözlük, kıvırcık)", "zack")], "isim"),
        ["correct names"], N_ISIM,
        B("1 Daisy, 2 Tom, 3 Jack, 4 Sarah, 5 Zack", "1 Daisy, 2 Tom, 3 Jack", "1 Sarah, 2 Tom, 3 Jack, 4 Daisy, 5 Zack",
          "Önce en kolay ayrıntıyı bul: gözlüklü kim? Kilolu kim? Kızıl saçlı kim?",
          "Zack gözlüklü ve kıvırcık; Jack plump (kilolu); Daisy ginger (kızıl) dalgalı saçlı; Sarah blonde, mavi gözlü; Tom ince, kısa dalgalı saçlı. (MEB örnek sorusu; s. 14, 20)",
          P("Resim 1 →", "Daisy", ["Sarah", "Zack"], k=["daisy"]),
          P("Resim 2 →", "Tom", ["Jack", "Zack"], k=["tom"]),
          P("Resim 3 →", "Jack", ["Tom", "Sarah"], k=["jack"]),
          P("Resim 4 →", "Sarah", ["Daisy", "Tom"], k=["sarah"]),
          P("Resim 5 →", "Zack", ["Jack", "Daisy"], k=["zack"])))],
    ikizler=[
        {"metin": ["Read the sentences and write the correct names. (Cümleleri oku, doğru isimleri yaz.)",
                   "Mina has long wavy brown hair and brown eyes.",
                   "Lara has short straight blonde hair and blue eyes.",
                   "Bora is plump with short black hair.",
                   "Melis is tall. She has long curly brown hair."],
         "svg": Z.kisiler([dict(sac="black", stil="kisa", goz="brown", beden="kilolu", tisort="#2f9e44"), dict(sac="brown", stil="uzun_dalgali", goz="brown", tisort="#e64980"),
                           dict(sac="blonde", stil="kisa", goz="blue", tisort="#1c7ed6"), dict(sac="brown", stil="uzun_kivircik", goz="green", beden="ince", tisort="#f08c00")], "Dört kişinin resmi: 1, 2, 3, 4"),
         "maddeler": [M("a", "Write the correct names for pictures 1–4.", "1. Bora 2. Mina 3. Lara 4. Melis",
                        [A("1. resim → Bora", "bora"), A("2. resim → Mina", "mina"), A("3. resim → Lara", "lara"), A("4. resim → Melis", "melis")], "isim")]},
        {"metin": ["Read the text and answer the questions. (Metni oku, soruları cevapla.)",
                   "Ali is tall and thin. He wears glasses. Ece is cute with long ginger hair. Can is plump with short black hair. Defne is beautiful with blue eyes and blonde hair."],
         "maddeler": [M("a", "Who wears glasses? Who is plump? Who has ginger hair? Who has blue eyes?", "Ali wears glasses. Can is plump. Ece has ginger hair. Defne has blue eyes.",
                        [A("glasses → Ali", "ali"), A("plump → Can", "can"), A("ginger hair → Ece", "ece"), A("blue eyes → Defne", "defne")], "isim")]}])

Y.meb(id="m5", no=5, kazanim=K1, oncelik=3,
    metin=["Complete the table according to the dialogue. (Diyaloğa göre tabloyu doldur.)",
           "Leo: Do you know my brothers?",
           "Mia: No, I don't. What are they like?",
           "Leo: Well, Sam and Brian are different from each other. Sam is tall and slim with dark hair. He is very serious and hardworking.",
           "Mia: What about Brian?",
           "Leo: Brian is short and he has blond hair. He is very funny and outgoing. He loves meeting new people.",
           "Mia: So, Brian is more social than Sam.",
           "Leo: Exactly!"],
    maddeler=[
        Q(M("a", "Complete the table for SAM: APPEARANCE and PERSONALITY.", "Appearance: tall, slim, dark hair. Personality: serious, hardworking.",
            [A("tall", "tall"), A("slim", "slim"), A("dark hair", "dark"), A("serious", "serious"), A("hardworking", "hardworking", "hard-working")], "tablo1"),
          ["APPEARANCE", "PERSONALITY"], N_TABLO1,
          B("Appearance: tall, slim, dark hair · Personality: serious, hardworking", "Appearance: tall · Personality: serious", "Appearance: serious, hardworking · Personality: tall, slim, dark hair",
            "Sam'in cümlesini bul. Boy ve saç bir sütuna, sıfatlar öbür sütuna.",
            "“Sam is tall and slim with dark hair.” → APPEARANCE. “He is very serious and hardworking.” → PERSONALITY. (MEB örnek sorusu)",
            P("Appearance:", "tall, slim, dark hair", ["serious, hardworking", "short, blond hair"], hepsi=[["tall"], ["slim"], ["dark"]]),
            P("Personality:", "serious, hardworking", ["funny, outgoing", "tall, slim"], hepsi=[["serious"], ["hardworking", "hard-working"]]))),
        Q(M("b", "Complete the table for BRIAN: APPEARANCE and PERSONALITY.", "Appearance: short, blond hair. Personality: funny, outgoing (social).",
            [A("short", "short"), A("blond hair", "blond"), A("funny", "funny"), A("outgoing / social", "outgoing", "social")], "tablo1"),
          ["APPEARANCE", "PERSONALITY"], N_TABLO1,
          B("Appearance: short, blond hair · Personality: funny, outgoing", "Appearance: short · Personality: funny", "Appearance: funny, outgoing · Personality: short, blond hair",
            "Brian'ın cümlesini bul: önce görünüş, sonra kişilik.",
            "“Brian is short and he has blond hair.” → APPEARANCE. “He is very funny and outgoing.” → PERSONALITY. (MEB örnek sorusu)",
            P("Appearance:", "short, blond hair", ["tall, dark hair", "funny, outgoing"], hepsi=[["short"], ["blond"]]),
            P("Personality:", "funny, outgoing", ["serious, hardworking", "short, blond hair"], hepsi=[["funny"], ["outgoing", "social"]])))],
    ikizler=[
        {"metin": ["Read the text and complete the table. (Metni oku, tabloyu doldur.)",
                   "Kerem and Arda are classmates, but they are quite different. Kerem has short curly hair and brown eyes. He is cheerful and talkative, so he easily makes new friends. "
                   "Arda has straight black hair and green eyes. He is quieter than Kerem, but he is very patient and helpful. Arda is also taller than Kerem."],
         "maddeler": [M("a", "Complete the table for KEREM: APPEARANCE and PERSONALITY.", "Appearance: short curly hair, brown eyes. Personality: cheerful, talkative.",
                        [A("curly hair", "curly"), A("brown eyes", "brown"), A("cheerful", "cheerful"), A("talkative", "talkative")], "tablo1"),
                      M("b", "Complete the table for ARDA: APPEARANCE and PERSONALITY.", "Appearance: straight black hair, green eyes, tall. Personality: quiet, patient, helpful.",
                        [A("straight black hair", "straight"), A("green eyes", "green"), A("patient", "patient"), A("helpful", "helpful")], "tablo1")]},
        {"metin": ["Read the text and complete the table. (Metni oku, tabloyu doldur.)",
                   "Betty and Lucy are sisters, but they are very different. Betty has long wavy blonde hair and brown eyes. Lucy is short with straight dark hair and blue eyes. "
                   "Betty is more hardworking than Lucy. She always does her homework and studies hard. She is also more outgoing than Lucy. She has a lot of friends. "
                   "Lucy is shy and quiet. She loves being alone. She is sometimes stubborn. She never changes her mind."],
         "maddeler": [M("a", "Complete the table for BETTY: APPEARANCE and PERSONALITY.", "Appearance: long wavy blonde hair, brown eyes. Personality: hardworking, outgoing.",
                        [A("wavy hair", "wavy"), A("blonde hair", "blond"), A("hardworking", "hardworking", "hard-working"), A("outgoing", "outgoing")], "tablo1"),
                      M("b", "Complete the table for LUCY: APPEARANCE and PERSONALITY.", "Appearance: short, straight dark hair, blue eyes. Personality: shy, quiet, stubborn.",
                        [A("straight hair", "straight"), A("blue eyes", "blue"), A("shy / quiet", "shy", "quiet"), A("stubborn", "stubborn")], "tablo1")]}])

Y.meb(id="m3", no=3, kazanim=K2, oncelik=3,
    metin=["Look at the table and complete the sentences. (Tabloya bak, cümleleri tamamla.)",
           "1. Helen is ______ than Sally. (age)",
           "2. Sally is ______ than Helen. (age)",
           "3. Helen is ______ than Sally. (height)",
           "4. Sally is ______ than Helen. (weight)",
           "5. Sally is ______ than Helen. (personality)"],
    svg=Z.tablo_svg(["", "SALLY", "HELEN"], [["AGE", "15", "17"], ["HEIGHT", "1.71 m", "1.65 m"], ["WEIGHT", "45 kg", "50 kg"], ["PERSONALITY", "generous *****", "generous **"]], [114, 108, 108],
                    etiket="Sally ve Helen tablosu: yaş 15 ve 17, boy 1.71 m ve 1.65 m, kilo 45 kg ve 50 kg, cömertlik 5 yıldız ve 2 yıldız"),
    maddeler=[Q(M("a", "Look at the table and complete the sentences 1–5.", "1. Helen is older than Sally. 2. Sally is younger than Helen. 3. Helen is shorter than Sally. 4. Sally is lighter than Helen. 5. Sally is more generous than Helen.",
        [A("1. older", "older"), A("2. younger", "younger"), A("3. shorter", "shorter"), A("4. lighter / thinner / slimmer", "lighter", "thinner", "slimmer"), A("5. more generous", "more generous")], "er"),
        ["Look at the table"], N_ER,
        B("older, younger, shorter, lighter, more generous", "older, younger, shorter", "older, younger, taller, heavier, generouser",
          "Her cümlede ilk kişinin sayısı büyük mü küçük mü? Cömertlikte yıldızları say.",
          "Helen 17 > Sally 15 → older / younger. Helen 1.65 < 1.71 → shorter. Sally 45 kg < 50 kg → lighter. 5 yıldız > 2 yıldız → more generous (uzun sıfat). (MEB örnek sorusu; s. 21)",
          P("1. Helen … than Sally (age) →", "older", ["younger", "taller"], k=["older"]),
          P("2. Sally … than Helen (age) →", "younger", ["older", "shorter"], k=["younger"]),
          P("3. Helen … than Sally (height) →", "shorter", ["taller", "older"], k=["shorter"]),
          P("4. Sally … than Helen (weight) →", "lighter", ["heavier", "fatter"], k=["lighter", "thinner", "slimmer"]),
          P("5. Sally … than Helen (personality) →", "more generous", ["very generous", "less generous"], k=["more generous"])))],
    ikizler=[
        {"metin": ["Look at the table and complete the sentences. (Tabloya bak, cümleleri tamamla.)",
                   "1. Duru is ______ than Ece. (young)",
                   "2. Duru is ______ than Ece. (tall)",
                   "3. Duru is ______ than Ece. (hardworking)",
                   "4. Ece is ______ than Duru. (talkative)",
                   "5. Duru is ______ than Ece. (punctual)"],
         "svg": Z.tablo_svg(["", "ECE", "DURU"], [["AGE", "13", "12"], ["HEIGHT", "158 cm", "165 cm"], ["STUDIES", "2 hours a day", "3 hours a day"],
                                                   ["TALKS", "to everyone", "usually quiet"], ["AT SCHOOL", "at 8.10", "at 7.55"]], [96, 117, 117],
                            etiket="Ece ve Duru tablosu: yaş 13 ve 12, boy 158 ve 165 cm, ders çalışma 2 ve 3 saat, Ece herkesle konuşur, Duru sessiz, okula 8.10 ve 7.55'te gelir"),
         "maddeler": [M("a", "Look at the table and complete the sentences 1–5.", "1. Duru is younger than Ece. 2. Duru is taller than Ece. 3. Duru is more hardworking than Ece. 4. Ece is more talkative than Duru. 5. Duru is more punctual than Ece.",
                        [A("1. younger", "younger"), A("2. taller", "taller"), A("3. more hardworking", "more hardworking", "more hard-working"), A("4. more talkative", "more talkative"), A("5. more punctual", "more punctual")], "er")]},
        {"metin": ["Look at the table and complete the sentences. (Tabloya bak, cümleleri tamamla.)",
                   "1. Can is ______ than Mert. (age)",
                   "2. Mert is ______ than Can. (age)",
                   "3. Mert is ______ than Can. (height)",
                   "4. Can is ______ than Mert. (weight)",
                   "5. Mert is ______ than Can. (personality)"],
         "svg": Z.tablo_svg(["", "CAN", "MERT"], [["AGE", "13", "11"], ["HEIGHT", "1.50 m", "1.62 m"], ["WEIGHT", "48 kg", "40 kg"], ["PERSONALITY", "punctual **", "punctual *****"]], [110, 110, 110],
                            etiket="Can ve Mert tablosu: yaş 13 ve 11, boy 1.50 ve 1.62 m, kilo 48 ve 40 kg, dakiklik 2 ve 5 yıldız"),
         "maddeler": [M("a", "Look at the table and complete the sentences 1–5.", "1. Can is older than Mert. 2. Mert is younger than Can. 3. Mert is taller than Can. 4. Can is heavier than Mert. 5. Mert is more punctual than Can.",
                        [A("1. older", "older"), A("2. younger", "younger"), A("3. taller", "taller"), A("4. heavier", "heavier", "fatter"), A("5. more punctual", "more punctual")], "er")]}])

Y.meb(id="m4", no=4, kazanim=K2, oncelik=2,
    metin=["Read the text and correct the mistakes. Rewrite the sentences. (Metni oku, yanlışları düzelt, cümleleri yeniden yaz.)",
           "Amy is 16 years old, and her sister Emma is 12 years old. Amy is 165 cm tall and Emma is 160 cm tall. Amy is slim with straight blonde hair and brown eyes. "
           "Emma has short wavy hair and green eyes. Amy is more hardworking; she always studies hard and does her homework. Emma is more outgoing than her sister; "
           "she likes meeting new people. Amy can sometimes be stubborn. She doesn't change her mind easily."],
    maddeler=[
        Q(M("a", "Correct the mistake and rewrite: 1. Amy is younger than Emma.", "Amy is older than Emma.",
            [A("older (ya da: Emma is younger)", "older", "emma is younger"), A("than Emma / than Amy", "than emma", "than amy")], "duzelt"),
          ["Correct the mistake"], N_DUZELT,
          B("Amy is older than Emma.", "older", "Amy is younger than Emma.",
            "Metinde Amy kaç yaşında, Emma kaç yaşında? Sonra yalnız yanlış kelimeyi değiştir.",
            "Amy 16, Emma 12 → Amy daha büyük: younger yerine older. Cümlenin geri kalanı aynı kalır. (MEB örnek sorusu)",
            P("Amy is", "older", ["younger", "taller"], k=["older"]),
            P("… than", "Emma", ["Amy", "Sally"], k=["emma"]))),
        Q(M("b", "Correct the mistake and rewrite: 2. Emma is taller than Amy.", "Emma is shorter than Amy.",
            [A("shorter (ya da: Amy is taller)", "shorter", "amy is taller"), A("than Amy / than Emma", "than amy", "than emma")], "duzelt"),
          ["Correct the mistake"], N_DUZELT,
          B("Emma is shorter than Amy.", "shorter", "Emma is taller than Amy.",
            "Metinde boyları bul: 165 cm mi 160 cm mi daha uzun?",
            "Amy 165 cm, Emma 160 cm → Emma daha kısa: taller yerine shorter. (MEB örnek sorusu)",
            P("Emma is", "shorter", ["taller", "older"], k=["shorter"]),
            P("… than", "Amy", ["Emma", "Sally"], k=["amy"]))),
        Q(M("c", "Correct the mistake and rewrite: 3. Amy has wavy blond hair and green eyes.", "Amy has straight blond hair and brown eyes.",
            [A("straight (wavy değil)", "straight"), A("brown eyes (green değil)", "brown")], "duzelt"),
          ["Correct the mistake"], N_DUZELT,
          B("Amy has straight blond hair and brown eyes.", "Amy has straight blond hair and green eyes.", "Amy has wavy blond hair and green eyes.",
            "Bu cümlede İKİ yanlış var: saçın şekli ve gözün rengi.",
            "Metin: “Amy is slim with straight blonde hair and brown eyes.” → wavy yerine straight, green yerine brown. (MEB örnek sorusu)",
            P("Amy has", "straight blond hair", ["wavy blond hair", "curly dark hair"], k=["straight"]),
            P("and", "brown eyes", ["green eyes", "blue eyes"], k=["brown"]))),
        Q(M("d", "Correct the mistake and rewrite: 4. Amy is more outgoing than Emma.", "Emma is more outgoing than Amy.",
            [AS("Emma önce (more outgoing olan Emma)", ["emma"], ["outgoing"]), A("than Amy", "than amy")], "duzelt"),
          ["Correct the mistake"], N_DUZELT,
          B("Emma is more outgoing than Amy.", "Emma.", "Amy is more outgoing than Emma.",
            "Metinde “more outgoing” kim için yazıyor? İsimlerin yerini değiştir.",
            "Metin: “Emma is more outgoing than her sister.” → isimler yer değiştirir: Emma is more outgoing than Amy. (MEB örnek sorusu)",
            P("Kim? →", "Emma", ["Amy", "Sally"], k=["emma"]),
            P("is more outgoing than", "Amy", ["Emma", "Helen"], k=["amy"]))),
        Q(M("e", "Correct the mistake and rewrite: 5. Emma doesn't change her mind easily.", "Amy doesn't change her mind easily.",
            [A("Amy (Emma değil)", "amy"), A("doesn't change her mind", "change")], "duzelt"),
          ["Correct the mistake"], N_DUZELT,
          B("Amy doesn't change her mind easily.", "Amy.", "Emma doesn't change her mind easily.",
            "Metnin sonunda kim inatçı (stubborn)?",
            "Metin: “Amy can sometimes be stubborn. She doesn't change her mind easily.” → Emma yerine Amy. (MEB örnek sorusu)",
            P("Kim? →", "Amy", ["Emma", "Helen"], k=["amy"]),
            P("doesn't", "change her mind easily", ["like meeting people", "study hard"], k=["change"])))],
    ikizler=[
        {"metin": ["Read the character clues. Correct the wrong sentences and write them again. (İpuçlarını oku, yanlış cümleleri düzeltip yeniden yaz.)",
                   "Melis: 165 cm (tall) · long curly brown hair · slim",
                   "Bora: 150 cm (short) · short black hair · plump"],
         "maddeler": [M("a", "Correct the mistake and rewrite: Melis is short and she has straight hair.", "Melis is tall and she has curly hair.",
                        [A("tall (short değil)", "tall"), A("curly (straight değil)", "curly")], "duzelt"),
                      M("b", "Correct the mistake and rewrite: Bora is tall and thin.", "Bora is short and plump.",
                        [A("short (tall değil)", "short"), A("plump (thin değil)", "plump")], "duzelt")]},
        {"metin": ["Read the text and correct the mistakes. Rewrite the sentences. (Metni oku, yanlışları düzelt, cümleleri yeniden yaz.)",
                   "Leo is 14 years old, and his brother Max is 11 years old. Leo is 170 cm tall and Max is 150 cm tall. Leo has curly black hair and blue eyes. "
                   "Max has straight brown hair and green eyes. Max is more outgoing than Leo; he has a lot of friends. Leo is more hardworking; he always does his homework."],
         "maddeler": [M("a", "Correct the mistake and rewrite: Max is older than Leo.", "Max is younger than Leo.",
                        [A("younger (ya da: Leo is older)", "younger", "leo is older"), A("than Leo / than Max", "than leo", "than max")], "duzelt"),
                      M("b", "Correct the mistake and rewrite: Leo has straight black hair and green eyes.", "Leo has curly black hair and blue eyes.",
                        [A("curly (straight değil)", "curly"), A("blue eyes (green değil)", "blue")], "duzelt"),
                      M("c", "Correct the mistake and rewrite: Leo is more outgoing than Max.", "Max is more outgoing than Leo.",
                        [AS("Max önce", ["max"], ["outgoing"]), A("than Leo", "than leo")], "duzelt")]}])

Y.meb(id="m6", no=6, kazanim=K3, oncelik=2,
    metin=["Answer the questions according to the text. (Metne göre soruları cevapla.)",
           "Hi! My name is Rose and I'm 15 years old. On weekdays, I get up early and eat breakfast with my family. After school, I play volleyball with my friends. "
           "I go hiking on Tuesdays and Thursdays because it helps me feel relaxed. I go swimming with my cousin on Saturdays. I usually ride my bike on Sundays. "
           "In the evenings, I spend time doing my homework and watching TV. I go to bed early to feel energetic the next day."],
    maddeler=[
        Q(M("a", "What does Rose do after school?", "She plays volleyball with her friends after school.",
            [A("plays (play)", "plays", "play"), A("volleyball", "volleyball")], "soru"),
          ["What", "after school"], N_WHAT,
          B("She plays volleyball.", "Volleyball.", "She goes hiking.",
            "Metinde “After school” kelimesini bul. Hemen sonra ne yazıyor?",
            "“After school, I play volleyball with my friends.” I → She olunca play → plays. (MEB örnek sorusu)",
            P("She", "plays volleyball", ["play volleyball", "goes hiking"], hepsi=[["plays"], ["volleyball"]]),
            P("with", "her friends", ["her cousin", "her family"], k=["friend"]))),
        Q(M("b", "How often does she go hiking?", "She goes hiking twice a week.",
            [A("twice (two times)", "twice", "two times", "2 times"), A("a week", "week")], "soru"),
          ["How often"], N_HOWOFTEN,
          B("Twice a week.", "Twice.", "In the mountains.",
            "How often = kaç kez? Metinde hiking hangi günler: kaç gün eder?",
            "“I go hiking on Tuesdays and Thursdays.” → 2 gün = twice a week. (MEB örnek sorusu)",
            P("She goes hiking", "twice a week", ["on Tuesdays", "every day"], hepsi=[["twice", "two times", "2 times"], ["week"]]))),
        Q(M("c", "What does Rose do on Sundays?", "She usually rides her bike on Sundays.",
            [A("rides (ride)", "rides", "ride"), A("bike", "bike", "bicycle")], "soru"),
          ["What", "on Sundays"], N_WHAT,
          B("She rides her bike.", "Bike.", "She goes swimming.",
            "Metinde “on Sundays” kelimesini bul. Hangi cümlede?",
            "“I usually ride my bike on Sundays.” → She (usually) rides her bike. Swimming Saturdays! (MEB örnek sorusu)",
            P("She", "rides her bike", ["ride her bike", "goes swimming"], hepsi=[["rides"], ["bike"]]))),
        Q(M("d", "Does she go to bed early?", "Yes, she does.",
            [A("Yes", "yes"), A("she does", "does")], "soru"),
          ["Does"], N_DOES,
          B("Yes, she does.", "Yes.", "Yes, she is.",
            "Soru Does ile başlıyor; cevapta da does kullan.",
            "“I go to bed early to feel energetic.” → Evet: Yes, she does. (MEB örnek sorusu; s. 31)",
            P("Cevap:", "Yes, she does", ["Yes, she is", "No, she doesn't"], hepsi=[["yes"], ["does"]])))],
    ikizler=[
        {"metin": ["Read the text and answer the questions. (Metni oku, soruları cevapla.)",
                   "Hello! I am Sue. I am a swimmer. I get up early every day. I eat healthy food. Then, I go to the swimming pool. I have training three hours every day. I want to win a gold medal at the Olympics."],
         "maddeler": [M("a", "Does Sue get up late?", "No, she doesn't. She gets up early every day.",
                        [A("No", "no"), A("she doesn't", "doesn't", "does not", "doesnt")], "soru"),
                      M("b", "How often does Sue have training?", "She has training every day.",
                        [A("every day", "every day", "everyday")], "soru"),
                      M("c", "What does Sue want to win?", "She wants to win a gold medal at the Olympics.",
                        [A("a gold medal", "gold medal", "medal"), A("at the Olympics", "olympic")], "soru")]},
        {"metin": ["Read Deniz's sports diary and answer the questions. (Deniz'in spor günlüğünü oku, soruları cevapla.)",
                   "Hi! I'm Deniz. I am a young swimmer. I get up at half past six every morning. I have eggs, cheese and milk for breakfast because I want to stay healthy. "
                   "I go to the swimming pool after school and practise for one and a half hours. I don't train on Sundays because I spend time with my family. "
                   "My dream is to win a national swimming competition one day."],
         "maddeler": [M("a", "What sport does Deniz do?", "Deniz does swimming. / Deniz is a swimmer.",
                        [A("swimming / swimmer", "swim")], "soru"),
                      M("b", "Why does Deniz eat healthy food?", "Because Deniz wants to stay healthy.",
                        [A("Because", "because"), A("stay healthy", "healthy")], "neden"),
                      M("c", "What does Deniz do on Sundays?", "Deniz spends time with the family on Sundays.",
                        [A("spends time", "spend"), A("family", "family")], "soru")]}])

Y.meb(id="m9", no=9, kazanim=K3, oncelik=3,
    metin=["Read the sentences and write the correct sports. (Cümleleri oku, doğru sporu yaz.)",
           "a) You need a ball for this sport. You must kick the ball into the goal. There are 11 players in each team.",
           "b) You need a racket and a small yellow ball. You must hit the ball over the net. You can play it with two or four players.",
           "c) You need a net and a ball. You must hit the ball with your hands or arms.",
           "d) You need a bow and some arrows. It is an individual sport. You try to hit the center of the target.",
           "e) You need a pair of sneakers and a backpack. It is a relaxing outdoor sport. You can do this sport in the mountains or forests."],
    maddeler=[Q(M("a", "Read the sentences and write the correct sports (a–e).", "a) football b) tennis c) volleyball d) archery e) hiking",
        [A("a) football", "football"), A("b) tennis", "tennis"), A("c) volleyball", "volleyball"), A("d) archery", "archery"), A("e) hiking", "hiking", "hike")], "spor"),
        ["correct sports"], N_SPOR,
        B("a football, b tennis, c volleyball, d archery, e hiking", "a football, b tennis, c volleyball", "a basketball, b tennis, c volleyball, d archery, e cycling",
          "Her cümlede ekipmanı bul: ball + goal, racket, net + hands, bow + arrows, sneakers + mountains.",
          "kick + goal + 11 players → football; racket → tennis; hands + net → volleyball; bow and arrows → archery; mountains, forests → hiking. (MEB örnek sorusu; s. 32, 34)",
          P("a) kick + goal →", "football", ["basketball", "tennis"], k=["football"]),
          P("b) racket + net →", "tennis", ["volleyball", "football"], k=["tennis"]),
          P("c) hands + net →", "volleyball", ["tennis", "basketball"], k=["volleyball"]),
          P("d) bow + arrows →", "archery", ["hiking", "cycling"], k=["archery"]),
          P("e) sneakers + mountains →", "hiking", ["swimming", "archery"], k=["hiking", "hike"])))],
    ikizler=[
        {"metin": ["Read the sentences and write the correct sports. (Cümleleri oku, doğru sporu yaz.)",
                   "a) You play it on a court. You hit a ball with a racket to throw it over the net.",
                   "b) It is a team game. Five players in each team play the game. You throw the ball into the basket.",
                   "c) It is an individual sport. You move in water using your arms and legs.",
                   "d) You need a bike and a helmet. You can ride in the park or on the road.",
                   "e) You need skis. You do this sport on snow in the mountains."],
         "maddeler": [M("a", "Write the correct sports (a–e).", "a) tennis b) basketball c) swimming d) cycling e) skiing",
                        [A("a) tennis", "tennis"), A("b) basketball", "basketball"), A("c) swimming", "swimming"), A("d) cycling", "cycling"), A("e) skiing", "skiing")], "spor")]},
        {"metin": ["Read the sports reporter's notes and answer the questions. (Spor muhabirinin notlarını oku, soruları cevapla.)",
                   "Today, I am at a basketball match. The players are playing on a court in a large sports hall. Basketball is usually an indoor sport. "
                   "The players need a basketball and comfortable sports shoes. There are also two referees, coaches and many spectators in the hall."],
         "maddeler": [M("a", "Where do people play this sport?", "They play it on a court in a sports hall.",
                        [A("on a court", "court")], "soru"),
                      M("b", "Is basketball usually an indoor or outdoor sport?", "It is usually an indoor sport.",
                        [A("indoor", "indoor")], "soru"),
                      M("c", "Write two things players need for this sport.", "They need a basketball and sports shoes.",
                        [A("a basketball", "ball"), A("sports shoes", "shoe")], "spor")]}])

Y.meb(id="m7", no=7, kazanim=K4, oncelik=3,
    metin=["Fill in the blanks according to the chart. (Grafiğe göre boşlukları doldur.)",
           "1. I ______ do exercise in the morning to stay fit. (100%)",
           "2. I ______ eat junk food. (0%)",
           "3. I ______ play basketball in the school garden. (70%)",
           "4. I ______ go to the gym on weekdays. (90%)",
           "5. I ______ go swimming with my friends at the weekend. (50%)"],
    svg=Z.piramit(),
    maddeler=[Q(M("a", "Fill in the blanks 1–5 according to the chart.", "1. always 2. never 3. often 4. usually 5. sometimes",
        [A("1. always (100%)", "always"), A("2. never (0%)", "never"), A("3. often (70%)", "often"), A("4. usually (90%)", "usually"), A("5. sometimes (50%)", "sometimes")], "siklik"),
        ["according to the chart"], N_SIKLIK,
        B("1 always, 2 never, 3 often, 4 usually, 5 sometimes", "1 always, 2 never, 3 often", "1 always, 2 never, 3 sometimes, 4 often, 5 usually",
          "Her cümlenin sonundaki yüzdeyi grafikte bul; yanındaki kelimeyi yaz.",
          "Grafik: 100% always, 90% usually, 70% often, 50% sometimes, 0% never. (MEB örnek sorusu)",
          P("1. (100%) I … do exercise →", "always", ["usually", "often"], k=["always"]),
          P("2. (0%) I … eat junk food →", "never", ["rarely", "sometimes"], k=["never"]),
          P("3. (70%) I … play basketball →", "often", ["usually", "sometimes"], k=["often"]),
          P("4. (90%) I … go to the gym →", "usually", ["always", "often"], k=["usually"]),
          P("5. (50%) I … go swimming →", "sometimes", ["usually", "never"], k=["sometimes"])))],
    ikizler=[
        {"metin": ["Look at Eren's sports habits. Fill in the blanks with always, usually, sometimes or never. (Eren'in spor alışkanlıklarına bak, boşlukları doldur.)",
                   "1. Eren ______ brushes his teeth.",
                   "2. He ______ plays basketball.",
                   "3. He ______ goes swimming.",
                   "4. He ______ goes skiing."],
         "svg": Z.tablo_svg(["EREN", "HOW OFTEN?"], [["brushes his teeth", "7 days a week"], ["plays basketball", "5 days a week"], ["goes swimming", "2 days a week"], ["goes skiing", "0 days"]], [165, 155],
                            etiket="Eren'in tablosu: dişlerini haftada 7 gün fırçalar, basketbol 5 gün, yüzme 2 gün, kayak 0 gün", ilk_kalin=False),
         "maddeler": [M("a", "Fill in the blanks 1–4 according to the table.", "1. always 2. usually 3. sometimes 4. never",
                        [A("1. always (7 days)", "always"), A("2. usually (5 days)", "usually"), A("3. sometimes (2 days)", "sometimes"), A("4. never (0 days)", "never")], "siklik")]},
        {"metin": ["Fill in the blanks according to the chart. (Grafiğe göre boşlukları doldur.)",
                   "1. I ______ eat breakfast. (100%)",
                   "2. My brother ______ plays video games. (0%)",
                   "3. We ______ go to the cinema. (50%)",
                   "4. She ______ walks to school. (90%)",
                   "5. They ______ ride their bikes in the park. (70%)"],
         "svg": Z.piramit(),
         "maddeler": [M("a", "Fill in the blanks 1–5 according to the chart.", "1. always 2. never 3. sometimes 4. usually 5. often",
                        [A("1. always", "always"), A("2. never", "never"), A("3. sometimes", "sometimes"), A("4. usually", "usually"), A("5. often", "often")], "siklik")]}])

Y.meb(id="m10", no=10, kazanim=K4, oncelik=3,
    metin=["Complete the table according to the dialogue. (Diyaloğa göre tabloyu doldur.)",
           "Jack: Hi! My name is Jack. My favourite sport is basketball. I love it very much.",
           "Sarah: Hello! I'm Sarah. My favourite sport is tennis. How often do you play basketball, Jack?",
           "Jack: I play it four times a week. My friends and I go to the basketball court and play there. You need a ball and a basket for it. What about tennis?",
           "Sarah: I play tennis twice a week. I usually play it at the tennis court.",
           "Jack: That sounds cool! What do you need for tennis?",
           "Sarah: We need a ball and a racket. You must hit the ball over the net."],
    maddeler=[
        Q(M("a", "Complete the table for JACK: Sport, Equipment, Place, Frequency.", "Sport: basketball · Equipment: ball and basket · Place: basketball court · Frequency: four times a week",
            [A("Sport: basketball", "basketball"), A("Equipment: ball and basket", "ball and basket", "ball and a basket", "basket and ball", "ball, basket", "ball, a basket"),
             A("Place: basketball court", "court"), A("Frequency: four times a week", "four times", "4 times")], "tablo2"),
          ["Sport", "Equipment", "Place", "Frequency"], N_TABLO2,
          B("basketball · ball and basket · basketball court · four times a week", "basketball · four times a week", "basketball court · basketball · four times a week · ball and basket",
            "Jack'in cümlelerini bul. How often sorusunun cevabı Frequency sütununa.",
            "Jack: basketball; “a ball and a basket”; “the basketball court”; “four times a week”. (MEB örnek sorusu)",
            P("Sport:", "basketball", ["tennis", "football"], k=["basketball"]),
            P("Equipment:", "ball and basket", ["racket and ball", "net and bow"], k=["ball and basket", "ball and a basket", "basket and ball", "ball, basket"]),
            P("Place:", "basketball court", ["tennis court", "swimming pool"], k=["basketball court"]),
            P("Frequency:", "four times a week", ["twice a week", "every day"], k=["four times", "4 times"]))),
        Q(M("b", "Complete the table for SARAH: Sport, Equipment, Place, Frequency.", "Sport: tennis · Equipment: racket and ball · Place: tennis court · Frequency: twice a week",
            [A("Sport: tennis", "tennis"), A("Equipment: racket and ball", "racket"), A("Place: tennis court", "court"), A("Frequency: twice a week", "twice", "two times", "2 times")], "tablo2"),
          ["Sport", "Equipment", "Place", "Frequency"], N_TABLO2,
          B("tennis · racket and ball · tennis court · twice a week", "tennis · twice a week", "tennis court · tennis · twice a week · racket and ball",
            "Sarah'nın cümlelerini bul. Equipment = ne gerekiyor (need)?",
            "Sarah: tennis; “a ball and a racket”; “the tennis court”; “twice a week”. (MEB örnek sorusu)",
            P("Sport:", "tennis", ["basketball", "volleyball"], k=["tennis"]),
            P("Equipment:", "racket and ball", ["ball and basket", "bow and arrows"], k=["racket"]),
            P("Place:", "tennis court", ["basketball court", "gym"], k=["tennis court"]),
            P("Frequency:", "twice a week", ["four times a week", "every day"], k=["twice", "two times", "2 times"])))],
    ikizler=[
        {"metin": ["Read the sports card and complete the table. (Spor kartını oku, tabloyu doldur.)",
                   "Meet Leo. Leo enjoys outdoor sports. His favourite sport is cycling. He usually rides his bike in the park at weekends. "
                   "He always wears a helmet to protect his head and uses gloves to keep his hands safe and comfortable."],
         "maddeler": [M("a", "Complete the table for LEO: Sport, Equipment, Place, Frequency.", "Sport: cycling · Equipment: bike, helmet, gloves · Place: park · Frequency: at weekends",
                        [A("Sport: cycling", "cycling"), A("Equipment: helmet, gloves", "helmet", "glove"), A("Place: park", "park"), A("Frequency: at weekends", "weekend")], "tablo2")]},
        {"metin": ["Complete the table according to the dialogue. (Diyaloğa göre tabloyu doldur.)",
                   "Mert: My favourite sport is swimming. I go swimming three times a week. I swim at the swimming pool near my house. I need a swimsuit and a swimming cap.",
                   "Elif: I love volleyball. I play it once a week in the school gym. We need a ball and a net.",
                   "Mert: That's great!"],
         "maddeler": [M("a", "Complete the table for MERT: Sport, Equipment, Place, Frequency.", "Sport: swimming · Equipment: swimsuit and swimming cap · Place: swimming pool · Frequency: three times a week",
                        [A("Sport: swimming", "swim"), A("Equipment: swimsuit, cap", "swimsuit", "cap"), A("Place: swimming pool", "pool"), A("Frequency: three times a week", "three times", "3 times")], "tablo2"),
                      M("b", "Complete the table for ELIF: Sport, Equipment, Place, Frequency.", "Sport: volleyball · Equipment: ball and net · Place: school gym · Frequency: once a week",
                        [A("Sport: volleyball", "volleyball"), A("Equipment: ball and net", "net"), A("Place: school gym", "gym"), A("Frequency: once a week", "once")], "tablo2")]}])

Y.meb(id="m8", no=8, kazanim=K4, oncelik=2,
    metin=["Answer the questions according to the text. (Metne göre soruları cevapla.)",
           "Scott is a 19-year-old football player. He always wakes up at seven in the morning. After breakfast, he usually rests. He trains every day because he wants to be a successful football player. "
           "In the evenings, he spends time with his family. They usually watch movies together. He goes to bed early to stay healthy and energetic."],
    maddeler=[
        Q(M("a", "What time does Scott get up?", "He always gets up at seven in the morning.",
            [A("seven", "seven", "7"), A("in the morning", "morning")], "neden"),
          ["What time"], N_WHATTIME,
          B("At seven in the morning.", "Seven.", "After breakfast.",
            "What time = saat kaçta? Metinde bir saat ara.",
            "“He always wakes up at seven in the morning.” wake up = get up. (MEB örnek sorusu)",
            P("He gets up at", "seven", ["eight", "night"], k=["seven", "7"]),
            P("in the", "morning", ["evening", "afternoon"], k=["morning"]))),
        Q(M("b", "What does he do in the evenings?", "He spends time with his family in the evenings. They usually watch movies together.",
            [A("spends time / watches movies", "spend", "movie", "film"), A("with his family", "family", "together")], "soru"),
          ["What", "in the evenings"], N_WHAT,
          B("He spends time with his family.", "Family.", "He rests.",
            "Metinde “In the evenings” kelimesini bul.",
            "“In the evenings, he spends time with his family.” (MEB örnek sorusu)",
            P("He", "spends time", ["spend time", "trains"], k=["spends"]),
            P("with his", "family", ["friends", "coach"], k=["family"]))),
        Q(M("c", "Why does Scott train hard?", "Because he wants to be a successful football player.",
            [A("Because", "because"), A("successful football player", "successful")], "neden"),
          ["Why"], N_WHY,
          B("Because he wants to be a successful football player.", "Successful.", "Because he gets up at seven.",
            "Why = neden? Metinde “because” kelimesini bul.",
            "“He trains every day because he wants to be a successful football player.” Cevap Because ile başlar. (MEB örnek sorusu)",
            P("İlk kelime:", "Because", ["So", "And"], k=["because"]),
            P("he wants to be a", "successful football player", ["tired football player", "healthy family"], k=["successful"])))],
    ikizler=[
        {"metin": ["Read the text and answer the questions. (Metni oku, soruları cevapla.)",
                   "Hello! My name is Daniel. I am a basketball player. I usually wake up at seven o'clock on weekdays. I have eggs and milk for breakfast because I want to stay healthy. "
                   "After school, I go to the sports centre. I practise basketball for two hours four times a week. My dream is to become a successful basketball player in the future."],
         "maddeler": [M("a", "What time does Daniel usually wake up?", "He usually wakes up at seven o'clock.",
                        [A("seven", "seven", "7"), A("o'clock", "clock")], "neden"),
                      M("b", "How often does Daniel practise basketball?", "He practises basketball four times a week.",
                        [A("four times", "four times", "4 times"), A("a week", "week")], "soru"),
                      M("c", "Why does Daniel have eggs and milk for breakfast?", "Because he wants to stay healthy.",
                        [A("Because", "because"), A("stay healthy", "healthy")], "neden")]},
        {"metin": ["Read Laura's interview and answer the questions. (Laura'nın röportajını oku, soruları cevapla.) (Kitap s. 41)",
                   "I get up early every day. I have a big breakfast, and go to the gym to exercise. After lunch, I have a rest. Then, I meet my coach at the swimming pool for the second part of my exercise. "
                   "I train four hours in a day and six days in a week. I always eat healthy food, never drink energy drinks."],
         "maddeler": [M("a", "When does Laura go to the gym?", "She goes to the gym after breakfast.",
                        [A("after breakfast", "breakfast")], "soru"),
                      M("b", "What does Laura do after lunch?", "She has a rest.",
                        [A("has a rest", "rest")], "soru"),
                      M("c", "How long does Laura train in a day?", "She trains four hours in a day.",
                        [A("four hours", "four hours", "4 hours")], "neden")]}])

# =====================================================================
# BENZER SORULAR (Konu Tekrarı): kısa cevap, tetik, kalıp notu, parçalar (sec YOK → doğrudan sınavdaki gibi yazma)
# =====================================================================
IKIZ = {
 ("m1i1", "a"): IK("patient, helpful, punctual, generous, hardworking", ["correct personality adjective"], N_SIFAT,
    P("1. waits calmly →", "patient", ["selfish", "punctual"], k=["patient"]),
    P("2. helps classmates →", "helpful", ["selfish", "patient"], k=["helpful"]),
    P("3. before the bell →", "punctual", ["generous", "patient"], k=["punctual"]),
    P("4. gives presents →", "generous", ["selfish", "punctual"], k=["generous"]),
    P("5. studies regularly →", "hardworking", ["selfish", "helpful"], k=["hardworking", "hard-working"])),
 ("m1i2", "a"): IK("Ece, Kerem, Mert", ["Who is generous", "Who is punctual", "Who is outgoing"], N_ISIM,
    P("Generous →", "Ece", ["Kerem", "Mert"], k=["ece"]),
    P("Punctual →", "Kerem", ["Ece", "Mert"], k=["kerem"]),
    P("Outgoing →", "Mert", ["Ece", "Kerem"], k=["mert"])),
 ("m2i1", "a"): IK("1 Bora, 2 Mina, 3 Lara, 4 Melis", ["correct names"], N_ISIM,
    P("Resim 1 →", "Bora", ["Lara", "Melis"], k=["bora"]),
    P("Resim 2 →", "Mina", ["Melis", "Lara"], k=["mina"]),
    P("Resim 3 →", "Lara", ["Mina", "Bora"], k=["lara"]),
    P("Resim 4 →", "Melis", ["Mina", "Bora"], k=["melis"])),
 ("m2i2", "a"): IK("Ali, Can, Ece, Defne", ["Who wears glasses", "Who is plump", "Who has ginger hair", "Who has blue eyes"], N_ISIM,
    P("glasses →", "Ali", ["Can", "Ece"], k=["ali"]),
    P("plump →", "Can", ["Ali", "Defne"], k=["can"]),
    P("ginger hair →", "Ece", ["Defne", "Ali"], k=["ece"]),
    P("blue eyes →", "Defne", ["Ece", "Can"], k=["defne"])),
 ("m5i1", "a"): IK("Appearance: curly hair, brown eyes · Personality: cheerful, talkative", ["APPEARANCE", "PERSONALITY"], N_TABLO1,
    P("Appearance:", "short curly hair, brown eyes", ["straight black hair, green eyes", "cheerful, talkative"], hepsi=[["curly"], ["brown"]]),
    P("Personality:", "cheerful, talkative", ["patient, helpful", "short curly hair"], hepsi=[["cheerful"], ["talkative"]])),
 ("m5i1", "b"): IK("Appearance: straight black hair, green eyes · Personality: patient, helpful", ["APPEARANCE", "PERSONALITY"], N_TABLO1,
    P("Appearance:", "straight black hair, green eyes", ["short curly hair, brown eyes", "patient, helpful"], hepsi=[["straight"], ["green"]]),
    P("Personality:", "quiet, patient, helpful", ["cheerful, talkative", "green eyes"], hepsi=[["patient"], ["helpful"]])),
 ("m5i2", "a"): IK("Appearance: long wavy blonde hair, brown eyes · Personality: hardworking, outgoing", ["APPEARANCE", "PERSONALITY"], N_TABLO1,
    P("Appearance:", "long wavy blonde hair, brown eyes", ["straight dark hair, blue eyes", "hardworking, outgoing"], hepsi=[["wavy"], ["blond"]]),
    P("Personality:", "hardworking, outgoing", ["shy, quiet", "long wavy hair"], hepsi=[["hardworking", "hard-working"], ["outgoing"]])),
 ("m5i2", "b"): IK("Appearance: short, straight dark hair, blue eyes · Personality: shy, quiet, stubborn", ["APPEARANCE", "PERSONALITY"], N_TABLO1,
    P("Appearance:", "short, straight dark hair, blue eyes", ["long wavy blonde hair", "shy, stubborn"], hepsi=[["straight"], ["blue"]]),
    P("Personality:", "shy, quiet, stubborn", ["hardworking, outgoing", "blue eyes"], hepsi=[["shy", "quiet"], ["stubborn"]])),
 ("m3i1", "a"): IK("younger, taller, more hardworking, more talkative, more punctual", ["Look at the table"], N_ER,
    P("1. Duru (young) →", "younger", ["older", "more young"], k=["younger"]),
    P("2. Duru (tall) →", "taller", ["shorter", "more tall"], k=["taller"]),
    P("3. Duru (hardworking) →", "more hardworking", ["lazier", "less hardworking"], k=["more hardworking", "more hard-working"]),
    P("4. Ece (talkative) →", "more talkative", ["quieter", "less talkative"], k=["more talkative"]),
    P("5. Duru (punctual) →", "more punctual", ["later", "less punctual"], k=["more punctual"])),
 ("m3i2", "a"): IK("older, younger, taller, heavier, more punctual", ["Look at the table"], N_ER,
    P("1. Can (age) →", "older", ["younger", "taller"], k=["older"]),
    P("2. Mert (age) →", "younger", ["older", "heavier"], k=["younger"]),
    P("3. Mert (height) →", "taller", ["shorter", "older"], k=["taller"]),
    P("4. Can (weight) →", "heavier", ["lighter", "thinner"], k=["heavier", "fatter"]),
    P("5. Mert (personality) →", "more punctual", ["very punctual", "less punctual"], k=["more punctual"])),
 ("m4i1", "a"): IK("Melis is tall and she has curly hair.", ["Correct the mistake"], N_DUZELT,
    P("Melis is", "tall", ["short", "plump"], k=["tall"]),
    P("and she has", "curly hair", ["straight hair", "short hair"], k=["curly"])),
 ("m4i1", "b"): IK("Bora is short and plump.", ["Correct the mistake"], N_DUZELT,
    P("Bora is", "short", ["tall", "slim"], k=["short"]),
    P("and", "plump", ["thin", "tall"], k=["plump"])),
 ("m4i2", "a"): IK("Max is younger than Leo.", ["Correct the mistake"], N_DUZELT,
    P("Max is", "younger", ["older", "taller"], k=["younger"]),
    P("… than", "Leo", ["Max", "Amy"], k=["leo"])),
 ("m4i2", "b"): IK("Leo has curly black hair and blue eyes.", ["Correct the mistake"], N_DUZELT,
    P("Leo has", "curly black hair", ["straight black hair", "straight brown hair"], k=["curly"]),
    P("and", "blue eyes", ["green eyes", "brown eyes"], k=["blue"])),
 ("m4i2", "c"): IK("Max is more outgoing than Leo.", ["Correct the mistake"], N_DUZELT,
    P("Kim? →", "Max", ["Leo", "Emma"], k=["max"]),
    P("is more outgoing than", "Leo", ["Max", "Amy"], k=["leo"])),
 ("m6i1", "a"): IK("No, she doesn't.", ["Does"], N_DOES,
    P("Cevap:", "No, she doesn't", ["Yes, she does", "No, she isn't"], hepsi=[["no"], ["doesn't", "does not", "doesnt"]])),
 ("m6i1", "b"): IK("Every day.", ["How often"], N_HOWOFTEN,
    P("She has training", "every day", ["three hours", "at the pool"], k=["every day", "everyday"])),
 ("m6i1", "c"): IK("A gold medal at the Olympics.", ["want to win"], N_WANT,
    P("She wants to win a", "gold medal", ["swimming pool", "healthy food"], k=["gold medal", "medal"]),
    P("at the", "Olympics", ["pool", "school"], k=["olympic"])),
 ("m6i2", "a"): IK("Deniz does swimming.", ["What sport"], N_WHAT,
    P("Deniz does", "swimming", ["running", "cycling"], k=["swim"])),
 ("m6i2", "b"): IK("Because Deniz wants to stay healthy.", ["Why"], N_WHY,
    P("İlk kelime:", "Because", ["So", "And"], k=["because"]),
    P("Deniz wants to", "stay healthy", ["win a medal", "sleep late"], k=["healthy"])),
 ("m6i2", "c"): IK("Deniz spends time with the family.", ["What", "on Sundays"], N_WHAT,
    P("Deniz", "spends time", ["trains", "swims"], k=["spend"]),
    P("with", "the family", ["the coach", "friends"], k=["family"])),
 ("m9i1", "a"): IK("a tennis, b basketball, c swimming, d cycling, e skiing", ["correct sports"], N_SPOR,
    P("a) racket + net →", "tennis", ["football", "swimming"], k=["tennis"]),
    P("b) five players + basket →", "basketball", ["volleyball", "tennis"], k=["basketball"]),
    P("c) arms and legs in water →", "swimming", ["skiing", "cycling"], k=["swimming"]),
    P("d) bike + helmet →", "cycling", ["swimming", "hiking"], k=["cycling"]),
    P("e) skis + snow →", "skiing", ["surfing", "jogging"], k=["skiing"])),
 ("m9i2", "a"): IK("On a court.", ["Where"], N_WHERE,
    P("They play it on a", "court", ["pool", "mountain"], k=["court"])),
 ("m9i2", "b"): IK("It is an indoor sport.", ["indoor or outdoor"], N_INOUT,
    P("It is an", "indoor sport", ["outdoor sport", "team medal"], k=["indoor"])),
 ("m9i2", "c"): IK("A basketball and sports shoes.", ["need"], N_NEED,
    P("1.", "a basketball", ["a racket", "a helmet"], k=["ball"]),
    P("2.", "sports shoes", ["skis", "gloves"], k=["shoe"])),
 ("m7i1", "a"): IK("1 always, 2 usually, 3 sometimes, 4 never", ["according to the table"], N_SIKLIK,
    P("1. 7 days a week →", "always", ["usually", "sometimes"], k=["always"]),
    P("2. 5 days a week →", "usually", ["always", "never"], k=["usually"]),
    P("3. 2 days a week →", "sometimes", ["usually", "always"], k=["sometimes"]),
    P("4. 0 days →", "never", ["sometimes", "usually"], k=["never"])),
 ("m7i2", "a"): IK("1 always, 2 never, 3 sometimes, 4 usually, 5 often", ["according to the chart"], N_SIKLIK,
    P("1. (100%) I … eat breakfast →", "always", ["often", "usually"], k=["always"]),
    P("2. (0%) My brother … plays →", "never", ["rarely", "sometimes"], k=["never"]),
    P("3. (50%) We … go to the cinema →", "sometimes", ["usually", "often"], k=["sometimes"]),
    P("4. (90%) She … walks to school →", "usually", ["always", "sometimes"], k=["usually"]),
    P("5. (70%) They … ride their bikes →", "often", ["usually", "never"], k=["often"])),
 ("m10i1", "a"): IK("cycling · bike, helmet, gloves · park · at weekends", ["Sport", "Equipment", "Place", "Frequency"], N_TABLO2,
    P("Sport:", "cycling", ["swimming", "tennis"], k=["cycling"]),
    P("Equipment:", "bike, helmet, gloves", ["racket and ball", "skis"], k=["helmet", "glove"]),
    P("Place:", "park", ["court", "pool"], k=["park"]),
    P("Frequency:", "at weekends", ["every day", "twice a week"], k=["weekend"])),
 ("m10i2", "a"): IK("swimming · swimsuit and cap · swimming pool · three times a week", ["Sport", "Equipment", "Place", "Frequency"], N_TABLO2,
    P("Sport:", "swimming", ["volleyball", "tennis"], k=["swimming"]),
    P("Equipment:", "a swimsuit and a swimming cap", ["a ball and a net", "a racket"], k=["swimsuit", "cap"]),
    P("Place:", "swimming pool", ["school gym", "park"], k=["pool"]),
    P("Frequency:", "three times a week", ["once a week", "every day"], k=["three times", "3 times"])),
 ("m10i2", "b"): IK("volleyball · ball and net · school gym · once a week", ["Sport", "Equipment", "Place", "Frequency"], N_TABLO2,
    P("Sport:", "volleyball", ["swimming", "basketball"], k=["volleyball"]),
    P("Equipment:", "a ball and a net", ["a swimsuit", "a racket"], k=["net"]),
    P("Place:", "school gym", ["swimming pool", "court"], k=["gym"]),
    P("Frequency:", "once a week", ["three times a week", "twice a week"], k=["once"])),
 ("m8i1", "a"): IK("At seven o'clock.", ["What time"], N_WHATTIME,
    P("He wakes up at", "seven o'clock", ["half past six", "after school"], k=["seven", "7"])),
 ("m8i1", "b"): IK("Four times a week.", ["How often"], N_HOWOFTEN,
    P("He practises", "four times a week", ["for two hours", "after school"], hepsi=[["four", "4"], ["week"]])),
 ("m8i1", "c"): IK("Because he wants to stay healthy.", ["Why"], N_WHY,
    P("İlk kelime:", "Because", ["So", "And"], k=["because"]),
    P("he wants to", "stay healthy", ["be late", "play games"], k=["healthy"])),
 ("m8i2", "a"): IK("After breakfast.", ["When"], N_WHEN,
    P("She goes to the gym", "after breakfast", ["after lunch", "in the evening"], k=["breakfast"])),
 ("m8i2", "b"): IK("She has a rest.", ["What", "after lunch"], N_WHAT,
    P("She", "has a rest", ["goes to the gym", "has breakfast"], k=["rest"])),
 ("m8i2", "c"): IK("Four hours.", ["How long"], N_HOWLONG,
    P("She trains", "four hours", ["six days", "every day"], k=["four hours", "4 hours"])),
}
for q in Y.d["mebSorular"]:
    for i, z in enumerate(q.get("ikizler", [])):
        zid = z.get("id") or f"{q['id']}i{i + 1}"
        for m in z["maddeler"]:
            b = IKIZ.get((zid, m["harf"]))
            if b: m.update(b)
            else: raise SystemExit(f"ikiz verisi eksik: {zid} {m['harf']}")

# =====================================================================
# POLLY'NİN CEVABINI DÜZELT: 8 eksik (yarım cevap) + 4 yanılgı (yalnız Hatırla'daki sık hatalardan)
# =====================================================================
def KH(kazanim, tur, soru, kuark, dogruSik, yanlis1, yanlis2, ipucu, aciklama, once, ornek, sonra, k, havuz):
    Y.kuark(kazanim=kazanim, tur=tur, soru=soru, kuark=kuark, secenekler=[dogruSik, yanlis1, yanlis2], dogru=0, ipucu=ipucu, aciklama=aciklama,
            dogruCevap=f"{once} {ornek} {sonra}".replace(" .", ".").strip(), tamamla={"once": once, "ornek": ornek, "sonra": sonra, "k": k, "havuz": havuz})

TAM, DOGRU_ = "Tam, eksik yok.", "Doğru, hata yok."
KH(K1, "eksik", "“Brian is short and he has blond hair.” Complete the table for BRIAN: APPEARANCE.", "short",
   "Eksik: saçı da yazılmalı (blond hair).", "Yanlış: tall yazılmalı.", TAM,
   "Cümlede Brian'ın görünüşüyle ilgili kaç bilgi var?", "Görünüş = boy + saç (+ göz). Cümlede iki bilgi var: short ve blond hair. (MEB örnek sorusu)",
   "Appearance: short,", "blond hair", "", ["blond"], ["funny", "outgoing"])
KH(K1, "eksik", "“Sam is very serious and hardworking.” Complete the table for SAM: PERSONALITY.", "serious",
   "Eksik: hardworking de yazılmalı.", "Yanlış: tall yazılmalı.", TAM,
   "Cümlede kaç kişilik sıfatı var?", "PERSONALITY sütununa cümledeki bütün sıfatlar yazılır: serious ve hardworking. (MEB örnek sorusu)",
   "Personality: serious,", "hardworking", "", ["hardworking", "hard-working"], ["tall", "slim"])
KH(K2, "eksik", "Text: “Amy is slim with straight blonde hair and brown eyes.” Correct the mistake: Amy has wavy blond hair and green eyes.", "Amy has straight blond hair and green eyes.",
   "Eksik: göz rengi de düzeltilmeli (brown eyes).", "Yanlış: saç rengi de değişmeli.", TAM,
   "Bu cümlede kaç yanlış vardı?", "İki yanlış var: wavy → straight ve green → brown. İkisi de düzelmeli. (MEB örnek sorusu)",
   "Amy has straight blond hair and", "brown eyes", ".", ["brown"], ["green eyes", "blue eyes"])
KH(K2, "eksik", "Sally: generous ★★★★★ · Helen: generous ★★. Sally is ______ than Helen.", "Sally is generous than Helen.",
   "Eksik: uzun sıfattan önce more gelmeli.", "Yanlış: generous yerine selfish yazılmalı.", TAM,
   "generous uzun bir sıfat mı?", "Uzun sıfatlarla karşılaştırma: more + sıfat + than → more generous. (s. 21)",
   "Sally is", "more generous", "than Helen.", ["more generous"], ["very generous", "less generous"])
KH(K3, "eksik", "Text: “I go hiking on Tuesdays and Thursdays.” How often does Rose go hiking?", "Twice.",
   "Eksik: “a week” eklenmeli.", "Yanlış: on Sundays yazılmalı.", TAM,
   "Twice … neyin içinde iki kez?", "Salı ve perşembe = haftada iki kez: twice a week. (MEB örnek sorusu)",
   "She goes hiking twice", "a week", ".", ["week"], ["a day", "a year"])
KH(K3, "eksik", "Text: “I go to bed early.” Does Rose go to bed early?", "Yes.",
   "Eksik: kısa cevap tamamlanmalı: Yes, she does.", "Yanlış: No olmalı.", TAM,
   "Does ile sorulan soruya tam kısa cevap nasıl verilir?", "Does …? sorusunun tam cevabı: Yes, she does. / No, she doesn't. (s. 31)",
   "Yes,", "she does", ".", ["does"], ["she is", "I am"])
KH(K4, "eksik", "Text: “He trains every day because he wants to be a successful football player.” Why does Scott train hard?", "He wants to be a successful football player.",
   "Eksik: cevap Because ile başlamalı.", "Yanlış: He is tired yazılmalı.", TAM,
   "Why sorusunun cevabı hangi kelimeyle başlar?", "Why → Because … Metindeki because'tan sonraki kısım cevaptır. (MEB örnek sorusu)",
   "", "Because", "he wants to be a successful football player.", ["because"], ["So", "And"])
KH(K4, "eksik", "Sarah: “We need a ball and a racket.” Complete the table for SARAH: Equipment.", "racket",
   "Eksik: top da yazılmalı (ball).", "Yanlış: basket yazılmalı.", TAM,
   "Sarah kaç şey gerektiğini söylüyor?", "Equipment = gerekenler: a ball and a racket. İkisi de yazılır. (MEB örnek sorusu)",
   "Equipment: racket and", "ball", "", ["ball"], ["net", "basket"])
KH(K2, "yanilgi", "Write the comparative form: generous", "generouser",
   "Yanlış: uzun sıfat -er almaz; more generous olmalı.", "Yanlış: the generous olmalı.", DOGRU_,
   "generous kısa mı uzun mu?", "Uzun sıfatlar -er almaz: more generous, more outgoing, more punctual. (s. 21)",
   "", "more generous", "", ["more generous"], ["very generous", "generous more"])
KH(K3, "yanilgi", "Text: “After school, I play volleyball with my friends.” What does Rose do after school?", "She play volleyball.",
   "Yanlış: she ile fiil -s alır: She plays volleyball.", "Yanlış: I play olmalı.", DOGRU_,
   "she / he ile fiilin sonuna ne gelir?", "I play → she plays. She / he ile fiil -s alır. (s. 30)",
   "She", "plays", "volleyball with her friends.", ["plays"], ["play", "playing"])
KH(K4, "yanilgi", "I ______ go swimming at the weekend. (50%)", "I usually go swimming at the weekend.",
   "Yanlış: %50 sometimes'tır; usually %90.", "Yanlış: never olmalı.", DOGRU_,
   "Grafikte %50 hangi kelime?", "MEB grafiği: usually %90, often %70, sometimes %50. (MEB örnek sorusu)",
   "I", "sometimes", "go swimming at the weekend.", ["sometimes"], ["usually", "often"])
KH(K1, "yanilgi", "My brother doesn't like sharing his things. He is ______.", "He is generous.",
   "Yanlış: paylaşmayan kişi selfish (bencil); generous cömerttir.", "Yanlış: punctual olmalı.", DOGRU_,
   "Paylaşmayı sevmeyen kişi cömert mi, bencil mi?", "selfish: yalnız kendini düşünen (Caring only about yourself). generous: paylaşan. (s. 10)",
   "He is", "selfish", ".", ["selfish"], ["generous", "honest"])

# =====================================================================
# PROVA YAZILILARI (2 deneme; Senaryo 1 dağılımı: her konudan 1 soru, 25'er puan; puanlar tahmini). Bağlamlar MEB ve benzerlerinden farklı.
# =====================================================================
Y.prova(id="p1", ad="Prova 1", sorular=[
    {"kazanim": K1, "puan": 25, "benzer": "m1", "metin": ["Complete the sentences with the correct words.",
        "1. Ali always shares his lunch with his friends. He is ______.", "2. Deniz is never late for lessons. She is ______.",
        "3. Burak always tells the truth. He is ______.", "4. Ayşe never changes her mind. She is ______.", "5. Can likes meeting new people. He has a lot of friends. He is ______."],
     "maddeler": [M("a", "Complete the sentences 1–5 with the correct words.", "1. generous 2. punctual 3. honest 4. stubborn 5. outgoing",
                    [A("1. generous", "generous"), A("2. punctual", "punctual"), A("3. honest", "honest"), A("4. stubborn", "stubborn"), A("5. outgoing", "outgoing")], "sifat", puan=25)]},
    {"kazanim": K2, "puan": 25, "benzer": "m3", "metin": ["Look at the table and complete the sentences.",
        "1. Veli is ______ than Ali. (age)", "2. Ali is ______ than Veli. (age)", "3. Ali is ______ than Veli. (height)", "4. Veli is ______ than Ali. (weight)", "5. Ali is ______ than Veli. (personality)"],
     "svg": Z.tablo_svg(["", "ALI", "VELI"], [["AGE", "14", "12"], ["HEIGHT", "1.60 m", "1.48 m"], ["WEIGHT", "52 kg", "40 kg"], ["PERSONALITY", "hardworking ****", "hardworking *"]], [110, 115, 115],
                        etiket="Ali ve Veli tablosu: yaş 14 ve 12, boy 1.60 ve 1.48 m, kilo 52 ve 40 kg, çalışkanlık 4 ve 1 yıldız"),
     "maddeler": [M("a", "Look at the table and complete the sentences 1–5.", "1. younger 2. older 3. taller 4. lighter 5. more hardworking",
                    [A("1. younger", "younger"), A("2. older", "older"), A("3. taller", "taller"), A("4. lighter / thinner", "lighter", "thinner", "slimmer"), A("5. more hardworking", "more hardworking", "more hard-working")], "er", puan=25)]},
    {"kazanim": K3, "puan": 25, "benzer": "m9", "metin": ["Read the sentences and write the correct sports.",
        "a) You need a ball and a basket. You must throw the ball into the basket. There are five players in each team.",
        "b) You need a bike and a helmet. You can do it in the park or on the road.",
        "c) You need a racket and a small ball. You play it on a court with two or four players.",
        "d) You do it in a pool or in the sea. Breaststroke and freestyle are two styles of it.",
        "e) You need a board. You do this sport on the waves in the sea."],
     "maddeler": [M("a", "Write the correct sports (a–e).", "a) basketball b) cycling c) tennis d) swimming e) surfing",
                    [A("a) basketball", "basketball"), A("b) cycling", "cycling"), A("c) tennis", "tennis"), A("d) swimming", "swimming"), A("e) surfing", "surfing")], "spor", puan=25)]},
    {"kazanim": K4, "puan": 25, "benzer": "m7", "metin": ["Fill in the blanks according to the chart.",
        "1. I ______ brush my teeth before bed. (100%)", "2. My sister ______ eats fast food. (0%)", "3. We ______ play football after school. (70%)",
        "4. My dad ______ reads a newspaper in the morning. (90%)", "5. I ______ watch TV at night. (50%)"],
     "svg": Z.piramit(),
     "maddeler": [M("a", "Fill in the blanks 1–5 according to the chart.", "1. always 2. never 3. often 4. usually 5. sometimes",
                    [A("1. always", "always"), A("2. never", "never"), A("3. often", "often"), A("4. usually", "usually"), A("5. sometimes", "sometimes")], "siklik", puan=25)]}])

Y.prova(id="p2", ad="Prova 2", sorular=[
    {"kazanim": K1, "puan": 25, "benzer": "m5", "metin": ["Complete the table according to the dialogue.",
        "Ece: Do you know my cousins, Arda and Selin?", "Mert: No, I don't. What are they like?",
        "Ece: Arda is tall and thin. He has short black hair and green eyes. He is very honest and helpful.", "Mert: And Selin?",
        "Ece: Selin is short and she has long curly ginger hair. She is funny and outgoing. She loves parties.", "Mert: So, Selin is more social than Arda."],
     "maddeler": [M("a", "Complete the table for ARDA: APPEARANCE and PERSONALITY.", "Appearance: tall, thin, short black hair, green eyes. Personality: honest, helpful.",
                    [A("tall", "tall"), A("thin", "thin"), A("green eyes / black hair", "green", "black"), A("honest", "honest"), A("helpful", "helpful")], "tablo1", puan=12),
                  M("b", "Complete the table for SELIN: APPEARANCE and PERSONALITY.", "Appearance: short, long curly ginger hair. Personality: funny, outgoing.",
                    [A("short", "short"), A("curly", "curly"), A("ginger hair", "ginger"), A("funny", "funny"), A("outgoing", "outgoing", "social")], "tablo1", puan=13)]},
    {"kazanim": K2, "puan": 25, "benzer": "m4", "metin": ["Read the text and correct the mistakes. Rewrite the sentences.",
        "Kerem is 13 years old, and his sister Zeynep is 10 years old. Kerem is 160 cm tall and Zeynep is 140 cm tall. Kerem has short straight black hair and brown eyes. "
        "Zeynep has long wavy brown hair and blue eyes. Zeynep is more outgoing than Kerem; she has a lot of friends. Kerem is more punctual; he is never late."],
     "maddeler": [M("a", "Correct the mistake and rewrite: Zeynep is older than Kerem.", "Zeynep is younger than Kerem.",
                    [A("younger (ya da: Kerem is older)", "younger", "kerem is older"), A("than Kerem / than Zeynep", "than kerem", "than zeynep")], "duzelt", puan=6),
                  M("b", "Correct the mistake and rewrite: Kerem is shorter than Zeynep.", "Kerem is taller than Zeynep.",
                    [A("taller (ya da: Zeynep is shorter)", "taller", "zeynep is shorter"), A("than Zeynep / than Kerem", "than zeynep", "than kerem")], "duzelt", puan=6),
                  M("c", "Correct the mistake and rewrite: Zeynep has short wavy hair and blue eyes.", "Zeynep has long wavy hair and blue eyes.",
                    [A("long (short değil)", "long"), A("wavy hair and blue eyes", "blue")], "duzelt", puan=6),
                  M("d", "Correct the mistake and rewrite: Kerem is more outgoing than Zeynep.", "Zeynep is more outgoing than Kerem.",
                    [AS("Zeynep önce", ["zeynep"], ["outgoing"]), A("than Kerem", "than kerem")], "duzelt", puan=7)]},
    {"kazanim": K3, "puan": 25, "benzer": "m6", "metin": ["Answer the questions according to the text.",
        "Hi! I'm Emre and I'm 13 years old. I get up at seven every day. After school, I play basketball with my classmates. I go swimming on Mondays and Wednesdays. "
        "On Saturdays, I usually go cycling with my dad. In the evenings, I do my homework. I never eat junk food because I want to be healthy."],
     "maddeler": [M("a", "What does Emre do after school?", "He plays basketball with his classmates.",
                    [A("plays (play)", "plays", "play"), A("basketball", "basketball")], "soru", puan=6),
                  M("b", "How often does he go swimming?", "He goes swimming twice a week.",
                    [A("twice (two times)", "twice", "two times", "2 times"), A("a week", "week")], "soru", puan=6),
                  M("c", "What does Emre do on Saturdays?", "He usually goes cycling with his dad.",
                    [A("goes cycling", "cycling"), A("with his dad", "dad")], "soru", puan=6),
                  M("d", "Does he eat junk food?", "No, he doesn't.",
                    [A("No", "no"), A("he doesn't", "doesn't", "does not", "doesnt")], "soru", puan=7)]},
    {"kazanim": K4, "puan": 25, "benzer": "m10", "metin": ["Complete the table according to the dialogue.",
        "Ayşe: My favourite sport is football. I play it twice a week in the school garden. We need a ball and sports shoes.",
        "Tom: I love skiing. I go skiing once a week in winter. I do it in the mountains. I need skis and warm clothes.",
        "Ayşe: Wow! That sounds fun."],
     "maddeler": [M("a", "Complete the table for AYŞE: Sport, Equipment, Place, Frequency.", "Sport: football · Equipment: ball and sports shoes · Place: school garden · Frequency: twice a week",
                    [A("Sport: football", "football"), A("Equipment: ball, sports shoes", "shoe"), A("Place: school garden", "garden"), A("Frequency: twice a week", "twice", "two times", "2 times")], "tablo2", puan=12),
                  M("b", "Complete the table for TOM: Sport, Equipment, Place, Frequency.", "Sport: skiing · Equipment: skis and warm clothes · Place: mountains · Frequency: once a week",
                    [A("Sport: skiing", "skiing"), A("Equipment: skis, warm clothes", "skis", "clothes"), A("Place: mountains", "mountain"), A("Frequency: once a week", "once")], "tablo2", puan=13)]}])

Y.yaz()
