# -*- coding: utf-8 -*-
"""Matematik (mat1) konu dosyalarını üretir: python3 gen_mat1.py
Her konu bir fonksiyon; çıktı public/mat1/konular/<id>.json.
Renk kodu: negatif = mavi (NEG), pozitif = turuncu (POS). Eksi işareti için gerçek eksi (−, U+2212) kullanılır.
Kesir: metinde [[3/4]] yazılır, sitede alt alta gösterilir."""
import json

NEG, POS, ZER = "#2364c7", "#d9480f", "#b7791f"
M = "−"  # eksi işareti


def bg(ic):
    return f"<svg viewBox='0 0 120 120' xmlns='http://www.w3.org/2000/svg' role='img'><rect width='120' height='120' rx='22' fill='#1b2340'/>{ic}</svg>"


def txt(x, y, t, renk="#f5f6fa", boy=14, kalin=800, hiza="middle"):
    return f"<text x='{x}' y='{y}' text-anchor='{hiza}' font-family='Lexend, Baloo 2, sans-serif' font-weight='{kalin}' font-size='{boy}' fill='{renk}'>{t}</text>"


# ---------- Ortak çizimler (koyu zemin üzerinde açık renkler) ----------
NB, OB = "#6fb3ff", "#ffa26b"  # zemin üstünde negatif / pozitif


def svg_sifir():
    return bg("<line x1='14' y1='80' x2='106' y2='80' stroke='#f5f6fa' stroke-width='3' stroke-linecap='round'/>"
              f"<line x1='30' y1='74' x2='30' y2='86' stroke='{NB}' stroke-width='3'/><line x1='90' y1='74' x2='90' y2='86' stroke='{OB}' stroke-width='3'/>"
              "<line x1='60' y1='80' x2='60' y2='26' stroke='#f5f6fa' stroke-width='3'/><path d='M60 26 L88 34 L60 42z' fill='#f2c14e'/>"
              "<circle cx='60' cy='80' r='14' fill='#f2c14e'/>" + txt(60, 86, "0", "#1b2340", 18)
              + txt(30, 104, M, NB, 18) + txt(90, 104, "+", OB, 18))


def svg_negatif():
    return bg("<rect x='52' y='14' width='16' height='76' rx='8' fill='#f5f6fa'/><circle cx='60' cy='94' r='13' fill='%s'/>" % NB
              + f"<rect x='56' y='66' width='8' height='28' fill='{NB}'/><line x1='40' y1='52' x2='80' y2='52' stroke='#f2c14e' stroke-width='3' stroke-dasharray='4 3'/>"
              + txt(32, 57, "0", "#f2c14e", 15)
              + "<g stroke='%s' stroke-width='2.4' stroke-linecap='round'><path d='M24 78v20M14 88h20M17 81l14 14M31 81l-14 14'/></g>" % NB
              + txt(92, 82, f"{M}5", NB, 20))


def svg_pozitif():
    return bg("<rect x='52' y='14' width='16' height='76' rx='8' fill='#f5f6fa'/><circle cx='60' cy='94' r='13' fill='%s'/>" % OB
              + f"<rect x='56' y='30' width='8' height='64' fill='{OB}'/><line x1='40' y1='52' x2='80' y2='52' stroke='#f2c14e' stroke-width='3' stroke-dasharray='4 3'/>"
              + txt(32, 57, "0", "#f2c14e", 15)
              + "<circle cx='24' cy='28' r='9' fill='#f2c14e'/><g stroke='#f2c14e' stroke-width='2.4' stroke-linecap='round'><path d='M24 12v4M24 40v4M8 28h4M36 28h4M13 17l3 3M32 36l3 3M35 17l-3 3M16 36l-3 3'/></g>"
              + txt(92, 40, "+5", OB, 20))


def svg_kelime():
    kart = lambda y: (f"<rect x='12' y='{y}' width='54' height='34' rx='7' fill='#f5f6fa'/>"
                      f"<line x1='19' y1='{y+10}' x2='58' y2='{y+10}' stroke='#9aa3bf' stroke-width='3' stroke-linecap='round'/>"
                      f"<line x1='19' y1='{y+18}' x2='50' y2='{y+18}' stroke='#9aa3bf' stroke-width='3' stroke-linecap='round'/>"
                      f"<line x1='19' y1='{y+26}' x2='42' y2='{y+26}' stroke='#9aa3bf' stroke-width='3' stroke-linecap='round'/>")
    return bg(kart(18) + kart(68)
              + "<path d='M70 35 h10 M76 30 l5 5 -5 5 M70 85 h10 M76 80 l5 5 -5 5' stroke='#f2c14e' stroke-width='3' fill='none' stroke-linecap='round' stroke-linejoin='round'/>"
              + f"<circle cx='96' cy='35' r='15' fill='{NB}'/>" + txt(96, 42, M, "#1b2340", 22)
              + f"<circle cx='96' cy='85' r='15' fill='{OB}'/>" + txt(96, 92, "+", "#1b2340", 22))


def svg_dogru():
    g = "<line x1='10' y1='62' x2='110' y2='62' stroke='#f5f6fa' stroke-width='3'/><path d='M8 62l7-4v8zM112 62l-7-4v8z' fill='#f5f6fa'/>"
    for i, v in enumerate([-2, -1, 0, 1, 2]):
        x = 20 + i * 20
        r = NB if v < 0 else OB if v > 0 else "#f2c14e"
        g += f"<line x1='{x}' y1='55' x2='{x}' y2='69' stroke='{r}' stroke-width='3'/>" + txt(x, 88, (M + str(-v)) if v < 0 else str(v), r, 14)
    g += f"<path d='M58 44 H22' stroke='{NB}' stroke-width='3' stroke-linecap='round'/><path d='M22 44l6-4v8z' fill='{NB}'/>"
    g += f"<path d='M62 44 H98' stroke='{OB}' stroke-width='3' stroke-linecap='round'/><path d='M98 44l-6-4v8z' fill='{OB}'/>"
    return bg(g)


def svg_aile():
    return bg(f"<rect x='8' y='40' width='42' height='28' rx='14' fill='{NB}'/>" + txt(29, 59, f"{M}3 {M}2 {M}1", "#1b2340", 10)
              + "<circle cx='60' cy='54' r='13' fill='#f2c14e'/>" + txt(60, 60, "0", "#1b2340", 16)
              + f"<rect x='74' y='40' width='38' height='28' rx='14' fill='{OB}'/>" + txt(93, 59, "1 2 3", "#1b2340", 11)
              + "<path d='M10 78 q0 8 8 8 h84 q8 0 8 -8' stroke='#f5f6fa' stroke-width='2.5' fill='none'/>" + txt(60, 104, "TAM SAYILAR", "#f5f6fa", 11)
              + "<path d='M48 32 q0 -8 8 -8 h46 q8 0 8 8' stroke='#5fd08f' stroke-width='2.5' fill='none'/>" + txt(80, 18, "DOĞAL", "#5fd08f", 10))


def svg_uzaklik():
    g = "<line x1='8' y1='78' x2='112' y2='78' stroke='#f5f6fa' stroke-width='3'/>"
    for i, v in enumerate(range(-2, 4)):
        x = 16 + i * 18
        r = NB if v < 0 else OB if v > 0 else "#f2c14e"
        g += f"<line x1='{x}' y1='72' x2='{x}' y2='84' stroke='{r}' stroke-width='3'/>" + txt(x, 100, (M + str(-v)) if v < 0 else str(v), r, 12)
    g += "<path d='M16 70 Q61 18 106 70' stroke='#f2c14e' stroke-width='3.5' fill='none' stroke-linecap='round'/><path d='M106 70l-9-3 6-6z' fill='#f2c14e'/>"
    g += "<circle cx='61' cy='34' r='13' fill='#f2c14e'/>" + txt(61, 40, "5", "#1b2340", 16)
    return bg(g)


def svg_h_dogru():
    g = "<line x1='12' y1='66' x2='108' y2='66' stroke='#f5f6fa' stroke-width='3'/>"
    for i in range(6):
        x = 18 + i * 17
        g += f"<line x1='{x}' y1='60' x2='{x}' y2='72' stroke='#f5f6fa' stroke-width='3'/>" + txt(x, 90, str(i), "#f5f6fa", 13)
    g += "<path d='M18 54 Q61 22 103 54' stroke='#f2c14e' stroke-width='3' fill='none'/><path d='M103 54l-8-2 5-6z' fill='#f2c14e'/>"
    return bg(g)


def svg_h_karsilastir():
    return bg(txt(34, 74, "9", OB, 40) + txt(60, 72, "&gt;", "#f2c14e", 36) + txt(88, 74, "5", "#f5f6fa", 30)
              + "<path d='M22 92 h78' stroke='#5a6280' stroke-width='3' stroke-linecap='round'/>")


def svg_h_fark():
    g = ""
    for i in range(5):
        g += f"<rect x='{20 + i * 16}' y='{92 - i * 16}' width='16' height='{16 + i * 16}' fill='#2b355c' stroke='#f5f6fa' stroke-width='1.5'/>"
    g += "<path d='M26 84 Q60 30 92 24' stroke='#f2c14e' stroke-width='3' fill='none' stroke-linecap='round'/><path d='M92 24l-9 0 5 7z' fill='#f2c14e'/>"
    g += txt(98, 104, "?", "#f2c14e", 20)
    return bg(g)


# ---------- Yardımcılar ----------
def S(soru, secenekler, dogru, ipucu, aciklama, **ek):
    d = {"soru": soru, "secenekler": secenekler, "dogru": dogru, "ipucu": ipucu, "aciklama": aciklama}
    d.update(ek)
    return d


def G(soru, cevap, ipucu, aciklama, **ek):          # tuş takımıyla sayı yazma
    d = {"soru": soru, "cevap": cevap, "ipucu": ipucu, "aciklama": aciklama}
    d.update(ek)
    return d


def N(soru, nokta, sd, ipucu, aciklama, **ek):       # sayı doğrusunda noktaya dokunma
    d = {"soru": soru, "nokta": nokta, "sayiDogrusu": sd, "ipucu": ipucu, "aciklama": aciklama}
    d.update(ek)
    return d


# =================================================================
def u1k1():
    return {
        "id": "u1k1", "unite": "1. Tema: Sayılar ve Nicelikler", "baslik": "Tam Sayılar ve Sayı Doğrusu", "sayfalar": "s. 15–24",
        "giris": "Bu konuda eksi sayılarla tanışacağız. Sıfırın altına inen sıcaklıkları, denizin altındaki derinlikleri ve yerin altındaki katları sayılarla yazmayı öğreneceğiz. Sonra hepsini sayı doğrusunda göstereceğiz.",
        "hazirlik": {
            "baslik": "Hazır mısın?",
            "giris": "Bu konu, sayı doğrusu ve sayıları karşılaştırma bilgilerinin üzerine kuruluyor. Önce bunları hatırlıyor musun bakalım. Not yok; sadece nereden başlayacağımızı bulacağız.",
            "maddeler": [
                {"ad": "Sayı doğrusu", "sinif": "Önceki yıllar", "svg": svg_h_dogru(),
                 "anlatim": "Sayı doğrusu, sayıların sırayla dizildiği bir çizgidir. Ardışık sayılar arasındaki aralıklar eşittir. Sağa gittikçe sayılar büyür.",
                 "akilda": "Sağa gittikçe büyür",
                 "ornek": {"problem": "Sayı doğrusunda 5'i nasıl buluruz?", "adimlar": [
                     {"metin": "0'dan başla."},
                     {"metin": "Sağa doğru 5 aralık say: 1, 2, 3, 4, 5.",
                      "sayiDogrusu": {"min": 0, "max": 8, "oklar": [{"bas": 0, "son": 5, "etiket": "5 aralık"}], "isaretler": [{"x": 5, "etiket": "5"}]}},
                     {"metin": "Durduğun yer 5'tir.", "islem": "0 → 5"}]},
                 "sorular": [
                     N("Sayı doğrusunda 6'nın yerine dokun.", 6, {"min": 0, "max": 10}, "0'dan başla ve sağa doğru 6 aralık say.", "6, 0'ın 6 aralık sağındadır."),
                     G("A noktası hangi sayıyı gösteriyor?", "7", "0'dan başlayıp A'ya kadar aralıkları say.", "0'dan A'ya kadar 7 aralık var. A = 7.",
                       sayiDogrusu={"min": 0, "max": 10, "isaretler": [{"x": 7, "etiket": "A"}], "gizle": [7]})]},
                {"ad": "Büyük mü, küçük mü?", "sinif": "Önceki yıllar", "svg": svg_h_karsilastir(),
                 "anlatim": "Sayı doğrusunda sağdaki sayı, soldaki sayıdan büyüktür. Büyüktür işareti >, küçüktür işareti < ile gösterilir. İşaretin açık ağzı her zaman büyük sayıya bakar.",
                 "akilda": "Ağız büyüğe açılır",
                 "ornek": {"problem": "3 ile 8'i karşılaştıralım.", "adimlar": [
                     {"metin": "İkisini sayı doğrusunda bul. 8 daha sağda.",
                      "sayiDogrusu": {"min": 0, "max": 10, "isaretler": [{"x": 3, "etiket": "3"}, {"x": 8, "etiket": "8"}]}},
                     {"metin": "Sağdaki büyüktür. O hâlde 8 daha büyük."},
                     {"metin": "İşaretin ağzını büyüğe aç.", "islem": "8 > 3   ya da   3 < 8"}]},
                 "sorular": [
                     S("Hangisi doğrudur?", ["9 > 5", "9 < 5", "5 > 9"], 0, "Hangisi daha büyük: 9 mu, 5 mi? İşaretin ağzı büyüğe açılır.", "9, 5'ten büyüktür. Ağız 9'a bakar: 9 > 5."),
                     S("Hangisi doğrudur?", ["12 < 7", "7 < 12", "7 > 12"], 1, "Hangisi daha büyük: 7 mi, 12 mi? Ağız büyüğe bakmalı.", "12 daha büyük. Ağız 12'ye bakar: 7 < 12.")]},
                {"ad": "Aradaki farkı bulma", "sinif": "Önceki yıllar", "svg": svg_h_fark(),
                 "anlatim": "İki sayı arasında kaç birim olduğunu bulmak için büyük sayıdan küçük sayıyı çıkarırız. Sayı doğrusunda aradaki aralıkları sayarak da bulabiliriz.",
                 "akilda": "Büyükten küçüğü çıkar",
                 "ornek": {"problem": "Bir apartmanda 3. kattan 8. kata çıkan asansör kaç kat çıkar?", "adimlar": [
                     {"metin": "Büyük sayı 8, küçük sayı 3."},
                     {"metin": "Büyükten küçüğü çıkar.", "islem": "8 − 3 = 5"},
                     {"metin": "Asansör 5 kat çıkar."}]},
                 "sorular": [
                     G("Bir apartmanda 2. kattan 9. kata çıkan asansör kaç kat çıkar?", "7", "Büyük sayıdan küçük sayıyı çıkar: 9 − 2.", "9 − 2 = 7. Asansör 7 kat çıkar.", birim="kat"),
                     G("Ali 4 yaşında, ablası 11 yaşında. Aralarında kaç yaş fark var?", "7", "Büyük sayıdan küçük sayıyı çıkar: 11 − 4.", "11 − 4 = 7 yaş fark var.", birim="yaş")]}
            ]},
        "kavramlar": [
            {"ad": "Sıfırın İki Anlamı", "renk": "#1f9e8f", "svg": svg_sifir(),
             "aciklama": "0 bazen \"hiç yok\" demektir: 0 MB internet, hiç internet kalmadı demektir. Bazen de bir başlangıç çizgisidir: 0 °C, deniz seviyesi, zemin kat gibi.",
             "ek": "Başlangıç çizgisi olan 0'ın altına da inebiliriz. Hava 0 °C'un altına düşebilir, bir araç deniz seviyesinin altına dalabilir. İşte bu yüzden yeni sayılara ihtiyaç var. (s. 15–16, 18)",
             "akilda": "0 = başlangıç çizgisi",
             "soru": S("Hangisinde 0, \"hiç yok\" anlamındadır?", ["Telefonda 0 MB internet kaldı.", "Hava sıcaklığı 0 °C.", "Asansör 0. katta (zemin kat)."], 0,
                       "Hangisinde bir şey tamamen bitmiş? Sıcaklık ve kat için 0 bir başlangıç çizgisidir.",
                       "0 MB = hiç internet kalmadı. 0 °C ve zemin kat ise başlangıç çizgisidir; altına inilebilir. (s. 15)")},
            {"ad": "Negatif Tam Sayılar", "renk": "#3274d6", "svg": svg_negatif(),
             "aciklama": f"Başlangıç çizgisinin altında ya da gerisinde kalan sayılardır. Önlerine \"{M}\" işareti konur. Okurken önce işareti, sonra sayıyı söyleriz: {M}8, \"eksi sekiz\" diye okunur.",
             "ek": f"Deringöz adlı su altı aracı deniz seviyesinin 8 metre altında. Konumu: {M}8 m. (s. 17–18)",
             "akilda": f"Altında = eksi ({M})",
             "sayiDogrusu": {"min": -10, "max": 10, "dikey": True, "birim": 16, "sifirEtiketi": "Deniz seviyesi",
                             "gizle": [v for v in range(-9, 10, 2)],
                             "isaretler": [{"x": -8, "etiket": f"Deringöz {M}8 m", "renk": NEG}, {"x": 10, "etiket": "Ekip +10 m", "renk": POS}]},
             "soru": S("Bir dalgıç deniz seviyesinin 5 metre altında. Konumunu hangi sayı gösterir?", ["+5 m", f"{M}5 m", "0 m"], 1,
                       f"\"Altında\" kelimesine dikkat. Altında olanların önüne hangi işaret konur?",
                       f"Deniz seviyesinin altı negatiftir: {M}5 m. (s. 18, 20)")},
            {"ad": "Pozitif Tam Sayılar", "renk": POS, "svg": svg_pozitif(),
             "aciklama": "Başlangıç çizgisinin üstünde ya da ilerisinde kalan sayılardır. Önlerine \"+\" işareti konur. Bu işaret yazılmasa da olur: +4 ile 4 aynı sayıdır.",
             "ek": "Araştırma ekibi deniz seviyesinin 10 metre üstünde: +10 m. Okurken \"artı on\" deriz. (s. 17, 20)",
             "akilda": "Üstünde = artı (+)",
             "soru": S("Hangisi +7 ile aynı sayıdır?", [f"{M}7", "0,7", "7"], 2,
                       "Pozitif sayıların önündeki + işareti yazılmayabilir.",
                       "+7 = 7. Pozitif sayıların önündeki + yazılmayabilir. (s. 20)")},
            {"ad": "Kelimeden Sayıya", "renk": "#7b4fc9", "svg": svg_kelime(),
             "aciklama": f"Problemlerde \"eksi\" kelimesi pek yazmaz. İşareti kelimelerden anlarız. Altı, borç, gider, zarar → eksi ({M}). Üstü, alacak, gelir, kâr → artı (+).",
             "ek": "Bir cümleyi sayıya çevirirken üç soru sor: Başlangıç (0) nerede? Yön hangisi, altı mı üstü mü? Kaç birim? (Kelime listesi: s. 20)",
             "akilda": f"Altı, borç, gider → {M}",
             "cozum": {"baslik": "Cümleyi sayıya çevirelim", "problem": "Bir maden ocağı yer yüzeyinin 40 metre altındadır. Bu konumu tam sayıyla yazalım.",
                       "adimlar": [
                           {"metin": "Başlangıç (0) nerede? Yer yüzeyi.", "islem": "Yer yüzeyi = 0"},
                           {"metin": "Yön hangisi? Cümle \"altında\" diyor. Altı eksidir.", "islem": f"Yön: {M}"},
                           {"metin": "Kaç birim? 40 metre.", "islem": "Miktar: 40"},
                           {"metin": "İşareti ve sayıyı birleştir.", "islem": f"{M}40 m"}],
                       "sonuc": f"Maden ocağının konumu {M}40 m'dir."},
             "sende": {"baslik": "Şimdi sen çevir", "problem": "Mert'in kartında 120 TL borç var. Bu durumu tam sayıyla yazalım.",
                       "adimlar": [
                           {"metin": "Başlangıç (0): Kartta ne para var ne borç.", "islem": "Boş kart = 0"},
                           {"metin": "Yön hangisi?",
                            "soru": S("\"Borç\" hangi işareti gösterir?", ["Artı (+)", f"Eksi ({M})", "İşaret yok"], 1,
                                      "Borç, gider ve zarar hangi gruptaydı?", "Borç eksidir."),
                            "islem": f"Yön: {M}"},
                           {"metin": "Kaç birim?",
                            "soru": G("Borç kaç TL?", "120", "Cümledeki sayıya bak.", "Borç 120 TL.", birim="TL"),
                            "islem": "Miktar: 120"},
                           {"metin": "Şimdi işareti ve sayıyı birleştir.",
                            "soru": G("Mert'in kartındaki durumu yaz.", "-120", f"Önce {M} tuşuna, sonra sayılara dokun.", f"Borç eksidir: {M}120 TL.", birim="TL"),
                            "islem": f"{M}120 TL"}],
                       "sonuc": f"Harika! 120 TL borç = {M}120 TL. Kitaptaki Mert'in kartı da böyle çalışıyor. (s. 18)"},
             "soru": S("Bir dükkân bu ay 500 TL zarar etti. Bu durumu hangi sayı gösterir?", [f"{M}500 TL", "+500 TL", "0 TL"], 0,
                       "Zarar hangi gruptaydı: altı, borç, gider, zarar…",
                       f"Zarar eksidir: {M}500 TL. (s. 20)")},
            {"ad": "Sayı Doğrusu", "renk": "#1f9e8f", "svg": svg_dogru(),
             "aciklama": "Tam sayıları bir çizgi üzerinde gösteririz. 0 tam ortadadır. Pozitif sayılar 0'ın sağında, negatif sayılar 0'ın solundadır.",
             "ek": "Termometreyi yan yatırdığını düşün: yukarısı sağa, aşağısı sola gelir. Sağa gittikçe sayılar büyür. (s. 19–20)",
             "akilda": "Sol eksi, sağ artı",
             "sayiDogrusu": {"min": -6, "max": 6, "isaretli": True},
             "cozum": {"baslik": f"{M}4'ü sayı doğrusunda bulalım",
                       "adimlar": [
                           {"metin": "Önce 0'ı bul. 0 başlangıç noktasıdır."},
                           {"metin": f"Sayı eksi mi, artı mı? {M}4 eksi. Eksi sayılar 0'ın solunda.", "islem": "Yön: sola"},
                           {"metin": "0'dan sola doğru 4 aralık say.",
                            "sayiDogrusu": {"min": -6, "max": 6, "oklar": [{"bas": 0, "son": -4, "etiket": "4 aralık sola", "renk": NEG}], "isaretler": [{"x": -4, "etiket": f"{M}4", "renk": NEG}]},
                            "islem": f"0 → {M}4"}],
                       "sonuc": f"{M}4, 0'ın 4 birim solundadır."},
             "soru": N("Sayı doğrusunda +5'in yerine dokun.", 5, {"min": -6, "max": 6}, "Artı sayılar 0'ın sağında. 0'dan sağa 5 aralık say.", "+5, 0'ın 5 birim sağındadır. (s. 20)")},
            {"ad": "Tam Sayılar Ailesi", "renk": ZER, "svg": svg_aile(),
             "aciklama": "Negatif tam sayılar, sıfır ve pozitif tam sayılar bir araya gelince tam sayıları oluşturur.",
             "ek": "Sıfır ne pozitif ne negatiftir; bu yüzden sıfırın işareti yoktur. Doğal sayılar (0, 1, 2, 3…) da tam sayıların içindedir. (s. 20)",
             "akilda": "Eksiler + 0 + artılar",
             "soru": S("Hangisi tam sayıdır ama doğal sayı değildir?", [f"{M}6", "0", "6"], 0,
                       "Doğal sayılar 0, 1, 2, 3… diye gider. İçinde eksi sayı var mı?",
                       f"{M}6 negatif bir tam sayıdır. Doğal sayılarda eksi sayı yoktur. (s. 20)")},
            {"ad": "İki Sayı Arasındaki Uzaklık", "renk": "#e8590c", "svg": svg_uzaklik(),
             "aciklama": "İki tam sayı arasındaki uzaklığı, sayı doğrusunda aradaki aralıkları sayarak buluruz. Uzaklık her zaman pozitif bir sayıdır.",
             "ek": "Aralıkları tek tek saymak her zaman işe yarar. Yol 0'dan geçiyorsa iki parçaya bölmek işi kolaylaştırır. (s. 22–23)",
             "akilda": "Aralıkları say",
             "cozum": {"baslik": f"{M}2 ile +3 arası kaç birim?",
                       "sayiDogrusu": {"min": -4, "max": 5, "isaretler": [{"x": -2, "etiket": f"{M}2", "renk": NEG}, {"x": 3, "etiket": "+3", "renk": POS}]},
                       "adimlar": [
                           {"metin": "İki sayıyı sayı doğrusunda bul. Aralarında 0 var."},
                           {"metin": f"{M}2'den 0'a kadar say: 2 aralık.",
                            "sayiDogrusu": {"min": -4, "max": 5, "oklar": [{"bas": -2, "son": 0, "etiket": "2", "renk": NEG}]}, "islem": f"{M}2 → 0 : 2 birim"},
                           {"metin": "0'dan +3'e kadar say: 3 aralık.",
                            "sayiDogrusu": {"min": -4, "max": 5, "oklar": [{"bas": 0, "son": 3, "etiket": "3", "renk": POS}]}, "islem": "0 → +3 : 3 birim"},
                           {"metin": "İki parçayı topla.", "islem": "2 + 3 = 5 birim"}],
                       "sonuc": f"{M}2 ile +3 arasında 5 birim uzaklık vardır."},
             "sende": {"baslik": "Asansörle kaç kat?", "problem": f"Bir AVM'de otopark {M}3. katta, sinema +4. katta. Otoparktan sinemaya asansörle kaç kat çıkılır?",
                       "sayiDogrusu": {"min": -4, "max": 5, "dikey": True, "birim": 28, "sifirEtiketi": "Zemin kat",
                                       "isaretler": [{"x": -3, "etiket": f"Otopark {M}3", "renk": NEG}, {"x": 4, "etiket": "Sinema +4", "renk": POS}]},
                       "adimlar": [
                           {"metin": "Otoparktan zemin kata (0) kaç kat var?",
                            "soru": G(f"{M}3'ten 0'a kaç kat çıkılır?", "3", f"{M}3, {M}2, {M}1, 0… aralıkları say.", f"{M}3'ten 0'a 3 kat.", birim="kat"),
                            "islem": f"{M}3 → 0 : 3 kat"},
                           {"metin": "Zemin kattan sinemaya kaç kat var?",
                            "soru": G("0'dan +4'e kaç kat çıkılır?", "4", "0'dan yukarı doğru aralıkları say.", "0'dan +4'e 4 kat.", birim="kat"),
                            "islem": "0 → +4 : 4 kat"},
                           {"metin": "İki parçayı topla.",
                            "soru": G("Toplam kaç kat çıkılır?", "7", "3 + 4 = ?", "3 + 4 = 7 kat.", birim="kat"),
                            "islem": "3 + 4 = 7 kat"}],
                       "sonuc": "Otoparktan sinemaya 7 kat çıkılır. Asansörde de tam böyle sayarız."},
             "soru": G(f"Sayı doğrusunda {M}1 ile +4 arasında kaç birim var?", "5",
                       f"{M}1'den 0'a kaç aralık? 0'dan +4'e kaç aralık? İkisini topla.",
                       f"{M}1 → 0: 1 birim, 0 → +4: 4 birim. 1 + 4 = 5 birim. (s. 23)", birim="birim",
                       sayiDogrusu={"min": -3, "max": 6, "isaretler": [{"x": -1, "etiket": f"{M}1", "renk": NEG}, {"x": 4, "etiket": "+4", "renk": POS}]})}
        ],
        "biliyorMusun": [
            f"Türkiye saati, dünya saatinin başlangıcı kabul edilen UTC'ye göre 3 saat ileride olduğu için UTC+3; New York saati 5 saat geride olduğu için UTC{M}5 diye yazılır. (s. 21)",
            f"Bazı aşılar +2 °C ile +8 °C arasında, bazıları ise {M}20 °C'ta saklanır. (s. 21)",
            f"Uzman bir dalgıç en fazla 40 metre derinliğe, yani {M}40 m'ye kadar dalabilir. (s. 21)"],
        "akildaKalsin": [
            "0 bazen \"hiç yok\", bazen \"başlangıç çizgisi\" demektir.",
            f"Başlangıcın altı, borç, gider, zarar → eksi ({M}).",
            "Başlangıcın üstü, alacak, gelir, kâr → artı (+).",
            "Sayı doğrusunda negatifler 0'ın solunda, pozitifler sağındadır.",
            "Sıfırın işareti yoktur. +4 ile 4 aynı sayıdır.",
            "İki sayı arasındaki uzaklığı aralıkları sayarak buluruz."],
        "merakKutusu": [
            {"soru": "Hava 0 °C ise hiç sıcaklık yok mu demek?", "cevap": f"Hayır. 0 °C bir başlangıç çizgisidir. Hava bundan daha da soğuyabilir: {M}5 °C gibi. (s. 15–16)"},
            {"soru": "Sıfır neden ne artı ne eksi?", "cevap": "Çünkü 0 başlangıç noktasıdır; pozitiflerle negatiflerin tam ortasında durur. Bu yüzden sıfırın işareti yoktur. (s. 20)"},
            {"soru": f"{M}8 nasıl okunur?", "cevap": "Önce işaret, sonra sayı söylenir: \"eksi sekiz\". (s. 18)"},
            {"soru": "+5 ile 5 aynı mı?", "cevap": "Evet. Pozitif sayıların önündeki + işareti yazılmayabilir: +4 = 4. (s. 20)"},
            {"soru": f"Asansördeki {M}1 düğmesi ne demek?", "cevap": f"Zemin kat 0 kabul edilir. {M}1, zemin katın bir kat altı demektir. (s. 20, 22)"},
            {"soru": "Tam sayılar günlük hayatta nerede işe yarar?", "cevap": "Hava sıcaklığında, dalış derinliğinde, ülkeler arasındaki saat farkında ve gıdaların soğukta saklanmasında. (s. 21)"}],
        "dusunVeYaz": [{"soru": "Günlük hayattan eksi bir sayıyla anlatılabilecek bir durum yaz. Sayısını da yaz.",
                        "ornekCevap": f"Kışın Kars'ta hava sıfırın 9 derece altına düştü. Sıcaklık {M}9 °C oldu.",
                        "anahtarlar": ["alt", "eksi", M, "borç"]}],
        "sorular": [
            S("Hava sıcaklığı sıfırın 6 derece altına düştü. Sıcaklık kaç derecedir?", [f"{M}6 °C", "0 °C", "+6 °C"], 0,
              "\"Sıfırın altı\" hangi işaretle gösterilir?", f"Sıfırın altı negatiftir: {M}6 °C. (s. 19–20)"),
            G("Bir denizaltı deniz seviyesinin 35 metre altında. Konumunu tam sayıyla yaz.", "-35",
              f"\"Altında\" eksi demek. Önce {M} tuşuna, sonra sayıya dokun.", f"Deniz seviyesinin 35 m altı: {M}35 m. (s. 17–18)", birim="m"),
            N("Sayı doğrusunda sıfırın 4 birim solundaki sayıya dokun.", -4, {"min": -6, "max": 6},
              "0'ı bul. Sola doğru 4 aralık say.", f"0'ın 4 birim solunda {M}4 vardır. (s. 20)"),
            S("Hangisi negatif bir tam sayıyla anlatılır?", ["Ayşe 50 TL kazandı.", "Asansör zemin katın 2 kat altına indi.", "Uçak deniz seviyesinin 10 km üstünde."], 1,
              "Altı, borç, gider, zarar… Hangi cümlede bu kelimelerden biri var?", f"Zemin katın 2 kat altı: {M}2. Kazanç ve \"üstünde\" pozitiftir. (s. 20)"),
            S("Sıfır için hangisi doğrudur?", ["Sıfır pozitif bir tam sayıdır.", "Sıfır negatif bir tam sayıdır.", "Sıfırın işareti yoktur."], 2,
              "Sıfır, sayı doğrusunun neresinde duruyordu?", "Sıfır ne pozitif ne negatiftir; işareti yoktur. (s. 20)"),
            G("A noktası hangi tam sayıyı gösteriyor?", "-5", "A, 0'ın solunda mı sağında mı? 0'dan A'ya kadar aralıkları say.",
              f"A, 0'ın 5 birim solunda: {M}5. (s. 20, 23)", sayiDogrusu={"min": -6, "max": 6, "isaretler": [{"x": -5, "etiket": "A"}], "gizle": [-5]}),
            S("Hangisi doğal sayıdır?", [f"{M}1", f"{M}10", "0"], 2,
              "Doğal sayılar 0, 1, 2, 3… Eksi sayı doğal sayı olur mu?", "0 bir doğal sayıdır. Eksi sayılar doğal sayı değildir. (s. 20)"),
            G(f"Bir binada otopark {M}2. katta, Elif +5. katta oturuyor. Otoparktan Elif'in katına kaç kat çıkılır?", "7",
              f"{M}2'den 0'a kaç kat? 0'dan +5'e kaç kat? İkisini topla.", f"{M}2 → 0: 2 kat, 0 → +5: 5 kat. 2 + 5 = 7 kat. (s. 22)", birim="kat"),
            N("Termometrede 0 °C'un 3 derece üstüne dokun.", 3, {"min": -5, "max": 5, "dikey": True, "birim": 26, "sifirEtiketi": "0 °C"},
              "\"Üstü\" artı demek. 0'dan yukarı 3 aralık say.", "0 °C'un 3 derece üstü +3 °C'tur. (s. 19–20)"),
            S("Mert'in kartında hafta başında 300 TL vardı. O hafta 400 TL harcadı. Kart borçlanabildiğine göre hafta sonunda kartın durumu nedir?",
              ["+100 TL", f"{M}100 TL", f"{M}400 TL"], 1,
              "300 TL'yi harcayınca kart 0 olur. Fazladan kaç TL harcadı? Fazlası borçtur.",
              f"300 TL harcayınca kart 0 olur. Kalan 100 TL borç olur: {M}100 TL. (s. 18)")]
    }


# ---------- u1k2 çizimleri ----------
def kesir_svg(x, y, pay, payda, renk="#f5f6fa", boy=20, isaret=""):
    """SVG içinde alt alta kesir (çizgi ile)."""
    g = ""
    if isaret:
        g += txt(x - boy * .75, y + boy * .35, isaret, renk, boy)
    g += txt(x, y - 4, pay, renk, boy) + f"<line x1='{x - boy * .55}' y1='{y + 2}' x2='{x + boy * .55}' y2='{y + 2}' stroke='{renk}' stroke-width='2.6' stroke-linecap='round'/>"
    g += txt(x, y + boy + 4, payda, renk, boy)
    return g


def svg_h_kesir():
    g = ""
    for i in range(4):
        g += f"<rect x='{16 + i * 22}' y='22' width='20' height='44' rx='4' fill='{OB if i < 3 else '#2b355c'}' stroke='#f5f6fa' stroke-width='1.5'/>"
    return bg(g + kesir_svg(60, 88, "3", "4", "#f5f6fa", 18))


def svg_h_denk():
    ust = "".join(f"<rect x='{14 + i * 46}' y='18' width='46' height='26' fill='{OB if i < 1 else '#2b355c'}' stroke='#f5f6fa' stroke-width='1.5'/>" for i in range(2))
    alt = "".join(f"<rect x='{14 + i * 23}' y='56' width='23' height='26' fill='{OB if i < 2 else '#2b355c'}' stroke='#f5f6fa' stroke-width='1.5'/>" for i in range(4))
    return bg(ust + alt + txt(36, 108, "1/2", "#f5f6fa", 15) + txt(60, 108, "=", "#f2c14e", 16) + txt(86, 108, "2/4", "#f5f6fa", 15))


def svg_h_tamli():
    g = ""
    for k in range(2):
        g += f"<circle cx='{26 + k * 34}' cy='40' r='15' fill='{OB}'/>"
    g += "<path d='M94 40 L94 25 A15 15 0 1 1 79 40 Z' fill='%s'/><circle cx='94' cy='40' r='15' fill='none' stroke='#f5f6fa' stroke-width='1.5'/>" % OB
    g += "<path d='M94 25 V55 M79 40 H109' stroke='#1b2340' stroke-width='1.6'/>"
    return bg(g + kesir_svg(34, 84, "11", "4", "#f5f6fa", 15) + txt(60, 96, "=", "#f2c14e", 16) + txt(78, 96, "2", "#f5f6fa", 18) + kesir_svg(94, 84, "3", "4", "#f5f6fa", 15))


def svg_arada():
    g = "<line x1='12' y1='70' x2='108' y2='70' stroke='#f5f6fa' stroke-width='3'/>"
    g += "<line x1='20' y1='62' x2='20' y2='78' stroke='#f2c14e' stroke-width='3'/><line x1='100' y1='62' x2='100' y2='78' stroke='#f5f6fa' stroke-width='3'/>"
    g += f"<line x1='60' y1='65' x2='60' y2='75' stroke='{OB}' stroke-width='3'/>"
    g += txt(20, 96, "0", "#f2c14e", 15) + txt(100, 96, "1", "#f5f6fa", 15)
    for x in (32, 72):  # ayak izleri
        g += f"<ellipse cx='{x}' cy='44' rx='7' ry='10' fill='{OB}'/><circle cx='{x + 4}' cy='30' r='2.5' fill='{OB}'/><circle cx='{x - 1}' cy='29' r='2.5' fill='{OB}'/>"
    g += kesir_svg(60, 98, "1", "2", OB, 12)
    return bg(g)


def svg_rasyonel():
    g = kesir_svg(52, 52, "a", "b", "#f5f6fa", 30)
    g += f"<rect x='72' y='70' width='38' height='24' rx='12' fill='{NB}'/>" + txt(91, 87, "b ≠ 0", "#1b2340", 12)
    g += txt(22, 30, "3/4", OB, 13) + txt(98, 30, "−5/2", NB, 13) + txt(22, 108, "0,3", OB, 13)
    return bg(g)


def svg_payda0():
    g = kesir_svg(48, 52, "8", "0", "#f5f6fa", 32)
    g += "<path d='M76 28 L106 58 M106 28 L76 58' stroke='#ff6b6b' stroke-width='6' stroke-linecap='round'/>"
    g += "<rect x='14' y='94' width='92' height='18' rx='9' fill='#ff6b6b'/>" + txt(60, 107, "TANIMSIZ", "#1b2340", 11)
    return bg(g)


def svg_aile2():
    g = "<rect x='8' y='8' width='104' height='104' rx='16' fill='#2b355c' stroke='#c99cff' stroke-width='2.5'/>" + txt(60, 26, "RASYONEL", "#c99cff", 11)
    g += "<rect x='20' y='36' width='80' height='68' rx='12' fill='#23325c' stroke='#f5f6fa' stroke-width='2.5'/>" + txt(60, 52, "TAM", "#f5f6fa", 11)
    g += "<rect x='44' y='62' width='50' height='34' rx='9' fill='#1f4a3a' stroke='#5fd08f' stroke-width='2.5'/>" + txt(69, 84, "DOĞAL", "#5fd08f", 10)
    g += txt(98, 26, "½", "#c99cff", 12) + txt(32, 84, M + "3", NB, 12)
    return bg(g)


def svg_eksi_butun():
    g = f"<path d='M34 24 Q20 60 34 96' stroke='{NB}' stroke-width='3.5' fill='none' stroke-linecap='round'/><path d='M100 24 Q114 60 100 96' stroke='{NB}' stroke-width='3.5' fill='none' stroke-linecap='round'/>"
    g += txt(15, 70, M, NB, 26) + txt(54, 72, "1", "#f5f6fa", 32) + kesir_svg(80, 54, "1", "2", "#f5f6fa", 20)
    return bg(g)


def svg_sd_rasyonel():
    g = "<line x1='8' y1='72' x2='112' y2='72' stroke='#f5f6fa' stroke-width='3'/>"
    for i in range(6):
        x = 16 + i * 17.6
        g += f"<line x1='{x}' y1='{64 if i in (0, 5) else 67}' x2='{x}' y2='{80 if i in (0, 5) else 77}' stroke='{NB}' stroke-width='{3 if i in (0, 5) else 2}'/>"
    g += txt(16, 98, M + "3", NB, 13) + txt(104, 98, M + "2", NB, 13)
    g += f"<path d='M104 60 Q78 28 51.2 60' stroke='#f2c14e' stroke-width='3' fill='none' stroke-linecap='round'/><path d='M51.2 60 l1 -9 6.5 5z' fill='#f2c14e'/>"
    g += f"<circle cx='51.2' cy='72' r='7' fill='{NB}' stroke='#f5f6fa' stroke-width='2'/>" + txt(78, 30, "3 parça", "#f2c14e", 11)
    return bg(g)


def svg_eksi_yer():
    g = txt(11, 46, M, NB, 18) + kesir_svg(26, 38, "9", "3", "#f5f6fa", 14)
    g += txt(42, 46, "=", "#f2c14e", 15) + kesir_svg(60, 38, M + "9", "3", "#f5f6fa", 14)
    g += txt(78, 46, "=", "#f2c14e", 15) + kesir_svg(96, 38, "9", M + "3", "#f5f6fa", 14)
    g += "<path d='M22 76 Q60 90 98 76' stroke='#f2c14e' stroke-width='2.5' fill='none'/>"
    g += f"<rect x='38' y='88' width='44' height='24' rx='12' fill='{NB}'/>" + txt(60, 105, M + "3", "#1b2340", 16)
    return bg(g)


# =================================================================
def u1k2():
    sd_kir = lambda mn, mx, bol, **ek: dict({"min": mn, "max": mx, "bolme": bol}, **ek)
    return {
        "id": "u1k2", "unite": "1. Tema: Sayılar ve Nicelikler", "baslik": "Rasyonel Sayılar", "sayfalar": "s. 25–34",
        "giris": "İki tam sayının arasında başka tam sayı yoktur. Ama arada başka sayılar vardır! Bu konuda kesir şeklinde yazılabilen bu sayılarla, yani rasyonel sayılarla tanışacağız ve onları sayı doğrusunda bulacağız.",
        "hazirlik": {
            "baslik": "Hazır mısın?",
            "giris": "Bu konu kesir bilgilerinin üzerine kuruluyor. Önce bunları hatırlıyor musun bakalım. Not yok; sadece nereden başlayacağımızı bulacağız.",
            "maddeler": [
                {"ad": "Kesir: pay ve payda", "sinif": "Önceki yıllar", "svg": svg_h_kesir(),
                 "anlatim": "Bir bütünü eş parçalara böleriz. Alttaki sayı (payda), bütünün kaç eş parçaya bölündüğünü gösterir. Üstteki sayı (pay), kaç parça aldığımızı gösterir.",
                 "akilda": "Payda: kaç parça? Pay: kaç aldık?",
                 "ornek": {"problem": "Bir çikolata 4 eş parçaya bölündü. 3 parçasını yedik. Yediğimiz kısmı kesirle yazalım.", "adimlar": [
                     {"metin": "Bütün kaç eş parçaya bölündü? 4. Bu sayı alta, paydaya yazılır.", "islem": "Payda = 4"},
                     {"metin": "Kaç parça yedik? 3. Bu sayı üste, paya yazılır.", "islem": "Pay = 3"},
                     {"metin": "İkisini birleştir.", "islem": "[[3/4]]"}]},
                 "sorular": [
                     S("Bir pizza 5 eş dilime bölündü, 2 dilimi yendi. Yenen kısım hangi kesirle gösterilir?", ["[[2/5]]", "[[5/2]]", "[[3/5]]"], 0,
                       "Payda kaç eş parça olduğunu, pay kaç parça yendiğini gösterir.", "5 eş dilimden 2'si yendi: [[2/5]]."),
                     G("[[3/8]] kesrinin paydası kaçtır?", "8", "Payda, kesir çizgisinin altındaki sayıdır.", "Kesir çizgisinin altındaki sayı 8'dir.")]},
                {"ad": "Denk kesir ve sadeleştirme", "sinif": "Önceki yıllar", "svg": svg_h_denk(),
                 "anlatim": "Pay ve paydayı aynı sayıya bölersek kesrin değeri değişmez: [[2/4]] = [[1/2]]. Bunlara denk kesir denir. Pay ve payda artık aynı sayıya bölünemiyorsa kesir en sade hâlindedir.",
                 "akilda": "Üstü ve altı aynı sayıya böl",
                 "ornek": {"problem": "[[6/8]] kesrini sadeleştirelim.", "adimlar": [
                     {"metin": "6 ve 8'in ikisi de 2'ye bölünür.", "islem": "6 ÷ 2 = 3   ve   8 ÷ 2 = 4"},
                     {"metin": "Yeni kesri yaz.", "islem": "[[6/8]] = [[3/4]]"},
                     {"metin": "3 ve 4'ü birlikte bölen başka sayı (1'den başka) yok. En sade hâl bu."}]},
                 "sorular": [
                     S("[[4/8]] kesrinin en sade hâli hangisidir?", ["[[2/4]]", "[[1/2]]", "[[1/4]]"], 1,
                       "4 ve 8'i birlikte bölebileceğin en büyük sayı 4'tür.", "4 ÷ 4 = 1, 8 ÷ 4 = 2. En sade hâl [[1/2]]. (s. 27)"),
                     G("[[6/9]] kesrini sadeleştirip en sade hâlini yaz.", "2/3", "6 ve 9'un ikisi de 3'e bölünür. Kesir çizgisi için / tuşunu kullan.",
                       "6 ÷ 3 = 2, 9 ÷ 3 = 3. En sade hâl [[2/3]].", kesir=True)]},
                {"ad": "Bileşik kesir ↔ tam sayılı kesir", "sinif": "Önceki yıllar", "svg": svg_h_tamli(),
                 "anlatim": "Payı paydadan büyük olan kesre bileşik kesir denir. Onu tam sayılı kesre çevirmek için payı paydaya böleriz: bölüm tam kısım, kalan yeni pay olur, payda aynı kalır. Geri çevirirken tam kısım × payda + pay yaparız.",
                 "akilda": "Böl: bölüm tam, kalan pay",
                 "ornek": {"problem": "[[11/4]] kesrini tam sayılı kesre çevirelim.", "adimlar": [
                     {"metin": "11'i 4'e böl.", "islem": "11 ÷ 4 = 2, kalan 3"},
                     {"metin": "Bölüm (2) tam kısım olur. Kalan (3) pay olur. Payda (4) aynı kalır.", "islem": "[[11/4]] = [[2 3/4]]"},
                     {"metin": "Kontrol: 2 × 4 + 3 = 11. Doğru!"}]},
                 "sorular": [
                     S("[[7/2]] kesri hangi tam sayılı kesre eşittir?", ["[[3 1/2]]", "[[2 1/2]]", "[[3 2/7]]"], 0,
                       "7'yi 2'ye böl. Bölüm tam kısım, kalan pay olur.", "7 ÷ 2 = 3, kalan 1: [[3 1/2]]."),
                     G("[[11/3]] kesrini tam sayılı kesre çevirirsen tam kısım kaç olur?", "3", "11'i 3'e böl. Bölüm kaç?", "11 ÷ 3 = 3, kalan 2: [[3 2/3]]. Tam kısım 3.")]},
                {"ad": "Eksi sayılar sayı doğrusunda", "sinif": "Geçen konu", "svg": svg_dogru(),
                 "anlatim": "Sayı doğrusunda 0'ın sağında pozitif sayılar, solunda negatif sayılar vardır. Eksi bir sayıyı bulmak için 0'dan sola doğru sayarız.",
                 "akilda": "Sol eksi, sağ artı",
                 "ornek": {"problem": f"{M}3'ü sayı doğrusunda bulalım.", "adimlar": [
                     {"metin": f"{M}3 eksi bir sayı. Eksi sayılar 0'ın solunda.", "islem": "Yön: sola"},
                     {"metin": "0'dan sola 3 aralık say.",
                      "sayiDogrusu": {"min": -5, "max": 3, "oklar": [{"bas": 0, "son": -3, "etiket": "3 aralık", "renk": NEG}], "isaretler": [{"x": -3, "etiket": f"{M}3", "renk": NEG}]},
                      "islem": f"0 → {M}3"}]},
                 "sorular": [
                     N(f"Sayı doğrusunda {M}3'ün yerine dokun.", -3, {"min": -5, "max": 5}, "0'ı bul. Sola doğru 3 aralık say.", f"{M}3, 0'ın 3 birim solundadır."),
                     S("Hangisi sayı doğrusunda 0'ın solundadır?", [f"{M}2", "2", "0"], 0, "0'ın solunda eksi sayılar vardır.", f"{M}2 negatiftir, 0'ın solundadır.")]}
            ]},
        "kavramlar": [
            {"ad": "Aradaki Sayılar", "renk": "#1f9e8f", "svg": svg_arada(),
             "aciklama": "Sayı doğrusunda 0 ile 1 arasında başka tam sayı yoktur. Ama arada başka sayılar vardır! Bu sayıları bulmak için aralığı eş parçalara böleriz.",
             "ek": "Kitaptaki Yasemin, 1 metrelik yolu eşit 2 adımda yürüyor. Bir adımı [[1/2]] metredir. Bu nokta, 0 ile 1'in tam ortasındadır. (s. 25)",
             "akilda": "Arayı eş parçalara böl",
             "sayiDogrusu": sd_kir(0, 2, 2, isaretler=[{"x": 0.5, "etiket": "1/2 m", "renk": POS}]),
             "soru": N("0 ile 1'in tam ortasındaki noktaya dokun.", 0.5, sd_kir(0, 2, 2),
                       "0 ile 1 arası 2 eş parçaya bölündü. Aradaki küçük çizgiye bak.", "0 ile 1'in tam ortası [[1/2]]'dir. (s. 25, 27)")},
            {"ad": "Rasyonel Sayı", "renk": "#7b4fc9", "svg": svg_rasyonel(),
             "aciklama": "Pay ve paydası tam sayı olan, paydası 0 olmayan bir kesir şeklinde yazılabilen sayılara rasyonel sayı denir. [[3/4]], [[-5/2]] ve [[8/1]] birer rasyonel sayıdır.",
             "ek": "0'dan büyük olanlara pozitif rasyonel sayı ([[5/7]]), 0'dan küçük olanlara negatif rasyonel sayı ([[-22/23]]) denir. 0,3 gibi ondalık sayılar da kesir şeklinde yazılabildiği için rasyonel sayıdır. (s. 28)",
             "akilda": "Kesir gibi yazılabilen sayı",
             "soru": S("Hangisi negatif bir rasyonel sayıdır?", ["[[3/4]]", "0", "[[-3/4]]"], 2,
                       "Negatif sayılar 0'dan küçüktür ve önlerinde eksi işareti vardır.", "[[-3/4]] sıfırdan küçüktür, negatif bir rasyonel sayıdır. (s. 28)")},
            {"ad": "Payda Sıfır Olamaz", "renk": "#c92a2a", "svg": svg_payda0(),
             "aciklama": "Bir rasyonel sayının paydası asla 0 olamaz. [[8/0]] gibi bir yazım tanımsızdır, yani bir sayı belirtmez.",
             "ek": "Neden? 8'i 0'a bölmek, 0 ile çarpınca 8 eden sayıyı aramaktır. Ama 0 ile çarpılan her sayı 0 olur, hiçbir zaman 8 olmaz. (s. 28)",
             "akilda": "Payda asla 0 olmaz",
             "soru": S("Hangisi bir rasyonel sayı değildir?", ["[[0/5]]", "[[5/0]]", "[[-5/1]]"], 1,
                       "Paydaya, yani kesir çizgisinin altına bak. Hangisinde 0 var?", "[[5/0]] tanımsızdır, çünkü paydası 0'dır. (s. 28)")},
            {"ad": "Sayı Aileleri", "renk": ZER, "svg": svg_aile2(),
             "aciklama": "Her tam sayı, paydası 1 olan bir kesir gibi yazılabilir: 5 = [[5/1]], [[-3/1]] = −3. Bu yüzden her tam sayı bir rasyonel sayıdır.",
             "ek": "Ama her rasyonel sayı tam sayı değildir: [[1/2]] bir tam sayı değildir. Doğal sayılar tam sayıların, tam sayılar da rasyonel sayıların içindedir. (s. 29–30)",
             "akilda": "Tam sayı = paydası 1",
             "soru": S("Hangisi rasyonel sayıdır ama tam sayı değildir?", ["[[7/8]]", "[[15/5]]", "[[-6/6]]"], 0,
                       "Sadeleştirince tam sayı çıkıyor mu, bak: 15 ÷ 5 = ?, 6 ÷ 6 = ?",
                       "[[15/5]] = 3 ve [[-6/6]] = −1 tam sayıdır. [[7/8]] ise 0 ile 1 arasındadır, tam sayı değildir. (s. 30)")},
            {"ad": "Eksi Bütüne Aittir", "renk": "#3274d6", "svg": svg_eksi_butun(),
             "aciklama": "[[-1 1/2]] sayısındaki eksi işareti yalnızca 1'e değil, sayının tamamına aittir. Yani [[-1 1/2]], [[1 1/2]]'nin negatifidir.",
             "ek": "Tam sayılı kesri çevirirken eksiyi kenara koy, sayıyı çevir, sonra eksiyi geri ekle: [[-1 1/2]] = [[-3/2]]. (s. 30)",
             "akilda": "Eksiyi kenara koy",
             "cozum": {"baslik": "Eksiyi kenara koyarak çevirelim", "problem": "[[-11/4]] sayısını tam sayılı kesre çevirelim.",
                       "adimlar": [
                           {"metin": "Eksi işaretini kenara koy. Şimdilik [[11/4]] ile çalışacağız.", "islem": f"{M} ( [[11/4]] )"},
                           {"metin": "11'i 4'e böl.", "islem": "11 ÷ 4 = 2, kalan 3"},
                           {"metin": "Bölüm tam kısım, kalan pay olur.", "islem": "[[11/4]] = [[2 3/4]]"},
                           {"metin": "Kenara koyduğun eksiyi geri ekle.", "islem": "[[-11/4]] = [[-2 3/4]]"}],
                       "sonuc": "[[-11/4]] = [[-2 3/4]]. Eksi, sayının tamamına aittir. (s. 30)"},
             "sende": {"baslik": "Şimdi sen çevir", "problem": "[[-7/3]] sayısını tam sayılı kesre çevirelim.",
                       "adimlar": [
                           {"metin": "Eksiyi kenara koy.", "islem": f"{M} ( [[7/3]] )"},
                           {"metin": "7'yi 3'e böl.",
                            "soru": G("7 ÷ 3 işleminde bölüm kaçtır?", "2", "3'ün kaç katı 7'yi geçmez? 3 × 2 = 6, 3 × 3 = 9.", "3 × 2 = 6. Bölüm 2."),
                            "islem": "7 ÷ 3 = 2, kalan ?"},
                           {"metin": "Kalanı bul.",
                            "soru": G("Kalan kaçtır?", "1", "7'den 6'yı çıkar.", "7 − 6 = 1. Kalan 1."),
                            "islem": "[[7/3]] = [[2 1/3]]"},
                           {"metin": "Eksiyi geri ekle.",
                            "soru": S("Sonuç hangisidir?", ["[[-2 1/3]]", "[[2 1/3]]", "[[-1 2/3]]"], 0,
                                      "Kenara koyduğun eksiyi unutma.", "Eksiyi geri ekleyince [[-2 1/3]] olur."),
                            "islem": "[[-7/3]] = [[-2 1/3]]"}],
                       "sonuc": "Harika! [[-7/3]] = [[-2 1/3]]."},
             "soru": S("[[-5/2]] hangi sayıya eşittir?", ["[[-2 1/2]]", "[[2 1/2]]", "[[-1 1/2]]"], 0,
                       "Eksiyi kenara koy. 5 ÷ 2 = 2, kalan 1. Sonra eksiyi geri ekle.", "[[5/2]] = [[2 1/2]], eksiyle [[-2 1/2]]. (s. 30)")},
            {"ad": "Sayı Doğrusunda Gösterme", "renk": "#1d6fa3", "svg": svg_sd_rasyonel(),
             "aciklama": "Bir rasyonel sayıyı sayı doğrusunda 4 adımda buluruz: 1) İşarete bak. 2) Hangi iki tam sayı arasında, bul. 3) O aralığı paydadaki sayı kadar eş parçaya böl. 4) Tam kısımdan başla, pay kadar ilerle.",
             "ek": "Sayı pozitifse sağa, negatifse sola ilerlenir. Her rasyonel sayının sayı doğrusunda bir yeri vardır. (s. 31–32)",
             "akilda": "İşaret, ara, böl, ilerle",
             "cozum": {"baslik": "[[7/4]] sayısını bulalım",
                       "adimlar": [
                           {"metin": "İşarete bak. [[7/4]] pozitif, sağa ilerleyeceğiz.", "islem": "Pozitif → sağa"},
                           {"metin": "Tam sayılı kesre çevir: 7 ÷ 4 = 1, kalan 3.", "islem": "[[7/4]] = [[1 3/4]] → 1 ile 2 arasında"},
                           {"metin": "1 ile 2 arasını payda kadar, yani 4 eş parçaya böl.", "sayiDogrusu": sd_kir(0, 3, 4), "islem": "4 eş parça"},
                           {"metin": "1'den başla, sağa 3 parça ilerle.",
                            "sayiDogrusu": sd_kir(0, 3, 4, oklar=[{"bas": 1, "son": 1.75, "etiket": "3 parça", "renk": POS}], isaretler=[{"x": 1.75, "etiket": "7/4", "renk": POS}]),
                            "islem": "[[7/4]] burada"}],
                       "sonuc": "[[7/4]] = [[1 3/4]], 1 ile 2 arasında, 1'den 3 parça sağdadır."},
             "sende": {"baslik": "Kitaptaki sayıyı sen bul", "problem": "[[-13/5]] sayısını sayı doğrusunda bulalım.",
                       "adimlar": [
                           {"metin": "İşarete bak.",
                            "soru": S("[[-13/5]] pozitif mi, negatif mi?", ["Negatif", "Pozitif", "İşareti yok"], 0, "Önünde eksi var mı?", "Önünde eksi var: negatif. Sola ilerleyeceğiz."),
                            "islem": "Negatif → sola"},
                           {"metin": "13 ÷ 5 = 2, kalan 3. Yani [[13/5]] = [[2 3/5]].",
                            "soru": S("O hâlde [[-13/5]] = [[-2 3/5]] hangi iki tam sayı arasındadır?", [f"{M}2 ile {M}3", "2 ile 3", f"{M}1 ile {M}2"], 0,
                                      f"Tam kısım {M}2. Negatif sayılarda bir sonraki tam sayı soldadır.", f"[[-2 3/5]], {M}2 ile {M}3 arasındadır."),
                            "islem": f"[[-13/5]] = [[-2 3/5]] → {M}2 ile {M}3 arası"},
                           {"metin": "Aralığı kaç eş parçaya böleceğiz?",
                            "soru": G("Aralık kaç eş parçaya bölünür?", "5", "Paydadaki sayıya bak.", "Payda 5: aralık 5 eş parçaya bölünür."),
                            "islem": "5 eş parça"},
                           {"metin": f"{M}2'den başla, sola 3 parça ilerle.",
                            "soru": N(f"{M}2'den sola doğru 3 küçük parça say ve o noktaya dokun.", -2.6, sd_kir(-3, 0, 5),
                                      f"Önce {M}2'yi bul. Sonra sola doğru küçük çizgileri say: 1, 2, 3.", f"{M}2'den sola 3 parça: [[-2 3/5]] = [[-13/5]]."),
                            "islem": "[[-13/5]] burada"}],
                       "sonuc": "Harika! [[-13/5]] sayısını kitaptaki 4 adımla buldun. (s. 32)"},
             "soru": N("[[3/4]] sayısının yerine dokun.", 0.75, sd_kir(0, 2, 4),
                       "0 ile 1 arası 4 eş parçaya bölündü. 0'dan sağa 3 küçük parça say.", "[[3/4]], 0'dan sağa 3 parçadadır. (s. 32)")},
            {"ad": "Eksinin Yeri", "renk": "#e8590c", "svg": svg_eksi_yer(),
             "aciklama": "Negatif bir rasyonel sayıda eksi işareti payda, paydada ya da kesir çizgisinin önünde olabilir. Sayının değeri değişmez.",
             "ek": "[[-9/3]], [[−9/3]] ve [[9/-3]] üçü de −3'e eşittir. Kitapta bunu hesap makinesiyle deniyorlar. (s. 33)",
             "akilda": "Eksi nerede olursa olsun aynı",
             "soru": S("Hangisi [[-6/2]] ile aynı değerdedir?", ["[[6/2]]", "[[6/-2]]", "[[-2/6]]"], 1,
                       "Eksinin yeri değişebilir ama sayılar aynı kalmalı: 6 ve 2.", "[[6/-2]] = −3 ve [[-6/2]] = −3. Eksinin yeri değeri değiştirmez. (s. 33)")}
        ],
        "biliyorMusun": [
            "Dünyada kişi başına düşen yenilenebilir tatlı su miktarının yaklaşık [[1/3]]'ü son 50 yılda azaldı. Bu yüzden suyu dikkatli kullanmalıyız. (s. 26)",
            "Kitaptaki su sayaçlarında [[3/6]], [[2/4]] ve [[1/2]] dolu bölmeler gösteriliyor. Üçü de sayı doğrusunda aynı noktadadır; yani üç öğrenci de suyun yarısını kullanmış. (s. 26–27)"],
        "akildaKalsin": [
            "İki tam sayı arasında başka tam sayı yoktur ama rasyonel sayılar vardır.",
            "Kesir şeklinde yazılabilen sayılar rasyonel sayıdır; paydası asla 0 olamaz.",
            "Her tam sayı bir rasyonel sayıdır: paydası 1'dir.",
            "[[-1 1/2]] sayısındaki eksi, sayının tamamına aittir.",
            "Sayı doğrusunda bulmak için: işaret, ara, böl, ilerle.",
            "Eksinin payda, paydada ya da kesrin önünde olması değeri değiştirmez."],
        "merakKutusu": [
            {"soru": "[[0/8]] bir rasyonel sayı mı?", "cevap": "Evet. 0'ı 8'e bölmek, 8 ile çarpınca 0 eden sayıyı aramaktır; bu sayı 0'dır. Yani [[0/8]] = 0. Pay 0 olabilir, payda olamaz. (s. 28)"},
            {"soru": "[[4/8]] ile [[1/2]] sayı doğrusunda aynı yerde mi?", "cevap": "Evet. Denk kesirler sayı doğrusunda aynı noktaya karşılık gelir. (s. 27)"},
            {"soru": "0,3 bir rasyonel sayı mı?", "cevap": "Evet. Ondalık gösterimi kesir şeklinde yazılabilen her sayı rasyonel sayıdır. (s. 28)"},
            {"soru": "Her rasyonel sayının sayı doğrusunda yeri var mı?", "cevap": "Evet. Her rasyonel sayı sayı doğrusunda bir noktaya karşılık gelir. (s. 31)"},
            {"soru": "[[-1 1/2]] ile [[-3/2]] aynı sayı mı?", "cevap": "Evet. Eksi bütüne aittir: [[1 1/2]] = [[3/2]], ikisinin de negatifi aynıdır. (s. 30)"}],
        "dusunVeYaz": [{"soru": "Bir rasyonel sayının paydası neden 0 olamaz? Kendi cümlelerinle anlat.",
                        "ornekCevap": "8'i 0'a bölersek, 0 ile çarpınca 8 eden bir sayı bulmamız gerekir. Ama 0 ile çarpılan her sayı 0 olur. Böyle bir sayı olmadığı için sonuç tanımsızdır.",
                        "anahtarlar": ["sıfır", "0", "çarp", "tanımsız"]}],
        "sorular": [
            S("Sayı doğrusunda 0 ile 1 arasında kaç tam sayı vardır?", ["1 tane", "2 tane", "Hiç yok"], 2,
              "Ardışık iki tam sayı arasında başka tam sayı olur mu?", "0 ile 1 ardışık tam sayılardır; aralarında başka tam sayı yoktur. (s. 25)"),
            N("[[1/4]] sayısının yerine dokun.", 0.25, sd_kir(0, 2, 4),
              "0 ile 1 arası 4 eş parçaya bölündü. 0'dan sağa 1 küçük parça say.", "[[1/4]], 0'dan sağa 1 parçadadır. (s. 32)"),
            S("Hangisi tanımsızdır?", ["[[0/7]]", "[[7/7]]", "[[7/0]]"], 2,
              "Paydası 0 olan bir kesir arıyoruz.", "[[7/0]] tanımsızdır; payda 0 olamaz. [[0/7]] = 0, [[7/7]] = 1. (s. 28)"),
            G("[[12/16]] kesrinin en sade hâlini yaz.", "3/4", "12 ve 16'nın ikisi de 4'e bölünür. Kesir çizgisi için / tuşunu kullan.",
              "12 ÷ 4 = 3, 16 ÷ 4 = 4. En sade hâl [[3/4]]. (s. 27)", kesir=True),
            S("Hangisi doğrudur?", ["Her rasyonel sayı bir tam sayıdır.", "Her tam sayı bir rasyonel sayıdır.", "[[1/2]] bir tam sayıdır."], 1,
              "Tam sayılar paydası kaç olan rasyonel sayılardır?", "Her tam sayı paydası 1 olan bir rasyonel sayıdır. Ama [[1/2]] gibi tam sayı olmayan rasyonel sayılar da vardır. (s. 29–30)"),
            G("[[20/5]] hangi tam sayıya eşittir?", "4", "20'yi 5'e böl.", "20 ÷ 5 = 4. Yani [[20/5]] = 4, bir tam sayıdır. (s. 30)"),
            N("[[-1/2]] sayısının yerine dokun.", -0.5, sd_kir(-2, 1, 2),
              "Negatif: 0'dan sola git. 0 ile −1 arası 2 eş parça; 1 parça say.", "[[-1/2]], 0'ın yarım birim solundadır. (s. 32)"),
            S("[[-7/4]] sayısı hangi iki tam sayı arasındadır?", ["1 ile 2", f"{M}1 ile {M}2", f"{M}2 ile {M}3"], 1,
              "Eksiyi kenara koy: 7 ÷ 4 = 1, kalan 3. Tam kısım kaç?", f"[[-7/4]] = [[-1 3/4]]. Bu sayı {M}1 ile {M}2 arasındadır. (s. 32)"),
            G("[[-1 2/3]] sayısını bileşik kesir olarak yaz.", "-5/3", "Eksiyi kenara koy. 1 × 3 + 2 = ? Payda 3 kalır. Sonra eksiyi geri ekle.",
              "1 × 3 + 2 = 5. [[1 2/3]] = [[5/3]], eksiyle [[-5/3]]. (s. 30)", kesir=True, kabul=["5/-3"]),
            S("Hangisi diğer ikisinden farklı bir sayıdır?", ["[[-8/2]]", "[[8/-2]]", "[[8/2]]"], 2,
              "Hangisinde hiç eksi yok?", "[[-8/2]] ve [[8/-2]] ikisi de −4'tür. [[8/2]] ise +4'tür. (s. 33)"),
            S("Bir su sayacının göstergesinde 4 eş bölmeden 2'si dolu. Kullanılan su, hakkın ne kadarıdır?", ["[[1/2]]", "[[2/2]]", "[[1/4]]"], 0,
              "Önce kesri yaz: 4 bölmeden 2'si. Sonra sadeleştir.", "4 bölmeden 2'si [[2/4]] = [[1/2]]. Suyun yarısı kullanılmış. (s. 26–27)"),
            G("A noktası hangi rasyonel sayıyı gösteriyor? Bileşik kesir olarak yaz.", "-11/4",
              f"A, {M}2'nin 3 parça solunda: [[-2 3/4]]. Bunu bileşik kesre çevir: 2 × 4 + 3 = ?",
              "A = [[-2 3/4]]. 2 × 4 + 3 = 11, yani A = [[-11/4]]. (s. 32)", kesir=True, denk=True, kabul=["11/-4"],
              sayiDogrusu=sd_kir(-3, 0, 4, isaretler=[{"x": -2.75, "etiket": "A", "renk": NEG}]))]
    }


# ---------- u1k3 çizimleri ----------
def svg_referans():
    g = "<rect x='20' y='90' width='80' height='16' rx='6' fill='#f5f6fa'/>" + txt(60, 102, "200 g", "#1b2340", 11)
    g += "<rect x='56' y='72' width='8' height='18' fill='#9aa3bf'/><rect x='28' y='66' width='64' height='8' rx='4' fill='#f5f6fa'/>"
    g += "<path d='M40 30 h40 l-4 36 h-32z' fill='#c98a4b'/><path d='M40 30 h40 l-2 7 h-36z' fill='#a8703b'/>" + txt(60, 56, "200 g", "#fff4e6", 11)
    g += "<path d='M60 30 V12' stroke='#f2c14e' stroke-width='2.5'/><path d='M60 12 l16 5 -16 5z' fill='#f2c14e'/>"
    return bg(g)


def svg_hata():
    g = "<line x1='10' y1='76' x2='110' y2='76' stroke='#f5f6fa' stroke-width='3'/>"
    for i in range(7):
        x = 18 + i * 14
        r = "#f2c14e" if i == 3 else "#f5f6fa"
        g += f"<line x1='{x}' y1='{70 if i != 3 else 66}' x2='{x}' y2='{82 if i != 3 else 86}' stroke='{r}' stroke-width='{2.5 if i != 3 else 3.5}'/>"
    g += txt(18, 100, "197", NB, 11) + txt(60, 100, "200", "#f2c14e", 12) + txt(102, 100, "203", OB, 11)
    g += f"<path d='M58 66 Q39 34 20 66' stroke='{NB}' stroke-width='3' fill='none' stroke-linecap='round'/><path d='M62 66 Q81 34 100 66' stroke='{OB}' stroke-width='3' fill='none' stroke-linecap='round'/>"
    g += txt(39, 40, "3 g", NB, 13) + txt(81, 40, "3 g", OB, 13)
    return bg(g)


def _sd_mini(y, vals, x0, adim, etiket=(), renk_etiket=True):
    """120×120 çizimlerde küçük yatay sayı doğrusu."""
    g = f"<line x1='8' y1='{y}' x2='112' y2='{y}' stroke='#f5f6fa' stroke-width='3'/>"
    for i, v in enumerate(vals):
        x = x0 + i * adim
        r = NB if v < 0 else OB if v > 0 else "#f2c14e"
        g += f"<line x1='{x}' y1='{y - 6}' x2='{x}' y2='{y + 6}' stroke='{r}' stroke-width='2.5'/>"
        if v in etiket:
            g += txt(x, y + 22, (M + str(-v)) if v < 0 else str(v), r, 12)
    return g


def svg_mutlak():
    g = txt(60, 46, f"|{M}3| = 3", "#f5f6fa", 24)
    g += _sd_mini(86, range(-3, 4), 24, 12, etiket=(-3, 0, 3))
    g += "<path d='M58 80 Q41 60 26 80' stroke='#f2c14e' stroke-width='3' fill='none' stroke-linecap='round'/><path d='M26 80 l2 -9 6 6z' fill='#f2c14e'/>"
    g += txt(42, 66, "3", "#f2c14e", 12)
    return bg(g)


def svg_ayna():
    g = _sd_mini(80, range(-4, 5), 12, 12, etiket=(-4, 0, 4))
    g += f"<path d='M58 72 Q35 40 12 72' stroke='{NB}' stroke-width='3' fill='none' stroke-linecap='round'/><path d='M62 72 Q85 40 108 72' stroke='{OB}' stroke-width='3' fill='none' stroke-linecap='round'/>"
    g += f"<circle cx='12' cy='80' r='6' fill='{NB}'/><circle cx='108' cy='80' r='6' fill='{OB}'/>"
    g += txt(34, 46, "4", NB, 16) + txt(86, 46, "4", OB, 16) + txt(60, 40, "=", "#f2c14e", 20)
    return bg(g)


def svg_eksi_yok():
    g = "<rect x='14' y='72' width='92' height='24' rx='4' fill='#f2c14e'/>"
    for i in range(11):
        x = 20 + i * 8
        g += f"<line x1='{x}' y1='72' x2='{x}' y2='{84 if i % 5 == 0 else 79}' stroke='#1b2340' stroke-width='2'/>"
    g += txt(30, 93, "0", "#1b2340", 9)
    g += f"<line x1='46' y1='36' x2='74' y2='36' stroke='{NB}' stroke-width='7' stroke-linecap='round'/>"
    g += "<circle cx='60' cy='36' r='22' fill='none' stroke='#ff6b6b' stroke-width='4.5'/><line x1='45' y1='51' x2='75' y2='21' stroke='#ff6b6b' stroke-width='4.5' stroke-linecap='round'/>"
    return bg(g)


def svg_iki_cevap():
    g = txt(60, 40, "| ? | = 4", "#f5f6fa", 20)
    g += _sd_mini(80, range(-4, 5), 12, 12, etiket=(-4, 0, 4))
    g += f"<circle cx='12' cy='80' r='7' fill='{NB}'/><circle cx='108' cy='80' r='7' fill='{OB}'/>"
    g += txt(12, 66, "?", NB, 14) + txt(108, 66, "?", OB, 14)
    return bg(g)


# =================================================================
def u1k3():
    sd = lambda mn, mx, **ek: dict({"min": mn, "max": mx}, **ek)
    kat = lambda mn, mx, **ek: dict({"min": mn, "max": mx, "dikey": True, "birim": 28, "sifirEtiketi": "Zemin kat"}, **ek)
    return {
        "id": "u1k3", "unite": "1. Tema: Sayılar ve Nicelikler", "baslik": "Mutlak Değer", "sayfalar": "s. 35–40",
        "giris": "Bir sayı 0'dan ne kadar uzakta? Bu konuda bunu ölçmeyi öğreneceğiz. Eksi ya da artı olması fark etmez; sadece kaç birim uzakta olduğuna bakacağız. Bu uzaklığa mutlak değer denir.",
        "hazirlik": {
            "baslik": "Hazır mısın?",
            "giris": "Bu konu, geçen iki konudaki sayı doğrusu bilgilerinin üzerine kuruluyor. Önce bunları hatırlıyor musun bakalım. Not yok; sadece nereden başlayacağımızı bulacağız.",
            "maddeler": [
                {"ad": "Eksi sayılar sayı doğrusunda", "sinif": "Geçen konu", "svg": svg_dogru(),
                 "anlatim": "Sayı doğrusunda 0'ın sağında pozitif sayılar, solunda negatif sayılar vardır. Eksi bir sayıyı bulmak için 0'dan sola doğru sayarız.",
                 "akilda": "Sol eksi, sağ artı",
                 "ornek": {"problem": f"{M}2'yi sayı doğrusunda bulalım.", "adimlar": [
                     {"metin": f"{M}2 eksi bir sayı. Eksi sayılar 0'ın solunda.", "islem": "Yön: sola"},
                     {"metin": "0'dan sola 2 aralık say.",
                      "sayiDogrusu": sd(-4, 4, oklar=[{"bas": 0, "son": -2, "etiket": "2 aralık", "renk": NEG}], isaretler=[{"x": -2, "etiket": f"{M}2", "renk": NEG}]),
                      "islem": f"0 → {M}2"}]},
                 "sorular": [
                     N(f"Sayı doğrusunda {M}4'ün yerine dokun.", -4, sd(-6, 6), "0'ı bul. Sola doğru 4 aralık say.", f"{M}4, 0'ın 4 birim solundadır."),
                     S("Hangisi sayı doğrusunda 0'ın solundadır?", ["5", f"{M}5", "0"], 1, "0'ın solunda eksi sayılar vardır.", f"{M}5 negatiftir, 0'ın solundadır.")]},
                {"ad": "İki sayı arasındaki uzaklık", "sinif": "Geçen konu", "svg": svg_uzaklik(),
                 "anlatim": "İki sayı arasındaki uzaklığı, sayı doğrusunda aradaki aralıkları sayarak buluruz. Uzaklık her zaman pozitif bir sayıdır.",
                 "akilda": "Aralıkları say",
                 "ornek": {"problem": f"0 ile {M}5 arasında kaç birim var?", "adimlar": [
                     {"metin": f"0'dan başla, {M}5'e kadar sola doğru aralıkları say: 1, 2, 3, 4, 5.",
                      "sayiDogrusu": sd(-6, 2, oklar=[{"bas": 0, "son": -5, "etiket": "5 aralık", "renk": NEG}])},
                     {"metin": "Uzaklık 5 birimdir. Uzaklığa eksi demeyiz.", "islem": "5 birim"}]},
                 "sorular": [
                     G(f"Sayı doğrusunda 0 ile {M}6 arasında kaç birim var?", "6", f"0'dan {M}6'ya kadar aralıkları say.", f"0 ile {M}6 arasında 6 aralık var: 6 birim.", birim="birim"),
                     G(f"Sayı doğrusunda {M}2 ile +3 arasında kaç birim var?", "5", f"{M}2'den 0'a kaç aralık? 0'dan +3'e kaç aralık? İkisini topla.", f"{M}2 → 0: 2 birim, 0 → +3: 3 birim. 2 + 3 = 5 birim.", birim="birim")]},
                {"ad": "Kesir ve ondalık sayıyı yerleştirme", "sinif": "Geçen konu", "svg": svg_sd_rasyonel(),
                 "anlatim": "Bir kesri ya da ondalık sayıyı sayı doğrusunda bulmak için önce işaretine bakarız, sonra hangi iki tam sayı arasında olduğunu buluruz. 1,5 sayısı 1 ile 2'nin tam ortasındadır.",
                 "akilda": "İşaret, ara, böl, ilerle",
                 "ornek": {"problem": "[[-1/2]] sayısını bulalım.", "adimlar": [
                     {"metin": "İşaret eksi: 0'dan sola gideceğiz.", "islem": "Yön: sola"},
                     {"metin": f"[[1/2]] yarım demek. 0 ile {M}1'in tam ortası.",
                      "sayiDogrusu": {"min": -2, "max": 1, "bolme": 2, "isaretler": [{"x": -0.5, "etiket": "−1/2", "renk": NEG}]},
                      "islem": f"[[-1/2]], 0 ile {M}1 arasında"}]},
                 "sorular": [
                     N("[[-1/2]] sayısının yerine dokun.", -0.5, {"min": -2, "max": 1, "bolme": 2},
                       f"Eksi: 0'dan sola. 0 ile {M}1 arası 2 eş parça; 1 parça say.", "[[-1/2]], 0'ın yarım birim solundadır."),
                     S(f"{M}1,5 hangi iki tam sayı arasındadır?", [f"1 ile 2", f"{M}1 ile {M}2", f"0 ile {M}1"], 1,
                       "Önce işarete bak: eksi. Sonra virgülden önceki sayıya bak: 1.", f"{M}1,5 sayısı {M}1 ile {M}2'nin tam ortasındadır.")]}
            ]},
        "kavramlar": [
            {"ad": "Başlangıç Noktası", "renk": "#1f9e8f", "svg": svg_referans(),
             "aciklama": "Bir şeyi ölçerken önce bir başlangıç noktası seçeriz. Kahve fabrikasında her paketin 200 gram olması isteniyor. Bu yüzden paketler 200 grama göre kontrol edilir.",
             "ek": "Başlangıç noktasına referans noktası da denir. Bazıları amaca göre değişir: çay paketinde 500 gram, şeker paketinde 1000 gram. Bazıları herkes için aynıdır: deniz seviyesi her zaman 0'dır. (s. 35–36)",
             "akilda": "Önce başlangıcı bul",
             "soru": S("Bir fabrikada her un paketinin 1000 gram olması isteniyor. Paketler hangi sayıya göre kontrol edilir?", ["1000 grama", "0 grama", "500 grama"], 0,
                       "Fabrika paketlerin kaç gram olmasını istiyor? Başlangıç noktası odur.",
                       "Hedef 1000 gram. Paketler 1000 grama göre kontrol edilir; 1000 gram başlangıç noktasıdır. (s. 36)")},
            {"ad": "Eksik ya da Fazla", "renk": "#7b4fc9", "svg": svg_hata(),
             "aciklama": "197 gramlık paket hedefin 3 gram eksiği, 203 gramlık paket 3 gram fazlası. İkisinin de hata miktarı 3 gramdır. Eksik ya da fazla olması fark etmez; sadece kaç birim uzakta olduğuna bakarız.",
             "ek": "Kitapta buna \"hata miktarı\" deniyor. Hata miktarı, başlangıç noktasına olan uzaklıktır. (s. 35–36)",
             "akilda": "Az ya da çok, uzaklık aynı",
             "cozum": {"baslik": "Hangi makine daha çok hata yaptı?",
                       "problem": "Kahve fabrikasında hedef 200 gram. 1. makinenin paketi 197 gram, 3. makinenin paketi 203 gram geldi. Hata miktarlarını karşılaştıralım.",
                       "adimlar": [
                           {"metin": "Başlangıç noktası nerede? Hedef kütle.", "islem": "Başlangıç = 200 g"},
                           {"metin": "197 gram, 200 gramdan kaç eksik?", "islem": "200 − 197 = 3 g eksik → hata 3 g"},
                           {"metin": "203 gram, 200 gramdan kaç fazla?", "islem": "203 − 200 = 3 g fazla → hata 3 g"},
                           {"metin": "Biri eksik, biri fazla. Ama ikisi de 200'e 3 gram uzakta.", "islem": "3 g = 3 g"}],
                       "sonuc": "İki makinenin hata miktarı eşit: 3 gram. Eksik ya da fazla olması hata miktarını değiştirmez. (s. 35)"},
             "soru": G("Hedef 200 gram. 199 gramlık paketin hata miktarı kaç gramdır?", "1",
                       "199 ile 200 arasında kaç gram var?", "200 − 199 = 1. Paket 1 gram eksik; hata miktarı 1 gram. (s. 35)", birim="g")},
            {"ad": "Mutlak Değer", "renk": "#3274d6", "svg": svg_mutlak(),
             "aciklama": "Bir sayının 0'a olan uzaklığına o sayının mutlak değeri denir. Sayı doğrusunda 0, bütün sayılar için ortak başlangıç noktasıdır.",
             "ek": f"Mutlak değer, sayının iki yanına dik çizgi çizerek gösterilir: |{M}3| = 3. Bu, \"{M}3'ün 0'a uzaklığı 3 birimdir\" demektir. (s. 37)",
             "akilda": "Mutlak değer = 0'a uzaklık",
             "sayiDogrusu": sd(-4, 4, oklar=[{"bas": 0, "son": -3, "etiket": "3 birim", "renk": NEG}], isaretler=[{"x": -3, "etiket": f"{M}3", "renk": NEG}]),
             "cozum": {"baslik": "Asansörle zemin kata uzaklık",
                       "problem": "Dört arkadaş bir AVM'nin zemin katında buluştu. Ece 2 kat aşağıdaki markete, Ahmet 2 kat yukarıdaki teknoloji mağazasına gitti. Zemin kata uzaklıklarını bulalım.",
                       "sayiDogrusu": kat(-3, 3, isaretler=[{"x": -2, "etiket": "Market (Ece)", "renk": NEG}, {"x": 2, "etiket": "Teknoloji (Ahmet)", "renk": POS}]),
                       "adimlar": [
                           {"metin": "Başlangıç (0) nerede? Zemin kat.", "islem": "Zemin kat = 0"},
                           {"metin": "Ece aşağı indi. Aşağı eksidir.", "islem": f"Ece: {M}2"},
                           {"metin": "Ahmet yukarı çıktı. Yukarı artıdır.", "islem": "Ahmet: +2"},
                           {"metin": "Zemin kata uzaklıkları kaç kat?", "islem": f"|{M}2| = 2   ve   |+2| = 2"}],
                       "sonuc": "Farklı katlara gittiler ama zemin kata uzaklıkları aynı: 2 kat. (s. 37)"},
             "sende": {"baslik": "Ada otoparka iniyor",
                       "problem": "Ada aynı AVM'de 3 kat aşağıdaki otoparka gitti. Ada'nın katını ve zemin kata uzaklığını bulalım.",
                       "sayiDogrusu": kat(-4, 3),
                       "adimlar": [
                           {"metin": "Ada asansörde hangi düğmeye basmalı?",
                            "soru": G("Otoparkın katını tam sayıyla yaz.", "-3", f"Aşağı eksidir. Önce {M} tuşuna, sonra sayıya dokun.", f"Zemin katın 3 kat altı: {M}3."),
                            "islem": f"Ada: {M}3"},
                           {"metin": "Otopark zemin kata kaç kat uzaklıkta?",
                            "soru": G("Zemin kata uzaklık kaç kat?", "3", "0'dan aşağı doğru aralıkları say. Uzaklığa eksi demeyiz.", "Otopark zemin kata 3 kat uzaklıkta.", birim="kat"),
                            "islem": "3 kat"},
                           {"metin": "Şimdi bunu mutlak değerle yaz.",
                            "soru": S("Hangisi doğrudur?", [f"|{M}3| = {M}3", f"|{M}3| = 3", f"|3| = {M}3"], 1,
                                      "Mutlak değer bir uzaklıktır. Uzaklık eksi olur mu?", f"{M}3'ün 0'a uzaklığı 3'tür: |{M}3| = 3."),
                            "islem": f"|{M}3| = 3"}],
                       "sonuc": f"Harika! Ada'nın katı {M}3, zemin kata uzaklığı |{M}3| = 3 kat. (s. 37)"},
             "soru": G(f"|{M}7| kaçtır?", "7", f"{M}7, 0'dan kaç birim uzakta? Sayı doğrusunda aralıkları say.",
                       f"{M}7'nin 0'a uzaklığı 7 birimdir: |{M}7| = 7. (s. 37)", sayiDogrusu=sd(-8, 1, isaretler=[{"x": -7, "etiket": f"{M}7", "renk": NEG}]))},
            {"ad": "Eksi de Artı da Aynı", "renk": "#e8590c", "svg": svg_ayna(),
             "aciklama": f"{M}4 ve +4, 0'ın iki yanında, 0'a aynı uzaklıktadır. Bu yüzden mutlak değerleri aynıdır: |{M}4| = |+4| = 4.",
             "ek": f"Kolay yol: İşareti sil, sayı kalır. Kesirde ve ondalık sayıda da aynısı olur: |[[-15/8]]| = [[15/8]], |{M}1,5| = 1,5. (s. 37–38)",
             "akilda": "İşareti sil, sayı kalır",
             "sayiDogrusu": sd(-5, 5, isaretler=[{"x": -4, "etiket": f"{M}4", "renk": NEG}, {"x": 4, "etiket": "+4", "renk": POS}]),
             "soru": S(f"|{M}9| ile |+9| için hangisi doğrudur?", [f"|{M}9| daha küçüktür.", "İkisi de 9'dur.", f"|{M}9| = {M}9"], 1,
                       f"{M}9 ve +9, 0'a kaçar birim uzakta?", f"{M}9 ve +9 0'a eşit uzaklıkta: |{M}9| = |+9| = 9. (s. 37)")},
            {"ad": "Mutlak Değer Eksi Olmaz", "renk": "#c92a2a", "svg": svg_eksi_yok(),
             "aciklama": "Uzaklık eksi olamaz. Bu yüzden bir sayının mutlak değeri ya 0 ya da pozitif bir sayıdır. Sıfırın mutlak değeri sıfırdır: |0| = 0.",
             "ek": f"Sondaj makinesi yer yüzeyinin 8,6 metre altında suya ulaştı. Konumu {M}8,6 m'dir ama yüzeye uzaklığı |{M}8,6| = 8,6 m'dir. (s. 37–38)",
             "akilda": "Mutlak değer hiç eksi olmaz",
             "soru": S("Hangisi doğrudur?", [f"|{M}6| = {M}6", "|0| = 1", f"|{M}6| = 6"], 2,
                       "Mutlak değer bir uzaklıktır. 0'ın uzaklığı kaçtır, eksi bir uzaklık olur mu?",
                       f"|{M}6| = 6 ve |0| = 0. Mutlak değer hiç eksi olmaz. (s. 37)")},
            {"ad": "Mutlak Değeri Verilen Sayı", "renk": "#1d6fa3", "svg": svg_iki_cevap(),
             "aciklama": "Mutlak değeri 4 olan sayıyı arıyorsak 0'a 4 birim uzaklıktaki sayıları buluruz. İki tane vardır: biri sağda (+4), biri solda (−4).",
             "ek": "Yalnızca 0'ın mutlak değeri 0'dır. Mutlak değeri eksi olan bir sayı ise yoktur, çünkü uzaklık eksi olmaz. (s. 37–38)",
             "akilda": "İki cevap: sağda ve solda",
             "cozum": {"baslik": "Üçgen hangi sayı olabilir?",
                       "problem": "Kitapta bir sayı üçgenle gösterilmiş ve mutlak değeri 12 verilmiş: |▲| = 12. Üçgen hangi sayılar olabilir?",
                       "adimlar": [
                           {"metin": "|▲| = 12 ne demek? Üçgen, 0'a 12 birim uzaklıkta.", "islem": "0'a uzaklık: 12"},
                           {"metin": "0'ın sağında, 12 birim uzakta hangi sayı var?", "islem": "▲ = +12"},
                           {"metin": "0'ın solunda, 12 birim uzakta hangi sayı var?", "islem": f"▲ = {M}12"},
                           {"metin": "İki cevabı birlikte yaz.", "islem": f"▲ = 12   ya da   ▲ = {M}12"}],
                       "sonuc": f"Mutlak değeri 12 olan iki sayı vardır: 12 ve {M}12. (s. 38)"},
             "sende": {"baslik": "Kenan aracını nereye park etti?",
                       "problem": "Çok katlı bir otoparkta giriş zemin kat kabul ediliyor; zeminin üstünde de altında da katlar var. Kenan aracını zemine 3 kat uzaklıktaki bir kata park etti. Hangi katlarda olabilir?",
                       "sayiDogrusu": kat(-4, 4, sifirEtiketi="Zemin kat (giriş)"),
                       "adimlar": [
                           {"metin": "Zeminin 3 kat üstü hangi kat?",
                            "soru": G("Zeminin 3 kat üstündeki katı yaz.", "3", "Yukarı artıdır. 0'dan yukarı 3 aralık say.", "Zeminin 3 kat üstü +3. kattır."),
                            "islem": "+3"},
                           {"metin": "Zeminin 3 kat altı hangi kat?",
                            "soru": G("Zeminin 3 kat altındaki katı yaz.", "-3", f"Aşağı eksidir. Önce {M} tuşuna dokun.", f"Zeminin 3 kat altı {M}3. kattır."),
                            "islem": f"{M}3"},
                           {"metin": "Kenan hangi katlarda olabilir?",
                            "soru": S("Doğru cevap hangisi?", ["Yalnız +3. kat", f"Yalnız {M}3. kat", f"+3. kat ya da {M}3. kat"], 2,
                                      "Zemine 3 kat uzaklıkta kaç kat var? Yukarıyı da aşağıyı da düşün.", f"İki kat da zemine 3 kat uzaklıkta: +3 ve {M}3."),
                            "islem": f"+3 ya da {M}3"}],
                       "sonuc": f"Harika! Zemine 3 kat uzaklıkta iki kat var: +3 ve {M}3. (s. 40)"},
             "soru": N("Mutlak değeri 2 olan negatif sayının yerine dokun.", -2, sd(-5, 5),
                       f"Mutlak değeri 2 olan sayılar 0'a 2 birim uzakta. Negatif olan 0'ın solundadır.", f"|{M}2| = 2 ve {M}2 negatiftir. (s. 37–38)")}
        ],
        "biliyorMusun": [
            "Marketteki birçok paketin üzerinde kütlenin yanında küçük bir \"e\" işareti vardır. Bu işaret, paketin kurallara uygun hazırlandığını gösterir. Kurallara göre 100 gramlık bir paket en fazla 4,5 gram eksik olabilir. (s. 35)",
            "Kitapta Ömer, saatlerinin ne kadar ileri ya da geri olduğunu TÜBİTAK Ulusal Metroloji Enstitüsünün (UME) gösterdiği saate göre kontrol ediyor. Doğru saat orada başlangıç noktasıdır. (s. 36)"],
        "akildaKalsin": [
            "Ölçmeden önce başlangıç (referans) noktasını bul.",
            "Eksik ya da fazla olması fark etmez; uzaklık aynıdır.",
            "Bir sayının 0'a uzaklığına mutlak değer denir.",
            f"|{M}4| = |+4| = 4: İşareti sil, sayı kalır.",
            "Mutlak değer hiç eksi olmaz. |0| = 0.",
            f"Mutlak değeri 4 olan iki sayı vardır: 4 ve {M}4."],
        "merakKutusu": [
            {"soru": "Mutlak değer neden hiç eksi olmuyor?", "cevap": "Çünkü mutlak değer bir uzaklıktır. \"Okul evime eksi 3 km uzakta\" demeyiz. Uzaklık ya 0'dır ya da pozitiftir. (s. 37)"},
            {"soru": f"|{M}3| nasıl okunur?", "cevap": f"\"Eksi üçün mutlak değeri\" diye okunur. Sonucu 3'tür: |{M}3| = 3."},
            {"soru": "Başlangıç noktası hep 0 mı?", "cevap": "Hayır. Çay fabrikasında başlangıç 500 gram, şeker fabrikasında 1000 gram olabilir. Ama sayı doğrusunda ve deniz seviyesinde başlangıç 0'dır. (s. 36–37)"},
            {"soru": "Mutlak değeri aynı olan iki sayı nerede durur?", "cevap": f"Sayı doğrusunda 0'ın iki yanında, 0'a eşit uzaklıkta dururlar: {M}5 ve +5 gibi. (s. 37)"},
            {"soru": "Kesirlerin de mutlak değeri olur mu?", "cevap": "Evet. Her rasyonel sayının 0'a bir uzaklığı vardır: |[[-15/8]]| = [[15/8]]. (s. 37)"}],
        "dusunVeYaz": [{"soru": "Günlük hayattan bir başlangıç noktası örneği yaz. Bir şeyin bu noktaya ne kadar uzak olduğunu anlat.",
                        "ornekCevap": f"Termometrede 0 °C başlangıç noktasıdır. Hava {M}5 °C olunca sıcaklık 0 °C'a 5 derece uzaktadır: |{M}5| = 5.",
                        "anahtarlar": ["başlangıç", "uzak", "0", "referans"]}],
        "sorular": [
            G(f"|{M}8| kaçtır?", "8", f"{M}8, 0'dan kaç birim uzakta?", f"{M}8'in 0'a uzaklığı 8 birimdir: |{M}8| = 8. (s. 37)"),
            S("Kahve fabrikasında hedef 200 gram. Hangi paketin hata miktarı daha büyüktür?", ["197 gramlık paket", "205 gramlık paket", "İkisi eşittir"], 1,
              "Her paketin 200'e kaç gram uzak olduğunu bul: 200 − 197 = ?, 205 − 200 = ?",
              "197 gram → 3 gram eksik, hata 3 g. 205 gram → 5 gram fazla, hata 5 g. 5 > 3. (s. 35)"),
            N("Mutlak değeri 3 olan pozitif sayının yerine dokun.", 3, sd(-5, 5),
              "0'a 3 birim uzakta iki sayı var. Pozitif olan 0'ın sağındadır.", "|+3| = 3 ve +3 pozitiftir. (s. 37)"),
            G("Bir sondaj makinesi yer yüzeyinin 8,6 metre altında suya ulaştı. Makinenin konumunu yaz.", "-8,6",
              f"\"Altında\" eksi demek. Önce {M} tuşuna, sonra 8, virgül ve 6'ya dokun.", f"Yüzeyin 8,6 m altı: {M}8,6 m. (s. 38)", birim="m"),
            G(f"Sondaj makinesinin konumu {M}8,6 m. Bu konumun yer yüzeyine uzaklığı kaç metredir?", "8,6",
              f"Uzaklık mutlak değerdir: |{M}8,6| = ? Uzaklık eksi olur mu?", f"|{M}8,6| = 8,6. Makine yüzeye 8,6 m uzaktadır. (s. 38)", birim="m"),
            S("Mutlak değeri 5 olan sayılar hangileridir?", ["Yalnız 5", f"Yalnız {M}5", f"5 ve {M}5"], 2,
              "0'a 5 birim uzaklıkta kaç sayı var? Sağa ve sola bak.", f"0'ın sağında 5, solunda {M}5 var. İkisinin de mutlak değeri 5'tir. (s. 38)"),
            G("|[[-3/4]]| kaçtır? Kesir olarak yaz.", "3/4", "İşareti sil, sayı kalır. Kesir çizgisi için / tuşunu kullan.",
              "|[[-3/4]]| = [[3/4]]. Mutlak değer hiç eksi olmaz. (s. 37–38)", kesir=True),
            G("UME'ye göre saat 14.00. Ömer'in kol saati 14.05'i gösteriyor. Kol saati kaç dakika hatalı?", "5",
              "Saat 14.00'ten kaç dakika ileride?", "14.05 − 14.00 = 5. Kol saati 5 dakika ileride; hata 5 dakikadır. (s. 36)", birim="dakika"),
            N("0'a 4 birim uzaklıktaki negatif sayıya dokun.", -4, sd(-6, 6),
              "0'dan sola doğru 4 aralık say.", f"0'ın 4 birim solunda {M}4 vardır: |{M}4| = 4. (s. 37)"),
            S("Mutlak değeri 3'ten küçük olan tam sayılar hangileridir?", ["0, 1, 2", f"{M}2, {M}1, 0, 1, 2", f"{M}3, {M}2, {M}1, 0, 1, 2, 3"], 1,
              f"0'a uzaklığı 0, 1 ya da 2 olan sayıları düşün. Eksi sayıları unutma. 3 ve {M}3'ün mutlak değeri 3'ten küçük mü?",
              f"|{M}2| = 2, |{M}1| = 1, |0| = 0, |1| = 1, |2| = 2. 3 ve {M}3'ün mutlak değeri 3'tür, 3'ten küçük değildir. (s. 38)"),
            S("AVM'nin zemin katından Ahmet 2 kat yukarı, Ece 2 kat aşağı gitti. Hangisi doğrudur?",
              ["Zemin kata uzaklıkları eşittir: 2 kat.", "Ahmet zemin kata daha uzaktır.", f"Ece'nin zemin kata uzaklığı {M}2 kattır."], 0,
              "İkisi de zeminden kaç kat uzaklaştı? Uzaklık eksi olur mu?", "İkisi de zemin kata 2 kat uzaktadır. Uzaklık eksi olmaz. (s. 37)"),
            G("Bir çay fabrikasında hedef 500 gram. Bir paket 496 gram geldi. Hata miktarı kaç gramdır?", "4",
              "Başlangıç noktası 500 gram. 496 ile 500 arasında kaç gram var?", "500 − 496 = 4. Hata miktarı 4 gramdır. (s. 36)", birim="g")]
    }


# ---------- u1k4 çizimleri ----------
def devir_svg(x, y, tam, devir, renk="#f5f6fa", boy=20):
    """SVG içinde devirli ondalık: tam kısım + üstü çizili devreden rakamlar (sola yaslı)."""
    g = txt(x, y, tam, renk, boy, hiza="start")
    gen = boy * 0.62
    x2 = x + len(tam) * gen
    g += txt(x2, y, devir, renk, boy, hiza="start")
    g += f"<line x1='{x2 + 1}' y1='{y - boy * 0.82}' x2='{x2 + len(devir) * gen - 1}' y2='{y - boy * 0.82}' stroke='{renk}' stroke-width='2.4' stroke-linecap='round'/>"
    return g


def svg_h_ondalik():
    g = "<rect x='14' y='26' width='92' height='40' rx='8' fill='#2b355c'/>"
    g += txt(28, 56, "0", "#f5f6fa", 24) + txt(44, 56, ",", "#f2c14e", 24) + txt(62, 56, "2", OB, 24) + txt(86, 56, "5", NB, 24)
    g += txt(62, 82, "onda", OB, 10) + txt(86, 82, "yüzde", NB, 10)
    g += txt(60, 106, "= 25/100", "#f5f6fa", 14)
    return bg(g)


def svg_h_genislet():
    g = kesir_svg(26, 48, "1", "4", "#f5f6fa", 20) + kesir_svg(94, 48, "25", "100", "#f5f6fa", 18)
    g += "<path d='M44 58 Q60 40 74 58' stroke='#f2c14e' stroke-width='3' fill='none' stroke-linecap='round'/><path d='M74 58 l-1 -9 -6 5z' fill='#f2c14e'/>"
    g += txt(60, 36, "×25", "#f2c14e", 13) + txt(60, 104, "üstü ve altı", "#9aa3bf", 10)
    return bg(g)


def svg_h_bolunme():
    g = f"<circle cx='36' cy='46' r='22' fill='{OB}'/>" + txt(36, 54, "2", "#1b2340", 24)
    g += f"<circle cx='84' cy='46' r='22' fill='{NB}'/>" + txt(84, 54, "5", "#1b2340", 24)
    g += txt(36, 92, "çift", "#f5f6fa", 11) + txt(84, 92, "0 ya da 5", "#f5f6fa", 11)
    g += txt(60, 110, "son rakama bak", "#9aa3bf", 10)
    return bg(g)


def svg_bolme():
    g = kesir_svg(30, 54, "1", "5", "#f5f6fa", 26)
    g += txt(60, 64, "=", "#f2c14e", 22)
    g += txt(92, 64, "1÷5", "#f5f6fa", 20)
    g += "<rect x='22' y='86' width='76' height='22' rx='11' fill='#f2c14e'/>" + txt(60, 102, "= 0,2", "#1b2340", 14)
    return bg(g)


def svg_onluk():
    g = ""
    for r in range(10):
        for c in range(10):
            g += f"<rect x='{20 + c * 8}' y='{14 + r * 8}' width='7' height='7' fill='{OB if r * 10 + c < 25 else '#2b355c'}'/>"
    g += txt(60, 108, "25/100 = 0,25", "#f5f6fa", 13)
    return bg(g)


def svg_sonlu():
    g = "<rect x='14' y='30' width='92' height='36' rx='10' fill='#2b355c'/>" + txt(56, 56, "0,25", "#f5f6fa", 24)
    g += "<circle cx='92' cy='48' r='9' fill='#5fd08f'/><path d='M87 48 l4 4 7 -8' stroke='#1b2340' stroke-width='3' fill='none' stroke-linecap='round'/>"
    g += txt(60, 92, "bölme bitti", "#5fd08f", 13)
    return bg(g)


def svg_devir():
    g = devir_svg(22, 58, "0,", "3", "#f5f6fa", 30)
    g += txt(78, 58, "=", "#f2c14e", 22)
    g += txt(60, 92, "0,3333…", NB, 16)
    g += f"<path d='M88 30 a14 14 0 1 1 -4 -10' stroke='{NB}' stroke-width='3' fill='none' stroke-linecap='round'/><path d='M84 20 l-1 -8 8 4z' fill='{NB}'/>"
    return bg(g)


def svg_25():
    g = kesir_svg(30, 40, "7", "20", "#f5f6fa", 18)
    g += txt(66, 34, "20 ÷ 2 = 10", "#f5f6fa", 9, 700) + txt(66, 48, "10 ÷ 2 = 5", "#f5f6fa", 9, 700) + txt(66, 62, "5 ÷ 5 = 1", "#f5f6fa", 9, 700)
    g += "<rect x='22' y='80' width='76' height='24' rx='12' fill='#5fd08f'/>" + txt(60, 97, "1 kaldı: sonlu", "#1b2340", 11)
    return bg(g)


def svg_ond_kesir():
    g = txt(60, 42, "1,32", "#f5f6fa", 24)
    g += "<path d='M60 52 v14' stroke='#f2c14e' stroke-width='3'/><path d='M60 70 l-5 -7 h10z' fill='#f2c14e'/>"
    g += kesir_svg(60, 90, "132", "100", "#f5f6fa", 16)
    return bg(g)


def svg_dev_kesir():
    g = devir_svg(16, 50, "0,", "3", "#f5f6fa", 26)
    g += txt(64, 50, "=", "#f2c14e", 22) + kesir_svg(92, 42, "3", "9", "#f5f6fa", 22)
    g += "<rect x='16' y='86' width='88' height='22' rx='11' fill='#2b355c'/>" + txt(60, 101, "devreden → 9", "#f2c14e", 11)
    return bg(g)


# =================================================================
def u1k4():
    sd = lambda mn, mx, bol, **ek: dict({"min": mn, "max": mx, "bolme": bol}, **ek)
    return {
        "id": "u1k4", "unite": "1. Tema: Sayılar ve Nicelikler", "baslik": "Rasyonel Sayıların Farklı Gösterimleri", "sayfalar": "s. 41–49",
        "giris": "Bir sayıyı iki türlü yazabiliriz: kesirle ([[1/5]]) ya da virgülle (0,2). Bu konuda kesirleri ondalık gösterime, ondalık gösterimleri kesre çevireceğiz. Bazı bölmelerin hiç bitmediğini de göreceğiz!",
        "hazirlik": {
            "baslik": "Hazır mısın?",
            "giris": "Bu konu ondalık sayılar, genişletme ve sadeleştirme bilgilerinin üzerine kuruluyor. Önce bunları hatırlıyor musun bakalım. Not yok; sadece nereden başlayacağımızı bulacağız.",
            "maddeler": [
                {"ad": "Ondalık gösterim ve basamaklar", "sinif": "Önceki yıllar", "svg": svg_h_ondalik(),
                 "anlatim": "Virgülden sonraki ilk basamak onda birler, ikinci basamak yüzde birler basamağıdır. 0,7 = [[7/10]], yani onda yedi. 0,25 = [[25/100]], yani yüzde yirmi beş.",
                 "akilda": "1 basamak = 10, 2 basamak = 100",
                 "ornek": {"problem": "0,25 sayısını kesir olarak yazalım.", "adimlar": [
                     {"metin": "Virgülden sonra kaç basamak var? 2 basamak: 2 ve 5.", "islem": "2 basamak"},
                     {"metin": "2 basamak varsa payda 100 olur.", "islem": "Payda = 100"},
                     {"metin": "Virgülü sil, sayıyı paya yaz.", "islem": "0,25 = [[25/100]]"}]},
                 "sorular": [
                     S("0,3 hangi kesre eşittir?", ["[[3/10]]", "[[3/100]]", "[[1/3]]"], 0,
                       "Virgülden sonra 1 basamak var. 1 basamak olunca payda kaç olur?", "0,3 = onda üç = [[3/10]]."),
                     G("[[45/100]] kesrini ondalık gösterimle yaz.", "0,45", "Payda 100: virgülden sonra 2 basamak olur. Önce 0, sonra virgül.",
                       "[[45/100]] = yüzde kırk beş = 0,45.", denk=True)]},
                {"ad": "Genişletme", "sinif": "Önceki yıllar", "svg": svg_h_genislet(),
                 "anlatim": "Bir kesrin payını ve paydasını aynı sayıyla çarparsak kesrin değeri değişmez. Buna genişletme denir: [[1/4]] = [[25/100]].",
                 "akilda": "Üstü ve altı aynı sayıyla çarp",
                 "ornek": {"problem": "[[3/5]] kesrinin paydasını 10 yapalım.", "adimlar": [
                     {"metin": "5'i kaçla çarparsak 10 olur?", "islem": "5 × 2 = 10"},
                     {"metin": "Payı da aynı sayıyla çarp.", "islem": "3 × 2 = 6"},
                     {"metin": "Yeni kesri yaz.", "islem": "[[3/5]] = [[6/10]]"}]},
                 "sorular": [
                     S("[[2/5]] kesrinin paydası 10 olan denki hangisidir?", ["[[2/10]]", "[[4/10]]", "[[5/10]]"], 1,
                       "5 × 2 = 10. Payı da 2 ile çarp.", "2 × 2 = 4, 5 × 2 = 10: [[2/5]] = [[4/10]]."),
                     G("[[1/4]] kesrinin paydasını 100 yapmak için pay ve paydayı kaçla çarparız?", "25", "4 × ? = 100. 25'er 25'er say: 25, 50, 75, 100.",
                       "4 × 25 = 100. Pay ve payda 25 ile çarpılır: [[1/4]] = [[25/100]].")]},
                {"ad": "Sadeleştirme", "sinif": "Önceki yıllar", "svg": svg_h_denk(),
                 "anlatim": "Pay ve paydayı aynı sayıya bölersek kesrin değeri değişmez. Artık birlikte bölünemiyorlarsa kesir en sade hâlindedir: [[6/10]] = [[3/5]].",
                 "akilda": "Üstü ve altı aynı sayıya böl",
                 "ornek": {"problem": "[[25/100]] kesrini sadeleştirelim.", "adimlar": [
                     {"metin": "25 ve 100'ün ikisi de 25'e bölünür.", "islem": "25 ÷ 25 = 1   ve   100 ÷ 25 = 4"},
                     {"metin": "Yeni kesri yaz. 1 ve 4 birlikte bölünemez: en sade hâl.", "islem": "[[25/100]] = [[1/4]]"}]},
                 "sorular": [
                     S("[[6/10]] kesrinin en sade hâli hangisidir?", ["[[3/5]]", "[[6/5]]", "[[1/2]]"], 0,
                       "6 ve 10'un ikisi de 2'ye bölünür.", "6 ÷ 2 = 3, 10 ÷ 2 = 5: [[3/5]]."),
                     G("[[50/100]] kesrinin en sade hâlini yaz.", "1/2", "50 ve 100'ün ikisi de 50'ye bölünür. Kesir çizgisi için / tuşunu kullan.",
                       "50 ÷ 50 = 1, 100 ÷ 50 = 2: [[1/2]].", kesir=True)]},
                {"ad": "2'ye ve 5'e bölünebilme", "sinif": "Önceki yıllar", "svg": svg_h_bolunme(),
                 "anlatim": "Son rakamı çift olan (0, 2, 4, 6, 8) sayılar 2'ye tam bölünür. Son rakamı 0 ya da 5 olan sayılar 5'e tam bölünür.",
                 "akilda": "Son rakama bak",
                 "ornek": {"problem": "40 sayısı 2'ye ve 5'e bölünür mü?", "adimlar": [
                     {"metin": "Son rakam 0. 0 çift bir rakamdır: 2'ye bölünür.", "islem": "40 ÷ 2 = 20"},
                     {"metin": "Son rakam 0: 5'e de bölünür.", "islem": "40 ÷ 5 = 8"}]},
                 "sorular": [
                     S("Hangisi 5'e tam bölünür?", ["12", "25", "33"], 1, "Son rakamı 0 ya da 5 olan sayıyı ara.", "25'in son rakamı 5: 25 ÷ 5 = 5."),
                     S("Hangisi 2'ye tam bölünür?", ["15", "9", "14"], 2, "Son rakamı çift olan sayıyı ara.", "14'ün son rakamı 4, çifttir: 14 ÷ 2 = 7.")]}
            ]},
        "kavramlar": [
            {"ad": "Kesir Çizgisi Bölmedir", "renk": "#1f9e8f", "svg": svg_bolme(),
             "aciklama": "Kesir çizgisi bölme demektir: [[1/5]] = 1 ÷ 5. Payı paydaya bölersek sayının virgüllü yazılışını, yani ondalık gösterimini buluruz.",
             "ek": "Kitaptaki kutu sütün hacmi [[1/5]] L. 1 ÷ 5 = 0,2 olduğu için sütün hacmi 0,2 L'dir. Aynı sayının iki farklı gösterimi: [[1/5]] = 0,2. (s. 41)",
             "akilda": "Çizgi = bölme",
             "cozum": {"baslik": "[[1/2]] kaç eder?", "problem": "[[1/2]] kesrini ondalık gösterimle yazalım.",
                       "adimlar": [
                           {"metin": "Kesir çizgisi bölmedir. Payı paydaya böleceğiz.", "islem": "[[1/2]] = 1 ÷ 2"},
                           {"metin": "1'in içinde 2 yok. Bölüme 0 yaz, virgül koy, 1'in yanına 0 ekle: 10 oldu.", "islem": "0,…   10 ÷ 2"},
                           {"metin": "10'un içinde 2 tam 5 kere var. Kalan 0: bölme bitti.", "islem": "10 ÷ 2 = 5   →   0,5"}],
                       "sonuc": "[[1/2]] = 0,5. Yarım, onda beş demektir."},
             "soru": S("[[3/4]] kesrindeki kesir çizgisi hangi işlemi gösterir?", ["3 × 4", "4 − 3", "3 ÷ 4"], 2,
                       "Kesir çizgisi hangi işlem demekti? Pay, paydaya …", "Kesir çizgisi bölmedir: [[3/4]] = 3 ÷ 4 = 0,75. (s. 41)")},
            {"ad": "Paydayı 10, 100, 1000 Yap", "renk": "#e8590c", "svg": svg_onluk(),
             "aciklama": "Paydayı genişletip 10, 100 ya da 1000 yapabiliyorsak ondalık gösterimi bulmak çok kolaydır: [[1/4]] = [[25/100]] = 0,25.",
             "ek": "Payda 10 ise virgülden sonra 1 basamak, 100 ise 2 basamak, 1000 ise 3 basamak olur. Kitaptaki madenî para [[1/4]] cm kalınlığında: 0,25 cm. (s. 41, 44)",
             "akilda": "10, 100, 1000'e genişlet",
             "cozum": {"baslik": "[[7/20]] kesrini çevirelim", "problem": "[[7/20]] kesrini ondalık gösterimle yazalım.",
                       "adimlar": [
                           {"metin": "20'yi kaçla çarparsak 10, 100 ya da 1000 olur? 20 × 5 = 100.", "islem": "20 × 5 = 100"},
                           {"metin": "Payı da 5 ile çarp.", "islem": "7 × 5 = 35"},
                           {"metin": "Yeni kesir: [[35/100]]. Payda 100: virgülden sonra 2 basamak.", "islem": "[[7/20]] = [[35/100]] = 0,35"}],
                       "sonuc": "[[7/20]] = 0,35. Paydayı 100 yapınca iş kolaylaştı."},
             "sende": {"baslik": "Şimdi sen çevir", "problem": "[[3/25]] kesrini ondalık gösterimle yazalım.",
                       "adimlar": [
                           {"metin": "Paydayı 100 yapmak için 25'i kaçla çarpmalıyız?",
                            "soru": G("25 × ? = 100", "4", "25'er 25'er say: 25, 50, 75, 100. Kaç kere saydın?", "25 × 4 = 100."),
                            "islem": "25 × 4 = 100"},
                           {"metin": "Payı da aynı sayıyla çarp.",
                            "soru": G("3 × 4 kaçtır? Yeni payı yaz.", "12", "3'ü 4 kere topla: 3 + 3 + 3 + 3.", "3 × 4 = 12. Yeni kesir [[12/100]]."),
                            "islem": "[[3/25]] = [[12/100]]"},
                           {"metin": "Payda 100: virgülden sonra 2 basamak.",
                            "soru": G("[[12/100]] kesrini ondalık gösterimle yaz.", "0,12", "Önce 0, sonra virgül, sonra 1 ve 2.", "[[12/100]] = 0,12.", denk=True),
                            "islem": "0,12"}],
                       "sonuc": "Harika! [[3/25]] = [[12/100]] = 0,12."},
             "soru": G("[[3/5]] kesrini ondalık gösterimle yaz.", "0,6", "5'i 10 yapmak için 2 ile çarp. Payı da 2 ile çarp.",
                       "[[3/5]] = [[6/10]] = 0,6. (s. 44)", denk=True)},
            {"ad": "Sonlu Ondalık Gösterim", "renk": "#2f9e44", "svg": svg_sonlu(),
             "aciklama": "Bazı bölmeler bir yerde biter. Virgülden sonra belli sayıda basamak kalır: 0,2 ya da 0,25 gibi. Buna sonlu ondalık gösterim denir.",
             "ek": "Kitapta [[72/15]] TL'lik fon kartonu 4,8 TL, [[185/2]] g'lık el sabunu 92,5 g ediyor. İkisinde de bölme bitiyor. (s. 41–42)",
             "akilda": "Bölme biter = sonlu",
             "soru": S("Hangisi sonlu ondalık gösterimdir?", ["0,333…", "0,75", "0,1666…"], 1,
                       "Hangisinde rakamlar bitiyor, sonunda üç nokta yok?", "0,75'te bölme bitmiş: sonludur. Üç noktalılarda rakamlar hiç bitmez. (s. 42)")},
            {"ad": "Devirli Ondalık Gösterim", "renk": "#3274d6", "svg": svg_devir(),
             "aciklama": "Bazı bölmeler hiç bitmez. Virgülden sonra aynı rakam ya da rakamlar sonsuza kadar tekrar eder: [[1/3]] = 0,333… Buna devirli ondalık gösterim denir.",
             "ek": "Tekrar eden (devreden) rakamların üstüne çizgi çekilir: 0,333… = 0,[[d:3]]. Kitaptaki küçük su şişesi [[1/3]] L, yani 0,[[d:3]] L'dir. (s. 41–42)",
             "akilda": "Rakam tekrar eder, üstüne çizgi",
             "cozum": {"baslik": "1 ÷ 3 neden bitmiyor?", "problem": "[[1/3]] kesrini ondalık gösterimle yazalım.",
                       "adimlar": [
                           {"metin": "1'in içinde 3 yok. Bölüme 0 ve virgül yaz, 1'in yanına 0 ekle: 10.", "islem": "0,…   10 ÷ 3"},
                           {"metin": "10'un içinde 3, 3 kere var. 3 × 3 = 9. Kalan 1.", "islem": "0,3   kalan 1"},
                           {"metin": "Kalan yine 1! Yanına 0 ekle: yine 10. Yine 3, yine kalan 1…", "islem": "0,33   kalan 1"},
                           {"metin": "Bölme hiç bitmeyecek. Tekrar eden 3'ün üstüne çizgi çekeriz.", "islem": "0,333… = 0,[[d:3]]"}],
                       "sonuc": "[[1/3]] = 0,[[d:3]]. Kalan hep aynı gelirse rakamlar da hep aynı gelir."},
             "soru": S("0,4545… sayısı devir çizgisiyle nasıl yazılır?", ["0,[[d:45]]", "0,4[[d:5]]", "0,[[d:4]]5"], 0,
                       "Hangi rakamlar birlikte tekrar ediyor: yalnız 5 mi, 45 mi?", "45, 45, 45… diye tekrar ediyor. Çizgi ikisinin de üstüne çekilir: 0,[[d:45]]. (s. 45)")},
            {"ad": "Sonlu mu, Devirli mi?", "renk": "#7b4fc9", "svg": svg_25(),
             "aciklama": "Kesri önce en sade hâline getir, sonra paydaya bak. Paydada 2 ve 5'ten başka asal çarpan (3, 7, 11… gibi) yoksa sonlu; varsa devirli ondalık gösterim olur.",
             "ek": "Kolay yol: Paydayı 2'ye ve 5'e bölebildiğin kadar böl. Geriye 1 kalırsa sonlu, başka bir sayı kalırsa devirlidir. Her rasyonel sayının mutlaka bir ondalık gösterimi vardır. (s. 43)",
             "akilda": "Paydada yalnız 2 ve 5 → sonlu",
             "cozum": {"baslik": "İkisinin de paydası 15, ama…", "problem": "Kitapta fon kartonu [[72/15]] TL, kurşun kalem [[92/15]] g. Paydaları aynı. Hangisi sonlu, hangisi devirli?",
                       "adimlar": [
                           {"metin": "Önce sadeleştir. 72 ve 15'in ikisi de 3'e bölünür.", "islem": "[[72/15]] = [[24/5]]"},
                           {"metin": "Payda 5. 5'i 5'e böl: 1 kaldı. Sonlu!", "islem": "[[24/5]] = 4,8"},
                           {"metin": "[[92/15]] sadeleşmez. 15'i 5'e böl: 3 kaldı. 3 de asal çarpan. Devirli!", "islem": "[[92/15]] = 6,1333… = 6,1[[d:3]]"}],
                       "sonuc": "Paydalar aynı olsa da sonuç farklı. Sırrı sadeleştirmede: [[72/15]] sadeleşince paydadaki 3 gitti. (s. 42–43)"},
             "sende": {"baslik": "Önce sadeleştir!", "problem": "[[3/12]] sayısının ondalık gösterimi sonlu mu, devirli mi?",
                       "adimlar": [
                           {"metin": "Önce en sade hâle getir.",
                            "soru": G("[[3/12]] kesrinin en sade hâlini yaz.", "1/4", "3 ve 12'nin ikisi de 3'e bölünür. Kesir çizgisi için / tuşu.",
                                      "3 ÷ 3 = 1, 12 ÷ 3 = 4: [[1/4]].", kesir=True),
                            "islem": "[[3/12]] = [[1/4]]"},
                           {"metin": "Paydayı 2'ye bölebildiğin kadar böl: 4 ÷ 2 = 2, 2 ÷ 2 = …",
                            "soru": G("Geriye hangi sayı kaldı?", "1", "2 ÷ 2 kaçtır?", "2 ÷ 2 = 1. Geriye 1 kaldı."),
                            "islem": "4 → 2 → 1"},
                           {"metin": "Geriye 1 kaldı. O hâlde?",
                            "soru": S("[[3/12]] sayısının ondalık gösterimi nasıldır?", ["Sonlu", "Devirli", "Ondalık gösterimi yoktur"], 0,
                                      "Geriye 1 kalırsa sonlu, başka sayı kalırsa devirli.", "Geriye 1 kaldı: sonlu. [[3/12]] = [[1/4]] = 0,25."),
                            "islem": "Sonlu: 0,25"}],
                       "sonuc": "Harika! 12'de 3 vardı ama sadeleşince gitti. Bu yüzden önce sadeleştiriyoruz."},
             "soru": S("[[1/6]] sayısının ondalık gösterimi nasıldır?", ["Sonlu", "Devirli", "Ondalık gösterimi yoktur"], 1,
                       "6'yı 2'ye böl. Geriye 1 mi kalıyor, başka bir sayı mı?", "6 ÷ 2 = 3. Geriye 3 kaldı: devirli. [[1/6]] = 0,1[[d:6]]. (s. 43)")},
            {"ad": "Ondalıktan Kesre", "renk": "#1d6fa3", "svg": svg_ond_kesir(),
             "aciklama": "Virgülden sonra kaç basamak varsa paydaya 1 ve yanına o kadar 0 yazarız. Virgülü silip sayıyı paya yazarız. Sonra sadeleştiririz.",
             "ek": "Kitapta bir öğrencinin boyu 1,32 m = [[132/100]] m = [[33/25]] m. Termostaki kahve 0,7 L = [[7/10]] L. (s. 44)",
             "akilda": "Basamak kadar sıfır",
             "soru": G("Termostaki kahve 0,7 L. Bu sayıyı kesir olarak yaz.", "7/10", "Virgülden sonra 1 basamak var: payda 10. Kesir çizgisi için / tuşu.",
                       "0,7 = [[7/10]]. (s. 44)", kesir=True, denk=True)},
            {"ad": "Devirliden Kesre", "renk": "#c92a2a", "svg": svg_dev_kesir(),
             "aciklama": "Paya, sayının tamamından (virgülsüz ve çizgisiz) devretmeyen kısmı çıkarırız. Paydaya, devreden her basamak için bir 9, virgülden sonra devretmeyen her basamak için bir 0 yazarız.",
             "ek": "En kolayları: 0,[[d:3]] = [[3/9]], 0,[[d:26]] = [[26/99]]. Devretmeyen basamak varsa: 0,1[[d:6]] = [[15/90]], çünkü 16 − 1 = 15; bir 9, bir 0. (s. 45–46)",
             "akilda": "Devreden 9, devretmeyen 0",
             "cozum": {"baslik": "0,1[[d:6]] kaçtır?", "problem": "0,1[[d:6]] sayısını kesre çevirelim.",
                       "adimlar": [
                           {"metin": "Sayının tamamını virgülsüz, çizgisiz yaz: 016, yani 16.", "islem": "Tamamı: 16"},
                           {"metin": "Devretmeyen kısmı yaz: çizgisiz kısım 01, yani 1.", "islem": "Devretmeyen: 1"},
                           {"metin": "Pay: tamamından devretmeyeni çıkar.", "islem": "Pay = 16 − 1 = 15"},
                           {"metin": "Payda: devreden 1 basamak → bir 9. Virgülden sonra devretmeyen 1 basamak → bir 0.", "islem": "Payda = 90"},
                           {"metin": "Kesri yaz ve sadeleştir.", "islem": "[[15/90]] = [[1/6]]"}],
                       "sonuc": "0,1[[d:6]] = [[15/90]] = [[1/6]]. Kontrol: [[1/6]] gerçekten 0,1666… çıkar."},
             "sende": {"baslik": "Kitaptaki sayıyı sen çevir", "problem": "0,[[d:4]] sayısını kesre çevirelim.",
                       "adimlar": [
                           {"metin": "Virgülden sonra devretmeyen basamak var mı?",
                            "soru": S("0,[[d:4]] sayısında virgülden sonra devretmeyen basamak var mı?", ["Yok, hepsi devrediyor", "Var, 1 tane", "Var, 2 tane"], 0,
                                      "Çizgi hangi rakamın üstünde? Virgülden sonra çizgisiz rakam var mı?", "Virgülden sonra yalnız 4 var ve o devrediyor."),
                            "islem": "Devretmeyen yok → 0 yazılmaz"},
                           {"metin": "Pay: tamamı 4, devretmeyen kısım 0.",
                            "soru": G("Pay kaç olur?", "4", "4 − 0 = ?", "4 − 0 = 4."),
                            "islem": "Pay = 4"},
                           {"metin": "Payda: devreden 1 basamak var.",
                            "soru": G("Payda kaç olur?", "9", "Devreden her basamak için bir 9 yazılır.", "1 devreden basamak → 9."),
                            "islem": "0,[[d:4]] = [[4/9]]"}],
                       "sonuc": "Harika! 0,[[d:4]] = [[4/9]]. (s. 46)"},
             "soru": S("0,[[d:5]] hangi kesre eşittir?", ["[[5/10]]", "[[5/99]]", "[[5/9]]"], 2,
                       "Devreden kaç basamak var? Her biri için bir 9 yazılır.", "Devreden 1 basamak → payda 9: 0,[[d:5]] = [[5/9]]. (s. 46)")}
        ],
        "biliyorMusun": [
            "Bilardoda 15 numaralı top ve bir beyaz top vardır. Kitaptaki Ahmet ilk atışında 15 topun 7'sini cebe sokuyor: [[7/15]] = 0,4[[d:6]]. (s. 49)",
            "Kitaptaki madenî para [[1/4]] cm, yani 0,25 cm kalınlığında. 100 tanesini üst üste koysan 25 cm'lik bir kule olur. (s. 41)"],
        "akildaKalsin": [
            "Kesir çizgisi bölme demektir: [[1/5]] = 1 ÷ 5 = 0,2.",
            "Paydayı 10, 100, 1000 yapabiliyorsan ondalık gösterimi bulmak kolaydır.",
            "Bölme biterse sonlu (0,25), hiç bitmezse devirli (0,[[d:3]]) ondalık gösterim olur.",
            "En sade hâldeki paydada yalnız 2 ve 5 varsa sonlu; başka asal çarpan varsa devirli.",
            "Ondalıktan kesre: virgülden sonraki basamak kadar sıfır, sonra sadeleştir.",
            "Devirliden kesre: devreden basamak kadar 9, devretmeyen kadar 0."],
        "merakKutusu": [
            {"soru": "0,999… gerçekten 1'e eşit mi?", "cevap": "Evet. [[1/3]] = 0,[[d:3]]. İki tarafı 3 ile çarparsan 1 = 0,[[d:9]] olur. Kural da aynı sonucu verir: 0,[[d:9]] = [[9/9]] = 1. Kitapta Sena ile Mete bunu tartışıyor. (s. 47–48)"},
            {"soru": "Her rasyonel sayının ondalık gösterimi var mı?", "cevap": "Evet. Bazılarınınki sonlu, bazılarınınki devirlidir ama hepsinin bir ondalık gösterimi vardır. (s. 43)"},
            {"soru": "Devir çizgisi neden çekilir?", "cevap": "Rakamlar sonsuza kadar tekrar ettiği için hepsini yazamayız. Çizgi \"bu rakamlar hep tekrar ediyor\" demektir. (s. 42, 45)"},
            {"soru": "0,3 ile 0,[[d:3]] aynı sayı mı?", "cevap": "Hayır. 0,3 = [[3/10]], 0,[[d:3]] = [[3/9]] = [[1/3]]. 0,[[d:3]] biraz daha büyüktür. (s. 41–42)"},
            {"soru": "Paydasında 3 olan her kesir devirli mi?", "cevap": "Önce sadeleştir! [[3/12]] sadeleşince [[1/4]] olur, sonludur. [[6/3]] ise 2'dir. Kurala en sade hâle bakarak karar verilir. (s. 43)"}],
        "dusunVeYaz": [{"soru": "[[1/3]] ve [[1/4]] kesirlerinden hangisinin ondalık gösterimi sonlu, hangisinin devirlidir? Neden?",
                        "ornekCevap": "[[1/4]] sonludur, çünkü paydası 4'te yalnız 2 var; 4'ü 100'e genişletebilirim: 0,25. [[1/3]] devirlidir, çünkü paydasında 3 var: 1 ÷ 3 hiç bitmez, 0,[[d:3]] olur.",
                        "anahtarlar": ["sonlu", "devir", "payda", "bitmez", "3"]}],
        "sorular": [
            N("[[2/5]] kesrini ondalık gösterime çevir ve sayı doğrusunda yerine dokun.", 0.4, sd(0, 1, 10),
              "[[2/5]] = 2 ÷ 5. Ya da paydayı 10 yap: 5 × 2 = 10, 2 × 2 = 4. Her küçük parça 0,1.",
              "[[2/5]] = [[4/10]] = 0,4: 0'dan sağa 4 parça. (s. 41, 44)"),
            G("[[9/25]] kesrini ondalık gösterimle yaz.", "0,36", "25'i 100 yapmak için kaçla çarparsın? Payı da aynı sayıyla çarp.",
              "25 × 4 = 100, 9 × 4 = 36: [[9/25]] = [[36/100]] = 0,36. (s. 44)", denk=True),
            S("Hangisinin ondalık gösterimi devirlidir?", ["[[3/8]]", "[[2/9]]", "[[7/10]]"], 1,
              "Paydaları 2'ye ve 5'e bölebildiğin kadar böl. Hangisinde 1'den başka sayı kalıyor?",
              "9'u 2'ye de 5'e de bölemeyiz; 9 = 3 × 3. [[2/9]] devirlidir: 0,[[d:2]]. (s. 43)"),
            S("Kitapta bir küp şekerin kütlesi [[16/6]] g, yani 2,666… g. Bu sayının doğru yazımı hangisidir?", ["2,[[d:6]]", "2,6", "[[d:2]],6"], 0,
              "Hangi rakam tekrar ediyor? Çizgi yalnızca tekrar eden rakamın üstüne çekilir.", "6 hep tekrar ediyor: 2,666… = 2,[[d:6]]. (s. 41)"),
            G("Bir öğrencinin boyu 1,32 m. Bunu paydası 100 olan bir kesir olarak yaz.", "132/100",
              "Virgülden sonra 2 basamak var. Virgülü sil, sayıyı paya yaz.", "1,32 = [[132/100]]. Sadeleşince [[33/25]] olur. (s. 44)", kesir=True),
            N("0,6 sayısının yerine dokun.", 0.6, sd(0, 1, 10),
              "0 ile 1 arası 10 eş parçaya bölündü. Her parça 0,1. 0'dan sağa 6 parça say.", "0,6 = [[6/10]]: 0'dan sağa 6 parça. (s. 44)"),
            S("[[18/15]] için hangisi doğrudur?", ["Sadeleşince [[6/5]] olur; ondalık gösterimi sonludur.", "Paydasında 3 olduğu için devirlidir.", "Ondalık gösterimi yoktur."], 0,
              "Önce sadeleştir: 18 ve 15'in ikisi de 3'e bölünür. Sonra paydaya bak.",
              "[[18/15]] = [[6/5]]. Paydada yalnız 5 var: sonlu. [[6/5]] = 1,2. (s. 43)"),
            G("Bilardoda Ahmet ikinci atışında masada kalan 8 topun 3'ünü cebe soktu. Bu oranı ondalık gösterimle yaz.", "0,375",
              "Oran [[3/8]]. 8'i 1000 yapmak için kaçla çarpmalısın? 8 × 125 = 1000.",
              "[[3/8]] = [[375/1000]] = 0,375. (s. 49)", denk=True),
            S("0,[[d:26]] hangi kesre eşittir?", ["[[26/100]]", "[[26/90]]", "[[26/99]]"], 2,
              "Devreden kaç basamak var? Devretmeyen basamak var mı?", "İki basamak devrediyor → 99; devretmeyen yok: 0,[[d:26]] = [[26/99]]. (s. 45)"),
            S("0,3 ile 0,[[d:3]] için hangisi doğrudur?", ["İkisi aynı sayıdır.", "0,3 = [[3/10]], 0,[[d:3]] = [[3/9]]; farklı sayılardır.", "0,3 devirli bir sayıdır."], 1,
              "Çizgi ne demekti? 0,3 bitiyor mu, 0,[[d:3]] bitiyor mu?", "0,3 sonludur: [[3/10]]. 0,[[d:3]] = 0,333… = [[3/9]]. Farklı sayılardır. (s. 42, 45)"),
            G(f"Hava sıcaklığı {M}14,2 °C. Bu sayıyı paydası 10 olan bir kesir olarak yaz.", "-142/10",
              f"Virgülden sonra 1 basamak var: payda 10. Eksiyi unutma: önce {M} tuşu.", f"{M}14,2 = [[-142/10]]. Sadeleşince [[-71/5]] olur. (s. 44)",
              kesir=True, kabul=["142/-10"]),
            S("Kitapta kutu süt [[1/5]] L, küçük su şişesi [[1/3]] L. Hangisi doğrudur?", ["İkisinin de ondalık gösterimi sonludur.", "Süt 0,2 L, su 0,[[d:3]] L'dir.", "Su 0,3 L'dir."], 1,
              "Paydalara bak: 5 ve 3. Hangisinde 2 ve 5'ten başka asal çarpan var?",
              "[[1/5]] = 0,2 sonludur. [[1/3]] = 0,[[d:3]] devirlidir. (s. 41–42)")]
    }


# ---------- u1k5 çizimleri ----------
def svg_sag_buyuk():
    g = _sd_mini(70, range(-3, 4), 24, 12, etiket=(-3, 0, 3))
    g += "<path d='M16 42 H104' stroke='#f2c14e' stroke-width='3.5' stroke-linecap='round'/><path d='M106 42 l-9 -5 v10z' fill='#f2c14e'/>"
    g += txt(60, 30, "büyür", "#f2c14e", 13) + txt(30, 110, "küçük", NB, 11) + txt(92, 110, "büyük", OB, 11)
    return bg(g)


def svg_isaretler():
    g = f"<rect x='8' y='44' width='34' height='30' rx='15' fill='{NB}'/>" + txt(25, 65, M, "#1b2340", 22)
    g += txt(50, 66, "&lt;", "#f2c14e", 20) + "<circle cx='66' cy='59' r='14' fill='#f2c14e'/>" + txt(66, 65, "0", "#1b2340", 16)
    g += txt(84, 66, "&lt;", "#f2c14e", 20) + f"<rect x='92' y='44' width='22' height='30' rx='11' fill='{OB}'/>" + txt(103, 65, "+", "#1b2340", 20)
    return bg(g)


def svg_ters():
    g = "<line x1='8' y1='78' x2='112' y2='78' stroke='#f5f6fa' stroke-width='3'/>"
    for x, r in ((12, NB), (60, "#f2c14e"), (108, OB)):
        g += f"<line x1='{x}' y1='70' x2='{x}' y2='86' stroke='{r}' stroke-width='3'/>"
    g += txt(12, 102, M + "1", NB, 11) + txt(60, 102, "0", "#f2c14e", 11) + txt(108, 102, "1", OB, 11)
    g += f"<circle cx='36' cy='78' r='5' fill='{NB}'/><circle cx='50' cy='78' r='5' fill='{NB}'/><circle cx='70' cy='78' r='5' fill='{OB}'/><circle cx='84' cy='78' r='5' fill='{OB}'/>"
    g += f"<path d='M84 66 Q60 30 36 66' stroke='{NB}' stroke-width='2.5' fill='none' stroke-dasharray='4 3'/><path d='M70 66 Q60 48 50 66' stroke='{NB}' stroke-width='2.5' fill='none' stroke-dasharray='4 3'/>"
    g += txt(60, 26, "ayna", "#f2c14e", 12)
    return bg(g)


def svg_dikey():
    g = "<rect x='0' y='46' width='120' height='74' fill='#1d4f7a' opacity='.55'/>"
    g += "<line x1='30' y1='12' x2='30' y2='110' stroke='#f5f6fa' stroke-width='3'/><path d='M30 8 l-5 8 h10z' fill='#f5f6fa'/>"
    g += "<line x1='22' y1='46' x2='38' y2='46' stroke='#f2c14e' stroke-width='3'/>" + txt(14, 50, "0", "#f2c14e", 12)
    g += f"<path d='M58 70 q10 -8 20 0 q-10 8 -20 0z M78 70 l8 -6 v12z' fill='{OB}'/>"
    g += f"<circle cx='70' cy='98' r='6' fill='{NB}'/><path d='M70 104 v8 M64 108 h12' stroke='{NB}' stroke-width='3' stroke-linecap='round'/>"
    g += txt(100, 30, "yukarı", "#f2c14e", 10) + txt(100, 42, "büyük", "#f2c14e", 10)
    return bg(g)


def svg_payda_es():
    g = ""
    for row, (n, renk) in enumerate(((3, NB), (5, OB))):
        y = 22 + row * 34
        for i in range(7):
            g += f"<rect x='{10 + i * 11}' y='{y}' width='10' height='24' fill='{renk if i < n else '#2b355c'}'/>"
        g += txt(104, y + 17, f"{n}/7", "#f5f6fa", 11)
    g += txt(60, 104, "3/7 &lt; 5/7", "#f2c14e", 15)
    return bg(g)


def svg_kisayol():
    g = "<line x1='12' y1='70' x2='108' y2='70' stroke='#f5f6fa' stroke-width='3'/>"
    for x, t in ((16, "0"), (60, "½"), (104, "1")):
        g += f"<line x1='{x}' y1='62' x2='{x}' y2='78' stroke='#f2c14e' stroke-width='3'/>" + txt(x, 96, t, "#f2c14e", 14)
    g += f"<circle cx='22' cy='70' r='5' fill='{NB}'/><circle cx='68' cy='70' r='5' fill='{OB}'/><circle cx='99' cy='70' r='5' fill='{OB}'/>"
    g += txt(22, 52, "1/10", NB, 10) + txt(68, 52, "5/9", OB, 10) + txt(99, 40, "9/10", OB, 10)
    return bg(g)


def svg_arada2():
    g = "<line x1='8' y1='70' x2='112' y2='70' stroke='#f5f6fa' stroke-width='3'/>"
    g += f"<line x1='24' y1='62' x2='24' y2='78' stroke='{OB}' stroke-width='3'/><line x1='96' y1='62' x2='96' y2='78' stroke='{OB}' stroke-width='3'/>"
    for x in (42, 60, 78):
        g += f"<circle cx='{x}' cy='70' r='{5 if x == 60 else 3.5}' fill='#f2c14e'/>"
    g += "<circle cx='60' cy='46' r='16' fill='none' stroke='#f5f6fa' stroke-width='3'/><path d='M71 57 l12 12' stroke='#f5f6fa' stroke-width='4' stroke-linecap='round'/>"
    g += txt(60, 51, "?", "#f2c14e", 14) + txt(24, 96, "2/8", OB, 11) + txt(96, 96, "4/8", OB, 11) + txt(60, 110, "3/8", "#f2c14e", 11)
    return bg(g)


# =================================================================
def u1k5():
    sd = lambda mn, mx, **ek: dict({"min": mn, "max": mx}, **ek)
    return {
        "id": "u1k5", "unite": "1. Tema: Sayılar ve Nicelikler", "baslik": "Karşılaştırma ve Sıralama", "sayfalar": "s. 50–61",
        "giris": "Mars mı daha soğuk, Neptün mü? [[-1/2]] mi büyük, [[-1/5]] mi? Bu konuda tam sayıları ve rasyonel sayıları karşılaştırıp sıralamayı öğreneceğiz. Sayı doğrusu en büyük yardımcımız olacak.",
        "hazirlik": {
            "baslik": "Hazır mısın?",
            "giris": "Bu konu sayı doğrusu, mutlak değer, payda eşitleme ve ondalık gösterim bilgilerinin üzerine kuruluyor. Önce bunları hatırlıyor musun bakalım. Not yok; sadece nereden başlayacağımızı bulacağız.",
            "maddeler": [
                {"ad": "Eksi sayılar sayı doğrusunda", "sinif": "Konu 1", "svg": svg_dogru(),
                 "anlatim": "Sayı doğrusunda 0'ın sağında pozitif sayılar, solunda negatif sayılar vardır. Eksi bir sayıyı bulmak için 0'dan sola doğru sayarız.",
                 "akilda": "Sol eksi, sağ artı",
                 "ornek": {"problem": f"{M}5'i sayı doğrusunda bulalım.", "adimlar": [
                     {"metin": f"{M}5 eksi bir sayı. Eksi sayılar 0'ın solunda.", "islem": "Yön: sola"},
                     {"metin": "0'dan sola 5 aralık say.",
                      "sayiDogrusu": sd(-6, 3, oklar=[{"bas": 0, "son": -5, "etiket": "5 aralık", "renk": NEG}], isaretler=[{"x": -5, "etiket": f"{M}5", "renk": NEG}]),
                      "islem": f"0 → {M}5"}]},
                 "sorular": [
                     N(f"Sayı doğrusunda {M}2'nin yerine dokun.", -2, sd(-5, 5), "0'ı bul. Sola doğru 2 aralık say.", f"{M}2, 0'ın 2 birim solundadır."),
                     S("Hangisi sayı doğrusunda 0'ın sağındadır?", [f"{M}4", "4", f"{M}1"], 1, "0'ın sağında artı sayılar vardır.", "4 pozitiftir, 0'ın sağındadır.")]},
                {"ad": "Mutlak değer", "sinif": "Konu 3", "svg": svg_mutlak(),
                 "anlatim": f"Bir sayının 0'a olan uzaklığına mutlak değer denir. İşareti sil, sayı kalır: |{M}6| = 6. Mutlak değer hiç eksi olmaz.",
                 "akilda": "Mutlak değer = 0'a uzaklık",
                 "ornek": {"problem": f"|{M}9| kaçtır?", "adimlar": [
                     {"metin": f"{M}9, 0'dan kaç birim uzakta? 9 birim."},
                     {"metin": "Uzaklık eksi olmaz.", "islem": f"|{M}9| = 9"}]},
                 "sorular": [
                     G(f"|{M}6| kaçtır?", "6", f"{M}6, 0'dan kaç birim uzakta? İşareti sil.", f"|{M}6| = 6."),
                     S("Hangisi 0'a daha uzaktır?", [f"{M}7", "5", "0"], 0, "Mutlak değerlerine bak: hangisinin 0'a uzaklığı daha çok?", f"|{M}7| = 7, |5| = 5. {M}7 daha uzaktır.")]},
                {"ad": "Payda eşitleme", "sinif": "Önceki yıllar", "svg": svg_h_genislet(),
                 "anlatim": "İki kesrin paydasını aynı yapmak için kesirleri genişletiriz. Paydalardan birinin, diğerinin katı olmasına bakarız: [[1/2]] ve [[3/4]] için [[1/2]] = [[2/4]].",
                 "akilda": "Paydaları aynı yap",
                 "ornek": {"problem": "[[2/3]] ile [[3/4]] kesirlerinin paydalarını eşitleyelim.", "adimlar": [
                     {"metin": "3'ün de 4'ün de katı olan bir sayı bul: 3 × 4 = 12.", "islem": "Ortak payda: 12"},
                     {"metin": "[[2/3]] kesrini 4 ile genişlet.", "islem": "[[2/3]] = [[8/12]]"},
                     {"metin": "[[3/4]] kesrini 3 ile genişlet.", "islem": "[[3/4]] = [[9/12]]"}]},
                 "sorular": [
                     G("[[1/3]] kesrini paydası 6 olacak şekilde genişlet. Pay kaç olur?", "2", "3 × 2 = 6. Payı da 2 ile çarp.", "1 × 2 = 2: [[1/3]] = [[2/6]]."),
                     S("[[1/2]] ile [[2/5]] kesirlerinin paydaları hangi sayıda eşitlenebilir?", ["10", "7", "3"], 0,
                       "Hem 2'nin hem 5'in katı olan sayıyı ara.", "10, hem 2'nin hem 5'in katıdır: [[5/10]] ve [[4/10]].")]},
                {"ad": "Kesirden ondalığa", "sinif": "Geçen konu", "svg": svg_onluk(),
                 "anlatim": "Paydayı 10, 100 ya da 1000 yaparak kesri ondalık gösterime çevirebiliriz: [[1/4]] = [[25/100]] = 0,25.",
                 "akilda": "10, 100, 1000'e genişlet",
                 "ornek": {"problem": "[[3/5]] kesrini ondalık gösterimle yazalım.", "adimlar": [
                     {"metin": "5 × 2 = 10. Payı da 2 ile çarp.", "islem": "[[3/5]] = [[6/10]]"},
                     {"metin": "Payda 10: virgülden sonra 1 basamak.", "islem": "[[6/10]] = 0,6"}]},
                 "sorular": [
                     G("[[1/4]] kesrini ondalık gösterimle yaz.", "0,25", "4 × 25 = 100. Payı da 25 ile çarp.", "[[1/4]] = [[25/100]] = 0,25.", denk=True),
                     S("[[4/5]] hangisine eşittir?", ["0,45", "0,8", "0,5"], 1, "5 × 2 = 10. Payı da 2 ile çarp.", "[[4/5]] = [[8/10]] = 0,8.")]}
            ]},
        "kavramlar": [
            {"ad": "Sağdaki Büyüktür", "renk": "#1f9e8f", "svg": svg_sag_buyuk(),
             "aciklama": "Sayı doğrusunda bir sayı, solundaki sayılardan büyük, sağındaki sayılardan küçüktür. Sağa gittikçe sayılar büyür, sola gittikçe küçülür.",
             "ek": f"+1, {M}3'ün sağında: +1 > {M}3. {M}5, {M}2'nin solunda: {M}5 < {M}2. Kitaptaki gezegenlerde Mars ({M}65 °C), Neptün'den ({M}200 °C) daha sıcaktır, çünkü sayı doğrusunda daha sağdadır. (s. 50–51)",
             "akilda": "Sağdaki büyük",
             "sayiDogrusu": sd(-6, 3, isaretler=[{"x": -5, "etiket": f"{M}5", "renk": NEG}, {"x": -2, "etiket": f"{M}2", "renk": NEG}]),
             "cozum": {"baslik": f"{M}7 mi büyük, {M}12 mi?", "problem": f"{M}7 ile {M}12'yi karşılaştıralım.",
                       "sayiDogrusu": sd(-13, 1, gizle=[-11, -10, -9, -8, -6, -5, -4, -3, -2, -1],
                                         isaretler=[{"x": -12, "etiket": f"{M}12", "renk": NEG}, {"x": -7, "etiket": f"{M}7", "renk": NEG}]),
                       "adimlar": [
                           {"metin": "İkisi de eksi: ikisi de 0'ın solunda."},
                           {"metin": f"{M}12, 0'dan 12 birim sola; {M}7 ise 7 birim sola gider. {M}12 daha solda.", "islem": f"{M}12 daha solda"},
                           {"metin": "Soldaki küçüktür.", "islem": f"{M}12 < {M}7"}],
                       "sonuc": f"{M}12 < {M}7. Sayı doğrusunda yerlerini bulmak her zaman işe yarar. (s. 51)"},
             "soru": S("Hangisi doğrudur?", [f"{M}5 > +7", f"{M}100 < {M}99", f"{M}7 < {M}12"], 1,
                       "Her çift için düşün: hangisi sayı doğrusunda daha solda?", f"{M}100, {M}99'un solundadır: {M}100 < {M}99. (s. 51)")},
            {"ad": "Negatif, Sıfır, Pozitif", "renk": ZER, "svg": svg_isaretler(),
             "aciklama": "Pozitif sayılar her zaman 0'dan büyüktür. Negatif sayılar her zaman 0'dan küçüktür. Bu yüzden her pozitif sayı, her negatif sayıdan büyüktür.",
             "ek": "İşaretler farklıysa hesap yapmaya gerek yok: [[1/100]] > [[-50/3]]. Kitaptaki Dikkat kutusunun ilk kısa yolu budur: pozitif mi, negatif mi? (s. 53, 57)",
             "akilda": "Negatif < 0 < pozitif",
             "soru": S("Hangisi doğrudur?", ["[[-1/2]] > 0", "0,1 > [[-9/2]]", f"{M}3 > 2"], 1,
                       "Bir pozitif sayı ile bir negatif sayıdan hangisi her zaman büyüktür?", "0,1 pozitif, [[-9/2]] negatif. Pozitif her zaman büyüktür. (s. 53)")},
            {"ad": "Negatiflerde Uzak Olan Küçük", "renk": "#3274d6", "svg": svg_ters(),
             "aciklama": "İki negatif sayıdan 0'a daha uzak olan, yani mutlak değeri büyük olan daha küçüktür: |" + M + "12| > |" + M + "7| olduğu için " + M + "12 < " + M + "7.",
             "ek": "Borç gibi düşün: 12 TL borcu olan, 7 TL borcu olandan daha zordadır. Kesirlerde de aynı: [[1/5]] < [[1/2]] ama [[-1/2]] < [[-1/5]]. Kitaptaki mor karton deneyinde pozitiflerin sırası, eksi işareti gelince tersine döner. (s. 52–53)",
             "akilda": "Eksiler ters sıralanır",
             "sayiDogrusu": {"min": -1, "max": 1, "bolme": 10, "isaretler": [{"x": -0.5, "etiket": "−1/2", "renk": NEG}, {"x": -0.2, "etiket": "−1/5", "renk": NEG},
                                                                          {"x": 0.2, "etiket": "1/5", "renk": POS}, {"x": 0.5, "etiket": "1/2", "renk": POS}]},
             "cozum": {"baslik": "[[-1/2]] mi büyük, [[-1/5]] mi?", "problem": "[[-1/2]] ile [[-1/5]] sayılarını karşılaştıralım.",
                       "adimlar": [
                           {"metin": "Önce eksileri sil: [[1/2]] ile [[1/5]]. [[1/2]] = 0,5 ve [[1/5]] = 0,2.", "islem": "[[1/2]] > [[1/5]]"},
                           {"metin": "Eksi gelince sıra döner. 0'a daha uzak olan [[-1/2]] daha soldadır.",
                            "sayiDogrusu": {"min": -1, "max": 1, "bolme": 10, "isaretler": [{"x": -0.5, "etiket": "−1/2", "renk": NEG}, {"x": -0.2, "etiket": "−1/5", "renk": NEG}]},
                            "islem": "[[-1/2]] daha solda"},
                           {"metin": "Soldaki küçüktür.", "islem": "[[-1/2]] < [[-1/5]]"}],
                       "sonuc": "[[-1/2]] < [[-1/5]]. Pozitiflerde büyük olan, negatif olunca küçük olur."},
             "sende": {"baslik": "Şimdi sen karşılaştır", "problem": "[[-3/4]] ile [[-1/4]] sayılarını karşılaştıralım.",
                       "adimlar": [
                           {"metin": "Önce eksileri sil.",
                            "soru": S("Hangisi büyüktür?", ["[[3/4]]", "[[1/4]]", "İkisi eşittir"], 0, "Paydalar aynı: payı büyük olan büyüktür.", "[[3/4]] > [[1/4]]."),
                            "islem": "[[3/4]] > [[1/4]]"},
                           {"metin": "Eksi gelince sıra döner.",
                            "soru": S("Hangisi doğrudur?", ["[[-3/4]] < [[-1/4]]", "[[-3/4]] > [[-1/4]]", "[[-3/4]] = [[-1/4]]"], 0,
                                      "0'a daha uzak olan negatif sayı daha küçüktür.", "[[-3/4]] 0'a daha uzak: [[-3/4]] < [[-1/4]]."),
                            "islem": "[[-3/4]] < [[-1/4]]"},
                           {"metin": "Sayı doğrusunda kontrol et.",
                            "soru": N("[[-3/4]] sayısının yerine dokun.", -0.75, {"min": -1, "max": 1, "bolme": 4},
                                      f"0'dan sola git. 0 ile {M}1 arası 4 eş parça; 3 parça say.", "[[-3/4]], [[-1/4]]'ün solundadır, yani daha küçüktür."),
                            "islem": "Soldaki küçük ✓"}],
                       "sonuc": "Harika! [[-3/4]] < [[-1/4]]."},
             "soru": S("Hangisi en küçüktür?", ["[[-1/3]]", "[[-2/3]]", "0"], 1,
                       "Negatif sayılardan 0'a daha uzak olan daha küçüktür.", "[[-2/3]], 0'a [[-1/3]]'ten daha uzaktır; en küçüğü odur. (s. 53)")},
            {"ad": "Dikey Sayı Doğrusu", "renk": "#1d6fa3", "svg": svg_dikey(),
             "aciklama": "Dikey sayı doğrusunda yukarı çıktıkça sayılar büyür, aşağı indikçe küçülür. Yukarıdaki sayı, aşağıdaki sayıdan büyüktür.",
             "ek": "Kitapta okyanusun farklı derinliklerinde yaşayan canlılar dikey sayı doğrusunda gösteriliyor. Daha derinde yaşayan canlının konumu daha küçük bir sayıdır. (s. 54)",
             "akilda": "Yukarıdaki büyük",
             "sayiDogrusu": {"min": -4, "max": 1, "dikey": True, "birim": 28, "sifirEtiketi": "Deniz seviyesi",
                             "isaretler": [{"x": -1, "etiket": f"Balık {M}1 m", "renk": NEG}, {"x": -3, "etiket": f"Dalgıç {M}3 m", "renk": NEG}]},
             "soru": S("Dikey sayı doğrusunda A noktası, B noktasının üstünde. Hangisi doğrudur?", ["A > B", "A < B", "A = B"], 0,
                       "Dikey sayı doğrusunda yukarıdaki sayı büyük müdür, küçük müdür?",
                       "Yukarıdaki sayı büyüktür: A > B. (s. 54)",
                       sayiDogrusu={"min": -4, "max": 1, "dikey": True, "birim": 24, "gizle": [-3, -1],
                                    "isaretler": [{"x": -1, "etiket": "A", "renk": NEG}, {"x": -3, "etiket": "B", "renk": NEG}]})},
            {"ad": "Paydaları ya da Payları Eşitle", "renk": "#e8590c", "svg": svg_payda_es(),
             "aciklama": "Paydalar eşitse payı büyük olan büyüktür: [[3/7]] < [[5/7]]. Paydalar farklıysa önce kesirleri genişletip paydaları eşitleriz.",
             "ek": "Paylar eşitse paydası küçük olan büyüktür: [[2/3]] > [[2/5]]. Kitapta basketbolcuların başarıları [[5/12]], [[3/8]], [[2/6]] payları 30'a eşitlenerek karşılaştırılıyor: [[30/72]] > [[30/80]] > [[30/90]]. (s. 55–56)",
             "akilda": "Altlar eşitse üstlere bak",
             "cozum": {"baslik": "[[2/3]] mü büyük, [[3/4]] mü?", "problem": "[[2/3]] ile [[3/4]] kesirlerini karşılaştıralım.",
                       "adimlar": [
                           {"metin": "Paydalar farklı: 3 ve 4. İkisinin de katı olan 12'yi seç.", "islem": "Ortak payda: 12"},
                           {"metin": "İki kesri de paydası 12 olacak şekilde genişlet.", "islem": "[[2/3]] = [[8/12]]   ve   [[3/4]] = [[9/12]]"},
                           {"metin": "Paydalar eşit: payı büyük olan büyüktür.", "islem": "[[8/12]] < [[9/12]]  →  [[2/3]] < [[3/4]]"}],
                       "sonuc": "[[2/3]] < [[3/4]]. Paydalar eşitlenince karşılaştırmak kolaylaşır."},
             "sende": {"baslik": "Şimdi sen eşitle", "problem": "[[3/5]] ile [[7/10]] kesirlerini karşılaştıralım.",
                       "adimlar": [
                           {"metin": "10, 5'in katıdır. [[3/5]] kesrinin paydasını 10 yapalım.",
                            "soru": G("5'i kaçla çarparsak 10 olur?", "2", "5 × ? = 10", "5 × 2 = 10."),
                            "islem": "5 × 2 = 10"},
                           {"metin": "Payı da aynı sayıyla çarp.",
                            "soru": G("[[3/5]] = ?/10. Yeni pay kaç?", "6", "3 × 2 = ?", "3 × 2 = 6: [[3/5]] = [[6/10]]."),
                            "islem": "[[3/5]] = [[6/10]]"},
                           {"metin": "Şimdi paydalar eşit: [[6/10]] ile [[7/10]].",
                            "soru": S("Hangisi doğrudur?", ["[[3/5]] < [[7/10]]", "[[3/5]] > [[7/10]]", "[[3/5]] = [[7/10]]"], 0,
                                      "Paydalar eşitse payı büyük olan büyüktür: 6 mı, 7 mi?", "6 < 7, yani [[3/5]] < [[7/10]]."),
                            "islem": "[[3/5]] < [[7/10]]"}],
                       "sonuc": "Harika! [[3/5]] < [[7/10]]."},
             "soru": S("Hangisi büyüktür?", ["[[4/9]]", "[[7/9]]", "İkisi eşittir"], 1,
                       "Paydalar eşit. Payı büyük olan büyüktür.", "Paydalar eşit, 7 > 4: [[7/9]] > [[4/9]]. (s. 55–56)")},
            {"ad": "Kısa Yollar", "renk": "#7b4fc9", "svg": svg_kisayol(),
             "aciklama": "Bazen hesap yapmaya gerek yoktur. Sayıların işaretine, tam kısmına ya da 0'a, [[1/2]]'ye, 1'e yakınlığına bakarız. Olmazsa ondalık gösterime çeviririz.",
             "ek": "Kitaptaki Dikkat kutusunun kısa yolları: işaret, tam kısım ([[2 1/5]] > [[1 7/8]]), 0'a, [[1/2]]'ye ve 1'e yakınlık, eşit pay ya da payda, ondalık gösterim. [[9/10]] 1'e çok yakın; [[1/10]] ise 0'a. (s. 57)",
             "akilda": "Önce kolay yolu ara",
             "cozum": {"baslik": "Hesapsız sıralayalım", "problem": "[[5/9]], [[1/10]] ve [[9/10]] sayılarını küçükten büyüğe sıralayalım.",
                       "adimlar": [
                           {"metin": "[[1/10]], 10 parçadan yalnız 1 tanesi: 0'a çok yakın.", "islem": "[[1/10]] → 0'a yakın"},
                           {"metin": "[[9/10]], 10 parçadan 9 tanesi: 1'e çok yakın.", "islem": "[[9/10]] → 1'e yakın"},
                           {"metin": "[[5/9]] yarıdan biraz fazla (9'un yarısı 4,5): ortada.", "islem": "[[5/9]] → [[1/2]]'ye yakın"},
                           {"metin": "Şimdi sırala.", "islem": "[[1/10]] < [[5/9]] < [[9/10]]"}],
                       "sonuc": "Hiç payda eşitlemeden sıraladık. Önce kısa yol, olmazsa payda eşitle ya da ondalığa çevir."},
             "soru": S("[[2 1/5]] ile [[1 7/8]] için hangisi doğrudur?", ["[[2 1/5]] > [[1 7/8]]", "[[2 1/5]] < [[1 7/8]]", "İkisi eşittir"], 0,
                       "Önce tam kısımlara bak: 2 mi büyük, 1 mi?", "Tam kısımlar farklı: 2 > 1. Kesirlere bakmaya gerek yok. (s. 57)")},
            {"ad": "Arada Hep Bir Sayı Var", "renk": "#2f9e44", "svg": svg_arada2(),
             "aciklama": f"{M}1 ile 0 arasında hiç tam sayı yoktur. Ama herhangi iki rasyonel sayı arasında en az bir rasyonel sayı bulunur.",
             "ek": "Aradaki sayıyı bulmak için paydaları büyütürüz. Kitapta [[-3/5]] ile [[-2/5]] arasında bir sayı aranıyor: paydayı 10 yapınca [[-6/10]] ile [[-4/10]] olur, arada [[-5/10]] vardır. Bu iş hiç bitmez. (s. 59–60)",
             "akilda": "Arada hep bir sayı var",
             "cozum": {"baslik": "[[1/4]] ile [[1/2]] arasında ne var?", "problem": "[[1/4]] ile [[1/2]] arasında bir rasyonel sayı bulalım.",
                       "adimlar": [
                           {"metin": "Paydaları 8 yap.", "islem": "[[1/4]] = [[2/8]]   ve   [[1/2]] = [[4/8]]"},
                           {"metin": "2 ile 4 arasında 3 var.", "islem": "[[2/8]] < [[3/8]] < [[4/8]]"},
                           {"metin": "Sayı doğrusunda bak.",
                            "sayiDogrusu": {"min": 0, "max": 1, "bolme": 8, "isaretler": [{"x": 0.25, "etiket": "1/4", "renk": POS}, {"x": 0.375, "etiket": "3/8", "renk": ZER}, {"x": 0.5, "etiket": "1/2", "renk": POS}]},
                            "islem": "[[3/8]] arada"}],
                       "sonuc": "[[1/4]] < [[3/8]] < [[1/2]]. Paydayı büyütünce aradaki sayılar ortaya çıkar."},
             "sende": {"baslik": "Şimdi sen bul", "problem": "[[1/5]] ile [[2/5]] arasında bir sayı bulalım.",
                       "adimlar": [
                           {"metin": "Paydayı 10 yapalım.",
                            "soru": G("[[1/5]] = ?/10. Pay kaç?", "2", "5 × 2 = 10. Payı da 2 ile çarp.", "1 × 2 = 2: [[1/5]] = [[2/10]]."),
                            "islem": "[[1/5]] = [[2/10]]"},
                           {"metin": "Diğerini de çevir.",
                            "soru": G("[[2/5]] = ?/10. Pay kaç?", "4", "2 × 2 = ?", "2 × 2 = 4: [[2/5]] = [[4/10]]."),
                            "islem": "[[2/5]] = [[4/10]]"},
                           {"metin": "2 ile 4 arasında hangi sayı var?",
                            "soru": G("Aradaki kesrin payı kaç? ?/10", "3", "2'den büyük, 4'ten küçük tam sayı.", "[[2/10]] < [[3/10]] < [[4/10]]."),
                            "islem": "[[3/10]] arada"}],
                       "sonuc": "Harika! [[1/5]] < [[3/10]] < [[2/5]]."},
             "soru": N("[[1/4]] ile [[1/2]] arasındaki sayıya dokun.", 0.375, {"min": 0, "max": 1, "bolme": 8},
                       "0 ile 1 arası 8 parça. [[1/4]] = [[2/8]], [[1/2]] = [[4/8]]. Aradaki çizgi hangisi?", "[[2/8]] ile [[4/8]] arasında [[3/8]] vardır. (s. 60)")}
        ],
        "biliyorMusun": [
            "Güneş'e en yakın gezegen Merkür'dür ama en sıcak gezegen Venüs'tür (464 °C). Venüs'ün yoğun atmosferi sera etkisi oluşturur. (s. 50)",
            f"Arabalarda radyatördeki suyun kışın donmaması için antifriz kullanılır. Kitaptaki antifriz {M}36,8 °C'ta donar; bundan soğuk havada işe yaramaz. (s. 61)",
            "Futbolda puanlar eşitse averajı büyük olan takım üstte yer alır. Yenilen gol atılandan fazlaysa averaj eksi olur. (s. 51)"],
        "akildaKalsin": [
            "Sayı doğrusunda sağdaki sayı büyüktür; dikey sayı doğrusunda yukarıdaki büyüktür.",
            "Negatif < 0 < pozitif. Her pozitif sayı her negatif sayıdan büyüktür.",
            "İki negatif sayıdan 0'a daha uzak olan küçüktür: eksiler ters sıralanır.",
            "Paydalar eşitse paya bak; değilse paydaları ya da payları eşitle.",
            "Önce kısa yol: işaret, tam kısım, 0'a, [[1/2]]'ye ve 1'e yakınlık, ondalık gösterim.",
            "İki rasyonel sayı arasında her zaman başka bir rasyonel sayı vardır."],
        "merakKutusu": [
            {"soru": f"{M}100 mü büyük, {M}99 mu?", "cevap": f"{M}99 büyüktür. {M}100, 0'a daha uzaktır ve sayı doğrusunda {M}99'un solundadır. (s. 51)"},
            {"soru": "Paylar eşitse hangisi büyük?", "cevap": "Paydası küçük olan. [[2/3]] bütünü 3'e, [[2/5]] 5'e böler; 3'e bölünen pastanın dilimleri daha büyüktür. (s. 55–56)"},
            {"soru": f"{M}1 ile 0 arasında kaç rasyonel sayı var?", "cevap": "Sayamayacağımız kadar çok! İki sayı arasına hep yeni bir sayı yerleştirebiliriz; paydayı büyüttükçe yenileri çıkar. (s. 59–60)"},
            {"soru": "Isı hangi yöne akar?", "cevap": f"Sıcaklığı yüksek olandan düşük olana. {M}3 °C'taki bir nesneden {M}7 °C'taki nesneye doğru akar, çünkü {M}3 > {M}7. (s. 61)"},
            {"soru": "Averaj eksi olabilir mi?", "cevap": f"Evet. Yenilen goller atılan gollerden fazlaysa averaj eksidir. Puanlar eşitse {M}1 averajlı takım, {M}2 averajlı takımın üstündedir. (s. 51)"}],
        "dusunVeYaz": [{"soru": "[[-1/2]] ile [[-1/3]] sayılarından hangisi büyüktür? Nasıl karar verdiğini anlat.",
                        "ornekCevap": "[[-1/3]] daha büyüktür. Eksileri silince [[1/2]] > [[1/3]]. Negatiflerde sıra döner; [[-1/2]] 0'a daha uzak olduğu için daha küçüktür.",
                        "anahtarlar": ["uzak", "sıfır", "ters", "dön", "sol"]}],
        "sorular": [
            S(f"Kitapta Mars'ın yüzey sıcaklığı {M}65 °C, Neptün'ünki {M}200 °C. Hangisi daha sıcaktır?", ["Mars", "Neptün", "İkisi eşittir"], 0,
              "Daha sıcak olan, sayı doğrusunda daha sağda olandır.", f"{M}65 > {M}200: Mars daha sıcaktır. (s. 50)"),
            N(f"{M}3'ten büyük olan en küçük tam sayıya dokun.", -2, sd(-6, 3),
              f"{M}3'ten büyük sayılar onun sağındadır. Sağdaki ilk tam sayı hangisi?", f"{M}3'ün hemen sağındaki tam sayı {M}2'dir. (s. 51)"),
            S("Hangisi doğrudur?", ["[[-5/6]] > [[1/8]]", "0 < [[-2/7]]", "[[-9/4]] < [[1/9]]"], 2,
              "Her seçenekte işaretlere bak. Negatif mi büyük, pozitif mi?", "[[-9/4]] negatif, [[1/9]] pozitif. Negatif her zaman küçüktür. (s. 53)"),
            S("Hangisi en küçüktür?", [f"{M}7", f"{M}1", f"{M}12"], 2,
              "Hepsi negatif. 0'a en uzak olanı bul.", f"{M}12, 0'a en uzak olandır; en küçüğü odur. (s. 51)"),
            S("Hangisi doğrudur?", ["[[-3/8]] < [[-5/8]]", "[[-5/8]] < [[-3/8]]", "[[-5/8]] = [[-3/8]]"], 1,
              "Eksileri sil: [[5/8]] mi büyük, [[3/8]] mü? Negatif olunca sıra döner.", "[[5/8]] > [[3/8]], eksi gelince [[-5/8]] < [[-3/8]]. (s. 53)"),
            G("İki takımın puanı eşit. A takımının averajı " + M + "2. B takımı sıralamada A'nın üstünde ise B'nin averajı en az kaç olabilir? (Averaj bir tam sayıdır.)", "-1",
              f"B'nin averajı {M}2'den büyük olmalı. {M}2'den büyük en küçük tam sayı hangisi?", f"{M}2'den büyük en küçük tam sayı {M}1'dir. (s. 51)",
              sayiDogrusu=sd(-5, 2)),
            S("Kitaptaki basketbolcular atışlarının [[5/12]], [[3/8]] ve [[2/6]] kadarını sayıya çevirdi. Büyükten küçüğe sıralama hangisidir?",
              ["[[5/12]] > [[3/8]] > [[2/6]]", "[[2/6]] > [[3/8]] > [[5/12]]", "[[3/8]] > [[5/12]] > [[2/6]]"], 0,
              "Payları 30 yap: [[30/72]], [[30/80]], [[30/90]]. Paylar eşitse paydası küçük olan büyüktür.",
              "[[30/72]] > [[30/80]] > [[30/90]], yani [[5/12]] > [[3/8]] > [[2/6]]. (s. 55–56)"),
            G("[[-7/3]] sayısından küçük olan en büyük tam sayı kaçtır?", "-3",
              f"[[-7/3]] = [[-2 1/3]]. Hangi iki tam sayı arasında? Küçük olan solda.", f"[[-7/3]] = [[-2 1/3]], {M}2 ile {M}3 arasındadır. Ondan küçük en büyük tam sayı {M}3'tür. (s. 60)",
              sayiDogrusu={"min": -4, "max": 0, "bolme": 3, "isaretler": [{"x": -7 / 3, "etiket": "−7/3", "renk": NEG}]}),
            N("[[-3/2]] ile [[-1/2]] arasındaki tam sayıya dokun.", -1, {"min": -3, "max": 1, "bolme": 2},
              f"[[-3/2]] = [[-1 1/2]]. Bu iki sayının arasında hangi tam sayı var?", f"[[-3/2]] < {M}1 < [[-1/2]]. Aradaki tam sayı {M}1'dir. (s. 59)"),
            G("Paydası 10 olan ve [[2/5]] ile [[3/5]] arasında bulunan kesri yaz.", "5/10",
              "Paydaları 10 yap: [[2/5]] = ?/10, [[3/5]] = ?/10. Aradaki payı bul.", "[[4/10]] < [[5/10]] < [[6/10]]. (s. 60)", kesir=True, denk=True),
            S(f"Bir dalgıç deniz seviyesinin [[3/2]] m altında, bir balık [[5/2]] m altında. Hangisi doğrudur?",
              ["Dalgıcın konumu daha büyük bir sayıdır.", "Balığın konumu daha büyük bir sayıdır.", "İkisi eşittir."], 0,
              "Konumları yaz: [[-3/2]] ve [[-5/2]]. Dikey sayı doğrusunda hangisi daha yukarıda?", "[[-3/2]] > [[-5/2]]. Dalgıç daha yukarıda, sayısı daha büyük. (s. 54)"),
            S("Hangisi [[1/2]]'den büyüktür?", ["[[4/9]]", "[[3/7]]", "[[5/8]]"], 2,
              "Paydanın yarısını bul. Pay, paydanın yarısından büyük mü?", "8'in yarısı 4; 5 > 4 olduğu için [[5/8]] > [[1/2]]. [[4/9]] ve [[3/7]] yarıdan küçüktür. (s. 57)")]
    }


# ---------- u1k6 çizimleri ----------
def svg6_yolculuk():
    g = txt(60, 34, f"({M}2) + (+4)", "#f5f6fa", 15)
    g += _sd_mini(86, range(-4, 5), 12, 12, etiket=(-2, 0, 2))
    g += f"<path d='M36 78 Q60 44 84 78' stroke='{OB}' stroke-width='3' fill='none' stroke-linecap='round'/><path d='M84 78 l-8 -3 4 -6z' fill='{OB}'/>"
    g += f"<circle cx='36' cy='86' r='6' fill='{NB}'/><circle cx='84' cy='86' r='6' fill='#f2c14e'/>"
    return bg(g)


def svg6_ayni():
    g = txt(60, 30, f"({M}3) + ({M}2)", "#f5f6fa", 15)
    g += f"<rect x='18' y='44' width='48' height='22' rx='6' fill='{NB}'/>" + txt(42, 60, "3", "#1b2340", 14)
    g += f"<rect x='70' y='44' width='32' height='22' rx='6' fill='{NB}'/>" + txt(86, 60, "2", "#1b2340", 14)
    g += "<path d='M18 74 q0 8 8 8 h68 q8 0 8 -8' stroke='#f2c14e' stroke-width='2.5' fill='none'/>"
    g += txt(60, 106, f"= {M}5", NB, 20)
    return bg(g)


def svg6_farkli():
    g = txt(60, 28, f"({M}5) + (+3)", "#f5f6fa", 15)
    g += f"<rect x='20' y='40' width='80' height='18' rx='5' fill='{NB}'/><rect x='20' y='40' width='48' height='18' rx='5' fill='#1b2340' opacity='.6'/>"
    g += f"<rect x='20' y='64' width='48' height='18' rx='5' fill='{OB}'/>"
    g += "<path d='M70 90 v6 h30 v-6' stroke='#f2c14e' stroke-width='2.5' fill='none'/>"
    g += txt(38, 110, f"5 {M} 3", "#f5f6fa", 13) + txt(86, 112, f"{M}2", NB, 18)
    return bg(g)


def svg6_ters():
    g = txt(60, 30, f"({M}3) + (+3)", "#f5f6fa", 15)
    g += _sd_mini(72, range(-4, 5), 12, 12, etiket=(-3, 0, 3))
    g += f"<path d='M60 64 Q42 34 24 64' stroke='{NB}' stroke-width='3' fill='none' stroke-linecap='round'/><path d='M24 64 l1 -9 7 5z' fill='{NB}'/>"
    g += f"<path d='M24 64 Q42 48 58 64' stroke='{OB}' stroke-width='3' fill='none' stroke-linecap='round'/><path d='M58 64 l-8 -2 4 -6z' fill='{OB}'/>"
    g += "<circle cx='60' cy='72' r='7' fill='#f2c14e'/>" + txt(60, 114, "= 0", "#f2c14e", 16)
    return bg(g)


def svg6_mutlak_once():
    g = txt(60, 36, f"|{M}5| + |{M}9|", "#f5f6fa", 17)
    g += "<path d='M60 46 v12' stroke='#f2c14e' stroke-width='3'/><path d='M60 66 l-6 -8 h12z' fill='#f2c14e'/>"
    g += txt(60, 88, "5 + 9", OB, 18) + txt(60, 110, "= 14", "#f2c14e", 17)
    return bg(g)


def svg6_cikarma():
    g = txt(60, 34, f"10 {M} ({M}6)", "#f5f6fa", 18)
    g += "<path d='M47 42 v14 M77 42 v14' stroke='#f2c14e' stroke-width='3'/><path d='M47 62 l-5 -7 h10z M77 62 l-5 -7 h10z' fill='#f2c14e'/>"
    g += txt(60, 84, "10 + (+6)", OB, 18) + txt(60, 110, "= 16", "#f2c14e", 16)
    return bg(g)


def svg6_arada():
    g = "<rect x='49' y='28' width='22' height='32' rx='6' fill='none' stroke='#f2c14e' stroke-width='2.5'/>"
    g += txt(30, 52, f"{M}4", NB, 24) + txt(60, 52, M, "#f2c14e", 24) + txt(88, 52, "5", OB, 24)
    g += txt(60, 78, "çıkar", "#f2c14e", 12) + txt(60, 104, f"({M}4) {M} (+5)", "#f5f6fa", 14)
    return bg(g)


# =================================================================
def u1k6():
    sd = lambda mn, mx, **ek: dict({"min": mn, "max": mx}, **ek)
    kat = lambda mn, mx, **ek: dict({"min": mn, "max": mx, "dikey": True, "birim": 28, "sifirEtiketi": "Zemin kat"}, **ek)
    ok = lambda a, b, e, r: {"bas": a, "son": b, "etiket": e, "renk": r}
    return {
        "id": "u1k6", "unite": "1. Tema: Sayılar ve Nicelikler", "baslik": "Tam Sayılarla Toplama ve Çıkarma", "sayfalar": "s. 62–72",
        "giris": "Sayı doğrusunda yürümeyi biliyorsun. Bu konuda eksi ve artı sayıları toplayıp çıkaracağız. Asansörle inip çıkmak, borç almak, denizaltının yükselmesi: hepsi birer toplama ya da çıkarma işlemi.",
        "hazirlik": {
            "baslik": "Hazır mısın?",
            "giris": "Bu konu; sayı doğrusu, işaret kelimeleri ve mutlak değer üzerine kuruluyor. Önce bunları hatırlıyor musun bakalım. Not yok; sadece nereden başlayacağımızı bulacağız.",
            "maddeler": [
                {"ad": "Eksi sayılar sayı doğrusunda", "sinif": "1. konu", "svg": svg_dogru(),
                 "anlatim": "Sayı doğrusunda 0'ın sağında pozitif sayılar, solunda negatif sayılar vardır. Eksi bir sayıyı bulmak için 0'dan sola doğru sayarız.",
                 "akilda": "Sol eksi, sağ artı",
                 "ornek": {"problem": f"{M}3'ü sayı doğrusunda bulalım.", "adimlar": [
                     {"metin": f"{M}3 eksi bir sayı. Eksi sayılar 0'ın solunda.", "islem": "Yön: sola"},
                     {"metin": "0'dan sola 3 aralık say.",
                      "sayiDogrusu": sd(-5, 3, oklar=[ok(0, -3, "3 aralık", NEG)], isaretler=[{"x": -3, "etiket": f"{M}3", "renk": NEG}]),
                      "islem": f"0 → {M}3"}]},
                 "sorular": [
                     N(f"Sayı doğrusunda {M}5'in yerine dokun.", -5, sd(-7, 5), "0'ı bul. Sola doğru 5 aralık say.", f"{M}5, 0'ın 5 birim solundadır."),
                     S("Hangisi sayı doğrusunda 0'ın solundadır?", ["4", "0", f"{M}4"], 2, "0'ın solunda eksi sayılar vardır.", f"{M}4 negatiftir, 0'ın solundadır.")]},
                {"ad": "Kelimeden sayıya", "sinif": "1. konu", "svg": svg_kelime(),
                 "anlatim": "Sözel problemlerde işareti kelime söyler. Altı, borç, gider, zarar, aşağı → eksi. Üstü, alacak, gelir, kâr, yukarı → artı.",
                 "akilda": "Kelime işareti söyler",
                 "ornek": {"problem": "Berk arkadaşından 65 TL borç aldı. Bunu tam sayıyla yazalım.", "adimlar": [
                     {"metin": "İşaret kelimesini bul: borç.", "islem": "Borç → eksi"},
                     {"metin": "Sayıyı işaretiyle yaz.", "islem": f"{M}65"}]},
                 "sorular": [
                     G("Deniz seviyesinin 100 metre altındaki bir denizaltının konumunu tam sayıyla yaz.", "-100",
                       f"\"Altında\" eksi demek. Önce {M} tuşuna dokun.", f"Deniz seviyesinin 100 m altı: {M}100 m.", birim="m"),
                     S("Hangisi artı (+) ile gösterilir?", ["5 TL borç", "3 kat aşağı", "20 TL kâr"], 2,
                       "Kâr mı, borç mu, aşağı mı? Hangisi artı kelimesi?", "Kâr artıdır: +20. Borç ve aşağı eksidir.")]},
                {"ad": "Mutlak değer", "sinif": "3. konu", "svg": svg_mutlak(),
                 "anlatim": "Bir sayının 0'a uzaklığına mutlak değer denir. Kısa yol: işareti sil, sayı kalır. Mutlak değer hiç eksi olmaz.",
                 "akilda": "İşareti sil, sayı kalır",
                 "ornek": {"problem": f"|{M}9| kaçtır?", "adimlar": [
                     {"metin": f"{M}9, 0'dan kaç birim uzakta?", "islem": "9 birim"},
                     {"metin": "Uzaklık eksi olmaz.", "islem": f"|{M}9| = 9"}]},
                 "sorular": [
                     G(f"|{M}15| kaçtır?", "15", "İşareti sil, sayı kalır.", f"|{M}15| = 15."),
                     S("Hangisinin mutlak değeri en büyüktür?", [f"{M}12", "8", "0"], 0,
                       "Her sayının işaretini sil. Hangisi 0'a en uzak?", f"|{M}12| = 12, |8| = 8, |0| = 0. En büyüğü 12.")]}
            ]},
        "kavramlar": [
            {"ad": "Toplama Bir Yolculuktur", "renk": "#1f9e8f", "svg": svg6_yolculuk(),
             "aciklama": "Toplamayı sayı doğrusunda bir yolculuk gibi düşün. Birinci sayıdan başla. Artı bir sayı eklersen sağa, eksi bir sayı eklersen sola git.",
             "ek": "Kitapta oyun puanları ve asansör örnekleri sayı doğrusunda böyle gösteriliyor: + işaretli puanlar sağa, − işaretli puanlar sola. (s. 63–64)",
             "akilda": "Artı sağa, eksi sola",
             "sayiDogrusu": sd(-5, 3, oklar=[ok(0, -4, f"{M}4", NEG), ok(-4, -2, "+2", POS)], isaretler=[{"x": -2, "etiket": f"{M}2", "renk": NEG}]),
             "cozum": {"baslik": "Seda hangi katta?",
                       "problem": "Seda zemin kattan asansöre bindi. Önce 4 kat aşağı indi, sonra 2 kat yukarı çıktı. Seda şimdi hangi katta?",
                       "sayiDogrusu": kat(-5, 2, oklar=[ok(0, -4, "4 aşağı", NEG), ok(-4, -2, "2 yukarı", POS)]),
                       "adimlar": [
                           {"metin": "Başlangıç (0) nerede? Zemin kat.", "islem": "Zemin kat = 0"},
                           {"metin": "4 kat aşağı indi. Aşağı eksidir: 0'dan 4 aralık aşağı.", "islem": f"0 + ({M}4) = {M}4"},
                           {"metin": f"2 kat yukarı çıktı. Yukarı artıdır: {M}4'ten 2 aralık yukarı.", "islem": f"({M}4) + (+2) = {M}2"}],
                       "sonuc": f"Seda {M}2. katta, yani zeminin 2 kat altında. İşlem: ({M}4) + (+2) = {M}2. (s. 62)"},
             "sende": {"baslik": "Ali asansörde",
                       "problem": "Ali zemin katın 6 kat altında. Asansörle 12 kat yukarı çıktı. Ali şimdi hangi katta?",
                       "sayiDogrusu": sd(-7, 7),
                       "adimlar": [
                           {"metin": "Başlangıç: Ali nerede?",
                            "soru": G("Ali'nin ilk katını tam sayıyla yaz.", "-6", f"Zeminin altı eksidir. Önce {M} tuşuna dokun.", f"Zeminin 6 kat altı: {M}6."),
                            "islem": f"Başlangıç: {M}6"},
                           {"metin": "Yön ve kaç birim? 12 kat yukarı.",
                            "soru": S("12 kat yukarı nasıl yazılır?", [f"{M}12", "+12", "0"], 1, "Yukarı artı mı, eksi mi?", "Yukarı artıdır: +12."),
                            "islem": "+12"},
                           {"metin": f"Yolculuğu yap: {M}6'dan sağa 12 aralık git.",
                            "soru": N(f"({M}6) + (+12) işleminin sonucuna dokun.", 6, sd(-7, 7),
                                      f"{M}6'dan başla. 6 aralık sağa gidince 0'a varırsın. Kalan aralıkları da say.", f"{M}6'dan 12 aralık sağa: +6."),
                            "islem": f"({M}6) + (+12) = +6"}],
                       "sonuc": "Harika! Ali şimdi 6. katta. (s. 64)"},
             "soru": N(f"({M}3) + (+5) işleminin sonucuna dokun.", 2, sd(-6, 6),
                       f"{M}3'ten başla. +5 artı: sağa 5 aralık git.", f"{M}3'ten sağa 5 aralık: {M}2, {M}1, 0, 1, 2. Sonuç +2. (s. 64)")},
            {"ad": "Aynı İşaret: Topla, İşareti Koru", "renk": "#7b4fc9", "svg": svg6_ayni(),
             "aciklama": "İki sayının işareti aynıysa mutlak değerlerini topla. Sonucun başına ortak işaretlerini yaz.",
             "ek": f"(+11) + (+8) = +19 ve ({M}20) + ({M}7) = {M}27. İki borç birleşince borç büyür; iki kâr birleşince kâr büyür. (s. 65)",
             "akilda": "Aynı işaret: topla, işareti koru",
             "cozum": {"baslik": "Berk'in toplam borcu",
                       "problem": "Berk kitap almak için arkadaşından 65 TL, kuzeninden 85 TL borç aldı. Toplam borcunu tam sayıyla yazalım.",
                       "adimlar": [
                           {"metin": "Kelimeye bak: borç eksidir.", "islem": f"Arkadaşı: {M}65, kuzeni: {M}85"},
                           {"metin": "İşlemi yaz.", "islem": f"({M}65) + ({M}85)"},
                           {"metin": "İşaretler aynı (ikisi de eksi). Mutlak değerleri topla.", "islem": "65 + 85 = 150"},
                           {"metin": "Ortak işareti başa yaz.", "islem": f"({M}65) + ({M}85) = {M}150"}],
                       "sonuc": f"Berk'in toplam borcu 150 TL; tam sayıyla {M}150. (s. 62)"},
             "soru": S(f"({M}20) + ({M}7) kaçtır?", [f"{M}13", "+27", f"{M}27"], 2,
                       "İşaretler aynı mı? Aynıysa 20 ile 7'yi topla, ortak işareti koru.",
                       f"İkisi de eksi: 20 + 7 = 27, işaret eksi: {M}27. (s. 65)")},
            {"ad": "Farklı İşaret: Çıkar, Büyüğün İşareti", "renk": "#e8590c", "svg": svg6_farkli(),
             "aciklama": "İşaretler farklıysa mutlak değeri büyük olandan küçük olanı çıkar. Sonuca, mutlak değeri büyük olanın işaretini koy.",
             "ek": f"({M}15) + (+6) = {M}9: 15 − 6 = 9, büyük olan {M}15. ({M}12) + (+16) = +4: 16 − 12 = 4, büyük olan +16. İp çekme oyunu gibi düşün: güçlü taraf kazanır, fark kadar. (s. 65)",
             "akilda": "Farklı işaret: çıkar, büyüğün işareti",
             "cozum": {"baslik": "Denizaltı yükseliyor",
                       "problem": "Deniz seviyesinin 100 metre altındaki bir denizaltı, yüzeye yaklaşmak için 50 metre yükseldi. Yeni konumu ne?",
                       "adimlar": [
                           {"metin": "Başlangıç (0) nerede? Deniz seviyesi. Denizaltı altında: eksi.", "islem": f"Başlangıç: {M}100"},
                           {"metin": "Yön: yükseldi, yukarı artıdır. Kaç metre?", "islem": "+50"},
                           {"metin": "İşaretler farklı: büyükten küçüğü çıkar.", "islem": f"({M}100) + (+50) → 100 {M} 50 = 50"},
                           {"metin": f"Mutlak değeri büyük olan {M}100. Onun işaretini koy.", "islem": f"({M}100) + (+50) = {M}50"}],
                       "sonuc": f"Denizaltı deniz seviyesinin 50 m altında: {M}50 m. (s. 62)"},
             "sende": {"baslik": "Mehmet'in bakiyesi",
                       "problem": f"Mehmet'in banka hesabında {M}175 TL var (bu bir borç). Hesabına 100 TL yatırdı. Yeni bakiyesi ne?",
                       "adimlar": [
                           {"metin": "İşlemi yaz: para yatırmak artıdır.", "islem": f"({M}175) + (+100)"},
                           {"metin": "İşaretler farklı. Büyükten küçüğü çıkar.",
                            "soru": G(f"175 {M} 100 kaçtır?", "75", "175'ten 100 çıkar.", f"175 {M} 100 = 75."),
                            "islem": f"175 {M} 100 = 75"},
                           {"metin": "Hangi sayının mutlak değeri büyük? Onun işaretini koy.",
                            "soru": S("Sonucun işareti ne olur?", ["Eksi, çünkü 175 daha büyük", "Artı, çünkü para yatırdı", "İşareti olmaz"], 0,
                                      "175 mi büyük, 100 mü? Büyük olanın işareti ne?", f"Mutlak değeri büyük olan {M}175; işaret eksi."),
                            "islem": f"({M}175) + (+100) = {M}75"}],
                       "sonuc": f"Harika! Mehmet'in bakiyesi {M}75 TL. Borcu azaldı ama bitmedi. (s. 68)"},
             "soru": G(f"({M}12) + (+16) kaçtır?", "4",
                       "İşaretler farklı: 16 ile 12'nin farkını bul. Hangisinin mutlak değeri büyük?",
                       f"16 {M} 12 = 4. Büyük olan +16, işaret artı: +4. (s. 65)")},
            {"ad": "Ters İşaretliler Toplanınca 0", "renk": "#b7791f", "svg": svg6_ters(),
             "aciklama": "Bir sayı ile ters işaretlisini toplarsan sonuç 0 olur. Sola ne kadar gidersen sağa da o kadar gelirsin.",
             "ek": f"Kitaptaki alıştırmada (+10) + ({M}10) işlemi var: sonuç 0. 3 kat inip 3 kat çıkan kişi yine zemin kattadır. (s. 66)",
             "akilda": "Sayı + tersi = 0",
             "soru": S(f"({M}8) + (+8) kaçtır?", [f"{M}16", "0", "+16"], 1,
                       f"{M}8 ile +8 birbirinin tersi mi? 8 sola, 8 sağa gidersen nereye varırsın?",
                       f"{M}8 ile +8 ters işaretlidir: toplamları 0. (s. 66)")},
            {"ad": "Önce Mutlak Değer", "renk": "#c92a2a", "svg": svg6_mutlak_once(),
             "aciklama": "İşlemde mutlak değer varsa önce onun sonucunu bul. Sonra işleme devam et.",
             "ek": f"|{M}5| + |{M}9| = (+5) + (+9) = 14. Mutlak değer hiç eksi olmaz; bu yüzden ikisi de artı olur. (s. 66)",
             "akilda": "Önce | | çözülür",
             "soru": G(f"|{M}3| + ({M}8) kaçtır?", "-5",
                       f"Önce |{M}3| kaç, onu bul. Sonra o sayıyı {M}8 ile topla.",
                       f"|{M}3| = 3. (+3) + ({M}8): işaretler farklı, 8 {M} 3 = 5, büyük olan {M}8: {M}5. (s. 66)")},
            {"ad": "Çıkarma = Tersiyle Toplama", "renk": "#1d6fa3", "svg": svg6_cikarma(),
             "aciklama": "Tam sayılarda çıkarma yaparken çıkan sayının işaretini ters çevir ve topla. Sonra toplama kurallarını kullan.",
             "ek": f"(+10) {M} ({M}8) = (+10) + (+8) = +18. ({M}12) {M} (+5) = ({M}12) + ({M}5) = {M}17. 6 {M} 9 = 6 + ({M}9) = {M}3. (s. 69)",
             "akilda": "Çıkarmayı çevir, topla",
             "cozum": {"baslik": "Karabatak ile balık",
                       "problem": "Bir karabatak deniz seviyesinin 10 m üstünde uçuyor. Tam altında bir balık, deniz seviyesinin 6 m altında yüzüyor. Aralarındaki yükseklik farkı kaç metre?",
                       "sayiDogrusu": {"min": -7, "max": 11, "dikey": True, "birim": 16, "sifirEtiketi": "Deniz seviyesi",
                                       "isaretler": [{"x": 10, "etiket": "Karabatak", "renk": POS}, {"x": -6, "etiket": "Balık", "renk": NEG}]},
                       "adimlar": [
                           {"metin": "Başlangıç (0): deniz seviyesi. Konumları yaz.", "islem": f"Karabatak: +10, balık: {M}6"},
                           {"metin": "Farkı bulmak için büyükten küçüğü çıkar.", "islem": f"(+10) {M} ({M}6)"},
                           {"metin": "Çıkarmayı toplamaya çevir: çıkan sayının işaretini ters yap.", "islem": "(+10) + (+6)"},
                           {"metin": "İşaretler aynı: topla.", "islem": "(+10) + (+6) = +16"}],
                       "sonuc": "Fark 16 m. Kontrol: Deniz seviyesinden karabatağa 10 m, balığa 6 m; 10 + 6 = 16. (s. 67)"},
             "sende": {"baslik": "Erzurum'da gece ile gündüz",
                       "problem": f"Erzurum'da gündüz sıcaklığı {M}5 °C, gece sıcaklığı {M}13 °C. Gündüz ile gece arasında kaç derece fark var?",
                       "sayiDogrusu": {"min": -14, "max": 1, "dikey": True, "birim": 16, "sifirEtiketi": "0 °C",
                                       "isaretler": [{"x": -5, "etiket": "Gündüz", "renk": NEG}, {"x": -13, "etiket": "Gece", "renk": NEG}]},
                       "adimlar": [
                           {"metin": "Farkı bulmak için büyükten küçüğü çıkar. Hangisi büyük?",
                            "soru": S("Hangisi daha büyüktür (daha sıcaktır)?", [f"{M}5 °C", f"{M}13 °C", "İkisi eşit"], 0,
                                      "Dikey sayı doğrusunda hangisi daha yukarıda?", f"{M}5, {M}13'ten yukarıdadır; daha büyüktür."),
                            "islem": f"({M}5) {M} ({M}13)"},
                           {"metin": "Çıkarmayı toplamaya çevir.",
                            "soru": S(f"({M}5) {M} ({M}13) hangisine eşittir?", [f"({M}5) + ({M}13)", f"({M}5) + (+13)", f"(+5) + ({M}13)"], 1,
                                      "Yalnız çıkan sayının işaretini ters çevir. Birinci sayıya dokunma.", f"{M}13'ün tersi +13: ({M}5) + (+13)."),
                            "islem": f"({M}5) + (+13)"},
                           {"metin": "İşaretler farklı: büyükten küçüğü çıkar, büyüğün işaretini koy.",
                            "soru": G(f"({M}5) + (+13) kaçtır?", "8", f"13 {M} 5 kaç? Büyük olan +13.", f"13 {M} 5 = 8, işaret artı: +8.", birim="derece"),
                            "islem": "= +8"}],
                       "sonuc": "Harika! Gündüz ile gece arasında 8 derece fark var. (s. 70)"},
             "soru": G(f"4 {M} ({M}5) kaçtır?", "9", "Çıkarmayı toplamaya çevir: 4 + (+5).", f"4 {M} ({M}5) = 4 + (+5) = 9. (s. 69)")},
            {"ad": "Aradaki Eksi Çıkarmadır", "renk": "#5f3dc4", "svg": svg6_arada(),
             "aciklama": f"{M}4 {M} 5 işleminde ortadaki {M} çıkarma işaretidir. 5'in işareti artıdır, yazılmamıştır: {M}4 {M} 5 = ({M}4) {M} (+5).",
             "ek": f"Sonra çıkarmayı çevirip topla: ({M}4) + ({M}5) = {M}9. Sayının başındaki {M} ile iki sayının arasındaki {M} işaretini karıştırma. (s. 69)",
             "akilda": "Aradaki eksi = çıkar",
             "soru": S(f"{M}4 {M} 5 kaçtır?", [f"{M}1", "+1", f"{M}9"], 2,
                       f"Aradaki {M} çıkarma: ({M}4) {M} (+5). Çevir ve topla.",
                       f"({M}4) {M} (+5) = ({M}4) + ({M}5) = {M}9. (s. 69)")}
        ],
        "biliyorMusun": [
            f"Dünyadaki saatler UTC denen ortak bir zamana göre ayarlanır. İstanbul UTC+3, Tokyo UTC+9, Vancouver UTC{M}8'dir. İstanbul Tokyo'dan 6 saat geride, Vancouver'dan 11 saat ileridedir: (+3) {M} (+9) = {M}6 ve (+3) {M} ({M}8) = +11. (s. 71–72)",
            "Gençtürk ailesi bir ayda lambaları kapatarak 100 TL, cihazları kapatarak 70 TL tasarruf etti; çamaşır makinesi yüzünden 60 TL fazla harcadı. Ailenin aylık değişimi de tam sayılarla toplanarak bulunur. (s. 62)"],
        "akildaKalsin": [
            "Toplama bir yolculuktur: artı sağa, eksi sola.",
            "Aynı işaret: mutlak değerleri topla, ortak işareti koru.",
            "Farklı işaret: büyükten küçüğü çıkar, büyüğün işaretini koy.",
            "Bir sayı ile ters işaretlisinin toplamı 0'dır.",
            f"Çıkarmayı çevir, topla: 4 {M} ({M}5) = 4 + (+5).",
            "İşlemde | | varsa önce onu çöz."],
        "merakKutusu": [
            {"soru": "Pozitif sayının başına + yazmak zorunlu mu?", "cevap": f"Hayır. Pozitif sayıların + işareti çoğu zaman yazılmaz: 7 = +7. Ama negatif sayıların {M} işareti mutlaka yazılır. (s. 66)"},
            {"soru": "Neden çıkarmayı toplamaya çeviriyoruz?", "cevap": f"Çünkü toplama kurallarını zaten biliyoruz. Bir sayıyı çıkarmak, tersini eklemekle aynı sonucu verir. Karabatak örneğinde 10 {M} ({M}6) ile 10 + 6 aynı sonucu verdi. (s. 67)"},
            {"soru": "Toplayınca sayı hep büyür mü?", "cevap": f"Hayır. Eksi bir sayı eklersen sonuç küçülür: 5 + ({M}3) = 2. Sayı doğrusunda sola gitmiş olursun. (s. 65)"},
            {"soru": "İki eksi sayının toplamı artı olabilir mi?", "cevap": f"Hayır. İki borç birleşince borç büyür: ({M}3) + ({M}4) = {M}7. (s. 65)"},
            {"soru": "Saat dilimleri neden + ve − ile yazılır?", "cevap": "Bir ülkenin saati UTC'ye göre ileride ise + , geride ise − ile gösterilir. UTC+3, İstanbul'un saatinin 3 saat ileride olduğunu söyler. (s. 71)"}],
        "dusunVeYaz": [{"soru": f"Hesabında {M}40 TL olan birine 25 TL para yatırılıyor. Yeni bakiyeyi bul ve nasıl bulduğunu anlat.",
                        "ornekCevap": f"({M}40) + (+25) işlemini yaparım. İşaretler farklı: 40 {M} 25 = 15. 40 daha büyük ve eksi, sonuç {M}15 TL. Borç azaldı ama bitmedi.",
                        "anahtarlar": ["farklı", "çıkar", "büyük", "15", "eksi"]}],
        "sorular": [
            G("Bir oyunda Alperen 1. bölümde 3 puan kaybetti, 2. bölümde 8 puan kazandı. Oyun sonu puanı kaçtır?", "5",
              f"Kaybetmek eksi, kazanmak artı: ({M}3) + (+8).", f"({M}3) + (+8): 8 {M} 3 = 5, büyük olan +8: +5 puan. (s. 63)", birim="puan"),
            S(f"({M}6) + ({M}5) + ({M}12) kaçtır?", [f"{M}23", "+23", f"{M}1"], 0,
              "Üçünün de işareti aynı. Mutlak değerleri topla, ortak işareti koru.", f"6 + 5 + 12 = 23, işaret eksi: {M}23. (s. 66)"),
            N(f"(+2) + ({M}7) işleminin sonucuna dokun.", -5, sd(-8, 4),
              f"+2'den başla. {M}7 eksi: sola 7 aralık git.", f"+2'den sola 7 aralık: {M}5. (s. 66)"),
            S("Hangisinin sonucu 0'dır?", ["(+7) + (+7)", f"({M}9) + (+9)", f"({M}5) + (+4)"], 1,
              "Hangisinde bir sayı ile ters işaretlisi toplanıyor?", f"{M}9 ile +9 ters işaretlidir: toplamları 0. (s. 66)"),
            G(f"(+5) {M} (+25) kaçtır?", "-20",
              f"Çıkarmayı toplamaya çevir: (+5) + ({M}25).", f"(+5) + ({M}25): 25 {M} 5 = 20, büyük olan {M}25: {M}20. (s. 69)"),
            S(f"Esma Hanım'ın hesabında {M}100 TL var. Hesabına 75 TL yatırdı. Yeni bakiyeyi hangi işlem verir?",
              [f"({M}100) + 75", f"({M}100) {M} 75", f"({M}100) + ({M}75)"], 0,
              "Para yatırmak artı mı, eksi mi? Bakiyeye eklenir mi, çıkar mı?", f"Yatırmak artıdır: ({M}100) + 75 = {M}25 TL. (s. 68)"),
            G(f"|{M}5| + |{M}9| kaçtır?", "14", "Önce mutlak değerleri bul, sonra topla.", f"|{M}5| = 5, |{M}9| = 9. 5 + 9 = 14. (s. 66)"),
            S(f"{M}3 {M} 4 {M} 5 kaçtır?", [f"{M}12", f"{M}4", "+6"], 0,
              f"Aradaki her {M} çıkarmadır: ({M}3) + ({M}4) + ({M}5).", f"({M}3) + ({M}4) + ({M}5) = {M}12. (s. 69)"),
            N("Ece zemin katta. Önce 5 kat aşağı indi, sonra 3 kat yukarı çıktı. Ece'nin katına dokun.", -2, kat(-6, 3),
              "Zemin kat 0. 5 aralık aşağı, sonra 3 aralık yukarı.", f"({M}5) + (+3) = {M}2. Ece {M}2. katta. (s. 62)"),
            G("Bir havucun yaprak ucu toprağın 18 cm üstünde, kök ucu toprağın 12 cm altında. Yaprak ucu ile kök ucu arasında kaç cm var?", "30",
              f"Toprak seviyesi 0. Yaprak +18, kök {M}12. Büyükten küçüğü çıkar.", f"(+18) {M} ({M}12) = (+18) + (+12) = 30 cm. (s. 68)", birim="cm")]
    }


# ---------- u1k7 çizimleri ----------
def svg6_carpim():
    g = "".join(f"<circle cx='{30 + i * 20}' cy='{24 + j * 20}' r='7' fill='{OB}'/>" for i in range(4) for j in range(3))
    g += txt(60, 100, "3 · 4 = 12", "#f5f6fa", 16)
    return bg(g)


def svg6_bolme_ters():
    g = txt(60, 42, "12 ÷ 3 = 4", "#f5f6fa", 16)
    g += "<path d='M50 54 v18 M70 54 v18' stroke='#f2c14e' stroke-width='3'/><path d='M50 50 l-5 7 h10z M70 76 l-5 -7 h10z' fill='#f2c14e'/>"
    g += txt(60, 100, "3 · 4 = 12", OB, 16)
    return bg(g)


def svg6_tekrar():
    g = txt(60, 30, f"4 · ({M}2)", "#f5f6fa", 16)
    g += _sd_mini(80, range(-8, 1), 12, 12, etiket=(-8, -4, 0))
    for a, b in ((108, 84), (84, 60), (60, 36), (36, 12)):
        g += f"<path d='M{a} 72 Q{(a + b) / 2:.0f} 50 {b} 72' stroke='{NB}' stroke-width='2.6' fill='none' stroke-linecap='round'/>"
    return bg(g)


def svg6_isaret(vurgu):
    g = txt(30, 34, "·", "#9aa3bf", 20) + txt(70, 34, "+", OB, 20) + txt(98, 34, M, NB, 20)
    g += txt(30, 66, "+", OB, 20) + txt(30, 98, M, NB, 20)
    g += "<path d='M18 42 h96 M44 14 v96' stroke='#5a6280' stroke-width='2'/>"
    hucre = {(0, 0): "+", (0, 1): M, (1, 0): M, (1, 1): "+"}
    for (r, c), s in hucre.items():
        x, y = 70 + c * 28, 60 + r * 32
        isik = (r == c) == (vurgu == "ayni")
        if isik:
            g += f"<rect x='{x - 13}' y='{y - 15}' width='26' height='26' rx='7' fill='none' stroke='#f2c14e' stroke-width='2.5'/>"
        g += txt(x, y + 6, s, OB if s == "+" else NB, 20 if isik else 16, 800 if isik else 600)
    return bg(g)


def svg6_eksileri():
    g = "".join(f"<circle cx='{x}' cy='44' r='14' fill='{NB}'/>" + txt(x, 51, M, "#1b2340", 20) for x in (24, 60, 96))
    g += "<path d='M24 60 Q42 80 60 60' stroke='#f2c14e' stroke-width='2.5' fill='none'/>" + txt(42, 90, "+", OB, 16)
    g += txt(60, 112, f"3 eksi: tek → {M}", "#f5f6fa", 12)
    return bg(g)


def svg6_maden():
    g = "<line x1='14' y1='20' x2='106' y2='20' stroke='#c98a4b' stroke-width='3'/>" + txt(26, 16, "0", "#f2c14e", 12)
    g += "<rect x='50' y='20' width='20' height='90' fill='#2b355c' stroke='#9aa3bf' stroke-width='1.5'/>"
    for k in range(1, 7):
        g += f"<circle cx='78' cy='{20 + k * 14}' r='3.5' fill='#f2c14e'/>"
    g += f"<rect x='53' y='92' width='14' height='14' rx='2' fill='{OB}'/>" + txt(30, 110, f"{M}24", NB, 13)
    g += txt(96, 62, "4 m", "#f2c14e", 11)
    return bg(g)


def svg6_gosterim():
    g = txt(60, 30, f"({M}12) ÷ 2", "#f5f6fa", 15) + txt(60, 56, f"({M}12) : 2", "#f5f6fa", 15)
    g += txt(44, 80, f"{M}12", "#f5f6fa", 15) + "<line x1='28' y1='86' x2='60' y2='86' stroke='#f5f6fa' stroke-width='2.5'/>" + txt(44, 104, "2", "#f5f6fa", 15)
    g += txt(92, 94, f"= {M}6", NB, 16)
    return bg(g)


def svg6_carp_bol():
    g = "<line x1='60' y1='16' x2='60' y2='104' stroke='#5a6280' stroke-width='2'/>"
    g += txt(30, 46, "×", "#f2c14e", 28) + txt(90, 46, "÷", "#f2c14e", 28)
    for x in (12, 24, 36):
        g += f"<path d='M{x} 70 q6 -10 12 0' stroke='{NB}' stroke-width='2.5' fill='none'/>"
    g += f"<rect x='68' y='62' width='44' height='12' rx='3' fill='{NB}'/><path d='M83 60 v16 M97 60 v16' stroke='#1b2340' stroke-width='2.5'/>"
    g += txt(30, 100, "tekrar", "#f5f6fa", 11) + txt(90, 100, "paylaştır", "#f5f6fa", 10)
    return bg(g)


# =================================================================
def u1k7():
    sd = lambda mn, mx, **ek: dict({"min": mn, "max": mx}, **ek)
    ok = lambda a, b, e, r: {"bas": a, "son": b, "etiket": e, "renk": r}
    return {
        "id": "u1k7", "unite": "1. Tema: Sayılar ve Nicelikler", "baslik": "Tam Sayılarla Çarpma ve Bölme", "sayfalar": "s. 73–81",
        "giris": "Bu konuda eksi ve artı sayılarla çarpma ve bölme yapacağız. İyi haber: işaret kuralı ikisinde de aynı! Klima kumandası, metro kartı ve maden asansörü bize yardım edecek.",
        "hazirlik": {
            "baslik": "Hazır mısın?",
            "giris": "Bu konu çarpım tablosu, bölme ve geçen konudaki toplama kuralı üzerine kuruluyor. Önce bunları hatırlıyor musun bakalım. Not yok.",
            "maddeler": [
                {"ad": "Çarpım tablosu", "sinif": "Önceki yıllar", "svg": svg6_carpim(),
                 "anlatim": "Çarpma, aynı sayıyı tekrar tekrar toplamaktır: 3 · 4 = 4 + 4 + 4 = 12.",
                 "akilda": "Çarpma = tekrarlı toplama",
                 "ornek": {"problem": "6 · 7 kaçtır?", "adimlar": [
                     {"metin": "6 tane 7'yi topla ya da çarpım tablosunu hatırla.", "islem": "7 + 7 + 7 + 7 + 7 + 7"},
                     {"metin": "Sonucu yaz.", "islem": "6 · 7 = 42"}]},
                 "sorular": [
                     G("7 · 8 kaçtır?", "56", "7'ler tablosunu say: 7, 14, 21, ... 8 kere.", "7 · 8 = 56."),
                     G("9 · 6 kaçtır?", "54", "9'lar tablosu: 9, 18, 27, ... 6 kere.", "9 · 6 = 54.")]},
                {"ad": "Bölme, çarpmanın tersidir", "sinif": "Önceki yıllar", "svg": svg6_bolme_ters(),
                 "anlatim": "42 ÷ 6 sorusunda \"6 kaç kere 42 eder?\" diye düşün. Bölmeyi çarpmayla kontrol edebilirsin.",
                 "akilda": "Bölmeyi çarpmayla kontrol et",
                 "ornek": {"problem": "24 ÷ 4 kaçtır?", "adimlar": [
                     {"metin": "4 kaç kere 24 eder?", "islem": "4 · 6 = 24"},
                     {"metin": "Demek ki:", "islem": "24 ÷ 4 = 6"}]},
                 "sorular": [
                     G("56 ÷ 8 kaçtır?", "7", "8 kaç kere 56 eder?", "8 · 7 = 56, yani 56 ÷ 8 = 7."),
                     S("72 ÷ 9 kaçtır?", ["7", "8", "9"], 1, "9 kaç kere 72 eder?", "9 · 8 = 72, yani 72 ÷ 9 = 8.")]},
                {"ad": "Eksi sayıları toplama", "sinif": "6. konu", "svg": svg6_ayni(),
                 "anlatim": f"İki eksi sayıyı toplarken mutlak değerleri topla, eksiyi koru: ({M}2) + ({M}2) = {M}4.",
                 "akilda": "Aynı işaret: topla, işareti koru",
                 "ornek": {"problem": f"({M}3) + ({M}3) + ({M}3) kaçtır?", "adimlar": [
                     {"metin": "İlk ikisini topla.", "islem": f"({M}3) + ({M}3) = {M}6"},
                     {"metin": "Üçüncüyü ekle.", "islem": f"({M}6) + ({M}3) = {M}9"}]},
                 "sorular": [
                     G(f"({M}5) + ({M}5) kaçtır?", "-10", "İşaretler aynı: 5 + 5, işaret eksi.", f"5 + 5 = 10, işaret eksi: {M}10."),
                     S(f"({M}2) + ({M}2) + ({M}2) kaçtır?", [f"{M}6", "+6", f"{M}4"], 0, "Üç tane 2'yi topla, eksiyi koru.", f"2 + 2 + 2 = 6, işaret eksi: {M}6.")]}
            ]},
        "kavramlar": [
            {"ad": "Çarpma = Tekrarlı Toplama", "renk": "#1f9e8f", "svg": svg6_tekrar(),
             "aciklama": f"4 · ({M}2), dört tane ({M}2)'yi toplamak demektir: ({M}2) + ({M}2) + ({M}2) + ({M}2) = {M}8.",
             "ek": f"Klima kumandasında mavi tuşa her basışta sıcaklık 2 °C düşer. Mavi tuşa 4 kez basınca sıcaklık 4 · ({M}2) = {M}8 °C değişir. (s. 73)",
             "akilda": "Kaç kere? Neyi? Topla",
             "sayiDogrusu": sd(-9, 1, oklar=[ok(0, -2, f"{M}2", NEG), ok(-2, -4, f"{M}2", NEG), ok(-4, -6, f"{M}2", NEG), ok(-6, -8, f"{M}2", NEG)]),
             "cozum": {"baslik": "Klima kumandası",
                       "problem": "Klimanın mavi tuşuna her basışta oda sıcaklığı 2 °C azalıyor. Ela tuşa 3 kez bastı. Sıcaklık ne kadar değişti?",
                       "adimlar": [
                           {"metin": "Her basışta ne oluyor? Azalmak eksidir.", "islem": f"Bir basış: {M}2"},
                           {"metin": "Kaç kez? 3 kez. Tekrarlı toplama yaz.", "islem": f"({M}2) + ({M}2) + ({M}2)"},
                           {"metin": "Aynı işaret: topla, eksiyi koru.", "islem": f"= {M}6"},
                           {"metin": "Bunu çarpmayla da yazabiliriz.", "islem": f"3 · ({M}2) = {M}6"}],
                       "sonuc": f"Sıcaklık 6 °C azaldı: 3 · ({M}2) = {M}6. (s. 73)"},
             "soru": G(f"2 · ({M}5) kaçtır?", "-10", f"2 tane ({M}5)'i topla.", f"({M}5) + ({M}5) = {M}10. (s. 73)")},
            {"ad": "Farklı İşaret: Çarpım Eksi", "renk": "#e8590c", "svg": svg6_isaret("farkli"),
             "aciklama": "Farklı işaretli iki tam sayının çarpımı negatiftir. Önce sayıları işaretsiz çarp, sonra başına eksi koy.",
             "ek": f"({M}6) · (+3) = {M}18 ve (+9) · ({M}1) = {M}9. (s. 74)",
             "akilda": "Farklı işaret → eksi",
             "cozum": {"baslik": "Metro kartı",
                       "problem": "Metroya her binişte öğrencinin kartından 7 TL düşüyor. Öğrenci bir günde 6 kez metroya bindi. Kartındaki bakiye ne kadar değişti?",
                       "adimlar": [
                           {"metin": "Her binişte ne oluyor? Para düşüyor: eksi.", "islem": f"Bir biniş: {M}7"},
                           {"metin": "Kaç kez? 6 kez. Çarpma yaz.", "islem": f"6 · ({M}7)"},
                           {"metin": "Önce işaretsiz çarp.", "islem": "6 · 7 = 42"},
                           {"metin": "İşaretler farklı (+ ve −): sonuç eksi.", "islem": f"6 · ({M}7) = {M}42"}],
                       "sonuc": f"Bakiye 42 TL azaldı: {M}42. (s. 74)"},
             "sende": {"baslik": "Su deposu",
                       "problem": "Bir su deposundan her gün 4 litre su boşaltılıyor. 5 gün sonunda depodaki su ne kadar değişir?",
                       "adimlar": [
                           {"metin": "Her gün değişim ne? Boşaltmak eksidir.",
                            "soru": G("Bir günlük değişimi tam sayıyla yaz.", "-4", f"Boşaltmak eksi. Önce {M} tuşuna dokun.", f"Her gün {M}4 L.", birim="L"),
                            "islem": f"Bir gün: {M}4"},
                           {"metin": "5 gün: çarpma yaz ve önce işaretsiz çarp.",
                            "soru": G("5 · 4 kaçtır?", "20", "5'ler tablosu: 5, 10, 15, 20.", "5 · 4 = 20."),
                            "islem": "5 · 4 = 20"},
                           {"metin": "İşaretler farklı. Sonucun işareti ne?",
                            "soru": S(f"5 · ({M}4) kaçtır?", ["+20", f"{M}20", f"{M}9"], 1, "Farklı işaretlerin çarpımı artı mı, eksi mi?", f"Farklı işaret → eksi: {M}20."),
                            "islem": f"5 · ({M}4) = {M}20"}],
                       "sonuc": f"Harika! Depodaki su 20 L azalır: {M}20. (s. 74)"},
             "soru": S(f"({M}6) · (+3) kaçtır?", [f"{M}18", "+18", f"{M}3"], 0,
                       "Önce 6 · 3'ü bul. İşaretler farklı mı?", f"6 · 3 = 18, işaretler farklı: {M}18. (s. 74)")},
            {"ad": "Aynı İşaret: Çarpım Artı", "renk": "#7b4fc9", "svg": svg6_isaret("ayni"),
             "aciklama": f"Aynı işaretli iki tam sayının çarpımı pozitiftir: (+4) · (+8) = +32, ({M}5) · ({M}7) = +35.",
             "ek": f"Kitaptaki örüntüye bak: 2 · ({M}2) = {M}4, 1 · ({M}2) = {M}2, 0 · ({M}2) = 0. Her adımda sonuç 2 artıyor. Devam edince ({M}1) · ({M}2) = +2 olur. (s. 73–74)",
             "akilda": "Aynı işaret → artı",
             "cozum": {"baslik": "Örüntüyü sürdürelim",
                       "problem": f"3 · ({M}2) = {M}6, 2 · ({M}2) = {M}4, 1 · ({M}2) = {M}2, 0 · ({M}2) = 0. Sonra ne gelir?",
                       "adimlar": [
                           {"metin": "Soldaki sayı her seferinde 1 azalıyor.", "islem": f"3, 2, 1, 0, {M}1, …"},
                           {"metin": "Sonuç her seferinde 2 artıyor.", "islem": f"{M}6, {M}4, {M}2, 0, …"},
                           {"metin": "0'dan sonra 2 artarsa?", "islem": f"({M}1) · ({M}2) = +2"},
                           {"metin": "Bir adım daha.", "islem": f"({M}2) · ({M}2) = +4"}],
                       "sonuc": "İki eksi sayının çarpımı artı çıktı. (s. 73)"},
             "soru": S(f"({M}5) · ({M}7) kaçtır?", [f"{M}35", "+35", f"{M}12"], 1,
                       "Önce 5 · 7'yi bul. İşaretler aynı mı?", "5 · 7 = 35, işaretler aynı: +35. (s. 74)")},
            {"ad": "Çok Çarpanda Eksileri Say", "renk": "#c92a2a", "svg": svg6_eksileri(),
             "aciklama": "Çok sayıda çarpan varsa eksi işaretlerini say. Eksi sayısı çiftse sonuç artı, tekse sonuç eksi olur.",
             "ek": f"Her iki eksi birbirini artıya çevirir. ({M}2) · ({M}3) · ({M}4): ilk ikisi +6 yapar, (+6) · ({M}4) = {M}24. Bir sayı 0 ile çarpılırsa sonuç her zaman 0'dır: 0 · ({M}22) = 0. (s. 75)",
             "akilda": "Çift eksi artı, tek eksi eksi",
             "soru": S(f"({M}2) · ({M}3) · ({M}4) çarpımının işareti nedir?", ["Artı", "Sıfır", "Eksi"], 2,
                       "Kaç tane eksi var? Çift mi, tek mi?", f"3 eksi var, 3 tek: sonuç eksi. ({M}2) · ({M}3) · ({M}4) = {M}24. (s. 75)")},
            {"ad": "Bölmede Aynı Kural", "renk": "#3274d6", "svg": svg6_maden(),
             "aciklama": "Bölmede de işaret kuralı çarpmadakiyle aynıdır: aynı işaret → artı, farklı işaret → eksi.",
             "ek": f"(+25) ÷ (+5) = +5, ({M}72) ÷ ({M}9) = +8, ({M}33) ÷ (+11) = {M}3. Bölen 0 olamaz. (s. 77)",
             "akilda": "Bölmede de aynı kural",
             "cozum": {"baslik": "Maden asansörü",
                       "problem": "Bir maden asansörü yer seviyesinden 24 m aşağıya 8 saniyede indi. Her saniye kaç metre yer değiştirdi?",
                       "adimlar": [
                           {"metin": "Başlangıç (0): yer seviyesi. Aşağı eksidir.", "islem": f"Toplam: {M}24 m"},
                           {"metin": "8 saniyeye eşit paylaştır: böl.", "islem": f"({M}24) ÷ 8"},
                           {"metin": "Önce işaretsiz böl.", "islem": "24 ÷ 8 = 3"},
                           {"metin": "İşaretler farklı: sonuç eksi.", "islem": f"({M}24) ÷ 8 = {M}3"}],
                       "sonuc": f"Asansör her saniye 3 m aşağı iniyor: {M}3. (s. 76)"},
             "sende": {"baslik": "Sultan'ın taksitleri",
                       "problem": "Sultan arkadaşından 450 TL borç aldı. Borcunu 3 eşit taksitte ödeyecek. Her taksiti tam sayıyla yazalım.",
                       "adimlar": [
                           {"metin": "Borç eksidir.",
                            "soru": G("Borcu tam sayıyla yaz.", "-450", f"Borç eksi. Önce {M} tuşuna dokun.", f"Borç: {M}450 TL.", birim="TL"),
                            "islem": f"{M}450"},
                           {"metin": "3 eşit parçaya böl. Önce işaretsiz böl.",
                            "soru": G("450 ÷ 3 kaçtır?", "150", "3 kaç kere 450 eder? 3 · 100 = 300, kalan 150.", "3 · 150 = 450, yani 450 ÷ 3 = 150."),
                            "islem": "450 ÷ 3 = 150"},
                           {"metin": "İşaretler farklı. Sonucun işareti ne?",
                            "soru": S(f"({M}450) ÷ 3 kaçtır?", ["+150", f"{M}150", f"{M}147"], 1, "Farklı işaret → artı mı, eksi mi?", f"Farklı işaret → eksi: {M}150."),
                            "islem": f"({M}450) ÷ 3 = {M}150"}],
                       "sonuc": f"Harika! Her taksit {M}150 TL. (s. 77)"},
             "soru": G(f"({M}72) ÷ ({M}9) kaçtır?", "8", "Önce 72 ÷ 9'u bul. İşaretler aynı mı?", "72 ÷ 9 = 8, işaretler aynı: +8. (s. 77)")},
            {"ad": "Bölmenin Farklı Yazılışları", "renk": "#b7791f", "svg": svg6_gosterim(),
             "aciklama": f"Bölme işlemi üç şekilde yazılabilir: ({M}12) ÷ 2, ({M}12) : 2 ya da kesir çizgisiyle [[-12/2]]. Hepsinin sonucu {M}6'dır.",
             "ek": "Kesir çizgisi bölme demektir; bunu 4. konuda da görmüştük. (s. 77)",
             "akilda": "÷ = : = kesir çizgisi",
             "soru": S(f"Hangisi ({M}20) ÷ 5 ile aynı sonucu verir?", [f"({M}20) · 5", f"({M}20) : 5", "20 : 5"], 1,
                       "÷ işaretinin başka yazılışını ara. Sayılar ve işaretleri de aynı kalmalı.", f"({M}20) : 5 = {M}4, ({M}20) ÷ 5 ile aynıdır. (s. 77)")},
            {"ad": "Çarp mı, Böl mü?", "renk": "#5f3dc4", "svg": svg6_carp_bol(),
             "aciklama": "Aynı değişim tekrar ediyorsa çarp. Bir toplamı eşit parçalara ayırıyorsan ya da \"kaç kere?\" diye soruyorsan böl.",
             "ek": f"Metro kartı: 6 kez {M}7 → 6 · ({M}7). Maden asansörü: {M}24 m'yi 8 saniyeye paylaştır → ({M}24) ÷ 8. (s. 74–76)",
             "akilda": "Tekrar → çarp, paylaştır → böl",
             "cozum": {"baslik": "Yarışmada kaç soru?",
                       "problem": f"Bir yarışmada her yanlış cevap {M}3 puan. Tüm sorulara yanlış cevap veren bir yarışmacı {M}75 puan aldı. Kaç soruya cevap verdi?",
                       "adimlar": [
                           {"metin": f"Ne veriliyor? Bir yanlış {M}3, toplam {M}75.", "islem": f"Bir soru: {M}3, toplam: {M}75"},
                           {"metin": f"Ne isteniyor? {M}3 kaç kere {M}75 eder? Bu bir bölme.", "islem": f"({M}75) ÷ ({M}3)"},
                           {"metin": "Önce işaretsiz böl.", "islem": "75 ÷ 3 = 25"},
                           {"metin": "İşaretler aynı: sonuç artı.", "islem": f"({M}75) ÷ ({M}3) = +25"}],
                       "sonuc": "Yarışmacı 25 soruya cevap verdi. (s. 77)"},
             "sende": {"baslik": "Serbest dalış",
                       "problem": "Bir dalgıç her dakika 13 m derine iniyor. Deniz seviyesinden başladı ve 78 m derinliğe ulaştı. Kaç dakika geçti?",
                       "adimlar": [
                           {"metin": "Çarp mı, böl mü? \"Kaç kere?\" diye soruyoruz.",
                            "soru": S("Hangi işlem yapılmalı?", [f"({M}78) ÷ ({M}13)", f"({M}78) · ({M}13)", f"({M}78) + ({M}13)"], 0,
                                      f"{M}13 kaç kere {M}78 eder? Kaç kere sorusu hangi işlem?", f"Kaç kere → böl: ({M}78) ÷ ({M}13)."),
                            "islem": f"({M}78) ÷ ({M}13)"},
                           {"metin": "Önce işaretsiz böl.",
                            "soru": G("78 ÷ 13 kaçtır?", "6", "13'ü say: 13, 26, 39, 52, 65, 78.", "13 · 6 = 78, yani 78 ÷ 13 = 6."),
                            "islem": "78 ÷ 13 = 6"},
                           {"metin": "İşaret ne olur?",
                            "soru": S("Sonucun işareti nedir?", ["Artı, çünkü işaretler aynı", "Eksi, çünkü derine indi", "İşareti olmaz"], 0,
                                      "İki sayının da işareti eksi. Aynı işaret → ?", "Aynı işaret → artı: +6."),
                            "islem": f"({M}78) ÷ ({M}13) = +6"}],
                       "sonuc": "Harika! 6 dakika geçti. (s. 78)"},
             "soru": S("Feyza'nın internet paketinden video izlediği her dakika için 150 MB düşüyor. 15 dakikalık değişimi hangi işlem verir?",
                       [f"15 · ({M}150)", f"({M}150) ÷ 15", f"15 + ({M}150)"], 0,
                       "Aynı değişim 15 kere mi tekrar ediyor, yoksa bir toplamı mı paylaştırıyoruz?", f"Her dakika {M}150, 15 kere: 15 · ({M}150) = {M}2250 MB. (s. 74)")}
        ],
        "biliyorMusun": [
            "Maden ocaklarında madenciler yer altı asansörleriyle iner. Kitaptaki asansörün tüneline her 4 metrede bir işaret lambası konmuş; 24 m inen madenciler 24 ÷ 4 = 6 lamba görür. (s. 76)",
            "Türk sporcu Şahika Ercümen, serbest dalışta tek nefeste 107 m derine inerek 2025'te dünya rekoru kırdı. (s. 78)"],
        "akildaKalsin": [
            f"Çarpma, tekrarlı toplamadır: 4 · ({M}2) = ({M}2) + ({M}2) + ({M}2) + ({M}2).",
            "Aynı işaret → artı; farklı işaret → eksi. Çarpmada da bölmede de.",
            "Çok çarpanda eksileri say: çiftse artı, tekse eksi.",
            "Bölme ÷, : ya da kesir çizgisiyle yazılır. Bölen 0 olamaz.",
            "Aynı değişim tekrar ediyorsa çarp; paylaştırıyorsan ya da \"kaç kere?\" diyorsan böl."],
        "merakKutusu": [
            {"soru": "İki eksinin çarpımı neden artı?", "cevap": f"Kitaptaki örüntüye bak: soldaki çarpanı 1 azalttıkça sonuç 2 artıyor. 0'dan sonra da artmaya devam eder: ({M}1) · ({M}2) = +2. (s. 73)"},
            {"soru": "Çarpma işaretini nasıl yazarız?", "cevap": f"Kitapta nokta (·) kullanılıyor: 6 · ({M}7). Eksi sayıyı parantez içine yazarız ki işaretler karışmasın. (s. 74)"},
            {"soru": "0'a bölebilir miyiz?", "cevap": f"Hayır. Bilgi kutusunda \"böleni sıfırdan farklı\" yazar. Ama 0'ın kendisi bölünebilir: 0 ÷ ({M}15) = 0. (s. 77–78)"},
            {"soru": "Çok sayıyı çarparken işareti hızlı nasıl bulurum?", "cevap": "Eksileri say: çiftse sonuç artı, tekse eksi. Sonra sayıları işaretsiz çarp. (s. 75)"},
            {"soru": "Dağa çıkınca hava neden soğur?", "cevap": "Yükseldikçe hava basıncı azalır, bu yüzden sıcaklık genellikle düşer. Kitaptaki dağcı her 100 m'de 1 °C soğuyan bir yerde tırmanıyor. (s. 80)"}],
        "dusunVeYaz": [{"soru": "Bir arkadaşın \"İki eksi sayının çarpımı da eksidir\" diyor. Ona doğrusunu bir örnekle anlat.",
                        "ornekCevap": f"Yanlış. ({M}5) · ({M}7) = +35. Aynı işaretli iki sayının çarpımı artıdır. Kitaptaki örüntüde de 0 · ({M}2) = 0'dan sonra ({M}1) · ({M}2) = +2 geliyor.",
                        "anahtarlar": ["artı", "aynı", "pozitif", "örüntü"]}],
        "sorular": [
            G(f"(+4) · ({M}10) kaçtır?", "-40", "Önce 4 · 10. İşaretler farklı mı?", f"4 · 10 = 40, işaretler farklı: {M}40. (s. 75)"),
            S(f"({M}10) · ({M}10) kaçtır?", [f"{M}100", "+100", "0"], 1, "İşaretler aynı mı?", "10 · 10 = 100, işaretler aynı: +100. (s. 75)"),
            N("Klimanın mavi tuşuna her basışta sıcaklık 2 °C azalıyor. Tuşa 3 kez basılınca sıcaklık değişimi kaç olur? Sayı doğrusunda dokun.", -6, sd(-8, 2),
              f"0'dan başla, her basışta 2 aralık sola git. 3 kez.", f"3 · ({M}2) = {M}6. (s. 73)"),
            S(f"({M}45) ÷ 9 kaçtır?", ["5", f"{M}36", f"{M}5"], 2, "Önce 45 ÷ 9. İşaretler farklı mı?", f"45 ÷ 9 = 5, işaretler farklı: {M}5. (s. 78)"),
            G(f"({M}144) ÷ ({M}12) kaçtır?", "12", "Önce 144 ÷ 12. İşaretler aynı mı?", "144 ÷ 12 = 12, işaretler aynı: +12. (s. 78)"),
            S(f"({M}3) · ({M}5) · ({M}6) çarpımının işareti nedir?", ["Eksi", "Artı", "Sıfır"], 0,
              "Eksileri say: çift mi, tek mi?", f"3 eksi var, tek: sonuç eksi. ({M}3) · ({M}5) · ({M}6) = {M}90. (s. 75)"),
            G("Bir apartmanda iki kat arası 3 m. Giriş katındaki asansör 18 m aşağı indi. Asansör hangi kata indi?", "-6",
              f"Aşağı eksi: {M}18 m. Her kat 3 m. Kaç kat? Böl.", f"({M}18) ÷ 3 = {M}6. Asansör {M}6. katta. (s. 77)"),
            S(f"Hangisi {M}4'e eşit değildir?", [f"({M}72) ÷ 18", f"72 : ({M}18)", f"({M}72) : ({M}18)"], 2,
              "Hangisinde iki sayının işareti aynı? Aynı işaret → artı.", f"({M}72) : ({M}18) = +4. Diğer ikisinde işaretler farklı: {M}4. (s. 78)"),
            N(f"0 · ({M}22) işleminin sonucuna dokun.", 0, sd(-5, 5),
              "Bir sayıyı 0 ile çarparsan ne olur?", f"0 ile çarpılan her sayı 0 eder: 0 · ({M}22) = 0. (s. 75)"),
            G("Bir dağcı her 100 m yukarı çıktığında hava 1 °C soğuyor. Dağcı 400 m yukarı çıktı. Sıcaklık kaç derece değişti?", "-4",
              f"Önce kaç kere 100 m çıktığını bul: 400 ÷ 100. Her seferinde {M}1 °C.", f"400 ÷ 100 = 4 kere. 4 · ({M}1) = {M}4 °C. (s. 81)", birim="°C")]
    }



# ---------- u1k8 çizimleri ----------
def _serit(x, y, n, dolu, renk, w=60, h=14):
    c = w / n
    return "".join(f"<rect x='{x + i * c:.1f}' y='{y}' width='{c:.1f}' height='{h}' fill='{renk if i < dolu else '#2b355c'}' stroke='#f5f6fa' stroke-width='1.2'/>" for i in range(n))


def svg8_esit_payda():
    g = _serit(12, 12, 5, 2, OB) + _serit(12, 46, 5, 1, OB) + _serit(12, 84, 5, 3, OB)
    g += txt(42, 41, "+", "#f2c14e", 16) + txt(42, 79, "=", "#f2c14e", 16)
    g += kesir_svg(98, 17, "2", "5", "#f5f6fa", 12) + kesir_svg(98, 51, "1", "5", "#f5f6fa", 12) + kesir_svg(98, 89, "3", "5", OB, 12)
    return bg(g)


def svg8_esitle():
    g = _serit(12, 16, 2, 1, NB) + _serit(12, 62, 10, 5, NB)
    g += txt(42, 50, "=", "#f2c14e", 18)
    g += kesir_svg(98, 21, "1", "2", NB, 13) + kesir_svg(98, 67, "5", "10", NB, 13)
    g += txt(60, 108, "dilimler aynı boy", "#f2c14e", 10)
    return bg(g)


def svg8_cikarma():
    g = "<circle cx='30' cy='44' r='17' fill='#f5f6fa'/>" + txt(30, 52, M, "#1b2340", 24)
    g += "<path d='M52 44 h18 M64 38 l7 6 -7 6' stroke='#f2c14e' stroke-width='3' fill='none' stroke-linecap='round' stroke-linejoin='round'/>"
    g += f"<circle cx='92' cy='44' r='17' fill='{OB}'/>" + txt(92, 52, "+", "#1b2340", 24)
    g += txt(60, 88, "çıkan sayının", "#f5f6fa", 11) + txt(60, 104, "işaretini çevir", "#f5f6fa", 11)
    return bg(g)


def svg8_tamli():
    g = f"<circle cx='24' cy='38' r='15' fill='{NB}'/><circle cx='60' cy='38' r='15' fill='{NB}'/>"
    g += f"<circle cx='96' cy='38' r='15' fill='#2b355c' stroke='#f5f6fa' stroke-width='1.5'/><path d='M96 38 L96 23 A15 15 0 0 1 109 30.5 Z' fill='{NB}'/>"
    g += txt(20, 96, M + "2", NB, 16) + kesir_svg(42, 84, "1", "6", NB, 12) + txt(62, 96, "=", "#f2c14e", 15) + kesir_svg(98, 84, "13", "6", NB, 15, M)
    return bg(g)


def svg8_ozellik():
    g = "<rect x='10' y='18' width='40' height='50' rx='8' fill='#2b355c'/><rect x='70' y='18' width='40' height='50' rx='8' fill='#2b355c'/>"
    g += kesir_svg(34, 38, "2", "9", NB, 15, M) + kesir_svg(90, 38, "2", "9", OB, 15) + txt(60, 50, "+", "#f2c14e", 18)
    g += "<path d='M30 74 Q60 88 90 74' stroke='#f2c14e' stroke-width='2.5' fill='none'/><circle cx='60' cy='100' r='13' fill='#f2c14e'/>" + txt(60, 106, "0", "#1b2340", 16)
    return bg(g)


def svg8_dal():
    g = "<rect x='12' y='36' width='62' height='11' rx='5' fill='#c98a4b'/><rect x='52' y='56' width='58' height='11' rx='5' fill='#a86f37'/>"
    g += "<rect x='50' y='30' width='26' height='42' rx='4' fill='none' stroke='#f2c14e' stroke-width='2.5' stroke-dasharray='4 3'/>"
    g += txt(60, 94, "üst üste", "#f2c14e", 12) + txt(60, 109, "bir kez say", "#f5f6fa", 11)
    return bg(g)


# =================================================================
def u1k8():
    sk = lambda mn, mx, b, **ek: dict({"min": mn, "max": mx, "bolme": b}, **ek)
    ok = lambda a, b, e, r: {"bas": a, "son": b, "etiket": e, "renk": r}
    return {
        "id": "u1k8", "unite": "1. Tema: Sayılar ve Nicelikler", "baslik": "Rasyonel Sayılarla Toplama ve Çıkarma", "sayfalar": "s. 82–87",
        "giris": "Kesirleri toplamayı geçen yıllardan, eksi sayıları toplamayı geçen konudan biliyorsun. Şimdi ikisini birleştiriyoruz. Yeni kural yok: kesir bilgisi + tam sayı kuralı = rasyonel sayılarla toplama.",
        "hazirlik": {
            "baslik": "Hazır mısın?",
            "giris": "Bu konu genişletme, kesirlerde toplama ve tam sayılarda toplama üzerine kuruluyor. Önce bunları hatırlıyor musun bakalım. Not yok.",
            "maddeler": [
                {"ad": "Genişletme (denk kesir)", "sinif": "Önceki yıllar", "svg": svg_h_denk(),
                 "anlatim": "Bir kesrin payını ve paydasını aynı sayıyla çarparsak denk bir kesir buluruz. Buna genişletme denir; değer değişmez: [[1/2]] = [[2/4]].",
                 "akilda": "Pay da payda da aynı sayıyla",
                 "ornek": {"problem": "[[2/3]] kesrini paydası 12 olacak şekilde genişletelim.", "adimlar": [
                     {"metin": "3'ü 12 yapan sayıyı bul: 3 · ? = 12.", "islem": "3 · 4 = 12"},
                     {"metin": "Payı da aynı sayıyla çarp: 2 · 4.", "islem": "[[2/3]] = [[8/12]]"}]},
                 "sorular": [
                     G("[[3/4]] kesrini paydası 12 olacak şekilde genişlet.", "9/12", "4 · 3 = 12. Payı da 3 ile çarp.", "3 · 3 = 9, 4 · 3 = 12: [[9/12]].", kesir=True),
                     G("[[2/5]] kesrini paydası 10 olacak şekilde genişlet.", "4/10", "5 · 2 = 10. Payı da 2 ile çarp.", "2 · 2 = 4, 5 · 2 = 10: [[4/10]].", kesir=True)]},
                {"ad": "Kesirlerde toplama", "sinif": "Önceki yıllar", "svg": svg8_esit_payda(),
                 "anlatim": "Paydalar eşitse payları toplarız, payda aynı kalır: [[2/5]] + [[1/5]] = [[3/5]]. Paydalar farklıysa önce genişletip eşitleriz.",
                 "akilda": "Paylar toplanır, payda kalır",
                 "ornek": {"problem": "[[1/2]] + [[1/4]] işlemini yapalım.", "adimlar": [
                     {"metin": "Paydalar farklı: 2 ve 4. 2'yi 4 yapmak için 2 ile genişlet.", "islem": "[[1/2]] = [[2/4]]"},
                     {"metin": "Şimdi payları topla, payda 4 kalır.", "islem": "[[2/4]] + [[1/4]] = [[3/4]]"}]},
                 "sorular": [
                     S("[[2/9]] + [[5/9]] kaçtır?", ["[[7/18]]", "[[7/9]]", "[[3/9]]"], 1, "Paydalar aynı. Yalnızca payları topla.", "2 + 5 = 7, payda 9 kalır: [[7/9]]."),
                     G("[[1/3]] + [[1/6]] kaçtır?", "3/6", "3'ü 6 yap: [[1/3]] = [[2/6]]. Sonra payları topla.", "[[2/6]] + [[1/6]] = [[3/6]] = [[1/2]].", kesir=True, denk=True)]},
                {"ad": "Tam sayılarda toplama", "sinif": "6. konu", "svg": svg6_farkli(),
                 "anlatim": "Aynı işaret: topla, işareti koru. Farklı işaret: büyükten küçüğü çıkar, büyüğün işaretini koy. Çıkarmada çıkan sayının işaretini çevir ve topla.",
                 "akilda": "Aynı topla, farklı çıkar",
                 "ornek": {"problem": "(−7) + (+3) kaçtır?", "adimlar": [
                     {"metin": "İşaretler farklı. Büyükten küçüğü çıkar.", "islem": "7 − 3 = 4"},
                     {"metin": "Mutlak değeri büyük olan −7. Onun işaretini koy.", "islem": "(−7) + (+3) = −4"}]},
                 "sorular": [
                     G("(−9) + (+4) kaçtır?", "-5", "İşaretler farklı: 9 − 4. Büyük olanın işareti ne?", "9 − 4 = 5, büyük olan −9: −5."),
                     S("(−6) − (+2) kaçtır?", ["−4", "−8", "+8"], 1, "Çıkarmayı çevir: (−6) + (−2). Aynı işaret.", "(−6) + (−2) = −8.")]}
            ]},
        "kavramlar": [
            {"ad": "Payda Aynıysa Payları Topla", "renk": "#1f9e8f", "svg": svg8_esit_payda(),
             "aciklama": "Paydalar eşitse yalnızca payları topla; payda aynı kalır. Payları toplarken tam sayı kuralını kullan.",
             "ek": "Negatif kesirde eksi işareti paya aittir: [[-5/10]] ile [[−5/10]] aynı sayıdır. Kitaptaki örnek: ([[-5/10]]) + ([[-2/10]]) işleminde paylar −5 ve −2; aynı işaret: 5 + 2 = 7, eksi kalır: [[-7/10]]. (s. 83)",
             "akilda": "Payda sabit, paylar toplanır",
             "cozum": {"baslik": "Denizaltı iniyor",
                       "problem": "Bir denizaltı deniz seviyesinin [[3/8]] km altında. Sonra [[2/8]] km daha aşağı indi. Denizaltı şimdi nerede?",
                       "sayiDogrusu": sk(-1, 0, 8, oklar=[ok(0, -0.375, "−3/8", NEG), ok(-0.375, -0.625, "−2/8", NEG)]),
                       "adimlar": [
                           {"metin": "Başlangıç (0) nerede? Deniz seviyesi. Altı eksidir.", "islem": "Başlangıç: [[-3/8]]"},
                           {"metin": "Yön: aşağı, yani eksi. Kaç birim? [[2/8]] km.", "islem": "([[-3/8]]) + ([[-2/8]])"},
                           {"metin": "Paydalar aynı (8). Payları topla: (−3) + (−2). Aynı işaret: topla, eksiyi koru.", "islem": "(−3) + (−2) = −5"},
                           {"metin": "Payda 8 kalır.", "islem": "([[-3/8]]) + ([[-2/8]]) = [[-5/8]]"}],
                       "sonuc": "Denizaltı deniz seviyesinin [[5/8]] km altında: [[-5/8]] km. (Kitaptaki denizaltı bağlamı, s. 82)"},
             "soru": N("([[-1/4]]) + ([[3/4]]) işleminin sonucuna dokun.", 0.5, sk(-1, 1, 4),
                       "Paydalar aynı. Payları topla: (−1) + (+3).", "(−1) + (+3) = +2. Sonuç [[2/4]] = [[1/2]]. (s. 83)")},
            {"ad": "Önce Paydaları Eşitle", "renk": "#7b4fc9", "svg": svg8_esitle(),
             "aciklama": "Paydalar farklıysa önce genişletip paydaları eşitle. Sonra payları topla.",
             "ek": "Farklı büyüklükteki dilimler toplanmaz; önce dilimleri aynı boya getiririz. Kitaptaki örnek: ([[-1/2]]) + ([[-1/5]]) = ([[-5/10]]) + ([[-2/10]]) = [[-7/10]]. (s. 83)",
             "akilda": "Önce payda, sonra pay",
             "cozum": {"baslik": "Paydalar 2 ve 5",
                       "problem": "([[-1/2]]) + ([[-1/5]]) işlemini yapalım.",
                       "adimlar": [
                           {"metin": "Paydalar farklı. Ortak payda bul: büyük paydanın katlarını say: 5, 10. 10'u 2 de böler.", "islem": "Ortak payda: 10"},
                           {"metin": "[[-1/2]] kesrini genişlet: 2 · 5 = 10, payı da 5 ile çarp.", "islem": "[[-1/2]] = [[-5/10]]"},
                           {"metin": "[[-1/5]] kesrini genişlet: 5 · 2 = 10, payı da 2 ile çarp.", "islem": "[[-1/5]] = [[-2/10]]"},
                           {"metin": "Payları topla: (−5) + (−2) = −7. Payda 10 kalır.", "islem": "([[-5/10]]) + ([[-2/10]]) = [[-7/10]]"}],
                       "sonuc": "([[-1/2]]) + ([[-1/5]]) = [[-7/10]]. (s. 83)"},
             "sende": {"baslik": "Paydalar 4 ve 8",
                       "problem": "([[-3/4]]) + [[5/8]] işlemini yap.",
                       "adimlar": [
                           {"metin": "4'ü 8 yapabiliriz: 4 · 2 = 8. Payı da 2 ile çarp.",
                            "soru": G("[[-3/4]] kesrini paydası 8 olacak şekilde yaz.", "-6/8", "3 · 2 = ? Eksiyi unutma: önce − tuşu.", "3 · 2 = 6, 4 · 2 = 8: [[-6/8]].", kesir=True, kabul=["6/-8"]),
                            "islem": "[[-3/4]] = [[-6/8]]"},
                           {"metin": "Payları topla: (−6) + (+5).",
                            "soru": G("(−6) + (+5) kaçtır?", "-1", "İşaretler farklı: 6 − 5. Büyük olan −6.", "6 − 5 = 1, büyük olan −6: −1."),
                            "islem": "(−6) + (+5) = −1"},
                           {"metin": "Payda 8 kalır.", "islem": "([[-3/4]]) + [[5/8]] = [[-1/8]]"}],
                       "sonuc": "Harika! Sonuç [[-1/8]]."},
             "soru": G("[[1/2]] + ([[-1/4]]) kaçtır?", "1/4", "[[1/2]] = [[2/4]]. Sonra payları topla: (+2) + (−1).",
                       "[[2/4]] + ([[-1/4]]) = [[1/4]]. (s. 83)", kesir=True, denk=True)},
            {"ad": "Çıkarma = Tersini Ekle", "renk": "#e8590c", "svg": svg8_cikarma(),
             "aciklama": "Rasyonel sayılarda da çıkarmayı toplamaya çevir: çıkan sayının işaretini ters yap ve topla.",
             "ek": "Tam sayılarda nasıl yapıyorsan öyle: önce çevir, sonra paydaları eşitle, sonra topla. (s. 83)",
             "akilda": "Çıkarmayı çevir, topla",
             "cozum": {"baslik": "Kitaptaki örnek",
                       "problem": "([[-3/4]]) − ([[8/12]]) işlemini yapalım.",
                       "adimlar": [
                           {"metin": "Çıkan sayı +[[8/12]]. İşaretini ters çevir, toplamaya geç.", "islem": "([[-3/4]]) + ([[-8/12]])"},
                           {"metin": "Paydaları eşitle: 4 · 3 = 12. Payı da 3 ile çarp.", "islem": "[[-3/4]] = [[-9/12]]"},
                           {"metin": "Payları topla: (−9) + (−8). Aynı işaret: topla, eksiyi koru.", "islem": "(−9) + (−8) = −17"},
                           {"metin": "Payda 12 kalır.", "islem": "([[-3/4]]) − ([[8/12]]) = [[-17/12]]"}],
                       "sonuc": "Sonuç [[-17/12]], yani [[-1 5/12]]. (s. 83)"},
             "soru": S("([[-2/7]]) − ([[3/7]]) kaçtır?", ["[[1/7]]", "[[-5/7]]", "[[-1/7]]"], 1,
                       "Çıkarmayı çevir: ([[-2/7]]) + ([[-3/7]]). Aynı işaret.", "([[-2/7]]) + ([[-3/7]]): 2 + 3 = 5, eksi kalır: [[-5/7]]. (s. 84)")},
            {"ad": "Tam Sayılı Kesirler", "renk": "#c92a2a", "svg": svg8_tamli(),
             "aciklama": "Tam sayılı kesirleri toplarken önce bileşik kesre çevir, sonra işlem yap. Eksi işareti sayının tamamına aittir.",
             "ek": "Kitap ikinci bir yol da gösteriyor: tam kısımları kendi arasında, kesir kısımları kendi arasında toplamak. İkisi aynı sonucu verir; biz birinci yolu kullanacağız. (s. 84)",
             "akilda": "Önce bileşik kesre çevir",
             "cozum": {"baslik": "Kitaptaki örnek",
                       "problem": "([[-2 1/6]]) + ([[1 2/6]]) işlemini yapalım.",
                       "adimlar": [
                           {"metin": "Eksiyi kenara koy: 2 · 6 + 1 = 13. Eksiyi geri ekle.", "islem": "[[-2 1/6]] = [[-13/6]]"},
                           {"metin": "1 · 6 + 2 = 8.", "islem": "[[1 2/6]] = [[8/6]]"},
                           {"metin": "Paydalar aynı. Payları topla: (−13) + (+8). Farklı işaret: 13 − 8 = 5, büyük olan −13.", "islem": "(−13) + (+8) = −5"},
                           {"metin": "Payda 6 kalır.", "islem": "([[-2 1/6]]) + ([[1 2/6]]) = [[-5/6]]"}],
                       "sonuc": "Sonuç [[-5/6]]. (s. 84)"},
             "sende": {"baslik": "Sıra sende",
                       "problem": "([[-1 1/4]]) + [[3/4]] işlemini yap.",
                       "adimlar": [
                           {"metin": "[[-1 1/4]] kesrini bileşik kesre çevir: 1 · 4 + 1.",
                            "soru": G("[[-1 1/4]] bileşik kesir olarak kaçtır?", "-5/4", "1 · 4 + 1 = ? Payda 4 kalır. Eksiyi unutma.", "1 · 4 + 1 = 5: [[-5/4]].", kesir=True, kabul=["5/-4"]),
                            "islem": "[[-1 1/4]] = [[-5/4]]"},
                           {"metin": "Payları topla: (−5) + (+3).",
                            "soru": G("(−5) + (+3) kaçtır?", "-2", "İşaretler farklı: 5 − 3. Büyük olan −5.", "5 − 3 = 2, büyük olan −5: −2."),
                            "islem": "= [[-2/4]]"},
                           {"metin": "Sonucu sadeleştir: 2 ve 4'ü 2 böler.",
                            "soru": S("[[-2/4]] en sade hâliyle hangisi?", ["[[-1/2]]", "[[-2/2]]", "[[1/2]]"], 0, "Pay ve paydayı 2'ye böl. Eksi kalır.", "2 ÷ 2 = 1, 4 ÷ 2 = 2: [[-1/2]]."),
                            "islem": "= [[-1/2]]"}],
                       "sonuc": "Harika! ([[-1 1/4]]) + [[3/4]] = [[-1/2]]."},
             "soru": G("([[-1 1/3]]) + ([[-2/3]]) kaçtır? Tam sayı olarak yaz.", "-2",
                       "Önce [[-1 1/3]] = [[-4/3]]. Sonra payları topla.", "([[-4/3]]) + ([[-2/3]]) = [[-6/3]] = −2. (s. 84)")},
            {"ad": "Toplamanın Özellikleri", "renk": "#1d6fa3", "svg": svg8_ozellik(),
             "aciklama": "Toplarken sayıların yerini değiştirebilir (değişme), istediğin ikisini önce toplayabilirsin (birleşme). 0 eklemek sayıyı değiştirmez (etkisiz eleman).",
             "ek": "Toplamları 0 olan iki sayı birbirinin tersidir (ters eleman): ([[-2/9]]) + [[2/9]] = 0. Kitaptaki örnekte ([[-2/9]] + [[1/3]]) + [[2/9]] işleminde tersler yan yana getirilir: [[1/3]] + 0 = [[1/3]]. Paydaları eşitlemeye bile gerek kalmaz. (s. 86)",
             "akilda": "Tersini bul, 0 yap",
             "soru": S("[[-3/5]] sayısının toplama işlemine göre tersi hangisidir?", ["[[3/5]]", "[[-5/3]]", "0"], 0,
                       "Hangisiyle toplayınca sonuç 0 olur?", "([[-3/5]]) + [[3/5]] = 0. Tersi [[3/5]]. (s. 86)")},
            {"ad": "Problemde Toplama ve Çıkarma", "renk": "#b7791f", "svg": svg8_dal(),
             "aciklama": "Sözel problemde önce iskeleti kur: Başlangıç (0) nerede? Yön hangisi? Kaç birim? Sonra kesirleri topla ya da çıkar.",
             "ek": "Kitaptaki dal probleminde iki dal üst üste bağlanır. Üst üste gelen kısım iki kez sayılmasın diye toplamdan çıkarılır. (s. 87)",
             "akilda": "0? Yön? Kaç birim?",
             "cozum": {"baslik": "Dalları bağlıyoruz",
                       "problem": "Bir dal [[3/4]] m, diğeri [[1 1/2]] m. Dallar [[1/4]] m'lik kısımları üst üste gelecek biçimde bağlandı. Yeni dal kaç metre?",
                       "adimlar": [
                           {"metin": "Ne veriliyor? İki dal ve üst üste gelen kısım. Ne isteniyor? Yeni dalın boyu.", "islem": "[[3/4]] m, [[1 1/2]] m, üst üste [[1/4]] m"},
                           {"metin": "Dalları uç uca topla. [[1 1/2]] = [[3/2]] = [[6/4]].", "islem": "[[3/4]] + [[6/4]] = [[9/4]]"},
                           {"metin": "Üst üste gelen kısım iki kez sayıldı: bir kez çıkar.", "islem": "[[9/4]] − [[1/4]] = [[8/4]]"},
                           {"metin": "Sadeleştir: 8 ÷ 4.", "islem": "[[8/4]] = 2"}],
                       "sonuc": "Yeni dal 2 m. (Kitaptaki dal problemine benzer, s. 87)"},
             "sende": {"baslik": "Denizaltı yükseliyor",
                       "problem": "Bir denizaltı deniz seviyesinin [[3/4]] km altına indi. Sonra [[1/8]] km yukarı çıktı. Denizaltının son konumu ne?",
                       "sayiDogrusu": sk(-1, 0, 8, isaretler=[{"x": -0.75, "etiket": "−3/4", "renk": NEG}]),
                       "adimlar": [
                           {"metin": "Başlangıç (0): deniz seviyesi. Altı eksi.",
                            "soru": G("Denizaltının ilk konumunu rasyonel sayıyla yaz.", "-3/4", "\"Altına\" eksi demek. Önce − tuşu, sonra 3, / ve 4.", "Deniz seviyesinin [[3/4]] km altı: [[-3/4]].", kesir=True, denk=True, kabul=["3/-4"]),
                            "islem": "Başlangıç: [[-3/4]]"},
                           {"metin": "Yön: yukarı, artı. İşlem: ([[-3/4]]) + [[1/8]]. Paydaları eşitle.",
                            "soru": S("[[-3/4]] kesrinin paydası 8 olunca hangisi olur?", ["[[-6/8]]", "[[-3/8]]", "[[-4/8]]"], 0, "4 · 2 = 8. Payı da 2 ile çarp.", "3 · 2 = 6: [[-6/8]]."),
                            "islem": "([[-6/8]]) + [[1/8]]"},
                           {"metin": "Payları topla: (−6) + (+1). Payda 8 kalır.",
                            "soru": G("Son konum kaçtır? Kesir olarak yaz.", "-5/8", "İşaretler farklı: 6 − 1. Büyük olan −6.", "(−6) + (+1) = −5: [[-5/8]].", kesir=True, denk=True, kabul=["5/-8"]),
                            "islem": "= [[-5/8]]"}],
                       "sonuc": "Harika! Denizaltı deniz seviyesinin [[5/8]] km altında. (s. 82)"},
             "soru": N("Bir kaplumbağa sayı doğrusunda 0'dan başlıyor. Önce [[3/4]] birim sağa, sonra [[5/4]] birim sola gidiyor. Kaplumbağanın yerine dokun.", -0.5, sk(-2, 1, 4),
                       "Sağa artı, sola eksi: [[3/4]] + ([[-5/4]]). Paydalar aynı.", "[[3/4]] + ([[-5/4]]) = [[-2/4]] = [[-1/2]].")}
        ],
        "biliyorMusun": [
            "Her yıl yaklaşık 8 milyon ton atık deniz ve okyanuslara karışıyor. Ülkemizde denizleri korumak için Sıfır Atık Mavi projesi başlatıldı. (s. 82)",
            "Denizaltı araştırma ekipleri farklı derinliklerdeki plastik yoğunluğunu ve canlıların davranışını kaydeder. Rota planlarken rasyonel sayılarla toplama ve çıkarma yaparlar. (s. 85)"],
        "akildaKalsin": [
            "Paydalar eşitse payları topla, payda aynı kalır.",
            "Paydalar farklıysa önce genişletip eşitle.",
            "Eksi işareti paya aittir; payları tam sayı kuralıyla topla.",
            "Çıkarmayı çevir, topla: çıkan sayının işaretini ters yap.",
            "Tam sayılı kesri önce bileşik kesre çevir.",
            "Sayı + tersi = 0; tersleri yan yana getirmek işlemi kolaylaştırır."],
        "merakKutusu": [
            {"soru": "Neden paydaları toplamıyoruz?", "cevap": "Payda dilimin büyüklüğünü söyler. [[1/4]] + [[2/4]] işleminde çeyrek dilimleri sayıyoruz: 1 çeyrek + 2 çeyrek = 3 çeyrek. Dilimin boyu değişmez, payda 4 kalır."},
            {"soru": "Ortak paydayı nasıl bulurum?", "cevap": "Büyük paydanın katlarını sırayla say (5, 10, 15, …) ve küçük paydanın da bölebildiği ilk sayıda dur. Paydaları birbiriyle çarpmak da her zaman işe yarar ama sayılar büyüyebilir."},
            {"soru": "Eksi işaretini paya mı, paydaya mı yazmalıyım?", "cevap": "İkisi de aynı sayıyı gösterir. Kitap, negatif rasyonel sayılarda eksinin paya dâhil olduğunu söyler; işlem yaparken eksiyi paya yazmak kolaylık sağlar. (s. 83)"},
            {"soru": "Tam sayılı kesirde iki yol aynı sonucu verir mi?", "cevap": "Evet. İster bileşik kesre çevir, ister tam kısımları ve kesir kısımları ayrı topla; sonuç aynıdır. (s. 84)"},
            {"soru": "Önce inip sonra çıkmak ile önce çıkıp sonra inmek aynı yere mi götürür?", "cevap": "Evet. Toplamada sayıların yeri değişse de sonuç değişmez; buna değişme özelliği denir. (s. 85–86)"}],
        "dusunVeYaz": [{"soru": "Ayşe [[1/2]] + [[1/3]] işleminde payları ve paydaları ayrı ayrı toplayıp [[2/5]] buldu. Hatası ne? Doğru sonucu bul.",
                        "ornekCevap": "Ayşe paydaları da toplamış ama paydalar toplanmaz. Önce paydaları 6'da eşitlerim: [[3/6]] + [[2/6]] = [[5/6]].",
                        "anahtarlar": ["payda", "eşitle", "topla", "6"]}],
        "sorular": [
            S("[[3/7]] + ([[-5/7]]) kaçtır?", ["[[8/7]]", "[[-2/7]]", "[[-2/14]]"], 1,
              "Paydalar aynı. Payları topla: (+3) + (−5). Payda 7 kalır.", "(+3) + (−5) = −2, payda 7: [[-2/7]]. Paydalar toplanmaz. (s. 84)"),
            G("([[-1/6]]) + ([[-1/3]]) kaçtır?", "-3/6", "3'ü 6 yap: [[-1/3]] = [[-2/6]]. Sonra payları topla.",
              "([[-1/6]]) + ([[-2/6]]) = [[-3/6]] = [[-1/2]]. (s. 83)", kesir=True, denk=True, kabul=["3/-6"]),
            N("([[-1/2]]) + ([[-3/4]]) işleminin sonucuna dokun.", -1.25, sk(-2, 0, 4),
              "[[-1/2]] = [[-2/4]]. Sonra payları topla: iki eksi.", "([[-2/4]]) + ([[-3/4]]) = [[-5/4]] = [[-1 1/4]]. (s. 83)"),
            S("([[-5/6]]) − ([[-1/6]]) kaçtır?", ["[[-6/6]]", "[[4/6]]", "[[-4/6]]"], 2,
              "Çıkarmayı çevir: ([[-5/6]]) + [[1/6]]. Farklı işaret.", "([[-5/6]]) + [[1/6]]: 5 − 1 = 4, büyük olan −5: [[-4/6]] = [[-2/3]]. (s. 84)"),
            G("[[9/2]] − [[10/2]] kaçtır?", "-1/2", "Çıkarmayı çevir: [[9/2]] + ([[-10/2]]). Paydalar aynı.",
              "(+9) + (−10) = −1, payda 2: [[-1/2]]. (s. 84)", kesir=True, denk=True, kabul=["1/-2"]),
            S("([[-2 1/5]]) + ([[1 3/5]]) kaçtır?", ["[[-3/5]]", "[[3/5]]", "[[-3 4/5]]"], 0,
              "Önce bileşik kesre çevir: [[-11/5]] ve [[8/5]].", "([[-11/5]]) + [[8/5]]: 11 − 8 = 3, büyük olan −11: [[-3/5]]. (s. 84)"),
            S("Hangisinde toplama işleminin ters eleman özelliği kullanılmıştır?", ["[[4/9]] + 0 = [[4/9]]", "([[-4/9]]) + [[4/9]] = 0", "[[1/9]] + [[4/9]] = [[4/9]] + [[1/9]]"], 1,
              "Ters eleman: toplamları 0 olan iki sayı.", "([[-4/9]]) + [[4/9]] = 0: ters eleman. 0 eklemek etkisiz eleman, yer değiştirmek değişme özelliğidir. (s. 86)"),
            N("Termometre [[1/2]] °C gösteriyor. Sıcaklık [[3/2]] °C düştü. Yeni sıcaklığa dokun.", -1, sk(-2, 2, 2),
              "Başlangıç [[1/2]]. Düşüş eksi: [[1/2]] + ([[-3/2]]). Paydalar aynı.", "(+1) + (−3) = −2: [[-2/2]] = −1 °C."),
            G("Bir dalgıç deniz seviyesinin [[5/2]] m altında. [[3/4]] m yukarı çıktı. Yeni konumunu kesir olarak yaz.", "-7/4",
              "Başlangıç [[-5/2]], yukarı artı: ([[-5/2]]) + [[3/4]]. Paydaları 4'te eşitle.",
              "([[-10/4]]) + [[3/4]]: 10 − 3 = 7, büyük olan −10: [[-7/4]] m. (Kitaptaki denizaltı bağlamı, s. 85)", kesir=True, denk=True, kabul=["7/-4"], birim="m"),
            S("Denizaltı önce [[7/3]] km aşağı inip sonra [[5/9]] km yukarı çıkıyor. Bir başkası önce [[5/9]] km çıkıp sonra [[7/3]] km iniyor. Hangisi doğrudur?",
              ["Birincisi daha derine iner", "İkincisi daha derine iner", "İkisi aynı yere varır"], 2,
              "Toplamada sayıların yeri değişirse sonuç değişir mi?", "([[-7/3]]) + [[5/9]] = [[5/9]] + ([[-7/3]]). Değişme özelliği: ikisi aynı yere varır. (s. 85)")]
    }


# ---------- u1k9 çizimleri ----------
def svg9_alan():
    g = ""
    for r in range(5):
        for c in range(3):
            dolu = c < 2 and r < 4
            yari = (c < 2) != (r < 4)
            g += f"<rect x='{24 + c * 24}' y='{10 + r * 14}' width='24' height='14' fill='{OB if dolu else ('#3a4570' if yari else '#2b355c')}' stroke='#f5f6fa' stroke-width='1.2'/>"
    g += txt(60, 104, "8 / 15", OB, 16)
    return bg(g)


def svg9_capraz():
    g = txt(34, 46, "5", "#f5f6fa", 22) + "<line x1='18' y1='54' x2='50' y2='54' stroke='#f5f6fa' stroke-width='2.6'/>" + txt(34, 78, "1", "#f5f6fa", 22)
    g += txt(60, 62, "·", "#f2c14e", 24)
    g += txt(74, 62, M, NB, 20) + txt(96, 46, "3", NB, 22) + "<line x1='82' y1='54' x2='110' y2='54' stroke='#6fb3ff' stroke-width='2.6'/>" + txt(96, 78, "25", NB, 22)
    g += "<path d='M40 34 L28 46 M108 66 L84 80' stroke='#f2c14e' stroke-width='2.5'/><path d='M42 42 L84 70' stroke='#f2c14e' stroke-width='2' stroke-dasharray='4 3'/>"
    g += txt(22, 24, "1", "#f2c14e", 13) + txt(108, 100, "5", "#f2c14e", 13)
    return bg(g)


def svg9_tamli():
    g = txt(20, 62, "2", "#f5f6fa", 24) + kesir_svg(40, 50, "1", "2", "#f5f6fa", 14)
    g += "<path d='M54 54 h14 M63 49 l6 5 -6 5' stroke='#f2c14e' stroke-width='3' fill='none' stroke-linecap='round' stroke-linejoin='round'/>"
    g += kesir_svg(92, 48, "5", "2", OB, 20) + txt(60, 106, "önce çevir", "#f2c14e", 12)
    return bg(g)


def svg9_harclik():
    g = ""
    for i in range(5):
        x = 18 + i * 21
        g += f"<circle cx='{x}' cy='40' r='9' fill='{'#f2c14e' if i == 0 else '#2b355c'}' stroke='#f2c14e' stroke-width='2'/>"
    g += "<path d='M8 56 q10 8 20 0' stroke='#f2c14e' stroke-width='2' fill='none'/>" + kesir_svg(18, 74, "1", "5", "#f2c14e", 12)
    g += txt(78, 92, "’i = ·", "#f5f6fa", 20)
    return bg(g)


def svg9_ozellik():
    return bg(txt(60, 46, "x · 1 = x", "#f5f6fa", 18) + txt(60, 82, "x · 0 = 0", "#f2c14e", 18)
              + "<path d='M22 98 h76' stroke='#5a6280' stroke-width='3' stroke-linecap='round'/>")


# =================================================================
def u1k9():
    sk = lambda mn, mx, b, **ek: dict({"min": mn, "max": mx, "bolme": b}, **ek)
    return {
        "id": "u1k9", "unite": "1. Tema: Sayılar ve Nicelikler", "baslik": "Rasyonel Sayılarla Çarpma", "sayfalar": "s. 88–95",
        "giris": "Kesirleri çarpmayı ve eksi sayılarla çarpmayı biliyorsun. Bu konuda ikisini birleştiriyoruz. Çarpmanın güzel yanı: paydaları eşitlemek yok! Köstebek, bayram harçlığı ve halı bize yardım edecek.",
        "hazirlik": {
            "baslik": "Hazır mısın?",
            "giris": "Bu konu kesirlerde çarpma, tam sayılarda çarpmanın işareti, tam sayılı kesirler ve sadeleştirme üzerine kuruluyor. Önce bunları hatırlıyor musun bakalım. Not yok.",
            "maddeler": [
                {"ad": "Kesirlerde çarpma", "sinif": "Önceki yıllar", "svg": svg9_alan(),
                 "anlatim": "Kesirleri çarparken payı payla, paydayı paydayla çarparız: [[2/3]] · [[4/5]] = [[8/15]].",
                 "akilda": "Pay paya, payda paydaya",
                 "ornek": {"problem": "[[1/2]] · [[3/4]] kaçtır?", "adimlar": [
                     {"metin": "Payları çarp: 1 · 3.", "islem": "Pay: 3"},
                     {"metin": "Paydaları çarp: 2 · 4.", "islem": "[[1/2]] · [[3/4]] = [[3/8]]"}]},
                 "sorular": [
                     G("[[2/5]] · [[1/3]] kaçtır?", "2/15", "Payları çarp: 2 · 1. Paydaları çarp: 5 · 3.", "2 · 1 = 2, 5 · 3 = 15: [[2/15]].", kesir=True),
                     G("[[3/4]] · [[1/2]] kaçtır?", "3/8", "Payları çarp: 3 · 1. Paydaları çarp: 4 · 2.", "3 · 1 = 3, 4 · 2 = 8: [[3/8]].", kesir=True)]},
                {"ad": "Çarpmada işaret", "sinif": "7. konu", "svg": svg6_isaret("ayni"),
                 "anlatim": "Aynı işaretli iki sayının çarpımı artı, farklı işaretli iki sayının çarpımı eksidir.",
                 "akilda": "Aynı artı, farklı eksi",
                 "ornek": {"problem": "(−4) · 3 kaçtır?", "adimlar": [
                     {"metin": "Önce işaretsiz çarp: 4 · 3.", "islem": "4 · 3 = 12"},
                     {"metin": "İşaretler farklı → eksi.", "islem": "(−4) · 3 = −12"}]},
                 "sorular": [
                     G("(−6) · (−5) kaçtır?", "30", "Önce 6 · 5. İşaretler aynı mı?", "6 · 5 = 30. İki eksi: aynı işaret → +30."),
                     S("(+7) · (−3) kaçtır?", ["+21", "−21", "−10"], 1, "Önce 7 · 3. İşaretler farklı.", "7 · 3 = 21. Farklı işaret → −21.")]},
                {"ad": "Tam sayılı kesir → bileşik kesir", "sinif": "2. konu", "svg": svg_h_tamli(),
                 "anlatim": "Tam kısmı payda ile çarp, payı ekle; payda aynı kalır: [[2 3/4]] = [[11/4]]. Eksi sayının tamamına aittir: [[-1 1/2]] = [[-3/2]].",
                 "akilda": "Tam · payda + pay",
                 "ornek": {"problem": "[[1 2/5]] sayısını bileşik kesre çevirelim.", "adimlar": [
                     {"metin": "Tam kısmı payda ile çarp, payı ekle: 1 · 5 + 2.", "islem": "1 · 5 + 2 = 7"},
                     {"metin": "Payda 5 kalır.", "islem": "[[1 2/5]] = [[7/5]]"}]},
                 "sorular": [
                     G("[[2 1/3]] sayısını bileşik kesir olarak yaz.", "7/3", "2 · 3 + 1 = ? Payda 3 kalır.", "2 · 3 + 1 = 7: [[7/3]].", kesir=True),
                     G("[[-1 3/4]] sayısını bileşik kesir olarak yaz.", "-7/4", "Eksiyi kenara koy: 1 · 4 + 3 = ? Sonra eksiyi geri ekle.", "1 · 4 + 3 = 7: [[-7/4]].", kesir=True, kabul=["7/-4"])]},
                {"ad": "Sadeleştirme", "sinif": "Önceki yıllar", "svg": svg_h_denk(),
                 "anlatim": "Pay ve paydayı aynı sayıya bölersek kesir sadeleşir; değer değişmez: [[6/8]] = [[3/4]].",
                 "akilda": "Pay da payda da aynı sayıya",
                 "ornek": {"problem": "[[10/15]] kesrini sadeleştirelim.", "adimlar": [
                     {"metin": "10 ve 15'i birlikte bölen sayı: 5.", "islem": "10 ÷ 5 = 2, 15 ÷ 5 = 3"},
                     {"metin": "Yeni kesri yaz.", "islem": "[[10/15]] = [[2/3]]"}]},
                 "sorular": [
                     G("[[12/18]] kesrinin en sade hâlini yaz.", "2/3", "12 ve 18'i birlikte bölen en büyük sayı 6.", "12 ÷ 6 = 2, 18 ÷ 6 = 3: [[2/3]].", kesir=True),
                     S("[[9/12]] en sade hâliyle hangisidir?", ["[[3/4]]", "[[3/6]]", "[[9/4]]"], 0, "9 ve 12'yi 3 böler.", "9 ÷ 3 = 3, 12 ÷ 3 = 4: [[3/4]].")]}
            ]},
        "kavramlar": [
            {"ad": "Pay Paya, Payda Paydaya", "renk": "#1f9e8f", "svg": svg9_alan(),
             "aciklama": "Rasyonel sayıları çarparken payları çarpıp paya, paydaları çarpıp paydaya yaz. Paydaları eşitlemeye gerek yok!",
             "ek": "Kitaptaki örnek: [[4/7]] · [[2/3]] = [[8/21]]. Toplamadan farklı olarak paydalar eşit olmak zorunda değil. (s. 90)",
             "akilda": "Pay paya, payda paydaya",
             "cozum": {"baslik": "İlk çarpım",
                       "problem": "[[2/3]] · [[4/5]] işlemini yapalım.",
                       "adimlar": [
                           {"metin": "Payları çarp: 2 · 4.", "islem": "Pay: 8"},
                           {"metin": "Paydaları çarp: 3 · 5.", "islem": "Payda: 15"},
                           {"metin": "Yeni kesri yaz.", "islem": "[[2/3]] · [[4/5]] = [[8/15]]"},
                           {"metin": "Sadeleşir mi? 8 ile 15'i birlikte bölen sayı yok.", "islem": "[[8/15]] en sade"}],
                       "sonuc": "[[2/3]] · [[4/5]] = [[8/15]]. (s. 90)"},
             "soru": G("[[3/4]] · [[5/7]] kaçtır?", "15/28", "Payları çarp: 3 · 5. Paydaları çarp: 4 · 7.",
                       "3 · 5 = 15, 4 · 7 = 28: [[15/28]]. (s. 90)", kesir=True)},
            {"ad": "İşaret Tam Sayılardaki Gibi", "renk": "#7b4fc9", "svg": svg6_isaret("farkli"),
             "aciklama": "Önce işareti belirle: aynı işaret artı, farklı işaret eksi. Sonra işaretsiz kesirleri çarp.",
             "ek": "Kitaptaki örnekler: ([[-6/11]]) · [[3/7]] = [[-18/77]] ve ([[-8/13]]) · ([[-1/3]]) = [[8/39]]. (s. 90)",
             "akilda": "Önce işaret, sonra kesir",
             "cozum": {"baslik": "Köstebek kazıyor",
                       "problem": "Bir köstebek dakikada [[3/25]] m derine iniyor. 4 dakika sonra yer seviyesine göre nerede?",
                       "adimlar": [
                           {"metin": "Başlangıç (0): yer seviyesi. Aşağı eksidir.", "islem": "Her dakika: [[-3/25]]"},
                           {"metin": "4 dakika boyunca: 4 kere. Bu bir çarpma.", "islem": "4 · ([[-3/25]])"},
                           {"metin": "İşaret: artı · eksi → eksi.", "islem": "Sonuç eksi"},
                           {"metin": "4'ü [[4/1]] gibi düşün. Payları çarp: 4 · 3 = 12; payda 25.", "islem": "4 · ([[-3/25]]) = [[-12/25]]"}],
                       "sonuc": "Köstebek yer seviyesinin [[12/25]] m altında: [[-12/25]] m. (s. 88)"},
             "sende": {"baslik": "İki eksi",
                       "problem": "([[-2/3]]) · ([[-5/7]]) işlemini yap.",
                       "adimlar": [
                           {"metin": "Önce işaret: eksi · eksi.",
                            "soru": S("Sonucun işareti ne olur?", ["Artı", "Eksi", "Sıfır"], 0, "İşaretler aynı mı, farklı mı?", "İki eksi: aynı işaret → artı."),
                            "islem": "Aynı işaret → artı"},
                           {"metin": "Şimdi işaretsiz çarp: payları 2 · 5, paydaları 3 · 7.",
                            "soru": G("[[2/3]] · [[5/7]] kaçtır?", "10/21", "2 · 5 = ? 3 · 7 = ?", "2 · 5 = 10, 3 · 7 = 21: [[10/21]].", kesir=True),
                            "islem": "([[-2/3]]) · ([[-5/7]]) = [[10/21]]"}],
                       "sonuc": "Harika! İki eksinin çarpımı artı: [[10/21]]."},
             "soru": S("([[-1/6]]) · [[1/3]] kaçtır?", ["[[1/18]]", "[[-1/18]]", "[[-2/9]]"], 1,
                       "Önce işaret: eksi · artı. Sonra 1 · 1 ve 6 · 3.", "Farklı işaret → eksi. 1 · 1 = 1, 6 · 3 = 18: [[-1/18]]. (s. 90)")},
            {"ad": "Önce Çapraz Sadeleştir", "renk": "#e8590c", "svg": svg9_capraz(),
             "aciklama": "Çarpmadan önce bir paydaki sayı ile bir paydadaki sayıyı aynı sayıya böl. Sayılar küçülür, işlem kolaylaşır; sonuç en sade çıkar.",
             "ek": "Kitapta köstebeğin 5 dakikadaki konumu iki yolla bulunuyor: önce çarpıp sonra sadeleştirmek ya da çarparken 5 ile 25'i 5'e bölmek. İkisi de [[-3/5]] verir; ikinci yol daha kısa. Biz hep ikinci yolu kullanacağız. (s. 89)",
             "akilda": "Önce sadeleştir, sonra çarp",
             "cozum": {"baslik": "Köstebek 5 dakika kazıyor",
                       "problem": "5 · ([[-3/25]]) işlemini yapalım.",
                       "adimlar": [
                           {"metin": "Önce işaret: artı · eksi → eksi.", "islem": "Sonuç eksi"},
                           {"metin": "5'i [[5/1]] yaz. Üstte 5, altta 25 var. İkisini de 5 böler.", "islem": "5 ÷ 5 = 1, 25 ÷ 5 = 5"},
                           {"metin": "Küçülmüş sayılarla çarp: pay 1 · 3, payda 1 · 5.", "islem": "[[1/1]] · [[3/5]] = [[3/5]]"},
                           {"metin": "İşareti koy.", "islem": "5 · ([[-3/25]]) = [[-3/5]]"}],
                       "sonuc": "Köstebek 5 dakikada yer seviyesinin [[3/5]] m altına iner. (s. 89)"},
             "sende": {"baslik": "Sıra sende",
                       "problem": "[[4/9]] · ([[-3/8]]) işlemini yap.",
                       "adimlar": [
                           {"metin": "Önce işaret: artı · eksi → eksi.", "islem": "Sonuç eksi"},
                           {"metin": "Üstteki 4 ile alttaki 8'i sadeleştir.",
                            "soru": S("4 ile 8'i hangi sayıya bölelim?", ["3", "4", "9"], 1, "Hem 4'ü hem 8'i bölen en büyük sayı hangisi?", "4 ÷ 4 = 1, 8 ÷ 4 = 2."),
                            "islem": "4 → 1, 8 → 2"},
                           {"metin": "Üstteki 3 ile alttaki 9'u 3 böler.",
                            "soru": S("3 ve 9, 3'e bölününce ne olur?", ["1 ve 3", "3 ve 9", "1 ve 9"], 0, "3 ÷ 3 = ? 9 ÷ 3 = ?", "3 ÷ 3 = 1, 9 ÷ 3 = 3."),
                            "islem": "3 → 1, 9 → 3"},
                           {"metin": "Şimdi çarp: pay 1 · 1, payda 3 · 2.",
                            "soru": G("Sonuç kaçtır? İşareti unutma.", "-1/6", "Pay 1 · 1, payda 3 · 2. Önce − tuşu.", "1 · 1 = 1, 3 · 2 = 6: [[-1/6]].", kesir=True, kabul=["1/-6"]),
                            "islem": "= [[-1/6]]"}],
                       "sonuc": "Harika! Sayılar küçüldü, sonuç zaten en sade: [[-1/6]]."},
             "soru": G("[[5/12]] · [[6/25]] kaçtır? En sade hâliyle yaz.", "1/10", "Çapraz bak: 5 ile 25'i 5 böler, 6 ile 12'yi 6 böler.",
                       "5 → 1, 25 → 5; 6 → 1, 12 → 2. [[1/2]] · [[1/5]] = [[1/10]]. (s. 90)", kesir=True)},
            {"ad": "Tam Sayılı Kesri Önce Çevir", "renk": "#c92a2a", "svg": svg9_tamli(),
             "aciklama": "Tam sayılı kesirle çarpmadan önce onu bileşik kesre çevir. Tam kısımları ve kesirleri ayrı çarpmak yanlış sonuç verir.",
             "ek": "Kitaptaki örnek: ([[-1 1/5]]) · [[2 3/6]] = ([[-6/5]]) · [[15/6]] = −3. (s. 90)",
             "akilda": "Önce bileşik kesir",
             "cozum": {"baslik": "Tam sayılı kesirle çarpma",
                       "problem": "([[-1 1/2]]) · [[4/9]] işlemini yapalım.",
                       "adimlar": [
                           {"metin": "Çevir: 1 · 2 + 1 = 3. Eksi tamamına ait.", "islem": "[[-1 1/2]] = [[-3/2]]"},
                           {"metin": "İşaret: eksi · artı → eksi.", "islem": "Sonuç eksi"},
                           {"metin": "Çapraz sadeleştir: 3 ile 9'u 3'e, 4 ile 2'yi 2'ye böl.", "islem": "[[1/1]] · [[2/3]]"},
                           {"metin": "Çarp ve işareti koy.", "islem": "([[-1 1/2]]) · [[4/9]] = [[-2/3]]"}],
                       "sonuc": "Sonuç [[-2/3]]. (s. 90)"},
             "soru": S("[[2 1/2]] · [[2/5]] kaçtır?", ["1", "[[4 2/10]]", "[[4/5]]"], 0,
                       "Önce [[2 1/2]] = [[5/2]]. Sonra çapraz sadeleştir.", "[[5/2]] · [[2/5]]: 5 ile 5, 2 ile 2 sadeleşir: 1. (s. 90)")},
            {"ad": "Bir Sayının Kesrini Bulma", "renk": "#1d6fa3", "svg": svg9_harclik(),
             "aciklama": "Bir çokluğun [[1/5]]'ini bulmak, o çokluğu [[1/5]] ile çarpmaktır. Harcama, azalma gibi kelimeler varsa değişim eksi olur.",
             "ek": "Kitaptaki örnek: Yiğit 1800 TL harçlığının [[1/5]]'ini kitaba harcadı: 1800 · ([[-1/5]]) = −360. Parası 360 TL azaldı. (s. 91)",
             "akilda": "Sayının kesri: çarp",
             "cozum": {"baslik": "Bayram harçlığı",
                       "problem": "Yiğit'in 1800 TL harçlığı var. [[1/5]]'ini kitaba, [[2/9]]'unu sinemaya harcadı. Kalanı kumbarasına attı. Kumbarasına kaç TL attı?",
                       "adimlar": [
                           {"metin": "Ne veriliyor? 1800 TL, [[1/5]]'i kitap, [[2/9]]'u sinema. Ne isteniyor? Kalan para.", "islem": "Başlangıç: 1800 TL"},
                           {"metin": "Kitap: harcama eksidir. 1800 ile 5'i sadeleştir: 1800 ÷ 5 = 360.", "islem": "1800 · ([[-1/5]]) = −360"},
                           {"metin": "Sinema: 1800 ÷ 9 = 200, sonra 200 · 2.", "islem": "1800 · ([[-2/9]]) = −400"},
                           {"metin": "Değişimleri başlangıca ekle.", "islem": "1800 + (−360) + (−400) = 1040"}],
                       "sonuc": "Yiğit kumbarasına 1040 TL attı. (s. 91)"},
             "sende": {"baslik": "Desenli halı",
                       "problem": "Alanı 16 m² olan bir halının [[3/8]]'ine yeni desen işlendi. Desenli alan kaç m²?",
                       "adimlar": [
                           {"metin": "\"[[3/8]]'ine\" ne demek?",
                            "soru": S("Hangi işlem yapılır?", ["16 + [[3/8]]", "16 · [[3/8]]", "16 − [[3/8]]"], 1, "'i, 'ine eki görünce hangi işlemi düşünüyoruz?", "'ine demek çarpmak: 16 · [[3/8]]."),
                            "islem": "16 · [[3/8]]"},
                           {"metin": "Çapraz sadeleştir: 16 ile 8'i 8 böler: 16 → 2, 8 → 1.",
                            "soru": G("16 · [[3/8]] kaçtır?", "6", "16 → 2, 8 → 1. Şimdi 2 · 3.", "2 · 3 = 6.", birim="m²"),
                            "islem": "2 · 3 = 6"}],
                       "sonuc": "Harika! Desenli alan 6 m². (s. 89)"},
             "soru": G("Bir sınıfta 30 öğrenci var. Öğrencilerin [[2/5]]'i gözlüklü. Kaç öğrenci gözlüklü?", "12",
                       "'i demek çarp: 30 · [[2/5]]. 30 ile 5'i sadeleştir.", "30 ÷ 5 = 6, 6 · 2 = 12 öğrenci.")},
            {"ad": "Çarpmanın Özellikleri", "renk": "#b7791f", "svg": svg9_ozellik(),
             "aciklama": "Çarparken sayıların yerini değiştirebilir, istediğin ikisini önce çarpabilirsin. 1 ile çarpmak sayıyı değiştirmez, 0 ile çarpmak sonucu 0 yapar.",
             "ek": "Çarpımları 1 olan iki sayı birbirinin tersidir: [[2/7]] · [[7/2]] = 1. Dağılma: 24 · ([[3/8]] + [[1/3]]) = 24 · [[3/8]] + 24 · [[1/3]] = 9 + 8 = 17. (s. 93–94)",
             "akilda": "1 korur, 0 yutar",
             "soru": S("[[-5/3]] sayısının çarpma işlemine göre tersi hangisidir?", ["[[5/3]]", "[[-3/5]]", "0"], 1,
                       "Hangisiyle çarpınca sonuç 1 olur? İşaret de aynı kalmalı.", "([[-5/3]]) · ([[-3/5]]) = [[15/15]] = 1. (s. 94)")}
        ],
        "biliyorMusun": [
            "Köstebekler yaşamlarının çoğunu yer altında geçirir; güçlü ön ayaklarıyla toprağı hızla kazıp tüneller açarlar. (s. 88)",
            "Bulut bilişimde dosyalar genel ağda saklanır. Bilgisayar bozulsa bile veriler zarar görmez. (s. 92)"],
        "akildaKalsin": [
            "Pay paya, payda paydaya: paydaları eşitlemeye gerek yok.",
            "İşaret tam sayılardaki gibi: aynı artı, farklı eksi.",
            "Önce çapraz sadeleştir, sonra çarp.",
            "Tam sayılı kesri önce bileşik kesre çevir.",
            "Bir sayının [[2/5]]'i = o sayı · [[2/5]].",
            "1 ile çarpmak sayıyı korur, 0 ile çarpmak 0 yapar."],
        "merakKutusu": [
            {"soru": "Çarpınca sayı hep büyür mü?", "cevap": "Hayır. 1'den küçük bir kesirle çarparsan sonuç küçülür: 16 · [[3/8]] = 6. 16'nın bir parçasını almış olursun. (s. 89)"},
            {"soru": "Çarpmada neden paydaları eşitlemiyoruz?", "cevap": "Çünkü çarpmada parçaları yan yana koymuyoruz, bir parçanın parçasını alıyoruz. Paylar ve paydalar kendi aralarında çarpılır. (s. 90)"},
            {"soru": "Çapraz sadeleştirmede hangi sayılar sadeleşir?", "cevap": "Bir paydaki sayı ile bir paydadaki sayı; aynı kesirde de olabilir, çaprazda da. İki payı ya da iki paydayı birbiriyle sadeleştiremezsin."},
            {"soru": "Bir sayı ile tersinin çarpımı neden 1?", "cevap": "[[2/7]] · [[7/2]] = [[14/14]] = 1. Pay ile payda yer değiştirince hepsi sadeleşir. (s. 94)"},
            {"soru": "0 ile çarpınca neden 0 çıkıyor?", "cevap": "Kitaptaki yükleme aracı dakikada [[5/2]] GB aktarıyor; hiç çalıştırılmazsa hiç veri aktarılmaz: [[5/2]] · 0 = 0. (s. 92)"}],
        "dusunVeYaz": [{"soru": "Ali [[2 1/2]] · [[2 1/3]] işleminde tamları ve kesirleri ayrı çarpıp [[4 1/6]] buldu. Doğru mu? Doğru sonucu bul.",
                        "ornekCevap": "Yanlış. Tam sayılı kesirler önce bileşik kesre çevrilir: [[5/2]] · [[7/3]] = [[35/6]] = [[5 5/6]].",
                        "anahtarlar": ["bileşik", "çevir", "35", "yanlış"]}],
        "sorular": [
            S("([[-4/5]]) · [[3/7]] kaçtır?", ["[[-12/35]]", "[[12/35]]", "[[-7/12]]"], 0,
              "Önce işaret: eksi · artı. Sonra 4 · 3 ve 5 · 7.", "Farklı işaret → eksi. 4 · 3 = 12, 5 · 7 = 35: [[-12/35]]. (s. 90)"),
            G("([[-2/3]]) · ([[-3/4]]) kaçtır? En sade hâliyle yaz.", "1/2", "İki eksi → artı. Çapraz sadeleştir: 3 ile 3, 2 ile 4.",
              "3 → 1, 3 → 1; 2 → 1, 4 → 2. [[1/1]] · [[1/2]] = [[1/2]]. (s. 90)", kesir=True),
            N("[[1/2]] · ([[-3/2]]) işleminin sonucuna dokun.", -0.75, sk(-2, 1, 4),
              "Farklı işaret → eksi. 1 · 3 = 3, 2 · 2 = 4.", "[[1/2]] · ([[-3/2]]) = [[-3/4]]. (s. 90)"),
            S("[[3/5]] · [[2/7]] kaçtır?", ["[[6/35]]", "[[5/12]]", "[[6/12]]"], 0,
              "Payları çarp, paydaları çarp. Toplamıyoruz!", "3 · 2 = 6, 5 · 7 = 35: [[6/35]]. (s. 90)"),
            S("([[-1 1/3]]) · [[3/8]] kaçtır?", ["[[-3/8]]", "[[-1 1/8]]", "[[-1/2]]"], 2,
              "Önce [[-1 1/3]] = [[-4/3]]. Sonra çapraz sadeleştir.", "([[-4/3]]) · [[3/8]]: 3 ile 3, 4 ile 8 sadeleşir: [[-1/2]]. (s. 90)"),
            G("Yiğit 600 TL harçlığının [[1/4]]'ünü harcadı. Parasındaki değişimi tam sayıyla yaz.", "-150",
              "Harcamak eksidir: 600 · ([[-1/4]]).", "600 ÷ 4 = 150. Harcama eksi: −150 TL. (s. 91)", birim="TL"),
            S("Hangisinde çarpma işleminin yutan eleman özelliği vardır?", ["[[3/4]] · 1 = [[3/4]]", "[[3/4]] · [[4/3]] = 1", "[[3/4]] · 0 = 0"], 2,
              "Yutan eleman her şeyi kendine çevirir. Hangi sayı?", "0 ile çarpım 0'dır: yutan eleman. 1 etkisiz eleman, [[4/3]] tersidir. (s. 94)"),
            N("Bir köstebek dakikada [[1/4]] m derine iniyor. 6 dakika sonraki konumuna sayı doğrusunda dokun.", -1.5, sk(-2, 0, 4),
              "Aşağı eksi: 6 · ([[-1/4]]). 6 tane çeyrek sola say.", "6 · ([[-1/4]]) = [[-6/4]] = [[-1 2/4]], yani −1,5 m. (s. 88)"),
            G("Bir halının alanı 12 m². Robot süpürge halının [[3/4]]'ünü süpürdü. Süpürülmeyen kısım kaç m²?", "3",
              "Önce süpürülen kısmı bul: 12 · [[3/4]]. Sonra 12'den çıkar.", "12 · [[3/4]] = 9 m² süpürüldü. 12 − 9 = 3 m² kaldı. (Kitaptaki robot süpürge problemine benzer, s. 95)", birim="m²"),
            G("24 · ([[3/8]] + [[1/3]]) kaçtır?", "17",
              "Dağılma özelliği: 24 · [[3/8]] + 24 · [[1/3]].", "24 · [[3/8]] = 9, 24 · [[1/3]] = 8. 9 + 8 = 17. (s. 93)")]
    }


# ---------- u1k10 Üslü İfadeler ----------
# Üs yazımı: metinde 5[[u:4]], ([[2/3]])[[u:5]] → ekranda üst simge, sesli okumada "5 üssü 4". SVG içinde Unicode üst simge.
def svg10_bakteri():
    g = "<circle cx='20' cy='48' r='9' fill='#5fd08f'/>"
    g += "<circle cx='54' cy='38' r='8' fill='#5fd08f'/><circle cx='54' cy='58' r='8' fill='#5fd08f'/>"
    for x, y in [(86, 36), (104, 36), (86, 58), (104, 58)]:
        g += f"<circle cx='{x}' cy='{y}' r='7' fill='#5fd08f'/>"
    g += "<path d='M32 48 h10 M38 44 l4 4 -4 4 M66 48 h8 M70 44 l4 4 -4 4' stroke='#f5f6fa' stroke-width='2.5' fill='none' stroke-linecap='round' stroke-linejoin='round'/>"
    g += txt(20, 82, "1", "#f5f6fa", 13) + txt(54, 82, "2", "#f5f6fa", 13) + txt(95, 82, "4", "#f5f6fa", 13)
    g += txt(60, 106, "2 · 2 = 2²", "#f2c14e", 15)
    return bg(g)


def svg10_taban():
    return bg(txt(48, 84, "5", "#f5f6fa", 60) + txt(80, 50, "4", OB, 28)
              + txt(48, 106, "taban", NB, 12) + txt(94, 24, "üs", OB, 13) + txt(98, 84, "= 625", "#f2c14e", 13))


def svg10_top():
    g = "<line x1='8' y1='100' x2='112' y2='100' stroke='#f5f6fa' stroke-width='3' stroke-linecap='round'/>"
    g += f"<circle cx='16' cy='20' r='7' fill='{OB}'/>"
    g += "<path d='M16 28 L24 98 Q42 30 60 98 Q72 60 84 98 Q92 78 100 98' stroke='#f2c14e' stroke-width='2.5' fill='none' stroke-linejoin='round'/>"
    g += txt(42, 32, "1/2", "#f5f6fa", 11) + txt(72, 58, "1/4", "#f5f6fa", 11) + txt(94, 74, "1/8", "#f5f6fa", 10)
    return bg(g)


def svg10_isaret():
    return bg(txt(60, 38, f"({M}2)² = +4", OB, 15) + txt(60, 66, f"({M}2)³ = {M}8", NB, 15)
              + "<path d='M22 80 h76' stroke='#5a6280' stroke-width='2' stroke-linecap='round'/>"
              + txt(36, 102, "çift +", OB, 13) + txt(86, 102, f"tek {M}", NB, 13))


def svg10_ozel():
    return bg(txt(60, 36, "1⁹ = 1", "#f5f6fa", 17) + txt(60, 66, "0⁷ = 0", "#f2c14e", 17) + txt(60, 96, "8¹ = 8", OB, 17))


def svg10_parantez():
    return bg(txt(60, 42, f"({M}3)² = 9", OB, 17) + txt(60, 68, "≠", "#f2c14e", 20) + txt(60, 96, f"{M}3² = {M}9", NB, 17))


def u1k10():
    sd = lambda mn, mx, **ek: dict({"min": mn, "max": mx}, **ek)
    return {
        "id": "u1k10", "unite": "1. Tema: Sayılar ve Nicelikler", "baslik": "Üslü İfadeler", "sayfalar": "s. 96–101",
        "giris": "Aynı sayıyı tekrar tekrar çarpmanın kısa bir yazılışı var: üslü ifade. Çoğalan bakteriler, zıplayan bir top ve harita uygulaması bize yardım edecek. Bu konuda sadece çarpma var!",
        "hazirlik": {
            "baslik": "Hazır mısın?",
            "giris": "Üslü ifadeler art arda çarpmaya, çarpmada işarete ve kesirlerde çarpmaya dayanıyor. Önce bunları hatırlıyor musun bakalım. Not yok.",
            "maddeler": [
                {"ad": "Art arda çarpma", "sinif": "Önceki yıllar", "svg": svg6_tekrar(),
                 "anlatim": "Çok sayıyı çarparken soldan başla, ikişer ikişer çarp: 2 · 3 · 4 = 6 · 4 = 24.",
                 "akilda": "İkişer ikişer çarp",
                 "ornek": {"problem": "5 · 5 · 5 kaçtır?", "adimlar": [
                     {"metin": "İlk ikisini çarp: 5 · 5.", "islem": "5 · 5 = 25"},
                     {"metin": "Sonucu kalan 5 ile çarp.", "islem": "25 · 5 = 125"}]},
                 "sorular": [
                     G("3 · 3 · 3 kaçtır?", "27", "Önce 3 · 3. Sonra çıkan sayıyı 3 ile çarp.", "3 · 3 = 9, 9 · 3 = 27."),
                     G("2 · 2 · 2 · 2 kaçtır?", "16", "İkişer ikişer: 2 · 2 = 4, sonra 4 · 2, sonra bir daha · 2.", "2 · 2 = 4, 4 · 2 = 8, 8 · 2 = 16.")]},
                {"ad": "Çok çarpanda eksileri say", "sinif": "7. konu", "svg": svg6_eksileri(),
                 "anlatim": "Çarpımda eksi işaretlerini say. Eksi sayısı çiftse sonuç artı, tekse sonuç eksi olur.",
                 "akilda": "Çift eksi artı, tek eksi eksi",
                 "ornek": {"problem": f"({M}2) · ({M}3) · ({M}1) kaçtır?", "adimlar": [
                     {"metin": "Eksileri say: 3 tane. 3 tek sayı.", "islem": "Sonuç eksi"},
                     {"metin": "İşaretsiz çarp: 2 · 3 · 1.", "islem": f"({M}2) · ({M}3) · ({M}1) = {M}6"}]},
                 "sorular": [
                     S(f"({M}1) · ({M}1) · ({M}1) çarpımının işareti nedir?", ["Artı", "Eksi", "Sıfır"], 1, "Kaç tane eksi var? Çift mi, tek mi?", "3 eksi var, 3 tek: sonuç eksi, −1."),
                     G(f"({M}2) · ({M}2) kaçtır?", "4", "İşaretsiz çarp: 2 · 2. İki eksi: çift.", "2 · 2 = 4. İki eksi → artı: +4.")]},
                {"ad": "Kesirlerde çarpma", "sinif": "9. konu", "svg": svg9_alan(),
                 "anlatim": "Kesirleri çarparken payı payla, paydayı paydayla çarparız: [[2/3]] · [[2/3]] = [[4/9]].",
                 "akilda": "Pay paya, payda paydaya",
                 "ornek": {"problem": "[[1/2]] · [[1/2]] kaçtır?", "adimlar": [
                     {"metin": "Payları çarp: 1 · 1.", "islem": "Pay: 1"},
                     {"metin": "Paydaları çarp: 2 · 2.", "islem": "[[1/2]] · [[1/2]] = [[1/4]]"}]},
                 "sorular": [
                     G("[[1/3]] · [[1/3]] kaçtır?", "1/9", "Payları çarp: 1 · 1. Paydaları çarp: 3 · 3.", "1 · 1 = 1, 3 · 3 = 9: [[1/9]].", kesir=True),
                     G("[[2/5]] · [[2/5]] kaçtır?", "4/25", "Payları çarp: 2 · 2. Paydaları çarp: 5 · 5.", "2 · 2 = 4, 5 · 5 = 25: [[4/25]].", kesir=True)]}
            ]},
        "kavramlar": [
            {"ad": "Tekrarlı Çarpımı Kısalt", "renk": "#1f9e8f", "svg": svg10_bakteri(),
             "aciklama": "Bir sayı kendisiyle tekrar tekrar çarpılıyorsa kısaca üslü ifade olarak yazarız: 5 · 5 · 5 · 5 = 5[[u:4]]. Sayıyı bir kez yaz, kaç kere çarpıldığını sağ üst köşeye küçük yaz.",
             "ek": "Dikkat: 5[[u:4]], 5 · 4 değildir! 5[[u:4]] = 5 · 5 · 5 · 5 = 625, ama 5 · 4 = 20. (s. 98)",
             "akilda": "Kaç kere çarpıldı? Üste yaz",
             "cozum": {"baslik": "Bakteriler çoğalıyor",
                       "problem": "Bir bakteri her 30 dakikada ikiye bölünüyor. Başta 1 bakteri var. 2 saat sonra kaç bakteri olur?",
                       "adimlar": [
                           {"metin": "2 saat = 120 dakika. 30 dakikalık kaç parça var?", "islem": "120 ÷ 30 = 4 bölünme"},
                           {"metin": "Her bölünmede sayı 2 katına çıkıyor: 4 kere · 2.", "islem": "1 · 2 · 2 · 2 · 2"},
                           {"metin": "2 sayısı 4 kere çarpılıyor. Kısa yazalım.", "islem": "2 · 2 · 2 · 2 = 2[[u:4]]"},
                           {"metin": "Değerini bul: ikişer ikişer çarp.", "islem": "2 · 2 = 4, 4 · 2 = 8, 8 · 2 = 16"}],
                       "sonuc": "2 saat sonra 16 bakteri olur: 2[[u:4]] = 16. (Kitaptaki bakteri etkinliğine benzer, s. 96)"},
             "sende": {"baslik": "Sıra sende",
                       "problem": "5 · 5 · 5 çarpımını üslü ifade olarak yaz ve değerini bul.",
                       "adimlar": [
                           {"metin": "Tekrar tekrar çarpılan sayı hangisi?",
                            "soru": S("Tekrar eden sayı hangisi?", ["3", "5", "15"], 1, "Çarpımda hangi sayıyı tekrar tekrar görüyorsun?", "Tekrar eden sayı 5."),
                            "islem": "Sayı: 5"},
                           {"metin": "5 kaç kere çarpılıyor? Say.",
                            "soru": G("5 kaç kere çarpılıyor?", "3", "5'leri tek tek say.", "Üç tane 5 var."),
                            "islem": "5 · 5 · 5 = 5[[u:3]]"},
                           {"metin": "Değerini bul: önce 5 · 5, sonra · 5.",
                            "soru": G("5[[u:3]] kaçtır?", "125", "5 · 5 = 25. Şimdi 25 · 5.", "25 · 5 = 125."),
                            "islem": "5[[u:3]] = 125"}],
                       "sonuc": "Harika! 5 · 5 · 5 = 5[[u:3]] = 125."},
             "soru": S("3 · 3 · 3 · 3 çarpımının üslü gösterimi hangisidir?", ["3[[u:4]]", "4[[u:3]]", "3 · 4"], 0,
                       "Hangi sayı tekrar ediyor? Kaç kere?", "3 sayısı 4 kere çarpılıyor: 3[[u:4]]. (s. 99)")},
            {"ad": "Taban, Üs ve Değer", "renk": "#7b4fc9", "svg": svg10_taban(),
             "aciklama": "5[[u:4]] = 625 ifadesinde tekrar tekrar çarpılan 5'e taban, kaç kere çarpıldığını gösteren 4'e üs (kuvvet), sonuca da üslü ifadenin değeri denir.",
             "ek": "5[[u:4]] \"beş üssü dört\" ya da \"beşin dördüncü kuvveti\" diye okunur. (s. 98)",
             "akilda": "Taban altta, üs üstte",
             "soru": G("2[[u:5]] kaçtır?", "32", "Taban 2, üs 5: 2 sayısını 5 kere çarp.",
                       "2 · 2 · 2 · 2 · 2: 4, 8, 16, 32. (s. 101)")},
            {"ad": "Kesrin Kuvveti", "renk": "#e8590c", "svg": svg10_top(),
             "aciklama": "Taban kesir olabilir. O zaman kesri parantez içine yazarız. Payın da paydanın da kuvveti alınır: ([[2/3]])[[u:2]] = [[2/3]] · [[2/3]] = [[4/9]].",
             "ek": "Kitaptaki örnek: ([[2/3]])[[u:5]] = [[32/243]]. 1'den küçük bir kesrin kuvveti alındıkça sayı küçülür. (s. 98)",
             "akilda": "Pay da payda da kuvvetlenir",
             "cozum": {"baslik": "Zıplayan top",
                       "problem": "Bir top her yere çarpışta, önceki yüksekliğinin yarısı kadar yükseliyor. 3. çarpıştan sonra, ilk yüksekliğin kaçta kaçına çıkar?",
                       "adimlar": [
                           {"metin": "Her çarpışta yükseklik [[1/2]] ile çarpılıyor.", "islem": "1. çarpış: [[1/2]]"},
                           {"metin": "3 çarpış: [[1/2]] üç kere çarpılıyor. Kısa yazalım.", "islem": "[[1/2]] · [[1/2]] · [[1/2]] = ([[1/2]])[[u:3]]"},
                           {"metin": "Pay: 1 · 1 · 1.", "islem": "Pay: 1"},
                           {"metin": "Payda: 2 · 2 · 2.", "islem": "([[1/2]])[[u:3]] = [[1/8]]"}],
                       "sonuc": "Top ilk yüksekliğin [[1/8]]'ine çıkar. (s. 97)"},
             "sende": {"baslik": "Harita büyüyor",
                       "problem": "Bir harita uygulamasında \"+\" tuşuna her basınca ekrandaki uzunluk [[3/2]] katına çıkıyor. Tuşa 2 kez basınca uzunluk ilk uzunluğun kaç katı olur?",
                       "adimlar": [
                           {"metin": "2 kez basınca [[3/2]] iki kere çarpılır.",
                            "soru": S("Hangi ifade doğru?", ["([[3/2]])[[u:2]]", "[[3/2]] · 2", "[[3/2]] + [[3/2]]"], 0, "Her basışta çarpıyoruz. Aynı kesir kaç kere çarpılıyor?", "[[3/2]] · [[3/2]] = ([[3/2]])[[u:2]]."),
                            "islem": "([[3/2]])[[u:2]]"},
                           {"metin": "Pay: 3 · 3. Payda: 2 · 2.",
                            "soru": G("([[3/2]])[[u:2]] kaçtır?", "9/4", "3 · 3 = ? 2 · 2 = ?", "3 · 3 = 9, 2 · 2 = 4: [[9/4]].", kesir=True),
                            "islem": "([[3/2]])[[u:2]] = [[9/4]]"}],
                       "sonuc": "Harika! Uzunluk ilk uzunluğun [[9/4]] katı olur. Başta 8 cm ise 8 · [[9/4]] = 18 cm olur. (Kitaptaki harita etkinliğine benzer, s. 99)"},
             "soru": G("([[1/2]])[[u:3]] kaçtır?", "1/8", "Pay: 1 · 1 · 1. Payda: 2 · 2 · 2.",
                       "1 · 1 · 1 = 1, 2 · 2 · 2 = 8: [[1/8]]. (s. 97)", kesir=True)},
            {"ad": "Eksi Taban: Çift Artı, Tek Eksi", "renk": "#3274d6", "svg": svg10_isaret(),
             "aciklama": "Taban artıysa her kuvveti artıdır. Taban eksiyse eksileri say: üs çiftse sonuç artı, üs tekse sonuç eksi.",
             "ek": f"({M}2)[[u:3]] = ({M}2) · ({M}2) · ({M}2) = {M}8: 3 eksi, tek. ({M}2)[[u:4]] = +16: 4 eksi, çift. (s. 100)",
             "akilda": "Çift üs artı, tek üs eksi",
             "cozum": {"baslik": "İşareti önce bul",
                       "problem": f"({M}2)[[u:4]] ve ({M}2)[[u:5]] kaçtır?",
                       "adimlar": [
                           {"metin": f"({M}2)[[u:4]]: dört tane ({M}2) çarpılıyor. 4 çift sayı.", "islem": "İşaret: artı"},
                           {"metin": "İşaretsiz değer: 2[[u:4]] = 16.", "islem": f"({M}2)[[u:4]] = +16"},
                           {"metin": f"({M}2)[[u:5]]: beş tane ({M}2). 5 tek sayı.", "islem": "İşaret: eksi"},
                           {"metin": "İşaretsiz değer: 2[[u:5]] = 32.", "islem": f"({M}2)[[u:5]] = {M}32"}],
                       "sonuc": "Önce üsse bak, işareti bul; sonra işaretsiz hesapla. (s. 100)"},
             "soru": N(f"({M}2)[[u:3]] kaçtır? Sayı doğrusunda dokun.", -8, sd(-8, 2),
                       "Üs 3: tek mi, çift mi? Sonra 2 · 2 · 2.", f"3 tek: sonuç eksi. 2 · 2 · 2 = 8: ({M}2)[[u:3]] = {M}8. (s. 100)")},
            {"ad": "Özel Tabanlar: 1, 0 ve Üs 1", "renk": "#b7791f", "svg": svg10_ozel(),
             "aciklama": "1'in her kuvveti 1'dir. 0'ın kuvvetleri 0'dır. Üs 1 ise sayı kendisi kalır.",
             "ek": f"Kitaptaki örnekler: 1[[u:2025]] = 1, 0[[u:7]] = 0, 1919[[u:1]] = 1919. ({M}1)'in kuvvetleri ya 1 ya {M}1 olur: ({M}1)[[u:19]] = {M}1, çünkü 19 tek. (s. 101)",
             "akilda": "1 hep 1, 0 hep 0",
             "soru": S("1[[u:2025]] kaçtır?", ["2025", "1", "0"], 1,
                       "1'i kendisiyle kaç kere çarparsan çarp, ne olur?", "1 · 1 · 1 · … = 1. (s. 101)")},
            {"ad": "Parantez Fark Yaratır", "renk": "#c92a2a", "svg": svg10_parantez(),
             "aciklama": f"({M}3)[[u:2]] demek iki tane ({M}3)'ün çarpımı: +9. {M}3[[u:2]] demek önce 3[[u:2]], sonra başına eksi: {M}9.",
             "ek": "Parantez yoksa üs sadece hemen önündeki sayıya aittir; eksi işareti kuvvete katılmaz. (s. 101, Dikkat kutusu)",
             "akilda": "Parantez yoksa eksi dışarıda",
             "cozum": {"baslik": "İki ifade aynı mı?",
                       "problem": f"({M}3)[[u:2]] ile {M}3[[u:2]] ifadelerini karşılaştıralım.",
                       "adimlar": [
                           {"metin": f"Parantez var: taban {M}3. İki tane ({M}3) çarpılır.", "islem": f"({M}3) · ({M}3) = +9"},
                           {"metin": "Parantez yok: üs sadece 3'e ait.", "islem": "3[[u:2]] = 3 · 3 = 9"},
                           {"metin": "Eksi işareti en sonda başa gelir.", "islem": f"{M}3[[u:2]] = {M}9"},
                           {"metin": "Sonuçları karşılaştır.", "islem": f"+9 ≠ {M}9"}],
                       "sonuc": "Parantezin yeri sonucu değiştirir. (s. 101)"},
             "soru": S(f"{M}4[[u:2]] kaçtır?", ["16", f"{M}16", f"{M}8"], 1,
                       "Parantez var mı? Yoksa üs sadece 4'e ait.", f"Parantez yok: 4[[u:2]] = 16, başına eksi: {M}16. (s. 101)")}
        ],
        "biliyorMusun": [
            "Telefon ve bilgisayarların depolama kapasiteleri genellikle 2'nin kuvvetleridir: 8, 16, 32, 64… (s. 98)",
            "Yoğurt ve turşuda faydalı bakteriler vardır. Uygun ortamda bakteriler katlanarak, yani üssel olarak çoğalır. (s. 96, 98)"],
        "akildaKalsin": [
            "Tekrarlı çarpımı üslü yaz: 5 · 5 · 5 · 5 = 5[[u:4]].",
            "Taban tekrar eden sayı, üs kaç kere çarpıldığı.",
            "5[[u:4]], 5 · 4 değildir!",
            "Kesrin kuvvetinde pay da payda da kuvvetlenir.",
            "Eksi tabanda çift üs artı, tek üs eksi.",
            f"({M}3)[[u:2]] = +9 ama {M}3[[u:2]] = {M}9."],
        "merakKutusu": [
            {"soru": "Bilgisayarların hafızası neden hep 8, 16, 32, 64 gibi sayılar?", "cevap": "Bu sayılar 2'nin kuvvetleridir: 2[[u:3]] = 8, 2[[u:4]] = 16, 2[[u:5]] = 32, 2[[u:6]] = 64. Depolama birimleri genellikle böyle büyür. (s. 98)"},
            {"soru": "Üssel büyüme ne demek?", "cevap": "Bir değerin her adımda aynı miktar eklenerek değil, katlanarak değişmesidir. Bakteri sayısı 1, 2, 4, 8, 16… diye çok hızlı büyür. (s. 98)"},
            {"soru": "Kesrin kuvvetini alınca sayı neden küçülüyor?", "cevap": "1'den küçük bir kesirle çarpınca sayının bir parçasını alırız. Top her zıplayışta yarıya iner: [[1/2]], [[1/4]], [[1/8]]… (s. 97)"},
            {"soru": "Radyoaktif maddeler nasıl azalır?", "cevap": "Bazı radyoaktif maddelerin miktarı zamanla kendiliğinden yarıya iner. Bu azalma da üssel olur. (s. 98)"},
            {"soru": f"({M}1)'in kuvvetleri neden hep 1 ya da {M}1?", "cevap": f"1 · 1 hep 1 olur; sadece işaret değişir. Üs çiftse +1, tekse {M}1: ({M}1)[[u:28]] = 1, ({M}1)[[u:29]] = {M}1. (s. 101)"}],
        "dusunVeYaz": [{"soru": f"Ece, \"({M}2)[[u:6]] ile {M}2[[u:6]] aynı sayıdır\" dedi. Haklı mı? Açıkla.",
                        "ornekCevap": f"Haklı değil. ({M}2)[[u:6]]'da taban {M}2; 6 tane eksi var, 6 çift → +64. {M}2[[u:6]]'da parantez yok, üs sadece 2'ye ait: 2[[u:6]] = 64, başına eksi → {M}64.",
                        "anahtarlar": ["parantez", "64", "çift", "taban"]}],
        "sorular": [
            S("7 · 7 · 7 · 7 · 7 çarpımının üslü gösterimi hangisidir?", ["7[[u:5]]", "5[[u:7]]", "7 · 5"], 0,
              "Taban tekrar eden sayı, üs kaç kere çarpıldığı.", "7 sayısı 5 kere çarpılıyor: 7[[u:5]]. (s. 99)"),
            G("4[[u:3]] kaçtır?", "64", "4'ü 3 kere çarp: 4 · 4 · 4.", "4 · 4 = 16, 16 · 4 = 64. (s. 101)"),
            S("6[[u:2]] ifadesinde taban ve üs hangisidir?", ["Taban 2, üs 6", "Taban 6, üs 2", "Taban 6, üs 6"], 1,
              "Büyük yazılan sayı taban, sağ üstteki küçük sayı üs.", "Taban 6, üs 2: 6 · 6 = 36. (s. 98)"),
            G("([[2/3]])[[u:2]] kaçtır?", "4/9", "Pay: 2 · 2. Payda: 3 · 3.", "2 · 2 = 4, 3 · 3 = 9: [[4/9]]. (s. 98)", kesir=True),
            N(f"({M}1)[[u:5]] kaçtır? Sayı doğrusunda dokun.", -1, sd(-3, 3),
              "Taban eksi, üs 5. 5 tek mi, çift mi?", f"5 tek: sonuç eksi. 1 · 1 · 1 · 1 · 1 = 1: ({M}1)[[u:5]] = {M}1. (s. 101)"),
            S("Hangisinin değeri eksidir?", ["5[[u:3]]", f"({M}5)[[u:2]]", f"({M}5)[[u:3]]"], 2,
              "Taban artıysa sonuç hep artı. Taban eksiyse üs tek mi, çift mi?", f"({M}5)[[u:3]]: taban eksi, üs 3 tek → eksi: {M}125. (s. 100)"),
            S("0[[u:7]] + 1[[u:7]] kaçtır?", ["0", "7", "1"], 2,
              "0'ın her kuvveti 0, 1'in her kuvveti 1.", "0[[u:7]] = 0, 1[[u:7]] = 1. 0 + 1 = 1. (s. 101)"),
            G(f"{M}2[[u:4]] kaçtır?", "-16", "Parantez yok: üs sadece 2'ye ait.", f"2[[u:4]] = 16. Başına eksi: {M}16. (s. 101)"),
            N("([[-1/2]])[[u:2]] kaçtır? Sayı doğrusunda dokun.", 0.25, sd(-1, 1, bolme=4),
              "Taban eksi, üs 2 çift: sonuç artı. Pay 1 · 1, payda 2 · 2.", "Çift üs → artı. [[1/2]] · [[1/2]] = [[1/4]]. (s. 101)"),
            G("Bir bakteri her 30 dakikada ikiye bölünüyor. Başta 1 bakteri var. 3 saat sonra kaç bakteri olur?", "64",
              "3 saatte kaç tane 30 dakika var? Her seferinde 2 ile çarp.", "3 saat = 6 kere 30 dakika. 2[[u:6]] = 64 bakteri. (s. 96)")]
    }


# ---------- u1k11 Rasyonel Sayılarla Bölme ----------
def svg11_sise():
    g = ""
    for i, x in enumerate((14, 46, 78)):
        g += f"<rect x='{x}' y='34' width='14' height='40' fill='{OB}' stroke='#f5f6fa' stroke-width='1.5'/>"
        g += f"<rect x='{x + 14}' y='34' width='14' height='40' fill='#c9733f' stroke='#f5f6fa' stroke-width='1.5'/>"
        g += txt(x + 14, 26, "1 L", "#f5f6fa", 11)
    g += txt(60, 102, "3 ÷ ½ = 6", "#f2c14e", 17)
    return bg(g)


def svg11_ters():
    g = kesir_svg(32, 44, "2", "3", OB, 22) + kesir_svg(88, 44, "3", "2", OB, 22)
    g += "<path d='M48 38 Q60 26 72 38' stroke='#f2c14e' stroke-width='2.5' fill='none'/><path d='M72 38 l-7 -1 4 -6z' fill='#f2c14e'/>"
    g += "<path d='M72 66 Q60 78 48 66' stroke='#f2c14e' stroke-width='2.5' fill='none'/><path d='M48 66 l7 1 -4 6z' fill='#f2c14e'/>"
    g += txt(60, 106, "çarpımı 1", "#f2c14e", 14)
    return bg(g)


def svg11_kct():
    g = kesir_svg(36, 26, "4", "9", "#f5f6fa", 14) + txt(60, 36, "÷", "#f5f6fa", 18) + kesir_svg(84, 26, "7", "3", "#f5f6fa", 14)
    g += "<path d='M60 52 v10 M55 58 l5 6 5 -6' stroke='#f2c14e' stroke-width='2.5' fill='none' stroke-linecap='round'/>"
    g += kesir_svg(36, 76, "4", "9", "#f5f6fa", 14) + txt(60, 86, "·", "#f2c14e", 22) + kesir_svg(84, 76, "3", "7", OB, 14)
    g += txt(60, 112, "koru · çevir · ters", "#f2c14e", 10)
    return bg(g)


def svg11_esit():
    g = kesir_svg(30, 38, "6", "7", OB, 18) + txt(60, 48, "÷", "#f5f6fa", 20) + kesir_svg(90, 38, "2", "7", OB, 18)
    g += "<circle cx='30' cy='54' r='12' fill='none' stroke='#f2c14e' stroke-width='2'/><circle cx='90' cy='54' r='12' fill='none' stroke='#f2c14e' stroke-width='2'/>"
    g += txt(60, 100, "6 ÷ 2 = 3", "#f2c14e", 16)
    return bg(g)


def svg11_tamli():
    g = txt(60, 34, f"({M}3¼) ÷ 2⅔", NB, 15)
    g += "<path d='M60 44 v10 M55 50 l5 6 5 -6' stroke='#f2c14e' stroke-width='2.5' fill='none' stroke-linecap='round'/>"
    g += txt(60, 76, f"{M}13/4 · 3/8", NB, 15)
    g += txt(60, 104, f"farklı → {M}", "#f2c14e", 14)
    return bg(g)


def svg11_cizgi():
    g = txt(60, 34, "5/4", OB, 18) + "<line x1='34' y1='44' x2='86' y2='44' stroke='#f5f6fa' stroke-width='3' stroke-linecap='round'/>" + txt(60, 66, "1/3", OB, 18)
    g += txt(60, 100, "5/4 ÷ 1/3", "#f2c14e", 16)
    return bg(g)


def u1k11():
    sk = lambda mn, mx, b, **ek: dict({"min": mn, "max": mx, "bolme": b}, **ek)
    return {
        "id": "u1k11", "unite": "1. Tema: Sayılar ve Nicelikler", "baslik": "Rasyonel Sayılarla Bölme", "sayfalar": "s. 102–107",
        "giris": "Kesirleri çarpmayı öğrendin. Bölme çok kolay olacak, çünkü her bölmeyi bir çarpmaya çevireceğiz! Sirke şişeleri, asansör ve kablolar bize yardım edecek.",
        "hazirlik": {
            "baslik": "Hazır mısın?",
            "giris": "Bu konu kesirlerde çarpma, tam sayılı kesirler ve bölmede işaret üzerine kuruluyor. Önce bunları hatırlıyor musun bakalım. Not yok.",
            "maddeler": [
                {"ad": "Kesirlerde çarpma ve çapraz sadeleştirme", "sinif": "9. konu", "svg": svg9_capraz(),
                 "anlatim": "Pay paya, payda paydaya çarpılır. Çarpmadan önce bir pay ile bir paydayı aynı sayıya bölerek sadeleştir: [[3/4]] · [[8/9]] → [[1/1]] · [[2/3]] = [[2/3]].",
                 "akilda": "Önce sadeleştir, sonra çarp",
                 "ornek": {"problem": "[[2/5]] · [[5/6]] kaçtır?", "adimlar": [
                     {"metin": "Üstteki 5 ile alttaki 5'i 5'e böl.", "islem": "5 → 1, 5 → 1"},
                     {"metin": "Üstteki 2 ile alttaki 6'yı 2'ye böl.", "islem": "2 → 1, 6 → 3"},
                     {"metin": "Küçülen sayıları çarp.", "islem": "[[2/5]] · [[5/6]] = [[1/3]]"}]},
                 "sorular": [
                     G("[[4/7]] · [[7/8]] kaçtır? En sade hâliyle yaz.", "1/2", "7 ile 7'yi, 4 ile 8'i sadeleştir.", "7 → 1, 7 → 1; 4 → 1, 8 → 2: [[1/2]].", kesir=True),
                     G("[[3/10]] · [[5/9]] kaçtır? En sade hâliyle yaz.", "1/6", "3 ile 9'u 3 böler, 5 ile 10'u 5 böler.", "3 → 1, 9 → 3; 5 → 1, 10 → 2: [[1/6]].", kesir=True)]},
                {"ad": "Tam sayılı kesir → bileşik kesir", "sinif": "2. konu", "svg": svg_h_tamli(),
                 "anlatim": "Tam kısmı payda ile çarp, payı ekle; payda aynı kalır: [[2 3/4]] = [[11/4]]. Eksi sayının tamamına aittir: [[-1 1/2]] = [[-3/2]].",
                 "akilda": "Tam · payda + pay",
                 "ornek": {"problem": "[[3 2/5]] sayısını bileşik kesre çevirelim.", "adimlar": [
                     {"metin": "Tam kısmı payda ile çarp, payı ekle: 3 · 5 + 2.", "islem": "3 · 5 + 2 = 17"},
                     {"metin": "Payda 5 kalır.", "islem": "[[3 2/5]] = [[17/5]]"}]},
                 "sorular": [
                     G("[[3 1/2]] sayısını bileşik kesir olarak yaz.", "7/2", "3 · 2 + 1 = ? Payda 2 kalır.", "3 · 2 + 1 = 7: [[7/2]].", kesir=True),
                     G("[[-2 1/4]] sayısını bileşik kesir olarak yaz.", "-9/4", "Eksiyi kenara koy: 2 · 4 + 1 = ? Sonra eksiyi geri ekle.", "2 · 4 + 1 = 9: [[-9/4]].", kesir=True, kabul=["9/-4"])]},
                {"ad": "Bölmede işaret", "sinif": "7. konu", "svg": svg6_isaret("farkli"),
                 "anlatim": "Bölmede de çarpmadaki kural geçerli: aynı işaretli iki sayının bölümü artı, farklı işaretli iki sayının bölümü eksidir.",
                 "akilda": "Aynı artı, farklı eksi",
                 "ornek": {"problem": "(−20) ÷ 4 kaçtır?", "adimlar": [
                     {"metin": "Önce işaretsiz böl: 20 ÷ 4.", "islem": "20 ÷ 4 = 5"},
                     {"metin": "İşaretler farklı → eksi.", "islem": "(−20) ÷ 4 = −5"}]},
                 "sorular": [
                     G("(−18) ÷ (−6) kaçtır?", "3", "Önce 18 ÷ 6. İşaretler aynı mı?", "18 ÷ 6 = 3. İki eksi: aynı işaret → +3."),
                     S("(+24) ÷ (−8) kaçtır?", ["+3", "−3", "−16"], 1, "Önce 24 ÷ 8. İşaretler farklı.", "24 ÷ 8 = 3. Farklı işaret → −3.")]}
            ]},
        "kavramlar": [
            {"ad": "Kaç Tane Sığar?", "renk": "#1f9e8f", "svg": svg11_sise(),
             "aciklama": "Bölme, “içinde kaç tane var?” sorusunun cevabıdır. 6 litre sirkeyi [[1/2]] litrelik şişelere doldurmak: 6'nın içinde kaç tane [[1/2]] var?",
             "ek": "Kitaptaki modelde her litre 2 eş parçaya ayrılır: 6 · 2 = 12 şişe. Yani 6 ÷ [[1/2]] ile 6 · 2 aynı sonucu verir. (s. 102)",
             "akilda": "Bölme: kaç tane sığar?",
             "cozum": {"baslik": "Sirke şişeleri",
                       "problem": "Zehra teyzenin 6 litre sirkesi var. Hepsini [[1/2]] litrelik şişelere dolduracak. Kaç şişe gerekir?",
                       "adimlar": [
                           {"metin": "Ne veriliyor? 6 litre sirke, şişeler [[1/2]] litre. Ne isteniyor? Şişe sayısı.", "islem": "6 ÷ [[1/2]]"},
                           {"metin": "Her litreyi 2 eş parçaya ayır: 1 litre 2 şişeyi doldurur.", "islem": "1 litre → 2 şişe"},
                           {"metin": "6 litre var: 6 kere 2 şişe.", "islem": "6 · 2 = 12"}],
                       "sonuc": "12 şişe gerekir. 6 ÷ [[1/2]] = 6 · 2 = 12. (s. 102)"},
             "soru": S("3 litre suyu [[1/4]] litrelik bardaklara dolduruyoruz. Kaç bardak dolar?", ["[[3/4]]", "7", "12"], 2,
                       "1 litreye kaç tane [[1/4]] litrelik bardak sığar? Sonra 3 litre için düşün.",
                       "1 litre = 4 bardak. 3 litre: 3 · 4 = 12 bardak. Yani 3 ÷ [[1/4]] = 12. (s. 102)")},
            {"ad": "Ters Çevir", "renk": "#7b4fc9", "svg": svg11_ters(),
             "aciklama": "Bir kesrin çarpma işlemine göre tersini bulmak için payla paydanın yerini değiştir. İşaret aynı kalır.",
             "ek": "Bir sayı ile tersinin çarpımı 1'dir: [[2/7]] · [[7/2]] = 1. Tam sayıyı önce [[5/1]] gibi yaz: 5'in tersi [[1/5]]. 0'ın tersi yoktur. (s. 103)",
             "akilda": "Pay ile payda yer değiştirir",
             "soru": G("[[-4/9]] sayısının çarpma işlemine göre tersini yaz.", "-9/4",
                       "Pay ile paydanın yerini değiştir. İşaret değişmez.", "4 ile 9 yer değiştirir, eksi kalır: [[-9/4]]. (s. 103)",
                       kesir=True, kabul=["9/-4"])},
            {"ad": "Böl = Tersiyle Çarp", "renk": "#e8590c", "svg": svg11_kct(),
             "aciklama": "Bölmeyi çarpmaya çevir: birinci sayıyı koru, ÷ işaretini · yap, ikinci sayıyı ters çevir. Sonra bildiğin gibi çarp: önce çapraz sadeleştir.",
             "ek": "Kitaptaki örnek: [[4/9]] ÷ [[7/3]] = [[4/9]] · [[3/7]]. 3 ile 9 sadeleşir: [[4/3]] · [[1/7]] = [[4/21]]. Yalnızca ikinci sayı ters çevrilir! (s. 104)",
             "akilda": "Koru, çevir, ters çevir",
             "cozum": {"baslik": "Kitaptaki örnek",
                       "problem": "[[4/9]] ÷ [[7/3]] işlemini yapalım.",
                       "adimlar": [
                           {"metin": "Birinci sayıyı koru.", "islem": "[[4/9]]"},
                           {"metin": "÷ işaretini · yap, ikinci sayıyı ters çevir: [[7/3]] → [[3/7]].", "islem": "[[4/9]] · [[3/7]]"},
                           {"metin": "Çapraz sadeleştir: üstteki 3 ile alttaki 9'u 3 böler.", "islem": "3 → 1, 9 → 3"},
                           {"metin": "Çarp: pay 4 · 1, payda 3 · 7.", "islem": "[[4/9]] ÷ [[7/3]] = [[4/21]]"}],
                       "sonuc": "[[4/9]] ÷ [[7/3]] = [[4/21]]. (s. 104)"},
             "sende": {"baslik": "Sıra sende",
                       "problem": "[[5/6]] ÷ [[10/9]] işlemini yap.",
                       "adimlar": [
                           {"metin": "Koru, çevir, ters çevir.",
                            "soru": S("[[5/6]] ÷ [[10/9]] hangi çarpmaya dönüşür?", ["[[6/5]] · [[10/9]]", "[[5/6]] · [[9/10]]", "[[5/6]] · [[10/9]]"], 1,
                                      "Birinci sayı aynen kalır. Hangisi ters çevrilir?", "Birinciyi koru, ikinciyi ters çevir: [[5/6]] · [[9/10]]."),
                            "islem": "[[5/6]] · [[9/10]]"},
                           {"metin": "Çapraz sadeleştir: 5 ile 10'u 5'e, 9 ile 6'yı 3'e böl.",
                            "soru": S("Sadeleşince ne kalır?", ["[[1/2]] · [[3/2]]", "[[1/2]] · [[3/1]]", "[[5/2]] · [[3/2]]"], 0,
                                      "5 ÷ 5 = 1, 10 ÷ 5 = 2. 9 ÷ 3 = 3, 6 ÷ 3 = 2. Her sayı kendi yerinde kalır.", "5 → 1, 6 → 2, 9 → 3, 10 → 2: [[1/2]] · [[3/2]]."),
                            "islem": "[[1/2]] · [[3/2]]"},
                           {"metin": "Şimdi çarp.",
                            "soru": G("Sonuç kaçtır?", "3/4", "Pay 1 · 3, payda 2 · 2.", "1 · 3 = 3, 2 · 2 = 4: [[3/4]].", kesir=True),
                            "islem": "= [[3/4]]"}],
                       "sonuc": "Harika! [[5/6]] ÷ [[10/9]] = [[3/4]]."},
             "soru": G("[[3/5]] ÷ [[9/10]] kaçtır? En sade hâliyle yaz.", "2/3",
                       "Koru, çevir, ters çevir: [[3/5]] · [[10/9]]. Sonra çapraz sadeleştir.",
                       "[[3/5]] · [[10/9]]: 3 ile 9'u 3'e, 10 ile 5'i 5'e böl: [[1/1]] · [[2/3]] = [[2/3]]. (s. 104)", kesir=True)},
            {"ad": "Paydalar Eşitse Payları Böl", "renk": "#1d6fa3", "svg": svg11_esit(),
             "aciklama": "Paydaları eşit olan iki kesirde payları birbirine bölebilirsin.",
             "ek": "Kitaptaki 1. yöntem: [[4/9]] ÷ [[7/3]] = [[4/9]] ÷ [[21/9]] = 4 ÷ 21 = [[4/21]]. Paydalar farklıysa önce eşitlemek gerekir; bu yüzden biz çoğunlukla tersiyle çarpacağız. (s. 104)",
             "akilda": "Eşit payda: payları böl",
             "cozum": {"baslik": "Eşit paydalar",
                       "problem": "[[6/7]] ÷ [[2/7]] işlemini yapalım.",
                       "adimlar": [
                           {"metin": "Paydalar aynı mı? İkisi de 7.", "islem": "Payda: 7 = 7"},
                           {"metin": "Payları böl: 6 ÷ 2.", "islem": "6 ÷ 2 = 3"},
                           {"metin": "Kontrol: tersiyle çarp. 7 ile 7, 6 ile 2 sadeleşir.", "islem": "[[6/7]] · [[7/2]] = 3"}],
                       "sonuc": "[[6/7]] ÷ [[2/7]] = 3. [[6/7]]'nin içinde 3 tane [[2/7]] var. (s. 104)"},
             "soru": S("[[8/5]] ÷ [[2/5]] kaçtır?", ["4", "[[16/25]]", "[[4/5]]"], 0,
                       "Paydalar eşit. Payları böl: 8 ÷ 2.", "Paydalar eşit, payları böl: 8 ÷ 2 = 4. (s. 104)")},
            {"ad": "Tam Sayılı Kesir ve İşaret", "renk": "#c92a2a", "svg": svg11_tamli(),
             "aciklama": "Tam sayılı kesri önce bileşik kesre çevir. İşaret, tam sayılarda bölmedeki gibi: aynı işaret artı, farklı işaret eksi.",
             "ek": "Kitaptaki örnek: ([[-3 1/4]]) ÷ [[2 2/3]] = ([[-13/4]]) ÷ [[8/3]] = ([[-13/4]]) · [[3/8]] = [[-39/32]]. (s. 104)",
             "akilda": "Önce çevir, sonra işaret",
             "cozum": {"baslik": "Asansör iniyor",
                       "problem": "Bir asansör zemin kattan [[11 1/5]] m aşağı indi. Katlar arası 2,8 m. Asansör kaçıncı katta?",
                       "adimlar": [
                           {"metin": "Başlangıç (0): zemin kat. Aşağı eksidir.", "islem": "[[-11 1/5]] m"},
                           {"metin": "Kaç kat? Her kat 2,8 m: bu bir paylaştırma, böl. 2,8 = [[28/10]].", "islem": "([[-11 1/5]]) ÷ [[28/10]]"},
                           {"metin": "Çevir: 11 · 5 + 1 = 56. Sonra koru, çevir, ters çevir.", "islem": "([[-56/5]]) · [[10/28]]"},
                           {"metin": "Çapraz sadeleştir: 56 ile 28'i 28'e, 10 ile 5'i 5'e böl. İşaret: farklı → eksi.", "islem": "([[-2/1]]) · [[2/1]] = −4"}],
                       "sonuc": "Asansör zemin katın 4 kat altında: −4. kat. (s. 104)"},
             "sende": {"baslik": "Kablo kesiliyor",
                       "problem": "Bir elektrik ustası [[9 3/5]] m kabloyu 8 eş parçaya ayıracak. Bir parça kaç metre?",
                       "adimlar": [
                           {"metin": "Ne veriliyor? [[9 3/5]] m kablo, 8 eş parça. Ne isteniyor? Bir parça.",
                            "soru": S("Hangi işlem yapılır?", ["[[9 3/5]] · 8", "[[9 3/5]] ÷ 8", "8 ÷ [[9 3/5]]"], 1,
                                      "Kabloyu 8 eş parçaya ayırıyoruz. Paylaştırınca hangi işlem?", "Kablo 8'e paylaştırılır: [[9 3/5]] ÷ 8."),
                            "islem": "[[9 3/5]] ÷ 8"},
                           {"metin": "Tam sayılı kesri çevir: 9 · 5 + 3.",
                            "soru": G("[[9 3/5]] bileşik kesir olarak kaçtır?", "48/5", "9 · 5 + 3 = ? Payda 5 kalır.", "9 · 5 + 3 = 48: [[48/5]].", kesir=True),
                            "islem": "[[48/5]] ÷ 8 = [[48/5]] · [[1/8]]"},
                           {"metin": "48 ile 8'i 8 böler: 48 → 6, 8 → 1. Şimdi çarp.",
                            "soru": G("Bir parça kaç metre? Bileşik kesir olarak yaz.", "6/5", "Pay 6 · 1, payda 5 · 1.", "[[6/5]] m = [[1 1/5]] m.", kesir=True, denk=True, birim="m"),
                            "islem": "= [[6/5]] = [[1 1/5]] m"}],
                       "sonuc": "Harika! Her parça [[1 1/5]] m. (s. 104)"},
             "soru": S("([[-1 1/2]]) ÷ ([[-3/4]]) kaçtır?", ["−2", "2", "[[9/8]]"], 1,
                       "Çevir: [[-1 1/2]] = [[-3/2]]. İki eksi → artı. Sonra koru, çevir, ters çevir.",
                       "([[-3/2]]) · ([[-4/3]]): aynı işaret → artı. 3 ile 3, 4 ile 2 sadeleşir: 2. (s. 104)")},
            {"ad": "Kesir Çizgisi de Bölmedir", "renk": "#b7791f", "svg": svg11_cizgi(),
             "aciklama": "Bölme kesir çizgisiyle de gösterilebilir: üstteki sayı bölünen, alttaki bölendir. Bir sayıyı 1'e bölünce kendisi, 1'i bir sayıya bölünce o sayının tersi çıkar.",
             "ek": "[[5/4]] ÷ [[1/3]] işlemi alt alta, kesir çizgisiyle de yazılabilir. Bölmede sayıların yeri değişirse sonuç değişir: bölmenin değişme özelliği yoktur. (s. 106)",
             "akilda": "1'e böl: aynı. 1'i böl: ters.",
             "soru": S("1 ÷ [[2/7]] kaçtır?", ["[[7/2]]", "[[2/7]]", "1"], 0,
                       "1'i bir sayıya bölünce o sayının tersi çıkar.", "1 ÷ [[2/7]] = 1 · [[7/2]] = [[7/2]]. (s. 106)")}
        ],
        "akildaKalsin": [
            "Bölme: içinde kaç tane sığar?",
            "Bölmeyi çarpmaya çevir: birinciyi koru, ikinciyi ters çevir.",
            "Ters çevirince işaret değişmez; 0'ın tersi yoktur.",
            "Paydalar eşitse payları böl.",
            "Tam sayılı kesri önce bileşik kesre çevir; işaret: aynı artı, farklı eksi.",
            "Bir sayı ÷ 1 = kendisi; 1 ÷ bir sayı = tersi."],
        "merakKutusu": [
            {"soru": "Bölünce sayı hep küçülür mü?", "cevap": "Hayır. 1'den küçük bir sayıya bölersen sonuç büyür: 6 ÷ [[1/2]] = 12. 6 litrenin içine 12 tane yarım litre sığar. (s. 102)"},
            {"soru": "Neden ikinci sayıyı ters çeviriyoruz?", "cevap": "Kitaptaki şişe modelinde 6'yı [[1/2]]'ye bölmek ile 6'yı 2 ile çarpmak aynı sonucu veriyor. 2, [[1/2]]'nin tersidir. (s. 102–103)"},
            {"soru": "Birinci sayıyı da ters çevirsem olur mu?", "cevap": "Olmaz. Yalnızca bölen, yani ikinci sayı ters çevrilir. [[2/3]] ÷ [[3/4]] = [[8/9]]; birinciyi çevirip çarparsan [[3/2]] · [[3/4]] = [[9/8]] gibi yanlış bir sonuç çıkar."},
            {"soru": "Bölmede sayıların yerini değiştirebilir miyim?", "cevap": "Hayır. [[2/3]] ÷ [[3/4]] = [[8/9]] ama [[3/4]] ÷ [[2/3]] = [[9/8]]. Bölmenin değişme özelliği yoktur. (s. 106)"},
            {"soru": "0'a bölebilir miyiz?", "cevap": "Hayır. 0 ile hangi sayıyı çarparsan çarp 1 bulamazsın; bu yüzden 0'ın tersi yoktur. Kitap da 1'in yalnızca sıfır dışındaki sayılara bölümünden söz eder. (s. 106)"},
            {"soru": "Ekmeği 8 kez kesersem kaç dilim olur?", "cevap": "9 dilim! Kitaptaki fırıncı [[20 2/5]] cm'lik ekmeği 8 kez kesiyor: 9 dilim çıkar. Bir dilim [[102/5]] ÷ 9 = [[34/15]] cm. Sayarken dikkat: kesim sayısı + 1 = dilim sayısı. (s. 105)"}],
        "dusunVeYaz": [{"soru": "Can [[6/7]] ÷ [[2/3]] işleminde birinci kesri ters çevirip [[7/6]] · [[2/3]] = [[7/9]] buldu. Hatası ne? Doğru sonucu bul.",
                        "ornekCevap": "Yanlış sayıyı ters çevirmiş. Birinci sayı korunur, ikinci sayı ters çevrilir: [[6/7]] · [[3/2]] = [[9/7]] = [[1 2/7]].",
                        "anahtarlar": ["ikinci", "ters", "koru", "9"]}],
        "sorular": [
            S("[[2/3]] ÷ [[3/4]] kaçtır?", ["[[8/9]]", "[[1/2]]", "[[9/8]]"], 0,
              "Koru, çevir, ters çevir: [[2/3]] · [[4/3]].", "[[2/3]] · [[4/3]] = [[8/9]]. (s. 105)"),
            G("[[9/8]] ÷ [[1/3]] kaçtır?", "27/8", "Koru, çevir, ters çevir: [[9/8]] · 3.",
              "[[9/8]] · [[3/1]] = [[27/8]] = [[3 3/8]]. (s. 105)", kesir=True, denk=True),
            N("([[-1/2]]) ÷ [[2/3]] işleminin sonucuna sayı doğrusunda dokun.", -0.75, sk(-2, 1, 4),
              "Farklı işaret → eksi. ([[-1/2]]) · [[3/2]].", "([[-1/2]]) · [[3/2]] = [[-3/4]]. (s. 105)"),
            S("(−8) ÷ ([[-4/3]]) kaçtır?", ["6", "−6", "[[32/3]]"], 0,
              "İki eksi → artı. (−8) · ([[-3/4]]).", "8 ile 4 sadeleşir: 2 · 3 = 6. Aynı işaret → +6. (s. 105)"),
            S("[[1 1/3]] ÷ [[1 1/4]] kaçtır?", ["[[15/16]]", "[[1 1/12]]", "[[16/15]]"], 2,
              "Önce ikisini de çevir: [[4/3]] ÷ [[5/4]].", "[[4/3]] · [[4/5]] = [[16/15]]. Tamları ayrı bölmek yanlış olur. (s. 105)"),
            G("Bir elektrik ustası [[3/4]] m kabloyu [[1/8]] m'lik parçalara ayırıyor. Kaç parça elde eder?", "6",
              "Kaç tane sığar? [[3/4]] ÷ [[1/8]].", "[[3/4]] · 8: 4 ile 8 sadeleşir: 3 · 2 = 6 parça. (Kitaptaki kablo örneğine benzer, s. 104)"),
            S("[[10/3]] ÷ [[5/3]] kaçtır?", ["[[2/3]]", "2", "[[50/9]]"], 1,
              "Paydalar eşit: payları böl.", "Paydalar eşit: 10 ÷ 5 = 2. (s. 104)"),
            S("Hangisi doğrudur?", ["[[2/3]] ÷ 1 = [[3/2]]", "[[2/3]] ÷ [[3/4]] = [[3/4]] ÷ [[2/3]]", "1 ÷ [[2/3]] = [[3/2]]"], 2,
              "1'e bölmek sayıyı değiştirmez. 1'i bir sayıya bölünce tersi çıkar.",
              "1 ÷ [[2/3]] = [[3/2]]. [[2/3]] ÷ 1 = [[2/3]] olur; bölmede yer değiştirince sonuç değişir. (s. 106)"),
            N("Derin dondurucudaki bir gıdanın sıcaklığı 3 dakikada [[3/2]] °C düştü. 1 dakikadaki ortalama değişime sayı doğrusunda dokun.", -0.5, sk(-2, 1, 2),
              "Düşmek eksidir: ([[-3/2]]) ÷ 3.", "([[-3/2]]) · [[1/3]] = [[-1/2]] °C. (Kitaptaki derin dondurucu örneğine benzer, s. 104)"),
            S("Hangi sayının çarpma işlemine göre tersi yoktur?", ["1", "0", "−1"], 1,
              "Hangi sayıyla neyi çarparsan çarp 1 bulamazsın?", "0 ile hangi sayıyı çarparsan çarp sonuç 0 olur, 1 olamaz. Bu yüzden 0'ın tersi yoktur ve 0'a bölme yapılmaz."),
            G("Esra'nın 5 m kurdelesi kaldı. Büyük bir hediye paketi için [[5/4]] m kurdele gerekiyor. En fazla kaç büyük paket süsleyebilir?", "4",
              "Kaç tane sığar? 5 ÷ [[5/4]].", "5 ÷ [[5/4]] = 5 · [[4/5]] = 4 paket. (Kitaptaki kurdele problemine benzer, s. 106)")]
    }


# ---------- u1k12 çizimleri ----------
def svg12_valiz():
    g = "<rect x='22' y='40' width='60' height='56' rx='8' fill='#f5f6fa'/><rect x='40' y='28' width='24' height='14' rx='5' fill='none' stroke='#f5f6fa' stroke-width='4'/>"
    g += "<line x1='22' y1='58' x2='82' y2='58' stroke='#9aa3bf' stroke-width='3'/>"
    g += txt(52, 84, "4 kg", "#1b2340", 15)
    for i, y in enumerate([30, 54, 78]):
        g += f"<circle cx='100' cy='{y}' r='10' fill='#f2c14e'/>" + txt(100, y + 5, str(i + 1), "#1b2340", 13)
    g += txt(60, 113, "sınır 20 kg", OB, 12)
    return bg(g)


def svg12_merdiven():
    adim = [("1", "üs", "#f2c14e"), ("2", "( )", OB), ("3", "· ÷", "#5fd08f"), ("4", "+ −", NB)]
    g = ""
    for i, (n, e, r) in enumerate(adim):
        x, y = 8 + i * 18, 8 + i * 22
        g += f"<rect x='{x}' y='{y}' width='{110 - x}' height='22' rx='4' fill='#2b355c' stroke='{r}' stroke-width='2'/>"
        g += txt(x + 10, y + 16, n, r, 13) + txt(x + 34, y + 16, e, "#f5f6fa", 14)
    g += txt(60, 114, "yukarıdan aşağı", "#9aa3bf", 11)
    return bg(g)


def svg12_soldan():
    g = txt(60, 62, "20 ÷ 4 · 5", "#f5f6fa", 18)
    g += "<path d='M16 34 H100' stroke='#f2c14e' stroke-width='3' stroke-linecap='round'/><path d='M104 34l-8-5v10z' fill='#f2c14e'/>"
    g += f"<circle cx='42' cy='84' r='10' fill='{OB}'/>" + txt(42, 89, "1", "#1b2340", 13)
    g += f"<circle cx='78' cy='84' r='10' fill='{NB}'/>" + txt(78, 89, "2", "#1b2340", 13)
    g += txt(60, 112, "= 25", "#f2c14e", 15)
    return bg(g)


def svg12_parantez():
    return bg(txt(60, 42, "(2 + 1)² = 9", OB, 15) + txt(60, 68, "≠", "#f2c14e", 20) + txt(60, 96, "2 + 1² = 3", NB, 15))


def svg12_cizgi():
    g = f"<rect x='14' y='22' width='62' height='30' rx='8' fill='none' stroke='{OB}' stroke-width='2.5'/>" + txt(45, 43, "3 + 9", OB, 16)
    g += "<line x1='12' y1='62' x2='78' y2='62' stroke='#f5f6fa' stroke-width='4' stroke-linecap='round'/>"
    g += f"<rect x='14' y='72' width='62' height='30' rx='8' fill='none' stroke='{NB}' stroke-width='2.5'/>" + txt(45, 93, "2 · 3", NB, 16)
    g += txt(98, 68, "= 2", "#f2c14e", 17)
    return bg(g)


def svg12_kart():
    g = "<rect x='14' y='26' width='92' height='56' rx='10' fill='#f5f6fa'/><rect x='14' y='38' width='92' height='10' fill='#9aa3bf'/>"
    g += txt(60, 72, "920 TL", OB, 17)
    g += "<path d='M60 88 v10 M55 94 l5 5 5 -5' stroke='#f5f6fa' stroke-width='2.5' fill='none' stroke-linecap='round' stroke-linejoin='round'/>"
    g += txt(60, 115, f"{M}40 TL", NB, 15)
    return bg(g)


def u1k12():
    return {
        "id": "u1k12", "unite": "1. Tema: Sayılar ve Nicelikler", "baslik": "Çok Adımlı İşlemler", "sayfalar": "s. 108–116",
        "giris": "Bir işlemde toplama, çarpma, üs ve parantez bir arada olabilir. Hangisini önce yapacağız? Bu konuda bir sıra öğreneceğiz. Sıra herkesi aynı cevaba götürür!",
        "hazirlik": {
            "baslik": "Hazır mısın?",
            "giris": "Bu konuda öğrendiğin bütün işlemleri bir arada kullanacağız. Önce işaret kurallarını, payda eşitlemeyi ve üslü ifadeleri hatırlıyor musun bakalım. Not yok.",
            "maddeler": [
                {"ad": "İşaret kuralları", "sinif": "6–7. konu", "svg": svg6_isaret("ayni"),
                 "anlatim": "Toplamada: aynı işaret → topla, işareti koru; farklı işaret → büyükten küçüğü çıkar, büyüğün işaretini koy. Çarpma ve bölmede: aynı işaret artı, farklı işaret eksi.",
                 "akilda": "Topluyor muyum, çarpıyor muyum?",
                 "ornek": {"problem": f"({M}6) + ({M}4) ile ({M}6) · ({M}4) aynı mı?", "adimlar": [
                     {"metin": "Toplama: aynı işaret, topla, eksiyi koru.", "islem": f"({M}6) + ({M}4) = {M}10"},
                     {"metin": "Çarpma: aynı işaret, sonuç artı.", "islem": f"({M}6) · ({M}4) = +24"}]},
                 "sorular": [
                     G(f"({M}7) + (+3) kaçtır?", "-4", "İşaretler farklı: büyükten küçüğü çıkar. Büyük olan hangisinin işareti?",
                       f"7 − 3 = 4. 7 daha büyük ve eksi: {M}4."),
                     S(f"({M}5) · ({M}2) kaçtır?", [f"{M}10", "+10", f"{M}7"], 1, "Çarpmada aynı işaret ne olur?",
                       "5 · 2 = 10. İki eksi: aynı işaret → +10.")]},
                {"ad": "Payda eşitleyerek toplama", "sinif": "8. konu", "svg": svg8_esitle(),
                 "anlatim": "Paydalar farklıysa önce genişletip eşitle; sonra payları topla ya da çıkar, payda aynı kalır.",
                 "akilda": "Önce paydaları eşitle",
                 "ornek": {"problem": "[[1/2]] + [[1/3]] kaçtır?", "adimlar": [
                     {"metin": "Ortak payda 6: [[1/2]] = [[3/6]], [[1/3]] = [[2/6]].", "islem": "[[3/6]] + [[2/6]]"},
                     {"metin": "Payları topla, payda 6 kalır.", "islem": "= [[5/6]]"}]},
                 "sorular": [
                     G("[[1/2]] + [[1/4]] kaçtır?", "3/4", "[[1/2]]'yi paydası 4 olacak şekilde genişlet.", "[[1/2]] = [[2/4]]. [[2/4]] + [[1/4]] = [[3/4]].", kesir=True, denk=True),
                     G("[[2/3]] − [[1/6]] kaçtır?", "1/2", "[[2/3]]'ü paydası 6 olacak şekilde genişlet.", "[[2/3]] = [[4/6]]. [[4/6]] − [[1/6]] = [[3/6]] = [[1/2]].", kesir=True, denk=True)]},
                {"ad": "Üslü ifade ve eksi", "sinif": "10. konu", "svg": svg10_parantez(),
                 "anlatim": f"Üs, tabanın kaç kere çarpıldığıdır: 2[[u:3]] = 2 · 2 · 2 = 8. Parantez varsa eksi de çarpılır: ({M}3)[[u:2]] = +9. Parantez yoksa eksi dışarıda kalır: {M}3[[u:2]] = {M}9.",
                 "akilda": "Parantez varsa eksi de çarpılır",
                 "ornek": {"problem": f"({M}2)[[u:2]] kaçtır?", "adimlar": [
                     {"metin": f"İki tane ({M}2)'yi çarp.", "islem": f"({M}2) · ({M}2)"},
                     {"metin": "Aynı işaret → artı.", "islem": "= +4"}]},
                 "sorular": [
                     S(f"({M}2)[[u:3]] kaçtır?", [f"{M}6", f"{M}8", "+8"], 1, f"Üç tane ({M}2)'yi çarp. Kaç tane eksi var: tek mi, çift mi?",
                       f"({M}2) · ({M}2) · ({M}2) = {M}8. Tek üs → eksi."),
                     S(f"{M}3[[u:2]] kaçtır?", [f"{M}9", "+9", f"{M}6"], 0, "Parantez var mı? Yoksa üs yalnızca 3'e ait.",
                       f"Parantez yok: 3[[u:2]] = 9, başına eksi: {M}9.")]}
            ]},
        "kavramlar": [
            {"ad": "Çok Adımlı İşlem", "renk": "#1f9e8f", "svg": svg12_valiz(),
             "aciklama": "İki ya da daha fazla işlem içeren ifadelere çok adımlı işlem denir. Bu işlemler belli bir sırayla yapılır. (s. 109)",
             "ek": "Gerçek yaşamdaki problemler çoğu zaman tek işlemle çözülmez. Kitaptaki valiz probleminde önce eşyaların kütlesi, sonra valizin toplam kütlesi, en son da kalan kütle bulunur. (s. 108)",
             "akilda": "Birden çok işlem, bir sıra",
             "cozum": {"baslik": "Valiz kaç kilo?",
                       "problem": "Melih Bey'in valizi boşken 4 kg. İçine her biri 3 kg olan 3 eşya koydu. Valizin sınırı 20 kg. Ek ücret ödememek için en fazla kaç kg daha eşya koyabilir?",
                       "adimlar": [
                           {"metin": "Ne veriliyor? Boş valiz 4 kg, 3 eşya (her biri 3 kg), sınır 20 kg. Ne isteniyor? Daha kaç kg konabilir?"},
                           {"metin": "1. adım: Eşyaların kütlesi. 3 eşya, her biri 3 kg.", "islem": "3 · 3 = 9"},
                           {"metin": "2. adım: Valizin şimdiki kütlesi. Boş valiz + eşyalar.", "islem": "4 + 9 = 13"},
                           {"metin": "3. adım: Sınıra kaç kg kaldı?", "islem": "20 − 13 = 7"}],
                       "sonuc": "7 kg daha koyabilir. Tek işlem olarak: 20 − (4 + 3 · 3) = 7. Kitaptaki valizde sayılar kesirli ama yol aynı. (s. 108)"},
             "soru": S("Hangisi çok adımlı bir işlemdir?", ["8 + 5", "8 + 5 · 2", "8 · 5"], 1,
                       "Kaç tane işlem işareti var? İki ya da daha fazla olanı ara.",
                       "8 + 5 · 2 içinde iki işlem var: toplama ve çarpma. Diğerlerinde tek işlem var. (s. 109)")},
            {"ad": "İşlem Sırası", "renk": "#7b4fc9", "svg": svg12_merdiven(),
             "aciklama": "Çok adımlı işlemlerde sıra şöyledir: 1) üslü ifadeler, 2) parantez içindeki işlemler, 3) çarpma ya da bölme, 4) toplama ya da çıkarma. (s. 109)",
             "ek": f"Merdiveni yukarıdan aşağı in: önce üs, en son toplama ve çıkarma. ({M}3) gibi bir parantez yalnızca sayının işaretini gösterir; içinde işlem yoksa atlanır.",
             "akilda": "Üs, parantez, çarp-böl, topla-çıkar",
             "cozum": {"baslik": "Kitaptaki işlem",
                       "problem": f"12 − ({M}3) · (+4) işlemini yapalım.",
                       "adimlar": [
                           {"metin": f"Üs var mı? Yok. Parantezlerin içinde işlem var mı? Yok; ({M}3) ve (+4) yalnızca işareti gösteriyor."},
                           {"metin": "Çarpma, çıkarmadan önce yapılır. Farklı işaret → eksi.", "islem": f"({M}3) · (+4) = {M}12"},
                           {"metin": "Şimdi çıkarma: çıkarmayı tersiyle toplamaya çevir.", "islem": f"12 − ({M}12) = 12 + 12"},
                           {"metin": "Topla.", "islem": "= 24"}],
                       "sonuc": f"12 − ({M}3) · (+4) = 24. Önce çıkarsaydık 12 − ({M}3) = 15, 15 · 4 = 60 gibi yanlış bir sonuç bulurduk. (s. 110)"},
             "sende": {"baslik": "Sıra sende",
                       "problem": f"5 + 2 · ({M}4) işlemini yap.",
                       "adimlar": [
                           {"metin": "Merdivene bak: üs yok, parantez içinde işlem yok.",
                            "soru": S("Önce hangi işlem yapılır?", ["5 + 2", f"2 · ({M}4)", "Fark etmez"], 1,
                                      "Merdivende çarpma mı önce geliyor, toplama mı?", f"Çarpma toplamadan önce: 2 · ({M}4)."),
                            "islem": f"2 · ({M}4) = {M}8"},
                           {"metin": "Şimdi toplama.",
                            "soru": G(f"5 + ({M}8) kaçtır?", "-3", "İşaretler farklı: büyükten küçüğü çıkar, büyüğün işaretini koy.", f"8 − 5 = 3, büyük olan eksi: {M}3."),
                            "islem": f"5 + ({M}8) = {M}3"}],
                       "sonuc": f"Harika! 5 + 2 · ({M}4) = {M}3."},
             "soru": G("3 + 4 · 2 kaçtır?", "11", "Merdivene bak: çarpma mı önce, toplama mı?",
                       "Önce çarpma: 4 · 2 = 8. Sonra toplama: 3 + 8 = 11. Önce toplasaydık yanlışlıkla 14 bulurduk. (s. 109)")},
            {"ad": "Aynı Öncelikte Soldan Sağa", "renk": "#e8590c", "svg": svg12_soldan(),
             "aciklama": "Aynı önceliğe sahip işlemlerde öncelik soldaki işleme aittir. Çarpma ile bölme kardeştir; toplama ile çıkarma da kardeştir. (s. 109)",
             "ek": "Kardeşler yan yana gelince yazıyı okur gibi soldan sağa git. 20 ÷ 4 · 5: önce 20 ÷ 4 = 5, sonra 5 · 5 = 25. Önce çarpsaydık 20 ÷ 20 = 1 gibi yanlış bir sonuç bulurduk. 10 − 3 + 2 de aynı: 7 + 2 = 9.",
             "akilda": "Kardeşler: soldan sağa",
             "soru": S("12 ÷ 2 · 3 kaçtır?", ["2", "9", "18"], 2,
                       "Bölme ve çarpma kardeş. Hangisi solda?",
                       "Soldan sağa: 12 ÷ 2 = 6, sonra 6 · 3 = 18. (s. 109)")},
            {"ad": "Önce Parantez", "renk": "#1d6fa3", "svg": svg12_parantez(),
             "aciklama": "Parantezin içindeki işlemler, dışarıdaki çarpma, bölme, toplama ve çıkarmadan önce yapılır. Parantezin kuvveti alınıyorsa önce parantezin içi yapılır, sonra kuvvet alınır. (s. 109)",
             "ek": "Parantez “bunu önce yap” demektir. (2 + 1)[[u:2]] = 3[[u:2]] = 9 ama 2 + 1[[u:2]] = 2 + 1 = 3. Parantez sonucu değiştirir. (s. 109)",
             "akilda": "Önce parantezin içi",
             "cozum": {"baslik": "İki parantez",
                       "problem": f"[({M}2) + (+7)] ÷ [({M}10) + (+5)] işlemini yapalım.",
                       "adimlar": [
                           {"metin": "İki büyük parantezin içinde toplama var. Önce onları yap."},
                           {"metin": "Soldaki parantez: farklı işaret, 7 − 2, büyüğün işareti artı.", "islem": f"({M}2) + (+7) = +5"},
                           {"metin": "Sağdaki parantez: farklı işaret, 10 − 5, büyüğün işareti eksi.", "islem": f"({M}10) + (+5) = {M}5"},
                           {"metin": "Şimdi böl. Farklı işaret → eksi.", "islem": f"(+5) ÷ ({M}5) = {M}1"}],
                       "sonuc": f"Sonuç {M}1. (s. 110)"},
             "sende": {"baslik": "Sıra sende",
                       "problem": "(3 − 5)[[u:2]] + 1 işlemini yap.",
                       "adimlar": [
                           {"metin": "Parantezin kuvveti alınıyor: önce parantezin içi.",
                            "soru": G("3 − 5 kaçtır?", "-2", "3'ten 5 adım geri git. 0'ı geçiyor musun?", f"3 − 5 = {M}2."),
                            "islem": f"({M}2)[[u:2]] + 1"},
                           {"metin": "Şimdi üs.",
                            "soru": S(f"({M}2)[[u:2]] kaçtır?", [f"{M}4", "+4", f"{M}2"], 1, f"İki tane ({M}2)'yi çarp. Aynı işaret ne yapar?", f"({M}2) · ({M}2) = +4."),
                            "islem": "4 + 1"},
                           {"metin": "En son toplama.", "islem": "= 5"}],
                       "sonuc": "Harika! (3 − 5)[[u:2]] + 1 = 5."},
             "soru": S("(4 + 2) · 3 kaçtır?", ["10", "18", "24"], 1,
                       "Önce parantezin içi: 4 + 2. Sonra çarp.",
                       "Parantez önce: 4 + 2 = 6. Sonra 6 · 3 = 18. Parantez olmasaydı 4 + 2 · 3 = 10 olurdu. (s. 109)")},
            {"ad": "Kesir Çizgisi Ayırır", "renk": "#b7791f", "svg": svg12_cizgi(),
             "aciklama": "Bölme kesir çizgisiyle gösterildiğinde önce paydaki ve paydadaki işlemler yapılır, en son bölünür. (s. 111)",
             "ek": "Kesir çizgisi, üstü ve altı ayrı parantezlere almak gibidir. Çizginin üstünde 3 + 9, altında 2 · 3 varsa: üst 3 + 9 = 12, alt 2 · 3 = 6, en son 12 ÷ 6 = 2. (s. 111)",
             "akilda": "Önce üst, sonra alt, en son böl",
             "soru": S("Kesir çizgisinin üstünde 6 + 4, altında 7 − 2 yazıyor. Sonuç kaçtır?", ["10", "5", "2"], 2,
                       "Önce üstü bul, sonra altı. En son böl.",
                       "Üst: 6 + 4 = 10. Alt: 7 − 2 = 5. 10 ÷ 5 = 2. (s. 111)")},
            {"ad": "Problemi İşleme Çevir", "renk": "#c92a2a", "svg": svg12_kart(),
             "aciklama": "Sözel bir problemi çözerken önce “Ne veriliyor, ne isteniyor?” diye sor. Sonra hangi işlemin önce yapılacağına karar ver ve adım adım ilerle.",
             "ek": "Her adımın bir anlamı olsun: “Bu sayı neyi gösteriyor?” Adımları birleştirince tek bir çok adımlı işlem çıkar; sırayı parantezle gösteririz. (s. 108)",
             "akilda": "Ne veriliyor? Ne önce?",
             "cozum": {"baslik": "Yemekhane kartı",
                       "problem": f"Nuran Hanım'ın yemek kartında 920 TL vardı. Her öğle yemeği için 120 TL çekiliyor. Bakiye eksiye düşebiliyor. Bir süre sonra bakiye {M}40 TL oldu. Kaç gün yemek yedi?",
                       "adimlar": [
                           {"metin": f"Ne veriliyor? Başta 920 TL, sonda {M}40 TL, her gün 120 TL. Ne isteniyor? Gün sayısı."},
                           {"metin": f"Toplam ne kadar harcandı? 920'den {M}40'a inildi; yol 0'dan geçiyor: 920'den 0'a 920, 0'dan {M}40'a 40.", "islem": f"920 − ({M}40) = 920 + 40 = 960"},
                           {"metin": "Her gün 120 TL: 960'ın içinde kaç tane 120 var?", "islem": "960 ÷ 120 = 8"},
                           {"metin": "Tek işlem olarak yaz; parantez önce yapılacağını gösterir.", "islem": f"[920 − ({M}40)] ÷ 120 = 8"}],
                       "sonuc": "Nuran Hanım 8 gün yemek yedi. (s. 113)"},
             "sende": {"baslik": "Ulaşım kartı",
                       "problem": "Ela'nın ulaşım kartında 50 TL var. Her binişte 15 TL düşüyor. Ela 4 kez bindi, sonra karta 30 TL yükledi. Kartta kaç TL var?",
                       "adimlar": [
                           {"metin": "Ne veriliyor? 50 TL, 4 biniş (her biri 15 TL), 30 TL yükleme. İşlem: 50 − 4 · 15 + 30.",
                            "soru": S("Önce hangi işlem yapılır?", ["50 − 4", "4 · 15", "15 + 30"], 1,
                                      "Merdivene bak: çarpma mı önce, toplama-çıkarma mı?", "Önce çarpma: 4 binişte 4 · 15 TL düşer."),
                            "islem": "4 · 15 = 60"},
                           {"metin": "Şimdi 50 − 60 + 30. Çıkarma ile toplama kardeş: soldan sağa.",
                            "soru": G("50 − 60 + 30 kaçtır?", "20", f"Soldan başla: 50 − 60 kaç? 0'ın altına iniyor musun? Sonra 30 ekle.",
                                      f"50 − 60 = {M}10, sonra {M}10 + 30 = 20.", birim="TL"),
                            "islem": f"{M}10 + 30 = 20"}],
                       "sonuc": "Harika! Kartta 20 TL var."},
             "soru": S("Mert her biri 10 TL olan 3 kalem aldı ve 50 TL verdi. Para üstünü hangi işlem verir?", ["50 − 3 · 10", "(50 − 3) · 10", "50 − 3 + 10"], 0,
                       "Önce kalemlere ne kadar ödendiğini düşün, sonra 50'den çıkar. Hangi işlem önce çarpıyor?",
                       "Kalemler: 3 · 10 = 30 TL. Para üstü: 50 − 30 = 20 TL. 50 − 3 · 10 işleminde çarpma önce yapılır. (Kitaptaki para üstü problemine benzer, s. 109)")}
        ],
        "akildaKalsin": [
            "İki ya da daha fazla işlem varsa bir sıra izlenir.",
            "Sıra: üs → parantez → çarpma-bölme → toplama-çıkarma.",
            "Aynı öncelikteki kardeş işlemlerde soldan sağa git.",
            "Parantezin kuvveti alınıyorsa önce parantezin içi.",
            "Kesir çizgisinde önce üst, sonra alt, en son böl.",
            "Sözel problemde önce sor: Ne veriliyor? Ne isteniyor? Ne önce?"],
        "merakKutusu": [
            {"soru": "Neden bir işlem sırası var?", "cevap": "Herkes farklı sırayla yapsa aynı işlemden farklı sonuçlar çıkardı: 2 + 3 · 4 işleminde biri 14, biri 20 bulurdu. Sıra kuralı herkesi aynı cevaba götürür."},
            {"soru": "Çarpma her zaman bölmeden önce mi yapılır?", "cevap": "Hayır. Çarpma ile bölme aynı önceliktedir; hangisi soldaysa o önce yapılır. Toplama ile çıkarma için de aynısı geçerli. (s. 109)"},
            {"soru": f"({M}3) gibi bir parantez de önce mi yapılır?", "cevap": f"Bu parantezin içinde işlem yok; yalnızca sayının eksi olduğunu gösteriyor. Ama ({M}3)[[u:2]] gibi kuvveti varsa parantez önemlidir: eksi de çarpılır, +9 olur."},
            {"soru": "Parantezi başka yere koyarsam sonuç değişir mi?", "cevap": "Evet! 2 + 3 · 4 = 14 ama (2 + 3) · 4 = 20. Kitapta da bir eşitliğin doğru olması için parantezi doğru yere koyman isteniyor. (s. 109)"},
            {"soru": "Kesir çizgisi neden parantez gibi?", "cevap": "Çünkü kesir çizgisi bir bölmedir ve önce üstteki, sonra alttaki işlem biter. Pay ve paydayı ayrı parantezlere almış gibi düşünebilirsin. (s. 111)"}],
        "dusunVeYaz": [{"soru": "Can 6 + 4 · 2 işleminin sonucunu 20 buldu. Hatası ne? Doğru sonucu bul.",
                        "ornekCevap": "Can önce toplamış: 6 + 4 = 10, 10 · 2 = 20. Ama çarpma toplamadan önce yapılır: 4 · 2 = 8, 6 + 8 = 14.",
                        "anahtarlar": ["çarp", "önce", "14"]}],
        "sorular": [
            S("2 + 3 · 4 kaçtır?", ["20", "14", "24"], 1,
              "Çarpma mı önce, toplama mı?", "Önce çarpma: 3 · 4 = 12. Sonra 2 + 12 = 14. (s. 109)"),
            G("[(+9) + (+21)] ÷ 2 kaçtır?", "15",
              "Önce parantezin içi, sonra bölme.", "Parantez: 9 + 21 = 30. Sonra 30 ÷ 2 = 15. (s. 110)"),
            S(f"2[[u:3]] + ({M}3)[[u:2]] kaçtır?", ["17", f"{M}1", "12"], 0,
              f"Önce iki üslü ifadeyi bul. ({M}3)[[u:2]]'de parantez var: eksi de çarpılır.",
              f"2[[u:3]] = 8, ({M}3)[[u:2]] = +9. 8 + 9 = 17. (s. 110)"),
            N(f"({M}1) + ({M}15) ÷ ({M}3) − ({M}2) işleminin sonucuna sayı doğrusunda dokun.", 6, {"min": -2, "max": 8},
              "Önce bölme. Sonra soldan sağa toplama ve çıkarma.",
              f"Bölme: ({M}15) ÷ ({M}3) = +5. Sonra ({M}1) + 5 = 4. En son 4 − ({M}2) = 4 + 2 = 6. (s. 110)"),
            S("10 − 6 + 2 kaçtır?", ["2", "4", "6"], 2,
              "Çıkarma ile toplama kardeş. Hangisi solda?",
              "Soldan sağa: 10 − 6 = 4, sonra 4 + 2 = 6. Önce 6 + 2 yapsaydık 2 bulurduk. (s. 109)"),
            S("Kesir çizgisinin üstünde 3 · 8, altında 10 − 4 yazıyor. Sonuç kaçtır?", ["24", "6", "4"], 2,
              "Önce üstteki çarpma, sonra alttaki çıkarma. En son böl.",
              "Üst: 3 · 8 = 24. Alt: 10 − 4 = 6. 24 ÷ 6 = 4. (s. 111)"),
            G("Tuğba kilogramı 40 TL olan elmadan ve kilogramı 30 TL olan mandalinadan 2'şer kilogram aldı. 200 TL verdi. Kaç TL para üstü alır?", "60",
              "Önce 1 kilogramlık elma ve mandalinanın fiyatını topla, 2 ile çarp. Sonra 200'den çıkar.",
              "1 kg elma + 1 kg mandalina: 40 + 30 = 70 TL. 2'şer kg: 2 · 70 = 140 TL. Para üstü: 200 − 140 = 60 TL. İşlem: 200 − 2 · (40 + 30) = 60. (Kitaptaki para üstü problemine benzer, s. 109)",
              birim="TL"),
            N("Asansör 3. kattaydı. 2 kez 4'er kat aşağı indi, sonra 1 kat yukarı çıktı. Asansörün durduğu kata dokun.", -4,
              {"min": -6, "max": 4, "dikey": True, "birim": 24, "sifirEtiketi": "Zemin kat"},
              f"İşlem: 3 + 2 · ({M}4) + 1. Önce çarpma.",
              f"İniş: 2 · ({M}4) = {M}8. Sonra 3 + ({M}8) = {M}5, en son {M}5 + 1 = {M}4. Asansör {M}4. katta."),
            S("Hangisinin sonucu en büyüktür?", ["(2 + 3)[[u:2]]", "2 + 3[[u:2]]", "2[[u:2]] + 3"], 0,
              "Üçünü de hesapla. Parantezin kuvveti alınıyorsa önce parantezin içi.",
              "(2 + 3)[[u:2]] = 5[[u:2]] = 25. 2 + 3[[u:2]] = 2 + 9 = 11. 2[[u:2]] + 3 = 4 + 3 = 7. En büyük 25. (s. 109)"),
            G("Bir depoda 40 litre su var. Musluk depoya saatte 2 litre su dolduruyor, vana saatte 6 litre boşaltıyor. İkisi birlikte 5 saat açık kalırsa depoda kaç litre su kalır?", "20",
              "Önce 1 saatte depodaki değişimi bul: dolan artı, boşalan eksi. Sonra 5 ile çarp, 40 ile topla.",
              f"1 saatte: 2 + ({M}6) = {M}4 litre. 5 saatte: 5 · ({M}4) = {M}20 litre. Kalan: 40 + ({M}20) = 20 litre. İşlem: 40 + 5 · (2 − 6) = 20. (Kitaptaki su deposu problemine benzer, s. 109)",
              birim="litre"),
            S("Valiz boşken 5 kg. İçine her biri 2 kg olan 4 eşya konuyor. Valizin kütlesini hangi işlem verir?", ["(5 + 4) · 2", "5 + 4 · 2", "5 · 4 + 2"], 1,
              "Önce eşyaların kütlesi: 4 eşya, her biri 2 kg. Sonra boş valizle topla. Hangi işlemde çarpma önce yapılıyor?",
              "Eşyalar: 4 · 2 = 8 kg. Valiz: 5 + 8 = 13 kg. 5 + 4 · 2 işleminde çarpma önce yapılır, sonuç 13. (Kitaptaki valiz problemine benzer, s. 108)")]
    }


# =================================================================
# Ara Duraklar (konu tarama): kapsanan konuların özeti + konuları birleştiren yeni sorular.
# Motor ayrıca kapsanan konuların kendi sorularından "eskiSoru" kadarını (zorlanılan kavramlar önce) ekler.
def K(konu, kavram=None):
    return {"konu": konu, "kavram": kavram} if kavram else {"konu": konu}


def u1t1():
    return {
        "id": "u1t1", "tur": "tarama", "unite": "1. Tema: Sayılar ve Nicelikler",
        "baslik": "Ara Durak 1: Sayıların Yeri ve Uzaklığı", "sayfalar": "Konu 1–3 · s. 15–40",
        "giris": "Üç konu bitti! Şimdi durup neler öğrendiğimize bakalım. Önce kısa özetleri oku ve kartları çevir. Sonra 10 soruluk tarama testini çöz. Not yok; neyi iyi bildiğini ve neye tekrar bakman gerektiğini bulacağız.",
        "buyukResim": "Bu üç konu birbirine bağlı. Önce tam sayıları sayı doğrusuna yerleştirdik: eksiler solda, artılar sağda. Sonra iki tam sayının arasındaki kesirleri bulduk. En son da her sayının 0'a ne kadar uzak olduğunu ölçtük: mutlak değer.",
        "kapsar": ["u1k1", "u1k2", "u1k3"],
        "hatirla": [
            {"konu": "u1k1", "maddeler": [
                f"Altı, borç, gider, zarar → eksi ({M}). Üstü, alacak, gelir, kâr → artı (+).",
                "Sayı doğrusunda negatifler 0'ın solunda, pozitifler sağındadır. Sıfırın işareti yoktur.",
                "İki sayı arasındaki uzaklık için aralıkları say. 0'dan geçiyorsa iki parçaya böl, topla."]},
            {"konu": "u1k2", "maddeler": [
                "Kesir şeklinde yazılabilen sayılar rasyonel sayıdır. Payda asla 0 olamaz.",
                "[[-1 1/2]] sayısındaki eksi, sayının tamamına aittir: eksiyi kenara koy, çevir, geri ekle.",
                "Sayı doğrusunda bulmak için: işaret, ara, böl, ilerle."]},
            {"konu": "u1k3", "maddeler": [
                "Bir sayının 0'a uzaklığına mutlak değer denir.",
                f"|{M}4| = |+4| = 4: İşareti sil, sayı kalır. Mutlak değer hiç eksi olmaz.",
                f"Mutlak değeri 4 olan iki sayı vardır: 4 ve {M}4."]}],
        "eskiSoru": 4,
        "sorular": [
            S("Hava sıcaklığı sıfırın 5 derece altında. Bu sıcaklığın 0 °C'a uzaklığı kaç derecedir?", ["5 derece", f"{M}5 derece", "0 derece"], 0,
              "Önce sıcaklığı yaz: sıfırın altı eksidir. Sonra 0'a uzaklığını düşün. Uzaklık eksi olur mu?",
              f"Sıcaklık {M}5 °C. 0 °C'a uzaklığı |{M}5| = 5 derecedir.",
              kaynak=[K("u1k1", "Negatif Tam Sayılar"), K("u1k3", "Mutlak Değer")]),
            G("Bir dalgıç deniz seviyesinin 12 metre altında, bir martı 5 metre üstünde uçuyor. Aralarında kaç metre var?", "17",
              f"Dalgıç {M}12, martı +5. Yol 0'dan geçiyor: {M}12'den 0'a kaç metre? 0'dan +5'e kaç metre? İkisini topla.",
              f"{M}12 → 0: 12 m, 0 → +5: 5 m. 12 + 5 = 17 m.", birim="m",
              kaynak=[K("u1k1", "Kelimeden Sayıya"), K("u1k1", "İki Sayı Arasındaki Uzaklık")]),
            N("Mutlak değeri [[1/2]] olan negatif sayının yerine dokun.", -0.5, {"min": -2, "max": 1, "bolme": 2},
              f"0'a yarım birim uzaklıkta iki sayı var. Negatif olan 0'ın solunda; 0 ile {M}1'in tam ortasında.",
              f"|[[-1/2]]| = [[1/2]] ve [[-1/2]] negatiftir. 0 ile {M}1'in tam ortasındadır.",
              kaynak=[K("u1k3", "Mutlak Değeri Verilen Sayı"), K("u1k2", "Sayı Doğrusunda Gösterme")]),
            S("|[[-5/2]]| hangi sayıya eşittir?", ["[[-2 1/2]]", "[[1 1/2]]", "[[2 1/2]]"], 2,
              "İşareti sil: [[5/2]] kalır. Sonra 5'i 2'ye böl: bölüm tam kısım, kalan pay olur.",
              "|[[-5/2]]| = [[5/2]]. 5 ÷ 2 = 2, kalan 1: [[5/2]] = [[2 1/2]]. Mutlak değer eksi olmaz.",
              kaynak=[K("u1k3", "Eksi de Artı da Aynı"), K("u1k2", "Eksi Bütüne Aittir")]),
            S("Hangisi doğrudur?", [f"|{M}2| = {M}2", f"[[-6/3]] = {M}2", "[[6/0]] = 0"], 1,
              "Üçüne de tek tek bak: Mutlak değer eksi olur mu? Payda 0 olabilir mi? 6 ÷ 3 kaçtır?",
              f"[[-6/3]] = {M}2 doğrudur. |{M}2| = 2 olmalıydı. [[6/0]] ise tanımsızdır; payda 0 olamaz.",
              kaynak=[K("u1k2", "Payda Sıfır Olamaz"), K("u1k3", "Mutlak Değer Eksi Olmaz")]),
            G("Meryem'in aklındaki sayının mutlak değeri 3, Cansel'inkinin 2. Bu iki sayı arasındaki uzaklık en çok kaç birim olabilir?", "5",
              f"Meryem'in sayısı 3 ya da {M}3, Cansel'inki 2 ya da {M}2. En uzak olmaları için biri 0'ın sağında, biri solunda olmalı.",
              f"{M}3 ile +2 (ya da +3 ile {M}2) arası: 3 + 2 = 5 birim. Kitapta aynı soru 12 ve 8 ile soruluyor. (s. 38)", birim="birim",
              sayiDogrusu={"min": -4, "max": 4},
              kaynak=[K("u1k3", "Mutlak Değeri Verilen Sayı"), K("u1k1", "İki Sayı Arasındaki Uzaklık")])]
    }


def u1t2():
    return {
        "id": "u1t2", "tur": "tarama", "unite": "1. Tema: Sayılar ve Nicelikler",
        "baslik": "Ara Durak 2: Gösterim ve Sıralama", "sayfalar": "Konu 4–5 · s. 41–61",
        "giris": "İki konu daha bitti! Durup bakalım. Önce kısa özetleri oku ve kartları çevir. Sonra 10 soruluk tarama testini çöz. Not yok; neyi iyi bildiğini ve neye tekrar bakman gerektiğini bulacağız.",
        "buyukResim": f"Bir sayıyı kesir ya da ondalık olarak yazabiliyoruz: [[-1/4]] ile {M}0,25 aynı sayıdır. Karşılaştırırken bu çok işe yarar: iki sayıyı aynı gösterime çevir, sonra sayı doğrusunda yerlerine bak. Sağdaki büyüktür, eksiler ters sıralanır.",
        "kapsar": ["u1k4", "u1k5"],
        "hatirla": [
            {"konu": "u1k4", "maddeler": [
                "Kesir çizgisi bölme demektir: [[1/5]] = 1 ÷ 5 = 0,2. Paydayı 10, 100, 1000 yapabiliyorsan daha kolay.",
                "Bölme biterse sonlu (0,25), hiç bitmezse devirli (0,[[d:3]]) ondalık gösterim olur. Paydada yalnız 2 ve 5 varsa sonludur.",
                "Ondalıktan kesre: virgülden sonraki basamak kadar sıfır, sonra sadeleştir."]},
            {"konu": "u1k5", "maddeler": [
                "Sayı doğrusunda sağdaki büyüktür; dikey sayı doğrusunda yukarıdaki büyüktür.",
                f"Negatif < 0 < pozitif. İki negatiften 0'a daha uzak olan küçüktür: {M}3 < {M}1.",
                "Önce kısa yol ara; yoksa paydaları ya da payları eşitle, ya da ikisini de ondalığa çevir."]}],
        "eskiSoru": 4,
        "sorular": [
            S("Hangisi [[-1/2]] ile 0 arasındadır?", ["[[-2/5]]", f"{M}0,6", f"{M}0,[[d:5]]"], 0,
              f"Hepsini ondalığa çevir. [[-1/2]] = {M}0,5. Hangisi {M}0,5'ten 0'a daha yakın?",
              f"[[-2/5]] = [[-4/10]] = {M}0,4. {M}0,5 < {M}0,4 < 0. {M}0,6 ve {M}0,555… ise {M}0,5'ten küçüktür; 0'a daha uzaktır.",
              kaynak=[K("u1k5", "Kısa Yollar"), K("u1k4", "Paydayı 10, 100, 1000 Yap")]),
            G(f"Üç şehirde sıcaklıklar ölçülüyor: {M}1,5 °C, [[-7/4]] °C ve {M}1,2 °C. En soğuk şehrin sıcaklığını ondalık gösterimle yaz.", "-1,75",
              "[[-7/4]]'ü ondalığa çevir: paydayı 100 yap. Sonra üç sayıdan 0'a en uzak olanı bul.",
              f"[[-7/4]] = [[-175/100]] = {M}1,75. {M}1,75 < {M}1,5 < {M}1,2. En soğuk {M}1,75 °C.",
              birim="°C", denk=True,
              kaynak=[K("u1k4", "Paydayı 10, 100, 1000 Yap"), K("u1k5", "Negatiflerde Uzak Olan Küçük")]),
            N(f"{M}1 ile {M}0,5 arasında, paydası 4 olan sayının yerine dokun.", -0.75, {"min": -2, "max": 0, "bolme": 4},
              f"{M}1 ile 0 arası 4 parçaya bölünmüş; her çizgi [[1/4]]. {M}0,5 = [[-2/4]]. Onunla {M}1 arasında hangi çizgi var?",
              f"[[-3/4]] = {M}0,75. {M}1 < {M}0,75 < {M}0,5.",
              kaynak=[K("u1k5", "Arada Hep Bir Sayı Var"), K("u1k4", "Ondalıktan Kesre")]),
            S("Hangisinin ondalık gösterimi hem devirlidir hem de 0'dan küçüktür?", ["[[-3/8]]", "[[1/6]]", "[[-1/3]]"], 2,
              "İki şey ara: işaret eksi mi? Paydada 2 ve 5'ten başka çarpan var mı?",
              f"[[-1/3]] = {M}0,[[d:3]]: negatif ve devirli. [[-3/8]] sonludur ({M}0,375; 8 = 2 × 2 × 2). [[1/6]] devirlidir ama pozitiftir.",
              kaynak=[K("u1k4", "Sonlu mu, Devirli mi?"), K("u1k5", "Negatif, Sıfır, Pozitif")]),
            G(f"İki dalgıç deniz seviyesinin altında. A dalgıcı {M}2,35 m'de, B dalgıcı [[-12/5]] m'de. Daha derindeki dalgıcın konumunu ondalık gösterimle yaz.", "-2,4",
              "[[-12/5]]'i ondalığa çevir. Daha derin olan, deniz seviyesine (0) daha uzak olandır.",
              f"[[-12/5]] = [[-24/10]] = {M}2,4. {M}2,4 < {M}2,35, yani B daha derinde: {M}2,4 m.",
              birim="m", denk=True, sayiDogrusu={"min": -3, "max": 0, "dikey": True, "sifirEtiketi": "Deniz seviyesi"},
              kaynak=[K("u1k4", "Kesir Çizgisi Bölmedir"), K("u1k5", "Dikey Sayı Doğrusu")]),
            S(f"{M}0,[[d:3]] ☐ {M}0,3 — kutuya hangi işaret gelir?", [">", "<", "="], 1,
              f"{M}0,[[d:3]] = {M}0,333… Hangisi 0'a daha uzak? Eksilerde uzak olan küçüktür.",
              f"{M}0,333… sayısı {M}0,3'ten 0'a daha uzaktır, yani daha küçüktür: {M}0,[[d:3]] < {M}0,3.",
              kaynak=[K("u1k4", "Devirli Ondalık Gösterim"), K("u1k5", "Negatiflerde Uzak Olan Küçük")])]
    }


def u1t3():
    return {
        "id": "u1t3", "tur": "tarama", "unite": "1. Tema: Sayılar ve Nicelikler",
        "baslik": "Ara Durak 3: Tam Sayılarla İşlemler", "sayfalar": "Konu 6–7 · s. 62–81",
        "giris": "Dört işlemi tam sayılarla yapmayı öğrendin! Durup bakalım. Önce kısa özetleri oku ve kartları çevir. Sonra 10 soruluk tarama testini çöz. Not yok; neyi iyi bildiğini ve neye tekrar bakman gerektiğini bulacağız.",
        "buyukResim": f"İki konuda da işaret önemli ama kurallar farklı. Toplamada sayı doğrusunda yürürüz; iki eksi toplanınca sonuç yine eksidir: ({M}6) + ({M}4) = {M}10. Çarpmada ise aynı işaret artı yapar: ({M}6) · ({M}4) = +24. Karıştırmamak için önce sor: Topluyor muyum, çarpıyor muyum?",
        "kapsar": ["u1k6", "u1k7"],
        "hatirla": [
            {"konu": "u1k6", "maddeler": [
                "Toplama bir yolculuktur: artı sağa, eksi sola.",
                "Aynı işaret: topla, işareti koru. Farklı işaret: büyükten küçüğü çıkar, büyüğün işaretini koy.",
                f"Çıkarma, tersiyle toplamadır: 4 {M} ({M}5) = 4 + (+5)."]},
            {"konu": "u1k7", "maddeler": [
                f"Çarpma tekrarlı toplamadır: 3 · ({M}2) = ({M}2) + ({M}2) + ({M}2).",
                "Aynı işaret → artı; farklı işaret → eksi. Bölmede de aynı kural.",
                "Çok çarpanda eksileri say: çiftse artı, tekse eksi. Bölen 0 olamaz."]}],
        "eskiSoru": 4,
        "oyunKavram": 8,
        "gruplar": [{"soru": "Bu kurallar hangi durum için?", "kutular": [
            {"etiket": "Aynı işaretli iki sayı", "uyeler": ["Aynı İşaret: Topla, İşareti Koru", "Aynı İşaret: Çarpım Artı"]},
            {"etiket": "Farklı işaretli iki sayı", "uyeler": ["Farklı İşaret: Çıkar, Büyüğün İşareti", "Farklı İşaret: Çarpım Eksi", "Ters İşaretliler Toplanınca 0"]},
            {"etiket": "Toplamaya çevir", "uyeler": ["Çıkarma = Tersiyle Toplama", "Çarpma = Tekrarlı Toplama"]}]}],
        "sorular": [
            G("Sabah hava sıcaklığı +5 °C. Sonra her saat 3 °C düşüyor. 4 saat sonra hava sıcaklığı kaç °C olur?", "-7",
              f"Düşüş eksidir: her saat {M}3. 4 saatlik değişim 4 · ({M}3). Sonra +5 ile topla.",
              f"Değişim: 4 · ({M}3) = {M}12. Yeni sıcaklık: (+5) + ({M}12) = {M}7 °C. İşaretler farklı: 12 − 5 = 7, büyüğün işareti eksi.",
              birim="°C", sayiDogrusu={"min": -8, "max": 6, "dikey": True, "birim": 22},
              kaynak=[K("u1k7", "Farklı İşaret: Çarpım Eksi"), K("u1k6", "Farklı İşaret: Çıkar, Büyüğün İşareti")]),
            S("Hangisinin sonucu artıdır (pozitiftir)?", [f"({M}6) + ({M}4)", f"({M}6) · ({M}4)", f"({M}6) {M} (+4)"], 1,
              "Önce işleme bak: toplama mı, çarpma mı? Toplamada iki eksi eksi kalır; çarpmada aynı işaret ne yapar?",
              f"({M}6) · ({M}4) = +24: aynı işaret, çarpım artı. ({M}6) + ({M}4) = {M}10: aynı işaret, topla, eksiyi koru. ({M}6) {M} (+4) = ({M}6) + ({M}4) = {M}10.",
              kaynak=[K("u1k6", "Aynı İşaret: Topla, İşareti Koru"), K("u1k7", "Aynı İşaret: Çarpım Artı")]),
            N("Asansör zemin katta. Her durakta 2 kat aşağı iniyor. 4 durak indikten sonra 3 kat yukarı çıktı. Asansörün katına dokun.", -5,
              {"min": -9, "max": 2, "dikey": True, "birim": 24, "sifirEtiketi": "Zemin kat"},
              f"Önce iniş: 4 durak, her biri {M}2 kat → 4 · ({M}2). Oradan 3 aralık yukarı çık.",
              f"İniş: 4 · ({M}2) = {M}8. Sonra ({M}8) + (+3) = {M}5. Asansör {M}5. katta.",
              kaynak=[K("u1k7", "Çarpma = Tekrarlı Toplama"), K("u1k6", "Toplama Bir Yolculuktur")]),
            S(f"Bir dondurucunun sıcaklığı 5 saatte +4 °C'tan {M}16 °C'a indi. Her saat aynı miktarda değiştiyse, saatte kaç derece değişti?",
              [f"{M}4 °C", "+4 °C", f"{M}20 °C"], 0,
              "Önce toplam değişimi bul: son sıcaklık − ilk sıcaklık. Sonra 5 saate eşit paylaştır.",
              f"Toplam değişim: ({M}16) {M} (+4) = ({M}16) + ({M}4) = {M}20 °C. Saatte: ({M}20) ÷ 5 = {M}4 °C. {M}20 toplam değişimdir, saatlik değil.",
              kaynak=[K("u1k6", "Çıkarma = Tersiyle Toplama"), K("u1k7", "Çarp mı, Böl mü?")]),
            G("Deniz'in ulaşım kartında 20 TL var. Kart eksiye düşebiliyor. Her binişte 8 TL düşüyor. Deniz 4 kez bindi. Kartın bakiyesi kaç TL oldu?", "-12",
              f"Gider eksidir: her biniş {M}8 TL. 4 binişte 4 · ({M}8). Sonra 20 TL ile topla.",
              f"Gider: 4 · ({M}8) = {M}32 TL. Bakiye: (+20) + ({M}32) = {M}12 TL. Kart 12 TL eksiye (borca) düştü.",
              birim="TL",
              kaynak=[K("u1k7", "Farklı İşaret: Çarpım Eksi"), K("u1k6", "Farklı İşaret: Çıkar, Büyüğün İşareti")]),
            S(f"Hangisinin sonucu {M}12'dir?", [f"({M}3) · ({M}4)", f"({M}8) {M} ({M}4)", f"|{M}3| · ({M}4)"], 2,
              f"Mutlak değer varsa önce onu bul: |{M}3| kaç? Sonra her işlemin işaretine bak.",
              f"|{M}3| · ({M}4) = 3 · ({M}4) = {M}12. ({M}3) · ({M}4) = +12 (aynı işaret). ({M}8) {M} ({M}4) = ({M}8) + (+4) = {M}4.",
              kaynak=[K("u1k6", "Önce Mutlak Değer"), K("u1k7", "Farklı İşaret: Çarpım Eksi")])]
    }


def u1t4():
    return {
        "id": "u1t4", "tur": "tarama", "unite": "1. Tema: Sayılar ve Nicelikler",
        "baslik": "Ara Durak 4: Rasyonel Sayılarla İşlemler", "sayfalar": "Konu 8–11 · s. 82–107",
        "giris": "Kesirlerle dört işlemi ve üslü ifadeleri öğrendin! Durup bakalım. Önce kısa özetleri oku ve kartları çevir. Sonra 10 soruluk tarama testini çöz. Not yok; neyi iyi bildiğini ve neye tekrar bakman gerektiğini bulacağız.",
        "buyukResim": "Dört konunun kuralı farklı; işe başlamadan önce sor: Hangi işlemi yapıyorum? Toplama ve çıkarmada önce paydalar eşitlenir. Çarpmada pay paya, payda paydaya çarpılır; payda eşitlemeye gerek yok. Bölmede ikinci kesir ters çevrilir, sonra çarpılır. Üslü ifade de tekrarlı çarpmadır. İşaret kuralı hep tam sayılardaki gibi.",
        "kapsar": ["u1k8", "u1k9", "u1k10", "u1k11"],
        "hatirla": [
            {"konu": "u1k8", "maddeler": [
                "Paydalar eşitse payları topla, payda aynı kalır.",
                "Paydalar farklıysa önce genişletip eşitle.",
                "Çıkarmayı çevir, topla: çıkan sayının işaretini ters yap."]},
            {"konu": "u1k9", "maddeler": [
                "Pay paya, payda paydaya: paydaları eşitlemeye gerek yok.",
                "Önce çapraz sadeleştir, sonra çarp. İşaret: aynı artı, farklı eksi.",
                "Bir sayının kesrini bulmak için çarp: 12'nin [[1/3]]'ü = 12 · [[1/3]] = 4."]},
            {"konu": "u1k10", "maddeler": [
                "Üs, tabanın kaç kere çarpıldığıdır: 5[[u:3]] = 5 · 5 · 5. 5 · 3 değil!",
                "Kesrin kuvvetinde pay da payda da kuvvetlenir.",
                f"Eksi tabanda çift üs artı, tek üs eksi. Parantez yoksa eksi dışarıda kalır: {M}2[[u:2]] = {M}4."]},
            {"konu": "u1k11", "maddeler": [
                "Bölme: içinde kaç tane sığar?",
                "Bölmeyi çarpmaya çevir: birinciyi koru, ikinciyi ters çevir.",
                "Ters çevirince işaret değişmez; 0'ın tersi yoktur."]}],
        "eskiSoru": 4,
        "oyunKavram": 8,
        "gruplar": [{"soru": "Bu kural hangi işlem için?", "kutular": [
            {"etiket": "Toplama ve çıkarma", "uyeler": ["Önce Paydaları Eşitle", "Çıkarma = Tersini Ekle"]},
            {"etiket": "Çarpma", "uyeler": ["Pay Paya, Payda Paydaya", "Önce Çapraz Sadeleştir"]},
            {"etiket": "Bölme", "uyeler": ["Böl = Tersiyle Çarp", "Ters Çevir"]},
            {"etiket": "Üslü ifade", "uyeler": ["Tekrarlı Çarpımı Kısalt", "Eksi Taban: Çift Artı, Tek Eksi"]}]}],
        "sorular": [
            G("Bir sürahide [[3/4]] litre su vardı. Ela bu suyun [[1/3]]'ünü içti. Sürahide kaç litre su kaldı?", "1/2",
              "Önce Ela'nın kaç litre içtiğini bul: [[3/4]]'ün [[1/3]]'ü, yani çarp. Sonra [[3/4]]'ten çıkar.",
              "İçilen: [[3/4]] · [[1/3]] = [[3/12]] = [[1/4]] litre. Kalan: [[3/4]] − [[1/4]] = [[2/4]] = [[1/2]] litre.",
              kesir=True, denk=True, birim="litre",
              kaynak=[K("u1k9", "Bir Sayının Kesrini Bulma"), K("u1k8", "Problemde Toplama ve Çıkarma")]),
            S("([[-2/3]])[[u:2]] · ([[-9/4]]) kaçtır?", ["+1", f"{M}1", "[[-4/9]]"], 1,
              "Önce üslü ifadeyi bul: eksi taban, çift üs. Sonra çarp; çarpmadan önce çapraz sadeleştir.",
              f"([[-2/3]])[[u:2]] = [[4/9]] (çift üs → artı). [[4/9]] · [[-9/4]]: 4 ile 4, 9 ile 9 sadeleşir → {M}1. İşaretler farklı, sonuç eksi.",
              kaynak=[K("u1k10", "Eksi Taban: Çift Artı, Tek Eksi"), K("u1k9", "Önce Çapraz Sadeleştir")]),
            N("[[3/4]] ÷ ([[-3/2]]) işleminin sonucunun yerine dokun.", -0.5, {"min": -2, "max": 1, "bolme": 2},
              "Bölmeyi çarpmaya çevir: [[3/4]]'ü koru, [[-3/2]]'yi ters çevir. İşaretler farklı → sonuç eksi.",
              f"[[3/4]] ÷ ([[-3/2]]) = [[3/4]] · ([[-2/3]]) = [[-6/12]] = [[-1/2]]. 0 ile {M}1'in tam ortası.",
              kaynak=[K("u1k11", "Böl = Tersiyle Çarp"), K("u1k9", "İşaret Tam Sayılardaki Gibi")]),
            G("Bir şişede [[3/4]] litre, diğerinde [[1 1/2]] litre limonata var. Hepsini [[1/4]] litrelik bardaklara dolduracağız. Kaç bardak dolar?", "9",
              "Önce iki şişedeki limonatayı topla (paydaları eşitle). Sonra toplamın içine [[1/4]] litre kaç kere sığar, bul.",
              "[[1 1/2]] = [[3/2]] = [[6/4]]. Toplam: [[3/4]] + [[6/4]] = [[9/4]] litre. [[9/4]] ÷ [[1/4]] = [[9/4]] · 4 = 9 bardak.",
              birim="bardak",
              kaynak=[K("u1k8", "Önce Paydaları Eşitle"), K("u1k11", "Kaç Tane Sığar?")]),
            S("Hangisi doğrudur?", ["[[1/2]] + [[1/3]] = [[2/5]]", "([[-1/2]])[[u:3]] = [[1/8]]", "[[2/3]] · [[3/4]] = [[1/2]]"], 2,
              "Üçünü tek tek kontrol et: Toplamada paydalar eşitlendi mi? Eksi taban tek üste ne olur? Çarpmada sadeleştir.",
              f"[[2/3]] · [[3/4]] = [[6/12]] = [[1/2]] doğru. [[1/2]] + [[1/3]] = [[3/6]] + [[2/6]] = [[5/6]] olmalıydı; paylar ve paydalar ayrı ayrı toplanmaz. ([[-1/2]])[[u:3]] = [[-1/8]]: tek üs, sonuç eksi.",
              kaynak=[K("u1k8", "Önce Paydaları Eşitle"), K("u1k10", "Eksi Taban: Çift Artı, Tek Eksi")]),
            G("Bir dalgıç deniz seviyesinin [[1 1/2]] metre altında. Sonra bulunduğu derinliğin yarısı kadar daha aşağı iniyor. Dalgıç şimdi kaç metrede? Bileşik kesir olarak yaz.", "-9/4",
              f"Başlangıç: {M}[[1 1/2]] = [[-3/2]]. İnilen yol: [[3/2]]'nin yarısı (çarp). Aşağı eksidir; iki eksiyi topla.",
              f"İnilen: [[3/2]] · [[1/2]] = [[3/4]] m. Yeni konum: [[-3/2]] + ([[-3/4]]) = [[-6/4]] + ([[-3/4]]) = [[-9/4]] m, yani [[-2 1/4]] m.",
              kesir=True, denk=True, kabul=["9/-4"], birim="m",
              sayiDogrusu={"min": -3, "max": 0, "dikey": True, "sifirEtiketi": "Deniz seviyesi"},
              kaynak=[K("u1k9", "Bir Sayının Kesrini Bulma"), K("u1k8", "Tam Sayılı Kesirler")])]
    }


def u1t5():
    return {
        "id": "u1t5", "tur": "tarama", "unite": "1. Tema: Sayılar ve Nicelikler",
        "baslik": "Tema Sonu Taraması", "sayfalar": "Konu 1–12 · s. 15–116",
        "giris": "Birinci temanın sonuna geldin, tebrikler! Şimdi 12 konuyu birlikte gözden geçireceğiz. Önce kısa özetleri oku ve kartları çevir. Sonra tarama testini çöz. Not yok; neyi iyi bildiğini ve neye tekrar bakman gerektiğini bulacağız.",
        "buyukResim": "Bu temada sayılarla bir yolculuk yaptık. Önce sayıları sayı doğrusuna yerleştirdik: tam sayılar, kesirler, ondalıklar. Sonra onları karşılaştırıp sıraladık. Ardından dört işlemi ve üslü ifadeleri öğrendik; işaret kuralı hep aynı kaldı. En sonunda bütün işlemleri bir sırayla birleştirdik: üs, parantez, çarpma-bölme, toplama-çıkarma.",
        "kapsar": ["u1k1", "u1k2", "u1k3", "u1k4", "u1k5", "u1k6", "u1k7", "u1k8", "u1k9", "u1k10", "u1k11", "u1k12"],
        "hatirla": [
            {"konu": "u1k1", "maddeler": [
                f"Altı, borç, gider, zarar → eksi ({M}). Üstü, alacak, gelir, kâr → artı (+).",
                "İki sayı arasındaki uzaklık: 0'dan geçiyorsa iki parçaya böl, topla."]},
            {"konu": "u1k2", "maddeler": [
                "Kesir şeklinde yazılabilen sayılar rasyonel sayıdır. Payda asla 0 olamaz.",
                "[[-1 1/2]] sayısındaki eksi, sayının tamamına aittir."]},
            {"konu": "u1k3", "maddeler": [
                "Mutlak değer, bir sayının 0'a uzaklığıdır; hiç eksi olmaz.",
                f"Mutlak değeri 4 olan iki sayı vardır: 4 ve {M}4."]},
            {"konu": "u1k4", "maddeler": [
                "Kesir çizgisi bölmedir: [[1/5]] = 1 ÷ 5 = 0,2.",
                "Paydada yalnız 2 ve 5 varsa ondalık gösterim sonludur; yoksa devirlidir."]},
            {"konu": "u1k5", "maddeler": [
                "Sayı doğrusunda sağdaki büyüktür.",
                f"İki negatiften 0'a uzak olan küçüktür: {M}3 < {M}1."]},
            {"konu": "u1k6", "maddeler": [
                "Aynı işaret: topla, işareti koru. Farklı işaret: büyükten küçüğü çıkar, büyüğün işareti.",
                f"Çıkarma, tersiyle toplamadır: 4 {M} ({M}5) = 4 + 5."]},
            {"konu": "u1k7", "maddeler": [
                "Çarpma ve bölmede aynı işaret artı, farklı işaret eksi.",
                "Çok çarpanda eksileri say: çiftse artı, tekse eksi."]},
            {"konu": "u1k8", "maddeler": [
                "Toplama ve çıkarmada önce paydaları eşitle.",
                "Tam sayılı kesri önce bileşik kesre çevir."]},
            {"konu": "u1k9", "maddeler": [
                "Pay paya, payda paydaya çarpılır; önce çapraz sadeleştir.",
                "Bir sayının kesrini bulmak için çarp: 12'nin [[1/3]]'ü = 4."]},
            {"konu": "u1k10", "maddeler": [
                "Üs, tabanın kaç kere çarpıldığıdır: 5[[u:3]] = 5 · 5 · 5.",
                f"Parantez yoksa eksi dışarıda kalır: ({M}3)[[u:2]] = 9 ama {M}3[[u:2]] = {M}9."]},
            {"konu": "u1k11", "maddeler": [
                "Bölmeyi çarpmaya çevir: birinciyi koru, ikinciyi ters çevir.",
                "Bölme sorusu: içinde kaç tane sığar?"]},
            {"konu": "u1k12", "maddeler": [
                "Sıra: üs → parantez → çarpma-bölme → toplama-çıkarma.",
                "Aynı öncelikteki işlemlerde soldan sağa git."]}],
        "eskiSoru": 6,
        "oyunKavram": 10,
        "gruplar": [{"soru": "Bu kural hangi işlem için?", "kutular": [
            {"etiket": "Toplama ve çıkarma", "uyeler": ["Aynı İşaret: Topla, İşareti Koru", "Önce Paydaları Eşitle"]},
            {"etiket": "Çarpma ve bölme", "uyeler": ["Aynı İşaret: Çarpım Artı", "Böl = Tersiyle Çarp"]},
            {"etiket": "Üslü ifade", "uyeler": ["Eksi Taban: Çift Artı, Tek Eksi", "Parantez Fark Yaratır"]},
            {"etiket": "İşlem sırası", "uyeler": ["Aynı Öncelikte Soldan Sağa", "Önce Parantez"]}]}],
        "sorular": [
            G(f"Selin'in yemek kartında 600 TL vardı. Her öğle yemeği için 90 TL çekiliyor; bakiye eksiye düşebiliyor. Bir süre sonra bakiye {M}30 TL oldu. Selin kaç gün yemek yedi?", "7",
              f"Önce toplam harcamayı bul: 600'den {M}30'a kaç TL inildi? Sonra her gün 90 TL: kaç tane 90 sığar?",
              f"Harcama: 600 {M} ({M}30) = 600 + 30 = 630 TL. Gün: 630 ÷ 90 = 7. Tek işlem: [600 {M} ({M}30)] ÷ 90 = 7. (Kitaptaki yemekhane kartı problemine benzer, s. 113)",
              birim="gün",
              kaynak=[K("u1k6", "Çıkarma = Tersiyle Toplama"), K("u1k7", "Çarp mı, Böl mü?"), K("u1k12", "Problemi İşleme Çevir")]),
            S("Bir fotoğrafçı makinesini 90 cm uzaklığa odakladı. Rüzgârda sallanan lale üç karede 86 cm, 95 cm ve 88 cm uzaklıkta kaldı. Odak uzaklığına en yakın kare en net çıkar. Hangisi?",
              ["1. kare (86 cm)", "2. kare (95 cm)", "3. kare (88 cm)"], 2,
              "Her karenin 90'dan farkını bul. Eksik ya da fazla olması önemli değil; uzaklık hep artıdır.",
              f"Farklar: 86 {M} 90 = {M}4, 95 {M} 90 = +5, 88 {M} 90 = {M}2. Uzaklıklar |{M}4| = 4, |+5| = 5, |{M}2| = 2. En yakın 3. kare. (s. 114)",
              kaynak=[K("u1k3", "Eksik ya da Fazla"), K("u1k3", "Mutlak Değer"), K("u1k1", "İki Sayı Arasındaki Uzaklık")]),
            G(f"Dört şehrin ocak ayı ortalama sıcaklıkları: 6 °C, {M}3 °C, 5 °C ve bilinmeyen bir sayı. Dört şehrin ortalaması 1 °C. Ortalama = toplam ÷ şehir sayısı. Bilinmeyen şehrin sıcaklığı kaç °C?", "-4",
              "Ortalamadan toplamı bul: toplam = 4 · 1. Sonra bilinen üç sıcaklığı topla ve aradaki farkı bul.",
              f"Toplam: 4 · 1 = 4. Bilinenler: 6 + ({M}3) + 5 = 8. Bilinmeyen: 4 {M} 8 = {M}4 °C. Kontrol: 8 + ({M}4) = 4, 4 ÷ 4 = 1. (Kitaptaki bölge sıcaklıkları sorusuna benzer, s. 115)",
              birim="°C", sayiDogrusu={"min": -5, "max": 7, "dikey": True, "birim": 22},
              kaynak=[K("u1k7", "Çarp mı, Böl mü?"), K("u1k6", "Farklı İşaret: Çıkar, Büyüğün İşareti"), K("u1k12", "Problemi İşleme Çevir")]),
            N("Bir ipin [[3/4]]'ü kesildi. Sonra kalan parçanın yarısı da kesildi. Elde kalan ip, başlangıçtaki ipin kaçta kaçıdır? Sayı doğrusunda dokun.", "1/8",
              {"min": 0, "max": 1, "bolme": 8},
              "Önce [[3/4]] kesilince kalanı bul: 1 − [[3/4]]. Sonra o parçanın yarısı gidiyor, yarısı kalıyor.",
              "İlk kesimden sonra kalan: 1 − [[3/4]] = [[1/4]]. Bunun yarısı kesilince [[1/4]] · [[1/2]] = [[1/8]] kalır. (Kitaptaki ip sorusuna benzer, s. 114)",
              kaynak=[K("u1k8", "Problemde Toplama ve Çıkarma"), K("u1k9", "Bir Sayının Kesrini Bulma"), K("u1k2", "Sayı Doğrusunda Gösterme")]),
            S("Hangisi doğrudur?",
              [f"{M}2[[u:4]] ile ({M}2)[[u:4]] aynı sayıdır.", f"Bir sayının {M}1 ile çarpımı, o sayının toplama işlemine göre tersidir.", "İki negatif sayının çarpımı negatiftir."], 1,
              f"Üçünü tek tek dene. Parantez yoksa eksi dışarıda mı kalır? 5 · ({M}1) kaç, 5'in tersi ne? ({M}2) · ({M}3) kaç?",
              f"5 · ({M}1) = {M}5 ve 5 + ({M}5) = 0: {M}1 ile çarpmak toplama işlemine göre tersini verir. {M}2[[u:4]] = {M}16 ama ({M}2)[[u:4]] = 16. İki negatifin çarpımı pozitiftir. (s. 112)",
              kaynak=[K("u1k10", "Parantez Fark Yaratır"), K("u1k6", "Ters İşaretliler Toplanınca 0"), K("u1k7", "Aynı İşaret: Çarpım Artı")]),
            N("([[1/2]] − 2) · [[2/3]] işleminin sonucuna sayı doğrusunda dokun.", -1, {"min": -2, "max": 1, "bolme": 2},
              "Önce parantez: 2'yi [[4/2]] yaz ve çıkar. Sonra [[2/3]] ile çarp; çapraz sadeleştir.",
              f"Parantez: [[1/2]] − [[4/2]] = [[-3/2]]. Çarpım: ([[-3/2]]) · [[2/3]]: 3 ile 3, 2 ile 2 sadeleşir → {M}1.",
              kaynak=[K("u1k12", "Önce Parantez"), K("u1k8", "Önce Paydaları Eşitle"), K("u1k9", "Önce Çapraz Sadeleştir")]),
            G(f"{M}0,25 + [[3/4]] · 2 işleminin sonucunu ondalık gösterimle yaz.", "1,25",
              "Önce çarpma: [[3/4]] · 2. Sonra kesri ondalığa çevir (paydayı 100 yap) ve topla.",
              f"Çarpma: [[3/4]] · 2 = [[6/4]] = [[3/2]] = 1,5. Toplama: {M}0,25 + 1,5 = 1,25.",
              denk=True,
              kaynak=[K("u1k12", "İşlem Sırası"), K("u1k4", "Paydayı 10, 100, 1000 Yap"), K("u1k6", "Farklı İşaret: Çıkar, Büyüğün İşareti")]),
            S("Hangisi en küçüktür?", [f"{M}3[[u:2]]", f"({M}2)[[u:3]]", "[[-1/2]] · 10"], 0,
              "Üçünün değerini bul. Sonra eksilerde 0'a en uzak olanı seç.",
              f"{M}3[[u:2]] = {M}9, ({M}2)[[u:3]] = {M}8, [[-1/2]] · 10 = {M}5. {M}9 < {M}8 < {M}5; en küçük {M}3[[u:2]].",
              kaynak=[K("u1k10", "Parantez Fark Yaratır"), K("u1k5", "Negatiflerde Uzak Olan Küçük")])]
    }


# =================================================================
# 2. TEMA: GEOMETRİK NİCELİKLER
# Çizim yardımcıları t2_cizim.py'de (eş küp yapıları, görünümler, prizma, açınım).
# Görünüm cevapları küp koordinatlarından hesaplanır (gor()); seçenekler birbirinden farklı mı diye assert edilir.
# Kitap dışı kararlar (Kemal'e bildirildi): ayrıt renkleri (en yeşil, boy mor, yükseklik pembe), geometri problem iskeleti
# (Kaplamak mı, doldurmak mı? / Ölçüler, birimler / Formül / Hesapla + birim), 6-12-8 sayıları (EBA 6. sınıf), açınımda karşı yüz stratejisi.
from t2_cizim import (EN, BOY, YUK, KUP, YUZ, ACIK, SOLUK, gsvg, kupler, yapi, yapi_boyut, gor, izgara, izgara_orta,
                      prizma, acinim, kare_ag, kare_ag_orta, _t as t2t)

T2 = "2. Tema: Geometrik Nicelikler"
TEAL = "#4fc3a1"


def secenekler(cizimler, w=330, h=150):
    """n seçenek paneli (1, 2, 3, 4 numaralı) yan yana; cizimler[i](cx, alt) → svg parçası."""
    n = len(cizimler); g = ""
    for k, f in enumerate(cizimler):
        cx = w / (2 * n) + k * w / n
        g += f(cx, h - 30)
        g += f"<circle cx='{cx:.1f}' cy='{h - 12}' r='10' fill='#f2c14e'/>" + t2t(cx, h - 7, str(k + 1), "#1b2340", 13)
        if k:
            g += f"<line x1='{k * w / n:.1f}' y1='8' x2='{k * w / n:.1f}' y2='{h - 28}' stroke='#3a4570' stroke-width='1.5' stroke-dasharray='4 4'/>"
    return g


def sec_svg(cizimler, w=330, h=150):
    return gsvg(w, h, secenekler(cizimler, w, h))


def ust_alt_svg(ust, cizimler, w=330, h_ust=130, h_alt=130, baslik=None):
    """Üstte bir çizim (yapı ya da görünüm), altında numaralı seçenekler."""
    g = ust(w / 2, h_ust - 22)
    if baslik:
        g += t2t(w / 2, 16, baslik, SOLUK, 12, 700)
    g += f"<line x1='10' y1='{h_ust - 2}' x2='{w - 10}' y2='{h_ust - 2}' stroke='#3a4570' stroke-width='1.5'/>"
    g += f"<g transform='translate(0 {h_ust})'>" + secenekler(cizimler, w, h_alt) + "</g>"
    return gsvg(w, h_ust + h_alt, g)


def gorunum_cizimi(kareler, s=22, renk=TEAL):
    return lambda cx, alt: izgara_orta(kareler, cx, alt, s, renk)


def yapi_cizimi(kup, s=24, yonler=False):
    return lambda cx, alt: yapi(kup, cx, alt, s, yonler)


def ayrik(*kumeler):
    assert len(set(kumeler)) == len(kumeler), "seçenekler birbirinden farklı olmalı"
    return kumeler


# ---------- Eş küp yapıları (i sağa, j arkaya, k yukarı) ----------
Y_L = [(0, 0, 0), (1, 0, 0), (2, 0, 0), (0, 0, 1)]                       # 3 yan yana + solda üstte 1
Y_KOSE = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 0, 1)]                    # L taban (arka sağda 1) + önde solda üstte 1
Y_SAKLI = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0), (0, 1, 1)]          # 2×2 taban + arka solda üstte 1 (altındaki küp saklı)
Y_MERDIVEN = [(0, 0, 0), (1, 0, 0), (1, 0, 1), (2, 0, 0), (2, 0, 1), (2, 0, 2)]
Y_ARTI = [(0, 0, 0), (1, 0, 0), (2, 0, 0), (1, 1, 0), (1, 0, 1)]
Y_IKI_KAT = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0), (0, 1, 1), (1, 1, 1)]
Y_SIRA3 = [(0, 0, 0), (0, 1, 0), (0, 2, 0)]                               # arka arkaya 3 küp
Y_IKILI = [(0, 0, 0), (1, 0, 0)]
Y_UCLU = [(0, 0, 0), (1, 0, 0), (2, 0, 0)]
Y_BLOK4 = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0)]

assert len(gor(Y_L, "on")) == 4 and len(gor(Y_L, "ust")) == 3 and len(gor(Y_L, "sag")) == 2
assert len(gor(Y_KOSE, "on")) == 3 and len(gor(Y_SAKLI, "on")) == 3
assert len(gor(Y_ARTI, "on")) == 4 and len(gor(Y_SIRA3, "on")) == 1


# ---------- Kavram ve hazırlık çizimleri (120 × 120) ----------
def svg2_yonler():
    g = kupler([(0, 0, 0)], 40, 82, 34)
    g += txt(57, 30, "Üst", "#f2c14e", 11) + txt(57, 112, "Ön", "#f5f6fa", 11) + txt(20, 70, "Sol", "#f5f6fa", 11)
    g += txt(102, 64, "Sağ", "#f5f6fa", 11) + txt(94, 22, "Arka", "#f2c14e", 11)
    g += "<path d='M57 34 v8 M57 98 v-6 M28 66 h8 M92 60 h-6' stroke='#f5f6fa' stroke-width='2' stroke-linecap='round'/>"
    return bg(g)


def svg2_kare_goster():
    g = kupler(Y_KOSE, 10, 92, 18)
    g += "<path d='M67 66 h10' stroke='#f2c14e' stroke-width='3' stroke-linecap='round'/><path d='M80 66l-6-4v8z' fill='#f2c14e'/>"
    g += izgara(gor(Y_KOSE, "on"), 84, 92, 14, TEAL)
    g += txt(60, 112, "önden 3 kare", "#f2c14e", 11)
    return bg(g)


def svg2_sakli():
    g = kupler([(0, 1, 0)], 30, 84, 30, renk=("#5a6280", "#3a4570", "#2b355c"))
    g += kupler([(0, 0, 0)], 30, 84, 30)
    g += "<path d='M74 44 l14 -14' stroke='#f2c14e' stroke-width='2.5' stroke-dasharray='4 3'/>" + txt(98, 26, "?", "#f2c14e", 20)
    g += txt(60, 108, "arkada saklı küp", "#f2c14e", 11)
    return bg(g)


def svg2_cizim():
    g = "".join(f"<line x1='{14 + i * 13}' y1='16' x2='{14 + i * 13}' y2='100' stroke='#2f3a63' stroke-width='1'/>" for i in range(8))
    g += "".join(f"<line x1='14' y1='{16 + i * 12}' x2='105' y2='{16 + i * 12}' stroke='#2f3a63' stroke-width='1'/>" for i in range(8))
    g += izgara(gor(Y_L, "on"), 27, 88, 13, TEAL)
    g += "<path d='M84 70 l14 -26 l4 4z' fill='#f2c14e'/><path d='M84 70 l3 -6 4 4z' fill='#f5f6fa'/>"
    g += txt(60, 114, "kareli kâğıda çiz", "#f2c14e", 11)
    return bg(g)


def svg2_simetri():
    on = gor(Y_MERDIVEN, "on"); arka = gor(Y_MERDIVEN, "arka")
    g = izgara(on, 10, 84, 14, TEAL) + izgara(arka, 68, 84, 14, "#ffa26b")
    g += "<line x1='60' y1='20' x2='60' y2='92' stroke='#f2c14e' stroke-width='2.5' stroke-dasharray='5 4'/>"
    g += txt(31, 104, "ön", TEAL, 12) + txt(89, 104, "arka", "#ffa26b", 12)
    return bg(g)


def svg2_gorunumden():
    g = izgara(frozenset({(0, 0), (0, 1), (1, 0)}), 10, 60, 14, TEAL) + txt(24, 74, "ön", TEAL, 10)
    g += izgara(frozenset({(0, 0), (1, 0)}), 10, 102, 14, "#ffa26b") + txt(24, 114, "üst", "#ffa26b", 10)
    g += "<path d='M50 64 h14' stroke='#f2c14e' stroke-width='3' stroke-linecap='round'/><path d='M66 64l-6-4v8z' fill='#f2c14e'/>"
    g += kupler([(0, 0, 0), (1, 0, 0), (0, 0, 1)], 70, 84, 16)
    return bg(g)


def svg2_h_simetri():
    sekil = frozenset({(0, 0), (0, 1), (0, 2), (1, 0)})
    ayna = frozenset({(1, 0), (1, 1), (1, 2), (0, 0)})
    g = izgara(sekil, 18, 88, 16, TEAL) + izgara(ayna, 70, 88, 16, "#ffa26b")
    g += "<line x1='60' y1='24' x2='60' y2='96' stroke='#f2c14e' stroke-width='2.5' stroke-dasharray='5 4'/>"
    return bg(g)


def svg2_h_kup():
    return bg(kupler([(0, 0, 0)], 32, 92, 44) + txt(60, 112, "6 kare yüz", "#f2c14e", 11))


def svg2_prizma():
    return bg(prizma(22, 92, 52, 40, 44, dolgu=True) + txt(60, 112, "kutu biçimi", "#f2c14e", 11))


def svg2_yak():
    g = prizma(20, 92, 54, 40, 46, vurgu="ayrit")
    g += "<circle cx='74' cy='46' r='5.5' fill='#ff8fab' stroke='#1b2340' stroke-width='1.5'/>"
    g += _poly2([(20, 92), (74, 92), (74, 46), (20, 46)], "#6fb3ff", 0.45)
    g += txt(34, 112, "yüz", "#6fb3ff", 10) + txt(66, 112, "ayrıt", "#f2c14e", 10) + txt(98, 112, "köşe", "#ff8fab", 10)
    return bg(g)


def _poly2(pts, renk, op):
    p = " ".join(f"{x},{y}" for x, y in pts)
    return f"<polygon points='{p}' fill='{renk}' fill-opacity='{op}'/>"


def svg2_es_yuz():
    g = acinim(46, 10, 28, 18, 24, boy=9)
    g += txt(60, 116, "aynı renk = eş", "#f2c14e", 10)
    return bg(g)


def svg2_acinim():
    g = prizma(8, 70, 30, 22, 26)
    g += "<path d='M50 52 h10' stroke='#f2c14e' stroke-width='3' stroke-linecap='round'/><path d='M62 52l-6-4v8z' fill='#f2c14e'/>"
    g += acinim(80, 14, 18, 12, 16, boy=8)
    return bg(g)


def svg2_farkli():
    a = [(1, 0, YUZ[0], ""), (0, 1, YUZ[2], ""), (1, 1, YUZ[1], ""), (2, 1, YUZ[2], ""), (1, 2, YUZ[0], ""), (1, 3, YUZ[1], "")]
    b = [(0, 0, YUZ[0], ""), (0, 1, YUZ[1], ""), (1, 1, YUZ[2], ""), (2, 1, YUZ[1], ""), (3, 1, YUZ[2], ""), (3, 2, YUZ[0], "")]
    return bg(kare_ag(a, 8, 16, 14) + kare_ag(b, 58, 30, 13) + txt(60, 112, "iki açınım, aynı kutu", "#f2c14e", 10))


def svg2_kapanir():
    a = [(1, 0, YUZ[0], ""), (0, 1, YUZ[2], ""), (1, 1, YUZ[1], ""), (2, 1, YUZ[2], ""), (1, 2, YUZ[0], ""), (1, 3, YUZ[1], "")]
    g = kare_ag(a, 14, 18, 14)
    g += "<path d='M74 54 l8 8 l16 -18' stroke='#5fd08f' stroke-width='5' fill='none' stroke-linecap='round' stroke-linejoin='round'/>"
    g += txt(60, 112, "6 yüz, eşler karşılıklı", "#f2c14e", 10)
    return bg(g)


def svg2_h_dikdortgen():
    g = "<rect x='14' y='34' width='58' height='36' fill='none' stroke='#6fb3ff' stroke-width='3'/>"
    g += "<rect x='82' y='40' width='26' height='26' fill='none' stroke='#ffa26b' stroke-width='3'/>"
    g += txt(43, 90, "dikdörtgen", "#6fb3ff", 10) + txt(95, 90, "kare", "#ffa26b", 10)
    return bg(g)


def svg2_h_kupacinim():
    a = [(1, 0, TEAL, ""), (0, 1, TEAL, ""), (1, 1, TEAL, ""), (2, 1, TEAL, ""), (1, 2, TEAL, ""), (1, 3, TEAL, "")]
    return bg(kare_ag(a, 39, 12, 21) + txt(98, 108, "6", "#f2c14e", 18))


def svg2_hediye():
    g = prizma(18, 96, 56, 40, 46)
    g += "<path d='M46 50 V96 M18 73 H74' stroke='#ff8fab' stroke-width='5'/><path d='M46 50 l-10 -10 M46 50 l10 -10' stroke='#ff8fab' stroke-width='4' stroke-linecap='round'/>"
    g += txt(60, 114, "bütün yüzleri kapla", "#f2c14e", 10)
    return bg(g)


def svg2_uc_cift():
    g = acinim(46, 8, 28, 16, 22, {"ust": "a·b", "on": "a·c", "alt": "a·b", "arka": "a·c", "sol": "b·c", "sag": "b·c"}, boy=8)
    return bg(g)


def svg2_formul():
    g = txt(60, 42, "2 · (a·b", "#ffd166", 15) + txt(60, 64, "+ a·c", "#6fb3ff", 15) + txt(60, 86, "+ b·c)", "#ff8fab", 15)
    g += txt(60, 110, "üçünü topla, 2 ile çarp", "#f2c14e", 10)
    return bg(g)


def svg2_kare_prizma():
    x, y, a, h = 40, 92, 30, 56
    g = prizma(x, y, a, a, h)
    g += _poly2([(x, y - h), (x + a, y - h), (x + a + a / 2, y - h - a / 2), (x + a / 2, y - h - a / 2)], "#ffd166", 0.75)
    g += txt(60, 112, "2 kare + 4 dikdörtgen", "#f2c14e", 9)
    return bg(g)


def svg2_kup():
    g = prizma(26, 92, 50, 50, 50)
    g += txt(60, 112, "6 · a²", "#f2c14e", 15)
    return bg(g)


def svg2_kapla():
    g = "<path d='M20 50 L60 30 L100 50 L60 70 Z' fill='none' stroke='#9aa3bf' stroke-width='2' stroke-dasharray='4 3'/>"
    g += "<path d='M20 50 V86 L60 106 L100 86 V50 L60 70 Z' fill='#33406e' stroke='#f5f6fa' stroke-width='2'/><path d='M60 70 V106' stroke='#f5f6fa' stroke-width='2'/>"
    g += txt(60, 22, "kapak yok", "#f2c14e", 11)
    return bg(g)


def svg2_h_alan():
    g = "".join(f"<rect x='{20 + i * 16}' y='{36 + j * 16}' width='16' height='16' fill='#2b355c' stroke='#6fb3ff' stroke-width='1.5'/>" for i in range(5) for j in range(3))
    g += txt(60, 104, "5 · 3 = 15", "#f2c14e", 14)
    return bg(g)


def svg2_h_kare_alan():
    g = "".join(f"<rect x='{36 + i * 16}' y='{24 + j * 16}' width='16' height='16' fill='#2b355c' stroke='#ffa26b' stroke-width='1.5'/>" for i in range(3) for j in range(3))
    g += txt(60, 104, "3 · 3 = 3²", "#f2c14e", 14)
    return bg(g)


def svg2_h_birim():
    g = "<line x1='16' y1='40' x2='60' y2='40' stroke='#6fb3ff' stroke-width='4' stroke-linecap='round'/>" + txt(38, 60, "cm", "#6fb3ff", 15)
    g += "<rect x='72' y='26' width='30' height='30' fill='#2b355c' stroke='#ffa26b' stroke-width='3'/>" + txt(87, 76, "cm²", "#ffa26b", 15)
    g += txt(60, 104, "uzunluk · alan", "#f2c14e", 11)
    return bg(g)


# ---------- Soru görselleri ----------
def svg_yapi(kup, s=30, w=330, h=160, yonler=True):
    _, yy = yapi_boyut(kup, s)
    alt = h - 22
    return gsvg(w, h, yapi(kup, w / 2, alt, s, yonler))


def svg_gorunum(kareler, etiket, s=26, w=330, h=130):
    return gsvg(w, h, izgara_orta(kareler, w / 2, h - 30, s, TEAL) + t2t(w / 2, h - 8, etiket, SOLUK, 12, 700))


def svg_iki_gorunum(a, ea, b, eb, s=24, w=330, h=130):
    g = izgara_orta(a, w / 4, h - 30, s, TEAL) + t2t(w / 4, h - 8, ea, SOLUK, 12, 700)
    g += izgara_orta(b, 3 * w / 4, h - 30, s, "#ffa26b") + t2t(3 * w / 4, h - 8, eb, SOLUK, 12, 700)
    return gsvg(w, h, g)


def svg_prizma_et(e, b, c, A=120, B=70, C=70, w=330, h=170):
    x = (w - A - B / 2) / 2
    return gsvg(w, h, prizma(x, h - 26, A, B, C, (e, b, c)))


def svg_acinim(A, B, C, yazi=None, w=330, h=None, boy=12):
    h = h or int(2 * B + 2 * C + 20)
    return gsvg(w, h, acinim(w / 2 - A / 2, 10, A, B, C, yazi, boy=boy))


def numarali_hac(s=30):
    """Haç açınım: 1-2-3-4 dikey, 5 ve 6 ikinin iki yanında. Karşılıklılar: 1–3, 2–4, 5–6."""
    return [(1, 0, TEAL, "1"), (1, 1, TEAL, "2"), (1, 2, TEAL, "3"), (1, 3, TEAL, "4"), (0, 1, "#ffa26b", "5"), (2, 1, "#ffa26b", "6")]


def numarali_141(s=30):
    """1-4-1 açınım: 1-2-3-4 yatay, 5 birin üstünde, 6 dördün altında. Karşılıklılar: 1–3, 2–4, 5–6."""
    return [(0, 1, TEAL, "1"), (1, 1, TEAL, "2"), (2, 1, TEAL, "3"), (3, 1, TEAL, "4"), (0, 0, "#ffa26b", "5"), (3, 2, "#ffa26b", "6")]


def svg_kare_ag(h_, s=30, w=330):
    C = max(c for c, *_ in h_) + 1; R = max(r for _, r, *_ in h_) + 1
    return gsvg(w, R * s + 16, kare_ag(h_, w / 2 - C * s / 2, 8, s, boy=15))


# Küp açınımları (seçenekler için)
AG_HAC = [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2), (1, 3)]
AG_141 = [(0, 1), (1, 1), (2, 1), (3, 1), (0, 0), (3, 2)]
AG_BLOK = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1)]        # 2 × 3 dikdörtgen: kapanmaz
AG_BES = [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]                  # 5 kare: bir yüz eksik
AG_SIRA5 = [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (2, 0)]        # 5 yan yana: üst üste biner


def ag_cizimi(hucre, s=16, renk=TEAL):
    return lambda cx, alt: kare_ag_orta([(c, r, renk, "") for c, r in hucre], cx, alt, s)


def prizma_ag(tur, s=1.0):
    """Dikdörtgenler prizması açınım seçenekleri: 'dogru' haç; 'bes' arka yüz eksik; 'cakisan' iki yan yüz aynı tarafta (sol yok, arka'nın sağında bir yan yüz daha)."""
    A, B, C = 26 * s, 14 * s, 20 * s

    def f(cx, alt):
        x, y = cx - A / 2, alt - (2 * B + 2 * C)
        yuz = {"ust": (x, y, A, B, YUZ[0]), "on": (x, y + B, A, C, YUZ[1]), "alt": (x, y + B + C, A, B, YUZ[0]),
               "arka": (x, y + 2 * B + C, A, C, YUZ[1]), "sol": (x - B, y + B, B, C, YUZ[2]), "sag": (x + A, y + B, B, C, YUZ[2])}
        if tur == "bes":
            del yuz["arka"]
        if tur == "cakisan":
            del yuz["sol"]; yuz["sag2"] = (x + A, y + 2 * B + C, B, C, YUZ[2])
        if tur == "cakisan_sol":
            del yuz["sag"]; yuz["sol2"] = (x - B, y + 2 * B + C, B, C, YUZ[2])
        return "".join(f"<rect x='{a:.1f}' y='{b:.1f}' width='{w:.1f}' height='{h:.1f}' fill='{r}' stroke='#1b2340' stroke-width='1.8'/>" for a, b, w, h, r in yuz.values())
    return f


# =================================================================
def u2k1():
    on_L, ust_L, sag_L = ayrik(gor(Y_L, "on"), gor(Y_L, "ust"), gor(Y_L, "sag"))
    on_M, arka_M = gor(Y_MERDIVEN, "on"), gor(Y_MERDIVEN, "arka")
    ters_M = frozenset((c, max(r for _, r in on_M) - r) for c, r in on_M)        # baş aşağı (yanlış seçenek)
    ayrik(arka_M, on_M, ters_M)
    sag_K, sol_K = gor(Y_KOSE, "sag"), gor(Y_KOSE, "sol")
    ters_K = frozenset((c, max(r for _, r in sag_K) - r) for c, r in sag_K)
    ayrik(sol_K, sag_K, ters_K)
    ust_K = gor(Y_KOSE, "ust")
    ayrik(ust_K, frozenset({(0, 0), (1, 0), (0, 1)}), frozenset({(0, 0), (1, 0)}))
    # "Hangi yapının önden görünümü bu?" seçenekleri
    Y_A = [(0, 0, 0), (1, 0, 0), (1, 0, 1)]
    Y_B = [(0, 0, 0), (1, 0, 0), (0, 0, 1)]
    Y_C = [(0, 0, 0), (1, 0, 0), (2, 0, 0)]
    hedef = gor(Y_A, "on")
    assert gor(Y_B, "on") != hedef and gor(Y_C, "on") != hedef
    # Görünümden en az küp: önden 1-2-1, üstten 3 yan yana → 4
    on_121 = frozenset({(0, 0), (1, 0), (1, 1), (2, 0)})
    ust_3 = frozenset({(0, 0), (1, 0), (2, 0)})
    assert gor(Y_ARTI[:3] + [(1, 0, 1)], "on") == on_121 and gor(Y_ARTI[:3] + [(1, 0, 1)], "ust") == ust_3
    eksik_L = [c for c in Y_L if c != (0, 0, 1)]
    assert gor(eksik_L, "ust") == ust_L and gor(eksik_L, "on") != on_L and gor(eksik_L, "sag") != sag_L

    return {
        "id": "u2k1", "unite": T2, "baslik": "Cisimlerin Farklı Yönlerden Görünümleri", "sayfalar": "s. 118–124",
        "giris": "Bir cisme önden, yandan ve üstten bakınca farklı şekiller görürüz. Bu konuda eş küplerden yapılmış yapılara altı yönden bakacağız. Gördüğümüz kareleri sayıp kareli kâğıda çizeceğiz.",
        "hazirlik": {
            "baslik": "Hazır mısın?",
            "giris": "Bu konuda simetriyi ve küpü kullanacağız. Önce ikisini hatırlıyor musun bakalım. Not yok.",
            "maddeler": [
                {"ad": "Doğruya göre simetri", "sinif": "Önceki yıllar", "svg": svg2_h_simetri(),
                 "anlatim": "Bir şekil bir doğru boyunca katlanınca iki parça tam üst üste geliyorsa, iki parça o doğruya göre simetriktir. Simetri ayna gibidir: sağdaki sola, soldaki sağa geçer.",
                 "akilda": "Ayna gibi ters çevir",
                 "ornek": {"problem": "Solda uzun kenarı olan bir L şeklinin dikey doğruya göre simetriği nasıl olur?", "adimlar": [
                     {"metin": "Dikey doğru aynadır. Soldaki kareler aynada sağa geçer.", "svg": gsvg(330, 110, izgara(frozenset({(0, 0), (0, 1), (0, 2), (1, 0)}), 110, 96, 24, TEAL)
                                                                                                        + "<line x1='165' y1='14' x2='165' y2='100' stroke='#f2c14e' stroke-width='3' stroke-dasharray='6 4'/>"
                                                                                                        + izgara(frozenset({(1, 0), (1, 1), (1, 2), (0, 0)}), 172, 96, 24, "#ffa26b"))},
                     {"metin": "Uzun kenar solda idi; simetrikte uzun kenar sağda olur.", "islem": "L ters döner"}]},
                 "sorular": [
                     S("Görseldeki şeklin dikey doğruya göre simetriği hangisi?",
                       ["1. çizim", "2. çizim", "3. çizim"], 1, "Aynada sağ ve sol yer değiştirir. Uzun kenar hangi tarafa geçer?",
                       "Soldaki uzun kenar aynada sağa geçer. Alt satır da ters döner: 2. çizim.",
                       svg=ust_alt_svg(gorunum_cizimi(frozenset({(0, 0), (0, 1), (0, 2), (1, 0)})),
                                       [gorunum_cizimi(frozenset({(0, 0), (0, 1), (0, 2), (1, 0)})), gorunum_cizimi(frozenset({(1, 0), (1, 1), (1, 2), (0, 0)})),
                                        gorunum_cizimi(frozenset({(0, 0), (0, 1), (0, 2), (1, 2)}))])),
                     S("Aynanın karşısında sağ elini kaldırıyorsun. Aynadaki görüntün hangi elini kaldırmış gibi görünür?", ["Sağ elini", "Sol elini", "İki elini"], 1,
                       "Simetride sağ ile sol yer değiştirir.", "Aynada sağ ile sol yer değiştirir; görüntü sol elini kaldırmış gibi görünür.")]},
                {"ad": "Küpün yüzleri", "sinif": "Önceki yıllar", "svg": svg2_h_kup(),
                 "anlatim": "Küpün 6 yüzü vardır. Yüzlerin hepsi birbirine eş karedir. Bu yüzden bir küpe hangi yönden bakarsan bak, bir kare görürsün.",
                 "akilda": "6 eş kare yüz",
                 "sorular": [
                     G("Bir küpün kaç yüzü vardır?", "6", "Bir zarı düşün: üstünde kaç farklı yüz var?", "Küpün 6 yüzü vardır: ön, arka, sağ, sol, üst, alt.",
                       yardim={"adimlar": ["Bir zarı düşün: 1'den 6'ya kadar sayılar ayrı yüzlerde.", "Ön, arka, sağ, sol, üst, alt yüzleri say."]}),
                     S("Küpün yüzleri hangi şekildir?", ["Üçgen", "Kare", "Daire"], 1, "Küpün kenarları eşit uzunluktadır.", "Küpün bütün yüzleri eş karedir.")]}
            ]},
        "kavramlar": [
            {"ad": "Altı Yön", "renk": "#1f9e8f", "svg": svg2_yonler(),
             "aciklama": "Bir yapıya altı yönden bakabiliriz: önden, arkadan, sağdan, soldan, üstten ve alttan. (s. 121–122)",
             "ek": "Yönler yapıya göre sabittir. Kitapta yönleri gösteren bir kâğıt kullanılır; böylece herkes “ön” deyince aynı tarafı anlar. (s. 121)",
             "akilda": "Ön-arka, sağ-sol, üst-alt",
             "soru": S("Bir yapıya kaç farklı yönden bakabiliriz?", ["4", "6", "8"], 1,
                       "Bilgi kartındaki yönleri tek tek say: ön, arka…", "Ön, arka, sağ, sol, üst ve alt: 6 yön. (s. 121–122)")},
            {"ad": "Görünüm Kare Gösterir", "renk": "#1d6fa3", "svg": svg2_kare_goster(),
             "aciklama": "Eş küplerden yapılmış bir yapıya bir yönden bakınca her küpün yalnızca bir yüzünü görürüz. Bu yüzler kare görünür. (s. 120–121)",
             "ek": "Görünüm, o yönden gördüğümüz karelerin çizimidir. Önden bakınca her sütunda üst üste kaç kare olduğunu sayarız.",
             "akilda": "Her sütunda kareleri say",
             "cozum": {"baslik": "Önden kaç kare?",
                       "problem": "Görseldeki yapıya önden bakınca kaç kare görürüz?",
                       "svg": svg_yapi(Y_L),
                       "adimlar": [
                           {"metin": "Yapının önünde dur. Soldan sağa kaç sütun var?", "islem": "3 sütun"},
                           {"metin": "Her sütunda üst üste kaç küp var? Soldaki 2, ortadaki 1, sağdaki 1.", "islem": "2 + 1 + 1"},
                           {"metin": "Topla. Gördüğün kareleri kareli kâğıda çiz.", "islem": "= 4 kare", "svg": svg_gorunum(on_L, "Önden görünüm")}],
                       "sonuc": "Önden görünüm 4 kareden oluşur. (s. 120)"},
             "soru": G("Görseldeki yapıya önden bakınca kaç kare görürsün?", str(len(gor(Y_KOSE, "on"))),
                       "Önden bak: kaç sütun var, her sütunda üst üste kaç küp var?", "Önde 2 sütun var: soldaki sütunda 2, sağdaki sütunda 1 kare. 2 + 1 = 3. Arkadaki küp öndekinin arkasında saklı. (s. 120)",
                       svg=svg_yapi(Y_KOSE), yardim={"adimlar": ["Yapının önünde dur. Soldan sağa kaç sütun var?", "Her sütunda üst üste kaç küp var? Arkadaki küp öndekinin arkasında.", "Sütunlardaki kareleri topla."]})},
            {"ad": "Saklanan Küpler", "renk": "#7b4fc9", "svg": svg2_sakli(),
             "aciklama": "Tek yönden bakmak yanıltabilir. Öndeki küp, arkasındaki küpü saklar. (s. 119)",
             "ek": "Kitaptaki yol fotoğrafında sağdaki ağaçlar art arda dizildiği için tek ağaç gibi görünür. Gerçek küplerde üstteki bir küp havada duramaz; altında onu taşıyan bir küp vardır. (s. 119–120)",
             "akilda": "Arkada ve altta küp olabilir",
             "cozum": {"baslik": "En az kaç küp?",
                       "problem": "Görseldeki yapı en az kaç küpten oluşur?",
                       "svg": svg_yapi(Y_SAKLI),
                       "adimlar": [
                           {"metin": "Görünen küpleri say: önde 2, arkada sağda 1, üstte 1.", "islem": "4 görünen küp"},
                           {"metin": "Üstteki küp havada duramaz. Altında, öndeki küpün arkasında saklı bir küp olmalı.", "islem": "+ 1 saklı küp"},
                           {"metin": "Topla.", "islem": "4 + 1 = 5"}],
                       "sonuc": "Yapı en az 5 küpten oluşur. “En az” diyoruz; çünkü görmediğimiz yerlerde başka küpler de olabilir. (s. 120)"},
             "soru": S("Görseldeki gibi arka arkaya dizilmiş 3 küpe önden bakınca kaç kare görürsün?", ["1", "3", "6"], 0,
                       "Öndeki küp, arkasındakileri saklar.", "Arka arkaya duran küpler önden bakınca tek kare gibi görünür. (s. 119)",
                       svg=svg_yapi(Y_SIRA3, s=28))},
            {"ad": "Görünümü Çizme", "renk": "#e8590c", "svg": svg2_cizim(),
             "aciklama": "Görünümü kareli kâğıda çizeriz: o yönden gördüğümüz her kareyi yerine koyarız. (s. 121)",
             "ek": "Üstten görünümde yapının ön tarafı aşağıda kalır. Sağdan bakınca yapının ön tarafı solunda kalır.",
             "akilda": "Gördüğün kareyi yerine çiz",
             "sende": {"baslik": "Sıra sende",
                       "problem": "Görseldeki yapının üstten görünümünü bulalım.",
                       "svg": svg_yapi(Y_KOSE),
                       "adimlar": [
                           {"metin": "Yukarıdan bak. Üst üste duran küpler tek kare görünür.",
                            "soru": G("Üstten bakınca kaç kare görürsün?", str(len(ust_K)), "Tabanda kaç küp var? Üstteki küp, altındaki küpün tam üstünde.",
                                      "Tabanda 3 küp var; üstteki küp öndeki soldaki küpün üstünde. Üstten 3 kare görünür.",
                                      yardim={"adimlar": ["Tabandaki küpleri say.", "Üstteki küp yeni bir kare eklemez; altındaki küpün üstünde."]}),
                            "islem": "3 kare"},
                           {"metin": "Kareler nasıl dizilmiş? Ön taraf aşağıda.",
                            "soru": S("Hangisi üstten görünüm?", ["1. çizim", "2. çizim", "3. çizim"], 0,
                                      "Önde yan yana 2 küp var, arkada sağda 1 küp. Ön taraf çizimde aşağıda.",
                                      "Ön sırada 2 kare, arka sırada sağda 1 kare: 1. çizim.",
                                      svg=sec_svg([gorunum_cizimi(ust_K), gorunum_cizimi(frozenset({(0, 0), (1, 0), (0, 1)})), gorunum_cizimi(frozenset({(0, 0), (1, 0)}))])),
                            "islem": "L biçiminde 3 kare", "svg": svg_gorunum(ust_K, "Üstten görünüm")}],
                       "sonuc": "Harika! Üstten görünüm L biçiminde 3 kare."},
             "soru": S("Görseldeki yapının sağdan görünümü hangisi?", ["1. çizim", "2. çizim", "3. çizim"], 2,
                       "Sağdan bakınca derinliği görürsün. Yapı tek sıra; en yüksek yeri kaç küp?",
                       "Yapı tek sıradır; sağdan bakınca tek sütun görünür. En yüksek yer 2 küp: üst üste 2 kare, 3. çizim. (s. 121)",
                       svg=ust_alt_svg(yapi_cizimi(Y_L, 22, True), [gorunum_cizimi(on_L), gorunum_cizimi(ust_L), gorunum_cizimi(sag_L)]))},
            {"ad": "Karşılıklı Görünümler Simetrik", "renk": "#c92a2a", "svg": svg2_simetri(),
             "aciklama": "Ön ile arka, sağ ile sol görünümler dikey bir doğruya göre simetriktir. Üst ile alt görünümler yatay bir doğruya göre simetriktir. (s. 122)",
             "ek": "Simetrik, ayna görüntüsü demek. Arkadan görünümü bulmak için önden görünümü dikey bir aynada çevir: sağdaki kareler sola geçer.",
             "akilda": "Arka = önün aynası",
             "cozum": {"baslik": "Arkadan görünüm",
                       "problem": "Önden görünümü görseldeki gibi olan yapının arkadan görünümünü bulalım.",
                       "svg": svg_gorunum(on_M, "Önden görünüm", s=22),
                       "adimlar": [
                           {"metin": "Önden bakınca merdiven sağa doğru yükseliyor."},
                           {"metin": "Yapının arkasına geç. Sağ ve sol yer değiştirir: dikey doğruya göre simetriğini al.", "islem": "ayna gibi çevir"},
                           {"metin": "Arkadan bakınca merdiven sola doğru yükselir.", "svg": svg_iki_gorunum(on_M, "Önden", arka_M, "Arkadan", s=20)}],
                       "sonuc": "Ön ile arka görünümler dikey bir doğruya göre simetriktir. (s. 122)"},
             "soru": S("Önden görünümü görseldeki gibi olan yapının arkadan görünümü hangisi?", ["1. çizim", "2. çizim", "3. çizim"], 0,
                       "Ön ile arka görünüm dikey bir doğruya göre simetrik: sağ ve sol yer değiştirir.",
                       "Arkadan bakınca sağ ve sol yer değiştirir. Merdiven sola doğru yükselir: 1. çizim. (s. 122)",
                       svg=ust_alt_svg(gorunum_cizimi(on_M, 18), [gorunum_cizimi(arka_M, 15), gorunum_cizimi(on_M, 15), gorunum_cizimi(ters_M, 15)], baslik="Önden görünüm"))},
            {"ad": "Görünümden Yapıya", "renk": "#b7791f", "svg": svg2_gorunumden(),
             "aciklama": "Görünümleri verilen bir yapıyı kurabiliriz. Önden görünüm sütunların yüksekliğini, üstten görünüm küplerin yere nasıl dizildiğini söyler. (s. 122–123)",
             "ek": "Kitapta görünümlerden yola çıkıp yapıyı en az kaç küple kurabileceğimizi buluyoruz. “En az” sorulunca yalnızca gereken küpleri sayarız. (s. 122)",
             "akilda": "Önden: yükseklik. Üstten: yer",
             "cozum": {"baslik": "Görünümlerden kur",
                       "problem": "Önden görünümü ve üstten görünümü verilen yapı en az kaç küptür?",
                       "svg": svg_iki_gorunum(frozenset({(0, 0), (0, 1), (1, 0)}), "Önden", frozenset({(0, 0), (1, 0)}), "Üstten"),
                       "adimlar": [
                           {"metin": "Üstten görünüm: yerde yan yana 2 kare. Küpler tek sırada."},
                           {"metin": "Önden görünüm: soldaki sütun 2 küp yüksekliğinde, sağdaki 1.", "islem": "2 + 1"},
                           {"metin": "Topla.", "islem": "= 3 küp", "svg": svg_yapi([(0, 0, 0), (1, 0, 0), (0, 0, 1)], s=28)}],
                       "sonuc": "Yapı en az 3 küpten oluşur. (s. 122)"},
             "soru": G("Önden görünümü yan yana 3 kare, üstten görünümü de yan yana 3 kare olan bir yapı en az kaç küptür?", "3",
                       "Üstten: yerde kaç küp var? Önden: sütunlar kaç küp yüksekliğinde?",
                       "Üstten 3 kare: yerde 3 küp. Önden her sütun 1 kare: üstte küp yok. 3 küp. (s. 122)",
                       yardim={"adimlar": ["Üstten görünüm: yerde kaç küp var?", "Önden görünüm: üst üste duran küp var mı?", "Yerdeki ve üstteki küpleri topla."]})}
        ],
        "akildaKalsin": [
            "Bir yapıya altı yönden bakılır: ön, arka, sağ, sol, üst, alt.",
            "Her yönden gördüğümüz küp yüzleri kare görünür.",
            "Öndeki küp arkasındakini saklar; tek yönden bakmak yanıltabilir.",
            "Üstten görünümde ön taraf aşağıda kalır.",
            "Ön-arka ve sağ-sol görünümler dikey, üst-alt görünümler yatay bir doğruya göre simetriktir.",
            "Önden görünüm yüksekliği, üstten görünüm yeri söyler."],
        "biliyorMusun": ["Sanal küplerle yapı kurulan bilgisayar programlarında yer çekimi yoktur. Bu yüzden küpler havada da durabilir; gerçek küplerde ise üstteki küp bir küpün üstünde durmalıdır. (s. 124)"],
        "merakKutusu": [
            {"soru": "Neden altı yön var da daha fazla yok?", "cevap": "Bir kutu gibi düşün: önü, arkası, iki yanı, üstü ve altı var. Yapının etrafında dönüp her yüze bakınca altı yön elde ederiz. (s. 121–122)"},
            {"soru": "Önden ve arkadan bakınca aynı sayıda kare mi görürüm?", "cevap": "Evet. Arkadan görünüm önden görünümün aynadaki görüntüsüdür; kareler yer değiştirir ama sayıları aynı kalır. (s. 122)"},
            {"soru": "Yapıdaki küp sayısını tek bir görünümden bulabilir miyim?", "cevap": "Çoğu zaman bulamazsın. Öndeki küp arkadakini saklar. Bu yüzden birkaç yönden bakar, “en az kaç küp” diye sorarız. (s. 119–120)"},
            {"soru": "Kitapta neden yönleri gösteren bir kâğıt kullanılıyor?", "cevap": "Yapıyı döndürünce “ön” başka tarafa geçebilir. Yön kâğıdı herkesin aynı tarafa ön demesini sağlar; anlaşmazlık olmaz. (s. 121)"}],
        "dusunVeYaz": [{"soru": "Bir yapıya yalnızca önden bakarak kaç küp olduğunu kesin söyleyebilir misin? Neden?",
                        "ornekCevap": "Hayır. Öndeki küpler arkadakileri saklar. Arkada ya da altta göremediğim küpler olabilir. Bu yüzden başka yönlerden de bakmalıyım.",
                        "anahtarlar": ["hayır", "sakla", "arka", "göreme", "yön"]}],
        "sorular": [
            G("Görseldeki yapıya önden bakınca kaç kare görürsün?", str(len(gor(Y_ARTI, "on"))),
              "Önden bak: soldan sağa kaç sütun var? Her sütunda üst üste kaç küp var?",
              "3 sütun var: soldaki 1, ortadaki 2, sağdaki 1 kare. 1 + 2 + 1 = 4. Arkadaki küp ortadaki küpün arkasında saklı. (s. 120)",
              svg=svg_yapi(Y_ARTI), kavram="Görünüm Kare Gösterir",
              yardim={"adimlar": ["Yapının önünde dur. Soldan sağa kaç sütun var?", "Her sütunda üst üste kaç küp var? Arkadaki küp öndekinin arkasında saklanıyor.", "Sütunlardaki kareleri topla."]}),
            S("Görseldeki yapının üstten görünümü hangisi?", ["1. çizim", "2. çizim", "3. çizim"], 1,
              "Yukarıdan bak: yerde kaç küp var? Üst üste duranlar tek kare görünür.",
              "Yerde yan yana 3 küp var; soldaki küpün üstündeki küp yeni kare eklemez. Üstten 3 kare yan yana: 2. çizim. (s. 121)",
              svg=ust_alt_svg(yapi_cizimi(Y_L, 22, True), [gorunum_cizimi(on_L), gorunum_cizimi(ust_L), gorunum_cizimi(sag_L)]), kavram="Görünümü Çizme"),
            G("Görseldeki yapı en az kaç küpten oluşur?", str(len(Y_IKI_KAT)),
              "Görünen küpleri say. Üstteki küplerin altında saklı küp olmalı mı?",
              "Önde 2, arkada 2 küp yerde duruyor; arkadakilerin üstünde 2 küp daha var. 4 + 2 = 6. (s. 120)",
              svg=svg_yapi(Y_IKI_KAT), kavram="Saklanan Küpler",
              yardim={"adimlar": ["Yerdeki küpleri say: önde kaç, arkada kaç?", "Üstteki küpleri say. Her biri bir küpün üstünde duruyor.", "Yerdekileri ve üsttekileri topla."]}),
            S("Önden görünümü görseldeki gibi olan yapının arkadan görünümü hangisi?", ["1. çizim", "2. çizim", "3. çizim"], 2,
              "Arkadan bakınca sağ ve sol yer değiştirir. Uzun sütun hangi tarafa geçer?",
              "Arka görünüm, önden görünümün dikey doğruya göre simetriğidir. Merdiven sola doğru yükselir: 3. çizim. (s. 122)",
              svg=ust_alt_svg(gorunum_cizimi(on_M, 18), [gorunum_cizimi(on_M, 15), gorunum_cizimi(ters_M, 15), gorunum_cizimi(arka_M, 15)], baslik="Önden görünüm"),
              kavram="Karşılıklı Görünümler Simetrik"),
            S("Sağdan görünümü görseldeki gibi olan yapının soldan görünümü hangisi?", ["1. çizim", "2. çizim", "3. çizim"], 0,
              "Sağ ile sol görünüm dikey bir doğruya göre simetriktir.",
              "Soldan görünüm, sağdan görünümün ayna görüntüsüdür: yüksek sütun öbür tarafa geçer: 1. çizim. (s. 122)",
              svg=ust_alt_svg(gorunum_cizimi(sag_K, 22), [gorunum_cizimi(sol_K, 18), gorunum_cizimi(sag_K, 18), gorunum_cizimi(ters_K, 18)], baslik="Sağdan görünüm"),
              kavram="Karşılıklı Görünümler Simetrik"),
            S("Hangisi doğrudur?",
              ["Üstten ve alttan görünümler dikey bir doğruya göre simetriktir.", "Önden ve arkadan görünümler dikey bir doğruya göre simetriktir.", "Sağdan ve soldan görünümler her zaman tamamen aynıdır."], 1,
              "Bilgi kartına bak: hangi çiftler dikey, hangi çift yatay doğruya göre simetrik?",
              "Ön-arka ve sağ-sol dikey, üst-alt yatay bir doğruya göre simetriktir. Sağ ve sol görünüm ayna görüntüsüdür; her zaman aynı değildir. (s. 122)",
              kavram="Karşılıklı Görünümler Simetrik"),
            G("Önden ve üstten görünümleri görseldeki gibi olan bir yapı en az kaç küptür?", "4",
              "Üstten: yerde kaç küp var? Önden: hangi sütun daha yüksek?",
              "Üstten 3 kare: yerde 3 küp. Önden ortadaki sütun 2 kare: ortadaki küpün üstünde 1 küp daha. 3 + 1 = 4. (s. 122)",
              svg=svg_iki_gorunum(on_121, "Önden", ust_3, "Üstten"), kavram="Görünümden Yapıya",
              yardim={"adimlar": ["Üstten görünüm: yerde kaç küp var?", "Önden görünüm: hangi sütunda üst üste 2 kare var?", "Yerdeki küplere üstteki küpü ekle."]}),
            S("Görseldeki yapıdan en üstteki küp çıkarılırsa hangi görünüm değişmez?", ["Önden görünüm", "Üstten görünüm", "Sağdan görünüm"], 1,
              "Üstteki küp kalkınca yukarıdan bakan biri yeni bir boşluk görür mü? Altında küp var mı?",
              "Üstteki küpün altında başka bir küp var. Yukarıdan yine 3 kare görünür; önden ve sağdan görünümde ise üstteki kare kaybolur. (s. 124)",
              svg=svg_yapi(Y_L), kavram="Görünüm Kare Gösterir"),
            S("Bir yapının ön tarafının tam karşısında hangi taraf vardır?", ["Arka", "Sağ", "Üst"], 0,
              "Altı yönü çiftler hâlinde düşün: ön-…, sağ-…, üst-…",
              "Yönler çiftler hâlindedir: ön-arka, sağ-sol, üst-alt. (s. 121–122)", kavram="Altı Yön"),
            S("Görseldeki önden görünüm hangi yapıya aittir?", ["1. yapı", "2. yapı", "3. yapı"], 0,
              "Her yapıya önden bak: hangi sütun 2 küp yüksekliğinde?",
              "Önden görünümde sağ sütun 2 kare yüksekliğinde. 1. yapıda sağdaki küpün üstünde bir küp var. (s. 123)",
              svg=ust_alt_svg(gorunum_cizimi(hedef, 22), [yapi_cizimi(Y_A, 20), yapi_cizimi(Y_B, 20), yapi_cizimi(Y_C, 20)], baslik="Önden görünüm"),
              kavram="Görünümden Yapıya")]
    }


# =================================================================
def u2k2():
    return {
        "id": "u2k2", "unite": T2, "baslik": "Prizma ve Açınımı", "sayfalar": "s. 125–128",
        "giris": "Ayakkabı kutusu, çikolata kutusu, ilaç kutusu… Hepsi aynı biçimde: dikdörtgenler prizması. Bu konuda kutuların yüzlerini, ayrıtlarını ve köşelerini tanıyacağız. Sonra bir kutuyu kesip düz açacağız.",
        "hazirlik": {
            "baslik": "Hazır mısın?",
            "giris": "Bu konuda dikdörtgen, kare ve küpün açınımını kullanacağız. Önce onları hatırlıyor musun bakalım. Not yok.",
            "maddeler": [
                {"ad": "Dikdörtgen ve kare", "sinif": "Önceki yıllar", "svg": svg2_h_dikdortgen(),
                 "anlatim": "Dikdörtgenin dört açısı da dik açıdır; karşılıklı kenarları eşittir. Karenin dört kenarı da eşittir. Kare, özel bir dikdörtgendir.",
                 "akilda": "Kare de bir dikdörtgendir",
                 "sorular": [
                     S("Hangisi doğrudur?", ["Her kare bir dikdörtgendir.", "Her dikdörtgen bir karedir.", "Karenin kenarları farklı uzunluktadır."], 0,
                       "Kare özel bir dikdörtgendir. Hangi şart kareyi özel yapar?", "Karenin dört açısı dik, karşılıklı kenarları eşit: o da bir dikdörtgendir. Ama her dikdörtgenin dört kenarı eşit değildir."),
                     S("Kenarları 3 cm ve 5 cm olan bir dikdörtgen için hangisi doğrudur?", ["Dört kenarı da 3 cm'dir.", "İki kenarı 3 cm, iki kenarı 5 cm'dir.", "Dört kenarı da 5 cm'dir."], 1,
                       "Dikdörtgenin karşılıklı kenarları eşittir.", "Karşılıklı kenarlar eşittir: iki kenar 3 cm, iki kenar 5 cm.")]},
                {"ad": "Küpün açınımı", "sinif": "Önceki yıllar", "svg": svg2_h_kupacinim(),
                 "anlatim": "Küp şeklindeki bir kutuyu bazı ayrıtlarından kesip düz açarsak 6 kareden oluşan bir şekil elde ederiz. Buna küpün açınımı denir. (s. 125)",
                 "akilda": "Küp açınımı: 6 kare",
                 "sorular": [
                     G("Küpün açınımı kaç kareden oluşur?", "6", "Küpün kaç yüzü var? Her yüz açınımda bir kare olur.", "Küpün 6 yüzü var; açınımı 6 kareden oluşur. (s. 125)",
                       yardim={"adimlar": ["Küpün yüzlerini say: ön, arka, sağ, sol, üst, alt.", "Her yüz açınımda bir kare olur."]}),
                     S("Görseldekilerden hangisi bir küpün açınımıdır?", ["1. çizim", "2. çizim", "3. çizim"], 0,
                       "Kare sayısını say: 6 olmalı. Sonra katlamayı hayal et: yüzler üst üste biniyor mu?",
                       "1. çizim haç biçiminde 6 kare: kapanınca küp olur. 2. çizimde 5 kare var. 3. çizim 2 sıra 3 kare: kapatınca yüzler üst üste biner.",
                       svg=sec_svg([ag_cizimi(AG_HAC), ag_cizimi(AG_BES), ag_cizimi(AG_BLOK)]))]}
            ]},
        "kavramlar": [
            {"ad": "Dikdörtgenler Prizması", "renk": "#1f9e8f", "svg": svg2_prizma(),
             "aciklama": "Ayakkabı kutusu gibi 6 yüzünün hepsi dikdörtgen olan cisme dikdörtgenler prizması denir. (s. 128)",
             "ek": "Kitapta parfüm kutusu ve çikolata kutusu dikdörtgenler prizmasına, ilaç kutusu da kare prizmaya örnek veriliyor. (s. 125–126)",
             "akilda": "Kutu biçimi: 6 dikdörtgen yüz",
             "soru": S("Hangisi dikdörtgenler prizmasına örnektir?", ["Çikolata kutusu", "Futbol topu", "Dondurma külahı"], 0,
                       "Kutu biçiminde olanı ara: bütün yüzleri dikdörtgen.", "Çikolata kutusunun 6 yüzü dikdörtgendir. Top ve külahın düz dikdörtgen yüzleri yoktur. (s. 126)")},
            {"ad": "Yüz, Ayrıt, Köşe", "renk": "#1d6fa3", "svg": svg2_yak(),
             "aciklama": "Prizmanın düz yüzeylerine yüz, iki yüzün birleştiği çizgiye ayrıt, ayrıtların buluştuğu noktaya köşe denir.",
             "ek": "Dikdörtgenler prizmasının 6 yüzü, 12 ayrıtı ve 8 köşesi vardır. Bir kutunun üzerinde sayarak kontrol edebilirsin.",
             "akilda": "6 yüz, 12 ayrıt, 8 köşe",
             "cozum": {"baslik": "Ayrıtları sayalım",
                       "problem": "Dikdörtgenler prizmasının kaç ayrıtı vardır?",
                       "svg": svg_prizma_et("", "", "", A=110, B=70, C=70),
                       "adimlar": [
                           {"metin": "Ön yüzün çevresindeki ayrıtları say.", "islem": "4"},
                           {"metin": "Arka yüzün çevresinde de 4 ayrıt var. Kesikli çizgiler arkada kalanları gösterir.", "islem": "4 + 4"},
                           {"metin": "Önü arkaya bağlayan çapraz ayrıtlar.", "islem": "4 + 4 + 4 = 12"}],
                       "sonuc": "Dikdörtgenler prizmasının 12 ayrıtı vardır."},
             "soru": G("Dikdörtgenler prizmasının kaç köşesi vardır?", "8",
                       "Ön yüzün köşelerini say, sonra arka yüzün köşelerini.", "Ön yüzde 4, arka yüzde 4 köşe: 4 + 4 = 8.",
                       yardim={"adimlar": ["Ön yüzün köşelerini say.", "Arka yüzde de aynı sayıda köşe var.", "İkisini topla."]})},
            {"ad": "Karşılıklı Yüzler Eştir", "renk": "#7b4fc9", "svg": svg2_es_yuz(),
             "aciklama": "Dikdörtgenler prizmasında karşılıklı duran iki yüz birbirine eştir: ön ile arka, üst ile alt, sağ ile sol. (s. 128)",
             "ek": "Böylece 6 yüz, 3 çift eş yüz olur. Kitaptaki açınımlarda eş yüzler aynı renkle boyanır. (s. 128)",
             "akilda": "3 çift eş yüz",
             "soru": S("Bir kutunun üst yüzüne eş olan yüz hangisidir?", ["Ön yüz", "Sağ yüz", "Alt yüz"], 2,
                       "Üst yüzün karşısında hangi yüz var?", "Karşılıklı yüzler eştir: üst yüzün karşısı alt yüzdür. (s. 128)")},
            {"ad": "Yüzey Açınımı", "renk": "#e8590c", "svg": svg2_acinim(),
             "aciklama": "Bir kutuyu bazı ayrıtlarından kesip düz açınca elde edilen şekle yüzey açınımı denir. Dikdörtgenler prizmasının açınımı 6 dikdörtgenden oluşur. (s. 128)",
             "ek": "Kitapta parfüm, çikolata ve ilaç kutuları kesilip açılıyor; her biri düz bir şekle dönüşüyor. (s. 125–126)",
             "akilda": "Kes, düz aç: 6 dikdörtgen",
             "cozum": {"baslik": "Kutuyu açalım",
                       "problem": "Bir çikolata kutusunu ayrıtlarından kesip düz açıyoruz.",
                       "svg": svg_prizma_et("", "", "", A=120, B=60, C=60),
                       "adimlar": [
                           {"metin": "Ortadaki sütunda 4 yüz yer alır: üst, ön, alt ve arka. Kutunun çevresine sarılan bir şerit gibi."},
                           {"metin": "Ön yüzün iki yanına sol ve sağ yüzler gelir.", "islem": "4 + 2 = 6 dikdörtgen"},
                           {"metin": "Eş yüzleri aynı renkle boya.", "svg": svg_acinim(70, 34, 40, {"ust": "üst", "on": "ön", "alt": "alt", "arka": "arka", "sol": "sol", "sag": "sağ"}, boy=11)}],
                       "sonuc": "6 dikdörtgenden oluşan bir açınım elde ettik. Aynı renkli yüzler eş ve kapanınca karşılıklı. (s. 128)"},
             "soru": S("Dikdörtgenler prizmasının açınımında kaç dikdörtgen vardır?", ["4", "6", "8"], 1,
                       "Açınımdaki her dikdörtgen kutunun bir yüzüdür.", "Kutunun 6 yüzü var; açınımda 6 dikdörtgen olur. (s. 128)")},
            {"ad": "Birden Fazla Açınım", "renk": "#c92a2a", "svg": svg2_farkli(),
             "aciklama": "Bir kutuyu farklı ayrıtlarından kesersek farklı açınımlar elde ederiz. Dikdörtgenler prizmasının birden fazla açınımı vardır. (s. 128)",
             "ek": "Açınımın biçimi değişse de yüzler aynıdır: yine 6 dikdörtgen, yine 3 çift eş yüz. (s. 128)",
             "akilda": "Biçim değişir, yüzler aynı",
             "soru": S("Ali ve Elif aynı kutuyu farklı ayrıtlarından kesip açtı. Hangisi doğrudur?",
                       ["Açınımları aynı olmak zorundadır.", "Elif'in açınımında daha çok yüz vardır.", "Açınımları farklı olabilir ama ikisinde de 6 yüz vardır."], 2,
                       "Kesilen ayrıt değişince ne değişir: biçim mi, yüzlerin sayısı mı?", "Farklı ayrıtlardan kesilince açınımın biçimi değişir ama kutunun 6 yüzü aynı kalır. (s. 128)")},
            {"ad": "Açınım Kapanır mı?", "renk": "#b7791f", "svg": svg2_kapanir(),
             "aciklama": "Bir açınımın kapanıp kutu olması için 6 yüzü olmalı, eş yüzler karşılıklı gelmeli ve hiçbir yüz başka bir yüzün üstüne binmemeli. (s. 127–128)",
             "ek": "Açınımda yan yana duran iki yüz, kutuda da komşu olur. Bir sırada aralarında tek bir yüz bulunan iki yüz ise kapanınca karşılıklı gelir. Kitaptaki oyunda da hangi yüzlerin karşılıklı geleceği tahmin ediliyor. (s. 127)",
             "akilda": "6 yüz, eşler karşılıklı, binme yok",
             "sende": {"baslik": "Sıra sende",
                       "problem": "Görseldeki açınım kapatılınca hangi yüzler karşılıklı gelir?",
                       "svg": svg_kare_ag(numarali_hac()),
                       "adimlar": [
                           {"metin": "2 numaralı yüzü taban yap. 1, 3, 5 ve 6 tabanın çevresinde duvar gibi kalkar.",
                            "soru": S("4 numaralı yüz nereye gelir?", ["Tabanın karşısına, kapak olur", "Tabanın yanına", "Tabanın altına"], 0,
                                      "4, 3'ün ucuna bağlı. 3 duvar olunca 4 nereye katlanır?", "3 duvar olarak kalkınca 4 tepeye katlanır ve kapak olur: 2 ile 4 karşılıklı."),
                            "islem": "2 ile 4 karşılıklı"},
                           {"metin": "Dik sırada 1 ile 3 arasında yalnızca 2 var.",
                            "soru": S("1 numaralı yüzün karşısına hangisi gelir?", ["2", "3", "5"], 1,
                                      "Bir sırada aralarında tek bir yüz olan iki yüz karşılıklı gelir.", "1 ile 3 arasında yalnızca 2 var: 1 ile 3 karşılıklı."),
                            "islem": "1 ile 3 karşılıklı"},
                           {"metin": "Kalan iki yüz: 5 ve 6. Yan sırada aralarında 2 var.", "islem": "5 ile 6 karşılıklı"}],
                       "sonuc": "Harika! Karşılıklı çiftler: 1–3, 2–4, 5–6."},
             "soru": S("Görseldeki açınımlardan hangisi kapanınca bir dikdörtgenler prizması olur?", ["1. çizim", "2. çizim", "3. çizim"], 1,
                       "Önce yüzleri say: 6 mı? Sonra katlamayı hayal et: iki yüz aynı yere geliyor mu?",
                       "2. çizimde 6 yüz var, eş yüzler karşılıklı. 1. çizimde 5 yüz var. 3. çizimde iki yan yüz aynı tarafa düşüp üst üste biner. (s. 128)",
                       svg=sec_svg([prizma_ag("bes"), prizma_ag("dogru"), prizma_ag("cakisan")], h=160))}
        ],
        "akildaKalsin": [
            "Dikdörtgenler prizmasının 6 yüzünün hepsi dikdörtgendir.",
            "Dikdörtgenler prizmasının 6 yüzü, 12 ayrıtı, 8 köşesi vardır.",
            "Karşılıklı yüzler eştir: 3 çift eş yüz.",
            "Kutuyu kesip düz açınca 6 dikdörtgenden oluşan bir açınım çıkar.",
            "Bir kutunun birden fazla açınımı olabilir.",
            "Açınım kapanınca eş yüzler karşılıklı gelmeli, yüzler üst üste binmemeli."],
        "merakKutusu": [
            {"soru": "Kare prizma da bir dikdörtgenler prizması mı?", "cevap": "Evet. Kare de özel bir dikdörtgendir. İki yüzü kare olan ilaç kutusu da bir dikdörtgenler prizmasıdır; ona kare prizma deriz. (s. 125–126)"},
            {"soru": "Bir kutunun kaç farklı açınımı olur?", "cevap": "Birden fazla. Hangi ayrıtları kestiğine göre açınımın biçimi değişir. Kitaptaki oyunda beş farklı açınım çiziliyor. (s. 127–128)"},
            {"soru": "Açınımda aynı renkli iki yüz yan yana gelirse ne olur?", "cevap": "Yan yana duran yüzler kutuda komşu olur, karşılıklı olamaz. Eş yüzler karşılıklı gelmesi gerektiği için böyle bir açınım doğru kapanmaz. (s. 127)"},
            {"soru": "Kesikli çizgiler neden var?", "cevap": "Kutunun arkasında kalan, bizim göremediğimiz ayrıtları gösterir. Böylece bütün ayrıtları sayabiliriz."}],
        "dusunVeYaz": [{"soru": "Bir açınımın kapanıp kutu olup olmayacağını nasıl kontrol edersin?",
                        "ornekCevap": "Önce yüzleri sayarım: 6 olmalı. Sonra eş yüzlerin karşılıklı gelip gelmediğine bakarım. Katlamayı hayal edip iki yüzün üst üste binip binmediğini kontrol ederim.",
                        "anahtarlar": ["6", "eş", "karşılıklı", "bin", "say"]}],
        "sorular": [
            S("Dikdörtgenler prizmasının kaç yüzü vardır?", ["6", "4", "8"], 0,
              "Kutunun önü, arkası, iki yanı, üstü ve altı.", "Ön, arka, sağ, sol, üst, alt: 6 yüz. (s. 128)", kavram="Yüz, Ayrıt, Köşe"),
            G("Dikdörtgenler prizmasının kaç ayrıtı vardır?", "12",
              "Ön yüzün çevresi, arka yüzün çevresi ve önü arkaya bağlayan ayrıtlar.", "Önde 4, arkada 4, önü arkaya bağlayan 4: 12 ayrıt.",
              kavram="Yüz, Ayrıt, Köşe", yardim={"adimlar": ["Ön yüzün çevresindeki ayrıtları say.", "Arka yüzün çevresinde de aynı sayıda ayrıt var.", "Önü arkaya bağlayan ayrıtları ekle."]}),
            S("Görseldeki prizmada sarı ile gösterilen nedir?", ["Ayrıt", "Yüz", "Köşe"], 0,
              "İki yüzün birleştiği çizgiye ne diyorduk?", "Sarı çizgi ön yüz ile sağ yüzün birleştiği yerdir: ayrıt.",
              svg=gsvg(330, 150, prizma(110, 130, 90, 60, 80, vurgu="ayrit")), kavram="Yüz, Ayrıt, Köşe"),
            S("Görseldeki açınımlardan hangisi bir dikdörtgenler prizmasının açınımıdır?", ["1. çizim", "2. çizim", "3. çizim"], 2,
              "Yüzleri say. Sonra katlamayı hayal et.", "3. çizimde 6 yüz var ve eş yüzler karşılıklı gelir. 1. çizimde yan yüzler üst üste biner, 2. çizimde bir yüz eksik. (s. 128)",
              svg=sec_svg([prizma_ag("cakisan"), prizma_ag("bes"), prizma_ag("dogru")], h=160), kavram="Açınım Kapanır mı?"),
            S("Açınımda aynı renkle boyanan iki yüz, kutu kapanınca nasıl durur?", ["Karşılıklı", "Yan yana", "Üst üste"], 0,
              "Aynı renk = eş yüz. Eş yüzler kutunun neresinde?", "Aynı renkli yüzler eştir ve kutu kapanınca karşılıklı durur. (s. 128)", kavram="Karşılıklı Yüzler Eştir"),
            G("Bir dikdörtgenler prizmasında kaç çift eş yüz vardır?", "3",
              "6 yüzü ikişer ikişer eşleştir.", "Ön-arka, üst-alt, sağ-sol: 3 çift. (s. 128)", kavram="Karşılıklı Yüzler Eştir",
              yardim={"adimlar": ["Karşılıklı yüzleri eşleştir: ön ile …", "Kaç çift oldu?"]}),
            S("Görseldeki açınım kapatılınca 2 numaralı yüzün karşısına hangisi gelir?", ["1", "5", "4"], 2,
              "Yatay sırada aralarında tek bir yüz olan iki yüz karşılıklı gelir.",
              "Yatay sırada 2 ile 4 arasında yalnızca 3 var: 2 ile 4 karşılıklı. (s. 127)",
              svg=svg_kare_ag(numarali_141(), s=30), kavram="Açınım Kapanır mı?"),
            S("Bir açınımda 5 dikdörtgen var. Kapatılınca ne olur?", ["Kapalı bir kutu olur.", "Kutunun bir yüzü açık kalır.", "İki kutu olur."], 1,
              "Kapalı bir kutunun kaç yüzü vardır?", "Kapalı kutu için 6 yüz gerekir. 5 yüzle bir yüz açık kalır. (s. 128)", kavram="Yüzey Açınımı"),
            S("Ela çikolata kutusunun açınımını çiziyor. Doğru bir çizimde hangisi olmalıdır?",
              ["6 dikdörtgen, 3 çift eş yüz", "4 dikdörtgen, 2 kare", "6 tane eş kare"], 0,
              "Dikdörtgenler prizmasının yüzlerini hatırla.", "Dikdörtgenler prizmasının açınımı 6 dikdörtgendir ve karşılıklı yüzler eştir. (s. 128)", kavram="Yüzey Açınımı"),
            S("Hangisi dikdörtgenler prizması biçiminde değildir?", ["Ayakkabı kutusu", "Tuğla", "Konserve kutusu"], 2,
              "Hangisinin yuvarlak yüzü var?", "Konserve kutusunun tabanları daire biçimindedir; yüzleri dikdörtgen değildir.", kavram="Dikdörtgenler Prizması"),
            S("Aynı kutunun iki farklı açınımında hangisi aynı kalır?", ["Açınımın biçimi", "Yüzlerin sayısı ve büyüklüğü", "Yüzlerin açınımdaki yeri"], 1,
              "Kutu değişmedi, yalnızca kesilen ayrıtlar değişti.", "Kesilen ayrıt değişince biçim değişir; yüzler aynı kalır: 6 yüz, aynı büyüklükte. (s. 128)", kavram="Birden Fazla Açınım")]
    }


# =================================================================
def u2k3():
    return {
        "id": "u2k3", "unite": T2, "baslik": "Yüzey Alanı", "sayfalar": "s. 129–133",
        "giris": "Bir hediye kutusunu paket kâğıdıyla kaplamak için ne kadar kâğıt gerekir? Bu konuda kutunun bütün yüzlerinin alanını toplayarak yüzey alanını bulacağız. Kare prizma ve küp için kısa yolları da öğreneceğiz.",
        "hazirlik": {
            "baslik": "Hazır mısın?",
            "giris": "Bu konuda dikdörtgenin ve karenin alanını çok kullanacağız. Önce bunları hatırlıyor musun bakalım. Not yok.",
            "maddeler": [
                {"ad": "Dikdörtgenin alanı", "sinif": "Önceki yıllar", "svg": svg2_h_alan(),
                 "anlatim": "Dikdörtgenin alanı, içine sığan birim karelerin sayısıdır. Kısa yoldan: bir kenarı diğer kenarla çarparız.",
                 "akilda": "Alan = kenar × kenar",
                 "ornek": {"problem": "Kenarları 4 cm ve 3 cm olan dikdörtgenin alanı kaç cm²?", "adimlar": [
                     {"metin": "İki kenarı çarp.", "islem": "4 · 3 = 12"},
                     {"metin": "Alan kare birimle yazılır.", "islem": "12 cm²"}]},
                 "sorular": [
                     G("Kenarları 5 cm ve 3 cm olan dikdörtgenin alanı kaç cm²?", "15", "İki kenarı çarp.", "5 · 3 = 15 cm².", birim="cm²",
                       yardim={"adimlar": ["Dikdörtgenin alanı için iki kenarı çarparız.", "5 ile 3'ü çarp."]}),
                     G("Kenarları 6 cm ve 4 cm olan dikdörtgenin alanı kaç cm²?", "24", "İki kenarı çarp.", "6 · 4 = 24 cm².", birim="cm²",
                       yardim={"adimlar": ["Dikdörtgenin alanı için iki kenarı çarparız.", "6 ile 4'ü çarp."]})]},
                {"ad": "Karenin alanı ve üs", "sinif": "1. tema, 10. konu", "svg": svg2_h_kare_alan(),
                 "anlatim": "Karenin kenarları eşit olduğu için alanı kenar · kenar olur. Bunu üsle kısaca a[[u:2]] diye yazarız: kenarı 3 cm olan karenin alanı 3[[u:2]] = 9 cm².",
                 "akilda": "Kare: a · a = a²",
                 "sorular": [
                     G("Kenarı 4 cm olan karenin alanı kaç cm²?", "16", "Kenarı kendisiyle çarp.", "4 · 4 = 4[[u:2]] = 16 cm².", birim="cm²",
                       yardim={"adimlar": ["Karenin dört kenarı eşit: alan = kenar · kenar.", "4 ile 4'ü çarp."]}),
                     S("5[[u:2]] kaçtır?", ["10", "25", "7"], 1, "Üs, tabanın kaç kere çarpıldığını söyler.", "5[[u:2]] = 5 · 5 = 25.")]},
                {"ad": "Alan birimleri", "sinif": "Önceki yıllar", "svg": svg2_h_birim(),
                 "anlatim": "Uzunluk cm, m gibi birimlerle ölçülür. Alan ise kare birimlerle ölçülür: cm², m². Küçük ² işareti “kare” diye okunur.",
                 "akilda": "Uzunluk cm, alan cm²",
                 "sorular": [
                     S("Bir kutunun bir yüzünün alanı hangisi gibi yazılır?", ["20 cm", "20 cm²", "20 kg"], 1, "Alan kare birimle yazılır.", "Alan cm², m² gibi kare birimlerle yazılır."),
                     S("Hangisi bir uzunluktur?", ["8 m", "8 m²", "8 kg"], 0, "Kare işareti olmayan uzunluk birimini ara.", "m bir uzunluk birimidir; m² alan birimidir.")]}
            ]},
        "kavramlar": [
            {"ad": "Yüzey Alanı", "renk": "#1f9e8f", "svg": svg2_hediye(),
             "aciklama": "Bir cismin bütün yüzlerinin alanlarının toplamına yüzey alanı denir. (s. 129)",
             "ek": "Yusuf Öğretmen hediye kutusunu paket kâğıdıyla kaplayacak. Gereken en az kâğıt, kutunun yüzey alanı kadardır. Yüzey alanı bir alan olduğu için cm², m² gibi kare birimlerle yazılır. (s. 129)",
             "akilda": "Bütün yüzleri kaplamak",
             "soru": S("Hediye kutusunu paket kâğıdıyla tamamen kaplamak için neyi bulmalıyız?", ["Kutunun yüzey alanını", "Kutunun ağırlığını", "Kutunun yüksekliğini"], 0,
                       "Kaplamak, bütün yüzlerin üstünü örtmek demek.", "Bütün yüzlerin alanları toplamı yüzey alanıdır; gereken en az kâğıt bu kadardır. (s. 129)")},
            {"ad": "Üç Çift Eş Yüz", "renk": "#1d6fa3", "svg": svg2_uc_cift(),
             "aciklama": "Ayrıtları a, b ve c olan bir dikdörtgenler prizmasında yüzlerin alanları a · b, a · c ve b · c'dir. Her birinden ikişer tane vardır. (s. 129)",
             "ek": "Karşılıklı yüzler eş olduğu için 6 yüzün alanını tek tek hesaplamak gerekmez: 3 farklı yüzü bulmak yeter. (s. 129)",
             "akilda": "3 farklı yüz, ikişer tane",
             "cozum": {"baslik": "Hediye kutusu",
                       "problem": "Yusuf Öğretmen'in hediye kutusunun ayrıtları 20 cm, 25 cm ve 30 cm. Üç farklı yüzün alanını bulalım.",
                       "svg": svg_prizma_et("20 cm", "25 cm", "30 cm", A=100, B=80, C=90, h=180),
                       "adimlar": [
                           {"metin": "En ile boyun yaptığı yüz (üst ve alt).", "islem": "20 · 25 = 500"},
                           {"metin": "En ile yüksekliğin yaptığı yüz (ön ve arka).", "islem": "20 · 30 = 600"},
                           {"metin": "Boy ile yüksekliğin yaptığı yüz (sağ ve sol).", "islem": "25 · 30 = 750"}],
                       "sonuc": "Kutuda 500 cm², 600 cm² ve 750 cm²'lik yüzlerden ikişer tane var. (s. 129)"},
             "soru": G("Ayrıtları 2 cm, 3 cm ve 4 cm olan bir kutunun en büyük yüzünün alanı kaç cm²?", "12",
                       "Üç farklı yüz: 2 · 3, 2 · 4 ve 3 · 4. Hangisi en büyük?", "Yüzler 6, 8 ve 12 cm². En büyüğü 3 · 4 = 12 cm². (s. 129)", birim="cm²",
                       yardim={"adimlar": ["Üç farklı yüzün alanını bul: 2 · 3, 2 · 4, 3 · 4.", "Üç sonucu karşılaştır."]})},
            {"ad": "Yüzey Alanı Formülü", "renk": "#7b4fc9", "svg": svg2_formul(),
             "aciklama": "Ayrıtları a, b ve c olan dikdörtgenler prizmasının yüzey alanı = 2 · (a · b + a · c + b · c). (s. 129)",
             "ek": "Üç farklı yüzün alanını topla, sonucu 2 ile çarp. Her yüzden iki tane olduğu için 2 ile çarparız. (s. 129)",
             "akilda": "Üçünü topla, 2 ile çarp",
             "cozum": {"baslik": "Kaç cm² kâğıt?",
                       "problem": "Hediye kutusunun yüzleri 500 cm², 600 cm² ve 750 cm². Yusuf Öğretmen'e en az kaç cm² paket kâğıdı gerekir?",
                       "adimlar": [
                           {"metin": "Kaplamak mı, doldurmak mı? Kaplamak: yüzey alanı."},
                           {"metin": "Üç farklı yüzü topla.", "islem": "500 + 600 + 750 = 1850"},
                           {"metin": "Her yüzden iki tane var: 2 ile çarp.", "islem": "2 · 1850 = 3700"}],
                       "sonuc": "En az 3700 cm² paket kâğıdı gerekir. (s. 129)"},
             "sende": {"baslik": "Sıra sende",
                       "problem": "Ayrıtları 2 cm, 3 cm ve 4 cm olan bir kutunun yüzey alanını bul.",
                       "svg": svg_prizma_et("2 cm", "3 cm", "4 cm", A=70, B=80, C=100, h=180),
                       "adimlar": [
                           {"metin": "Üç farklı yüzün alanı: 2 · 3, 2 · 4 ve 3 · 4.",
                            "soru": G("6 + 8 + 12 kaçtır?", "26", "Önce 6 ile 8'i topla, sonra 12 ekle.", "6 + 8 = 14, 14 + 12 = 26.",
                                      yardim={"adimlar": ["6 ile 8'i topla.", "Çıkan sayıya 12 ekle."]}),
                            "islem": "6 + 8 + 12 = 26"},
                           {"metin": "Her yüzden iki tane var.",
                            "soru": G("2 · 26 kaçtır?", "52", "26'yı iki kere topla.", "26 + 26 = 52.",
                                      yardim={"adimlar": ["2 · 26, iki tane 26 demek.", "26 ile 26'yı topla."]}),
                            "islem": "2 · 26 = 52 cm²"}],
                       "sonuc": "Harika! Kutunun yüzey alanı 52 cm²."},
             "soru": S("Ayrıtları a, b ve c olan dikdörtgenler prizmasının yüzey alanı hangisidir?", ["a · b · c", "a + b + c", "2 · (a · b + a · c + b · c)"], 2,
                       "Üç farklı yüzün alanını topla, 2 ile çarp.", "Yüzler a · b, a · c, b · c; ikişer tane. 2 · (a · b + a · c + b · c). (s. 129)")},
            {"ad": "Kare Prizma", "renk": "#e8590c", "svg": svg2_kare_prizma(),
             "aciklama": "İki karşılıklı yüzü kare olan dikdörtgenler prizmasına kare prizma denir. Kare prizma, dikdörtgenler prizmasının özel bir durumudur. (s. 131)",
             "ek": "Kitaptaki şurup kutusu kare prizmadır. Taban kenarı a, yüksekliği b ise: yüzey alanı = 2 · a[[u:2]] + 4 · a · b. (s. 130–131)",
             "akilda": "2 kare + 4 eş dikdörtgen",
             "cozum": {"baslik": "Şurup kutusu",
                       "problem": "Tabanı kenarı 3 cm olan kare, yüksekliği 10 cm olan bir şurup kutusunun yüzey alanını bulalım.",
                       "svg": svg_prizma_et("3 cm", "3 cm", "10 cm", A=50, B=50, C=120, h=180),
                       "adimlar": [
                           {"metin": "İki kare yüz: 3 · 3 = 9. İki tane.", "islem": "2 · 9 = 18"},
                           {"metin": "Dört eş dikdörtgen yüz: 3 · 10 = 30. Dört tane.", "islem": "4 · 30 = 120"},
                           {"metin": "Topla.", "islem": "18 + 120 = 138"}],
                       "sonuc": "Şurup kutusunun yüzey alanı 138 cm². (s. 131)"},
             "soru": G("Tabanı kenarı 2 cm olan kare, yüksekliği 5 cm olan kare prizmanın yüzey alanı kaç cm²?", "48",
                       "İki kare yüz: 2 · 2. Dört eş dikdörtgen yüz: 2 · 5.", "2 · 4 = 8 ve 4 · 10 = 40. 8 + 40 = 48 cm². (s. 131)", birim="cm²",
                       yardim={"adimlar": ["İki kare yüz: 2 · 2, iki tane.", "Dört eş dikdörtgen yüz: 2 · 5, dört tane.", "İki sonucu topla."]})},
            {"ad": "Küp", "renk": "#c92a2a", "svg": svg2_kup(),
             "aciklama": "Bütün yüzleri eş kare olan prizmaya küp denir. Küpün yüzey alanı = 6 · a[[u:2]]. (s. 131)",
             "ek": "Küp de dikdörtgenler prizmasının özel bir durumudur: üç ayrıtı da eşittir. 6 yüzün hepsi aynı karedir. (s. 131)",
             "akilda": "6 eş kare: 6 · a²",
             "soru": G("Bir ayrıtı 2 cm olan küpün yüzey alanı kaç cm²?", "24",
                       "Bir yüzün alanı 2 · 2. Küpün kaç yüzü var?", "Bir yüz 2 · 2 = 4 cm². 6 yüz: 6 · 4 = 24 cm². (s. 131)", birim="cm²",
                       yardim={"adimlar": ["Bir yüzün alanı: 2 · 2.", "Küpün 6 eş yüzü var: bir yüzün alanını 6 ile çarp."]})},
            {"ad": "Hangi Yüzler Kaplanacak?", "renk": "#b7791f", "svg": svg2_kapla(),
             "aciklama": "Problemde önce sor: Kaplamak mı istiyorum, doldurmak mı? Kaplamaksa yüzey alanını bulurum. Sonra kaç yüzün kaplanacağını sayarım.",
             "ek": "Kapaksız bir kutuda üst yüz yoktur; yalnızca 5 yüz kaplanır. Kitaptaki marangoz ise blokların bütün yüzlerini koruyucu malzemeyle kaplıyor. (s. 133)",
             "akilda": "Kaplamak = yüzey alanı; yüzleri say",
             "sende": {"baslik": "Kapaksız kutu",
                       "problem": "Tabanı 10 cm × 10 cm, yüksekliği 5 cm olan kapaksız bir kutunun dışı boyanacak. Kaç cm² boyanır?",
                       "adimlar": [
                           {"metin": "Kaplamak mı, doldurmak mı? Boyamak bir kaplamadır. Kapak yok.",
                            "soru": G("Kaç yüz boyanır?", "5", "Kutunun 6 yüzü var; biri eksik.", "Kapak yok: 6 − 1 = 5 yüz (taban ve 4 yan yüz).",
                                      yardim={"adimlar": ["Kapalı bir kutunun kaç yüzü var?", "Kapak yoksa bir yüz eksik."]}),
                            "islem": "taban + 4 yan yüz"},
                           {"metin": "Taban: 10 · 10.", "islem": "100"},
                           {"metin": "Yan yüzlerin her biri 10 · 5 = 50. Dört tane.",
                            "soru": G("4 · 50 kaçtır?", "200", "4 tane 50'yi topla.", "4 · 50 = 200.",
                                      yardim={"adimlar": ["4 · 50, dört tane 50 demek.", "50 + 50 + 50 + 50"]}),
                            "islem": "4 · 50 = 200"},
                           {"metin": "Topla.", "islem": "100 + 200 = 300 cm²"}],
                       "sonuc": "Harika! 300 cm² boyanır."},
             "soru": S("Ayrıtı 10 cm olan küp şeklindeki bir kutunun bütün yüzleri boyanacak. Boyanacak alanı hangi işlem verir?", ["6 · 10 · 10", "4 · 10", "10 · 10 · 10"], 0,
                       "Boyamak = kaplamak. Küpün kaç yüzü var, bir yüzün alanı ne?", "Bir yüz 10 · 10; 6 yüz var: 6 · 10 · 10 = 600 cm². (s. 131)")}
        ],
        "akildaKalsin": [
            "Yüzey alanı, bütün yüzlerin alanlarının toplamıdır.",
            "Karşılıklı yüzler eş: 3 farklı yüzü bul, ikişer tane say.",
            "Dikdörtgenler prizması: 2 · (a · b + a · c + b · c).",
            "Kare prizma: 2 · a² + 4 · a · b. Küp: 6 · a².",
            "Yüzey alanı kare birimle yazılır: cm², m².",
            "Önce sor: Kaplamak mı, doldurmak mı? Kaç yüz kaplanacak?"],
        "merakKutusu": [
            {"soru": "Açınımın alanı ile yüzey alanı aynı mı?", "cevap": "Evet. Açınım, kutunun bütün yüzlerinin düz yere serilmiş hâlidir. Açınımın alanı kutunun yüzey alanına eşittir. (s. 129)"},
            {"soru": "Neden 2 ile çarpıyoruz?", "cevap": "Karşılıklı yüzler eş olduğu için her yüzden iki tane var. Üç farklı yüzü toplayınca kutunun yarısını bulmuş oluruz; 2 ile çarpınca tamamı çıkar. (s. 129)"},
            {"soru": "Küpü ortadan kesince yüzey alanı değişir mi?", "cevap": "Kitaptaki marangoz uzun bir bloğu ortadan kesip iki küp yapıyor. Kesilen yerde iki yeni yüz ortaya çıkar; bu yüzden iki küpün toplam yüzey alanı, bloğunkinden büyük olur. (s. 133)"},
            {"soru": "Kare prizmada 2 kare mi, 4 kare mi var?", "cevap": "Kare prizmanın iki karşılıklı yüzü kare, diğer dört yüzü eş dikdörtgendir. Dört yüz de kare olsaydı küp olurdu. (s. 131)"}],
        "dusunVeYaz": [{"soru": "Can, ayrıtları 2 cm, 3 cm ve 5 cm olan kutunun yüzey alanını 2 · 3 + 2 · 5 + 3 · 5 = 31 cm² buldu. Hatası ne? Doğru sonucu bul.",
                        "ornekCevap": "Can üç farklı yüzü topladı ama 2 ile çarpmayı unuttu. Her yüzden iki tane var: 2 · 31 = 62 cm².",
                        "anahtarlar": ["2 ile çarp", "iki", "62", "unut"]}],
        "sorular": [
            G("Ayrıtları 2 cm, 3 cm ve 5 cm olan dikdörtgenler prizmasının yüzey alanı kaç cm²?", "62",
              "Üç farklı yüz: 2 · 3, 2 · 5, 3 · 5. Topla, 2 ile çarp.", "Yüzler 6, 10, 15. 6 + 10 + 15 = 31. 2 · 31 = 62 cm². (s. 129)",
              birim="cm²", kavram="Yüzey Alanı Formülü",
              yardim={"adimlar": ["Kaplamak mı, doldurmak mı? Yüzey alanı soruluyor.", "Üç farklı yüzün alanını bul: 2 · 3, 2 · 5, 3 · 5.", "Üçünü topla.", "Toplamı 2 ile çarp."]}),
            G("Bir ayrıtı 5 cm olan küpün yüzey alanı kaç cm²?", "150",
              "Bir yüzün alanını bul, 6 ile çarp.", "Bir yüz 5 · 5 = 25 cm². 6 · 25 = 150 cm². (s. 131)", birim="cm²", kavram="Küp",
              yardim={"adimlar": ["Küpün bir yüzü kare: 5 · 5.", "Küpün 6 eş yüzü var.", "Bir yüzün alanını 6 ile çarp."]}),
            S("Görseldeki açınımda yüzlerin alanları cm² olarak yazılmıştır. Kutunun yüzey alanı kaç cm²?", ["26", "52", "48"], 1,
              "Açınımdaki altı sayıyı topla.", "8 + 8 + 12 + 12 + 6 + 6 = 52 cm². Açınımın alanı yüzey alanına eşittir. (s. 129)",
              svg=svg_acinim(80, 40, 50, {"ust": "8", "on": "12", "alt": "8", "arka": "12", "sol": "6", "sag": "6"}, boy=15), kavram="Üç Çift Eş Yüz"),
            G("Tabanı kenarı 4 cm olan kare, yüksekliği 5 cm olan kare prizmanın yüzey alanı kaç cm²?", "112",
              "İki kare yüz: 4 · 4. Dört eş dikdörtgen yüz: 4 · 5.", "2 · 16 = 32 ve 4 · 20 = 80. 32 + 80 = 112 cm². (s. 131)", birim="cm²", kavram="Kare Prizma",
              yardim={"adimlar": ["İki kare yüzün alanı: 4 · 4, iki tane.", "Dört eş dikdörtgen yüzün alanı: 4 · 5, dört tane.", "İki sonucu topla."]}),
            S("Hangisi yüzey alanı için uygun bir birimdir?", ["cm", "kg", "cm²"], 2,
              "Yüzey alanı bir alandır. Alan hangi birimle yazılır?", "Alan kare birimle yazılır: cm². (s. 129)", kavram="Yüzey Alanı"),
            S("Bir dikdörtgenler prizmasının birbirinden farklı üç yüzünün alanları 20 cm², 30 cm² ve 40 cm²'dir. Yüzey alanı kaç cm²'dir?", ["90", "120", "180"], 2,
              "Her yüzden kaç tane var?", "Her yüzden iki tane var: 2 · (20 + 30 + 40) = 180 cm². (s. 132)", kavram="Üç Çift Eş Yüz"),
            G("Tabanı 6 cm × 4 cm, yüksekliği 3 cm olan kapaksız bir kutunun dışı kâğıtla kaplanacak. Kaç cm² kâğıt gerekir?", "84",
              "Kapak yok: taban + 4 yan yüz. Ön-arka 6 · 3, sağ-sol 4 · 3.", "Taban 6 · 4 = 24. Ön ve arka 2 · 18 = 36. Sağ ve sol 2 · 12 = 24. 24 + 36 + 24 = 84 cm².",
              birim="cm²", kavram="Hangi Yüzler Kaplanacak?",
              yardim={"adimlar": ["Kaplamak mı, doldurmak mı? Kaplamak. Kapak yok: kaç yüz kaplanacak?", "Tabanın alanı: 6 · 4.", "Ön ve arka: 6 · 3, iki tane. Sağ ve sol: 4 · 3, iki tane.", "Hepsini topla."]}),
            S("Bir küpün bütün ayrıtlarının uzunlukları toplamı 60 cm'dir. Bu küpün yüzey alanı kaç cm²'dir?", ["150", "60", "360"], 0,
              "Küpün 12 eş ayrıtı var. Önce bir ayrıtı bul.", "Bir ayrıt 60 ÷ 12 = 5 cm. Yüzey alanı 6 · 5 · 5 = 150 cm². (s. 132)", kavram="Küp",
              yardim={"adimlar": ["Küpün 12 ayrıtı var ve hepsi eşit.", "Bir ayrıt: 60 ÷ 12.", "Bir yüzün alanını bul, 6 ile çarp."]}),
            S("Hangisi doğrudur?", ["Küp bir dikdörtgenler prizmasıdır.", "Kare prizmanın bütün yüzleri karedir.", "Küpün yüzleri farklı büyüklüktedir."], 0,
              "Kare özel bir dikdörtgendir. Küpün yüzleri ne şekildedir?", "Küp ve kare prizma, dikdörtgenler prizmasının özel durumlarıdır. (s. 131)", kavram="Kare Prizma"),
            G("Ela ayrıtları 10 cm, 10 cm ve 20 cm olan bir kutuyu paket kâğıdıyla kaplayacak. En az kaç cm² kâğıt gerekir?", "1000",
              "Kaplamak = yüzey alanı. Üç farklı yüz: 10 · 10, 10 · 20, 10 · 20.", "Yüzler 100, 200, 200. Toplam 500. 2 · 500 = 1000 cm². (s. 129)",
              birim="cm²", kavram="Yüzey Alanı",
              yardim={"adimlar": ["Kaplamak mı, doldurmak mı? Kaplamak: yüzey alanı.", "Üç farklı yüzün alanı: 10 · 10, 10 · 20, 10 · 20.", "Üçünü topla.", "Toplamı 2 ile çarp."]})]
    }


# =================================================================
def u2t1():
    return {
        "id": "u2t1", "tur": "tarama", "unite": T2,
        "baslik": "Ara Durak 1: Cisimler ve Yüzeyleri", "sayfalar": "Konu 1–3 · s. 118–133",
        "giris": "İlk üç konuyu bitirdin, tebrikler! Şimdi kısa bir mola verip öğrendiklerimizi birlikte gözden geçireceğiz. Önce özetleri oku ve kartları çevir, sonra tarama testini çöz. Not yok.",
        "buyukResim": "Önce eş küplerden yapılara altı yönden baktık ve kareleri saydık. Sonra bir kutuyu kesip açtık: 6 yüz, 3 çift eş yüz. En son bu yüzlerin alanlarını toplayıp yüzey alanını bulduk. Kutu biçimindeki bir küp yapısında altı görünümdeki karelerin toplamı da yüzey alanını verir!",
        "kapsar": ["u2k1", "u2k2", "u2k3"],
        "hatirla": [
            {"konu": "u2k1", "maddeler": [
                "Bir yapıya altı yönden bakılır; her küp yüzü kare görünür.",
                "Öndeki küp arkasındakini saklar: “en az kaç küp” diye sorarız.",
                "Ön-arka ve sağ-sol görünümler ayna gibidir (dikey doğruya göre simetrik)."]},
            {"konu": "u2k2", "maddeler": [
                "Dikdörtgenler prizması: 6 yüz, 12 ayrıt, 8 köşe.",
                "Karşılıklı yüzler eştir: 3 çift.",
                "Açınım 6 dikdörtgendir; eş yüzler kapanınca karşılıklı gelir."]},
            {"konu": "u2k3", "maddeler": [
                "Yüzey alanı = bütün yüzlerin alanları toplamı.",
                "2 · (a · b + a · c + b · c); küpte 6 · a².",
                "Kaplamak = yüzey alanı; birim cm²."]}],
        "eskiSoru": 4,
        "oyunKavram": 8,
        "gruplar": [{"soru": "Bu bilgi hangi konudan?", "kutular": [
            {"etiket": "Görünümler", "uyeler": ["Altı Yön", "Karşılıklı Görünümler Simetrik"]},
            {"etiket": "Açınım", "uyeler": ["Yüzey Açınımı", "Açınım Kapanır mı?"]},
            {"etiket": "Yüzey alanı", "uyeler": ["Yüzey Alanı Formülü", "Küp"]}]}],
        "sorular": [
            G("Görseldeki yapı, ayrıtı 1 cm olan 2 eş küpten yapıldı. Yapının yüzey alanı kaç cm²?", "10",
              "Altı yönden bak ve kareleri say. Her kare 1 cm².",
              "Önden 2, arkadan 2, üstten 2, alttan 2, sağdan 1, soldan 1 kare: 10 kare. Her kare 1 cm²: 10 cm².",
              birim="cm²", svg=svg_yapi(Y_IKILI, s=40),
              kaynak=[K("u2k1", "Görünüm Kare Gösterir"), K("u2k3", "Yüzey Alanı")],
              yardim={"adimlar": ["Kaplamak mı, doldurmak mı? Yüzey alanı: bütün yüzleri say.", "Önden, arkadan, üstten, alttan kaç kare görünür?", "Sağdan ve soldan kaç kare görünür?", "Bütün kareleri topla; her kare 1 cm²."]}),
            G("Ayrıtı 1 cm olan 3 eş küp yan yana dizildi; 3 cm, 1 cm ve 1 cm'lik bir prizma oluştu. Bu prizmanın yüzey alanı kaç cm²?", "14",
              "Üç farklı yüz: 3 · 1, 3 · 1, 1 · 1. Topla, 2 ile çarp. Ya da altı yönden kareleri say.",
              "Yüzler 3, 3 ve 1 cm². 2 · (3 + 3 + 1) = 14 cm². Kareleri sayınca da 3 + 3 + 3 + 3 + 1 + 1 = 14.",
              birim="cm²", svg=svg_yapi(Y_UCLU, s=36),
              kaynak=[K("u2k1", "Görünüm Kare Gösterir"), K("u2k3", "Yüzey Alanı Formülü")],
              yardim={"adimlar": ["Kaplamak mı, doldurmak mı? Yüzey alanı.", "Ölçüler: 3 cm, 1 cm, 1 cm. Üç farklı yüz: 3 · 1, 3 · 1, 1 · 1.", "Üçünü topla.", "Toplamı 2 ile çarp."]}),
            S("Görseldeki açınım kapatılıp küp yapıldı. Önden bakınca 2 numaralı yüz görünüyor. Arkadan bakınca hangi yüz görünür?", ["4", "3", "5"], 0,
              "Arka, önün karşısıdır. Açınımda 2'nin karşısına hangi yüz gelir?",
              "Dik sırada 2 ile 4 arasında yalnızca 3 var: 2 ile 4 karşılıklı. Ön yüz 2 ise arka yüz 4. (s. 127)",
              svg=svg_kare_ag(numarali_hac()),
              kaynak=[K("u2k2", "Açınım Kapanır mı?"), K("u2k1", "Altı Yön")]),
            S("Ela ayrıtları 2 cm, 3 cm ve 4 cm olan bir kutunun açınımını çizdi. Açınımda 3 cm × 4 cm'lik kaç dikdörtgen olmalıdır?", ["1", "2", "3"], 1,
              "Karşılıklı yüzler eştir. 3 cm × 4 cm'lik yüzün karşısında ne var?",
              "Her yüzün karşısında eşi vardır: 3 cm × 4 cm'lik yüzden 2 tane olur. (s. 128–129)",
              kaynak=[K("u2k2", "Karşılıklı Yüzler Eştir"), K("u2k3", "Üç Çift Eş Yüz")]),
            G("Ayrıtı 2 cm olan küp şeklindeki bir zarın açınımı kartondan kesilecek. Açınım en az kaç cm² karton tutar?", "24",
              "Açınımın alanı, küpün yüzey alanına eşittir.",
              "Açınım 6 eş kareden oluşur. Bir kare 2 · 2 = 4 cm². 6 · 4 = 24 cm².",
              birim="cm²", kaynak=[K("u2k2", "Yüzey Açınımı"), K("u2k3", "Küp")],
              yardim={"adimlar": ["Küpün açınımı kaç kareden oluşur?", "Bir karenin alanı: 2 · 2.", "Bir karenin alanını kare sayısıyla çarp."]}),
            G("Görseldeki yapı, ayrıtı 1 cm olan 4 eş küpten yapıldı. Üstten görünümü 4 kare, önden görünümü 2 karedir. Yapının yüzey alanı kaç cm²?", "16",
              "Altı yönden kareleri say: üst ve alt, ön ve arka, sağ ve sol.",
              "Üst 4, alt 4, ön 2, arka 2, sağ 2, sol 2: 16 kare. Her kare 1 cm²: 16 cm². Formülle: 2 · (4 + 2 + 2) = 16.",
              birim="cm²", svg=svg_yapi(Y_BLOK4, s=36),
              kaynak=[K("u2k1", "Görünümden Yapıya"), K("u2k3", "Yüzey Alanı")],
              yardim={"adimlar": ["Kaplamak mı, doldurmak mı? Yüzey alanı.", "Üstten ve alttan kaç kare? Önden ve arkadan kaç kare?", "Sağdan ve soldan kaç kare?", "Hepsini topla; her kare 1 cm²."]}),
            S("Hangisi doğrudur?",
              ["Küpün açınımı 4 kareden oluşur.", "Önden ve arkadan görünümlerdeki kare sayıları farklıdır.", "Bir kutunun açınımının alanı, kutunun yüzey alanına eşittir."], 2,
              "Açınım, kutunun bütün yüzlerinin düz yere serilmiş hâlidir.",
              "Açınım bütün yüzlerden oluştuğu için alanı yüzey alanına eşittir. Küp açınımı 6 karedir; ön ve arka görünümler ayna gibidir, kare sayıları aynıdır.",
              kaynak=[K("u2k2", "Yüzey Açınımı"), K("u2k3", "Yüzey Alanı"), K("u2k1", "Karşılıklı Görünümler Simetrik")])]
    }


# =================================================================
# Tema 2 · Hacim (u2k4, u2k5, u2t2) — 16 Ekim 2026
# Kitap dışı: "Kaplamak mı, doldurmak mı?" ayrı kavram kartı (Kemal onayı), birim küp = hacmin "cetveli" benzetmesi,
# 18 küplü prizmaların ve ayrıt-kat ilişkisinin sonuçları kitabın etkinliklerinden (s. 141, 143) formülle türetildi.
from t2_cizim import _poly as t2poly

SOLUK_KUP = ("#5a6280", "#3a4570", "#2b355c")
ALTIN_KUP = ("#ffe8a3", "#f2c14e", "#b8902a")


def kutu(I, J, K_):
    return [(i, j, k) for i in range(I) for j in range(J) for k in range(K_)]


def kupler_r(kup, x0, y0, s, renk_f, d=None, cizgi="#1b2340"):
    """kupler() gibi; her küpün rengi renk_f(i, j, k) ile seçilir (tek sıralama, üst üste binme doğru)."""
    d = s * 0.5 if d is None else d
    out = ""
    for i, j, k in sorted(set(kup), key=lambda c: (-c[1], c[2], c[0])):
        r = renk_f(i, j, k)
        x, y = x0 + i * s + j * d, y0 - k * s - j * d
        out += t2poly([(x, y), (x + s, y), (x + s, y - s), (x, y - s)], r[1], cizgi)
        out += t2poly([(x, y - s), (x + s, y - s), (x + s + d, y - s - d), (x + d, y - s - d)], r[0], cizgi)
        out += t2poly([(x + s, y), (x + s + d, y - d), (x + s + d, y - s - d), (x + s, y - s)], r[2], cizgi)
    return out


def katman_svg(I, J, K_, s=24, w=330, h=170, kat_yazi=True):
    """Prizma birim küplerle dolu; alt katman altın renkli."""
    yw, yh = yapi_boyut(kutu(I, J, K_), s)
    x0, alt = (w - yw) / 2, h - 22
    g = kupler_r(kutu(I, J, K_), x0, alt, s, lambda i, j, k: ALTIN_KUP if k == 0 else KUP)
    if kat_yazi:
        g += t2t(x0 + yw + 8, alt - s / 2 + 4, "1. katman", "#f2c14e", 12, 800, "start")
    return gsvg(w, h, g)


def svg_dolu(kup, s=30, w=330, h=160):
    """Birim küplerle dolu prizma; yön etiketi yok."""
    return svg_yapi(kup, s=s, w=w, h=h, yonler=False)


# ---------- Kavram ve hazırlık çizimleri (120 × 120) ----------
def svg2_hacim():
    return bg(kupler(kutu(3, 2, 2), 24, 90, 18) + txt(60, 112, "kapladığı yer", "#f2c14e", 11))


def svg2_kapla_doldur():
    g = prizma(8, 84, 36, 24, 34, vurgu="yuz")
    g += kupler(kutu(2, 2, 2), 66, 84, 16)
    g += txt(32, 28, "kapla", "#ffd166", 12) + txt(90, 28, "doldur", "#4fc3a1", 12)
    g += txt(32, 104, "alan br²", "#ffd166", 10) + txt(90, 104, "hacim br³", "#4fc3a1", 10)
    return bg(g)


def svg2_es_nesne():
    g = "<path d='M12 30 V84 H56 V30' fill='none' stroke='#f5f6fa' stroke-width='2.5'/><path d='M64 30 V84 H108 V30' fill='none' stroke='#f5f6fa' stroke-width='2.5'/>"
    for n in range(8):
        g += f"<circle cx='{21 + (n % 3) * 13}' cy='{75 - (n // 3) * 13}' r='6' fill='#ffd166'/>"
    for n in range(6):
        g += f"<circle cx='{73 + (n % 3) * 13}' cy='{75 - (n // 3) * 13}' r='6' fill='#ffd166'/>"
    g += txt(34, 100, "8", "#f5f6fa", 13) + txt(86, 100, "6", "#f5f6fa", 13)
    g += txt(60, 116, "aynı bilyeyle say", "#f2c14e", 10)
    return bg(g)


def svg2_birim_kup():
    g = kupler([(0, 0, 0)], 34, 88, 40)
    g += txt(54, 102, "1", EN, 13) + txt(28, 72, "1", YUK, 13) + txt(102, 84, "1", BOY, 13)
    g += txt(60, 116, "her ayrıtı 1 birim", "#f2c14e", 10)
    return bg(g)


def svg2_say():
    return bg(kupler(kutu(3, 2, 2), 24, 90, 18) + txt(60, 112, "12 küp = 12 br³", "#f2c14e", 11))


def svg2_uygun_birim():
    g = "<rect x='10' y='34' width='46' height='46' fill='none' stroke='#f5f6fa' stroke-width='2.5'/>"
    g += "<rect x='12' y='58' width='42' height='20' fill='#6fb3ff' stroke='#1b2340' stroke-width='1.5'/><rect x='12' y='38' width='42' height='18' fill='#6fb3ff' stroke='#1b2340' stroke-width='1.5'/>"
    g += "<rect x='64' y='34' width='46' height='46' fill='none' stroke='#f5f6fa' stroke-width='2.5'/>"
    g += "".join(f"<rect x='{65 + c * 14.7:.1f}' y='{35 + r * 14.7:.1f}' width='14.7' height='14.7' fill='#4fc3a1' stroke='#1b2340' stroke-width='1.5'/>" for c in range(3) for r in range(3))
    g += txt(33, 96, "boşluk", "#ff8fab", 11) + txt(87, 96, "tam dolar", "#4fc3a1", 11)
    g += txt(60, 114, "küp daha uygun", "#f2c14e", 10)
    return bg(g)


def svg2_h_carpim():
    g = "".join(f"<circle cx='{30 + i * 20}' cy='{30 + j * 20}' r='7' fill='#4fc3a1'/>" for i in range(4) for j in range(3))
    g += txt(60, 104, "4 · 3 = 12", "#f2c14e", 15)
    return bg(g)


def svg2_h_uc_carp():
    return bg(txt(60, 46, "2 · 3 · 4", "#f5f6fa", 18) + txt(60, 72, "= 6 · 4", "#9aa3bf", 15) + txt(60, 98, "= 24", "#f2c14e", 18))


def svg2_h_ondalik():
    return bg(txt(60, 50, "2,5 · 4", "#f5f6fa", 18) + txt(60, 78, "= 10", "#f2c14e", 20) + txt(60, 104, "virgülü yerleştir", "#9aa3bf", 10))


def svg2_h_us():
    return bg(txt(60, 46, "3³", "#f2c14e", 26) + txt(60, 74, "3 · 3 · 3", "#f5f6fa", 15) + txt(60, 100, "= 27", "#f2c14e", 17))


def svg2_katman():
    g = kupler_r(kutu(5, 2, 3), 24, 86, 12, lambda i, j, k: ALTIN_KUP if k == 0 else SOLUK_KUP)
    g += txt(60, 108, "1 kat: 10 küp · 3 kat", "#f2c14e", 10)
    return bg(g)


def svg2_formul_hacim():
    return bg(prizma(22, 84, 48, 36, 40, ("a", "b", "c")) + txt(60, 114, "a · b · c", "#f2c14e", 13))


def svg2_kup_hacim():
    return bg(prizma(32, 86, 40, 40, 40, ("a", "a", "a")) + txt(60, 116, "a · a · a = a³", "#f2c14e", 12))


def svg2_br3():
    g = txt(60, 40, "br · br · br", "#f5f6fa", 15) + txt(60, 68, "= br³", "#f2c14e", 22)
    g += txt(60, 98, "alan br², hacim br³", "#9aa3bf", 10)
    return bg(g)


def svg2_ayni_hacim():
    g = kupler(kutu(3, 3, 2), 6, 88, 10) + kupler(kutu(6, 1, 3), 60, 88, 8)
    g += txt(60, 110, "ikisi de 18 küp", "#f2c14e", 11)
    return bg(g)


def svg2_iki_kat():
    g = prizma(8, 86, 30, 20, 24) + prizma(66, 86, 30, 20, 48)
    g += "<path d='M50 60 h8' stroke='#f2c14e' stroke-width='3' stroke-linecap='round'/><path d='M61 60l-6-4v8z' fill='#f2c14e'/>"
    g += txt(60, 108, "yükseklik 2 kat", "#f783ac", 10) + txt(60, 118, "hacim 2 kat", "#f2c14e", 10)
    return bg(g)


# =================================================================
def u2k4():
    return {
        "id": "u2k4", "unite": T2, "baslik": "Hacim ve Birim Küp", "sayfalar": "s. 134–138",
        "giris": "Bir kutunun içine kaç şeker sığar? Bu konuda bir cismin kapladığı yeri, yani hacmini öğreneceğiz. Kutuları eş küplerle doldurup küpleri sayarak hacmi bulacağız.",
        "hazirlik": {
            "baslik": "Hazır mısın?",
            "giris": "Bu konuda küpleri sayacağız ve çarpma yapacağız. Önce bunları hatırlıyor musun bakalım. Not yok.",
            "maddeler": [
                {"ad": "Çarparak sayma", "sinif": "Önceki yıllar", "svg": svg2_h_carpim(),
                 "anlatim": "Sıra sıra dizilmiş şeyleri tek tek saymak yerine çarparız: 3 sırada 4'er tane varsa 3 · 4 = 12 tane vardır.",
                 "akilda": "Sıra sayısı × bir sıradaki",
                 "ornek": {"problem": "Bir kolide 5 sıra, her sırada 4 şişe var. Kaç şişe var?", "adimlar": [
                     {"metin": "Bir sırada kaç şişe var?", "islem": "4"},
                     {"metin": "Kaç sıra var?", "islem": "5"},
                     {"metin": "Çarp.", "islem": "5 · 4 = 20"}]},
                 "sorular": [
                     G("3 sırada 6'şar elma var. Kaç elma var?", "18", "Sıra sayısını bir sıradakiyle çarp.", "3 · 6 = 18 elma.",
                       yardim={"adimlar": ["Kaç sıra var? Bir sırada kaç elma var?", "3 ile 6'yı çarp."]}),
                     G("Her katında 8 daire olan 4 katlı bir apartmanda kaç daire var?", "32", "Kat sayısını bir kattaki daire sayısıyla çarp.", "4 · 8 = 32 daire.",
                       yardim={"adimlar": ["Kaç kat var? Bir katta kaç daire var?", "4 ile 8'i çarp."]})]},
                {"ad": "Kaplamak: yüzey alanı", "sinif": "2. tema, 3. konu", "svg": svg2_hediye(),
                 "anlatim": "Bir kutunun bütün yüzlerini kâğıtla kaplamak için yüzey alanını buluruz. Yüzey alanı cm², br² gibi kare birimlerle yazılır.",
                 "akilda": "Kaplamak = yüzey alanı",
                 "sorular": [
                     S("Bir kutuyu paket kâğıdıyla kaplamak için neyi bulmalıyız?", ["Ağırlığını", "Yüzey alanını", "Rengini"], 1,
                       "Kaplamak, bütün yüzlerin üstünü örtmek demek.", "Bütün yüzlerin alanları toplamı yüzey alanıdır."),
                     S("Yüzey alanı hangi birimle yazılır?", ["cm²", "cm", "kg"], 0, "Alan kare birimle yazılır.", "Yüzey alanı bir alandır: cm².")]},
                {"ad": "Saklı küpleri saymak", "sinif": "2. tema, 1. konu", "svg": svg2_sakli(),
                 "anlatim": "Eş küplerden yapılmış bir yapıda öndeki küpler arkadakileri saklar. Küpleri sayarken görünmeyenleri de düşünürüz.",
                 "akilda": "Arkadakileri de say",
                 "sorular": [
                     G("Görseldeki kutu biçimindeki yapı kaç küpten oluşur?", "4", "Öndeki 2 küpün arkasında da küpler var.",
                       "Önde 2, arkada 2 küp: 2 + 2 = 4.", svg=svg_dolu(kutu(2, 2, 1), s=40),
                       yardim={"adimlar": ["Önden kaç küp görünüyor?", "Arkada da aynı sayıda küp var. İkisini topla."]}),
                     G("Görseldeki kutu biçimindeki yapı kaç küpten oluşur?", "6", "Öndeki sıranın arkasında bir sıra daha var.",
                       "Önde 3, arkada 3 küp: 3 + 3 = 6.", svg=svg_dolu(kutu(3, 2, 1), s=36),
                       yardim={"adimlar": ["Önden kaç küp görünüyor?", "Arkada da aynı sayıda küp var. İkisini topla."]})]}
            ]},
        "kavramlar": [
            {"ad": "Hacim", "renk": "#1f9e8f", "svg": svg2_hacim(),
             "aciklama": "Bir cismin uzayda kapladığı yere o cismin hacmi denir. (s. 136)",
             "ek": "Bir kutunun hacmi, içine ne kadar şey sığacağını (kapasitesini) anlatır. Hacmi büyük olan kutuya daha çok şey sığar. (s. 136)",
             "akilda": "Kapladığı yer",
             "soru": S("Bir cismin uzayda kapladığı yere ne denir?", ["Yüzey alanı", "Hacim", "Ayrıt"], 1,
                       "Bilgi kartındaki ilk cümleye bak.", "Bir cismin uzayda kapladığı yere hacim denir. (s. 136)")},
            {"ad": "Kaplamak mı, Doldurmak mı?", "renk": "#b7791f", "svg": svg2_kapla_doldur(),
             "aciklama": "Bir kutunun dışını kaplamak için yüzey alanını, içini doldurmak için hacmini buluruz.",
             "ek": "Yüzey alanı kare birimle (br²), hacim küp birimle (br³) yazılır. Bir problemde ilk sorumuz hep aynı: Kaplamak mı, doldurmak mı?",
             "akilda": "Kapla = alan, doldur = hacim",
             "sende": {"baslik": "Sıra sende",
                       "problem": "Görseldeki kutu, ayrıtı 1 br olan birim küplerle dolu. İçini kaç küp doldurur? Dışını kaplamak için kaç kare gerekir?",
                       "svg": svg_dolu(kutu(2, 2, 1), s=40),
                       "adimlar": [
                           {"metin": "Doldurmak: içindeki küpleri say. Önde 2, arkada 2 küp var.",
                            "soru": G("Kutunun içinde kaç birim küp var?", "4", "Öndeki ve arkadaki küpleri topla.", "2 + 2 = 4 birim küp.",
                                      yardim={"adimlar": ["Önde kaç küp var?", "Arkada da 2 küp var. İkisini topla."]}),
                            "islem": "2 + 2 = 4 → hacim 4 br³"},
                           {"metin": "Kaplamak: dıştaki kareleri say. Üstte 4, altta 4 kare.", "islem": "4 + 4 = 8"},
                           {"metin": "Ön, arka, sağ ve sol yüzlerin her birinde 2 kare var.",
                            "soru": G("4 · 2 kaçtır?", "8", "Dört tane 2'yi topla.", "4 · 2 = 8.",
                                      yardim={"adimlar": ["4 · 2, dört tane 2 demek.", "2 + 2 + 2 + 2"]}),
                            "islem": "4 · 2 = 8"},
                           {"metin": "Bütün kareleri topla.", "islem": "8 + 8 = 16 → yüzey alanı 16 br²"}],
                       "sonuc": "Harika! İçini 4 küp doldurur, dışını 16 kare kaplar. Hacim ile yüzey alanı farklı şeylerdir."},
             "soru": S("Bir akvaryuma kaç kova su sığacağını bulmak istiyoruz. Neyi bulmalıyız?", ["Yüzey alanını", "Çevresini", "Hacmini"], 2,
                       "Su akvaryumun dışını mı kaplar, içini mi doldurur?", "Su akvaryumun içini doldurur. Doldurmak = hacim.")},
            {"ad": "Eş Nesnelerle Ölçme", "renk": "#1d6fa3", "svg": svg2_es_nesne(),
             "aciklama": "Bir kutunun hacmini, içini aralarında boşluk kalmayacak biçimde dolduran eş nesneleri sayarak ölçeriz. (s. 136)",
             "ek": "Dikkat: İki kutuyu karşılaştırırken ikisini de aynı nesnelerle doldurmalıyız. Alper bir kutuda 594 çubuk makarna, ötekinde 495 fiyonk makarna saydı; makarnalar farklı olduğu için bu sayılar karşılaştırılamaz. (s. 135)",
             "akilda": "Aynı nesneyle doldur, say",
             "cozum": {"baslik": "Denge oyunu kutuları",
                       "problem": "Ali ve Filiz'in denge oyunlarındaki tahta parçaların hepsi aynı. Ali her katta 4 parça olacak biçimde 10 kat, Filiz her katta 3 parça olacak biçimde 13 kat yaptı ve yapılarını kutularına yerleştirdi. Hangi kutunun hacmi daha büyük?",
                       "adimlar": [
                           {"metin": "Parçalar eş mi? Evet, hepsi aynı. Öyleyse sayıları karşılaştırabiliriz."},
                           {"metin": "Ali: her katta 4 parça, 10 kat.", "islem": "4 · 10 = 40 parça"},
                           {"metin": "Filiz: her katta 3 parça, 13 kat.", "islem": "3 · 13 = 39 parça"},
                           {"metin": "Karşılaştır.", "islem": "40 > 39"}],
                       "sonuc": "Ali'nin kutusuna daha çok parça sığdı: Ali'nin kutusunun hacmi daha büyük. (s. 136)"},
             "soru": S("Ayşe bir kutuyu bilyelerle, Can başka bir kutuyu pinpon toplarıyla doldurdu. Sayılara bakarak hangi kutunun hacminin büyük olduğunu bulabilir miyiz?",
                       ["Evet, sayısı çok olan büyüktür.", "Evet, sayısı az olan büyüktür.", "Hayır, ikisi de aynı nesneyle doldurulmalı."], 2,
                       "Dikkat kutusunu hatırla: nesneler aynı mı?", "Bilye ve pinpon topu farklı büyüklükte. Karşılaştırmak için iki kutu da aynı eş nesnelerle doldurulmalı. (s. 135)")},
            {"ad": "Birim Küp", "renk": "#7b4fc9", "svg": svg2_birim_kup(),
             "aciklama": "Ayrıt uzunluklarının her biri 1 birim olan küplere birim küp denir. (s. 138)",
             "ek": "Birim küp, hacim ölçmenin cetveli gibidir: herkes aynı küpü kullanınca sonuçlar karşılaştırılabilir.",
             "akilda": "Her ayrıtı 1 birim",
             "soru": S("Birim küpün her bir ayrıtı kaç birimdir?", ["1", "2", "6"], 0, "Adında “birim” var.", "Birim küpün her ayrıtı 1 birimdir. (s. 138)")},
            {"ad": "Birim Küp Cinsinden Hacim", "renk": "#2f8f73", "svg": svg2_say(),
             "aciklama": "Bir prizmanın içini boşluk kalmayacak şekilde dolduran birim küplerin sayısı, prizmanın birim küp cinsinden hacmidir. (s. 138)",
             "ek": "12 birim küp sığan bir prizmanın hacmi 12 br³ diye yazılır (12 birimküp). Saklı küpleri unutmamak için sıra sıra, kat kat say. (s. 137–138)",
             "akilda": "Kaç birim küp sığıyor?",
             "cozum": {"baslik": "Küpleri sayalım",
                       "problem": "Görseldeki prizma birim küplerle dolu. Hacmi kaç br³?",
                       "svg": svg_dolu(kutu(3, 2, 2), s=34),
                       "adimlar": [
                           {"metin": "Alt katta önden bir sıra görünüyor.", "islem": "3 küp"},
                           {"metin": "Arkasında saklı bir sıra daha var.", "islem": "3 + 3 = 6 (alt kat)"},
                           {"metin": "Üstte aynı bir kat daha var.", "islem": "6 + 6 = 12"}],
                       "sonuc": "Prizmanın hacmi 12 br³. (s. 137)"},
             "sende": {"baslik": "Sıra sende",
                       "problem": "Görseldeki prizma birim küplerle dolu. Hacmi kaç br³?",
                       "svg": svg_dolu(kutu(3, 2, 3), s=30, h=180),
                       "adimlar": [
                           {"metin": "Alt kat: önde 3, arkada 3 küp.",
                            "soru": G("Alt katta kaç küp var?", "6", "Öndeki ve arkadaki sırayı topla.", "3 + 3 = 6.",
                                      yardim={"adimlar": ["Önden bir sırada kaç küp var?", "Arkada da aynı sıra var. İkisini topla."]}),
                            "islem": "3 + 3 = 6"},
                           {"metin": "Kaç kat var? Görselde 3 kat.", "islem": "3 kat"},
                           {"metin": "Her katta 6 küp, 3 kat.",
                            "soru": G("6 + 6 + 6 kaçtır?", "18", "Üç tane 6'yı topla.", "6 + 6 + 6 = 18.",
                                      yardim={"adimlar": ["Önce 6 + 6.", "Sonuca bir 6 daha ekle."]}),
                            "islem": "6 + 6 + 6 = 18 br³"}],
                       "sonuc": "Harika! Prizmanın hacmi 18 br³."},
             "soru": G("Görseldeki prizma birim küplerle dolu. Hacmi kaç br³?", "8", "Alt kattaki küpleri say, sonra üst katı ekle.",
                       "Alt katta 2 + 2 = 4, üst katta 4 küp: 4 + 4 = 8 br³. (s. 137)", birim="br³", svg=svg_dolu(kutu(2, 2, 2), s=40),
                       yardim={"adimlar": ["Alt katta önde kaç küp var? Arkada da aynısı var.", "Üst katta da alt kat kadar küp var. İki katı topla."]})},
            {"ad": "Daha Uygun Birim", "renk": "#5f3dc4", "svg": svg2_uygun_birim(),
             "aciklama": "Hacmi ölçerken arada boşluk bırakmayan nesne daha uygun birimdir. Eş küpler kutuyu boşluksuz doldurur. (s. 138)",
             "ek": "Kitaptaki cam kap kutularla doldurulunca arada boşluk kaldı; küplerle doldurulunca hiç boşluk kalmadı. Farklı nesneler farklı sonuç verdi; küp daha uygun birimdir. (s. 138)",
             "akilda": "Boşluk kalmasın: küp kullan",
             "soru": S("Bir kutunun hacmini ölçmek için hangisi en uygun birimdir?", ["Pinpon topu", "Eş küpler", "Farklı boyda taşlar"], 1,
                       "Hangisi arada boşluk bırakmaz ve hepsi aynı mı?", "Toplar arasında boşluk kalır, farklı taşlar eş değil. Eş küpler boşluksuz doldurur. (s. 138)")}
        ],
        "biliyorMusun": ["Japonya'da bazı çiftçiler karpuzları küçükken cam kutulara koyarak kare prizma biçiminde büyütür. Böylece karpuzlar yuvarlanıp düşmez, kamyonda aralarında boşluk kalmaz. (s. 136)"],
        "akildaKalsin": [
            "Hacim, bir cismin uzayda kapladığı yerdir.",
            "Kaplamak = yüzey alanı (br²); doldurmak = hacim (br³).",
            "Hacmi, kutuyu boşluksuz dolduran eş nesneleri sayarak ölçeriz.",
            "Karşılaştırmak için iki kutuyu da aynı nesneyle doldur.",
            "Birim küp: her ayrıtı 1 birim olan küp.",
            "Sığan birim küp sayısı = hacim (br³). Saklı küpleri de say."],
        "merakKutusu": [
            {"soru": "Makarnaları saymak neden işe yaramadı?", "cevap": "Çubuk makarna ile fiyonk makarna farklı büyüklükte. Farklı nesnelerle sayınca hangi kutunun büyük olduğu kesin bilinemez; ikisi de aynı nesneyle doldurulmalı. (s. 135)"},
            {"soru": "Pinpon topu neden iyi bir birim değil?", "cevap": "Topların arasında boşluk kalır. Hacmi doğru ölçmek için boşluk bırakmayan eş küpler kullanılır. (s. 138)"},
            {"soru": "Bir kutuya 10 büyük küp sığıyorsa hacmi 10 br³ mü?", "cevap": "Yalnızca küplerin ayrıtı 1 birimse. Kitapta ayrıtı 2 birim olan 10 küp bir prizmayı dolduruyor. Böyle bir küpün içine 2 · 2 · 2 = 8 birim küp sığar; prizmanın hacmi 10 · 8 = 80 br³ olur. (s. 137)"},
            {"soru": "br³ nasıl okunur?", "cevap": "“Birimküp” diye okunur. Hacim, kaç birim küp sığdığını söyler. (s. 137–138)"}],
        "dusunVeYaz": [{"soru": "Deniz bir kutuya 20 bilye, Ece başka bir kutuya 15 küp yerleştirdi. Deniz “Benim kutumun hacmi daha büyük.” dedi. Haklı mı? Neden?",
                        "ornekCevap": "Bilemeyiz. Kutular farklı nesnelerle doldurulmuş. Karşılaştırmak için iki kutu da aynı eş nesnelerle doldurulmalı. Ayrıca bilyelerin arasında boşluk kalır.",
                        "anahtarlar": ["aynı", "eş", "bilemeyiz", "farklı", "boşluk"]}],
        "sorular": [
            G("Görseldeki prizma birim küplerle dolu. Hacmi kaç br³?", "6",
              "Önden görünen sıranın arkasında bir sıra daha var.", "Önde 3, arkada 3 küp: 3 + 3 = 6 br³. (s. 137)",
              birim="br³", svg=svg_dolu(kutu(3, 2, 1), s=40), kavram="Birim Küp Cinsinden Hacim",
              yardim={"adimlar": ["Kaplamak mı, doldurmak mı? İçini dolduran küpleri sayıyoruz.", "Önden bir sırada kaç küp var?", "Arkada saklı bir sıra daha var.", "İki sırayı topla."]}),
            S("Hacim neyi anlatır?", ["Bir cismin yüzlerinin alanını", "Bir cismin ayrıtlarının sayısını", "Bir cismin kapladığı yeri"], 2,
              "Hacim kutunun içiyle mi ilgili, dışıyla mı?", "Hacim, bir cismin uzayda kapladığı yerdir. (s. 136)", kavram="Hacim"),
            S("Hangisinde hacmi bulmamız gerekir?", ["Kutuyu paket kâğıdıyla kaplamak", "Kutuya kaç oyuncak sığacağını bulmak", "Kutunun bir kenarını ölçmek"], 1,
              "Kaplamak mı, doldurmak mı?", "Oyuncaklar kutunun içini doldurur. Doldurmak = hacim.", kavram="Kaplamak mı, Doldurmak mı?"),
            G("Görseldeki prizma birim küplerle dolu. Hacmi kaç br³?", "12",
              "Alt katı say, sonra kaç kat olduğuna bak.", "Alt katta 2 + 2 = 4 küp. 3 kat var: 4 + 4 + 4 = 12 br³. (s. 137)",
              birim="br³", svg=svg_dolu(kutu(2, 2, 3), s=34, h=180), kavram="Birim Küp Cinsinden Hacim",
              yardim={"adimlar": ["Kaplamak mı, doldurmak mı? İçindeki küpleri sayıyoruz.", "Alt katta önde kaç küp var? Arkada da aynısı var.", "Kaç kat var?", "Her katta aynı sayıda küp var: katları topla."]}),
            S("Ece iki kutunun hacmini karşılaştırmak istiyor. Ne yapmalı?",
              ["İkisini de aynı eş küplerle doldurup küpleri saymalı.", "Birini bilyeyle, diğerini küple doldurmalı.", "Yalnızca kutuların rengine bakmalı."], 0,
              "Dikkat kutusu: nesneler aynı olmalı.", "Karşılaştırmak için iki kutu da aynı eş nesnelerle doldurulmalı. (s. 135)", kavram="Eş Nesnelerle Ölçme"),
            S("Mert kutusuna her katta 6 tahta olacak biçimde 5 kat, Elif aynı tahtalardan her katta 4 tane olacak biçimde 8 kat yerleştirdi. Kutular tam doldu. Hangi kutunun hacmi daha büyük?",
              ["Mert'in", "Elif'in", "İkisi eşit"], 1,
              "Tahtalar aynı. Her kutuya kaç tahta sığdığını bul.", "Mert 6 · 5 = 30, Elif 4 · 8 = 32 tahta. 32 > 30: Elif'in kutusu daha büyük. (s. 136)",
              kavram="Eş Nesnelerle Ölçme",
              yardim={"adimlar": ["Tahtalar eş mi? Evet: sayıları karşılaştırabiliriz.", "Mert: 6 · 5.", "Elif: 4 · 8.", "İki sayıyı karşılaştır."]}),
            S("Birim küp hangisidir?", ["Her ayrıtı 2 birim olan küp", "Bir yüzü 1 birim olan dikdörtgen", "Her ayrıtı 1 birim olan küp"], 2,
              "Adında “birim” var.", "Ayrıtlarının her biri 1 birim olan küpe birim küp denir. (s. 138)", kavram="Birim Küp"),
            G("Bir kutuya her sırada 5 birim küp olacak şekilde 3 sıra dizildi ve kutu tek katla tamamen doldu. Kutunun hacmi kaç br³?", "15",
              "Sıra sayısını bir sıradaki küp sayısıyla çarp.", "3 · 5 = 15 birim küp: hacim 15 br³. (s. 138)", birim="br³", kavram="Birim Küp Cinsinden Hacim",
              yardim={"adimlar": ["Kaplamak mı, doldurmak mı? Kutuyu dolduran küpleri sayıyoruz.", "Bir sırada kaç küp, kaç sıra var?", "Sıra sayısını bir sıradaki küp sayısıyla çarp."]}),
            S("Cam bir kap bir kez kibrit kutularıyla, bir kez eş küplerle dolduruldu. Kutularla doldurunca arada boşluk kaldı. Hacmi ölçmek için hangisi daha uygun?",
              ["Eş küpler", "Kibrit kutuları", "İkisi de aynı sonucu verir"], 0,
              "Hangisi boşluk bırakmadı?", "Küpler boşluksuz doldurur; boşluk kalırsa hacim yanlış ölçülür. (s. 138)", kavram="Daha Uygun Birim"),
            S("Görseldeki kutu birim küplerle dolu. Hangisi doğrudur?",
              ["Hacmi 4 br³, yüzey alanı 16 br²", "Hacmi 16 br³, yüzey alanı 4 br²", "Hacmi ile yüzey alanı aynı sayıdır"], 0,
              "İçindeki küpleri say (hacim), dıştaki kareleri say (yüzey alanı).",
              "İçinde 4 küp: 4 br³. Dışta üst 4, alt 4, dört yan yüzde 2'şer kare: 16 br².",
              svg=svg_dolu(kutu(2, 2, 1), s=40), kavram="Kaplamak mı, Doldurmak mı?",
              yardim={"adimlar": ["Doldurmak = hacim: içindeki küpleri say.", "Kaplamak = yüzey alanı: üstteki ve alttaki kareleri say.", "Dört yan yüzdeki kareleri ekle."]})]
    }


# =================================================================
def u2k5():
    return {
        "id": "u2k5", "unite": T2, "baslik": "Dikdörtgenler Prizmasının Hacmi", "sayfalar": "s. 138–143",
        "giris": "Büyük bir kutudaki birim küpleri tek tek saymak çok uzun sürer. Bu konuda küpleri saymadan, ayrıtları çarparak hacmi bulmayı öğreneceğiz.",
        "hazirlik": {
            "baslik": "Hazır mısın?",
            "giris": "Bu konuda üç sayıyı çarpacağız. Önce çarpmayı ve üssü hatırlıyor musun bakalım. Not yok.",
            "maddeler": [
                {"ad": "Üç sayıyı çarpma", "sinif": "Önceki yıllar", "svg": svg2_h_uc_carp(),
                 "anlatim": "Üç sayıyı çarparken önce ikisini çarparız, çıkan sonucu üçüncüyle çarparız. Hangi ikisiyle başladığımız sonucu değiştirmez.",
                 "akilda": "İkisini çarp, sonra üçüncüyle",
                 "ornek": {"problem": "2 · 3 · 4 kaçtır?", "adimlar": [
                     {"metin": "Önce ilk iki sayıyı çarp.", "islem": "2 · 3 = 6"},
                     {"metin": "Sonucu üçüncü sayıyla çarp.", "islem": "6 · 4 = 24"}]},
                 "sorular": [
                     G("3 · 2 · 5 kaçtır?", "30", "Önce 3 · 2, sonra 5 ile çarp.", "3 · 2 = 6, 6 · 5 = 30.",
                       yardim={"adimlar": ["Önce 3 · 2.", "Sonucu 5 ile çarp."]}),
                     G("4 · 5 · 2 kaçtır?", "40", "Önce 4 · 5, sonra 2 ile çarp.", "4 · 5 = 20, 20 · 2 = 40.",
                       yardim={"adimlar": ["Önce 4 · 5.", "Sonucu 2 ile çarp."]})]},
                {"ad": "Ondalık sayıyla çarpma", "sinif": "1. tema, 9. konu", "svg": svg2_h_ondalik(),
                 "anlatim": "2,5 · 4 işleminde 2,5'i 4 kere toplarız: 2,5 + 2,5 + 2,5 + 2,5 = 10. Ya da virgül yokmuş gibi çarparız (25 · 4 = 100), sonra virgülden sonra 1 basamak ayırırız: 10,0 = 10.",
                 "akilda": "Çarp, sonra virgülü yerleştir",
                 "sorular": [
                     G("1,5 · 4 kaçtır?", "6", "1,5'i 4 kere topla.", "1,5 + 1,5 + 1,5 + 1,5 = 6.", denk=True,
                       yardim={"adimlar": ["1,5 · 4, dört tane 1,5 demek.", "İki tane 1,5 = 3. Dört tanesi kaç?"]}),
                     S("0,5 · 6 kaçtır?", ["3", "30", "0,3"], 0, "0,5 yarım demek. 6'nın yarısı kaç?", "0,5 · 6 = 3.")]},
                {"ad": "Üslü ifade", "sinif": "1. tema, 10. konu", "svg": svg2_h_us(),
                 "anlatim": "3[[u:3]], 3'ün 3 kere kendisiyle çarpılması demektir: 3 · 3 · 3 = 27.",
                 "akilda": "a³ = a · a · a",
                 "sorular": [
                     G("2[[u:3]] kaçtır?", "8", "2'yi 3 kere çarp.", "2 · 2 · 2 = 8.",
                       yardim={"adimlar": ["2[[u:3]] = 2 · 2 · 2.", "Önce 2 · 2, sonra sonucu 2 ile çarp."]}),
                     S("4[[u:3]] hangisine eşittir?", ["4 · 3", "4 · 4 · 4", "4 + 4 + 4"], 1, "Üs, tabanın kaç kere çarpıldığını söyler.", "4[[u:3]] = 4 · 4 · 4 = 64.")]}
            ]},
        "kavramlar": [
            {"ad": "Katman", "renk": "#1f9e8f", "svg": svg2_katman(),
             "aciklama": "Prizmanın tabanına dizilen birim küpler bir katman oluşturur. Bir katmandaki küp sayısı ile katman sayısını çarparak bütün küpleri buluruz. (s. 139)",
             "ek": "Ahmet tabana 10 birim küp dizdi; prizma 3 katmanla doldu: 10 · 3 = 30. Ceren ve Mehmet küpleri başka yüzlere dizdi ama sonuç yine 30 çıktı. (s. 139)",
             "akilda": "Bir kat × kat sayısı",
             "cozum": {"baslik": "Ahmet'in prizması",
                       "problem": "Prizmanın tabanında 5 sütun ve 2 sıra birim küp var; prizma 3 katmanla doluyor. Kaç birim küp sığar?",
                       "svg": katman_svg(5, 2, 3, s=24),
                       "adimlar": [
                           {"metin": "Taban katmanı: 5 sütun, 2 sıra.", "islem": "5 · 2 = 10 küp"},
                           {"metin": "Kaç katman var?", "islem": "3 katman"},
                           {"metin": "Bir katmanı katman sayısıyla çarp.", "islem": "10 · 3 = 30"}],
                       "sonuc": "Prizmaya 30 birim küp sığar: hacmi 30 br³. (s. 139)"},
             "soru": G("Bir prizmanın taban katmanında 8 birim küp var ve prizma 4 katmanla doluyor. Hacmi kaç br³?", "32",
                       "Bir katmandaki küp sayısını katman sayısıyla çarp.", "8 · 4 = 32 br³. (s. 139)", birim="br³",
                       yardim={"adimlar": ["Bir katmanda kaç küp var? Kaç katman var?", "İkisini çarp."]})},
            {"ad": "Hacim Formülü", "renk": "#7b4fc9", "svg": svg2_formul_hacim(),
             "aciklama": "Dikdörtgenler prizmasının hacmi = taban alanı × yükseklik = a · b · c. Önce tabanın iki dik ayrıtı çarpılır (taban alanı), sonra yükseklikle çarpılır. (s. 140)",
             "ek": "Hangi yüzü taban seçersek seçelim sonuç değişmez: (a · b) · c = (b · c) · a = (a · c) · b. (s. 140)",
             "akilda": "En × boy × yükseklik",
             "cozum": {"baslik": "Formülle hacim",
                       "problem": "Ayrıtları 6 br, 4 br ve 5 br olan dikdörtgenler prizmasının hacmini bulalım.",
                       "svg": svg_prizma_et("6 br", "4 br", "5 br", A=120, B=80, C=100, h=170),
                       "adimlar": [
                           {"metin": "Kaplamak mı, doldurmak mı? Doldurmak: hacim."},
                           {"metin": "Taban alanı: tabanın iki dik ayrıtını çarp.", "islem": "6 · 4 = 24 br²"},
                           {"metin": "Taban alanını yükseklikle çarp.", "islem": "24 · 5 = 120"}],
                       "sonuc": "Prizmanın hacmi 120 br³. (s. 140)"},
             "sende": {"baslik": "Sıra sende",
                       "problem": "Ayrıtları 10 br, 4 br ve 2 br olan dikdörtgenler prizmasının hacmini bul.",
                       "svg": svg_prizma_et("10 br", "4 br", "2 br", A=150, B=70, C=50, h=130),
                       "adimlar": [
                           {"metin": "Taban alanı: 10 · 4.",
                            "soru": G("10 · 4 kaçtır?", "40", "10 ile çarpınca sonuna 0 eklenir.", "10 · 4 = 40.",
                                      yardim={"adimlar": ["4'ü 10 ile çarp.", "10 ile çarpınca sayının sonuna bir 0 eklenir."]}),
                            "islem": "10 · 4 = 40 br²"},
                           {"metin": "Taban alanını yükseklikle çarp.",
                            "soru": G("40 · 2 kaçtır?", "80", "40'ı iki kere topla.", "40 + 40 = 80.",
                                      yardim={"adimlar": ["40 · 2, iki tane 40 demek.", "40 ile 40'ı topla."]}),
                            "islem": "40 · 2 = 80 br³"}],
                       "sonuc": "Harika! Prizmanın hacmi 80 br³."},
             "soru": S("Ayrıtları a, b ve c olan dikdörtgenler prizmasının hacmi hangisidir?", ["a + b + c", "2 · (a · b + a · c + b · c)", "a · b · c"], 2,
                       "Taban alanını (a · b) yükseklikle çarp.", "Hacim = (a · b) · c = a · b · c. Öbür ifade yüzey alanıdır. (s. 140)")},
            {"ad": "Kare Prizma ve Küp", "renk": "#e8590c", "svg": svg2_kup_hacim(),
             "aciklama": "Kare prizma ve küp, dikdörtgenler prizmasının özel hâlleridir; hacimleri aynı bağıntıyla bulunur. Küpün bir ayrıtı a ise hacmi a · a · a = a[[u:3]]. (s. 142)",
             "ek": "Kare prizma: taban 2 br × 2 br, yükseklik 4 br → 4 · 4 = 16 br³. Küp: taban 3 br × 3 br, yükseklik 3 br → 9 · 3 = 27 br³. (s. 142)",
             "akilda": "Küp: a · a · a = a³",
             "cozum": {"baslik": "Küpün hacmi",
                       "problem": "Bir ayrıtı 3 br olan küpün hacmini bulalım.",
                       "svg": svg_prizma_et("3 br", "3 br", "3 br", A=80, B=80, C=80, h=160),
                       "adimlar": [
                           {"metin": "Taban bir kare: 3 · 3.", "islem": "3 · 3 = 9 br²"},
                           {"metin": "Yükseklik de 3 br.", "islem": "9 · 3 = 27"},
                           {"metin": "Üsle kısaca yazarız.", "islem": "3[[u:3]] = 27"}],
                       "sonuc": "Küpün hacmi 27 br³. (s. 142)"},
             "soru": G("Bir ayrıtı 4 br olan küpün hacmi kaç br³?", "64", "Küpün üç ayrıtı da 4 br: 4 · 4 · 4.",
                       "4 · 4 = 16, 16 · 4 = 64 br³. (s. 142)", birim="br³",
                       yardim={"adimlar": ["Küpün üç ayrıtı eşit: 4 · 4 · 4.", "Önce 4 · 4, sonra sonucu 4 ile çarp."]})},
            {"ad": "Hacim Birimi br³", "renk": "#b7791f", "svg": svg2_br3(),
             "aciklama": "Hacimde üç ayrıt çarpıldığı için birim de üç kez çarpılır: br · br · br = br³. (s. 142)",
             "ek": "Uzunluk br, alan br², hacim br³ ile yazılır. br³ “birimküp” diye okunur. (s. 138, 142)",
             "akilda": "Uzunluk br, alan br², hacim br³",
             "soru": S("Bir prizmanın hacmi hangisi gibi yazılır?", ["24 br", "24 br³", "24 br²"], 1,
                       "Hacimde kaç ayrıt çarpılır?", "Üç ayrıt çarpıldığı için hacim br³ ile yazılır. (s. 142)")},
            {"ad": "Aynı Hacim, Farklı Prizma", "renk": "#2f8f73", "svg": svg2_ayni_hacim(),
             "aciklama": "18 eş küple birbirinden farklı prizmalar yapılabilir. Şekilleri farklı olsa da hepsinin hacmi 18 küptür. (s. 141)",
             "ek": "18 küple yapılan prizmaların ayrıtları: 1, 1, 18 · 1, 2, 9 · 1, 3, 6 · 2, 3, 3. Üç sayının çarpımı hep 18. (s. 141)",
             "akilda": "Şekil değişir, küp sayısı aynı",
             "sende": {"baslik": "Sıra sende",
                       "problem": "Hacmi 24 br³ olan bir prizmanın tabanı 4 br ve 3 br. Yüksekliği kaç br?",
                       "adimlar": [
                           {"metin": "Taban alanı: 4 · 3.",
                            "soru": G("4 · 3 kaçtır?", "12", "4'ü 3 kere topla.", "4 · 3 = 12.",
                                      yardim={"adimlar": ["4 · 3, üç tane 4 demek.", "4 + 4 + 4"]}),
                            "islem": "4 · 3 = 12 br²"},
                           {"metin": "Taban alanı × yükseklik = 24. 12'yi hangi sayıyla çarpınca 24 olur?",
                            "soru": G("12 · ? = 24. Soru işaretinin yerine hangi sayı gelir?", "2", "12'yi kaç kere toplayınca 24 olur?", "12 · 2 = 24.",
                                      yardim={"adimlar": ["12 + 12 kaç eder?", "Kaç tane 12 topladın?"]}),
                            "islem": "12 · 2 = 24"}],
                       "sonuc": "Harika! Prizmanın yüksekliği 2 br."},
             "soru": S("Hangisi 18 eş birim küpten yapılmış bir prizmanın ayrıtları olabilir?", ["2 br, 3 br, 3 br", "2 br, 2 br, 3 br", "3 br, 3 br, 3 br"], 0,
                       "Üç sayıyı çarp: hangisi 18 ediyor?", "2 · 3 · 3 = 18. Öbürleri 12 ve 27. (s. 141)")},
            {"ad": "Ayrıt Değişince Hacim", "renk": "#c92a2a", "svg": svg2_iki_kat(),
             "aciklama": "Bir ayrıt 2 katına çıkarsa hacim de 2 katına çıkar. Üç ayrıtın hepsi 2 katına çıkarsa hacim 2 · 2 · 2 = 8 katına çıkar. (s. 143)",
             "ek": "Örnek: 2 · 3 · 4 = 24 br³. Yükseklik 8 br olursa 2 · 3 · 8 = 48 br³, yani 2 katı. Bir ayrıtı 2 katına çıkarıp başka bir ayrıtı yarıya indirirsek hacim değişmez. (s. 143)",
             "akilda": "Bir ayrıt 2 kat → hacim 2 kat",
             "cozum": {"baslik": "Bütün ayrıtlar 2 katı",
                       "problem": "Ayrıtları 1 br, 2 br ve 3 br olan prizmanın bütün ayrıtları 2 katına çıkarıldı. Hacmi kaç katına çıktı?",
                       "adimlar": [
                           {"metin": "İlk hacim.", "islem": "1 · 2 · 3 = 6"},
                           {"metin": "Yeni ayrıtlar 2 br, 4 br ve 6 br.", "islem": "2 · 4 · 6 = 48"},
                           {"metin": "Kaç katı? Büyüğü küçüğe böl.", "islem": "48 ÷ 6 = 8"}],
                       "sonuc": "Bütün ayrıtlar 2 katı olunca hacim 8 katı oldu: 2 · 2 · 2 = 8. (s. 143)"},
             "soru": S("Bir prizmanın yalnızca yüksekliği 2 katına çıkarılırsa hacmi ne olur?", ["Değişmez", "2 katına çıkar", "8 katına çıkar"], 1,
                       "Hacim = taban alanı × yükseklik. Taban aynı kaldı.", "Taban alanı aynı, yükseklik 2 katı: hacim de 2 katı. (s. 143)")}
        ],
        "akildaKalsin": [
            "Bir katmandaki küp sayısı × katman sayısı = birim küp sayısı.",
            "Hacim = taban alanı × yükseklik = a · b · c.",
            "Hangi yüz taban olursa olsun hacim aynı çıkar.",
            "Küpün hacmi a · a · a = a³.",
            "Hacim br³ ile yazılır: br · br · br.",
            "Bir ayrıt 2 katı → hacim 2 katı; üç ayrıt 2 katı → hacim 8 katı."],
        "merakKutusu": [
            {"soru": "Neden önce tabanı çarpıyoruz?", "cevap": "Taban alanı, bir katmandaki birim küp sayısını verir. Yükseklik ise kaç katman olduğunu söyler. İkisini çarpınca bütün küpler çıkar. (s. 140)"},
            {"soru": "Birim küpler uzunluk ölçer mi?", "cevap": "Hayır, birim küp hacim ölçer. Ama bir ayrıt boyunca dizilen küpler ayrıtın uzunluğu hakkında, tabandaki küpler de taban alanı hakkında fikir verir. (s. 140)"},
            {"soru": "Farklı görünen yapıların hacmi eşit olabilir mi?", "cevap": "Evet. Aynı sayıda eş küpten yapılan yapıların biçimi farklı olsa da hacimleri eşittir. (s. 141)"},
            {"soru": "Küpün ayrıtı 3 katına çıkarsa hacmi de 3 katına mı çıkar?", "cevap": "Hayır. Üç ayrıt da 3 katına çıkar: hacim 3 · 3 · 3 = 27 katına çıkar. (s. 143)"}],
        "dusunVeYaz": [{"soru": "Ece, ayrıtları 2 br, 3 br ve 5 br olan prizmanın hacmini 2 + 3 + 5 = 10 br³ buldu. Hatası ne? Doğru sonucu bul.",
                        "ornekCevap": "Ece ayrıtları topladı. Hacim için ayrıtlar çarpılır: 2 · 3 · 5 = 30 br³.",
                        "anahtarlar": ["çarp", "topla", "30"]}],
        "sorular": [
            G("Ayrıtları 5 br, 3 br ve 4 br olan dikdörtgenler prizmasının hacmi kaç br³?", "60",
              "Taban alanını bul, yükseklikle çarp.", "Taban alanı 5 · 3 = 15 br². 15 · 4 = 60 br³. (s. 140)",
              birim="br³", svg=svg_prizma_et("5 br", "3 br", "4 br", A=120, B=70, C=90, h=160), kavram="Hacim Formülü",
              yardim={"adimlar": ["Kaplamak mı, doldurmak mı? Doldurmak: hacim.", "Ölçüler: 5 br, 3 br, 4 br. Birimler aynı.", "Formül: taban alanı × yükseklik. Önce 5 · 3.", "Taban alanını 4 ile çarp."]}),
            G("Görseldeki prizma birim küplerle dolu. Alt katman altın renkli. Prizmanın hacmi kaç br³?", "24",
              "Alt katmandaki küpleri say, katman sayısıyla çarp.", "Alt katman 4 · 3 = 12 küp. 2 katman: 12 · 2 = 24 br³. (s. 139)",
              birim="br³", svg=katman_svg(4, 3, 2, s=26), kavram="Katman",
              yardim={"adimlar": ["Kaplamak mı, doldurmak mı? Hacim: içindeki küpler.", "Alt katman: önde kaç sütun, kaç sıra var?", "Kaç katman var?", "Bir katmanı katman sayısıyla çarp."]}),
            S("Bir ayrıtı 5 br olan küpün hacmi kaç br³'tür?", ["15", "125", "25"], 1,
              "Küpün üç ayrıtı eşit: 5 · 5 · 5.", "5 · 5 = 25, 25 · 5 = 125 br³. (s. 142)", kavram="Kare Prizma ve Küp"),
            S("Taban alanı 12 br², yüksekliği 5 br olan prizmanın hacmi hangisidir?", ["60 br³", "60 br²", "17 br³"], 0,
              "Hacim = taban alanı × yükseklik; birimi br³.", "12 · 5 = 60. Hacim br³ ile yazılır: 60 br³. (s. 142)", kavram="Hacim Birimi br³"),
            G("Hacmi 40 br³ olan bir prizmanın taban alanı 8 br²'dir. Yüksekliği kaç br?", "5",
              "Taban alanı × yükseklik = hacim. 8 ile hangi sayıyı çarpınca 40 olur?", "8 · 5 = 40: yükseklik 5 br. (s. 140)",
              birim="br", kavram="Hacim Formülü",
              yardim={"adimlar": ["Kaplamak mı, doldurmak mı? Hacim verilmiş.", "Formül: taban alanı × yükseklik = hacim.", "8 · ? = 40. 8'i kaç kere toplayınca 40 olur?"]}),
            S("Hangisi 18 eş birim küpten yapılmış bir prizmanın ayrıtları olamaz?", ["1 br, 2 br, 9 br", "2 br, 3 br, 3 br", "2 br, 2 br, 4 br"], 2,
              "Her birinde üç sayıyı çarp.", "1 · 2 · 9 = 18, 2 · 3 · 3 = 18, ama 2 · 2 · 4 = 16. (s. 141)", kavram="Aynı Hacim, Farklı Prizma"),
            S("Ayrıtları 3 br, 4 br ve 5 br olan bir prizmanın yalnızca yüksekliği 2 katına çıkarıldı. Yeni hacim kaç br³?", ["120", "60", "480"], 0,
              "Önce eski hacmi bul. Yükseklik 2 katı olunca hacim ne olur?", "Eski hacim 3 · 4 · 5 = 60 br³. Yükseklik 2 katı: 60 · 2 = 120 br³. (s. 143)",
              kavram="Ayrıt Değişince Hacim",
              yardim={"adimlar": ["Eski hacim: 3 · 4 · 5.", "Yalnızca bir ayrıt 2 katı oldu: hacim de 2 katı olur.", "Eski hacmi 2 ile çarp."]}),
            G("Bir kutunun tabanı 2,5 br ve 4 br, yüksekliği 3 br'dir. Hacmi kaç br³?", "30",
              "Taban alanı 2,5 · 4. Sonra 3 ile çarp.", "2,5 · 4 = 10 br². 10 · 3 = 30 br³. (s. 140)", birim="br³", denk=True, kavram="Hacim Formülü",
              yardim={"adimlar": ["Kaplamak mı, doldurmak mı? Doldurmak: hacim.", "Taban alanı: 2,5 · 4. Dört tane 2,5'i topla.", "Taban alanını yükseklikle (3) çarp."]}),
            S("Bir küpün bütün ayrıtları 2 katına çıkarılırsa hacmi kaç katına çıkar?", ["2", "4", "8"], 2,
              "Üç ayrıt da 2 katı oluyor.", "Üç ayrıt 2 katı: 2 · 2 · 2 = 8 katı. (s. 143)", kavram="Ayrıt Değişince Hacim"),
            G("Ayrıtı 1 br olan birim küplerle bir ayrıtı 3 br olan küp yapılacak. Kaç birim küp gerekir?", "27",
              "Küpün hacmini bul: 3 · 3 · 3.", "Bir katmanda 3 · 3 = 9 küp, 3 katman: 27 birim küp. (s. 142)", kavram="Kare Prizma ve Küp",
              yardim={"adimlar": ["Kaplamak mı, doldurmak mı? Doldurmak: hacim.", "Bir katmanda 3 · 3 küp var.", "Kaç katman var? Bir katmanı katman sayısıyla çarp."]})]
    }


# =================================================================
def u2t2():
    return {
        "id": "u2t2", "tur": "tarama", "unite": T2,
        "baslik": "Ara Durak 2: Hacim", "sayfalar": "Konu 4–5 · s. 134–143",
        "giris": "Hacim konularını bitirdin, tebrikler! Kısa bir mola verip birim küpleri ve hacim formülünü birlikte gözden geçireceğiz. Önce özetleri oku ve kartları çevir, sonra tarama testini çöz. Not yok.",
        "buyukResim": "Önce bir kutunun hacmini, içini dolduran birim küpleri sayarak bulduk. Sonra saymayı kısalttık: bir katmandaki küp sayısını katman sayısıyla çarptık. Bu da hacim formülünü verdi: a · b · c. Unutma: yüzey alanı kaplar, hacim doldurur!",
        "kapsar": ["u2k4", "u2k5"],
        "hatirla": [
            {"konu": "u2k4", "maddeler": [
                "Hacim, cismin kapladığı yerdir; kutuyu boşluksuz dolduran eş nesneleri sayarak ölçülür.",
                "Karşılaştırmak için aynı nesneyle doldur; en uygun birim birim küptür.",
                "Kaplamak = yüzey alanı (br²), doldurmak = hacim (br³)."]},
            {"konu": "u2k5", "maddeler": [
                "Bir katmandaki küp × katman sayısı = hacim.",
                "Hacim = taban alanı × yükseklik = a · b · c; küpte a³.",
                "Bir ayrıt 2 katı → hacim 2 katı; üçü 2 katı → 8 katı."]}],
        "eskiSoru": 4,
        "oyunKavram": 8,
        "gruplar": [{"soru": "Bu bilgi hangi konudan?", "kutular": [
            {"etiket": "Birim küple ölçme", "uyeler": ["Hacim", "Birim Küp", "Eş Nesnelerle Ölçme"]},
            {"etiket": "Hacim formülü", "uyeler": ["Hacim Formülü", "Katman", "Kare Prizma ve Küp"]}]}],
        "sorular": [
            G("Görseldeki prizma birim küplerle dolu. Alt katmanı say, sonra katman sayısıyla çarp. Hacmi kaç br³?", "12",
              "Alt katmanda önde 3, arkada 3 küp var.", "Alt katman 3 · 2 = 6 küp. 2 katman: 6 · 2 = 12 br³.",
              birim="br³", svg=katman_svg(3, 2, 2, s=34),
              kaynak=[K("u2k4", "Birim Küp Cinsinden Hacim"), K("u2k5", "Katman")],
              yardim={"adimlar": ["Kaplamak mı, doldurmak mı? Doldurmak: hacim.", "Alt katman: önde kaç küp, arkada kaç küp?", "Kaç katman var?", "Bir katmanı katman sayısıyla çarp."]}),
            S("Ayrıtları 3 br, 2 br ve 2 br olan bir kutu için hangisi doğrudur?",
              ["Kutunun içini 12 birim küp doldurur.", "Kutunun içini 32 birim küp doldurur.", "Kutuyu kaplamak için 12 kare yeter."], 0,
              "Doldurmak = hacim (3 · 2 · 2). Kaplamak = yüzey alanı.",
              "Hacim 3 · 2 · 2 = 12 br³: içini 12 küp doldurur. Yüzey alanı 2 · (6 + 6 + 4) = 32 br²: kaplamak için 32 kare gerekir.",
              kaynak=[K("u2k4", "Kaplamak mı, Doldurmak mı?"), K("u2k5", "Hacim Formülü")],
              yardim={"adimlar": ["Doldurmak = hacim: 3 · 2 · 2.", "Kaplamak = yüzey alanı: bütün yüzlerin alanı.", "Her şıkta “doldurmak” mı, “kaplamak” mı yazıyor, kontrol et."]}),
            G("Bir eczacı eş ilaç kutularını rafa yerleştirdi: tabanda 4 sıra, her sırada 6 kutu var ve 2 kat dizdi. Raf boşluk kalmadan doldu. Raf kaç ilaç kutusu alıyor?", "48",
              "Bir katmandaki kutu sayısını bul, kat sayısıyla çarp.", "Bir katman 4 · 6 = 24 kutu. 2 kat: 24 · 2 = 48 kutu. Rafın kapasitesi 48 ilaç kutusu. (s. 137)",
              kaynak=[K("u2k4", "Eş Nesnelerle Ölçme"), K("u2k5", "Katman")],
              yardim={"adimlar": ["Kaplamak mı, doldurmak mı? Raf kutularla doluyor: hacim.", "Bir katta kaç kutu? 4 sıra, her sırada 6 kutu.", "Kaç kat var?", "Bir katı kat sayısıyla çarp."]}),
            S("Görseldeki üç yapı birim küplerle dolu prizmalardır. Hangi ikisinin hacmi eşittir?",
              ["1. ve 2. yapı", "1. ve 3. yapı", "2. ve 3. yapı"], 1,
              "Her yapıda bir katmanı say, katman sayısıyla çarp.",
              "1. yapı 3 · 2 · 2 = 12, 2. yapı 2 · 2 · 2 = 8, 3. yapı 6 · 1 · 2 = 12 br³. Biçimleri farklı ama 1. ve 3. yapının hacmi eşit.",
              svg=sec_svg([yapi_cizimi(kutu(3, 2, 2), 14), yapi_cizimi(kutu(2, 2, 2), 14), yapi_cizimi(kutu(6, 1, 2), 14)], h=160),
              kaynak=[K("u2k4", "Birim Küp Cinsinden Hacim"), K("u2k5", "Aynı Hacim, Farklı Prizma")],
              yardim={"adimlar": ["1. yapı: bir katmanda kaç küp, kaç katman?", "2. ve 3. yapı için de aynısını yap.", "Hangi iki sayı eşit?"]}),
            G("Ela'nın kutusunun tabanı 6 br ve 5 br, yüksekliği 2 br. Kutuyu ayrıtı 1 br olan küp şekerlerle boşluk kalmadan dolduracak. Kaç şeker gerekir?", "60",
              "Her küp şeker bir birim küp. Kutunun hacmini bul.", "Taban alanı 6 · 5 = 30. 30 · 2 = 60 br³: 60 şeker gerekir.",
              kaynak=[K("u2k4", "Birim Küp"), K("u2k5", "Hacim Formülü")],
              yardim={"adimlar": ["Kaplamak mı, doldurmak mı? Doldurmak: hacim.", "Küp şekerin ayrıtı 1 br: her şeker bir birim küp.", "Taban alanı: 6 · 5.", "Taban alanını yükseklikle çarp."]}),
            S("Mert iki kutuyu aynı eş küplerle doldurdu. Birinci kutunun ayrıtları 4 br, 3 br, 2 br; ikinci kutununki 2 br, 2 br, 5 br. Hangisinin hacmi daha büyük?",
              ["İkisi eşit", "Birinci kutunun", "İkinci kutunun"], 1,
              "İki kutunun hacmini ayrı ayrı bul.", "Birinci 4 · 3 · 2 = 24 br³, ikinci 2 · 2 · 5 = 20 br³. 24 > 20.",
              kaynak=[K("u2k4", "Eş Nesnelerle Ölçme"), K("u2k5", "Hacim Formülü")],
              yardim={"adimlar": ["Küpler aynı: hacimleri karşılaştırabiliriz.", "Birinci kutu: 4 · 3 · 2.", "İkinci kutu: 2 · 2 · 5. İki sonucu karşılaştır."]}),
            S("Küp şeklindeki küçük bir kutunun ayrıtı 2 br, büyük bir kutunun ayrıtı 4 br. Büyük kutuya küçük kutulardan kaç tane sığar?", ["2", "4", "8"], 2,
              "İki kutunun hacmini bul; büyüğü küçüğe böl.",
              "Küçük kutu 2 · 2 · 2 = 8 br³, büyük kutu 4 · 4 · 4 = 64 br³. 64 ÷ 8 = 8 tane. Ayrıtlar 2 katı olunca hacim 8 katı olur.",
              kaynak=[K("u2k5", "Ayrıt Değişince Hacim"), K("u2k4", "Eş Nesnelerle Ölçme")],
              yardim={"adimlar": ["Küçük kutunun hacmi: 2 · 2 · 2.", "Büyük kutunun hacmi: 4 · 4 · 4.", "Büyük hacmi küçük hacme böl."]})]
    }



# Tema 2 · Ölçme birimleri ve problemler (u2k6, u2k7, u2t3, u2k8, u2t4) — 17 Ekim 2026
# Kitap dışı: "basamak/merdiven" görseli (kitaptaki Bilgi Kutusu basamak diyagramının sadeleştirilmiş hâli),
# "1 mL = 1 cm³" kitapta açıkça yazmıyor; s. 147–148'deki iki Bilgi Kutusundan (1 dm³ = 1 L, 1 L = 1000 mL) ve
# 6. konudaki 1 dm³ = 1000 cm³ kuralından türetildi. u2k8'de kaplama problemleri alan birimi çevirmesi gerektirmeyecek
# biçimde (ölçü ve fiyat aynı birimde) yazıldı (Kemal'in kararı: temeli bilsin, ayrıntıya girme).
SU = "#6fb3ff"


def merdiven_svg(birimler, k, w=330, h=150):
    """Birim basamakları: soldan sağa aşağı iner; aşağı × k (turuncu), yukarı ÷ k (mavi)."""
    g = ""
    for i, b in enumerate(birimler):
        x, y = 10 + i * 80, 14 + i * 28
        g += f"<rect x='{x}' y='{y}' width='64' height='26' rx='7' fill='{TEAL}' stroke='#1b2340' stroke-width='1.5'/>"
        g += t2t(x + 32, y + 18, b, "#1b2340", 14)
        if i < len(birimler) - 1:
            g += t2t(x + 74, y + 10, f"× {k}", "#ffa26b", 12, 800, "start")
            g += t2t(x + 40, y + 52, f"÷ {k}", SU, 12)
    return gsvg(w, h, g)


def kap_cizimi(once, sonra=None, maks=1000, cisim=False, H=104, W=56):
    """Dereceli kap: su seviyesi 'once'; sonra verilirse cisimli ikinci seviye. cx, alt → svg parçası."""
    def f(cx, alt):
        x, ust = cx - W / 2, alt - H
        sev = sonra if sonra is not None else once
        yy = alt - H * sev / maks
        g = f"<rect x='{x:.1f}' y='{yy:.1f}' width='{W}' height='{alt - yy:.1f}' fill='{SU}' fill-opacity='0.45'/>"
        if cisim:
            g += f"<path d='M{cx - 16:.1f} {alt - 2:.1f} q4 -18 18 -16 q14 2 12 16 z' fill='#9aa3bf' stroke='#1b2340' stroke-width='1.5'/>"
        g += f"<path d='M{x:.1f} {ust:.1f} V{alt:.1f} H{x + W:.1f} V{ust:.1f}' fill='none' stroke='#f5f6fa' stroke-width='2.5'/>"
        for v in range(0, maks + 1, maks // 5):
            ty = alt - H * v / maks
            g += f"<line x1='{x:.1f}' y1='{ty:.1f}' x2='{x + 10:.1f}' y2='{ty:.1f}' stroke='#f5f6fa' stroke-width='1.5'/>"
            if v:
                g += t2t(x - 4, ty + 4, str(v), SOLUK, 10, 700, "end")
        g += f"<line x1='{x - 2:.1f}' y1='{yy:.1f}' x2='{x + W + 2:.1f}' y2='{yy:.1f}' stroke='#f2c14e' stroke-width='3'/>"
        g += t2t(x + W + 6, yy + 4, f"{sev} mL", "#f2c14e", 12, 800, "start")
        return g
    return f


def kap_svg(once, sonra, maks=1000, w=330, h=160):
    g = kap_cizimi(once, maks=maks)(w * 0.27, h - 30) + kap_cizimi(once, sonra, maks, True)(w * 0.70, h - 30)
    g += t2t(w * 0.27, h - 8, "Önce", SOLUK, 12, 700) + t2t(w * 0.70, h - 8, "Cismi atınca", SOLUK, 12, 700)
    return gsvg(w, h, g)


def akvaryum_svg(e, b, c, oran, su_yazi, A=150, B=80, C=100, w=330, h=180):
    x, y = (w - A - B / 2) / 2 - 10, h - 28
    D, S_ = B * 0.5, C * oran
    g = prizma(x, y, A, B, C, (e, b, c), dolgu=False)
    g += t2poly([(x, y), (x + A, y), (x + A, y - S_), (x, y - S_)], SU, "none", 0, " fill-opacity='0.45'")
    g += t2poly([(x, y - S_), (x + A, y - S_), (x + A + D, y - S_ - D), (x + D, y - S_ - D)], SU, "none", 0, " fill-opacity='0.3'")
    g += t2poly([(x + A, y), (x + A + D, y - D), (x + A + D, y - S_ - D), (x + A, y - S_)], SU, "none", 0, " fill-opacity='0.25'")
    if su_yazi:
        g += t2t(x + A / 2, y - S_ / 2 + 5, su_yazi, "#f2c14e", 13)
    return gsvg(w, h, g)


# ---------- Kavram ve hazırlık çizimleri (120 × 120) ----------
def svg6_m3():
    return bg(prizma(30, 78, 50, 40, 46, ("1 m", "1 m", "1 m"), gizli=False) + txt(60, 114, "1 m³", "#f2c14e", 14))


def svg6_uygun():
    g = "<rect x='12' y='42' width='40' height='34' rx='4' fill='#9aa3bf'/><circle cx='22' cy='80' r='6' fill='#5a6280'/><circle cx='44' cy='80' r='6' fill='#5a6280'/>"
    g += "<rect x='78' y='46' width='18' height='30' rx='3' fill='#ffa26b'/><rect x='84' y='40' width='6' height='7' fill='#f5f6fa'/>"
    g += txt(32, 102, "m³", "#f2c14e", 16) + txt(87, 102, "küçük", "#f2c14e", 12)
    g += txt(60, 26, "büyüğe büyük birim", SOLUK, 10, 700)
    return bg(g)


def svg6_1000():
    g = "".join(f"<rect x='{24 + i * 7}' y='{30 + j * 7}' width='7' height='7' fill='{TEAL}' stroke='#1b2340' stroke-width='0.6'/>" for i in range(10) for j in range(10))
    g += txt(60, 26, "1 m = 10 dm", "#f5f6fa", 11)
    g += txt(60, 112, "10 · 10 · 10 = 1000", "#f2c14e", 11)
    return bg(g)


def svg6_merdiven(birimler=("m³", "dm³", "cm³", "mm³"), k="1000"):
    g = ""
    for i, b in enumerate(birimler):
        x, y = 6 + i * 26, 8 + i * 22
        g += f"<rect x='{x}' y='{y}' width='32' height='20' rx='5' fill='{TEAL}' stroke='#1b2340' stroke-width='1.2'/>" + txt(x + 16, y + 14, b, "#1b2340", 10)
    g += txt(36, 112, f"↓ × {k}", "#ffa26b", 11) + txt(88, 112, f"↑ ÷ {k}", SU, 11)
    return bg(g)


def svg6_carp():
    return bg(txt(60, 40, "2,5 m³", "#f5f6fa", 16) + txt(60, 64, "× 1000 ↓", "#ffa26b", 12) + txt(60, 92, "2500 dm³", "#f2c14e", 16))


def svg6_bol():
    return bg(txt(60, 40, "6000 cm³", "#f5f6fa", 15) + txt(60, 64, "÷ 1000 ↑", SU, 12) + txt(60, 92, "6 dm³", "#f2c14e", 17))


def svg6_esitle():
    g = txt(60, 30, "2 m · 1 m · 50 cm", "#ff8fab", 11)
    g += txt(60, 56, "↓ hepsi dm", SOLUK, 11, 700)
    g += txt(60, 82, "20 · 10 · 5", "#4fc3a1", 15) + txt(60, 106, "= 1000 dm³", "#f2c14e", 13)
    return bg(g)


def svg6_h_uzunluk():
    g = "<line x1='12' y1='60' x2='108' y2='60' stroke='#f5f6fa' stroke-width='3'/>"
    g += "".join(f"<line x1='{12 + i * 9.6:.1f}' y1='{52 if i in (0, 10) else 55}' x2='{12 + i * 9.6:.1f}' y2='{68 if i in (0, 10) else 65}' stroke='#f5f6fa' stroke-width='2'/>" for i in range(11))
    g += txt(60, 40, "1 m", "#f2c14e", 14) + txt(60, 90, "= 10 dm = 100 cm", "#f5f6fa", 11)
    return bg(g)


def svg6_h_1000():
    return bg(txt(60, 42, "6 · 1000", "#f5f6fa", 16) + txt(60, 70, "= 6000", "#f2c14e", 18) + txt(60, 98, "virgül 3 basamak", SOLUK, 10))


def svg7_litre():
    g = "<path d='M44 30 h32 v10 q12 8 12 22 v40 q0 6 -6 6 h-44 q-6 0 -6 -6 v-40 q0 -14 12 -22z' fill='none' stroke='#f5f6fa' stroke-width='2.5'/>"
    g += f"<path d='M33 66 h54 v36 q0 4 -4 4 h-46 q-4 0 -4 -4z' fill='{SU}' fill-opacity='0.5'/>"
    g += txt(60, 92, "1 L", "#f2c14e", 16)
    return bg(g)


def svg7_dm3():
    g = prizma(14, 80, 40, 30, 40, ("1 dm", "", ""), gizli=False)
    g += f"<rect x='74' y='40' width='34' height='40' fill='{SU}' fill-opacity='0.5' stroke='#f5f6fa' stroke-width='2'/>"
    g += txt(60, 116, "1 dm³ = 1 L", "#f2c14e", 12)
    return bg(g)


def svg7_ml():
    g = kupler([(0, 0, 0)], 20, 80, 26) + txt(36, 100, "1 cm³", "#f5f6fa", 11)
    g += f"<rect x='76' y='54' width='20' height='26' fill='{SU}' fill-opacity='0.5' stroke='#f5f6fa' stroke-width='2'/>" + txt(86, 100, "1 mL", "#f5f6fa", 11)
    g += txt(60, 30, "aynı hacim", "#f2c14e", 12)
    return bg(g)


def svg7_kap():
    g = kap_cizimi(300, 450, 500, True, H=80, W=40)(44, 98)
    return bg(g)


def svg7_sirala():
    g = txt(60, 30, "2 L · 1500 mL", "#ff8fab", 11) + txt(60, 44, "180 cL", "#ff8fab", 11)
    g += txt(60, 62, "↓ hepsi mL", SOLUK, 11, 700)
    g += txt(60, 84, "2000 · 1500 · 1800", "#4fc3a1", 11) + txt(60, 106, "sonra sırala", "#f2c14e", 12)
    return bg(g)


def svg7_h_10():
    return bg(txt(60, 42, "3,5 · 10", "#f5f6fa", 16) + txt(60, 70, "= 35", "#f2c14e", 18) + txt(60, 98, "virgül 1 basamak", SOLUK, 10))


def svg8_iskelet():
    g = ""
    for i, (s, r) in enumerate([("Ne veriliyor?", "#f5f6fa"), ("Kapla mı?", "#ffd166"), ("Birim aynı mı?", "#ff8fab"), ("Hesapla", "#4fc3a1")]):
        g += f"<circle cx='16' cy='{24 + i * 24}' r='8' fill='{r}'/>" + txt(16, 28 + i * 24, str(i + 1), "#1b2340", 10)
        g += txt(30, 28 + i * 24, s, r, 11, 700, "start")
    return bg(g)


def svg8_sigar():
    g = prizma(10, 90, 70, 30, 40) + kupler(kutu(2, 1, 1), 14, 90, 18)
    g += txt(60, 112, "büyük ÷ küçük", "#f2c14e", 12)
    return bg(g)


def svg8_kapla():
    g = prizma(28, 82, 48, 30, 40, vurgu="yuz")
    g += txt(60, 104, "alan × fiyat", "#f2c14e", 13)
    return bg(g)


def svg8_su():
    g = prizma(20, 86, 60, 30, 56, dolgu=False)
    g += t2poly([(20, 86), (80, 86), (80, 62), (20, 62)], SU, "none", 0, " fill-opacity='0.5'")
    g += txt(50, 80, "?", "#f2c14e", 16) + txt(60, 112, "hacim ÷ taban alanı", "#f2c14e", 10)
    return bg(g)


def svg8_cisim():
    g = prizma(20, 86, 60, 30, 56, dolgu=False)
    g += t2poly([(20, 86), (80, 86), (80, 56), (20, 56)], SU, "none", 0, " fill-opacity='0.5'")
    g += "<line x1='20' y1='64' x2='80' y2='64' stroke='#f5f6fa' stroke-width='1.5' stroke-dasharray='4 3'/>"
    g += "<path d='M30 85 q4 -10 12 -9 q8 1 7 9z' fill='#9aa3bf'/>"
    g += txt(60, 112, "taban alanı × yükselme", "#f2c14e", 10)
    return bg(g)


def svg8_havuz():
    g = f"<rect x='14' y='44' width='92' height='34' rx='4' fill='{SU}' fill-opacity='0.5' stroke='#f5f6fa' stroke-width='2'/>"
    g += txt(60, 30, "1 m³ = 1000 L", "#f2c14e", 14) + txt(60, 100, "büyük su → m³", SOLUK, 11, 700)
    return bg(g)


# =================================================================
def u2k6():
    return {
        "id": "u2k6", "unite": T2, "baslik": "Hacim Ölçme Birimleri", "sayfalar": "s. 144–146",
        "giris": "Bir kamyon kumu ile bir küp şekeri aynı birimle ölçmek zor olur. Bu konuda hacim birimlerini (m³, dm³, cm³, mm³) tanıyacağız. Bir birimi ötekine çevirmeyi adım adım öğreneceğiz.",
        "hazirlik": {
            "baslik": "Hazır mısın?",
            "giris": "Bu konuda birimleri çevireceğiz ve 1000 ile çarpıp böleceğiz. Önce bunları hatırlıyor musun bakalım. Not yok.",
            "maddeler": [
                {"ad": "Uzunluk birimleri", "sinif": "Önceki yıllar", "svg": svg6_h_uzunluk(),
                 "anlatim": "1 metre 10 desimetredir, 1 desimetre 10 santimetredir. Yani 1 m = 10 dm = 100 cm.",
                 "akilda": "1 m = 10 dm, 1 dm = 10 cm",
                 "ornek": {"problem": "3 m kaç dm?", "adimlar": [
                     {"metin": "1 m = 10 dm.", "islem": "1 m → 10 dm"},
                     {"metin": "3 metre, 3 tane 10 dm demek.", "islem": "3 · 10 = 30 dm"}]},
                 "sorular": [
                     G("2 m kaç dm?", "20", "1 m = 10 dm.", "2 · 10 = 20 dm.", birim="dm",
                       yardim={"adimlar": ["1 m kaç dm?", "2 tane 10'u topla."]}),
                     G("50 cm kaç dm?", "5", "1 dm = 10 cm. 50'nin içinde kaç tane 10 var?", "50 ÷ 10 = 5 dm.", birim="dm",
                       yardim={"adimlar": ["1 dm = 10 cm.", "50'yi 10'a böl."]})]},
                {"ad": "1000 ile çarpma ve bölme", "sinif": "Önceki yıllar", "svg": svg6_h_1000(),
                 "anlatim": "1000 ile çarparken sayının sonuna üç 0 ekleriz: 6 · 1000 = 6000. Sayı ondalıksa virgülü 3 basamak sağa kaydırırız: 2,5 · 1000 = 2500. 1000'e bölerken tersini yaparız: 6000 ÷ 1000 = 6.",
                 "akilda": "× 1000: üç 0 ekle",
                 "ornek": {"problem": "2,5 · 1000 kaçtır?", "adimlar": [
                     {"metin": "Virgülü 3 basamak sağa kaydır. 2,5'te virgülden sonra 1 basamak var.", "islem": "2,5 → 25"},
                     {"metin": "Eksik kalan 2 basamağa 0 yaz.", "islem": "2500"}]},
                 "sorular": [
                     G("6 · 1000 kaçtır?", "6000", "1000 ile çarparken sona üç 0 ekle.", "6 · 1000 = 6000.",
                       yardim={"adimlar": ["1000'de kaç tane 0 var?", "6'nın sonuna o kadar 0 ekle."]}),
                     G("2,5 · 1000 kaçtır?", "2500", "Virgülü 3 basamak sağa kaydır.", "2,5 · 1000 = 2500.", denk=True,
                       yardim={"adimlar": ["Virgülü 1 basamak kaydırınca 25 olur.", "2 basamak daha var: sona 0 ekle."]})]},
                {"ad": "Prizmanın hacmi", "sinif": "2. tema, 5. konu", "svg": svg2_formul_hacim(),
                 "anlatim": "Dikdörtgenler prizmasının hacmi üç ayrıtın çarpımıdır: a · b · c. Ayrıtlar m ile verilirse hacim m³ olur.",
                 "akilda": "Hacim = a · b · c",
                 "sorular": [
                     G("Ayrıtları 2 m, 3 m ve 1 m olan prizmanın hacmi kaç m³?", "6", "Üç ayrıtı çarp.", "2 · 3 · 1 = 6 m³.", birim="m³",
                       yardim={"adimlar": ["Önce 2 · 3.", "Sonucu 1 ile çarp."]}),
                     G("Ayrıtları 2 m, 2 m ve 5 m olan prizmanın hacmi kaç m³?", "20", "Üç ayrıtı çarp.", "2 · 2 · 5 = 20 m³.", birim="m³",
                       yardim={"adimlar": ["Önce 2 · 2.", "Sonucu 5 ile çarp."]})]}
            ]},
        "kavramlar": [
            {"ad": "Metreküp", "renk": "#1f9e8f", "svg": svg6_m3(),
             "aciklama": "Hacim ölçülerinin temel birimi metreküptür ve m³ ile gösterilir. Her ayrıtı 1 m olan küpün hacmi 1 m³'tür. (s. 146)",
             "ek": "m³'ten küçük birimler de vardır: desimetreküp (dm³), santimetreküp (cm³), milimetreküp (mm³). (s. 146)",
             "akilda": "Temel birim: m³",
             "soru": S("Hacim ölçülerinin temel birimi hangisidir?", ["Metre", "Metreküp", "Metrekare"], 1,
                       "Bilgi kartındaki ilk cümleye bak.", "Hacmin temel birimi metreküptür (m³). Metre uzunluk, metrekare alan birimidir. (s. 146)")},
            {"ad": "Hangi Birim Uygun?", "renk": "#b7791f", "svg": svg6_uygun(),
             "aciklama": "Büyük hacimler (beton, kum, konteyner) büyük birimle, küçük hacimler küçük birimle ölçülür. (s. 144)",
             "ek": "Elif'in babası bahçe için “5 m³ kum” istedi. Bir meyve suyu kutusuna “0,0002 m³” yazsak komik olurdu; küçük kutu için küçük birim kullanılır. (s. 144)",
             "akilda": "Büyüğe büyük, küçüğe küçük birim",
             "soru": S("Bir kamyonun taşıdığı kumun hacmi için en uygun birim hangisidir?", ["mm³", "cm³", "m³"], 2,
                       "Kum çok mu, az mı?", "Kamyondaki kum çok büyük bir hacimdir: m³ uygun. (s. 144)")},
            {"ad": "1 m³ = 1000 dm³", "renk": "#1d6fa3", "svg": svg6_1000(),
             "aciklama": "Ayrıtı 1 m olan bir koliye ayrıtı 1 dm olan kutulardan 10 · 10 · 10 = 1000 tane sığar. Bu yüzden 1 m³ = 1000 dm³. (s. 145)",
             "ek": "1 m = 10 dm. Kolinin tabanına 10 · 10 = 100 kutu dizilir; 10 kat olunca 1000 kutu olur. Hacimde üç ayrıt olduğu için 10 değil 1000 katı. (s. 145)",
             "akilda": "1 m³ = 1000 dm³",
             "cozum": {"baslik": "Koliye kaç kutu sığar?",
                       "problem": "Ayrıtı 1 m olan bir koliyi, ayrıtı 1 dm olan küp kutularla dolduralım.",
                       "adimlar": [
                           {"metin": "Kolinin her ayrıtı 1 m = 10 dm. Bir kenara 10 kutu dizilir.", "islem": "1 m = 10 dm"},
                           {"metin": "Taban katmanı: 10 sıra, her sırada 10 kutu.", "islem": "10 · 10 = 100 kutu"},
                           {"metin": "10 katman var.", "islem": "100 · 10 = 1000 kutu"}],
                       "sonuc": "Koliye 1000 kutu sığar: 1 m³ = 1000 dm³. (s. 145)"},
             "soru": G("Ayrıtı 1 m olan bir koliye ayrıtı 1 dm olan küp kutulardan kaç tane sığar?", "1000", "Bir kenara 10 kutu dizilir: 10 · 10 · 10.",
                       "10 · 10 · 10 = 1000 kutu. (s. 145)",
                       yardim={"adimlar": ["1 m kaç dm?", "Taban katmanında 10 · 10 kutu var.", "Kaç katman var? Bir katmanı katman sayısıyla çarp."]})},
            {"ad": "Hacim Basamakları", "renk": "#7b4fc9", "svg": svg6_merdiven(),
             "aciklama": "Hacim birimleri büyükten küçüğe sıralanır: m³, dm³, cm³, mm³. Aşağı inerken her basamakta 1000 ile çarparız, yukarı çıkarken 1000'e böleriz. (s. 146)",
             "ek": "Kitaptaki Bilgi Kutusu bunu basamaklarla gösterir. Kolay hatırlamak için basamakları bir merdiven gibi düşün: aşağı in → × 1000, yukarı çık → ÷ 1000.",
             "akilda": "Aşağı × 1000, yukarı ÷ 1000",
             "soru": S("Büyük birimden küçük birime (örneğin m³'ten dm³'e) çevirirken ne yaparız?",
                       ["1000 ile çarparız.", "1000'e böleriz.", "10 ile çarparız."], 0,
                       "Merdivende aşağı iniyoruz.", "Aşağı inerken her basamakta 1000 ile çarparız. (s. 146)")},
            {"ad": "Büyükten Küçüğe: Çarp", "renk": "#e8590c", "svg": svg6_carp(),
             "aciklama": "Büyük birimi küçük birime çevirince sayı büyür: her basamak için 1000 ile çarparız. (s. 146)",
             "ek": "Ondalık sayıda virgülü 3 basamak sağa kaydırırız: 2,5 m³ = 2500 dm³. İki basamak inersek iki kez 1000 ile çarparız: 2 m³ = 2000 dm³ = 2 000 000 cm³.",
             "akilda": "Küçük birim → büyük sayı",
             "cozum": {"baslik": "m³'ten dm³'e",
                       "problem": "2,5 m³ kaç dm³'tür?",
                       "svg": merdiven_svg(["m³", "dm³", "cm³", "mm³"], "1000"),
                       "adimlar": [
                           {"metin": "m³'ten dm³'e: bir basamak aşağı iniyoruz.", "islem": "× 1000"},
                           {"metin": "Virgülü 3 basamak sağa kaydır; eksik basamağa 0 yaz.", "islem": "2,5 · 1000 = 2500"}],
                       "sonuc": "2,5 m³ = 2500 dm³. (s. 146)"},
             "sende": {"baslik": "Sıra sende",
                       "problem": "0,4 dm³ kaç cm³'tür?",
                       "adimlar": [
                           {"metin": "dm³'ten cm³'e: bir basamak aşağı.", "islem": "× 1000"},
                           {"metin": "0,4'ü 1000 ile çarp.",
                            "soru": G("0,4 · 1000 kaçtır?", "400", "Virgülü 3 basamak sağa kaydır.", "0,4 · 1000 = 400.", denk=True,
                                      yardim={"adimlar": ["0,4'te virgülden sonra 1 basamak var: 4 olur.", "2 basamak daha kaydır: sona iki 0 ekle."]}),
                            "islem": "0,4 · 1000 = 400 cm³"}],
                       "sonuc": "Harika! 0,4 dm³ = 400 cm³."},
             "soru": G("3 dm³ kaç cm³?", "3000", "dm³'ten cm³'e bir basamak aşağı: 1000 ile çarp.", "3 · 1000 = 3000 cm³. (s. 146)", birim="cm³",
                       yardim={"adimlar": ["Merdivende aşağı mı iniyoruz, yukarı mı çıkıyoruz?", "Aşağı: 1000 ile çarp."]})},
            {"ad": "Küçükten Büyüğe: Böl", "renk": "#2f8f73", "svg": svg6_bol(),
             "aciklama": "Küçük birimi büyük birime çevirince sayı küçülür: her basamak için 1000'e böleriz. (s. 146)",
             "ek": "1000'e bölerken sondan üç 0 sileriz ya da virgülü 3 basamak sola kaydırırız: 3500 dm³ = 3,5 m³.",
             "akilda": "Büyük birim → küçük sayı",
             "cozum": {"baslik": "dm³'ten m³'e",
                       "problem": "3500 dm³ kaç m³'tür?",
                       "adimlar": [
                           {"metin": "dm³'ten m³'e: bir basamak yukarı çıkıyoruz.", "islem": "÷ 1000"},
                           {"metin": "Virgülü 3 basamak sola kaydır.", "islem": "3500 ÷ 1000 = 3,5"}],
                       "sonuc": "3500 dm³ = 3,5 m³. (s. 146)"},
             "sende": {"baslik": "Sıra sende",
                       "problem": "8000 mm³ kaç cm³'tür?",
                       "adimlar": [
                           {"metin": "mm³'ten cm³'e: bir basamak yukarı.", "islem": "÷ 1000"},
                           {"metin": "8000'i 1000'e böl.",
                            "soru": G("8000 ÷ 1000 kaçtır?", "8", "Sondan üç 0 sil.", "8000 ÷ 1000 = 8.",
                                      yardim={"adimlar": ["1000'de kaç tane 0 var?", "8000'in sonundan o kadar 0 sil."]}),
                            "islem": "8000 ÷ 1000 = 8 cm³"}],
                       "sonuc": "Harika! 8000 mm³ = 8 cm³."},
             "soru": G("6000 cm³ kaç dm³?", "6", "cm³'ten dm³'e bir basamak yukarı: 1000'e böl.", "6000 ÷ 1000 = 6 dm³. (s. 146)", birim="dm³",
                       yardim={"adimlar": ["Merdivende aşağı mı iniyoruz, yukarı mı çıkıyoruz?", "Yukarı: 1000'e böl. Sondan üç 0 sil."]})},
            {"ad": "Önce Birimleri Eşitle", "renk": "#c92a2a", "svg": svg6_esitle(),
             "aciklama": "Ayrıtlar farklı birimlerle verilmişse önce hepsini aynı birime çeviririz, sonra çarparız. (s. 146)",
             "ek": "Kitaptaki sebze yatağının ölçüleri 2 m, 1,5 m ve 40 cm'dir: m ile cm karışık. Hepsini dm'ye çevirirsek hacim doğrudan dm³ çıkar. (s. 146)",
             "akilda": "Önce aynı birim, sonra çarp",
             "cozum": {"baslik": "Sebze yatağı",
                       "problem": "Bir sebze yatağı 2 m uzunluğunda, 1 m genişliğinde ve 50 cm derinliğindedir. Her toprak paketi 50 dm³. Kaç paket toprak gerekir?",
                       "svg": svg_prizma_et("2 m", "1 m", "50 cm", A=150, B=70, C=50, h=130),
                       "adimlar": [
                           {"metin": "Kaplamak mı, doldurmak mı? Toprak yatağı dolduruyor: hacim."},
                           {"metin": "Birimler aynı mı? Hayır. Hepsini dm yap.", "islem": "2 m = 20 dm, 1 m = 10 dm, 50 cm = 5 dm"},
                           {"metin": "Hacmi bul.", "islem": "20 · 10 · 5 = 1000 dm³"},
                           {"metin": "Bir paket 50 dm³. Kaç paket?", "islem": "1000 ÷ 50 = 20"}],
                       "sonuc": "20 paket toprak gerekir. (s. 146)"},
             "sende": {"baslik": "Sıra sende",
                       "problem": "Bir kutunun ayrıtları 1 m, 4 dm ve 20 cm. Hacmi kaç dm³?",
                       "adimlar": [
                           {"metin": "Birimleri dm yap: 1 m = 10 dm, 4 dm aynı kalır.", "islem": "10 dm, 4 dm"},
                           {"metin": "20 cm kaç dm?",
                            "soru": G("20 cm kaç dm?", "2", "1 dm = 10 cm.", "20 ÷ 10 = 2 dm.", birim="dm",
                                      yardim={"adimlar": ["1 dm kaç cm?", "20'yi 10'a böl."]}),
                            "islem": "20 cm = 2 dm"},
                           {"metin": "Üç ayrıtı çarp.",
                            "soru": G("10 · 4 · 2 kaçtır?", "80", "Önce 10 · 4, sonra 2 ile çarp.", "10 · 4 = 40, 40 · 2 = 80.",
                                      yardim={"adimlar": ["Önce 10 · 4.", "Sonucu 2 ile çarp."]}),
                            "islem": "10 · 4 · 2 = 80 dm³"}],
                       "sonuc": "Harika! Kutunun hacmi 80 dm³."},
             "soru": S("Ayrıtları 1 m, 5 dm ve 2 dm olan bir kutunun hacmini dm³ olarak bulmak için ilk ne yapmalıyız?",
                       ["1 · 5 · 2 işlemini yaparız.", "1 m'yi 10 dm'ye çeviririz.", "Sayıları toplarız."], 1,
                       "Birimler aynı mı?", "Önce birimleri eşitleriz: 1 m = 10 dm. Sonra 10 · 5 · 2 = 100 dm³. (s. 146)")}
        ],
        "akildaKalsin": [
            "Hacmin temel birimi metreküptür (m³).",
            "Büyük hacimler büyük birimle, küçük hacimler küçük birimle ölçülür.",
            "1 m³ = 1000 dm³, 1 dm³ = 1000 cm³, 1 cm³ = 1000 mm³.",
            "Basamakta aşağı inerken × 1000, yukarı çıkarken ÷ 1000.",
            "Küçük birime çevirince sayı büyür, büyük birime çevirince küçülür.",
            "Ayrıtların birimleri farklıysa önce eşitle, sonra çarp."],
        "merakKutusu": [
            {"soru": "Uzunlukta 1 m = 10 dm iken hacimde neden 1000 katı?", "cevap": "Hacimde üç ayrıt vardır. Her ayrıt 10 katı olunca hacim 10 · 10 · 10 = 1000 katı olur. (s. 145)"},
            {"soru": "Neden her şeyi m³ ile ölçmüyoruz?", "cevap": "Küçük şeyler için m³ çok büyük kalır; meyve suyu kutusu 0,0002 m³ gibi garip bir sayı olur. Küçük şeye küçük birim yakışır. (s. 144)"},
            {"soru": "Sayı büyüdü mü, küçüldü mü diye nasıl kontrol ederim?", "cevap": "Küçük birime çevirdiysen sayı büyümeli (3 m³ = 3000 dm³). Büyük birime çevirdiysen sayı küçülmeli (6000 cm³ = 6 dm³)."},
            {"soru": "Kamyonun kasasına kaç koli sığar?", "cevap": "Kitaptaki kamyonun kasası 3 m, 2 m ve 2 m. Ayrıtı 1 m olan kolilerden 3 · 2 · 2 = 12 tane sığar; kasanın hacmi 12 m³'tür. (s. 145)"}],
        "dusunVeYaz": [{"soru": "Can “3 m³ = 30 dm³” dedi. Hatası ne? Doğrusunu yaz.",
                        "ornekCevap": "Can uzunluktaki gibi 10 ile çarptı. Hacimde her basamak 1000 katıdır: 3 m³ = 3000 dm³.",
                        "anahtarlar": ["1000", "3000", "10"]}],
        "sorular": [
            S("Bir yüzme havuzundaki suyun hacmi için en uygun birim hangisidir?", ["m³", "cm³", "mm³"], 0,
              "Havuz büyük mü, küçük mü?", "Havuz çok büyüktür; büyük birim m³ uygundur. (s. 144)", kavram="Hangi Birim Uygun?"),
            G("3 m³ kaç dm³?", "3000", "1 m³ = 1000 dm³.", "3 · 1000 = 3000 dm³. (s. 146)", birim="dm³", kavram="1 m³ = 1000 dm³",
              yardim={"adimlar": ["m³'ten dm³'e: aşağı mı, yukarı mı?", "Aşağı: 1000 ile çarp. 3'ün sonuna üç 0 ekle."]}),
            G("5 dm³ kaç cm³?", "5000", "dm³'ten cm³'e bir basamak aşağı: 1000 ile çarp.", "5 · 1000 = 5000 cm³. (s. 146)", birim="cm³", kavram="Büyükten Küçüğe: Çarp",
              yardim={"adimlar": ["dm³ büyük, cm³ küçük birim: sayı büyüyecek.", "1000 ile çarp."]}),
            G("7000 cm³ kaç dm³?", "7", "cm³'ten dm³'e bir basamak yukarı: 1000'e böl.", "7000 ÷ 1000 = 7 dm³. (s. 146)", birim="dm³", kavram="Küçükten Büyüğe: Böl",
              yardim={"adimlar": ["cm³ küçük, dm³ büyük birim: sayı küçülecek.", "1000'e böl: sondan üç 0 sil."]}),
            S("cm³'ü m³'e çevirirken ne yaparız?", ["Her basamakta 1000 ile çarparız.", "Her basamakta 1000'e böleriz.", "Her basamakta 10'a böleriz."], 1,
              "cm³ küçük, m³ büyük birim. Merdivende yukarı mı çıkıyoruz?", "Yukarı çıkıyoruz: her basamakta 1000'e böleriz. (s. 146)", kavram="Hacim Basamakları"),
            G("0,5 m³ kaç dm³?", "500", "1000 ile çarp: virgülü 3 basamak sağa kaydır.", "0,5 · 1000 = 500 dm³. (s. 146)", birim="dm³", kavram="Büyükten Küçüğe: Çarp",
              yardim={"adimlar": ["m³'ten dm³'e: aşağı iniyoruz, 1000 ile çarp.", "0,5'te virgülü 1 basamak kaydırınca 5 olur. 2 basamak daha var."]}),
            S("Hangisi doğrudur?", ["1 dm³ = 100 cm³", "1 cm³ = 10 mm³", "1 m³ = 1000 dm³"], 2,
              "Hacimde basamaklar arası 10 mu, 1000 mi?", "Hacimde her basamak 1000 katıdır: 1 m³ = 1000 dm³. (s. 146)", kavram="1 m³ = 1000 dm³"),
            G("Ayrıtları 2 m, 1 m ve 50 cm olan prizma biçimindeki bir çukurun hacmi kaç dm³?", "1000",
              "Önce bütün ayrıtları dm'ye çevir.", "2 m = 20 dm, 1 m = 10 dm, 50 cm = 5 dm. 20 · 10 · 5 = 1000 dm³. (s. 146)", birim="dm³", kavram="Önce Birimleri Eşitle",
              yardim={"adimlar": ["Kaplamak mı, doldurmak mı? Doldurmak: hacim.", "Birimler aynı mı? Hepsini dm yap: 20 dm, 10 dm, 5 dm.", "Önce 20 · 10.", "Sonucu 5 ile çarp."]}),
            G("4500 dm³ kaç m³?", "4,5", "dm³'ten m³'e: 1000'e böl, virgülü 3 basamak sola kaydır.", "4500 ÷ 1000 = 4,5 m³. (s. 146)", birim="m³", denk=True, kavram="Küçükten Büyüğe: Böl",
              yardim={"adimlar": ["dm³'ten m³'e: yukarı çıkıyoruz, 1000'e böl.", "4500'de virgül en sondadır. Virgülü 3 basamak sola kaydır."]}),
            S("Her ayrıtı 1 m olan küpün hacmi hangisidir?", ["1 m²", "1 m³", "3 m"], 1,
              "Hacim küp birimle yazılır.", "1 · 1 · 1 = 1 m³. (s. 146)", kavram="Metreküp")]
    }


# =================================================================
def u2k7():
    return {
        "id": "u2k7", "unite": T2, "baslik": "Sıvı Ölçme Birimleri", "sayfalar": "s. 147–151",
        "giris": "Su şişelerinde “1 L” ya da “500 mL” yazar. Bu konuda sıvı ölçme birimlerini öğreneceğiz. Litrenin hacim birimleriyle ilişkisini ve taş gibi düzgün olmayan cisimlerin hacmini ölçmeyi göreceğiz.",
        "hazirlik": {
            "baslik": "Hazır mısın?",
            "giris": "Bu konuda 10 ile çarpıp böleceğiz ve hacim basamaklarını kullanacağız. Önce bunları hatırlıyor musun bakalım. Not yok.",
            "maddeler": [
                {"ad": "Hacim basamakları", "sinif": "2. tema, 6. konu", "svg": svg6_merdiven(),
                 "anlatim": "Hacimde aşağı inerken her basamakta 1000 ile çarparız, yukarı çıkarken 1000'e böleriz: 1 dm³ = 1000 cm³.",
                 "akilda": "Aşağı × 1000, yukarı ÷ 1000",
                 "sorular": [
                     G("2 dm³ kaç cm³?", "2000", "Aşağı iniyoruz: 1000 ile çarp.", "2 · 1000 = 2000 cm³.", birim="cm³",
                       yardim={"adimlar": ["dm³'ten cm³'e aşağı mı, yukarı mı?", "Aşağı: 1000 ile çarp."]}),
                     G("3000 cm³ kaç dm³?", "3", "Yukarı çıkıyoruz: 1000'e böl.", "3000 ÷ 1000 = 3 dm³.", birim="dm³",
                       yardim={"adimlar": ["cm³'ten dm³'e aşağı mı, yukarı mı?", "Yukarı: 1000'e böl, sondan üç 0 sil."]})]},
                {"ad": "10 ile çarpma ve bölme", "sinif": "Önceki yıllar", "svg": svg7_h_10(),
                 "anlatim": "10 ile çarparken sona bir 0 ekleriz ya da virgülü 1 basamak sağa kaydırırız: 3,5 · 10 = 35. 10'a bölerken tersini yaparız: 40 ÷ 10 = 4.",
                 "akilda": "× 10: virgül 1 basamak sağa",
                 "sorular": [
                     G("3,5 · 10 kaçtır?", "35", "Virgülü 1 basamak sağa kaydır.", "3,5 · 10 = 35.", denk=True,
                       yardim={"adimlar": ["3,5'te virgülden sonra kaç basamak var?", "Virgülü 1 basamak sağa kaydır."]}),
                     G("40 ÷ 10 kaçtır?", "4", "Sondan bir 0 sil.", "40 ÷ 10 = 4.",
                       yardim={"adimlar": ["10'da kaç tane 0 var?", "40'ın sonundan bir 0 sil."]})]},
                {"ad": "Prizmanın hacmi", "sinif": "2. tema, 5. konu", "svg": svg2_formul_hacim(),
                 "anlatim": "Dikdörtgenler prizmasının hacmi üç ayrıtın çarpımıdır: a · b · c. Ayrıtlar dm ile verilirse hacim dm³ olur.",
                 "akilda": "Hacim = a · b · c",
                 "sorular": [
                     G("Ayrıtları 2 dm, 3 dm ve 1 dm olan kabın hacmi kaç dm³?", "6", "Üç ayrıtı çarp.", "2 · 3 · 1 = 6 dm³.", birim="dm³",
                       yardim={"adimlar": ["Önce 2 · 3.", "Sonucu 1 ile çarp."]}),
                     G("Ayrıtları 4 dm, 2 dm ve 1 dm olan kabın hacmi kaç dm³?", "8", "Üç ayrıtı çarp.", "4 · 2 · 1 = 8 dm³.", birim="dm³",
                       yardim={"adimlar": ["Önce 4 · 2.", "Sonucu 1 ile çarp."]})]}
            ]},
        "kavramlar": [
            {"ad": "Litre", "renk": "#1f9e8f", "svg": svg7_litre(),
             "aciklama": "Sıvıların hacmini ölçmede temel birim litredir ve L ile gösterilir. (s. 148)",
             "ek": "Su, süt, zeytinyağı, benzin gibi sıvıları litreyle ölçeriz. Sıvı ölçü birimleri aynı zamanda birer hacim ölçüsüdür. (s. 147–148)",
             "akilda": "Sıvı: litre (L)",
             "soru": S("Litre hangi sembolle gösterilir?", ["L", "m", "kg"], 0, "Litrenin baş harfi.", "Litre L ile gösterilir. (s. 148)")},
            {"ad": "1 dm³ = 1 L", "renk": "#1d6fa3", "svg": svg7_dm3(),
             "aciklama": "Kenar uzunlukları 1 dm olan küpün hacmi 1 dm³'tür ve 1 dm³ = 1 L'dir. (s. 147)",
             "ek": "Bir kabın kaç litre su alacağını bulmak için ayrıtlarını dm'ye çevirip hacmini dm³ olarak buluruz. Kaç dm³ ise o kadar litredir. (s. 147)",
             "akilda": "1 dm³ = 1 L",
             "cozum": {"baslik": "Kap kaç litre alır?",
                       "problem": "Ayrıtları 2 dm, 3 dm ve 1 dm olan bir kap kaç litre su alır?",
                       "svg": svg_prizma_et("2 dm", "3 dm", "1 dm", A=100, B=90, C=40, h=120),
                       "adimlar": [
                           {"metin": "Kaplamak mı, doldurmak mı? Su kabı dolduruyor: hacim."},
                           {"metin": "Birimler aynı: hepsi dm. Hacmi bul.", "islem": "2 · 3 · 1 = 6 dm³"},
                           {"metin": "1 dm³ = 1 L.", "islem": "6 dm³ = 6 L"}],
                       "sonuc": "Kap 6 litre su alır. (s. 147)"},
             "sende": {"baslik": "Sıra sende",
                       "problem": "Ayrıtları 20 cm, 10 cm ve 10 cm olan bir kap kaç litre su alır?",
                       "adimlar": [
                           {"metin": "Birimleri dm yap: 10 cm = 1 dm.",
                            "soru": G("20 cm kaç dm?", "2", "1 dm = 10 cm.", "20 ÷ 10 = 2 dm.", birim="dm",
                                      yardim={"adimlar": ["1 dm kaç cm?", "20'yi 10'a böl."]}),
                            "islem": "2 dm, 1 dm, 1 dm"},
                           {"metin": "Hacmi bul.", "islem": "2 · 1 · 1 = 2 dm³"},
                           {"metin": "dm³'ü litreye çevir.",
                            "soru": G("2 dm³ kaç litredir?", "2", "1 dm³ = 1 L.", "2 dm³ = 2 L.", birim="L",
                                      yardim={"adimlar": ["1 dm³ kaç litre?", "2 dm³ kaç litre olur?"]}),
                            "islem": "2 dm³ = 2 L"}],
                       "sonuc": "Harika! Kap 2 litre su alır."},
             "soru": G("Hacmi 5 dm³ olan bir kap kaç litre su alır?", "5", "1 dm³ = 1 L.", "5 dm³ = 5 L. (s. 147)", birim="L",
                       yardim={"adimlar": ["1 dm³ kaç litre?", "5 dm³ kaç litre olur?"]})},
            {"ad": "Sıvı Basamakları", "renk": "#7b4fc9", "svg": svg6_merdiven(("L", "dL", "cL", "mL"), "10"),
             "aciklama": "Litrenin alt birimleri desilitre (dL), santilitre (cL) ve mililitredir (mL). Her basamak arasında 10 katlık ilişki vardır: 1 L = 10 dL = 100 cL = 1000 mL. (s. 148)",
             "ek": "Uzunluktaki gibi: aşağı inerken × 10, yukarı çıkarken ÷ 10. Hacim basamaklarında 1000, sıvıda 10 olduğuna dikkat et. (s. 148)",
             "akilda": "Sıvıda her basamak × 10",
             "cozum": {"baslik": "L'den cL'ye",
                       "problem": "2 L kaç cL'dir?",
                       "svg": merdiven_svg(["L", "dL", "cL", "mL"], "10"),
                       "adimlar": [
                           {"metin": "L'den dL'ye bir basamak aşağı.", "islem": "2 · 10 = 20 dL"},
                           {"metin": "dL'den cL'ye bir basamak daha aşağı.", "islem": "20 · 10 = 200 cL"}],
                       "sonuc": "2 L = 200 cL. (s. 148)"},
             "sende": {"baslik": "Sıra sende",
                       "problem": "450 cL kaç L'dir?",
                       "adimlar": [
                           {"metin": "cL'den dL'ye bir basamak yukarı: 10'a böl.",
                            "soru": G("450 ÷ 10 kaçtır?", "45", "Sondan bir 0 sil.", "450 ÷ 10 = 45.",
                                      yardim={"adimlar": ["10'a bölerken sondan bir 0 silinir.", "450'nin sonundaki 0'ı sil."]}),
                            "islem": "450 ÷ 10 = 45 dL"},
                           {"metin": "dL'den L'ye bir basamak daha yukarı: virgülü 1 basamak sola kaydır.",
                            "soru": G("45 ÷ 10 kaçtır?", "4,5", "Virgülü 1 basamak sola kaydır.", "45 ÷ 10 = 4,5.", denk=True,
                                      yardim={"adimlar": ["45'te virgül en sondadır: 45,0.", "Virgülü 1 basamak sola kaydır."]}),
                            "islem": "45 ÷ 10 = 4,5 L"}],
                       "sonuc": "Harika! 450 cL = 4,5 L."},
             "soru": G("3 L kaç mL?", "3000", "1 L = 1000 mL.", "3 · 1000 = 3000 mL. (s. 148)", birim="mL",
                       yardim={"adimlar": ["L'den mL'ye üç basamak aşağı: 10 · 10 · 10 = 1000.", "3'ü 1000 ile çarp."]})},
            {"ad": "1 mL = 1 cm³", "renk": "#e8590c", "svg": svg7_ml(),
             "aciklama": "1 L = 1000 mL ve 1 dm³ = 1000 cm³ olduğu için 1 mL = 1 cm³'tür. (s. 147–148)",
             "ek": "Bu bilgi kitaptaki iki Bilgi Kutusundan çıkar: 1 dm³ = 1 L, 1 L = 1000 mL ve 1 dm³ = 1000 cm³. Dereceli kapta okunan mL, cismin cm³ olarak hacmidir.",
             "akilda": "1 mL = 1 cm³",
             "soru": S("Hacmi 250 cm³ olan bir bardak kaç mL su alır?", ["25", "250", "2500"], 1,
                       "1 mL = 1 cm³.", "1 cm³ = 1 mL olduğu için 250 cm³ = 250 mL. (s. 147–148)")},
            {"ad": "Su Seviyesi Farkı", "renk": "#2f8f73", "svg": svg7_kap(),
             "aciklama": "Düzgün olmayan bir cismin (taş, silgi) hacmini dereceli kapla ölçeriz: cismi suya atarız, su seviyesindeki fark cismin hacmidir. (s. 148–149)",
             "ek": "Cisim suyun içinde yer kaplar, su bu yüzden yükselir. Fark mL ise cismin hacmi aynı sayıda cm³'tür. (s. 149)",
             "akilda": "Sonra − önce = cismin hacmi",
             "cozum": {"baslik": "Taşın hacmi",
                       "problem": "Dereceli kapta 300 mL su var. Bir taş atınca su 450 mL'ye çıktı. Taşın hacmi kaç cm³?",
                       "svg": kap_svg(300, 450, 500),
                       "adimlar": [
                           {"metin": "Önce ne kadar su vardı?", "islem": "300 mL"},
                           {"metin": "Taşı atınca kaç mL oldu?", "islem": "450 mL"},
                           {"metin": "Farkı bul: büyükten küçüğü çıkar.", "islem": "450 − 300 = 150 mL"},
                           {"metin": "1 mL = 1 cm³.", "islem": "150 mL = 150 cm³"}],
                       "sonuc": "Taşın hacmi 150 cm³. (s. 149)"},
             "soru": G("Dereceli kapta 500 mL su vardı. Bir kaşık atınca su 700 mL'ye çıktı. Kaşığın hacmi kaç cm³?", "200",
                       "Su seviyesindeki farkı bul.", "700 − 500 = 200 mL = 200 cm³. (s. 149)", birim="cm³", svg=kap_svg(500, 700),
                       yardim={"adimlar": ["Önce kaç mL, sonra kaç mL?", "Büyükten küçüğü çıkar."]})},
            {"ad": "Aynı Birime Çevir, Sırala", "renk": "#c92a2a", "svg": svg7_sirala(),
             "aciklama": "Farklı birimlerle yazılmış sıvı miktarlarını karşılaştırmak için önce hepsini aynı birime çeviririz. (s. 151)",
             "ek": "En kolayı hepsini mL'ye çevirmektir; sayılar tam sayı olur. Kitapta otomobil depolarının kapasiteleri böyle sıralanır. (s. 151)",
             "akilda": "Önce aynı birim, sonra sırala",
             "cozum": {"baslik": "Şişeleri sıralayalım",
                       "problem": "2 L, 1500 mL ve 180 cL'lik üç şişeyi küçükten büyüğe sıralayalım.",
                       "adimlar": [
                           {"metin": "2 L'yi mL yap: 1 L = 1000 mL.", "islem": "2 L = 2000 mL"},
                           {"metin": "180 cL'yi mL yap: 1 cL = 10 mL.", "islem": "180 · 10 = 1800 mL"},
                           {"metin": "Şimdi karşılaştır.", "islem": "1500 < 1800 < 2000"}],
                       "sonuc": "1500 mL < 180 cL < 2 L. (s. 151)"},
             "soru": S("Hangisi en çok sıvıdır?", ["900 mL", "1 L", "80 cL"], 1,
                       "Hepsini mL'ye çevir.", "1 L = 1000 mL, 80 cL = 800 mL. En büyüğü 1000 mL: 1 L. (s. 151)")}
        ],
        "biliyorMusun": ["Kral Hiero (Hiyero) tacının saf altın olup olmadığını merak etti. Arşimet tacı ve aynı ağırlıktaki saf altını suya bıraktı. Taç daha çok su taşırdı; demek ki içine başka maden karışmıştı. (s. 148)"],
        "akildaKalsin": [
            "Sıvıların temel ölçü birimi litredir (L).",
            "1 dm³ = 1 L.",
            "1 L = 10 dL = 100 cL = 1000 mL; sıvıda her basamak × 10.",
            "1 mL = 1 cm³.",
            "Düzgün olmayan cismin hacmi = su seviyesindeki fark.",
            "Karşılaştırmadan önce hepsini aynı birime (mL) çevir."],
        "merakKutusu": [
            {"soru": "Litre de bir hacim birimi mi?", "cevap": "Evet. Sıvı ölçü birimleri aynı zamanda birer hacim ölçüsüdür: 1 L, kenarı 1 dm olan küpün hacmine eşittir. (s. 147)"},
            {"soru": "Hacimde 1000, sıvıda 10 katı; neden farklı?", "cevap": "Hacim birimleri küp birimlerdir (üç ayrıt), bu yüzden 1000 katı. Litrenin alt birimleri ise uzunluk birimleri gibi 10'ar katı ayrılır. (s. 148)"},
            {"soru": "Taşı suya atınca su neden yükselir?", "cevap": "Taş suyun içinde yer kaplar; su ona yer açmak için yükselir. Yükselen su kadar hacim taşındır. (s. 149)"},
            {"soru": "Büyük bir taşı küçük kapla ölçebilir miyim?", "cevap": "Taş kabın ağzından girmeli ve tamamen suyun içinde kalmalı; su da taşmamalı. Büyük cisim için büyük dereceli kap gerekir. (s. 148)"}],
        "dusunVeYaz": [{"soru": "Ece “1 L = 100 mL” dedi. Haklı mı? Açıkla.",
                        "ornekCevap": "Haklı değil. 1 L = 10 dL = 100 cL = 1000 mL. Ece mL ile cL'yi karıştırdı.",
                        "anahtarlar": ["1000", "cL", "değil"]}],
        "sorular": [
            S("Hangisinin miktarı litreyle ölçülür?", ["Bir şişe zeytinyağı", "Bir masanın uzunluğu", "Bir çantanın ağırlığı"], 0,
              "Litre sıvılar için kullanılır.", "Zeytinyağı bir sıvıdır; litreyle ölçülür. (s. 148)", kavram="Litre"),
            G("Hacmi 4 dm³ olan bir kap kaç litre su alır?", "4", "1 dm³ = 1 L.", "4 dm³ = 4 L. (s. 147)", birim="L", kavram="1 dm³ = 1 L",
              yardim={"adimlar": ["1 dm³ kaç litre?", "4 dm³ kaç litre olur?"]}),
            G("2 L kaç mL?", "2000", "1 L = 1000 mL.", "2 · 1000 = 2000 mL. (s. 148)", birim="mL", kavram="Sıvı Basamakları",
              yardim={"adimlar": ["1 L kaç mL?", "2'yi 1000 ile çarp."]}),
            G("Dereceli kapta 400 mL su vardı. Bir taş atınca su 550 mL'ye çıktı. Taşın hacmi kaç cm³?", "150",
              "Su seviyesindeki farkı bul.", "550 − 400 = 150 mL = 150 cm³. (s. 149)", birim="cm³", svg=kap_svg(400, 550), kavram="Su Seviyesi Farkı",
              yardim={"adimlar": ["Önce kaç mL vardı? Taşı atınca kaç mL oldu?", "Büyükten küçüğü çıkar.", "1 mL = 1 cm³."]}),
            S("1 L kaç cL'dir?", ["100", "10", "1000"], 0, "L → dL → cL: iki basamak aşağı.", "1 L = 10 dL = 100 cL. (s. 148)", kavram="Sıvı Basamakları"),
            S("Hacmi 500 cm³ olan bir kap kaç mL su alır?", ["50", "500", "5000"], 1, "1 mL = 1 cm³.", "500 cm³ = 500 mL. (s. 147–148)", kavram="1 mL = 1 cm³"),
            S("1,5 L, 1200 mL ve 140 cL'lik üç şişeden en az su alan hangisidir?", ["140 cL", "1,5 L", "1200 mL"], 2,
              "Hepsini mL'ye çevir.", "1,5 L = 1500 mL, 140 cL = 1400 mL. En küçüğü 1200 mL. (s. 151)", kavram="Aynı Birime Çevir, Sırala",
              yardim={"adimlar": ["1,5 L kaç mL? (× 1000)", "140 cL kaç mL? (× 10)", "Üç sayıyı karşılaştır."]}),
            G("Ayrıtları 20 cm, 10 cm ve 10 cm olan kutu biçimindeki bir kap kaç litre su alır?", "2",
              "Ayrıtları dm'ye çevir, hacmi bul.", "2 dm, 1 dm, 1 dm. 2 · 1 · 1 = 2 dm³ = 2 L. (s. 147)", birim="L", kavram="1 dm³ = 1 L",
              yardim={"adimlar": ["Kaplamak mı, doldurmak mı? Doldurmak: hacim.", "Birimleri dm yap: 20 cm = 2 dm, 10 cm = 1 dm.", "Hacmi bul: 2 · 1 · 1.", "1 dm³ = 1 L."]}),
            G("35 dL kaç L?", "3,5", "dL'den L'ye bir basamak yukarı: 10'a böl.", "35 ÷ 10 = 3,5 L. (s. 148)", birim="L", denk=True, kavram="Sıvı Basamakları",
              yardim={"adimlar": ["dL'den L'ye yukarı mı, aşağı mı?", "Yukarı: 10'a böl. Virgülü 1 basamak sola kaydır."]}),
            S("Dereceli kaba bir taş atınca su seviyesi yükseldi. Taşın hacmi neye eşittir?",
              ["Taşın ağırlığına", "Kaptaki suyun hepsine", "Su seviyesindeki farka"], 2,
              "Taş suyun içinde yer kaplar.", "Su, taşın hacmi kadar yükselir: hacim = seviye farkı. (s. 149)", kavram="Su Seviyesi Farkı")]
    }


# =================================================================
def u2t3():
    return {
        "id": "u2t3", "tur": "tarama", "unite": T2,
        "baslik": "Ara Durak 3: Ölçme Birimleri", "sayfalar": "Konu 6–7 · s. 144–151",
        "giris": "Ölçme birimlerini bitirdin, tebrikler! Kısa bir mola verip hacim ve sıvı birimlerini birlikte gözden geçireceğiz. Önce özetleri oku ve kartları çevir, sonra tarama testini çöz. Not yok.",
        "buyukResim": "Önce hacim birimlerini öğrendik: m³, dm³, cm³, mm³; basamaklar arası 1000. Sonra sıvı birimlerini öğrendik: L, dL, cL, mL; basamaklar arası 10. İki aileyi birleştiren köprü: 1 dm³ = 1 L ve 1 cm³ = 1 mL.",
        "kapsar": ["u2k6", "u2k7"],
        "hatirla": [
            {"konu": "u2k6", "maddeler": [
                "Hacmin temel birimi m³; büyük hacme büyük birim.",
                "m³ → dm³ → cm³ → mm³: aşağı × 1000, yukarı ÷ 1000.",
                "Ayrıtların birimi farklıysa önce eşitle, sonra çarp."]},
            {"konu": "u2k7", "maddeler": [
                "1 dm³ = 1 L ve 1 cm³ = 1 mL.",
                "L → dL → cL → mL: aşağı × 10, yukarı ÷ 10.",
                "Cismin hacmi = su seviyesindeki fark."]}],
        "eskiSoru": 4,
        "oyunKavram": 8,
        "gruplar": [{"soru": "Hangi birim ailesi?", "kutular": [
            {"etiket": "Hacim birimleri (× 1000)", "uyeler": ["Metreküp", "1 m³ = 1000 dm³", "Hacim Basamakları"]},
            {"etiket": "Sıvı birimleri (× 10)", "uyeler": ["Litre", "Sıvı Basamakları"]},
            {"etiket": "İki aileyi bağlar", "uyeler": ["1 dm³ = 1 L", "1 mL = 1 cm³"]}]}],
        "sorular": [
            G("Bir depoda 2 m³ su var. Bu su kaç litredir?", "2000",
              "Önce m³'ü dm³'e çevir, sonra 1 dm³ = 1 L.", "2 m³ = 2000 dm³ = 2000 L.", birim="L",
              kaynak=[K("u2k6", "1 m³ = 1000 dm³"), K("u2k7", "1 dm³ = 1 L")],
              yardim={"adimlar": ["m³'ten dm³'e: 1000 ile çarp.", "dm³ ile litre arasındaki ilişki ne?"]}),
            G("Ayrıtları 2 dm, 10 cm ve 5 cm olan kutu biçimindeki bir kap kaç mL su alır?", "1000",
              "Birimleri cm'ye çevir; 1 cm³ = 1 mL.", "2 dm = 20 cm. 20 · 10 · 5 = 1000 cm³ = 1000 mL.", birim="mL",
              kaynak=[K("u2k6", "Önce Birimleri Eşitle"), K("u2k7", "1 mL = 1 cm³")],
              yardim={"adimlar": ["Kaplamak mı, doldurmak mı? Doldurmak: hacim.", "Birimler aynı mı? 2 dm'yi cm yap: 20 cm.", "Hacmi bul: 20 · 10 · 5.", "cm³ ile mL arasındaki ilişki ne?"]}),
            G("Dereceli kapta 250 mL su vardı. Bir silgi atınca su 400 mL'ye çıktı. Silginin hacmi kaç cm³?", "150",
              "Su seviyesindeki farkı bul; 1 mL = 1 cm³.", "400 − 250 = 150 mL = 150 cm³.", birim="cm³", svg=kap_svg(250, 400, 500),
              kaynak=[K("u2k7", "Su Seviyesi Farkı"), K("u2k7", "1 mL = 1 cm³")],
              yardim={"adimlar": ["Önce kaç mL, sonra kaç mL?", "Büyükten küçüğü çıkar.", "mL ile cm³ arasındaki ilişki ne?"]}),
            S("Hangisi 1 L'ye eşit değildir?", ["1 dm³", "100 cL", "100 cm³"], 2,
              "1 L = 1 dm³ = 1000 cm³.", "1 L = 1 dm³ = 100 cL = 1000 cm³. 100 cm³ ise 100 mL'dir.",
              kaynak=[K("u2k7", "Sıvı Basamakları"), K("u2k6", "Hacim Basamakları")]),
            S("1,2 dm³, 1500 mL ve 130 cL'lik üç şişeden en çok su alan hangisidir?", ["1500 mL", "1,2 dm³", "130 cL"], 0,
              "Hepsini mL'ye çevir.", "1,2 dm³ = 1,2 L = 1200 mL, 130 cL = 1300 mL. En büyüğü 1500 mL.",
              kaynak=[K("u2k7", "Aynı Birime Çevir, Sırala"), K("u2k7", "1 dm³ = 1 L")],
              yardim={"adimlar": ["1,2 dm³ kaç litre? Kaç mL?", "130 cL kaç mL? (× 10)", "Üç sayıyı karşılaştır."]}),
            G("Hacmi 60 dm³ olan bir akvaryum 2 L'lik şişelerle doldurulacak. Kaç şişe su gerekir?", "30",
              "Önce akvaryumun kaç litre aldığını bul.", "60 dm³ = 60 L. 60 ÷ 2 = 30 şişe.",
              kaynak=[K("u2k7", "1 dm³ = 1 L"), K("u2k6", "Önce Birimleri Eşitle")],
              yardim={"adimlar": ["Birimler aynı mı? dm³'ü litreye çevir.", "60 L'de kaç tane 2 L var?"]}),
            S("Elif “Hacim birimlerinde basamaklar arası 10, sıvı birimlerinde 1000 katıdır.” dedi. Elif haklı mı?",
              ["Evet, haklı.", "Hayır; hacimde 1000, sıvıda 10 katıdır.", "Hayır; ikisinde de 100 katıdır."], 1,
              "1 m³ kaç dm³? 1 L kaç dL?", "1 m³ = 1000 dm³ (× 1000), 1 L = 10 dL (× 10). Elif ikisini karıştırdı.",
              kaynak=[K("u2k6", "Hacim Basamakları"), K("u2k7", "Sıvı Basamakları")])]
    }


# =================================================================
def u2k8():
    return {
        "id": "u2k8", "unite": T2, "baslik": "Yüzey Alanı ve Hacim Problemleri", "sayfalar": "s. 152–156",
        "giris": "Bu konuda öğrendiklerimizi gerçek hayatta kullanacağız: kutuları koliye yerleştireceğiz, bir kutuyu kumaşla kaplayacağız, akvaryuma su dolduracağız. Her problemde aynı dört soruyu soracağız.",
        "hazirlik": {
            "baslik": "Hazır mısın?",
            "giris": "Bu konuda yüzey alanını, hacmi ve birim çevirmeyi birlikte kullanacağız. Önce bunları hatırlıyor musun bakalım. Not yok.",
            "maddeler": [
                {"ad": "Yüzey alanı", "sinif": "2. tema, 3. konu", "svg": svg2_hediye(),
                 "anlatim": "Yüzey alanı bütün yüzlerin alanlarının toplamıdır. Küpün 6 eş kare yüzü vardır: yüzey alanı 6 · a · a.",
                 "akilda": "Kaplamak = yüzey alanı",
                 "sorular": [
                     G("Ayrıtı 2 cm olan küpün yüzey alanı kaç cm²?", "24", "Bir yüz 2 · 2. Küpün 6 yüzü var.", "2 · 2 = 4 cm². 6 · 4 = 24 cm².", birim="cm²",
                       yardim={"adimlar": ["Bir yüzün alanı: 2 · 2.", "6 yüz var: bir yüzü 6 ile çarp."]}),
                     G("Ayrıtı 1 cm olan küpün yüzey alanı kaç cm²?", "6", "Bir yüz 1 · 1. Küpün 6 yüzü var.", "1 · 1 = 1 cm². 6 · 1 = 6 cm².", birim="cm²",
                       yardim={"adimlar": ["Bir yüzün alanı: 1 · 1.", "6 yüz var."]})]},
                {"ad": "Hacim", "sinif": "2. tema, 5. konu", "svg": svg2_formul_hacim(),
                 "anlatim": "Dikdörtgenler prizmasının hacmi üç ayrıtın çarpımıdır: a · b · c.",
                 "akilda": "Doldurmak = hacim",
                 "sorular": [
                     G("Ayrıtları 2 cm, 3 cm ve 4 cm olan prizmanın hacmi kaç cm³?", "24", "Üç ayrıtı çarp.", "2 · 3 · 4 = 24 cm³.", birim="cm³",
                       yardim={"adimlar": ["Önce 2 · 3.", "Sonucu 4 ile çarp."]}),
                     G("Ayrıtları 5 cm, 2 cm ve 1 cm olan prizmanın hacmi kaç cm³?", "10", "Üç ayrıtı çarp.", "5 · 2 · 1 = 10 cm³.", birim="cm³",
                       yardim={"adimlar": ["Önce 5 · 2.", "Sonucu 1 ile çarp."]})]},
                {"ad": "Hacim ve sıvı birimleri", "sinif": "2. tema, 6–7. konu", "svg": svg7_dm3(),
                 "anlatim": "1 m³ = 1000 dm³, 1 dm³ = 1 L, 1 L = 1000 mL, 1 cm³ = 1 mL.",
                 "akilda": "1 dm³ = 1 L",
                 "sorular": [
                     G("3 dm³ kaç litredir?", "3", "1 dm³ = 1 L.", "3 dm³ = 3 L.", birim="L",
                       yardim={"adimlar": ["1 dm³ kaç litre?", "3 dm³ kaç litre olur?"]}),
                     S("2000 mL kaç litredir?", ["2", "20", "200"], 0, "1 L = 1000 mL.", "2000 ÷ 1000 = 2 L.")]}
            ]},
        "kavramlar": [
            {"ad": "Problem İskeleti", "renk": "#1f9e8f", "svg": svg8_iskelet(),
             "aciklama": "Her problemde aynı dört soruyu sırayla sorarız: 1) Ne veriliyor, ne isteniyor? 2) Kaplamak mı, doldurmak mı? 3) Birimler aynı mı? 4) Hesapla ve birimi yaz.",
             "ek": "Bu sıralama kitap dışı bir strateji; kitaptaki dört problem de bu adımlarla çözülebilir. Kaplamak = yüzey alanı (cm², dm²), doldurmak = hacim (cm³, dm³, L). (s. 152–155)",
             "akilda": "Ne? Kapla mı? Birim? Hesapla",
             "soru": S("“Bir koliye kaç kutu sığar?” sorusunda neyi kullanırız?", ["Yüzey alanını", "Hacmi", "Çevreyi"], 1,
                       "Kutular koliyi kaplıyor mu, dolduruyor mu?", "Kutular koliyi doldurur: hacim kullanırız. (s. 152)")},
            {"ad": "Kaç Kutu Sığar?", "renk": "#1d6fa3", "svg": svg8_sigar(),
             "aciklama": "Büyük kutuya kaç küçük kutu sığdığını bulmak için büyük hacmi küçük hacme böleriz. (s. 152)",
             "ek": "Kitapta bir konteyner 400 eş kutuyla tam doluyor. Kutular boşluksuz diziliyorsa: kutu sayısı = büyük hacim ÷ küçük hacim. (s. 152)",
             "akilda": "Büyük hacim ÷ küçük hacim",
             "cozum": {"baslik": "Dolaba kutular",
                       "problem": "Bir dolabın içi 6 dm, 4 dm ve 2 dm. Ayrıtı 2 dm olan küp kutular dolaba boşluk kalmadan dizilecek. Kaç kutu sığar?",
                       "svg": svg_prizma_et("6 dm", "4 dm", "2 dm", A=150, B=90, C=50, h=130),
                       "adimlar": [
                           {"metin": "Ne veriliyor? Dolap ve kutunun ayrıtları. Ne isteniyor? Kutu sayısı."},
                           {"metin": "Doldurmak: hacim. Dolabın hacmi.", "islem": "6 · 4 · 2 = 48 dm³"},
                           {"metin": "Bir kutunun hacmi.", "islem": "2 · 2 · 2 = 8 dm³"},
                           {"metin": "Büyük hacmi küçük hacme böl.", "islem": "48 ÷ 8 = 6"}],
                       "sonuc": "Dolaba 6 kutu sığar. (s. 152)"},
             "sende": {"baslik": "Sıra sende",
                       "problem": "Bir kolinin ayrıtları 4 dm, 3 dm ve 2 dm. Ayrıtları 2 dm, 1 dm ve 1 dm olan kutular koliye boşluk kalmadan dizilecek. Kaç kutu sığar?",
                       "adimlar": [
                           {"metin": "Kolinin hacmi.",
                            "soru": G("4 · 3 · 2 kaçtır?", "24", "Önce 4 · 3, sonra 2 ile çarp.", "4 · 3 = 12, 12 · 2 = 24.",
                                      yardim={"adimlar": ["Önce 4 · 3.", "Sonucu 2 ile çarp."]}),
                            "islem": "4 · 3 · 2 = 24 dm³"},
                           {"metin": "Bir kutunun hacmi.", "islem": "2 · 1 · 1 = 2 dm³"},
                           {"metin": "Büyük hacmi küçük hacme böl.",
                            "soru": G("24 ÷ 2 kaçtır?", "12", "24'ün yarısı kaç?", "24 ÷ 2 = 12.",
                                      yardim={"adimlar": ["24'ü 2 eş parçaya ayır.", "Bir parça kaç eder?"]}),
                            "islem": "24 ÷ 2 = 12"}],
                       "sonuc": "Harika! Koliye 12 kutu sığar."},
             "soru": G("Bir kolinin hacmi 24 dm³, bir kutunun hacmi 4 dm³. Kutular koliyi boşluk kalmadan dolduruyor. Koliye kaç kutu sığar?", "6",
                       "Büyük hacmi küçük hacme böl.", "24 ÷ 4 = 6 kutu. (s. 152)",
                       yardim={"adimlar": ["Büyük hacim hangisi, küçük hacim hangisi?", "24'ü 4'e böl."]})},
            {"ad": "Kaplama Maliyeti", "renk": "#b7791f", "svg": svg8_kapla(),
             "aciklama": "Bir kutuyu kaplamanın maliyeti = yüzey alanı × 1 birim karenin fiyatı. (s. 153)",
             "ek": "Kitapta Ahmet Bey takı kutularını kumaşla kaplıyor. Ölçüler dm ise fiyat da “1 dm²” için verilmeli; birimler aynı olunca doğrudan çarparız. Kapaksız ya da altı kaplanmayan kutuda o yüzü saymayız. (s. 153)",
             "akilda": "Yüzey alanı × fiyat",
             "cozum": {"baslik": "Küp kutuyu kaplayalım",
                       "problem": "Ayrıtı 2 dm olan küp şeklindeki bir kutunun bütün yüzleri kumaşla kaplanacak. Kumaşın 1 dm²'si 3 TL. Kumaş kaç TL tutar?",
                       "svg": svg_prizma_et("2 dm", "2 dm", "2 dm", A=80, B=80, C=80, h=150),
                       "adimlar": [
                           {"metin": "Kaplamak mı, doldurmak mı? Kaplamak: yüzey alanı."},
                           {"metin": "Bir yüzün alanı.", "islem": "2 · 2 = 4 dm²"},
                           {"metin": "Küpün 6 yüzü var.", "islem": "6 · 4 = 24 dm²"},
                           {"metin": "Birimler aynı (dm²). Fiyatla çarp.", "islem": "24 · 3 = 72 TL"}],
                       "sonuc": "Kumaş 72 TL tutar. (s. 153)"},
             "sende": {"baslik": "Sıra sende",
                       "problem": "Bir kare prizmanın tabanı 2 dm × 2 dm, yüksekliği 3 dm. Bütün yüzleri kaplanacak. Kumaşın 1 dm²'si 2 TL. Kaç TL tutar?",
                       "adimlar": [
                           {"metin": "İki kare yüz (alt ve üst).", "islem": "2 · (2 · 2) = 8 dm²"},
                           {"metin": "Dört yan yüz: her biri 2 · 3.",
                            "soru": G("4 · (2 · 3) kaçtır?", "24", "Önce parantez: 2 · 3. Sonra 4 ile çarp.", "2 · 3 = 6, 4 · 6 = 24.",
                                      yardim={"adimlar": ["Önce parantez: 2 · 3.", "Sonucu 4 ile çarp."]}),
                            "islem": "4 · 6 = 24 dm²"},
                           {"metin": "Yüzey alanı.", "islem": "8 + 24 = 32 dm²"},
                           {"metin": "Fiyatla çarp.",
                            "soru": G("32 · 2 kaçtır?", "64", "32'yi iki kere topla.", "32 + 32 = 64.",
                                      yardim={"adimlar": ["32 · 2, iki tane 32 demek.", "32 ile 32'yi topla."]}),
                            "islem": "32 · 2 = 64 TL"}],
                       "sonuc": "Harika! Kumaş 64 TL tutar."},
             "soru": G("Bir kutunun yüzey alanı 20 dm². Kumaşın 1 dm²'si 4 TL. Kutuyu kaplamak kaç TL tutar?", "80",
                       "Yüzey alanını fiyatla çarp.", "20 · 4 = 80 TL. (s. 153)", birim="TL",
                       yardim={"adimlar": ["Birimler aynı mı? Yüzey alanı dm², fiyat 1 dm² için.", "20'yi 4 ile çarp."]})},
            {"ad": "Suyun Yüksekliği", "renk": "#7b4fc9", "svg": svg8_su(),
             "aciklama": "Akvaryumdaki suyun hacmi = taban alanı × suyun yüksekliği. Yüksekliği bulmak için hacmi taban alanına böleriz. (s. 154)",
             "ek": "Su litre verilirse önce dm³'e çeviririz (1 L = 1 dm³). Taban da dm ile verilmeli ki birimler aynı olsun. (s. 154)",
             "akilda": "Yükseklik = hacim ÷ taban alanı",
             "cozum": {"baslik": "Akvaryumda su",
                       "problem": "Tabanı 4 dm × 2 dm olan bir akvaryuma 16 L su kondu. Su kaç dm yüksekliğe çıkar?",
                       "svg": akvaryum_svg("4 dm", "2 dm", "5 dm", 0.4, "? dm"),
                       "adimlar": [
                           {"metin": "Ne isteniyor? Suyun yüksekliği."},
                           {"metin": "Birimler aynı mı? Litreyi dm³ yap.", "islem": "16 L = 16 dm³"},
                           {"metin": "Taban alanı.", "islem": "4 · 2 = 8 dm²"},
                           {"metin": "Hacmi taban alanına böl.", "islem": "16 ÷ 8 = 2 dm"}],
                       "sonuc": "Su 2 dm yüksekliğe çıkar. (s. 154)"},
             "soru": G("Taban alanı 6 dm² olan bir akvaryuma 12 L su kondu. Su kaç dm yüksekliğe çıkar?", "2",
                       "12 L = 12 dm³. Hacmi taban alanına böl.", "12 ÷ 6 = 2 dm. (s. 154)", birim="dm",
                       yardim={"adimlar": ["Litreyi dm³ yap: 12 L = 12 dm³.", "Hacmi taban alanına böl: 12 ÷ 6."]})},
            {"ad": "Eklenen Cismin Hacmi", "renk": "#e8590c", "svg": svg8_cisim(),
             "aciklama": "Akvaryuma kum ya da taş eklenince su yükselir. Eklenen cismin hacmi = taban alanı × suyun yükselmesi. (s. 154)",
             "ek": "Kitapta Samet akvaryumuna kum ekliyor; su 0,5 cm yükseliyor. Yükselen su, prizma biçiminde ince bir dilimdir; hacmini taban alanıyla buluruz. (s. 154)",
             "akilda": "Taban alanı × yükselme",
             "cozum": {"baslik": "Samet'in akvaryum kumu",
                       "problem": "Tabanı 40 cm × 25 cm olan akvaryuma kum eklenince su 0,5 cm yükseldi. Kumun hacmi kaç cm³?",
                       "svg": akvaryum_svg("40 cm", "25 cm", "30 cm", 0.55, ""),
                       "adimlar": [
                           {"metin": "Ne isteniyor? Kumun hacmi."},
                           {"metin": "Taban alanı.", "islem": "40 · 25 = 1000 cm²"},
                           {"metin": "Taban alanını yükselmeyle çarp.", "islem": "1000 · 0,5 = 500 cm³"}],
                       "sonuc": "Kumun hacmi 500 cm³. (s. 154)"},
             "sende": {"baslik": "Sıra sende",
                       "problem": "Tabanı 20 cm × 10 cm olan akvaryuma taşlar konunca su 2 cm yükseldi. Taşların hacmi kaç cm³?",
                       "adimlar": [
                           {"metin": "Taban alanı.",
                            "soru": G("20 · 10 kaçtır?", "200", "10 ile çarpınca sona bir 0 eklenir.", "20 · 10 = 200.",
                                      yardim={"adimlar": ["10 ile çarpıyoruz.", "20'nin sonuna bir 0 ekle."]}),
                            "islem": "20 · 10 = 200 cm²"},
                           {"metin": "Yükselmeyle çarp.",
                            "soru": G("200 · 2 kaçtır?", "400", "200'ü iki kere topla.", "200 + 200 = 400.",
                                      yardim={"adimlar": ["200 · 2, iki tane 200 demek.", "200 ile 200'ü topla."]}),
                            "islem": "200 · 2 = 400 cm³"}],
                       "sonuc": "Harika! Taşların hacmi 400 cm³."},
             "soru": S("Akvaryuma bir cisim eklenince su yükseldi. Cismin hacmi nasıl bulunur?",
                       ["Taban alanı × yükselme", "Taban alanı + yükselme", "Yükselme × yükselme"], 0,
                       "Yükselen su ince bir prizma gibi.", "Yükselen suyun hacmi = taban alanı × yükselme; bu da cismin hacmidir. (s. 154)")},
            {"ad": "Litre mi, Metreküp mü?", "renk": "#2f8f73", "svg": svg8_havuz(),
             "aciklama": "Çok büyük su miktarlarını (havuz, şehir) m³ ile yazarız. 1 m³ = 1000 dm³ = 1000 L. (s. 155)",
             "ek": "Litreden m³'e: 1000'e böl. m³'ten litreye: 1000 ile çarp. Kitapta diş fırçalarken boşa akan su, olimpik havuz büyüklüğüyle karşılaştırılıyor. (s. 155)",
             "akilda": "1 m³ = 1000 L",
             "cozum": {"baslik": "Boşa akan su",
                       "problem": "Diş fırçalarken musluk 2 dakika açık kalıyor ve dakikada 5 L su akıyor. 100 kişi birer kez diş fırçalarsa kaç m³ su boşa akar?",
                       "adimlar": [
                           {"metin": "Bir kişi bir kez.", "islem": "2 · 5 = 10 L"},
                           {"metin": "100 kişi.", "islem": "100 · 10 = 1000 L"},
                           {"metin": "Litreyi m³ yap: 1000 L = 1 m³.", "islem": "1000 ÷ 1000 = 1 m³"}],
                       "sonuc": "1 m³ su boşa akar. Musluğu kapatmak çok su kazandırır! (s. 155)"},
             "soru": S("Bir havuz 50 m³ su alıyor. Bu kaç litredir?", ["500", "5000", "50 000"], 2,
                       "1 m³ = 1000 L.", "50 · 1000 = 50 000 L. (s. 155)")}
        ],
        "biliyorMusun": [
            "Kitaptaki bilgiye göre diş fırçalarken musluk açık kalınca dakikada yaklaşık 5 litre su boşa akar. Bunu yapan herkesin harcadığı su, olimpik bir yüzme havuzunu bile doldurabilir. (s. 155)",
            "Anıtkabir'de mozolenin bulunduğu bölümde 44 sütun vardır. Kare prizma biçimindeki her sütunun tabanı 1,5 m, yüksekliği 14 m'dir. (s. 156)"],
        "akildaKalsin": [
            "Dört soru: Ne veriliyor? Kaplamak mı, doldurmak mı? Birimler aynı mı? Hesapla + birim.",
            "Kaç kutu sığar? Büyük hacim ÷ küçük hacim.",
            "Kaplama maliyeti = yüzey alanı × 1 birim karenin fiyatı.",
            "Suyun yüksekliği = hacim ÷ taban alanı.",
            "Eklenen cismin hacmi = taban alanı × yükselme.",
            "Büyük su miktarlarında 1 m³ = 1000 L."],
        "merakKutusu": [
            {"soru": "Kutular koliye tam sığmazsa ne olur?", "cevap": "Hacimleri bölmek yetmez; her kenara kaç kutu dizildiğine de bakmak gerekir. Bu konudaki sorularda kutular hep boşluksuz diziliyor. (s. 152)"},
            {"soru": "Neden önce birimleri eşitliyoruz?", "cevap": "dm ile cm çarpılınca anlamsız bir sonuç çıkar. Hepsini aynı birime çevirince sonuç doğru birimle çıkar."},
            {"soru": "Akvaryuma kum ekleyince neden daha az su sığar?", "cevap": "Kum akvaryumda yer kaplar. Akvaryumun hacminden su ve kumun hacmini çıkarınca kalan boşluk kadar su eklenebilir. (s. 154)"},
            {"soru": "Olimpik havuz ne kadar büyük?", "cevap": "Kitaptaki ölçüler 50 m, 25 m ve 2 m: 50 · 25 · 2 = 2500 m³, yani 2 500 000 litre su alır. (s. 155)"}],
        "dusunVeYaz": [{"soru": "Bir kutuyu kumaşla kaplamak ile içine kum doldurmak için hangi ölçüleri bulursun? Neden farklı?",
                        "ornekCevap": "Kaplamak için yüzey alanını, doldurmak için hacmi bulurum. Kumaş kutunun dışını kaplar, kum içini doldurur.",
                        "anahtarlar": ["yüzey", "hacim", "kapla", "doldur"]}],
        "sorular": [
            S("Bir problemi çözmeye başlarken ilk ne yaparız?", ["Hemen sayıları çarparız.", "Ne verildiğini ve ne istendiğini buluruz.", "Bütün sayıları toplarız."], 1,
              "Dört sorunun ilki.", "Önce ne verildiğini ve ne istendiğini buluruz; sonra kaplamak mı doldurmak mı diye sorarız.", kavram="Problem İskeleti"),
            G("Bir rafın içi 8 dm, 2 dm ve 2 dm. Ayrıtı 2 dm olan küp kutular rafa boşluk kalmadan dizilecek. Kaç kutu sığar?", "4",
              "Rafın hacmini bir kutunun hacmine böl.", "Raf 8 · 2 · 2 = 32 dm³, kutu 2 · 2 · 2 = 8 dm³. 32 ÷ 8 = 4. (s. 152)", kavram="Kaç Kutu Sığar?",
              yardim={"adimlar": ["Kaplamak mı, doldurmak mı? Kutular rafı dolduruyor: hacim.", "Rafın hacmi: 8 · 2 · 2.", "Kutunun hacmi: 2 · 2 · 2.", "Büyük hacmi küçük hacme böl."]}),
            G("Ayrıtı 3 dm olan küp şeklindeki bir kutunun bütün yüzleri kaplanacak. Kumaşın 1 dm²'si 2 TL. Kumaş kaç TL tutar?", "108",
              "Önce yüzey alanını bul, sonra fiyatla çarp.", "Bir yüz 3 · 3 = 9 dm². 6 · 9 = 54 dm². 54 · 2 = 108 TL. (s. 153)", birim="TL", kavram="Kaplama Maliyeti",
              yardim={"adimlar": ["Kaplamak mı, doldurmak mı? Kaplamak: yüzey alanı.", "Bir yüz: 3 · 3. Küpün 6 yüzü var.", "Birimler aynı (dm²). Yüzey alanını 2 TL ile çarp."]}),
            G("Tabanı 5 dm × 2 dm olan bir akvaryuma 30 L su kondu. Su kaç dm yüksekliğe çıkar?", "3",
              "30 L = 30 dm³. Hacmi taban alanına böl.", "Taban alanı 5 · 2 = 10 dm². 30 ÷ 10 = 3 dm. (s. 154)", birim="dm", kavram="Suyun Yüksekliği",
              svg=akvaryum_svg("5 dm", "2 dm", "4 dm", 0.75, "? dm"),
              yardim={"adimlar": ["Ne isteniyor? Suyun yüksekliği.", "Birimler aynı mı? 30 L = 30 dm³.", "Taban alanı: 5 · 2.", "Hacmi taban alanına böl."]}),
            G("Tabanı 20 cm × 15 cm olan bir akvaryuma taşlar konunca su 2 cm yükseldi. Taşların hacmi kaç cm³?", "600",
              "Taban alanını yükselmeyle çarp.", "20 · 15 = 300 cm². 300 · 2 = 600 cm³. (s. 154)", birim="cm³", kavram="Eklenen Cismin Hacmi",
              yardim={"adimlar": ["Ne isteniyor? Taşların hacmi.", "Taban alanı: 20 · 15.", "Taban alanını yükselmeyle (2 cm) çarp."]}),
            G("Bir su deposu 3 m³ su alıyor. Bu kaç litredir?", "3000", "1 m³ = 1000 L.", "3 · 1000 = 3000 L. (s. 155)", birim="L", kavram="Litre mi, Metreküp mü?",
              yardim={"adimlar": ["1 m³ kaç litre?", "3'ü 1000 ile çarp."]}),
            S("Bir kolinin ayrıtları 4 dm, 4 dm ve 2 dm. Ayrıtları 4 dm, 2 dm ve 1 dm olan kutular koliye boşluk kalmadan dizilecek. Kaç kutu sığar?", ["4", "8", "16"], 0,
              "İki hacmi bul, büyüğü küçüğe böl.", "Koli 4 · 4 · 2 = 32 dm³, kutu 4 · 2 · 1 = 8 dm³. 32 ÷ 8 = 4. (s. 152)", kavram="Kaç Kutu Sığar?",
              yardim={"adimlar": ["Kolinin hacmi: 4 · 4 · 2.", "Kutunun hacmi: 4 · 2 · 1.", "Büyük hacmi küçük hacme böl."]}),
            S("Tabanları aynı iki akvaryumdan ikincisine birincinin 2 katı su kondu. İkinci akvaryumdaki suyun yüksekliği için ne söylenebilir?",
              ["Aynı kalır.", "Yarısı olur.", "2 katı olur."], 2,
              "Yükseklik = hacim ÷ taban alanı. Taban aynı.", "Taban alanı aynı, hacim 2 katı: yükseklik de 2 katı olur. (s. 154)", kavram="Suyun Yüksekliği"),
            G("Diş fırçalarken musluk 2 dakika açık kalıyor ve dakikada 5 L su akıyor. 4 kişilik bir aile günde 2 kez diş fırçalarsa kaç litre su boşa akar?", "80",
              "Bir kişinin bir kez fırçalamasıyla başla.", "Bir fırçalama 2 · 5 = 10 L. 4 kişi · 2 kez = 8 fırçalama. 8 · 10 = 80 L. (s. 155)", birim="L", kavram="Problem İskeleti",
              yardim={"adimlar": ["Ne veriliyor? 2 dakika, dakikada 5 L, 4 kişi, günde 2 kez.", "Bir fırçalamada: 2 · 5.", "Toplam kaç fırçalama var? 4 · 2.", "Fırçalama sayısını bir fırçalamadaki suyla çarp."]}),
            S("Tabanı 30 cm × 20 cm olan bir akvaryuma kum eklenince su 1 cm yükseldi. Kumun hacmi kaç cm³'tür?", ["600", "60", "50"], 0,
              "Taban alanını yükselmeyle çarp.", "30 · 20 = 600 cm². 600 · 1 = 600 cm³. (s. 154)", kavram="Eklenen Cismin Hacmi")]
    }


# =================================================================
def u2t4():
    return {
        "id": "u2t4", "tur": "tarama", "unite": T2,
        "baslik": "Tema Sonu Taraması", "sayfalar": "Konu 1–8 · s. 118–158",
        "giris": "İkinci temanın sonuna geldin, tebrikler! Şimdi 8 konuyu birlikte gözden geçireceğiz. Önce kısa özetleri oku ve kartları çevir. Sonra tarama testini çöz. Not yok; neyi iyi bildiğini ve neye tekrar bakman gerektiğini bulacağız.",
        "buyukResim": "Bu temada kutularla bir yolculuk yaptık. Önce küp yapılarına altı yönden baktık. Sonra kutuyu açıp yüzlerini gördük ve yüzey alanını bulduk: kaplamak. Ardından kutunun içini birim küplerle doldurup hacmi bulduk: doldurmak. Hacmi m³, dm³, cm³ ve litreyle ölçmeyi öğrendik. En sonunda hepsini gerçek hayat problemlerinde birlikte kullandık.",
        "kapsar": ["u2k1", "u2k2", "u2k3", "u2k4", "u2k5", "u2k6", "u2k7", "u2k8"],
        "hatirla": [
            {"konu": "u2k1", "maddeler": [
                "Bir yapıya altı yönden bakılır; her küp yüzü kare görünür.",
                "Öndeki küp arkasındakini saklar."]},
            {"konu": "u2k2", "maddeler": [
                "Dikdörtgenler prizması: 6 yüz, 12 ayrıt, 8 köşe; karşılıklı yüzler eş.",
                "Açınım kapanınca eş yüzler karşılıklı gelir."]},
            {"konu": "u2k3", "maddeler": [
                "Yüzey alanı = 2 · (a · b + a · c + b · c); küpte 6 · a².",
                "Kaplamak = yüzey alanı (cm²)."]},
            {"konu": "u2k4", "maddeler": [
                "Hacim, cismin kapladığı yerdir; birim küplerle ölçülür.",
                "Doldurmak = hacim (cm³)."]},
            {"konu": "u2k5", "maddeler": [
                "Hacim = a · b · c; küpte a³.",
                "Bir ayrıt 2 katı → hacim 2 katı."]},
            {"konu": "u2k6", "maddeler": [
                "m³ → dm³ → cm³ → mm³: aşağı × 1000, yukarı ÷ 1000.",
                "Ayrıtların birimi farklıysa önce eşitle."]},
            {"konu": "u2k7", "maddeler": [
                "1 dm³ = 1 L, 1 cm³ = 1 mL.",
                "L → dL → cL → mL: her basamak × 10."]},
            {"konu": "u2k8", "maddeler": [
                "Ne veriliyor? Kaplamak mı, doldurmak mı? Birimler aynı mı? Hesapla.",
                "Kaç kutu: büyük hacim ÷ küçük hacim; su yüksekliği: hacim ÷ taban alanı."]}],
        "eskiSoru": 6,
        "oyunKavram": 10,
        "gruplar": [{"soru": "Kaplamak mı, doldurmak mı, çevirmek mi?", "kutular": [
            {"etiket": "Kaplamak (yüzey alanı)", "uyeler": ["Yüzey Alanı Formülü", "Kaplama Maliyeti"]},
            {"etiket": "Doldurmak (hacim)", "uyeler": ["Hacim Formülü", "Kaç Kutu Sığar?", "Suyun Yüksekliği"]},
            {"etiket": "Birim çevirmek", "uyeler": ["Hacim Basamakları", "Sıvı Basamakları"]}]}],
        "sorular": [
            S("Ayrıtları 3 dm, 2 dm ve 2 dm olan kapaklı bir kutu için hangisi doğrudur?",
              ["İçine 12 L su sığar.", "İçine 32 L su sığar.", "Dışını kaplamak için 12 dm² kumaş yeter."], 0,
              "Doldurmak = hacim (3 · 2 · 2); kaplamak = yüzey alanı.",
              "Hacim 3 · 2 · 2 = 12 dm³ = 12 L. Yüzey alanı 2 · (6 + 6 + 4) = 32 dm²; kaplamak için 32 dm² gerekir.",
              kaynak=[K("u2k3", "Yüzey Alanı Formülü"), K("u2k5", "Hacim Formülü"), K("u2k7", "1 dm³ = 1 L")],
              yardim={"adimlar": ["Doldurmak = hacim: 3 · 2 · 2. dm³'ü litreye çevir.", "Kaplamak = yüzey alanı: 2 · (3 · 2 + 3 · 2 + 2 · 2).", "Her şıkta “sığar” mı, “kaplamak” mı yazıyor, kontrol et."]}),
            G("Görseldeki yapı, ayrıtı 1 cm olan eş küplerden yapılmış kutu biçiminde bir yapıdır. Hacmi kaç cm³?", "12",
              "Arkadaki saklı küpleri de say: bir katman × katman sayısı.", "Bir katman 3 · 2 = 6 küp, 2 katman: 12 küp. Her küp 1 cm³: 12 cm³.",
              birim="cm³", svg=svg_dolu(kutu(3, 2, 2), s=34),
              kaynak=[K("u2k1", "Saklanan Küpler"), K("u2k4", "Birim Küp Cinsinden Hacim")],
              yardim={"adimlar": ["Kaplamak mı, doldurmak mı? Doldurmak: hacim.", "Alt katman: önde 3 küp, arkasında saklı bir sıra daha.", "Kaç katman var?", "Bir katmanı katman sayısıyla çarp."]}),
            G("Açınımı 6 eş kareden oluşan bir kutunun her karesinin kenarı 2 dm. Bu kutu kaç litre su alır?", "8",
              "6 eş kare: kutu bir küp. Hacmini bul, litreye çevir.", "Küpün ayrıtı 2 dm: 2 · 2 · 2 = 8 dm³ = 8 L.", birim="L",
              kaynak=[K("u2k2", "Yüzey Açınımı"), K("u2k5", "Kare Prizma ve Küp"), K("u2k7", "1 dm³ = 1 L")],
              yardim={"adimlar": ["6 eş kareden oluşan açınım hangi cismin açınımıdır?", "Küpün hacmi: 2 · 2 · 2.", "dm³'ü litreye çevir."]}),
            G("Tabanı 4 dm × 3 dm olan bir akvaryumda 24 L su var. Su kaç dm yüksekliktedir?", "2",
              "24 L = 24 dm³. Hacmi taban alanına böl.", "Taban alanı 4 · 3 = 12 dm². 24 ÷ 12 = 2 dm.", birim="dm",
              kaynak=[K("u2k8", "Suyun Yüksekliği"), K("u2k7", "1 dm³ = 1 L")],
              yardim={"adimlar": ["Ne isteniyor? Suyun yüksekliği.", "Birimler aynı mı? 24 L = 24 dm³.", "Taban alanı: 4 · 3.", "Hacmi taban alanına böl."]}),
            S("1 m³ su kaç litredir?", ["100", "1000", "10 000"], 1,
              "1 m³ = 1000 dm³ ve 1 dm³ = 1 L.", "1 m³ = 1000 dm³ = 1000 L.",
              kaynak=[K("u2k6", "1 m³ = 1000 dm³"), K("u2k8", "Litre mi, Metreküp mü?")]),
            G("Bir kolinin ayrıtları 50 cm, 30 cm ve 80 cm. Kolinin hacmi kaç dm³?", "120",
              "Önce ayrıtları dm'ye çevir.", "5 dm, 3 dm, 8 dm. 5 · 3 · 8 = 120 dm³. (s. 156)", birim="dm³",
              kaynak=[K("u2k6", "Önce Birimleri Eşitle"), K("u2k5", "Hacim Formülü")],
              yardim={"adimlar": ["Kaplamak mı, doldurmak mı? Hacim.", "Birimleri dm yap: 50 cm = 5 dm, 30 cm = 3 dm, 80 cm = 8 dm.", "Önce 5 · 3.", "Sonucu 8 ile çarp."]}),
            G("Ayrıtları 3 m, 4 m ve 5 m olan prizmanın hacmi 60 m³'tür. Bu prizmanın yüzey alanı kaç m²?", "94",
              "Üç farklı yüzün alanını topla, 2 ile çarp.", "Yüzler 3 · 4 = 12, 3 · 5 = 15, 4 · 5 = 20. 2 · (12 + 15 + 20) = 94 m². (s. 157)", birim="m²",
              kaynak=[K("u2k3", "Yüzey Alanı Formülü"), K("u2k5", "Hacim Formülü")],
              yardim={"adimlar": ["Kaplamak mı, doldurmak mı? Yüzey alanı soruluyor.", "Üç farklı yüz: 3 · 4, 3 · 5, 4 · 5.", "Üçünü topla.", "Toplamı 2 ile çarp."]}),
            S("Hangisinde hacim bulunur?", ["Duvarı boyamak", "Kutuyu kâğıtla kaplamak", "Havuzu suyla doldurmak"], 2,
              "Kaplamak mı, doldurmak mı?", "Boyamak ve kaplamak yüzey alanıdır. Su havuzu doldurur: hacim.",
              kaynak=[K("u2k4", "Kaplamak mı, Doldurmak mı?"), K("u2k8", "Problem İskeleti")])]
    }


# =================================================================
# 3. TEMA: İSTATİSTİKSEL ARAŞTIRMA
# Kitap dışı kararlar (Kemal'e bildirildi): "sayarak mı, ölçerek mi?" stratejisi ve karar ağacı (asıl kural: arada başka değer
# olabilir mi?), kesikli = merdiven / sürekli = rampa benzetmesi, örneklem için çorba benzetmesi. Kitabın öğrenciye bıraktığı
# sonuçlar (Defne'nin soruları s. 165, Aras'ın termometresi s. 168) Bilgi Kutusu/Hatırlatma metninden türetildi.
T3 = "3. Tema: İstatistiksel Araştırma"
P31, P32, P33 = "(s. 159–164)", "(s. 165–168)", "(s. 169–170, 192–193)"
KAT, NIC, KES, SUR = "#ff8fb1", "#4fc3a1", "#8ce99a", "#c3a6ff"   # SVG koyu zemininde açık tonlar


def _kutu(x, y, w, h, yazi, renk, boy=10, yazi_renk="#1b2340"):
    return (f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='7' fill='{renk}'/>"
            + txt(x + w / 2, y + h / 2 + boy * 0.36, yazi, yazi_renk, boy))


def _ok(x1, y1, x2, y2, renk="#f5f6fa"):
    return f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{renk}' stroke-width='2.5' stroke-linecap='round'/>"


def sutun_svg(etiketler, degerler, ust=None, w=330, h=160, renk=TEAL, baslik=None):
    """Basit sütun grafiği (şeffaf zemin)."""
    ust = ust or max(degerler)
    x0, y0, yuk = 40, h - 26, h - 52
    g = _ok(x0, y0, w - 10, y0) + _ok(x0, y0, x0, y0 - yuk - 6)
    for i in range(0, ust + 1, max(1, ust // 5)):
        y = y0 - yuk * i / ust
        g += f"<line x1='{x0}' y1='{y}' x2='{w - 10}' y2='{y}' stroke='#3a4570' stroke-width='1'/>" + txt(x0 - 8, y + 4, str(i), "#f5f6fa", 11, 600, "end")
    adim = (w - 10 - x0) / len(degerler)
    for i, (e, d) in enumerate(zip(etiketler, degerler)):
        bx = x0 + adim * i + adim * 0.22
        bh = yuk * d / ust
        g += f"<rect x='{bx:.1f}' y='{y0 - bh:.1f}' width='{adim * 0.56:.1f}' height='{bh:.1f}' rx='3' fill='{renk}'/>"
        g += txt(bx + adim * 0.28, y0 + 16, e, "#f5f6fa", 11, 600)
    if baslik:
        g += txt(w / 2, 14, baslik, "#f2c14e", 12)
    return gsvg(w, h, g)


def karar_agaci_svg(w=330, h=176):
    g = _kutu(105, 6, 120, 26, "Cevap sayı mı?", "#f2c14e", 12)
    g += _ok(140, 32, 62, 56) + _ok(190, 32, 252, 56)
    g += txt(70, 40, "hayır", "#f5f6fa", 10, 600) + txt(262, 40, "evet", "#f5f6fa", 10, 600)
    g += _kutu(10, 58, 104, 26, "Kategorik", KAT, 12) + _kutu(206, 58, 96, 26, "Nicel", NIC, 12)
    g += _ok(254, 84, 254, 96)
    g += _kutu(170, 96, 156, 26, "Arada değer olur mu?", "#f2c14e", 11)
    g += _ok(220, 122, 186, 140) + _ok(278, 122, 300, 140)
    g += txt(174, 130, "hayır", "#f5f6fa", 10, 600) + txt(316, 128, "evet", "#f5f6fa", 10, 600)
    g += _kutu(130, 142, 96, 30, "Kesikli", KES, 12) + _kutu(234, 142, 92, 30, "Sürekli", SUR, 12)
    g += txt(56, 112, "sözcük:", "#ff8fb1", 10, 600) + txt(56, 126, "renk, ders", "#ff8fb1", 10, 600)
    return gsvg(w, h, g)


def svg3_veri():
    g = "<rect x='28' y='16' width='64' height='88' rx='8' fill='#f5f6fa'/><rect x='44' y='10' width='32' height='12' rx='4' fill='#f2c14e'/>"
    for i, s in enumerate(["88", "95", "118", "132"]):
        g += txt(60, 42 + i * 17, s, "#1b2340", 13)
    return bg(g + txt(60, 113, "veri seti", "#f2c14e", 11))


def svg3_kategorik():
    g = _kutu(12, 20, 46, 24, "mavi", "#6fb3ff", 11) + _kutu(62, 20, 46, 24, "yeşil", "#8ce99a", 11)
    g += _kutu(12, 52, 46, 24, "Fen", KAT, 11) + _kutu(62, 52, 46, 24, "Türkçe", KAT, 10)
    g += _kutu(22, 84, 76, 20, "otobüs", "#f2c14e", 11)
    return bg(g + txt(60, 113, "sözcükle", KAT, 11))


def svg3_nicel():
    g = txt(36, 46, "3", NIC, 26) + txt(84, 46, "1,5", NIC, 22) + txt(60, 88, "24,75", NIC, 22)
    return bg(g + txt(60, 112, "sayıyla", NIC, 11))


def svg3_kesikli():
    g = ""
    for i in range(4):   # merdiven
        g += f"<rect x='{14 + i * 24}' y='{86 - i * 18}' width='24' height='{18 + i * 18}' fill='{KES}' opacity='{0.55 + i * 0.15}'/>"
        g += txt(26 + i * 24, 82 - i * 18, str(i), "#f5f6fa", 12)
    return bg(g + txt(60, 113, "basamak basamak", KES, 11))


def svg3_surekli():
    g = f"<path d='M12 98 L108 30 L108 98 Z' fill='{SUR}' opacity='0.8'/>"
    g += "<circle cx='60' cy='64' r='5' fill='#f2c14e'/>" + txt(44, 54, "1,505", "#f2c14e", 11)
    return bg(g + txt(60, 113, "her noktada dur", SUR, 11))


def svg3_adimlar():
    g = ""
    for i, (e, r) in enumerate([("Sor", "#f2c14e"), ("Topla", NIC), ("Analiz et", SUR), ("Yorumla", KAT)]):
        y = 20 + i * 26
        g += f"<circle cx='26' cy='{y}' r='11' fill='{r}'/>" + txt(26, y + 5, str(i + 1), "#1b2340", 13)
        g += txt(44, y + 5, e, "#f5f6fa", 12, 700, "start")
    return bg(g)


def svg3_h_sutun():
    g = _ok(18, 96, 108, 96) + _ok(18, 96, 18, 18)
    for i, (d, e) in enumerate([(3, "Pt"), (5, "Sa"), (2, "Ça")]):
        g += f"<rect x='{28 + i * 27}' y='{96 - d * 14}' width='18' height='{d * 14}' rx='2' fill='{TEAL}'/>" + txt(37 + i * 27, 110, e, "#f5f6fa", 10, 600)
    g += "<line x1='18' y1='26' x2='64' y2='26' stroke='#f2c14e' stroke-width='1.5' stroke-dasharray='3 3'/>" + txt(12, 30, "5", "#f2c14e", 10)
    return bg(g)


def svg3_h_arada():
    g = _ok(12, 64, 108, 64)
    g += "<line x1='20' y1='56' x2='20' y2='72' stroke='#f5f6fa' stroke-width='3'/><line x1='100' y1='56' x2='100' y2='72' stroke='#f5f6fa' stroke-width='3'/>"
    g += txt(20, 90, "1", "#f5f6fa", 14) + txt(100, 90, "2", "#f5f6fa", 14)
    g += "<circle cx='60' cy='64' r='6' fill='#f2c14e'/>" + txt(60, 48, "1,5", "#f2c14e", 14)
    return bg(g + txt(60, 112, "arada hep sayı", "#f2c14e", 11))


def svg3_soru():
    g = txt(60, 64, "?", "#f2c14e", 52)
    for i in range(5):
        g += f"<circle cx='{20 + i * 20}' cy='92' r='7' fill='{NIC}'/>"
    return bg(g + txt(60, 114, "bütün grup", NIC, 11))


def svg3_iyi_soru():
    g = ""
    for i, s in enumerate(["amaç net", "ölçülebilir", "toplanabilir"]):
        y = 30 + i * 28
        g += f"<rect x='14' y='{y - 12}' width='18' height='18' rx='4' fill='#8ce99a'/>"
        g += f"<path d='M18 {y - 3} l4 4 l7 -9' stroke='#1b2340' stroke-width='3' fill='none'/>" + txt(38, y + 3, s, "#f5f6fa", 11, 700, "start")
    return bg(g)


def svg3_degisebilir():
    g = _ok(14, 96, 106, 96)
    for i, (hh, r) in enumerate([(40, NIC), (62, "#f2c14e"), (30, KAT), (52, SUR)]):
        g += f"<circle cx='{26 + i * 23}' cy='{90 - hh}' r='7' fill='{r}'/><rect x='{21 + i * 23}' y='{96 - hh}' width='10' height='{hh}' rx='3' fill='{r}'/>"
    return bg(g + txt(60, 114, "herkes farklı", "#f2c14e", 11))


def _noktalar(cx, cy, r, renk, n=18, rr=3.2):
    import math
    g = ""
    for i in range(n):
        a, d = i * 2.4, r * math.sqrt((i + 0.5) / n)
        g += f"<circle cx='{cx + d * math.cos(a):.1f}' cy='{cy + d * math.sin(a):.1f}' r='{rr}' fill='{renk}'/>"
    return g


def svg3_evren():
    g = f"<circle cx='60' cy='54' r='42' fill='none' stroke='#f2c14e' stroke-width='3'/>" + _noktalar(60, 54, 36, "#f5f6fa", 40)
    return bg(g + txt(60, 112, "en geniş grup", "#f2c14e", 11))


def svg3_orneklem():
    g = f"<circle cx='60' cy='54' r='42' fill='none' stroke='#f2c14e' stroke-width='3'/>" + _noktalar(60, 54, 36, "#5a6280", 40)
    g += f"<circle cx='74' cy='64' r='18' fill='none' stroke='{NIC}' stroke-width='3'/>" + _noktalar(74, 64, 13, NIC, 7)
    return bg(g + txt(60, 112, "küçük grup", NIC, 11))


def svg3_temsil():
    g = "<path d='M22 50 h76 l-8 42 h-60 z' fill='#f2c14e'/><ellipse cx='60' cy='50' rx='38' ry='8' fill='#ffa94d'/>"
    g += "<path d='M84 18 l-18 34' stroke='#f5f6fa' stroke-width='4' stroke-linecap='round'/><ellipse cx='64' cy='54' rx='8' ry='4' fill='#f5f6fa'/>"
    return bg(g + txt(60, 112, "bir kaşık yeter", "#f2c14e", 11))


def svg3_anket():
    g = "<rect x='26' y='12' width='68' height='90' rx='8' fill='#f5f6fa'/>"
    for i, s in enumerate(["1. Kaç saat", "uyuyorsun?", "____"]):
        g += txt(60, 36 + i * 18, s, "#1b2340", 10)
    g += f"<circle cx='42' cy='88' r='5' fill='{NIC}'/><circle cx='60' cy='88' r='5' fill='{NIC}'/><circle cx='78' cy='88' r='5' fill='{NIC}'/>"
    return bg(g + txt(60, 113, "her kişiye", NIC, 11))


def svg3_plan():
    g = ""
    for i, s in enumerate(["Nerede?", "Ne zaman?", "Nasıl?", "Kaydet"]):
        g += _kutu(18, 12 + i * 24, 84, 20, s, ["#f2c14e", NIC, SUR, KAT][i], 11)
    return bg(g + txt(60, 114, "önce plan", "#f2c14e", 11))


def svg3_kaynak():
    g = "<path d='M60 12 l38 14 v26 c0 26 -18 42 -38 50 c-20 -8 -38 -24 -38 -50 v-26 z' fill='#4fc3a1'/>"
    g += txt(60, 56, "gov.tr", "#1b2340", 14) + txt(60, 74, "edu.tr", "#1b2340", 12)
    return bg(g)


def svg3_kisisel():
    g = "<rect x='16' y='26' width='88' height='56' rx='8' fill='#f5f6fa'/><circle cx='38' cy='50' r='11' fill='#ffa94d'/>"
    g += "<rect x='56' y='40' width='38' height='6' rx='3' fill='#5a6280'/><rect x='56' y='52' width='30' height='6' rx='3' fill='#5a6280'/><rect x='26' y='66' width='68' height='6' rx='3' fill='#5a6280'/>"
    return bg(g + txt(60, 104, "kişiye ait", "#f2c14e", 11))


def svg3_izin():
    g = "<rect x='34' y='52' width='52' height='42' rx='8' fill='#f2c14e'/><path d='M44 52 v-12 a16 16 0 0 1 32 0 v12' stroke='#f2c14e' stroke-width='7' fill='none'/>"
    g += "<circle cx='60' cy='70' r='6' fill='#1b2340'/><rect x='57' y='72' width='6' height='12' fill='#1b2340'/>"
    return bg(g + txt(60, 112, "izin al, gizli tut", "#f2c14e", 11))


def svg3_kvkk():
    g = "<path d='M60 12 l38 14 v26 c0 26 -18 42 -38 50 c-20 -8 -38 -24 -38 -50 v-26 z' fill='#c3a6ff'/>"
    g += txt(60, 62, "KVKK", "#1b2340", 18)
    return bg(g)


# =================================================================
def u3k1():
    return {
        "id": "u3k1", "unite": T3, "baslik": "Veri Türleri", "sayfalar": "s. 159–164",
        "giris": "Her gün bir sürü bilgi topluyoruz: kaç saat uyuduğumuz, kaç kardeşimiz olduğu, en sevdiğimiz renk. Bu bilgilere veri denir. Bu konuda verileri türlerine ayırmayı öğreneceğiz. Sonra bir araştırmanın 4 adımını tanıyacağız.",
        "hazirlik": {
            "baslik": "Hazır mısın?",
            "giris": "Bu konuda grafik okuyacağız ve ondalık sayılarla karşılaşacağız. Önce bunları hatırlıyor musun bakalım. Not yok.",
            "maddeler": [
                {"ad": "Sütun grafiği okuma", "sinif": "Önceki yıllar", "svg": svg3_h_sutun(),
                 "anlatim": "Sütun grafiğinde her sütunun boyu bir sayıyı gösterir. Sütunun tepesinden sola, sayıların yazdığı eksene bakarak değeri okuruz.",
                 "akilda": "Sütunun tepesi = değer",
                 "ornek": {"problem": "Grafikte Salı günü kaç kitap okunmuş?", "adimlar": [
                     {"metin": "Salı sütununu bul.", "islem": "Sa"},
                     {"metin": "Sütunun tepesinden sola bak.", "islem": "5 kitap"}]},
                 "sorular": [
                     S("Grafiğe göre en çok kitap hangi gün okunmuş?", ["Pazartesi", "Salı", "Çarşamba"], 1,
                       "En uzun sütunu bul.", "En uzun sütun Salı'ya ait: 5 kitap.",
                       svg=sutun_svg(["Pzt", "Salı", "Çrş"], [3, 5, 2], 5, baslik="Okunan kitap sayısı")),
                     G("Grafiğe göre Pazartesi günü kaç kitap okunmuş?", "3", "Pazartesi sütununun tepesinden sola bak.", "Pazartesi sütunu 3'e kadar uzanıyor.",
                       svg=sutun_svg(["Pzt", "Salı", "Çrş"], [3, 5, 2], 5, baslik="Okunan kitap sayısı"),
                       yardim={"adimlar": ["Pazartesi sütununu bul.", "Tepesinden sola, sayı eksenine bak."]})]},
                {"ad": "İki sayı arasında başka sayı", "sinif": "1. tema, 5. konu", "svg": svg3_h_arada(),
                 "anlatim": "1 ile 2 arasında 1,5 vardır. 1,5 ile 2 arasında da 1,7 vardır. İki ondalık sayı arasında her zaman başka bir sayı bulunur.",
                 "akilda": "Arada hep bir sayı var",
                 "sayiDogrusu": {"min": 1, "max": 2, "bolme": 10, "isaretler": [{"x": 1.5, "etiket": "1,5", "renk": "#f2c14e"}]},
                 "sorular": [
                     S("1,4 ile 1,5 arasında başka bir sayı var mı?", ["Yok", "Var, örneğin 1,45", "Var, örneğin 1,6"], 1,
                       "İki ondalık sayının arasına bir basamak daha ekleyebilirsin.", "1,40 ile 1,50 arasında 1,45 vardır."),
                     S("Hangisi 2 ile 3 arasındadır?", ["2,6", "3,2", "1,9"], 0,
                       "2'den büyük, 3'ten küçük sayıyı ara.", "2 < 2,6 < 3.")]}
            ]},
        "kavramlar": [
            {"ad": "Veri", "renk": "#b7791f", "svg": svg3_veri(),
             "aciklama": "Bir soruya cevap bulmak için topladığımız bilgilere veri denir. Toplanan verilerin hepsine birden veri seti deriz.",
             "ek": "Kitaptaki örnekte 26 öğrencinin bir haftada okuduğu sayfa sayıları (88, 95, 118 …) bir veri setidir. (s. 159)",
             "akilda": "Toplanan bilgi = veri",
             "soru": S("26 öğrencinin bir haftada okuduğu sayfa sayılarının hepsine birden ne denir?", ["Veri seti", "Grafik", "Araştırma sorusu"], 0,
                       "Bilgi kartındaki ikinci cümleye bak.", "Toplanan verilerin hepsine birden veri seti denir. (s. 159)")},
            {"ad": "Kategorik Veri", "renk": "#c2255c", "svg": svg3_kategorik(),
             "aciklama": "Sayıyla değil, sözcükle (bir grup adıyla) yazılan veriye kategorik veri denir. Örneğin en sevilen ders, göz rengi, okula geliş aracı.",
             "ek": "6. sınıftan hatırla: Cevaplar sözcüktür ama her grupta kaç kişi olduğunu sayabiliriz: “Fen: 12 kişi, İngilizce: 4 kişi” gibi.",
             "akilda": "Cevap sözcükse: kategorik",
             "soru": S("“En sevdiğin renk hangisi?” sorusunun cevapları hangi veri türüdür?", ["Nicel veri", "Sürekli veri", "Kategorik veri"], 2,
                       "Cevaplar sayı mı, sözcük mü?", "Cevaplar sözcüktür (mavi, yeşil …): kategorik veri.")},
            {"ad": "Nicel Veri", "renk": "#1f9e8f", "svg": svg3_nicel(),
             "aciklama": "Sayısal olarak ifade edilebilen verilere nicel veri denir. (s. 163)",
             "ek": "Kardeş sayısı, boy uzunluğu, bir ürünün fiyatı nicel veridir. Nicel veriler ikiye ayrılır: kesikli ve sürekli. (s. 163)",
             "akilda": "Cevap sayıysa: nicel",
             "soru": S("Hangisi nicel veridir?", ["Okuldaki öğrenci sayısı", "Tuttuğun takım", "Doğduğun şehir"], 0,
                       "Sayıyla yazılanı bul.", "Öğrenci sayısı sayıyla yazılır: nicel veri. (s. 163)")},
            {"ad": "Kesikli Veri", "renk": "#2f8f73", "svg": svg3_kesikli(),
             "aciklama": "Kesikli veri, iki değer arasında başka değer alamaz. Genelde sayarak bulunur: 2 kardeş olur, 2,5 kardeş olmaz. (s. 163)",
             "ek": "Kardeş sayısı, kitaplıktaki kitap sayısı, atılan gol sayısı, okuldaki öğrenci sayısı kesikli veridir (s. 163). Merdiven gibi düşün: basamaktan basamağa atlarsın, arada duramazsın.",
             "akilda": "Sayarak bulunur: kesikli",
             "cozum": {"baslik": "Hangi veri türü?",
                       "problem": "Bir sınıftaki öğrencilerin kardeş sayıları hangi veri türüdür?",
                       "svg": karar_agaci_svg(),
                       "adimlar": [
                           {"metin": "Cevap sayı mı, sözcük mü? Sayı: 0, 1, 2, 3 …", "islem": "Sayı → nicel"},
                           {"metin": "Bu sayıyı sayarak mı, ölçerek mi buluyoruz? Kardeşlerimizi sayarız.", "islem": "Sayarak → kesikli"},
                           {"metin": "Kontrol et: 2 kardeş ile 3 kardeş arasında başka değer var mı? 2,5 kardeş olmaz.", "islem": "Arada değer yok ✓"}],
                       "sonuc": "Kardeş sayısı kesikli veridir. (s. 163)"},
             "sende": {"baslik": "Sıra sende",
                       "problem": "Bir maçta atılan gol sayıları hangi veri türüdür?",
                       "adimlar": [
                           {"metin": "Cevap sayı mı, sözcük mü?",
                            "soru": S("Gol sayısının cevabı nasıl yazılır?", ["Sayıyla: 0, 1, 2 …", "Sözcükle: takım adı", "Renkle"], 0,
                                      "“Kaç gol?” diye soruyoruz.", "Gol sayısı 0, 1, 2 … diye sayıyla yazılır."),
                            "islem": "Sayı → nicel"},
                           {"metin": "Sayarak mı, ölçerek mi?",
                            "soru": S("Golleri nasıl buluruz?", ["Cetvelle ölçerek", "Sayarak", "Tartarak"], 1,
                                      "Bir gol, iki gol …", "Golleri tek tek sayarız; 1,5 gol olmaz."),
                            "islem": "Sayarak → kesikli"}],
                       "sonuc": "Harika! Gol sayısı kesikli veridir. (s. 163)"},
             "soru": S("Hangisi kesikli veridir?", ["Boy uzunluğu", "Vücut sıcaklığı", "Kitaplıktaki kitap sayısı"], 2,
                       "Hangisini sayarak buluruz?", "Kitapları tek tek sayarız; 3,5 kitap olmaz: kesikli veri. (s. 163)")},
            {"ad": "Sürekli Veri", "renk": "#7b4fc9", "svg": svg3_surekli(),
             "aciklama": "Sürekli veri, iki ölçüm arasında sınırsız değer alabilir. Genelde ölçerek bulunur: boy 1,50 m, 1,505 m … olabilir. (s. 163)",
             "ek": "Boy uzunluğu, aylık yağış miktarı, vücut sıcaklığı, ürünlerin fiyatları sürekli veridir (s. 163). Rampa gibi düşün: her noktada durabilirsin. Emin olamazsan sor: “Arada başka değer olabilir mi?”",
             "akilda": "Ölçerek bulunur: sürekli",
             "cozum": {"baslik": "Bitkinin boyu",
                       "problem": "Humuslu toprakta yetişen bir bitkinin boyu 4 haftada 2,0 cm'den 10,0 cm'ye çıkmış. Bitki boyu hangi veri türüdür?",
                       "adimlar": [
                           {"metin": "Cevap sayı mı? Evet: 2,0 cm, 5,5 cm, 8,7 cm …", "islem": "Sayı → nicel"},
                           {"metin": "Boyu sayarak mı, ölçerek mi buluruz? Cetvelle ölçeriz.", "islem": "Ölçerek → sürekli"},
                           {"metin": "Kontrol et: 5,5 cm ile 5,6 cm arasında 5,55 cm olabilir mi? Evet.", "islem": "Arada değer var ✓"}],
                       "sonuc": "Bitki boyu sürekli veridir. (s. 163)"},
             "sende": {"baslik": "Sıra sende",
                       "problem": "Bir ürünün fiyatı 24,75 TL. Fiyat hangi veri türüdür?",
                       "adimlar": [
                           {"metin": "Cevap sayı: 24,75.", "islem": "Sayı → nicel"},
                           {"metin": "Arada başka değer olabilir mi?",
                            "soru": S("24,75 TL ile 24,80 TL arasında başka fiyat olabilir mi?", ["Hayır, olamaz.", "Evet, 24,78 TL gibi.", "Sadece 25 TL olabilir."], 1,
                                      "İki ondalık sayının arasında hep başka sayı vardır.", "24,75 < 24,78 < 24,80: arada değer var."),
                            "islem": "Arada değer var → sürekli"}],
                       "sonuc": "Harika! Ürünlerin fiyatları sürekli veridir. (s. 163)"},
             "soru": S("Hangisi sürekli veridir?", ["Kardeş sayısı", "Aylık yağış miktarı", "Atılan gol sayısı"], 1,
                       "Hangisini ölçerek buluruz?", "Yağış miktarı ölçülür; arada sınırsız değer olabilir: sürekli veri. (s. 163)")},
            {"ad": "Araştırmanın 4 Adımı", "renk": "#5f3dc4", "svg": svg3_adimlar(),
             "aciklama": "İstatistiksel araştırma 4 adımda yapılır: 1) Araştırma sorusunu belirle, 2) Verileri topla, 3) Verileri analiz et, 4) Yorumla ve karar ver. (s. 164)",
             "ek": "Analiz adımında veriler grafikle gösterilir ve veri setini temsil edecek değer bulunur. Bir adım uygun gitmezse geri dönülüp yeniden planlanabilir. (s. 164)",
             "akilda": "Sor, topla, analiz et, yorumla",
             "soru": S("Araştırmanın ilk adımı hangisidir?", ["Araştırma sorusunu belirlemek", "Verileri toplamak", "Grafik çizmek"], 0,
                       "Bilgi kartında 1 numaralı adıma bak.", "Önce araştırma sorusu belirlenir, sonra veriler toplanır. (s. 164)")}
        ],
        "gruplar": [{"soru": "Hangi grupta?", "kutular": [
            {"etiket": "Sözcükle yazılır", "uyeler": ["Kategorik Veri"]},
            {"etiket": "Sayıyla yazılır", "uyeler": ["Nicel Veri", "Kesikli Veri", "Sürekli Veri"]},
            {"etiket": "Araştırmanın parçası", "uyeler": ["Veri", "Araştırmanın 4 Adımı"]}]}],
        "akildaKalsin": [
            "Bir soruya cevap için topladığımız bilgilere veri denir.",
            "Cevap sözcükse kategorik, sayıysa nicel veridir.",
            "Kesikli veri: arada değer yok, genelde sayarak bulunur (kardeş sayısı).",
            "Sürekli veri: arada sınırsız değer var, genelde ölçerek bulunur (boy uzunluğu).",
            "Emin değilsen sor: “Arada başka değer olabilir mi?”",
            "Araştırmanın 4 adımı: Sor, topla, analiz et, yorumla."],
        "merakKutusu": [
            {"soru": "Uyku süresi hangi veri türüdür?", "cevap": "Uyku süresi ölçülür. 8 saat ile 9 saat arasında 8,5 saat de olabilir: sürekli veri. (s. 162–163)"},
            {"soru": "Geri kazanım yüzdeleri (27,20 … 36,08) hangi veri türüdür?", "cevap": "Sayıyla yazılır ve iki değer arasında başka değer olabilir: sürekli veri. (s. 163)"},
            {"soru": "Sürekli veriye neden “sürekli” deniyor?", "cevap": "Bir çizgi gibi kesintisizdir: iki değer arasında sınırsız değer vardır. Kesikli veri ise basamak basamak ilerler. (s. 163)"},
            {"soru": "Kategorik verileri hiç sayamaz mıyız?", "cevap": "Cevaplar sözcüktür ama her gruba kaç kişinin düştüğünü sayabiliriz. Bu sayılarla grafik çizeriz."},
            {"soru": "Araştırma bitince bir daha başa dönülmez mi?", "cevap": "Döner! Sonuç soruya cevap vermiyorsa adımlara geri dönüp yeniden planlama yapılabilir. (s. 164)"}],
        "dusunVeYaz": [{"soru": "Okuldaki kitap sayısı ile bir ayda yağan yağmur miktarı aynı veri türü müdür? Neden?",
                        "ornekCevap": "Hayır. Kitap sayısı sayarak bulunur, arada değer olmaz: kesikli. Yağmur miktarı ölçülür, arada sınırsız değer olabilir: sürekli.",
                        "anahtarlar": ["kesikli", "sürekli", "say", "ölç", "arada"]}],
        "sorular": [
            S("“Okula nasıl geliyorsun?” sorusunun cevapları (otobüs, yürüyerek, araba) hangi veri türüdür?", ["Kategorik veri", "Kesikli veri", "Sürekli veri"], 0,
              "Cevaplar sayı mı, sözcük mü?", "Cevaplar sözcüktür: kategorik veri.", kavram="Kategorik Veri"),
            S("Bir sınıftaki öğrencilerin kardeş sayıları hangi veri türüdür?", ["Sürekli veri", "Kategorik veri", "Kesikli veri"], 2,
              "Kardeşleri sayar mıyız, ölçer miyiz?", "Kardeşler sayılır; 2,5 kardeş olmaz: kesikli veri. (s. 163)", kavram="Kesikli Veri"),
            S("Vücut sıcaklığı hangi veri türüdür?", ["Kesikli veri", "Sürekli veri", "Kategorik veri"], 1,
              "36,5 °C ile 36,6 °C arasında başka değer olabilir mi?", "Vücut sıcaklığı ölçülür; arada sınırsız değer olabilir: sürekli veri. (s. 163)", kavram="Sürekli Veri"),
            G("Şu verilerden kaç tanesi kesikli veridir? Gol sayısı · boy uzunluğu · kitap sayısı · yağış miktarı · öğrenci sayısı", "3",
              "Her biri için sor: sayarak mı, ölçerek mi?", "Gol, kitap ve öğrenci sayısı kesiklidir: 3 tane. (s. 163)", kavram="Kesikli Veri",
              yardim={"adimlar": ["Her veri için sor: sayarak mı buluyoruz, ölçerek mi?", "Sayarak bulunanları işaretle.", "İşaretlediklerini say."]}),
            S("Nicel veri için hangisi doğrudur?", ["Sayısal olarak ifade edilir.", "Sözcükle ifade edilir.", "Sadece tam sayı olur."], 0,
              "Bilgi kartındaki tanıma bak.", "Nicel veriler sayısal olarak ifade edilir; 1,5 gibi ondalık da olabilir. (s. 163)", kavram="Nicel Veri"),
            S("Bir bitkinin boyu 5,5 cm'den 8,7 cm'ye uzadı. Bu iki ölçüm arasında kaç farklı boy olabilir?", ["Hiç yok", "Sadece 3", "Sınırsız"], 2,
              "Boy sürekli veridir.", "Sürekli veri iki ölçüm arasında sınırsız değer alabilir. (s. 163)", kavram="Sürekli Veri"),
            S("Melis verilerini grafikle gösterdi ve veri setini temsil edecek değeri buldu. Melis hangi adımdadır?", ["Veri toplama", "Veri analizi", "Araştırma sorusunu belirleme"], 1,
              "Grafik ve temsil değeri hangi adımda yapılır?", "Grafik çizmek ve temsil değeri bulmak 3. adım olan veri analizidir. (s. 164)", kavram="Araştırmanın 4 Adımı"),
            G("Araştırma sürecinde “Yorumlama ve karar verme” kaçıncı adımdır?", "4",
              "Adımları sırayla say: Sor, topla, analiz et, …", "Sor (1), topla (2), analiz et (3), yorumla (4). (s. 164)", kavram="Araştırmanın 4 Adımı",
              yardim={"adimlar": ["İlk adım araştırma sorusu.", "Sonra verileri toplama, sonra analiz.", "Analizden sonra gelen adımın sırasını say."]}),
            S("Türkiye'nin 2021–2024 geri kazanım yüzdeleri (27,20 … 36,08) bir tabloya yazıldı. Bu sayıların hepsine birden ne denir?", ["Anket", "Veri seti", "Grafik"], 1,
              "Toplanan verilerin hepsine birden ne deniyordu?", "Toplanan verilerin hepsine birden veri seti denir. (s. 163)", kavram="Veri"),
            S("Hangisinin cevabı kategorik veri olur?", ["Kaç saat uyudun?", "Boyun kaç cm?", "Hangi sporu seversin?"], 2,
              "Cevabı sözcük olan soruyu bul.", "Spor adı sözcüktür (futbol, voleybol): kategorik veri.", kavram="Kategorik Veri")]
    }


# =================================================================
def u3k2():
    return {
        "id": "u3k2", "unite": T3, "baslik": "Araştırma Sorusu, Evren ve Örneklem", "sayfalar": "s. 165–168",
        "giris": "Bir şeyi merak edince önce iyi bir soru sorarız. Bu konuda araştırma sorusu yazmayı öğreneceğiz. Sonra verileri kimden toplayacağımıza karar vereceğiz: evren ve örneklem.",
        "hazirlik": {
            "baslik": "Hazır mısın?",
            "giris": "Bu konu önceki konunun devamı. Veri türlerini ve araştırmanın adımlarını hatırlıyor musun bakalım. Not yok.",
            "maddeler": [
                {"ad": "Veri türleri", "sinif": "3. tema, 1. konu", "svg": svg3_kesikli(),
                 "anlatim": "Cevap sözcükse kategorik, sayıysa nicel veridir. Nicel veride arada başka değer olamıyorsa kesikli, olabiliyorsa süreklidir.",
                 "akilda": "Sözcük mü, sayı mı? Arada değer var mı?",
                 "ornek": {"problem": "Boy uzunluğu hangi veri türüdür?", "adimlar": [
                     {"metin": "Cevap sayı mı? Evet: 1,52 m.", "islem": "Nicel"},
                     {"metin": "1,52 m ile 1,53 m arasında değer olabilir mi? Evet.", "islem": "Sürekli"}]},
                 "sorular": [
                     S("“Günde kaç litre su içersin?” sorusunun cevabı hangi veri türüdür?", ["Kategorik", "Kesikli", "Sürekli"], 2,
                       "1,5 L ile 2 L arasında değer olabilir mi?", "Su miktarı ölçülür; arada değer olabilir: sürekli."),
                     S("“Kaç kardeşin var?” sorusunun cevabı hangi veri türüdür?", ["Sürekli", "Kesikli", "Kategorik"], 1,
                       "Kardeşleri sayarız.", "Kardeş sayısı sayılır; arada değer olmaz: kesikli.")]},
                {"ad": "Araştırmanın 4 adımı", "sinif": "3. tema, 1. konu", "svg": svg3_adimlar(),
                 "anlatim": "Araştırma 4 adımda yapılır: 1) Soruyu belirle, 2) Verileri topla, 3) Analiz et, 4) Yorumla ve karar ver.",
                 "akilda": "Sor, topla, analiz et, yorumla",
                 "sorular": [
                     S("Verileri toplamadan önce hangi adım yapılır?", ["Araştırma sorusunu belirlemek", "Grafik çizmek", "Yorumlamak"], 0,
                       "Birinci adım hangisiydi?", "Önce araştırma sorusu belirlenir."),
                     S("Grafik çizmek hangi adımın içindedir?", ["Veri toplama", "Veri analizi", "Araştırma sorusu"], 1,
                       "Grafik, verileri incelemek içindir.", "Grafik çizmek veri analizi adımındadır.")]}
            ]},
        "kavramlar": [
            {"ad": "Araştırma Sorusu", "renk": "#c2255c", "svg": svg3_soru(),
             "aciklama": "Araştırma sorusu, bir grubun verileriyle cevaplanacak sorudur. Çoğu zaman “… eğilimi nasıldır?” diye yazılır. (s. 165)",
             "ek": "Örnek: “7/A sınıfı öğrencilerinin günlük su tüketimlerinin eğilimi nasıldır?” Cevap tek kişiden değil, bütün sınıfın verilerinden çıkar. (s. 165)",
             "akilda": "Grubun verisiyle cevaplanır",
             "soru": S("Hangisi bir araştırma sorusudur?", ["7/A sınıfı öğrencilerinin günlük su tüketimlerinin eğilimi nasıldır?", "Bir günde kaç litre su içersin?", "Su içmeyi sever misin?"], 0,
                       "Bir grubun verileriyle cevaplanan soruyu bul.", "Bu soru bütün sınıfın verileriyle cevaplanır. (s. 165)")},
            {"ad": "İyi Araştırma Sorusu", "renk": "#e8590c", "svg": svg3_iyi_soru(),
             "aciklama": "İyi bir araştırma sorusunun amacı nettir, neyi ölçeceğimiz bellidir, veri toplamaya uygundur ve cevapları kişiden kişiye değişir. (s. 165)",
             "ek": "“Su içmeyi sever misin?” araştırma sorusu olarak uygun değildir: Cevabı evet ya da hayır, ne ölçeceğimiz belli değil.",
             "akilda": "Net, ölçülebilir, toplanabilir",
             "cozum": {"baslik": "Soru uygun mu?",
                       "problem": "Defne su tüketimini araştırıyor. Sorusu: “Günde 2,5 litreden az mı su içersiniz?” Bu, araştırma sorusu olarak uygun mu?",
                       "adimlar": [
                           {"metin": "Cevap ne olur? Sadece evet ya da hayır.", "islem": "Evet / hayır"},
                           {"metin": "Neyi ölçüyoruz? Kaç litre içildiğini öğrenemiyoruz.", "islem": "Miktar kayboluyor ✗"},
                           {"metin": "Grubun verisiyle cevaplanan daha iyi bir soru yaz.", "islem": "7/A öğrencilerinin günlük su tüketimlerinin eğilimi nasıldır?"}],
                       "sonuc": "“2,5 litreden az mı?” uygun değildir; grubun su tüketiminin eğilimini sormak daha iyidir. (s. 165)"},
             "sende": {"baslik": "Sıra sende",
                       "problem": "Okulundaki öğrencilerin ekran kullanım sürelerini araştıracaksın.",
                       "adimlar": [
                           {"metin": "İyi bir araştırma sorusu seç.",
                            "soru": S("Hangisi daha iyi bir araştırma sorusudur?", ["Telefonu sever misin?", "Okulumuzdaki öğrencilerin günlük ekran kullanım sürelerinin eğilimi nasıldır?", "Dün telefona baktın mı?"], 1,
                                      "Grubun verisiyle cevaplanan, ölçülecek şeyi belli olan soruyu bul.", "Bu soru bütün okulun ekran sürelerini soruyor; ölçülecek şey belli."),
                            "islem": "Grubun ekran süreleri soruluyor ✓"},
                           {"metin": "Bu soruda neyi ölçeceğiz?",
                            "soru": S("Bu araştırmada neyi ölçeceğiz?", ["En sevilen oyunu", "Günlük ekran süresini", "Telefon markasını"], 1,
                                      "Soruda hangi süre geçiyor?", "Ölçeceğimiz şey günlük ekran kullanım süresidir."),
                            "islem": "Ölçülecek: günlük ekran süresi"}],
                       "sonuc": "Harika! Amacı net, ölçülecek şeyi belli bir soru yazdın. (s. 166)"},
             "soru": S("“Su içmeyi sever misin?” neden iyi bir araştırma sorusu değildir?", ["Çok uzun olduğu için", "Sayı içerdiği için", "Ne ölçeceğimiz belli olmadığı için"], 2,
                       "İyi sorunun özelliklerine bak: ölçülecek şey belli mi?", "Cevabı evet/hayır; neyi ölçeceğimiz belli değil. (s. 165)")},
            {"ad": "Değişebilirlik", "renk": "#2f8f73", "svg": svg3_degisebilir(),
             "aciklama": "Aynı soruyu farklı kişilere sorunca farklı cevaplar alırız. Araştırma sorusunun cevapları kişiden kişiye değişebilmelidir. (s. 165)",
             "ek": "Kalp ritmi kişinin yaşına ve kütlesine göre değişir (s. 165). Hasta Alya'nın ateşi 40,1 °C, sağlıklı Elif'inki 36,3 °C. Aras'ın ateşi iki termometrede farklı çıktı: ölçüm aracı da fark yaratabilir. (s. 168)",
             "akilda": "Cevaplar kişiden kişiye değişir",
             "soru": S("Aras'ın ateşi aynı anda A termometresinde 38,7 °C, B termometresinde 39,0 °C çıktı. Farkın sebebi nedir?", ["Aras'ın hastalanması", "Ölçüm aracının farklı olması", "Aras'ın yaşı"], 1,
                       "Değişen şey Aras mı, termometre mi?", "Aynı anda ölçülmüş; değişen tek şey termometre. Ölçüm aracı fark yaratır. (s. 168)")},
            {"ad": "Evren", "renk": "#b7791f", "svg": svg3_evren(),
             "aciklama": "Evren, araştırma sorusuna yönelik verilerin toplanabileceği en geniş gruptur. (s. 165)",
             "ek": "“Denizli'deki ortaokul öğrencilerinin kantin sırasında bekledikleri süre …” sorusunun evreni Denizli'de kantini olan bütün ortaokullardır. (s. 166)",
             "akilda": "En geniş grup",
             "soru": S("“Türkiye'deki 7. sınıf öğrencilerinin uyku süreleri” araştırmasının evreni hangisidir?", ["Türkiye'deki bütün 7. sınıf öğrencileri", "Ela'nın sınıfı", "Ela'nın okulu"], 0,
                       "Soru kimleri kapsıyor? En geniş grup hangisi?", "Soru Türkiye'deki bütün 7. sınıfları kapsıyor: evren budur. (s. 165)")},
            {"ad": "Örneklem", "renk": "#1f9e8f", "svg": svg3_orneklem(),
             "aciklama": "Evrenin hepsine ulaşmak çoğu zaman zor ve pahalıdır. Evreni temsil eden daha küçük bir grup seçilir; buna örneklem denir. (s. 165)",
             "ek": "Çorbanın tadına bakarken bütün tencereyi içmeyiz, bir kaşık yeter. Ama önce çorbayı karıştırırız ki kaşıktaki bütün tencereye benzesin.",
             "akilda": "Evrenden seçilen küçük grup",
             "cozum": {"baslik": "Kantin sırası",
                       "problem": "İpek'in sorusu: “Denizli'deki ortaokul öğrencilerinin teneffüste kantin sırasında bekledikleri süre nasıl bir eğilim gösterir?” Evren ve örneklem ne olabilir?",
                       "adimlar": [
                           {"metin": "Soru kimleri kapsıyor? Denizli'deki ortaokul öğrencilerini.", "islem": "Evren: Denizli'de kantini olan bütün ortaokullar"},
                           {"metin": "Hepsine ulaşmak zor. Ulaşabileceğimiz, evrene benzeyen bir grup seç.", "islem": "Örneklem: Cumhuriyet Ortaokulunun bütün öğrencileri"},
                           {"metin": "Kontrol et: Bu grup evrenin içinde mi? Evet.", "islem": "Örneklem evrenin içinde ✓"}],
                       "sonuc": "Evren Denizli'de kantini olan ortaokullar, örneklem Cumhuriyet Ortaokulunun bütün öğrencileri. (s. 166)"},
             "sende": {"baslik": "Sıra sende",
                       "problem": "Betül, Muğla'daki marketlerde glütensiz makarnanın 100 gram fiyatını araştırıyor.",
                       "adimlar": [
                           {"metin": "Önce evreni bul.",
                            "soru": S("Bu araştırmanın evreni hangisidir?", ["Betül'ün evi", "Muğla'daki bütün marketler", "Türkiye'deki bütün fırınlar"], 1,
                                      "Araştırma hangi şehirdeki marketleri kapsıyor?", "Araştırma Muğla'daki marketleri kapsıyor."),
                            "islem": "Evren: Muğla'daki bütün marketler"},
                           {"metin": "Şimdi evreni temsil edecek bir örneklem seç.",
                            "soru": S("Hangisi uygun bir örneklemdir?", ["İstanbul'daki 5 market", "Sadece Betül'ün evine en yakın market", "Muğla'nın farklı ilçelerinden büyük ve küçük 15 market"], 2,
                                      "Örneklem evrenin içinde olmalı ve ona benzemeli.", "Farklı ilçelerden, büyük ve küçük marketler Muğla'yı temsil eder."),
                            "islem": "Örneklem: farklı türden Muğla marketleri"}],
                       "sonuc": "Harika! Marketlerin büyüklüğü ve türü farklı olunca örneklem evreni daha iyi temsil eder. (s. 168)"},
             "soru": S("Evrenin hepsine ulaşmak zor olduğunda ne yapılır?", ["Araştırmadan vazgeçilir.", "Veriler tahmin edilir.", "Evreni temsil eden bir örneklem seçilir."], 2,
                       "Bilgi kartında küçük grubu anlatan cümleye bak.", "Evreni temsil eden daha küçük bir grup, yani örneklem seçilir. (s. 165)")},
            {"ad": "Örneklem Evreni Temsil Etmeli", "renk": "#7b4fc9", "svg": svg3_temsil(),
             "aciklama": "Örneklem evrenin özelliklerini taşımalıdır. Sadece kantine en yakın sınıftan veri toplamak sonucu yanlış yorumlatabilir. (s. 166)",
             "ek": "Kantine en yakın sınıf sıraya erken girer; onların bekleme süresi bütün okulu göstermez. Bazen örneklem gerekmez: TÜİK bazı araştırmalarda evrenin tamamına güvenilir kaynaklardan ulaşır. (s. 167)",
             "akilda": "Örneklem evrene benzemeli",
             "soru": S("Okuldaki öğrencilerin ekran süreleri araştırılıyor. Hangi örneklem en uygundur?", ["Sadece bilgisayar kulübü üyeleri", "Her sınıftan rastgele seçilen öğrenciler", "Sadece öğretmenler"], 1,
                       "Bütün okula benzeyen grubu bul.", "Her sınıftan seçilen öğrenciler bütün okulu temsil eder. (s. 166)")}
        ],
        "gruplar": [{"soru": "Hangisi neyle ilgili?", "kutular": [
            {"etiket": "Ne soruyoruz?", "uyeler": ["Araştırma Sorusu", "İyi Araştırma Sorusu", "Değişebilirlik"]},
            {"etiket": "Kimden veri topluyoruz?", "uyeler": ["Evren", "Örneklem", "Örneklem Evreni Temsil Etmeli"]}]}],
        "akildaKalsin": [
            "Araştırma sorusu bir grubun verileriyle cevaplanır: “… eğilimi nasıldır?”",
            "İyi araştırma sorusu: amacı net, ölçülecek şey belli, veri toplamaya uygun.",
            "Cevaplar kişiden kişiye değişir: değişebilirlik.",
            "Evren, verilerin toplanabileceği en geniş gruptur.",
            "Örneklem, evreni temsil eden daha küçük gruptur.",
            "Örneklem evrene benzemeli; yoksa sonuç yanlış yorumlanır."],
        "merakKutusu": [
            {"soru": "TÜİK nasıl oluyor da bütün Türkiye'yi biliyor?", "cevap": "Bazı araştırmalarda evrenin tamamına güvenilir kurumların hazır verileriyle ulaşılır; o zaman örneklem gerekmez. (s. 167)"},
            {"soru": "Kalp ritmi neden herkeste farklı?", "cevap": "Yaş, kütle gibi özelliklere ve verinin toplandığı gruba göre değişir. Buna değişebilirlik denir. (s. 165)"},
            {"soru": "Neden “eğilim” kelimesini kullanıyoruz?", "cevap": "Tek bir kişiyi değil, grubun genel durumunu merak ediyoruz: Çoğu ne kadar su içiyor, hangi değerler sık? (s. 165)"},
            {"soru": "Market örnekleminde neden büyük ve küçük marketler olmalı?", "cevap": "Fiyatlar marketin büyüklüğüne ve türüne göre değişebilir. Sadece büyük marketler seçilirse sonuç Muğla'nın tamamını göstermez. (s. 168)"},
            {"soru": "Kız ve erkek öğrencileri karşılaştıran soru da araştırma sorusu olur mu?", "cevap": "Olur: “7/A'daki kız ve erkek öğrencilerin günlük su tüketimlerinin eğilimi nasıl değişmektedir?” iki grubu karşılaştırır. (s. 165)"}],
        "dusunVeYaz": [{"soru": "Okulundaki öğrencilerin kaç saat uyuduğunu araştıracaksın. Bir araştırma sorusu yaz; evreni ve örneklemi söyle.",
                        "ornekCevap": "Araştırma sorusu: Okulumuzdaki öğrencilerin günlük uyku sürelerinin eğilimi nasıldır? Evren: okuldaki bütün öğrenciler. Örneklem: her sınıftan seçilen 5 öğrenci.",
                        "anahtarlar": ["eğilim", "evren", "örneklem", "öğrenci"]}],
        "sorular": [
            S("Hangisi araştırma sorusu olarak uygundur?", ["Spor yapmayı sever misin?", "7/B sınıfı öğrencilerinin haftalık spor sürelerinin eğilimi nasıldır?", "Dün spor yaptın mı?"], 1,
              "Bir grubun verileriyle cevaplanan soruyu bul.", "Bu soru bütün sınıfın spor sürelerini soruyor. (s. 165)", kavram="Araştırma Sorusu"),
            S("“İzmir'deki ortaokulların kütüphanelerindeki kitap sayıları nasıl bir eğilim gösterir?” sorusunun evreni hangisidir?",
              ["Bir okulun kütüphanesi", "Türkiye'deki bütün kütüphaneler", "İzmir'deki bütün ortaokulların kütüphaneleri"], 2,
              "Soru hangi şehri ve hangi okulları kapsıyor?", "Soru İzmir'deki bütün ortaokul kütüphanelerini kapsıyor. (s. 165)", kavram="Evren"),
            S("Bir araştırmada evren “okuldaki bütün öğrenciler”dir. Hangisi bu evreni temsil etmez?", ["Her sınıftan seçilen 5 öğrenci", "Sadece basketbol takımındaki öğrenciler", "Her sınıftan rastgele seçilen öğrenciler"], 1,
              "Bütün okula benzemeyen grubu bul.", "Sadece takım üyeleri bütün okula benzemez; sonucu yanlış yorumlatır. (s. 166)", kavram="Örneklem Evreni Temsil Etmeli"),
            G("Bir okulda 15 sınıf var. Her sınıftan 4 öğrenci seçildi. Örneklemde kaç öğrenci var?", "60",
              "Sınıf sayısını, her sınıftan seçilen kişi sayısıyla çarp.", "15 · 4 = 60 öğrenci.", kavram="Örneklem", birim="öğrenci",
              yardim={"adimlar": ["Kaç sınıf var?", "Her sınıftan kaç kişi seçildi?", "Sınıf sayısını her sınıftan seçilen kişi sayısıyla çarp."]}),
            S("Bir sınıftaki öğrencilerin boy uzunlukları birbirinden farklıdır. Bu duruma ne denir?", ["Değişebilirlik", "Örneklem", "Evren"], 0,
              "Cevapların kişiden kişiye değişmesi …", "Verilerin kişiden kişiye değişmesine değişebilirlik denir. (s. 165)", kavram="Değişebilirlik"),
            S("Hangisi iyi bir araştırma sorusunun özelliği değildir?", ["Amacı nettir.", "Veri toplamaya uygundur.", "Cevabı herkes için aynıdır."], 2,
              "İyi soruda cevaplar kişiden kişiye değişir mi?", "İyi araştırma sorusunun cevapları kişiden kişiye değişir. (s. 165)", kavram="İyi Araştırma Sorusu"),
            S("Evren ile örneklem için hangisi doğrudur?", ["Örneklem evrenden büyüktür.", "Örneklem evrenin içinden seçilen küçük gruptur.", "Evren ile örneklem her zaman aynıdır."], 1,
              "Çorba ve kaşığı düşün.", "Örneklem, evreni temsil eden daha küçük bir gruptur. (s. 165)", kavram="Örneklem"),
            G("Bir araştırmanın evreni 120 öğrenci, örneklemi bunlardan 30 öğrenci. Evrende olup örneklemde olmayan kaç öğrenci var?", "90",
              "Evrendeki öğrenci sayısından örneklemdekileri çıkar.", "120 − 30 = 90 öğrenci.", kavram="Evren", birim="öğrenci",
              yardim={"adimlar": ["Evrende kaç öğrenci var?", "Örneklemde kaç öğrenci var?", "Evrendekilerden örneklemdekileri çıkar."]}),
            S("Aynı anda iki farklı termometreyle ölçülen ateşin farklı çıkmasının sebebi nedir?", ["Kişinin değişmesi", "Ölçüm aracının farklı olması", "Evrenin büyük olması"], 1,
              "Aynı anda ölçüldüyse değişen ne?", "Kişi aynı, zaman aynı; değişen termometre. (s. 168)", kavram="Değişebilirlik"),
            S("TÜİK bazı araştırmalarda neden örneklem kullanmaz?", ["Örneklem seçmek yasak olduğu için", "Araştırma sorusu olmadığı için", "Evrenin tamamına güvenilir hazır verilerle ulaşabildiği için"], 2,
              "Evrenin tamamına ulaşabiliyorsa örneklem gerekir mi?", "TÜİK evrenin tamamına güvenilir kaynaklardan ulaşabilir. (s. 167)", kavram="Örneklem Evreni Temsil Etmeli")]
    }


# =================================================================
def u3k3():
    return {
        "id": "u3k3", "unite": T3, "baslik": "Veri Toplama ve Kişisel Veriler", "sayfalar": "s. 169–170, 192–193",
        "giris": "Araştırma sorusu ve örneklem hazır. Şimdi verileri toplama zamanı! Bu konuda anket sorusu yazmayı, plan yapmayı ve güvenilir kaynak seçmeyi öğreneceğiz. Kişisel verileri nasıl koruyacağımızı da konuşacağız.",
        "hazirlik": {
            "baslik": "Hazır mısın?",
            "giris": "Bu konu önceki konunun devamı. Araştırma sorusunu, evreni ve örneklemi hatırlıyor musun bakalım. Not yok.",
            "maddeler": [
                {"ad": "Araştırma sorusu", "sinif": "3. tema, 2. konu", "svg": svg3_soru(),
                 "anlatim": "Araştırma sorusu bir grubun verileriyle cevaplanır. Çoğu zaman “… eğilimi nasıldır?” diye yazılır.",
                 "akilda": "Grubun verisiyle cevaplanır",
                 "sorular": [
                     S("Hangisi bir araştırma sorusudur?", ["Kitap okumayı sever misin?", "7/A öğrencilerinin haftalık kitap okuma sürelerinin eğilimi nasıldır?", "Dün kitap okudun mu?"], 1,
                       "Grubun verisiyle cevaplanan soruyu bul.", "Bu soru bütün sınıfın verileriyle cevaplanır."),
                     S("Araştırma sorusu kimin verileriyle cevaplanır?", ["Bir grubun", "Sadece bir kişinin", "Hiç kimsenin"], 0,
                       "“Eğilim” bir kişiyi mi, grubu mu anlatır?", "Araştırma sorusu bir grubun verileriyle cevaplanır.")]},
                {"ad": "Evren ve örneklem", "sinif": "3. tema, 2. konu", "svg": svg3_orneklem(),
                 "anlatim": "Evren, verilerin toplanabileceği en geniş gruptur. Örneklem, evreni temsil eden daha küçük gruptur.",
                 "akilda": "Evren büyük, örneklem küçük",
                 "sorular": [
                     S("Evreni temsil eden küçük gruba ne denir?", ["Veri seti", "Örneklem", "Anket"], 1,
                       "Çorbadan alınan bir kaşığı düşün.", "Evreni temsil eden küçük gruba örneklem denir."),
                     S("Hangisi doğrudur?", ["Örneklem evrenden büyüktür.", "Evren en geniş gruptur.", "Evren ile örneklem hep aynıdır."], 1,
                       "En geniş grup hangisiydi?", "Evren en geniş gruptur; örneklem onun içinden seçilir.")]}
            ]},
        "kavramlar": [
            {"ad": "Anket Sorusu", "renk": "#1f9e8f", "svg": svg3_anket(),
             "aciklama": "Anket sorusu, örneklemdeki her kişiye tek tek sorulan sorudur. Cevapları birleşince araştırma sorusunun verisi olur. (s. 169)",
             "ek": "Araştırma sorusu: “Sınıfımızdaki öğrencilerin boy uzunluklarının eğilimi nasıldır?” Anket sorusu: “Boyun kaç santimetre?” (s. 169)",
             "akilda": "Kişiye sorulur, cevaplar birleşir",
             "cozum": {"baslik": "Araştırma sorusundan anket sorusuna",
                       "problem": "Araştırma sorusu: “Sınıfımızdaki öğrencilerin günlük uyku sürelerinin eğilimi nasıldır?” Her arkadaşına ne soracaksın?",
                       "adimlar": [
                           {"metin": "Araştırma sorusunda neyi ölçüyoruz?", "islem": "Ölçülecek: günlük uyku süresi"},
                           {"metin": "Bunu tek bir kişiye nasıl sorarsın?", "islem": "Anket sorusu: Günde kaç saat uyuyorsun?"},
                           {"metin": "Cevaplar birleşince sınıfın veri seti olur.", "islem": "8, 9, 7,5, 10 …"}],
                       "sonuc": "Anket sorusu her kişiye sorulur; cevaplar birleşince araştırma sorusunu cevaplarız. (s. 169)"},
             "sende": {"baslik": "Sıra sende",
                       "problem": "Araştırma sorusu: “7/A sınıfı öğrencilerinin günlük su tüketimlerinin eğilimi nasıldır?”",
                       "adimlar": [
                           {"metin": "Her arkadaşına soracağın anket sorusunu seç.",
                            "soru": S("Hangisi bu araştırma için uygun bir anket sorusudur?", ["Su içmeyi sever misin?", "Hangi renk bardağı seversin?", "Bir günde kaç litre su içersin?"], 2,
                                      "Ölçülecek şey su miktarı.", "Bu soru her kişinin içtiği su miktarını öğrenir."),
                            "islem": "Anket sorusu: Bir günde kaç litre su içersin?"}],
                       "sonuc": "Harika! Cevaplar birleşince 7/A'nın su tüketimi veri seti olur."},
             "soru": S("Anket sorusu kime sorulur?", ["Örneklemdeki her kişiye", "Sadece öğretmene", "Hiç kimseye; tahmin edilir"], 0,
                       "Bilgi kartındaki ilk cümleye bak.", "Anket sorusu örneklemdeki her kişiye tek tek sorulur. (s. 169)")},
            {"ad": "Veri Toplama Planı", "renk": "#b7791f", "svg": svg3_plan(),
             "aciklama": "Veri toplamadan önce plan yapılır: Veriler nerede, ne zaman, nasıl toplanacak ve nasıl kaydedilecek? (s. 169)",
             "ek": "Toplanacak veriler araştırma sorusunun amacına uygun olmalıdır (s. 169). Örnek: Sıralar için öğrencilerin boyu sınıfta, salı günü, mezurayla ölçülür ve tabloya yazılır.",
             "akilda": "Nerede? Ne zaman? Nasıl? Kaydet!",
             "soru": S("Sıralar için öğrencilerin boyu ölçülecek. Planda “Nasıl?” sorusunun cevabı hangisi olabilir?", ["Pazartesi günü", "Sınıfta", "Mezurayla ölçerek"], 2,
                       "“Nasıl” bir yöntemi sorar.", "Mezurayla ölçmek bir yöntemdir; pazartesi “ne zaman”, sınıf “nerede” sorusunun cevabıdır. (s. 169)")},
            {"ad": "Güvenilir Kaynak", "renk": "#2f8f73", "svg": svg3_kaynak(),
             "aciklama": "Hazır verileri güvenilir kaynaklardan alırız: edu.tr, gov.tr, org.tr gibi uzantılı resmî adreslerden. (s. 169)",
             "ek": "Mustafa Bey orman yangını verilerini güvenilir sitelerden arar (s. 169). Sosyal medyada kaynağı yazmayan bir habere hemen inanmayız; güvenilir bir kaynaktan kontrol ederiz. (s. 192)",
             "akilda": "Resmî site, kaynağı belli",
             "soru": S("Orman yangını verileri için hangisi daha güvenilir bir kaynaktır?", ["Kaynağı belirtilmemiş bir sosyal medya paylaşımı", "Uzantısı gov.tr olan resmî bir kurum sitesi", "Bir arkadaşın tahmini"], 1,
                       "Bilgi kartındaki uzantılara bak.", "gov.tr uzantılı resmî siteler güvenilir kaynaklardır. (s. 169)")},
            {"ad": "Kişisel Veri", "renk": "#c2255c", "svg": svg3_kisisel(),
             "aciklama": "Kişilerin sağlık, kimlik, banka, adres ve günlük yaşam bilgileri kişisel veridir. (s. 170)",
             "ek": "“Ev adresiniz nedir?”, “Boyunuz kaç metredir?”, “Günlük ekran süreniz ne kadar?” sorularının cevapları kişisel veri içerir. (s. 170)",
             "akilda": "Kişiye ait bilgi = kişisel veri",
             "cozum": {"baslik": "Duru'nun profili",
                       "problem": "Duru sosyal medyada doğum tarihini, okulunun adını ve yaşadığı şehri herkese açık paylaştı. Bunlar kişisel veri mi?",
                       "adimlar": [
                           {"metin": "Doğum tarihi kime ait? Duru'ya; kimlik bilgisidir.", "islem": "Kişisel veri"},
                           {"metin": "Okul adı ve şehir Duru'nun nerede olduğunu gösterir: adres ve günlük yaşam bilgisi.", "islem": "Kişisel veri"},
                           {"metin": "Hesap herkese açık: Bu bilgileri tanımadığı kişiler de görür.", "islem": "Gizlilik tehlikede"}],
                       "sonuc": "Üçü de kişisel veridir. Hesabı gizli yapmak ve bu bilgileri paylaşmamak daha güvenlidir. (s. 192)"},
             "sende": {"baslik": "Sıra sende",
                       "problem": "Bir sınıf anketinde şu soru var: “Banka hesabında ne kadar para var?”",
                       "adimlar": [
                           {"metin": "Soru hangi bilgiyi istiyor?",
                            "soru": S("Bu soru hangi bilgiyi istiyor?", ["Hava durumu bilgisi", "Banka bilgisi", "Okulun adı"], 1,
                                      "Soruda “banka hesabı” geçiyor.", "Soru kişinin banka bilgisini istiyor."),
                            "islem": "Banka bilgisi → kişisel veri"},
                           {"metin": "Bu soru ankete konmalı mı?",
                            "soru": S("Bu soru sınıf anketine konmalı mı?", ["Hayır; kişisel veri istiyor ve araştırma için gerekmiyor.", "Evet; her ankette olmalı.", "Sadece cevabı kısaysa"], 0,
                                      "Banka bilgisi kişisel veridir.", "Gerekmeyen kişisel bilgiler ankette sorulmaz."),
                            "islem": "Gereksiz kişisel soru sorma"}],
                       "sonuc": "Harika! Kişisel veri isteyen gereksiz soruları anketten çıkardın. (s. 170)"},
             "soru": S("Hangisi kişisel veridir?", ["Türkiye'nin başkenti", "Bir haftada kaç gün olduğu", "Bir öğrencinin ev adresi"], 2,
                       "Kişiye ait bilgiyi bul.", "Ev adresi kişiye aittir: kişisel veri. (s. 170)")},
            {"ad": "İzin ve Gizlilik", "renk": "#e8590c", "svg": svg3_izin(),
             "aciklama": "Ankette toplanan veriler izin alınmadan başkalarıyla paylaşılmaz. Gerekmeyen kişisel sorular sorulmaz. (s. 170)",
             "ek": "Buse anketteki arkadaşlarının kilo ve boy bilgilerini izinsiz paylaştı; bu, kişisel verilerin gizliliğini ihlal eder (s. 170). Ege bir oyunu indirmek için izin metnini okumadan onayladı; önce okumalıydı. (s. 193)",
             "akilda": "İzin al, gizli tut",
             "soru": S("Buse anket verilerini (kilo, boy) izin almadan internette paylaştı. Bu davranış neye yol açar?", ["Kişisel verilerin gizliliğinin ihlaline", "Araştırmanın daha iyi olmasına", "Örneklemin büyümesine"], 0,
                       "İzinsiz paylaşılan bilgi kime aittir?", "İzinsiz paylaşmak kişisel verilerin gizliliğini ihlal eder. (s. 170)")},
            {"ad": "KVKK", "renk": "#7b4fc9", "svg": svg3_kvkk(),
             "aciklama": "Kişisel Verilerin Korunması Kanunu (KVKK), Türkiye'de kişisel verilerin işlenmesi ve korunmasıyla ilgili temel kanundur. (s. 193)",
             "ek": "KVKK'nin amacı kişilerin özel hayatının gizliliğini korumak, temel hak ve özgürlükleri güvence altına almaktır. (s. 193)",
             "akilda": "Kişisel verileri koruyan kanun",
             "soru": S("KVKK'nin amacı nedir?", ["Anketleri yasaklamak", "Kişilerin özel hayatının gizliliğini korumak", "Herkesin bilgisini paylaşmak"], 1,
                       "Kanunun adında “korunması” geçiyor.", "KVKK özel hayatın gizliliğini korur. (s. 193)")}
        ],
        "gruplar": [{"soru": "Hangisi neyle ilgili?", "kutular": [
            {"etiket": "Veriyi toplamak", "uyeler": ["Anket Sorusu", "Veri Toplama Planı", "Güvenilir Kaynak"]},
            {"etiket": "Veriyi korumak", "uyeler": ["Kişisel Veri", "İzin ve Gizlilik", "KVKK"]}]}],
        "akildaKalsin": [
            "Anket sorusu örneklemdeki her kişiye sorulur; cevaplar birleşince veri seti olur.",
            "Plan: Nerede? Ne zaman? Nasıl? Nasıl kaydedeceğim?",
            "Hazır veriler güvenilir kaynaklardan alınır (gov.tr, edu.tr, org.tr).",
            "Sağlık, kimlik, banka, adres ve günlük yaşam bilgileri kişisel veridir.",
            "Toplanan veriler izinsiz paylaşılmaz; gereksiz kişisel soru sorulmaz.",
            "KVKK kişisel verileri koruyan kanundur."],
        "merakKutusu": [
            {"soru": "Anketlerde adımı sormak gerekli mi?", "cevap": "Araştırma için gerekmiyorsa ad soyad sormamak kişisel verileri korur. Buse'nin anketinde ad soyad bile zorunluydu. (s. 170)"},
            {"soru": "Boyum neden kişisel veri?", "cevap": "Boy, kilo gibi bilgiler kişinin sağlığı ve günlük yaşamıyla ilgilidir; kişiye aittir. (s. 170)"},
            {"soru": "“Su İçmek Zararlı!” diye bir haber gördüm. İnanmalı mıyım?", "cevap": "Kaynağı yazmayan haberleri hemen paylaşmayız; doğruluğunu güvenilir bir kaynaktan kontrol ederiz. (s. 192)"},
            {"soru": "Uygulamalar neden izin istiyor?", "cevap": "Bilgilerimize ulaşmak için. İzin metnini okumadan “Tüm izinleri kabul ediyorum.” dememeliyiz. (s. 193)"},
            {"soru": "Hazır veri ne demek?", "cevap": "Başka bir kurumun önceden topladığı veridir. Mustafa Bey orman yangını verilerini kendisi toplamaz, güvenilir sitelerden alır. (s. 169)"}],
        "dusunVeYaz": [{"soru": "Sınıfında bir anket yapacaksın. Arkadaşlarının kişisel verilerini korumak için nelere dikkat edersin? İki şey yaz.",
                        "ornekCevap": "Gerekmeyen kişisel bilgileri (ad soyad, adres) sormam. Toplanan cevapları izin almadan kimseyle paylaşmam.",
                        "anahtarlar": ["izin", "paylaş", "ad", "adres", "gizli"]}],
        "sorular": [
            S("Hangisi anket sorusudur?", ["Okulumuzdaki öğrencilerin uyku sürelerinin eğilimi nasıldır?", "Dün gece kaç saat uyudun?", "Uyku neden önemlidir?"], 1,
              "Tek bir kişiye sorulan soruyu bul.", "“Dün gece kaç saat uyudun?” her kişiye tek tek sorulur. (s. 169)", kavram="Anket Sorusu"),
            S("Veri toplama planında “Ne zaman?” sorusunun cevabı hangisi olabilir?", ["Mezurayla", "Salı günü ilk derste", "Okul bahçesinde"], 1,
              "Zaman bildiren cevabı bul.", "“Salı günü ilk derste” zamanı söyler. (s. 169)", kavram="Veri Toplama Planı"),
            S("Hazır veri ararken hangisi en güvenilir kaynaktır?", ["Uzantısı edu.tr olan bir üniversite sitesi", "Yazarı belli olmayan bir blog", "Bir sosyal medya yorumu"], 0,
              "Resmî uzantılı adresi bul.", "edu.tr uzantılı resmî siteler güvenilir kaynaklardır. (s. 169)", kavram="Güvenilir Kaynak"),
            S("Hangisinin cevabı kişisel veri içerir?", ["Bir yılda kaç ay vardır?", "Ailenizin gelir düzeyi nasıldır?", "Türkiye'nin en uzun nehri hangisidir?"], 1,
              "Kişiye ait bilgiyi soran soruyu bul.", "Ailenin gelir düzeyi kişisel veridir. (s. 170)", kavram="Kişisel Veri"),
            G("Bu sorulardan kaç tanesinin cevabı kişisel veri içerir? Ev adresin ne? · Başkentimiz neresi? · Boyun kaç metre? · Banka hesabında ne kadar para var?", "3",
              "Her soru için sor: Cevap kişiye mi ait?", "Adres, boy ve banka bilgisi kişiseldir: 3 tane. (s. 170)", kavram="Kişisel Veri",
              yardim={"adimlar": ["Her soru için sor: Cevap bir kişiye mi ait?", "Kişiye ait bilgileri işaretle.", "İşaretlediklerini say."]}),
            S("Ege bir oyunu indirmek için izin metnini okumadan onayladı. Ne yapmalıydı?", ["Bütün izinleri hemen kabul etmeliydi.", "Metni okuyup hangi bilgilerinin istendiğine bakmalıydı.", "Şifresini arkadaşlarıyla paylaşmalıydı."], 1,
              "İzin metni neden okunur?", "İzin metni okunmadan onaylanmamalı; hangi bilgilerin istendiği görülmeli. (s. 193)", kavram="İzin ve Gizlilik"),
            S("Türkiye'de kişisel verilerin korunmasıyla ilgili temel kanun hangisidir?", ["KVKK", "TÜİK", "Anket"], 0,
              "Kısaltmanın açılımını düşün: Kişisel Verilerin …", "Kişisel Verilerin Korunması Kanunu: KVKK. (s. 193)", kavram="KVKK"),
            S("Kaynağı belirtilmemiş “Su İçmek Zararlı!” başlıklı bir haber gördün. Ne yaparsın?", ["Hemen herkesle paylaşırım.", "Su içmeyi bırakırım.", "Doğruluğunu güvenilir bir kaynaktan kontrol ederim."], 2,
              "Kaynağı belli olmayan habere hemen inanılır mı?", "Kaynağı belirtilmeyen haberi güvenilir bir kaynaktan kontrol ederiz. (s. 192)", kavram="Güvenilir Kaynak"),
            G("Sınıfta 28 öğrenci var. 4 öğrenci ankete katılmak istemedi. Kaç öğrencinin verisi toplanır?", "24",
              "Ankete katılmayanların verisi toplanmaz.", "28 − 4 = 24 öğrenci.", kavram="İzin ve Gizlilik", birim="öğrenci",
              yardim={"adimlar": ["Sınıfta kaç öğrenci var?", "Kaç kişi katılmak istemedi?", "Toplamdan katılmayanları çıkar."]}),
            S("Araştırma sorusu: “Sınıfımızdaki öğrencilerin boy uzunluklarının eğilimi nasıldır?” Hangisi uygun bir anket sorusudur?", ["Ev adresin nedir?", "En sevdiğin ders hangisi?", "Boyun kaç santimetre?"], 2,
              "Ölçülecek şey nedir?", "Araştırma boyu soruyor; anket sorusu da her kişinin boyunu sormalı. (s. 169)", kavram="Anket Sorusu")]
    }


# =================================================================
def u3t1():
    return {
        "id": "u3t1", "tur": "tarama", "unite": T3,
        "baslik": "Ara Durak 1: Araştırmaya Hazırlık", "sayfalar": "Konu 1–3 · s. 159–170, 192–193",
        "giris": "Araştırmaya hazırlık bitti, tebrikler! Kısa bir mola verip veri türlerini, araştırma sorusunu ve veri toplamayı birlikte gözden geçireceğiz. Önce özetleri oku ve kartları çevir, sonra tarama testini çöz. Not yok.",
        "buyukResim": "Önce verileri tanıdık: kategorik, kesikli, sürekli. Sonra araştırmanın ilk adımını yaptık: iyi bir soru, evren ve örneklem. En son verileri topladık: anket, plan, güvenilir kaynak ve kişisel verilerin korunması.",
        "kapsar": ["u3k1", "u3k2", "u3k3"],
        "hatirla": [
            {"konu": "u3k1", "maddeler": [
                "Cevap sözcükse kategorik, sayıysa nicel veri.",
                "Kesikli: arada değer yok (sayarak). Sürekli: arada sınırsız değer (ölçerek).",
                "4 adım: Sor, topla, analiz et, yorumla."]},
            {"konu": "u3k2", "maddeler": [
                "Araştırma sorusu grubun verisiyle cevaplanır: “… eğilimi nasıldır?”",
                "Evren en geniş grup; örneklem onu temsil eden küçük grup.",
                "Örneklem evrene benzemeli."]},
            {"konu": "u3k3", "maddeler": [
                "Anket sorusu her kişiye tek tek sorulur.",
                "Hazır veri güvenilir kaynaktan (gov.tr, edu.tr).",
                "Kişisel veriler izinsiz paylaşılmaz; KVKK korur."]}],
        "eskiSoru": 4,
        "oyunKavram": 8,
        "gruplar": [{"soru": "Araştırmanın hangi işi?", "kutular": [
            {"etiket": "Verinin türü", "uyeler": ["Kategorik Veri", "Kesikli Veri", "Sürekli Veri"]},
            {"etiket": "Soru ve kimden?", "uyeler": ["Araştırma Sorusu", "Evren", "Örneklem"]},
            {"etiket": "Veriyi toplamak ve korumak", "uyeler": ["Anket Sorusu", "Güvenilir Kaynak", "Kişisel Veri"]}]}],
        "sorular": [
            S("Defne, 7/A'daki öğrencilerin günde kaç litre su içtiğini araştırıyor. Toplayacağı veriler hangi türdedir?", ["Kategorik veri", "Kesikli veri", "Sürekli veri"], 2,
              "1,5 L ile 2 L arasında başka değer olabilir mi?", "Su miktarı ölçülür; arada sınırsız değer olabilir: sürekli veri.",
              kaynak=[K("u3k2", "Araştırma Sorusu"), K("u3k1", "Sürekli Veri")],
              yardim={"adimlar": ["Anket sorusunun cevabı sayı mı, sözcük mü?", "Litreyi sayarak mı, ölçerek mi buluruz?", "Arada başka değer olabilir mi?"]}),
            S("“Okulumuzdaki öğrencilerin en sevdiği derslerin dağılımı nasıl bir eğilim gösterir?” araştırmasında veri türü ve evren hangisidir?",
              ["Kategorik veri; okuldaki bütün öğrenciler", "Sürekli veri; sadece 7/A sınıfı", "Kesikli veri; Türkiye'deki bütün öğrenciler"], 0,
              "Ders adı sayı mı, sözcük mü? Soru kimleri kapsıyor?", "Ders adları sözcüktür: kategorik. Soru okuldaki bütün öğrencileri kapsar: evren.",
              kaynak=[K("u3k1", "Kategorik Veri"), K("u3k2", "Evren")]),
            G("Ela'nın okulunda 8 sınıf var. Her sınıftan 5 öğrenciye anket sorusu soruldu. Ankete kaç öğrenci katıldı?", "40",
              "Sınıf sayısını her sınıftan seçilen kişi sayısıyla çarp.", "8 · 5 = 40 öğrenci. Bu 40 öğrenci örneklemdir.", birim="öğrenci",
              kaynak=[K("u3k2", "Örneklem"), K("u3k3", "Anket Sorusu")],
              yardim={"adimlar": ["Kaç sınıf var?", "Her sınıftan kaç öğrenciye soruldu?", "Sınıf sayısını her sınıftaki kişi sayısıyla çarp."]}),
            S("Hangisi “verileri toplama” adımında yapılır?", ["Anket sorusunu sorup cevapları kaydetmek", "Araştırma sorusunu yazmak", "Sonuçları yorumlamak"], 0,
              "4 adımı sırayla düşün: Sor, topla, …", "Anket sorusunu sormak ve cevapları kaydetmek 2. adım olan veri toplamadır.",
              kaynak=[K("u3k1", "Araştırmanın 4 Adımı"), K("u3k3", "Veri Toplama Planı")]),
            S("Buse'nin anketinde kilo ve boy soruları vardı. Bu veriler hangi türdedir ve onlarla ne yapılmalıdır?",
              ["Kategorik veri; herkese açık paylaşılmalı", "Sürekli veri; izinsiz paylaşılmamalı", "Kesikli veri; internette yayımlanmalı"], 1,
              "Kilo ve boy ölçülür mü, sayılır mı? Kime ait bilgiler?", "Kilo ve boy ölçülür: sürekli veri. Kişisel veridir; izinsiz paylaşılmaz.",
              kaynak=[K("u3k1", "Sürekli Veri"), K("u3k3", "İzin ve Gizlilik")]),
            G("Bir araştırmanın evreni 300 öğrenci. Örneklem için her 10 öğrenciden 1'i seçiliyor. Örneklemde kaç öğrenci olur?", "30",
              "300'ün içinde kaç tane 10 var?", "300 ÷ 10 = 30 öğrenci.", birim="öğrenci",
              kaynak=[K("u3k2", "Evren"), K("u3k2", "Örneklem")],
              yardim={"adimlar": ["Evrende kaç öğrenci var?", "Her 10 öğrenciden kaçı seçiliyor?", "300'ü 10'a böl."]}),
            S("Mustafa Bey orman yangınlarında her yıl yanan alanı (hektar) inceliyor. Veriyi nereden almalı ve bu veri hangi türdedir?",
              ["Bir arkadaşından; kategorik veri", "Sosyal medyadan; kesikli veri", "Resmî bir kurum sitesinden; sürekli veri"], 2,
              "Güvenilir kaynak hangisi? Alan ölçülür mü, sayılır mı?", "Resmî siteler güvenilirdir. Yanan alan ölçülür: sürekli veri.",
              kaynak=[K("u3k3", "Güvenilir Kaynak"), K("u3k1", "Sürekli Veri")])]
    }


# =================================================================
# Tema 3 · Konu 4–5: grafik çizimleri (şeffaf zemin, soru/adım görseli) ve kavram çizimleri
def sayi_yaz(v, ond=None):
    """Grafik etiketleri: 5,38 · 27,8 · 5 422 (binlik boşluk, ondalık virgül)."""
    if ond is None:
        ond = 0 if float(v).is_integer() else len(str(v).split(".")[1])
    s = f"{v:,.{ond}f}".replace(",", " ").replace(".", ",")
    return s


def cizgi_svg(etiketler, seriler, ymin, ymax, adim, w=330, h=176, baslik=None, deger_yaz=True, ond=None, efont=10, lejant=None):
    """Çizgi grafiği. seriler: [(değerler, renk)]. deger_yaz: noktaların üstüne değer yazılır."""
    ust = 30 if (baslik or lejant) else 14
    if baslik and lejant:
        ust = 44
    x0, y0 = 50, h - 26
    yuk = y0 - ust
    sx = lambda i: x0 + 18 + (w - x0 - 34) * (i / (len(etiketler) - 1))
    sy = lambda v: y0 - yuk * (v - ymin) / (ymax - ymin)
    g = ""
    v = ymin
    while v <= ymax + 1e-9:
        y = sy(v)
        g += f"<line x1='{x0}' y1='{y:.1f}' x2='{w - 8}' y2='{y:.1f}' stroke='#3a4570' stroke-width='1'/>" + txt(x0 - 6, y + 4, sayi_yaz(round(v, 3), ond), "#f5f6fa", 10, 600, "end")
        v += adim
    g += _ok(x0, y0, w - 8, y0) + _ok(x0, y0, x0, ust - 4)
    for i, e in enumerate(etiketler):
        g += txt(sx(i), y0 + 16, e, "#f5f6fa", efont, 600)
    for degerler, renk in seriler:
        pts = " ".join(f"{sx(i):.1f},{sy(d):.1f}" for i, d in enumerate(degerler))
        g += f"<polyline points='{pts}' fill='none' stroke='{renk}' stroke-width='3' stroke-linejoin='round' stroke-linecap='round'/>"
        for i, d in enumerate(degerler):
            g += f"<circle cx='{sx(i):.1f}' cy='{sy(d):.1f}' r='4.5' fill='{renk}' stroke='#1b2340' stroke-width='1.5'/>"
            if deger_yaz:
                g += txt(sx(i), sy(d) - 9, sayi_yaz(d, ond), renk, 10, 700)
    if baslik:
        g += txt(w / 2, 15, baslik, "#f2c14e", 12)
    if lejant:
        ly = 31 if baslik else 15
        lx = 60
        for ad, renk in lejant:
            g += f"<rect x='{lx}' y='{ly - 8}' width='14' height='5' rx='2' fill='{renk}'/>" + txt(lx + 18, ly - 2, ad, renk, 10, 700, "start")
            lx += 22 + len(ad) * 6.4
    return gsvg(w, h, g)


def nokta_grafik_svg(sayilar, mn, mx, w=300, h=150, baslik=None, eksen=None, renk=NIC):
    """Nokta grafiği: sayilar = {değer: kaç tane}; aynı değerdeki noktalar üst üste yığılır."""
    x0, x1, y0 = 30, w - 20, h - (40 if eksen else 26)
    sx = lambda v: x0 + (x1 - x0) * (v - mn) / (mx - mn)
    g = _ok(x0 - 10, y0, x1 + 10, y0)
    for v in range(mn, mx + 1):
        g += f"<line x1='{sx(v):.1f}' y1='{y0 - 5}' x2='{sx(v):.1f}' y2='{y0 + 5}' stroke='#f5f6fa' stroke-width='2'/>" + txt(sx(v), y0 + 19, str(v), "#f5f6fa", 12)
    for v, n in sayilar.items():
        for k in range(n):
            g += f"<circle cx='{sx(v):.1f}' cy='{y0 - 13 - k * 15}' r='6' fill='{renk}'/>"
    if eksen:
        g += txt((x0 + x1) / 2, h - 6, eksen, "#f5f6fa", 11, 600)
    if baslik:
        g += txt(w / 2, 15, baslik, "#f2c14e", 12)
    return gsvg(w, h, g)


def svg3_nokta_g():
    g = _ok(12, 88, 108, 88)
    for i, n in enumerate([2, 4, 3, 1]):
        x = 24 + i * 24
        g += f"<line x1='{x}' y1='84' x2='{x}' y2='92' stroke='#f5f6fa' stroke-width='2'/>" + txt(x, 104, str(i), "#f5f6fa", 11)
        for k in range(n):
            g += f"<circle cx='{x}' cy='{76 - k * 15}' r='6' fill='{NIC}'/>"
    return bg(g + txt(60, 20, "üst üste", "#f2c14e", 11))


def svg3_yigilmaz():
    g = _ok(10, 84, 110, 84)
    for i, x in enumerate([18, 31, 47, 58, 74, 90, 103]):
        g += f"<circle cx='{x}' cy='72' r='5' fill='{SUR}'/>"
    g += txt(30, 100, "5257", "#f5f6fa", 9, 600) + txt(88, 100, "5624", "#f5f6fa", 9, 600)
    g += txt(60, 40, "hep tek nokta", "#f2c14e", 11)
    return bg(g + txt(60, 114, "yığılma yok", SUR, 11))


def svg3_cizgi():
    g = _ok(16, 96, 108, 96) + _ok(16, 96, 16, 16)
    pts = [(26, 70), (46, 82), (66, 56), (86, 60), (102, 30)]
    g += f"<polyline points='{' '.join(f'{x},{y}' for x, y in pts)}' fill='none' stroke='#f2c14e' stroke-width='3' stroke-linejoin='round'/>"
    for x, y in pts:
        g += f"<circle cx='{x}' cy='{y}' r='4' fill='#f2c14e'/>"
    return bg(g + txt(64, 112, "zaman →", "#f5f6fa", 10, 600))


def svg3_yon():
    g = (_ok(14, 40, 40, 18) + "<path d='M40 18 l-9 1 6 7z' fill='#8ce99a'/>" + txt(27, 54, "artış", "#8ce99a", 11))
    g += (_ok(46, 18, 72, 40) + "<path d='M72 40 l-2 -9 -6 6z' fill='#6fb3ff'/>" + txt(60, 54, "azalış", "#6fb3ff", 10))
    g += (_ok(80, 30, 108, 30) + txt(94, 54, "sabit", "#f2c14e", 11))
    g += _ok(14, 96, 106, 96)
    pts = [(18, 86), (38, 70), (58, 72), (78, 72), (102, 88)]
    g += f"<polyline points='{' '.join(f'{x},{y}' for x, y in pts)}' fill='none' stroke='#f5f6fa' stroke-width='2.5'/>"
    return bg(g + txt(60, 113, "çizginin yönü", "#f2c14e", 10))


def svg3_hangi():
    g = _ok(10, 56, 54, 56) + _ok(66, 56, 110, 56)
    for i, hh in enumerate([20, 34, 26]):
        g += f"<rect x='{15 + i * 13}' y='{56 - hh}' width='9' height='{hh}' fill='{TEAL}'/>"
    pts = [(70, 44), (82, 36), (94, 40), (106, 20)]
    g += f"<polyline points='{' '.join(f'{x},{y}' for x, y in pts)}' fill='none' stroke='#f2c14e' stroke-width='3'/>"
    g += txt(32, 74, "say", TEAL, 11) + txt(88, 74, "zaman", "#f2c14e", 11)
    g += txt(32, 92, "karşılaştır", "#f5f6fa", 9, 600) + txt(88, 92, "değişim", "#f5f6fa", 9, 600)
    return bg(g)


def svg3_egilim():
    g = _ok(14, 96, 108, 96)
    pts = [(20, 30), (36, 38), (52, 32), (68, 54), (84, 50), (100, 76)]
    g += f"<polyline points='{' '.join(f'{x},{y}' for x, y in pts)}' fill='none' stroke='#6fb3ff' stroke-width='3' stroke-linejoin='round'/>"
    g += "<line x1='18' y1='24' x2='100' y2='86' stroke='#f2c14e' stroke-width='2.5' stroke-dasharray='5 4'/><path d='M104 90 l-10 -1 5 -7z' fill='#f2c14e'/>"
    return bg(g + txt(60, 113, "genel yön", "#f2c14e", 11))


def svg3_tahmin():
    g = _ok(14, 96, 108, 96) + "<line x1='76' y1='18' x2='76' y2='96' stroke='#5a6280' stroke-width='1.5' stroke-dasharray='3 3'/>"
    pts = [(18, 80), (36, 70), (54, 60), (72, 48)]
    g += f"<polyline points='{' '.join(f'{x},{y}' for x, y in pts)}' fill='none' stroke='{NIC}' stroke-width='3'/>"
    g += "<line x1='72' y1='48' x2='100' y2='32' stroke='#f2c14e' stroke-width='3' stroke-dasharray='5 4'/>" + txt(102, 26, "?", "#f2c14e", 18)
    return bg(g + txt(40, 113, "veri", NIC, 11) + txt(94, 113, "ötesi", "#f2c14e", 11))


def svg3_referans():
    g = "<rect x='14' y='34' width='92' height='34' fill='#8ce99a' opacity='0.25'/>"
    g += "<line x1='14' y1='34' x2='106' y2='34' stroke='#8ce99a' stroke-width='2' stroke-dasharray='5 4'/><line x1='14' y1='68' x2='106' y2='68' stroke='#8ce99a' stroke-width='2' stroke-dasharray='5 4'/>"
    g += "<circle cx='66' cy='46' r='7' fill='#f2c14e'/>" + txt(60, 26, "referans aralığı", "#8ce99a", 10)
    return bg(g + txt(60, 94, "karşılaştır", "#f2c14e", 12))


def svg3_temsil_deger():
    g = _ok(14, 92, 106, 92)
    for i, hh in enumerate([60, 58, 60, 52, 42]):
        g += f"<rect x='{20 + i * 17}' y='{92 - hh}' width='11' height='{hh}' rx='2' fill='{TEAL}'/>"
    g += "<line x1='14' y1='38' x2='106' y2='38' stroke='#f2c14e' stroke-width='3'/>" + txt(60, 26, "27,8", "#f2c14e", 15)
    return bg(g + txt(60, 112, "tek sayıyla özet", "#f2c14e", 10))


def svg3_yok():
    g = "<rect x='12' y='14' width='60' height='76' rx='8' fill='#f5f6fa'/>"
    for i, s in enumerate(["30,0", "29,6", "30,0", "27,1", "22,4"]):
        g += txt(42, 30 + i * 14, s, "#1b2340", 11)
    g += txt(94, 54, "27,8", "#f2c14e", 15) + txt(94, 74, "yok ama", "#f5f6fa", 9, 600) + txt(94, 86, "temsil eder", "#f5f6fa", 9, 600)
    return bg(g + txt(60, 112, "listede olmayabilir", "#f2c14e", 10))


def svg3_iddia():
    g = txt(60, 30, "“En az 13 km”", "#f2c14e", 12)
    g += _ok(14, 70, 106, 70)
    for x in (20, 38, 50, 58, 72):
        g += f"<circle cx='{x}' cy='62' r='4' fill='{NIC}'/>"
    g += "<line x1='86' y1='48' x2='86' y2='78' stroke='#ff8fb1' stroke-width='3'/>" + txt(86, 92, "13", "#ff8fb1", 12)
    return bg(g + txt(60, 112, "veriyle sına", "#f2c14e", 11))


def svg3_ortalama():
    g = ""
    for i, hh in enumerate([4, 6, 8]):
        g += f"<rect x='{18 + i * 20}' y='{90 - hh * 8}' width='14' height='{hh * 8}' rx='2' fill='{NIC}'/>"
    g += txt(42, 104, "4 + 6 + 8", "#f5f6fa", 10, 600) + txt(92, 60, "=", "#f2c14e", 16)
    for i in range(3):
        g += f"<rect x='{80 + i * 9}' y='{90 - 48}' width='7' height='48' rx='2' fill='#f2c14e'/>"
    return bg(g + txt(94, 104, "6 6 6", "#f2c14e", 10))


def svg3_ortanca():
    g = ""
    for i, s in enumerate(["1", "3", "5", "7", "9"]):
        r = "#f2c14e" if i == 2 else "#5a6280"
        g += f"<rect x='{8 + i * 21}' y='42' width='19' height='28' rx='5' fill='{r}'/>" + txt(17.5 + i * 21, 61, s, "#1b2340" if i == 2 else "#f5f6fa", 14)
    return bg(g + txt(60, 30, "sırala", "#f5f6fa", 11, 600) + txt(60, 96, "ortadaki", "#f2c14e", 12))


def svg3_tepe():
    g = _ok(14, 86, 106, 86)
    for i, n in enumerate([2, 3, 1]):
        x = 32 + i * 28
        g += txt(x, 102, str(i + 2), "#f5f6fa", 12)
        for k in range(n):
            g += f"<circle cx='{x}' cy='{76 - k * 15}' r='6' fill='{'#f2c14e' if n == 3 else NIC}'/>"
    return bg(g + txt(60, 20, "en çok tekrar", "#f2c14e", 11))


# Veri setleri (kitaptan; altın fiyatları en yakın TL'ye yuvarlandı)
ALTIN_G = ["27.10", "28.10", "31.10", "05.11", "10.11", "11.11"]
ALTIN_D = [5422, 5258, 5448, 5370, 5524, 5624]
KAR_G = ["1970–80", "1981–91", "1992–02", "2003–13", "2014–24"]
KAR_D = [30.0, 29.6, 30.0, 27.1, 22.4]
ATLAMA_G = ["2017", "2018", "2019", "2020", "2021"]
ATLAMA_D = [5.17, 5.27, 5.38, 5.37, 5.36]
FIDAN_G = ["1. hf", "2. hf", "3. hf", "4. hf", "5. hf", "6. hf"]
FIDAN_D = [10, 12, 17, 18, 21, 23]                    # kitap dışı örnek
KARDES = {0: 2, 1: 5, 2: 3, 3: 1, 4: 1}                # 12 öğrencinin kardeş sayısı (kitap dışı örnek)
PERS_G = ["Doğum", "1 ay", "2 ay", "3 ay", "6 ay", "9 ay", "12 ay"]
P25 = [34.0, 37.0, 38.7, 40.2, 42.7, 44.9, 46.1]
P50 = [34.9, 37.8, 39.5, 41.1, 43.6, 45.8, 47.0]
P75 = [35.9, 38.7, 40.6, 42.0, 44.5, 46.6, 47.9]
P25R, P50R, P75R = "#6fb3ff", "#8ce99a", "#ffa26b"


def altin_svg(deger=True):
    return cizgi_svg(ALTIN_G, [(ALTIN_D, "#f2c14e")], 5200, 5700, 100, baslik="Gram altın alış fiyatı (TL, yaklaşık)", deger_yaz=deger)


def kar_svg(deger=True):
    return cizgi_svg(KAR_G, [(KAR_D, "#6fb3ff")], 20, 32, 2, baslik="Ortalama kar örtülü gün sayısı", deger_yaz=deger, ond=1 if deger else 0, efont=9)


def atlama_svg(deger=True):
    return cizgi_svg(ATLAMA_G, [(ATLAMA_D, OB)], 5.1, 5.4, 0.05, baslik="Esra Bayrak'ın atlayışları (m)", deger_yaz=deger, ond=2)


def fidan_svg(deger=True):
    return cizgi_svg(FIDAN_G, [(FIDAN_D, "#8ce99a")], 8, 26, 2, baslik="Fidanın boyu (cm)", deger_yaz=deger)


def kardes_svg():
    return nokta_grafik_svg(KARDES, 0, 4, baslik="7/B'de 12 öğrencinin kardeş sayısı", eksen="Kardeş sayısı")


def persentil_svg():
    return cizgi_svg(PERS_G, [(P25, P25R), (P50, P50R), (P75, P75R)], 32, 48, 2, h=200, baslik="Erkek bebeklerin baş çevresi (cm)",
                     deger_yaz=False, efont=9, lejant=[("P25", P25R), ("P50", P50R), ("P75", P75R)])


# =================================================================
def u3k4():
    return {
        "id": "u3k4", "unite": T3, "baslik": "Nokta ve Çizgi Grafiği", "sayfalar": "s. 171–172",
        "giris": "Verileri topladık. Şimdi onları bir resme çevireceğiz. Bu resme grafik diyoruz. Bu konuda nokta grafiğini hatırlayacağız ve çizgi grafiğini tanıyacağız. Çizgi grafiği, bir şeyin zamanla nasıl değiştiğini en iyi gösteren grafiktir.",
        "hazirlik": {
            "baslik": "Hazır mısın?",
            "giris": "Bu konuda grafik okuyacağız ve ondalık sayıları karşılaştıracağız. Önce bunları hatırlıyor musun bakalım. Not yok.",
            "maddeler": [
                {"ad": "Sütun grafiği okuma", "sinif": "Önceki yıllar", "svg": svg3_h_sutun(),
                 "anlatim": "Sütun grafiğinde her sütunun boyu bir sayıyı gösterir. Sütunun tepesinden sola, sayıların yazdığı eksene bakarak değeri okuruz.",
                 "akilda": "Sütunun tepesi = değer",
                 "ornek": {"problem": "Grafikte Salı günü kaç kitap okunmuş?", "adimlar": [
                     {"metin": "Salı sütununu bul.", "islem": "Sa"},
                     {"metin": "Sütunun tepesinden sola bak.", "islem": "5 kitap"}]},
                 "sorular": [
                     G("Grafiğe göre Çarşamba günü kaç kitap okunmuş?", "2", "Çarşamba sütununun tepesinden sola bak.", "Çarşamba sütunu 2'ye kadar uzanıyor.",
                       svg=sutun_svg(["Pzt", "Salı", "Çrş"], [3, 5, 2], 5, baslik="Okunan kitap sayısı"),
                       yardim={"adimlar": ["Çarşamba sütununu bul.", "Tepesinden sola, sayı eksenine bak."]}),
                     S("Grafiğe göre en az kitap hangi gün okunmuş?", ["Pazartesi", "Salı", "Çarşamba"], 2,
                       "En kısa sütunu bul.", "En kısa sütun Çarşamba'ya ait: 2 kitap.",
                       svg=sutun_svg(["Pzt", "Salı", "Çrş"], [3, 5, 2], 5, baslik="Okunan kitap sayısı"))]},
                {"ad": "Sürekli veri", "sinif": "3. tema, 1. konu", "svg": svg3_surekli(),
                 "anlatim": "Ölçerek bulduğumuz, iki değer arasında başka değer olabilen veri süreklidir: boy, sıcaklık, fiyat.",
                 "akilda": "Ölçerek bulunur: sürekli",
                 "sorular": [
                     S("Bir ürünün her gün değişen fiyatı hangi veri türüdür?", ["Kategorik veri", "Kesikli veri", "Sürekli veri"], 2,
                       "Fiyatlar arasında başka fiyat olabilir mi?", "24,75 TL ile 24,80 TL arasında başka fiyat olabilir: sürekli veri. (s. 163)"),
                     S("Hangisi sürekli veridir?", ["Bir fidanın boyu", "Sınıftaki öğrenci sayısı", "En sevilen meyve"], 0,
                       "Hangisini cetvelle ölçeriz?", "Fidanın boyu ölçülür: sürekli veri.")]},
                {"ad": "Ondalık sayıları karşılaştırma", "sinif": "1. tema, 5. konu", "svg": svg3_h_arada(),
                 "anlatim": "Önce virgülden önceki kısma bakarız. Aynıysa virgülden sonraki basamakları soldan sağa karşılaştırırız: 5,38 > 5,27 çünkü 3 > 2.",
                 "akilda": "Soldan sağa, basamak basamak",
                 "ornek": {"problem": "5,38 mi büyük, 5,36 mı?", "adimlar": [
                     {"metin": "Virgülden önceki kısımlar aynı: 5.", "islem": "5 = 5"},
                     {"metin": "Onda birler aynı: 3. Yüzde birlere bak: 8 > 6.", "islem": "5,38 > 5,36"}]},
                 "sorular": [
                     S("Hangisi en büyüktür?", ["5,27", "5,38", "5,36"], 1,
                       "Virgülden sonraki ilk basamaklar: 2, 3, 3. Eşit olanlarda ikinci basamağa bak.", "5,38 > 5,36 > 5,27."),
                     S("Hangisi en küçüktür?", ["22,4", "27,1", "29,6"], 0,
                       "Virgülden önceki kısma bak.", "22 < 27 < 29: en küçük 22,4.")]}
            ]},
        "kavramlar": [
            {"ad": "Nokta Grafiği", "renk": "#1f9e8f", "svg": svg3_nokta_g(),
             "aciklama": "Nokta grafiğinde her veri bir noktadır. Aynı değerdeki veriler sayı doğrusunun üstünde üst üste yığılır.",
             "ek": "Yığın ne kadar yüksekse o değer o kadar çok tekrar etmiştir. Kardeş sayısı gibi sayarak bulunan verilerde iyi çalışır. (s. 172)",
             "akilda": "Aynı değer: üst üste",
             "cozum": {"baslik": "Nokta grafiğini oku",
                       "problem": "7/B'deki 12 öğrencinin kardeş sayıları nokta grafiğinde. Kaç öğrencinin 1 kardeşi var?",
                       "svg": kardes_svg(),
                       "adimlar": [
                           {"metin": "Alttaki sayı doğrusunda 1'i bul.", "islem": "1 kardeş"},
                           {"metin": "1'in üstündeki noktaları say. Her nokta bir öğrenci.", "islem": "5 nokta"}],
                       "sonuc": "5 öğrencinin 1 kardeşi var. En yüksek yığın da bu: en çok tekrar eden değer 1."},
             "soru": G("Grafikte kaç öğrencinin 2 kardeşi var?", "3", "2'nin üstündeki noktaları say.", "2'nin üstünde 3 nokta var: 3 öğrenci.",
                       svg=kardes_svg(), birim="öğrenci", yardim={"adimlar": ["Sayı doğrusunda 2'yi bul.", "Üstündeki noktaları tek tek say."]})},
            {"ad": "Nokta Grafiği Ne Zaman Uymaz?", "renk": "#7b4fc9", "svg": svg3_yigilmaz(),
             "aciklama": "Altın fiyatı gibi sürekli verilerde neredeyse her değer farklıdır. Noktalar yığılmaz; her değerde tek nokta kalır.",
             "ek": "Nokta grafiği verileri yığarak gösterir. Sürekli verilerin yığılmalı gösterilmesi gerekmez. Ayrıca nokta grafiğinde günlerin sırası görünmez, değişim izlenemez. (s. 172)",
             "akilda": "Hep farklı değer: yığın olmaz",
             "soru": S("Gram altının 11 günlük fiyatları (5 421,88 · 5 257,73 · 5 390,82 …) nokta grafiğine uygun mu?",
                       ["Uygun; noktalar üst üste yığılır.", "Uygun değil; değerler hep farklı, değişim görünmez.", "Uygun; çünkü veri kategoriktir."], 1,
                       "Bilgi kartına bak: değerler birbirini tekrar ediyor mu?", "Fiyatlar hep farklıdır ve sürekli veridir; yığılma olmaz, değişim de görünmez. (s. 172)")},
            {"ad": "Çizgi Grafiği", "renk": "#b7791f", "svg": svg3_cizgi(),
             "aciklama": "Çizgi grafiğinde noktalar bir çizgiyle birleştirilir. Yatay eksende zaman, dikey eksende ölçülen değer vardır. (s. 172)",
             "ek": "Bir değişkenin zamana bağlı değişimini göstermek için en etkili grafiktir. Bir noktanın değerini okumak için noktadan sola, dikey eksene bakarız. (s. 172)",
             "akilda": "Noktaları birleştir: zamanla değişim",
             "cozum": {"baslik": "Çizgi grafiğini oku",
                       "problem": "Grafikte gram altının bazı günlerdeki alış fiyatları var. 31 Ekim'de 1 gram altın kaç TL?",
                       "svg": altin_svg(),
                       "adimlar": [
                           {"metin": "Yatay eksende (zaman) 31.10'u bul.", "islem": "31.10"},
                           {"metin": "Yukarı çık, çizginin üstündeki noktayı bul.", "islem": "nokta"},
                           {"metin": "Noktanın yanındaki değeri oku. Emin olmak için sola, dikey eksene bak: 5 400 ile 5 500 arasında.", "islem": "5 448 TL"}],
                       "sonuc": "31 Ekim'de 1 gram altın yaklaşık 5 448 TL. (s. 171–172)"},
             "sende": {"baslik": "Sıra sende",
                       "problem": "Aynı grafikte 11 Kasım'daki fiyatı bul.",
                       "svg": altin_svg(),
                       "adimlar": [
                           {"metin": "Yatay eksende 11.11'i bul.", "islem": "11.11 (en sağdaki)"},
                           {"metin": "Noktanın değerini oku.",
                            "soru": G("11 Kasım'da 1 gram altın kaç TL?", "5624", "En sağdaki noktanın üstüne bak.", "En sağdaki nokta 5 624 TL.", birim="TL",
                                      svg=altin_svg(), yardim={"adimlar": ["Yatay eksende en sağdaki tarihi bul.", "Noktanın üstündeki sayıyı oku."]}),
                            "islem": "5 624 TL"}],
                       "sonuc": "Harika! Grafikteki en yüksek fiyat da bu."},
             "soru": S("Çizgi grafiğinde yatay eksende genellikle ne olur?", ["Zaman (gün, hafta, yıl)", "Kategoriler (renkler)", "Hiçbir şey"], 0,
                       "Çizgi grafiği neyin değişimini gösteriyordu?", "Çizgi grafiği zamana bağlı değişimi gösterir; yatay eksende zaman olur. (s. 172)")},
            {"ad": "Artış, Azalış, Sabit", "renk": "#2f8f73", "svg": svg3_yon(),
             "aciklama": "Çizgi yukarı çıkıyorsa artış, aşağı iniyorsa azalış, düz gidiyorsa değişim yok (sabit) demektir. (s. 172)",
             "ek": "Çizgi ne kadar dikse değişim o kadar büyüktür. En büyük değişimi bulmak için iki nokta arasındaki farkı hesaplarız: büyükten küçüğü çıkar.",
             "akilda": "Yukarı artış, aşağı azalış",
             "cozum": {"baslik": "En büyük artış",
                       "problem": "Ela fidanının boyunu 6 hafta ölçtü (kitap dışı örnek). Hangi iki hafta arasında en çok uzadı?",
                       "svg": fidan_svg(),
                       "adimlar": [
                           {"metin": "Çizgi hep yukarı gidiyor: fidan her hafta uzamış.", "islem": "artış"},
                           {"metin": "En dik çıkan parçayı bul: 2. hafta ile 3. hafta arası.", "islem": "12 → 17"},
                           {"metin": "Farkı hesapla: büyükten küçüğü çıkar.", "islem": "17 − 12 = 5 cm"}],
                       "sonuc": "En çok artış 2. ve 3. hafta arasında: 5 cm."},
             "sende": {"baslik": "Sıra sende",
                       "problem": "Altın grafiğinde 27 Ekim'den 28 Ekim'e fiyat ne oldu?",
                       "svg": altin_svg(),
                       "adimlar": [
                           {"metin": "Çizginin yönüne bak.",
                            "soru": S("27.10'dan 28.10'a çizgi nereye gidiyor?", ["Yukarı", "Aşağı", "Düz"], 1,
                                      "İlk iki noktayı karşılaştır.", "5 422'den 5 258'e iniyor: aşağı."),
                            "islem": "Aşağı → azalış"},
                           {"metin": "Ne kadar azaldı?",
                            "soru": G("Fiyat kaç TL azaldı?", "164", "Büyükten küçüğü çıkar: 5 422 − 5 258.", "5 422 − 5 258 = 164 TL.", birim="TL",
                                      yardim={"adimlar": ["İki fiyatı oku: 5 422 ve 5 258.", "Büyükten küçüğü çıkar."]}),
                            "islem": "164 TL azaldı"}],
                       "sonuc": "Harika! Çizgi aşağı inince azalış olur."},
             "soru": S("Bir çizgi grafiğinde çizgi iki nokta arasında düz gidiyorsa ne anlarız?", ["Değer arttı.", "Değer azaldı.", "Değer değişmedi."], 2,
                       "Bilgi kartında “düz” kelimesine bak.", "Düz çizgi: iki zaman arasında değer aynı kalmış.")},
            {"ad": "Hangi Grafik?", "renk": "#5f3dc4", "svg": svg3_hangi(),
             "aciklama": "Sayıp karşılaştırmak için sütun ya da nokta grafiği; bir değerin zamanla nasıl değiştiğini görmek için çizgi grafiği kullanırız.",
             "ek": "Altın fiyatları sütun grafiğiyle de çizilebilir; günler karşılaştırılır ama değerleri okumak ve değişimi izlemek zordur. Bu yüzden çizgi grafiği daha uygundur. (s. 171)",
             "akilda": "Zamanla değişim: çizgi",
             "soru": S("Bir şehrin 1 hafta boyunca her gün öğlen ölçülen sıcaklığı hangi grafikle en iyi gösterilir?", ["Nokta grafiği", "Çizgi grafiği", "Hiçbiri"], 1,
                       "Zamanla değişen sürekli bir veri mi?", "Sıcaklık zamanla değişen sürekli veridir: çizgi grafiği. (s. 172)")}
        ],
        "gruplar": [{"soru": "Hangi grafikle ilgili?", "kutular": [
            {"etiket": "Noktalar üst üste", "uyeler": ["Nokta Grafiği", "Nokta Grafiği Ne Zaman Uymaz?"]},
            {"etiket": "Noktalar çizgiyle birleşir", "uyeler": ["Çizgi Grafiği", "Artış, Azalış, Sabit"]},
            {"etiket": "Grafik seçme", "uyeler": ["Hangi Grafik?"]}]}],
        "akildaKalsin": [
            "Nokta grafiğinde aynı değerler üst üste yığılır.",
            "Sürekli verilerde değerler hep farklıdır; nokta grafiği uygun olmaz.",
            "Çizgi grafiği zamanla değişimi gösterir: yatayda zaman, dikeyde değer.",
            "Çizgi yukarı: artış. Aşağı: azalış. Düz: sabit.",
            "En büyük değişim için iki değerin farkını bul: büyükten küçüğü çıkar."],
        "merakKutusu": [
            {"soru": "Altın fiyatlarını kim yayımlıyor?", "cevap": "Türkiye Cumhuriyet Merkez Bankası her gün altın ve döviz verilerini paylaşır. Kitaptaki fiyatlar saat 15.00'te geçerli olan alış fiyatlarıdır. (s. 171)"},
            {"soru": "Çizgi grafiğinde noktaların arasındaki çizgi ne anlatır?", "cevap": "İki ölçüm arasındaki değişimi gösterir. Çizgi sayesinde artış ve azalış bir bakışta görülür. (s. 172)"},
            {"soru": "Dikey eksen neden 0'dan başlamıyor?", "cevap": "Altın fiyatları hep 5 200 ile 5 700 arasında. Ekseni 0'dan başlatsaydık çizgi neredeyse düz görünürdü ve değişim fark edilmezdi. (s. 172)"},
            {"soru": "Sütun grafiği hiç mi işe yaramaz?", "cevap": "Yarar! Günleri karşılaştırmak için kullanılabilir. Ama değerleri okumak ve değişimi izlemek çizgi grafiğinde daha kolaydır. (s. 171)"},
            {"soru": "Günlük hayatta hangi veriler çizgi grafiğine uygun?", "cevap": "Zamanla değişen sürekli veriler: bir fidanın boyu, günlük sıcaklık, bir ürünün fiyatı, bir bebeğin kilosu. (s. 172)"}],
        "dusunVeYaz": [{"soru": "Bir sınıftaki öğrencilerin kardeş sayıları için nokta grafiği, bir haftalık hava sıcaklığı için çizgi grafiği seçiliyor. Neden?",
                        "ornekCevap": "Kardeş sayıları tekrar eder, aynı değerler üst üste yığılır; nokta grafiği uygun. Sıcaklık zamanla değişen sürekli veri; değişimi çizgi grafiği gösterir.",
                        "anahtarlar": ["yığıl", "tekrar", "zaman", "değiş", "sürekli"]}],
        "sorular": [
            N("Nokta grafiğine göre en çok tekrar eden kardeş sayısı hangisi? Sayı doğrusunda dokun.", 1, {"min": 0, "max": 4},
              "En yüksek yığını bul.", "1'in üstünde 5 nokta var: en yüksek yığın.", svg=kardes_svg(), kavram="Nokta Grafiği",
              yardim={"adimlar": ["Her sayının üstündeki noktaları say.", "En çok nokta hangi sayının üstünde?"]}),
            G("Nokta grafiğine göre kaç öğrencinin 3 ya da daha fazla kardeşi var?", "2", "3'ün ve 4'ün üstündeki noktaları topla.", "3'te 1, 4'te 1 nokta: 2 öğrenci.",
              svg=kardes_svg(), birim="öğrenci", kavram="Nokta Grafiği",
              yardim={"adimlar": ["“3 ya da daha fazla” hangi sayılar? 3 ve 4.", "3'ün üstündeki noktaları say.", "4'ün üstündekileri de say ve topla."]}),
            G("Altın grafiğine göre 5 Kasım'da 1 gram altın kaç TL?", "5370", "05.11'in üstündeki noktaya bak.", "05.11 noktasında 5 370 TL yazıyor.",
              svg=altin_svg(), birim="TL", kavram="Çizgi Grafiği",
              yardim={"adimlar": ["Yatay eksende 05.11'i bul.", "Yukarı çık, noktayı bul ve değerini oku."]}),
            S("Altın grafiğine göre en düşük fiyat hangi gün?", ["27 Ekim", "28 Ekim", "5 Kasım"], 1,
              "En alttaki noktayı bul.", "En alttaki nokta 28.10: 5 258 TL. (s. 172)", svg=altin_svg(), kavram="Çizgi Grafiği"),
            S("Altın grafiğinde 5 Kasım'dan 11 Kasım'a fiyat nasıl değişmiş?", ["Sürekli azalmış.", "Hiç değişmemiş.", "Sürekli artmış."], 2,
              "Son üç noktada çizgi nereye gidiyor?", "5 370 → 5 524 → 5 624: çizgi hep yukarı, fiyat artmış.", svg=altin_svg(), kavram="Artış, Azalış, Sabit"),
            G("Fidan grafiğine göre fidan 1. haftadan 6. haftaya kadar toplam kaç cm uzamış?", "13", "Son boydan ilk boyu çıkar.", "23 − 10 = 13 cm.",
              svg=fidan_svg(), birim="cm", kavram="Artış, Azalış, Sabit",
              yardim={"adimlar": ["1. haftadaki boyu oku.", "6. haftadaki boyu oku.", "Büyükten küçüğü çıkar."]}),
            S("Fidan grafiğinde en az uzama hangi iki hafta arasında?", ["3. ve 4. hafta", "1. ve 2. hafta", "5. ve 6. hafta"], 0,
              "En yatık (en az eğimli) parçayı bul ya da farkları hesapla.", "17 → 18: sadece 1 cm. En yatık parça burası.", svg=fidan_svg(), kavram="Artış, Azalış, Sabit"),
            S("Hangi veri seti için çizgi grafiği en uygundur?", ["Sınıftaki öğrencilerin göz renkleri", "Bir sınıfta en sevilen dersler", "Bir bebeğin 12 ay boyunca her ay ölçülen boyu"], 2,
              "Hangisi zamanla değişen sürekli bir veri?", "Bebeğin boyu zamanla değişen sürekli veridir: çizgi grafiği. (s. 172)", kavram="Hangi Grafik?"),
            S("Melis günlük altın fiyatlarını nokta grafiğiyle göstermek istiyor. Hangisi doğrudur?",
              ["Fiyatlar hep farklı olduğu için noktalar yığılmaz; çizgi grafiği daha uygun olur.", "Nokta grafiği en uygun grafiktir.", "Altın fiyatı kategorik veridir."], 0,
              "Fiyatlar tekrar ediyor mu?", "Sürekli verilerde değerler hep farklıdır; değişimi çizgi grafiği gösterir. (s. 172)", kavram="Nokta Grafiği Ne Zaman Uymaz?"),
            N("Nokta grafiğinde en az öğrencinin olduğu kardeş sayılarından küçük olanına dokun.", 3, {"min": 0, "max": 4},
              "En alçak yığınlar hangileri? Onlardan küçüğünü seç.", "3 ve 4'te birer nokta var; küçük olan 3.", svg=kardes_svg(), kavram="Nokta Grafiği",
              yardim={"adimlar": ["Her sayının üstündeki noktaları say.", "En az nokta olan sayıları bul.", "Bu sayılardan küçük olanı seç."]})]
    }


def u3k5():
    return {
        "id": "u3k5", "unite": T3, "baslik": "Temsil Değeri ve Tahmin", "sayfalar": "s. 173–179",
        "giris": "Grafiği çizdik. Şimdi yorumlama zamanı! Bu konuda grafiğin genel yönünü (eğilimi) okuyacağız, gelecek için tahmin yapacağız. Sonra bir veri setini tek bir sayıyla özetlemeyi ve bir iddiayı verilerle sınamayı öğreneceğiz.",
        "hazirlik": {
            "baslik": "Hazır mısın?",
            "giris": "Bu konuda aritmetik ortalama, ortanca ve tepe değeri kullanacağız. Önceki yıllardan hatırlıyor musun bakalım. Not yok.",
            "maddeler": [
                {"ad": "Aritmetik ortalama", "sinif": "Önceki yıllar", "svg": svg3_ortalama(),
                 "anlatim": "Bütün verileri topla, toplamı veri sayısına böl. Sonuç, verileri eşit paylaştırsaydık her birine düşen değerdir.",
                 "akilda": "Topla, kaç tane varsa ona böl",
                 "ornek": {"problem": "4, 6, 8 sayılarının aritmetik ortalaması kaçtır?", "adimlar": [
                     {"metin": "Bütün sayıları topla.", "islem": "4 + 6 + 8 = 18"},
                     {"metin": "Kaç sayı var? 3. Toplamı 3'e böl.", "islem": "18 ÷ 3 = 6"}]},
                 "sorular": [
                     G("2, 5, 8 sayılarının aritmetik ortalaması kaçtır?", "5", "Topla, sonra 3'e böl.", "2 + 5 + 8 = 15; 15 ÷ 3 = 5.",
                       yardim={"adimlar": ["Üç sayıyı topla.", "Toplamı 3'e böl."]}),
                     G("10, 20, 30, 40 sayılarının aritmetik ortalaması kaçtır?", "25", "Topla, sonra 4'e böl.", "10 + 20 + 30 + 40 = 100; 100 ÷ 4 = 25.",
                       yardim={"adimlar": ["Dört sayıyı topla.", "Toplamı 4'e böl."]})]},
                {"ad": "Ortanca", "sinif": "Önceki yıllar", "svg": svg3_ortanca(),
                 "anlatim": "Verileri küçükten büyüğe sırala. Tam ortadaki değer ortancadır. Veri sayısı çiftse ortadaki iki değerin ortalaması alınır.",
                 "akilda": "Sırala, ortadakini al",
                 "ornek": {"problem": "7, 1, 9, 3, 5 verilerinin ortancası kaçtır?", "adimlar": [
                     {"metin": "Küçükten büyüğe sırala.", "islem": "1, 3, 5, 7, 9"},
                     {"metin": "5 veri var; ortadaki 3. sıradaki.", "islem": "Ortanca = 5"}]},
                 "sorular": [
                     G("8, 2, 6 verilerinin ortancası kaçtır?", "6", "Önce sırala: 2, 6, 8.", "Sıralı: 2, 6, 8. Ortadaki 6.",
                       yardim={"adimlar": ["Sayıları küçükten büyüğe sırala.", "Ortadaki sayıyı bul."]}),
                     G("4, 9, 1, 7, 3 verilerinin ortancası kaçtır?", "4", "Önce sırala.", "Sıralı: 1, 3, 4, 7, 9. Ortadaki 4.",
                       yardim={"adimlar": ["Sayıları küçükten büyüğe sırala.", "5 sayı var; 3. sıradakini bul."]})]},
                {"ad": "Tepe değer", "sinif": "Önceki yıllar", "svg": svg3_tepe(),
                 "anlatim": "Veri setinde en çok tekrar eden değere tepe değer denir. Nokta grafiğinde en yüksek yığındır.",
                 "akilda": "En çok tekrar eden",
                 "sorular": [
                     G("2, 3, 3, 5, 3, 2 verilerinin tepe değeri kaçtır?", "3", "Hangi sayı en çok yazılmış?", "3 üç kez tekrar ediyor: tepe değer 3.",
                       yardim={"adimlar": ["Her sayının kaç kez yazıldığını say.", "En çok yazılan sayıyı seç."]}),
                     G("10,5 · 12,5 · 10,5 · 9,0 verilerinin tepe değeri kaçtır?", "10,5", "Hangi sayı iki kez yazılmış?", "10,5 iki kez tekrar ediyor.", denk=True,
                       yardim={"adimlar": ["Her sayının kaç kez yazıldığını say.", "En çok yazılan sayıyı seç."]})]}
            ]},
        "kavramlar": [
            {"ad": "Eğilim", "renk": "#2364c7", "svg": svg3_egilim(),
             "aciklama": "Eğilim, çizginin genel yönüdür. Arada küçük inişler çıkışlar olsa da çizgi genel olarak artıyor mu, azalıyor mu ona bakarız.",
             "ek": "Türkiye'de ortalama kar örtülü gün sayısı 1970–1980'de 30,0 iken 2014–2024'te 22,4 olmuş. Arada küçük bir artış olsa da genel eğilim azalıştır. (s. 175)",
             "akilda": "Genel yön: eğilim",
             "cozum": {"baslik": "Eğilimi bul",
                       "problem": "Kar örtülü gün sayısının 1970–2024 arasındaki eğilimi nasıldır?",
                       "svg": kar_svg(),
                       "adimlar": [
                           {"metin": "İlk ve son değere bak.", "islem": "30,0 → 22,4"},
                           {"metin": "Aradaki küçük değişimlere takılma: 29,6'dan 30,0'a küçük bir çıkış var.", "islem": "küçük iniş çıkış"},
                           {"metin": "Çizgi genel olarak nereye gidiyor? Aşağı.", "islem": "Eğilim: azalış"}],
                       "sonuc": "Kar örtülü gün sayısı azalma eğilimindedir; özellikle son iki dönemde hızla azalmış. (s. 175)"},
             "soru": S("Bir çizgi grafiği arada bir kez inip genel olarak yukarı çıkıyor. Eğilimi nedir?", ["Artış", "Azalış", "Sabit"], 0,
                       "Bilgi kartı: küçük inişlere değil, genel yöne bak.", "Genel yön yukarı: eğilim artıştır.")},
            {"ad": "Veri Ötesi: Tahmin", "renk": "#1f9e8f", "svg": svg3_tahmin(),
             "aciklama": "Eğilime bakarak gelecekte ne olabileceğini tahmin edebiliriz. Buna veri ötesini yorumlamak denir. (s. 174)",
             "ek": "Tahmin kesin değildir; “… olabilir” deriz. Kitaptaki örnek: Bir çiftçi son 10 yılda yağışın azaldığını görür ve kuraklığa dayanıklı ürün ekmeye ya da damla sulama yaptırmaya karar verir. (s. 174)",
             "akilda": "Eğilim devam ederse…",
             "soru": S("Kar örtülü gün sayısı azalma eğiliminde. 2025–2035 için en uygun tahmin hangisi?",
                       ["Kesinlikle 40 güne çıkacak.", "Bir daha hiç kar yağmayacak.", "Kar örtülü gün sayısı azalmaya devam edebilir."], 2,
                       "Tahmin eğilime uymalı ama kesin konuşmamalı.", "Eğilim azalış; tahmin “azalmaya devam edebilir” olur. Tahmin kesin değildir. (s. 174–175)")},
            {"ad": "Referans Değeri", "renk": "#2f8f73", "svg": svg3_referans(),
             "aciklama": "Referans değeri, bir ölçümü karşılaştırmak için önceden belirlenmiş değerdir. (s. 177)",
             "ek": "Doktorlar bebeğin baş çevresini persentil eğrileriyle karşılaştırır. P50 (50. persentil) değerindeki bebek normal aralıktadır; P75'teki bebek yaşıtlarının %75'inden büyüktür. (s. 177)",
             "akilda": "Karşılaştırma için hazır değer",
             "cozum": {"baslik": "Kerem'in baş çevresi",
                       "problem": "9 aylık Kerem'in baş çevresi 46 cm. Grafikteki referans değerlerine göre nasıl yorumlarsın?",
                       "svg": persentil_svg(),
                       "adimlar": [
                           {"metin": "Grafikte 9 ay sütununu bul ve değerleri oku.", "islem": "P50 = 45,8 · P75 = 46,6"},
                           {"metin": "46 hangi iki değerin arasında?", "islem": "45,8 < 46 < 46,6"},
                           {"metin": "Yorumla: P50'nin biraz üstünde, P75'in altında.", "islem": "normal aralıkta"}],
                       "sonuc": "Kerem'in baş çevresi referans değerlerine göre normal aralıkta, ortanın biraz üstünde. (s. 177–178)"},
             "soru": S("Referans değeri ne için kullanılır?", ["Grafiğe renk vermek için", "Araştırma sorusu yazmak için", "Bir ölçümü karşılaştırmak için"], 2,
                       "Bilgi kartındaki tanıma bak.", "Referans değeri, ölçümü karşılaştırmak için önceden belirlenmiş değerdir. (s. 177)")},
            {"ad": "Temsil Değeri", "renk": "#b7791f", "svg": svg3_temsil_deger(),
             "aciklama": "Bir veri setini tek bir sayıyla özetleyen değere temsil değeri denir. Genelde aritmetik ortalama, ortanca ya da tepe değerden biri seçilir.",
             "ek": "Hangisini seçtiğimizi gerekçesiyle söyleriz. Kitapta kar örtülü gün sayıları için bir temsil değeri seçilip gerekçesi yazılıyor. (s. 175)",
             "akilda": "Bütün veriyi tek sayıyla söyle",
             "cozum": {"baslik": "Kar verisinin ortalaması",
                       "problem": "Kar örtülü gün sayıları: 30,0 · 29,6 · 30,0 · 27,1 · 22,4. Aritmetik ortalamayı temsil değeri olarak seçelim.",
                       "adimlar": [
                           {"metin": "Bütün değerleri topla.", "islem": "30,0 + 29,6 + 30,0 + 27,1 + 22,4 = 139,1"},
                           {"metin": "5 değer var: toplamı 5'e böl.", "islem": "139,1 ÷ 5 = 27,82"},
                           {"metin": "Yuvarla.", "islem": "≈ 27,8 gün"}],
                       "sonuc": "Temsil değeri yaklaşık 27,8 gün. Gerekçe: Bütün dönemleri hesaba katan ortalamayı seçtik. (s. 175)"},
             "sende": {"baslik": "Sıra sende",
                       "problem": "Aynı veri setinde (30,0 · 29,6 · 30,0 · 27,1 · 22,4) tepe değeri ve ortancayı bul.",
                       "adimlar": [
                           {"metin": "En çok tekrar eden değer hangisi?",
                            "soru": G("Tepe değer kaçtır?", "30", "Hangi sayı iki kez yazılmış?", "30,0 iki kez var.", denk=True,
                                      yardim={"adimlar": ["Her sayının kaç kez yazıldığını say.", "En çok yazılanı seç."]}),
                            "islem": "Tepe değer = 30,0"},
                           {"metin": "Sırala: 22,4 · 27,1 · 29,6 · 30,0 · 30,0. Ortadaki hangisi?",
                            "soru": G("Ortanca kaçtır?", "29,6", "5 değer var; 3. sıradakine bak.", "Sıralı listede 3. değer 29,6.", denk=True,
                                      yardim={"adimlar": ["Sıralı listeye bak.", "5 değer var; 3. sıradakini bul."]}),
                            "islem": "Ortanca = 29,6"}],
                       "sonuc": "Harika! Üç ölçü de farklı: 27,8 · 29,6 · 30,0. Hangisini seçeceğimizi gerekçesiyle söyleriz."},
             "soru": S("Temsil değeri için hangisi doğrudur?", ["Veri setini tek bir sayıyla özetler.", "Her zaman en büyük veridir.", "Grafiğin başlığıdır."], 0,
                       "Bilgi kartındaki ilk cümleye bak.", "Temsil değeri, veri setini tek sayıyla özetler.")},
            {"ad": "Temsil Değeri Listede Olmayabilir", "renk": "#7b4fc9", "svg": svg3_yok(),
             "aciklama": "Temsil değeri veri setindeki sayılardan biri olmayabilir. Örneğin 27,8 kar verisi listesinde yoktur ama veriyi temsil eder. (s. 176)",
             "ek": "Kesikli bir veri seti sürekli bir sayıyla temsil edilebilir: gün sayısı kesiklidir, 27,8 ise ondalıktır. Temsil değeri, gerekçesi söylenerek ortalamaya yakın bir sayı da olabilir: “yaklaşık 28 gün” gibi. (s. 176)",
             "akilda": "Listede yoksa da olur",
             "soru": S("Kar verisinin ortalaması 27,8 tabloda yok. Bu bir sorun mu?", ["Evet, temsil değeri tabloda olmalı.", "Hayır, temsil değeri veri setinde olmayabilir.", "Evet, ortalama yanlış hesaplanmış."], 1,
                       "Bilgi kartındaki ilk cümleye bak.", "Temsil değeri veri setinde yer almayabilir. (s. 176)")},
            {"ad": "Veriyle İddiayı Sınama", "renk": "#c2255c", "svg": svg3_iddia(),
             "aciklama": "Biri bir iddiada bulunursa verileri toplar, ortalama, ortanca ve tepe değeri hesaplar ve iddiayla karşılaştırırız. (s. 176)",
             "ek": "Mühendis, motorla arabanın 1 litre benzinle en az 13 km gideceğini iddia ediyor. 10 deneme sürüşü: 11,7 · 10,0 · 13,0 · 10,5 · 12,5 · 10,5 · 9,0 · 13,5 · 14,0 · 15,0 km. (s. 176)",
             "akilda": "İddia + veri = karar",
             "cozum": {"baslik": "Mühendisin iddiası",
                       "problem": "İddia: “1 litre benzinle en az 13 km.” Verilere göre doğrulanıyor mu?",
                       "adimlar": [
                           {"metin": "Ortalama: 10 değeri topla, 10'a böl.", "islem": "119,7 ÷ 10 = 11,97 km"},
                           {"metin": "Ortanca: sırala (9,0 · 10,0 · 10,5 · 10,5 · 11,7 · 12,5 · 13,0 · 13,5 · 14,0 · 15,0). Ortadaki iki değerin ortalaması.", "islem": "(11,7 + 12,5) ÷ 2 = 12,1 km"},
                           {"metin": "Tepe değer: 10,5 iki kez tekrar ediyor.", "islem": "10,5 km"},
                           {"metin": "Üçünü de 13 ile karşılaştır.", "islem": "11,97 · 12,1 · 10,5 < 13"}],
                       "sonuc": "Üç ölçü de 13 km'den az: iddia bu verilerle doğrulanmıyor. (s. 176)"},
             "sende": {"baslik": "Sıra sende",
                       "problem": "Bir başka araba 5 deneme yaptı: 12, 14, 13, 15, 16 km. İddia yine “en az 13 km”.",
                       "adimlar": [
                           {"metin": "Ortalamayı bul.",
                            "soru": G("5 denemenin aritmetik ortalaması kaç km?", "14", "Topla, 5'e böl.", "12 + 14 + 13 + 15 + 16 = 70; 70 ÷ 5 = 14 km.", birim="km",
                                      yardim={"adimlar": ["Beş değeri topla.", "Toplamı 5'e böl."]}),
                            "islem": "Ortalama = 14 km"},
                           {"metin": "13 ile karşılaştır.",
                            "soru": S("Ortalamaya göre iddia için ne söylenebilir?", ["İddiayı destekliyor.", "İddiayı çürütüyor.", "Karşılaştırılamaz."], 0,
                                      "14 mü büyük, 13 mü?", "14 > 13: ortalama iddiayı destekliyor."),
                            "islem": "14 > 13 ✓"}],
                       "sonuc": "Harika! Bu araç için veriler iddiayı destekliyor."},
             "soru": S("Mühendisin verilerinde ortalama 11,97, ortanca 12,1 km. İddia “en az 13 km”. Hangisi doğrudur?",
                       ["İddia doğrulanmıştır.", "İddia bu verilerle doğrulanmaz.", "Veriler iddiayla ilgili değildir."], 1,
                       "İki ölçüyü 13 ile karşılaştır.", "11,97 ve 12,1, 13'ten küçük: iddia doğrulanmaz. (s. 176)")}
        ],
        "gruplar": [{"soru": "Ne işe yarar?", "kutular": [
            {"etiket": "Grafiği yorumlamak", "uyeler": ["Eğilim", "Veri Ötesi: Tahmin"]},
            {"etiket": "Tek sayıyla özetlemek", "uyeler": ["Temsil Değeri", "Temsil Değeri Listede Olmayabilir"]},
            {"etiket": "Karşılaştırıp karar vermek", "uyeler": ["Referans Değeri", "Veriyle İddiayı Sınama"]}]}],
        "akildaKalsin": [
            "Eğilim çizginin genel yönüdür; küçük iniş çıkışlara takılma.",
            "Eğilim devam ederse gelecekte ne olabileceğini tahmin ederiz; tahmin kesin değildir.",
            "Referans değeri, bir ölçümü karşılaştırmak için önceden belirlenmiş değerdir.",
            "Temsil değeri veri setini tek sayıyla özetler; veri setinde olmayabilir.",
            "Bir iddiayı sınamak için ortalama, ortanca ve tepe değeri iddiayla karşılaştır."],
        "merakKutusu": [
            {"soru": "Persentil ne demek?", "cevap": "Bir bebeğin ölçüsünün yaşıtlarına göre yerini gösterir. P75'teki bebek, yaşıtlarının %75'inden daha uzun ya da kilolu demektir. (s. 177)"},
            {"soru": "Kar örtülü gün sayısı neden önemli?", "cevap": "İklim verileri, tarım planlaması, su kaynaklarının yönetimi ve kış turizmi bu sayıya bakılarak planlanır. (s. 175)"},
            {"soru": "Ortalama ile ortanca neden farklı çıkar?", "cevap": "Ortalama bütün sayıları hesaba katar; çok küçük ya da çok büyük bir değer onu çeker. Ortanca sadece sıralamadaki ortaya bakar."},
            {"soru": "Gün sayısı kesikliyse 27,8 gün nasıl olur?", "cevap": "Gerçekte 27,8 gün yaşanmaz ama veriyi özetleyen sayı olarak kullanılabilir. Kesikli bir veri seti sürekli bir sayıyla temsil edilebilir. (s. 176)"},
            {"soru": "Esra Bayrak kimdir?", "cevap": "Uzun atlamada ülkemizi temsil eden millî paralimpik sporcumuzdur. Atlayış mesafeleri 2017'de 5,17 m, 2019'da 5,38 m. (s. 179)"},
            {"soru": "Bir tahmin yanlış çıkarsa?", "cevap": "Olabilir! Tahmin eğilime dayanır ama kesin değildir. Yeni veriler gelince tahmini güncelleriz."}],
        "dusunVeYaz": [{"soru": "Bir kayak merkezinde kayak okulu açacağını düşün. Kar örtülü gün sayısının azalma eğilimi sana ne söyler? Kararını nasıl etkiler?",
                        "ornekCevap": "Kar örtülü gün sayısı azalıyor; bu devam ederse kayak yapılabilecek gün sayısı azalabilir. Okulu açmadan önce o merkezin kendi verilerine bakardım ya da yapay kar gibi önlemleri düşünürdüm.",
                        "anahtarlar": ["azal", "eğilim", "devam", "tahmin", "karar"]}],
        "sorular": [
            S("Kar grafiğine göre ortalama kar örtülü gün sayısının genel eğilimi nedir?", ["Artış", "Azalış", "Hiç değişmemiş"], 1,
              "İlk ve son değere bak: 30,0 ve 22,4.", "Arada küçük bir çıkış olsa da genel yön aşağı: azalış. (s. 175)", svg=kar_svg(), kavram="Eğilim"),
            G("Kar grafiğine göre 2003–2013 ile 2014–2024 dönemleri arasında kar örtülü gün sayısı kaç gün azalmış?", "4,7", "Büyükten küçüğü çıkar: 27,1 − 22,4.",
              "27,1 − 22,4 = 4,7 gün.", denk=True, birim="gün", svg=kar_svg(), kavram="Eğilim",
              yardim={"adimlar": ["İki dönemin değerlerini oku: 27,1 ve 22,4.", "Büyükten küçüğü çıkar; virgülleri alt alta yaz."]}),
            S("Bir çiftçi son 10 yılda yağışın azaldığını gördü. Veri ötesini yorumlayarak hangi kararı verebilir?",
              ["Çok su isteyen ürün ekmek", "Kuraklığa dayanıklı ürün ekmek ya da damla sulama yaptırmak", "Verilere hiç bakmamak"], 1,
              "Yağış azalmaya devam ederse ne olur?", "Yağış azalırsa az su isteyen ürün ve damla sulama verimi artırır. (s. 174)", kavram="Veri Ötesi: Tahmin"),
            S("9 aylık bir bebeğin baş çevresi 44,9 cm. Referans değerlerine göre (P25 = 44,9 · P50 = 45,8 · P75 = 46,6) hangisi doğrudur?",
              ["P25 değerinde", "P50 değerinde", "P75'in üstünde"], 0,
              "44,9 hangi değere eşit?", "44,9 cm, 9 ayda P25 değerine eşit. (s. 177)", svg=persentil_svg(), kavram="Referans Değeri"),
            G("Esra Bayrak'ın 5 atlayışı (5,17 · 5,27 · 5,38 · 5,37 · 5,36) için ortanca kaç metredir?", "5,36", "Önce küçükten büyüğe sırala.",
              "Sıralı: 5,17 · 5,27 · 5,36 · 5,37 · 5,38. Ortadaki 5,36. (s. 179)", denk=True, birim="m", kavram="Temsil Değeri",
              yardim={"adimlar": ["Sayıları küçükten büyüğe sırala.", "5 sayı var: 3. sıradakini bul."]}),
            N("Bir sınıftaki öğrencilerin evcil hayvan sayıları: 0, 2, 1, 1, 3, 1, 0. Tepe değere sayı doğrusunda dokun.", 1, {"min": 0, "max": 3},
              "Hangi sayı en çok yazılmış?", "1 üç kez yazılmış: tepe değer 1.", kavram="Temsil Değeri",
              yardim={"adimlar": ["Her sayının kaç kez yazıldığını say.", "En çok yazılan sayıyı seç."]}),
            N("Veriler: 4, 1, 3, 2, 0. Ortancaya sayı doğrusunda dokun.", 2, {"min": 0, "max": 4},
              "Önce sırala: 0, 1, 2, 3, 4.", "Sıralı: 0, 1, 2, 3, 4. Ortadaki 2.", kavram="Temsil Değeri",
              yardim={"adimlar": ["Sayıları küçükten büyüğe sırala.", "Ortadaki sayıyı bul."]}),
            S("3, 4, 6, 7 verilerinin ortalaması 5'tir. Hangisi doğrudur?", ["5 veri setinde olmadığı için temsil değeri olamaz.", "Ortalama yanlış hesaplanmıştır.", "5 veri setinde olmasa da temsil değeri olabilir."], 2,
              "Temsil değeri veri setinde olmak zorunda mı?", "Temsil değeri veri setinde yer almayabilir: 5 bu veriyi temsil eder. (s. 176)", kavram="Temsil Değeri Listede Olmayabilir"),
            S("Bir pil üreticisi “Pillerimiz en az 10 saat dayanır.” diyor. 5 pilin süreleri: 11, 12, 10, 13, 9 saat. Ortalama 11 saat. Hangisi doğrudur?",
              ["İddia kesinlikle yanlıştır.", "Veriler iddiayla ilgili değildir.", "Ortalama iddiayı destekliyor ama 9 saatlik bir pil var; daha çok veri gerekebilir."], 2,
              "Ortalamayı 10 ile karşılaştır. Bütün piller 10 saat dayanmış mı?", "11 > 10: ortalama destekliyor. Ama 9 saatlik pil “en az 10” iddiasına uymuyor. (s. 176)", kavram="Veriyle İddiayı Sınama"),
            G("Mühendisin 10 deneme sürüşünden kaç tanesinde araba 13 km ya da daha fazla gitmiş? (11,7 · 10,0 · 13,0 · 10,5 · 12,5 · 10,5 · 9,0 · 13,5 · 14,0 · 15,0)", "4",
              "13'e eşit ya da 13'ten büyük olanları say.", "13,0 · 13,5 · 14,0 · 15,0: 4 deneme. 10 denemenin 6'sı 13 km'nin altında. (s. 176)", kavram="Veriyle İddiayı Sınama",
              yardim={"adimlar": ["Her değeri 13 ile karşılaştır.", "13'e eşit ya da büyük olanları işaretle.", "İşaretlediklerini say."]})]
    }


def u3t2():
    return {
        "id": "u3t2", "tur": "tarama", "unite": T3,
        "baslik": "Ara Durak 2: Grafik ve Temsil Değeri", "sayfalar": "Konu 4–5 · s. 171–179",
        "giris": "Grafik çizip yorumlamayı bitirdin, tebrikler! Kısa bir mola verip nokta ve çizgi grafiğini, eğilimi ve temsil değerini birlikte gözden geçireceğiz. Önce özetleri oku ve kartları çevir, sonra tarama testini çöz. Not yok.",
        "buyukResim": "Önce verileri resme çevirdik: tekrar eden veriler için nokta grafiği, zamanla değişen veriler için çizgi grafiği. Sonra grafiği yorumladık: eğilim, tahmin, referans değeri. En son veriyi tek bir sayıyla özetledik ve bir iddiayı verilerle sınadık.",
        "kapsar": ["u3k4", "u3k5"],
        "hatirla": [
            {"konu": "u3k4", "maddeler": [
                "Nokta grafiği: aynı değerler üst üste yığılır.",
                "Çizgi grafiği: zamanla değişim; yatayda zaman, dikeyde değer.",
                "Çizgi yukarı artış, aşağı azalış, düz sabit."]},
            {"konu": "u3k5", "maddeler": [
                "Eğilim genel yöndür; tahmin “… olabilir” diye yapılır.",
                "Temsil değeri: ortalama, ortanca ya da tepe değer; veri setinde olmayabilir.",
                "İddia, ölçülerle karşılaştırılarak sınanır."]}],
        "eskiSoru": 4,
        "oyunKavram": 8,
        "gruplar": [{"soru": "Hangisiyle ilgili?", "kutular": [
            {"etiket": "Grafik çizmek", "uyeler": ["Nokta Grafiği", "Çizgi Grafiği", "Hangi Grafik?"]},
            {"etiket": "Grafiği yorumlamak", "uyeler": ["Artış, Azalış, Sabit", "Eğilim", "Veri Ötesi: Tahmin"]},
            {"etiket": "Tek sayıyla özetlemek", "uyeler": ["Temsil Değeri", "Temsil Değeri Listede Olmayabilir"]}]}],
        "sorular": [
            S("Esra Bayrak'ın 2017–2021 atlayışlarını göstermek için hangi grafik uygundur ve eğilim nedir?",
              ["Nokta grafiği; azalış", "Çizgi grafiği; önce artış, sonra neredeyse sabit", "Çizgi grafiği; sürekli azalış"], 1,
              "Yıllara göre değişim mi gösteriliyor? Çizgi önce nereye, sonra nasıl gidiyor?",
              "Zamanla değişim çizgi grafiğiyle gösterilir. 5,17 → 5,38'e çıkıyor, sonra 5,37 ve 5,36: neredeyse sabit. (s. 179)",
              svg=atlama_svg(), kaynak=[K("u3k4", "Hangi Grafik?"), K("u3k5", "Eğilim")]),
            G("Grafiğe göre Esra Bayrak'ın atlayışı 2017'den 2019'a kaç metre artmış?", "0,21",
              "2019 değerinden 2017 değerini çıkar.", "5,38 − 5,17 = 0,21 m. (s. 179)", denk=True, birim="m", svg=atlama_svg(),
              kaynak=[K("u3k4", "Çizgi Grafiği"), K("u3k4", "Artış, Azalış, Sabit")],
              yardim={"adimlar": ["Başlangıç: 2017'deki değeri oku.", "Bitiş: 2019'daki değeri oku.", "Büyükten küçüğü çıkar; virgülleri alt alta yaz."]}),
            N("Nokta grafiğindeki kardeş sayılarının tepe değerine sayı doğrusunda dokun.", 1, {"min": 0, "max": 4},
              "Tepe değer en yüksek yığındır.", "1'in üstünde 5 nokta: tepe değer 1.", svg=kardes_svg(),
              kaynak=[K("u3k4", "Nokta Grafiği"), K("u3k5", "Temsil Değeri")],
              yardim={"adimlar": ["Tepe değer en çok tekrar eden değerdir.", "Nokta grafiğinde en yüksek yığını bul."]}),
            G("Bir fidanın 4 haftalık boyları çizgi grafiğinde: 6, 8, 11, 15 cm. Bu boyların aritmetik ortalaması kaç cm?", "10",
              "Dört değeri topla, 4'e böl.", "6 + 8 + 11 + 15 = 40; 40 ÷ 4 = 10 cm. 10 listede yok ama veriyi temsil eder.", birim="cm",
              svg=cizgi_svg(["1. hf", "2. hf", "3. hf", "4. hf"], [([6, 8, 11, 15], "#8ce99a")], 4, 16, 2, baslik="Fidanın boyu (cm)"),
              kaynak=[K("u3k4", "Çizgi Grafiği"), K("u3k5", "Temsil Değeri Listede Olmayabilir")],
              yardim={"adimlar": ["Grafikten dört değeri oku.", "Hepsini topla.", "Toplamı veri sayısına böl."]}),
            S("Kar örtülü gün sayısı azalma eğiliminde. Kayak okulu açmak isteyen Furkan için en uygun düşünce hangisi?",
              ["Grafik her yıl artacağını gösteriyor.", "Grafiklerin karar vermeye bir faydası yoktur.", "Azalma devam edebilir; karar vermeden önce başka araştırma soruları da sormalıyım."], 2,
              "Eğilim nereye gidiyor? Tahmin kesin mi?", "Eğilim azalış; devam edebilir. Karar için başka sorular da gerekir. (s. 175)",
              svg=kar_svg(), kaynak=[K("u3k4", "Artış, Azalış, Sabit"), K("u3k5", "Veri Ötesi: Tahmin")]),
            S("3 aylık bir bebeğin baş çevresi 40,5 cm. Grafikte 3. ayda P25 = 40,2 ve P50 = 41,1. Hangisi doğrudur?",
              ["P25 ile P50 arasında, normal aralıkta", "P25'in altında", "P75'in üstünde"], 0,
              "40,5'i 40,2 ve 41,1 ile karşılaştır.", "40,2 < 40,5 < 41,1: P25 ile P50 arasında. (s. 177)", svg=persentil_svg(),
              kaynak=[K("u3k4", "Çizgi Grafiği"), K("u3k5", "Referans Değeri")]),
            S("Atlayışların ortalaması 5,31 m. Bu sayı tabloda yok. Hangisi doğrudur?",
              ["Ortalama tabloda olmadığı için temsil değeri olamaz.", "Ortalama en büyük değere eşit olmalıdır.", "Temsil değeri veri setinde olmayabilir; 5,31 veriyi temsil eder."], 2,
              "Temsil değeri veri setinde olmak zorunda mı?", "Temsil değeri veri setinde yer almayabilir. (s. 176)", svg=atlama_svg(),
              kaynak=[K("u3k5", "Temsil Değeri Listede Olmayabilir"), K("u3k4", "Çizgi Grafiği")])]
    }


TARAMALAR = [u1t1, u1t2, u1t3, u1t4, u1t5, u2t1, u2t2, u2t3, u2t4, u3t1, u3t2]
KONULAR = [u1k1, u1k2, u1k3, u1k4, u1k5, u1k6, u1k7, u1k8, u1k9, u1k10, u1k11, u1k12, u2k1, u2k2, u2k3, u2k4, u2k5, u2k6, u2k7, u2k8,
           u3k1, u3k2, u3k3, u3k4, u3k5] + TARAMALAR

# =================================================================
# İpucu verisi. Motor her soruda "İpucu" düğmesi gösterir; açılınca önce bağlı kavramı hatırlatır,
# sonra "yardim.adimlar" adımlarını tek tek açar (yoksa "ipucu"yu). Cevabı söyleme; son adım cevaba bir adım kala dursun.
# TEST_KAVRAM: test sorularının sırasıyla bağlı olduğu kavram (None: bağlantı yok).
# YARDIM: soru metninin başıyla eşleşir (kavram sorusu, test ya da tarama sorusu); {"adimlar": [...], "hatirla"?: "kavram yerine özel hatırlatma"}.
TEST_KAVRAM = {
    "u1k1": ["Negatif Tam Sayılar", "Negatif Tam Sayılar", "Sayı Doğrusu", "Kelimeden Sayıya", "Tam Sayılar Ailesi",
             "Sayı Doğrusu", "Tam Sayılar Ailesi", "İki Sayı Arasındaki Uzaklık", "Pozitif Tam Sayılar", "Kelimeden Sayıya"],
    "u1k2": ["Aradaki Sayılar", "Sayı Doğrusunda Gösterme", "Payda Sıfır Olamaz", None, "Sayı Aileleri", "Sayı Aileleri",
             "Sayı Doğrusunda Gösterme", "Eksi Bütüne Aittir", "Eksi Bütüne Aittir", "Eksinin Yeri", None, "Sayı Doğrusunda Gösterme"],
    "u1k3": ["Mutlak Değer", "Eksik ya da Fazla", "Mutlak Değeri Verilen Sayı", None, "Mutlak Değer Eksi Olmaz", "Mutlak Değeri Verilen Sayı",
             "Eksi de Artı da Aynı", "Eksik ya da Fazla", "Mutlak Değeri Verilen Sayı", "Mutlak Değer", "Mutlak Değer", "Başlangıç Noktası"],
    "u1k4": ["Kesir Çizgisi Bölmedir", "Paydayı 10, 100, 1000 Yap", "Sonlu mu, Devirli mi?", "Devirli Ondalık Gösterim", "Ondalıktan Kesre", "Ondalıktan Kesre",
             "Sonlu mu, Devirli mi?", "Paydayı 10, 100, 1000 Yap", "Devirliden Kesre", "Devirli Ondalık Gösterim", "Ondalıktan Kesre", "Sonlu Ondalık Gösterim"],
    "u1k5": ["Sağdaki Büyüktür", "Sağdaki Büyüktür", "Negatif, Sıfır, Pozitif", "Negatiflerde Uzak Olan Küçük", "Negatiflerde Uzak Olan Küçük", "Sağdaki Büyüktür",
             "Paydaları ya da Payları Eşitle", "Sağdaki Büyüktür", "Arada Hep Bir Sayı Var", "Arada Hep Bir Sayı Var", "Dikey Sayı Doğrusu", "Kısa Yollar"],
    "u1k6": ["Farklı İşaret: Çıkar, Büyüğün İşareti", "Aynı İşaret: Topla, İşareti Koru", "Toplama Bir Yolculuktur", "Ters İşaretliler Toplanınca 0", "Çıkarma = Tersiyle Toplama",
             "Toplama Bir Yolculuktur", "Önce Mutlak Değer", "Aradaki Eksi Çıkarmadır", "Toplama Bir Yolculuktur", "Çıkarma = Tersiyle Toplama"],
    "u1k7": ["Farklı İşaret: Çarpım Eksi", "Aynı İşaret: Çarpım Artı", "Çarpma = Tekrarlı Toplama", "Bölmede Aynı Kural", "Bölmede Aynı Kural",
             "Çok Çarpanda Eksileri Say", "Çarp mı, Böl mü?", "Bölmenin Farklı Yazılışları", "Çok Çarpanda Eksileri Say", "Çarp mı, Böl mü?"],
    "u1k8": ["Payda Aynıysa Payları Topla", "Önce Paydaları Eşitle", "Önce Paydaları Eşitle", "Çıkarma = Tersini Ekle", "Çıkarma = Tersini Ekle",
             "Tam Sayılı Kesirler", "Toplamanın Özellikleri", "Problemde Toplama ve Çıkarma", "Problemde Toplama ve Çıkarma", "Toplamanın Özellikleri"],
    "u1k9": ["İşaret Tam Sayılardaki Gibi", "Önce Çapraz Sadeleştir", "İşaret Tam Sayılardaki Gibi", "Pay Paya, Payda Paydaya", "Tam Sayılı Kesri Önce Çevir",
             "Bir Sayının Kesrini Bulma", "Çarpmanın Özellikleri", "İşaret Tam Sayılardaki Gibi", "Bir Sayının Kesrini Bulma", "Çarpmanın Özellikleri"],
    "u1k10": ["Tekrarlı Çarpımı Kısalt", "Taban, Üs ve Değer", "Taban, Üs ve Değer", "Kesrin Kuvveti", "Eksi Taban: Çift Artı, Tek Eksi",
              "Eksi Taban: Çift Artı, Tek Eksi", "Özel Tabanlar: 1, 0 ve Üs 1", "Parantez Fark Yaratır", "Eksi Taban: Çift Artı, Tek Eksi", "Tekrarlı Çarpımı Kısalt"],
    "u1k11": ["Böl = Tersiyle Çarp", "Böl = Tersiyle Çarp", "Tam Sayılı Kesir ve İşaret", "Tam Sayılı Kesir ve İşaret", "Tam Sayılı Kesir ve İşaret",
              "Kaç Tane Sığar?", "Paydalar Eşitse Payları Böl", "Kesir Çizgisi de Bölmedir", "Böl = Tersiyle Çarp", "Ters Çevir", "Kaç Tane Sığar?"],
    "u1k12": ["İşlem Sırası", "Önce Parantez", "İşlem Sırası", "İşlem Sırası", "Aynı Öncelikte Soldan Sağa", "Kesir Çizgisi Ayırır",
              "Problemi İşleme Çevir", "Problemi İşleme Çevir", "Önce Parantez", "Problemi İşleme Çevir", "Çok Adımlı İşlem"],
}
YARDIM = {
    "u1k1": {
        f"Sayı doğrusunda {M}1 ile +4": {"adimlar": [
            "Yol 0'dan geçiyor. Yolu iki parçaya böl.", f"{M}1'den 0'a kaç aralık var? Say.", "0'dan +4'e kaç aralık var? Say.", "İki parçayı topla."]},
        "Bir denizaltı deniz seviyesinin 35": {"adimlar": [
            "Başlangıç (0) nerede? Deniz seviyesi.", "\"Altında\" hangi işaret? Altı, borç, gider, zarar → eksi.", "Kaç birim? Cümledeki sayıya bak.", f"Önce {M} tuşuna, sonra sayılara dokun."]},
        "A noktası hangi tam sayıyı": {"adimlar": [
            "A, 0'ın solunda mı, sağında mı? Solundaysa sayı eksidir.", "0'dan A'ya kadar aralıkları tek tek say.", "İşareti ve saydığın sayıyı birlikte yaz."]},
        f"Bir binada otopark {M}2": {"adimlar": [
            "Zemin kat 0'dır. Otopark 0'ın altında, Elif'in katı üstünde.", "Otoparktan zemin kata kaç kat çıkılır?", "Zemin kattan Elif'in katına kaç kat çıkılır?", "İki parçayı topla."]},
        "Mert'in kartında hafta başında": {"adimlar": [
            "Kartta 300 TL var. 300 TL harcayınca kartta kaç TL kalır?", "Harcadığı 400 TL'nin kaç TL'si daha ödenecek? 400 − 300 = ?", "Kalan kısım borç olur. Borç hangi işaretle yazılır?"]},
    },
    "u1k2": {
        "[[12/16]] kesrinin en sade": {
            "hatirla": "Sadeleştirmek, pay ve paydayı aynı sayıya bölmektir. Kesrin değeri değişmez. Pay ve payda artık birlikte bölünemiyorsa kesir en sade hâlindedir.",
            "adimlar": ["12 ve 16'yı birlikte bölen bir sayı bul: 2 mi, 4 mü?", "En büyüğünü seçersen tek seferde biter.", "Payı da paydayı da o sayıya böl.", "Önce payı, sonra / tuşunu, sonra paydayı yaz."]},
        "[[20/5]] hangi tam": {"adimlar": [
            "Kesir çizgisi bölme demektir: [[20/5]] = 20 ÷ 5.", "5'er 5'er say: 5, 10, 15, 20… Kaç kere saydın?"]},
        "[[-1 2/3]] sayısını bileşik": {"adimlar": [
            "Eksiyi kenara koy. Şimdilik [[1 2/3]] ile çalış.", "Tam kısmı payda ile çarp: 1 × 3.", "Çıkan sayıya payı ekle. Bu yeni pay olur; payda 3 kalır.",
            f"Eksiyi geri ekle: önce {M} tuşuna, sonra pay, / ve payda."]},
        "A noktası hangi rasyonel": {"adimlar": [
            "A, 0'ın solunda: sayı eksi.", "A hangi iki tam sayı arasında? Bir birim kaç küçük parçaya bölünmüş?",
            f"{M}2'den sola kaç küçük parça gidilmiş? Önce tam sayılı kesir olarak düşün.", "Tam sayılı kesri bileşik kesre çevir: tam × payda + pay. Eksiyi unutma."]},
        "Bir su sayacının göstergesinde": {
            "hatirla": "Denk kesirler aynı miktarı gösterir: [[2/4]] ile [[1/2]] sayı doğrusunda aynı yerdedir. Sadeleştirmek için pay ve paydayı aynı sayıya böleriz.",
            "adimlar": ["Önce kesri yaz: 4 eş bölmeden kaçı dolu?", "Pay ve paydayı aynı sayıya bölerek sadeleştir."]},
    },
    "u1k3": {
        "Hedef 200 gram. 199": {"adimlar": [
            "Başlangıç noktası 200 gram.", "199'dan 200'e kaç gram var? Say.", "Eksik ya da fazla olması fark etmez; sadece kaç gram uzak?"]},
        f"|{M}7| kaçtır": {"adimlar": [
            f"|{M}7|, {M}7'nin 0'a uzaklığı demek.", f"Sayı doğrusunda {M}7'den 0'a kaç aralık var? Say.", "Uzaklık eksi olmaz."]},
        f"|{M}8| kaçtır": {"adimlar": [
            f"|{M}8|, {M}8'in 0'a uzaklığıdır.", f"{M}8 ile 0 arasındaki aralıkları say. Ya da kısa yol: işareti sil.", f"Uzaklık eksi olmaz; cevabın önüne {M} koyma."]},
        "Bir sondaj makinesi yer yüzeyinin": {
            "hatirla": "Başlangıç (0) yer yüzeyidir. Yüzeyin altı eksi, üstü artı ile yazılır.",
            "adimlar": ["Başlangıç (0): yer yüzeyi.", "Makine aşağı indi. \"Altında\" hangi işaret?", f"Önce {M} tuşuna dokun, sonra 8, virgül ve 6."]},
        "Sondaj makinesinin konumu": {"adimlar": [
            f"Uzaklık mutlak değerdir: |{M}8,6|.", "İşareti sil, sayı kalır.", "Virgül tuşunu kullanmayı unutma."]},
        "|[[-3/4]]| kaçtır": {"adimlar": [
            "Mutlak değer hiç eksi olmaz.", "İşareti silince geriye hangi kesir kalıyor?", "Kesri yazmak için önce pay, sonra / tuşu, sonra payda."]},
        "UME'ye göre saat 14.00": {"adimlar": [
            "Başlangıç noktası doğru saat: 14.00.", "Kol saati 14.05'i gösteriyor. 14.00'ten 14.05'e kaç dakika var?", "İleri ya da geri olması fark etmez; sadece kaç dakika?"]},
        "Bir çay fabrikasında hedef 500": {"adimlar": [
            "Başlangıç noktası: hedef 500 gram.", "496'dan 500'e kaç gram var? 497, 498, 499, 500 diye say.", "Eksik olması fark etmez; sadece kaç gram uzak?"]},
    },
    "u1k4": {
        "[[3/5]] kesrini ondalık": {"adimlar": [
            "Paydayı 10 yapabilir misin? 5 × ? = 10.", "Payı da aynı sayıyla çarp.", "Payda 10 ise virgülden sonra 1 basamak olur. Önce 0, sonra virgül."]},
        "Termostaki kahve 0,7": {"adimlar": [
            "Virgülden sonra kaç basamak var?", "1 basamak varsa payda 10 olur.", "Virgülü sil, sayıyı paya yaz. Önce pay, sonra / tuşu, sonra payda."]},
        "[[9/25]] kesrini ondalık": {"adimlar": [
            "Paydayı 100 yap: 25 × ? = 100. 25'er 25'er say.", "Payı da aynı sayıyla çarp: 9 × 4 = ?", "Payda 100: virgülden sonra 2 basamak. Önce 0, sonra virgül."]},
        "Bir öğrencinin boyu 1,32": {"adimlar": [
            "Virgülden sonra kaç basamak var? 3 ve 2.", "2 basamak varsa payda 100 olur.", "Virgülü sil: 1,32 → 132. Bu sayı paya yazılır."]},
        "Bilardoda Ahmet ikinci": {
            "hatirla": "Paydayı 10, 100 ya da 1000 yapabiliyorsak ondalık gösterimi bulmak kolaydır. Payda 1000 ise virgülden sonra 3 basamak olur.",
            "adimlar": ["Önce oranı kesirle yaz: 8 topun 3'ü.", "8'i 10 ya da 100 yapamazsın ama 1000 yapabilirsin: 8 × 125 = 1000.",
                        "Payı da 125 ile çarp: 3 × 125 = 375.", "Payda 1000: virgülden sonra 3 basamak."]},
        "Hava sıcaklığı " + M + "14,2": {"adimlar": [
            "Virgülden sonra kaç basamak var? Payda kaç olur?", "Virgülü sil: 14,2 → 142.", f"Eksi işaretini unutma: önce {M} tuşu, sonra pay, / ve payda."]},
        "Hangisinin ondalık gösterimi devirlidir": {"adimlar": [
            "Her kesrin paydasına bak: 8, 9, 10.", "Paydayı 2'ye ve 5'e bölebildiğin kadar böl.", "Geriye 1 kalan sonludur. Geriye başka sayı kalan hangisi?"]},
    },
    "u1k5": {
        "İki takımın puanı eşit": {
            "hatirla": "Sayı doğrusunda sağdaki sayı büyüktür. Averajı büyük olan takım üstte yer alır.",
            "adimlar": ["B, A'nın üstünde: B'nin averajı A'nınkinden büyük olmalı.", f"Sayı doğrusunda {M}2'yi bul. Ondan büyük sayılar sağında.", f"{M}2'nin hemen sağındaki tam sayı hangisi?"]},
        "[[-7/3]] sayısından küçük": {"adimlar": [
            "Eksiyi kenara koy: 7 ÷ 3 = 2, kalan 1. Yani [[-7/3]] = [[-2 1/3]].", f"[[-2 1/3]] hangi iki tam sayı arasında? {M}2 ile …",
            "Küçük olan solda. [[-7/3]]'ün solundaki ilk tam sayı hangisi?", f"Eksiyi unutma: önce {M} tuşu."]},
        "Paydası 10 olan ve": {"adimlar": [
            "[[2/5]] kesrini paydası 10 olacak şekilde genişlet: 5 × 2 = 10.", "[[3/5]] kesrini de genişlet.", "Paylar arasındaki sayıyı bul ve paydasını 10 yaz."]},
        "Kitaptaki basketbolcular": {"adimlar": [
            "Payları eşitle: 5, 3 ve 2'nin hepsi 30'a genişletilebilir.", "[[5/12]] = [[30/72]], [[3/8]] = [[30/80]], [[2/6]] = [[30/90]].", "Paylar eşitse paydası küçük olan büyüktür."]},
    },
    "u1t1": {
        "Bir dalgıç deniz seviyesinin 12": {"adimlar": [
            f"Deniz seviyesi 0. Dalgıç altında ({M}12), martı üstünde (+5).", "Dalgıçtan deniz seviyesine kaç metre?", "Deniz seviyesinden martıya kaç metre?", "İki parçayı topla."]},
        "Meryem'in aklındaki": {"adimlar": [
            f"Mutlak değeri 3 olan sayılar: 3 ve {M}3. Mutlak değeri 2 olanlar: 2 ve {M}2.",
            f"En uzak olmaları için biri 0'ın solunda, biri sağında olmalı: {M}3 ile +2 gibi.", f"{M}3'ten 0'a kaç birim? 0'dan +2'ye kaç birim? Topla."]},
    },
    "u1t2": {
        "Üç şehirde sıcaklıklar": {"adimlar": [
            "Önce hepsini aynı gösterime getir: [[-7/4]]'ün paydasını 100 yap (4 × 25 = 100).",
            f"[[-175/100]] ondalık olarak kaçtır? Virgülden sonra 2 basamak.",
            f"Üç sayı da negatif. Eksilerde 0'a en uzak olan en küçüktür, yani en soğuktur.",
            "Tam kısımlar eşit (1). Virgülden sonraki basamaklara bak: hangisi en büyük?"]},
        "İki dalgıç deniz seviyesinin": {"adimlar": [
            "Deniz seviyesi 0. İki dalgıç da altında, ikisi de eksi.",
            "[[-12/5]]'in paydasını 10 yap (5 × 2 = 10). Kaç onda kaç olur?",
            f"Şimdi {M}2,35 ile karşılaştır. Daha derin olan 0'a daha uzak olandır.",
            "İkisinin tam kısmı 2. Onda birler basamağına bak."]},
    },
    "u1t3": {
        "Sabah hava sıcaklığı +5": {"adimlar": [
            "Başlangıç: +5 °C.", f"Yön: düşüş eksidir. Her saat {M}3.",
            f"Kaç birim? 4 saatte toplam değişim 4 · ({M}3). İşaretler farklı → eksi.",
            "+5 ile bu değişimi topla: işaretler farklı, büyükten küçüğü çıkar, büyüğün işaretini koy."]},
        "Deniz'in ulaşım kartında": {"adimlar": [
            "Başlangıç: kartta +20 TL.", f"Yön: gider eksidir. Her biniş {M}8 TL.",
            f"Kaç birim? 4 binişte toplam gider 4 · ({M}8).",
            f"+20 ile bu gideri topla. Hangisinin mutlak değeri büyük? Sonuç eksiyse önce {M} tuşuna dokun."]},
        "Asansör zemin katta": {"adimlar": [
            "Başlangıç (0): zemin kat.", f"Yön: aşağı eksi. 4 durakta 4 · ({M}2) kat iner.",
            "Oradan 3 kat yukarı (artı) çık: sayı doğrusunda 3 aralık yukarı say."]},
        "Bir dondurucunun sıcaklığı": {"adimlar": [
            "İlk sıcaklık +4 °C, son sıcaklık −16 °C.", f"Toplam değişim = son − ilk: ({M}16) {M} (+4). Çıkarmayı tersiyle toplamaya çevir.",
            "Bu değişim 5 saate eşit paylaşıldı: böl. Farklı işaret → eksi."]},
    },
    "u1t4": {
        "Bir sürahide [[3/4]] litre": {"adimlar": [
            "Başlangıç: sürahide [[3/4]] litre su.", "Yön: içilen su azalır, yani çıkaracağız.",
            "Kaç birim? İçilen su [[3/4]]'ün [[1/3]]'ü: bir sayının kesri için çarp. Önce çapraz sadeleştir.",
            "Paydalar aynı mı? [[3/4]]'ten içilen suyu çıkar ve sadeleştir."]},
        "Bir şişede [[3/4]] litre": {"adimlar": [
            "[[1 1/2]]'yi önce bileşik kesre çevir: 1 × 2 + 1.", "Paydaları 4'te eşitle ve iki şişeyi topla.",
            "Kaç bardak? Toplamı [[1/4]]'e böl: birinciyi koru, ikinciyi ters çevir, çarp."]},
        "Bir dalgıç deniz seviyesinin [[1 1/2]]": {"adimlar": [
            f"Başlangıç (0): deniz seviyesi. Dalgıç altında: {M}[[1 1/2]] = [[-3/2]].",
            "Yön: aşağı iniyor, eksi.", "Kaç birim? [[3/2]]'nin yarısı: [[3/2]] · [[1/2]].",
            f"[[-3/2]]'yi paydası 4 olacak şekilde genişlet ve inilen yolu ekle. Önce {M} tuşu, sonra pay, / ve payda."]},
    },
    "u1k6": {
        f"({M}12) + (+16) kaçtır": {"adimlar": [
            "İşaretlere bak: biri eksi, biri artı. Farklı işaret.", "Mutlak değerleri yaz: 12 ve 16. Büyükten küçüğü çıkar.", "Hangisinin mutlak değeri büyük? Onun işaretini koy."]},
        f"|{M}3| + ({M}8) kaçtır": {"adimlar": [
            f"Önce |{M}3| kaç? İşareti sil.", f"Şimdi (+3) + ({M}8) işlemini yap. İşaretler farklı.", "8'den 3'ü çıkar. Büyük olan hangisi, işareti ne?"]},
        f"4 {M} ({M}5) kaçtır": {"adimlar": [
            "Çıkarmayı toplamaya çevir: çıkan sayının işaretini ters yap.", f"4 {M} ({M}5) = 4 + (?)", "İşaretler aynı: topla."]},
        "Bir oyunda Alperen": {"adimlar": [
            "Başlangıç (0): oyunun başı. Kaybetmek eksi, kazanmak artı.", f"İşlemi yaz: ({M}3) + (+8).", "İşaretler farklı: 8'den 3'ü çıkar. Büyük olanın işaretini koy."]},
        f"(+5) {M} (+25) kaçtır": {"adimlar": [
            f"Çıkarmayı toplamaya çevir: (+5) + ({M}25).", "İşaretler farklı: 25'ten 5'i çıkar.", "Mutlak değeri büyük olan hangisi? Onun işaretini koy."]},
        f"|{M}5| + |{M}9| kaçtır": {"adimlar": [
            f"Önce |{M}5| kaç?", f"Sonra |{M}9| kaç?", "İki sonucu topla."]},
        "Bir havucun yaprak ucu": {"adimlar": [
            f"Başlangıç (0): toprak seviyesi. Üstü artı, altı eksi: yaprak +18, kök {M}12.", f"Fark için büyükten küçüğü çıkar: (+18) {M} ({M}12).", "Çıkarmayı toplamaya çevir ve topla."]},
    },
    "u1k7": {
        f"2 · ({M}5) kaçtır": {"adimlar": [
            f"2 · ({M}5), 2 tane ({M}5) demek.", f"({M}5) + ({M}5) işlemini yap: aynı işaret, topla, eksiyi koru."]},
        f"({M}72) ÷ ({M}9) kaçtır": {"adimlar": [
            "Önce işaretsiz böl: 72 ÷ 9. 9 kaç kere 72 eder?", "İşaretler aynı mı, farklı mı?", "Aynı işaret → artı."]},
        f"(+4) · ({M}10) kaçtır": {"adimlar": [
            "Önce işaretsiz çarp: 4 · 10.", "İşaretler aynı mı, farklı mı?", f"Farklı işaret → eksi. Önce {M} tuşuna dokun."]},
        f"({M}144) ÷ ({M}12) kaçtır": {"adimlar": [
            "Önce işaretsiz böl: 144 ÷ 12. 12 kaç kere 144 eder? 12 · 10 = 120, kalan 24.", "İşaretler aynı mı?", "Aynı işaret → artı."]},
        "Bir apartmanda iki kat arası": {"adimlar": [
            f"Başlangıç (0): giriş katı. Aşağı eksi: {M}18 m.", "Her kat 3 m. Kaç kat? Bu bir paylaştırma: böl.", f"({M}18) ÷ 3: önce 18 ÷ 3, sonra işaret."]},
        "Bir dağcı her 100 m": {"adimlar": [
            "Kaç kere 100 m çıktı? 400 ÷ 100.", f"Her seferinde sıcaklık {M}1 °C değişiyor.", f"Kaç kere · ({M}1): işaretler farklı → eksi."]},
    },
    "u1k8": {
        "[[1/2]] + ([[-1/4]]) kaçtır": {"adimlar": [
            "Paydalar 2 ve 4. 2'yi 4 yapmak için 2 ile genişlet.", "[[1/2]] kaç dörtte kaç olur? Payı da 2 ile çarp.", "Payları topla: (+2) + (−1). Payda 4 kalır."]},
        "([[-1 1/3]]) + ([[-2/3]]) kaçtır": {"adimlar": [
            "[[-1 1/3]] kesrini bileşik kesre çevir: 1 · 3 + 1. Eksi kalır.", "Paydalar aynı: payları topla. İkisi de eksi: aynı işaret.", "Çıkan kesri tam sayıya çevir: payı paydaya böl."]},
        "([[-1/6]]) + ([[-1/3]]) kaçtır": {"adimlar": [
            "Paydalar 6 ve 3. 3'ü 6 yapmak için 2 ile genişlet.", "[[-1/3]] kaç altıda kaç olur?", "Payları topla: iki eksi, aynı işaret. Payda 6 kalır."]},
        "[[9/2]] − [[10/2]] kaçtır": {"adimlar": [
            "Çıkarmayı çevir: [[9/2]] + ([[-10/2]]).", "Paydalar aynı. Payları topla: (+9) + (−10).", "Payda 2 kalır. Sonuç eksiyse önce − tuşuna dokun."]},
        "Bir dalgıç deniz seviyesinin": {"adimlar": [
            "Başlangıç (0): deniz seviyesi. Altı eksi: [[-5/2]].", "Yön: yukarı, artı: + [[3/4]].", "Paydaları 4'te eşitle: [[-5/2]] = [[-10/4]].", "Payları topla: (−10) + (+3). Payda 4 kalır."]},
    },
    "u1k9": {
        "[[3/4]] · [[5/7]] kaçtır": {"adimlar": [
            "Sadeleşen var mı? Üstteki 3, 5 ile alttaki 4, 7 arasında ortak bölen yok.", "Payları çarp: 3 · 5.", "Paydaları çarp: 4 · 7."]},
        "[[5/12]] · [[6/25]] kaçtır": {"adimlar": [
            "Çapraz bak: üstteki 5 ile alttaki 25'i 5 böler.", "Üstteki 6 ile alttaki 12'yi 6 böler.", "Küçülen sayıları çarp: pay payla, payda paydayla."]},
        "Bir sınıfta 30 öğrenci": {"adimlar": [
            "'i demek çarp: 30 · [[2/5]].", "Çapraz sadeleştir: 30 ile 5'i 5 böler.", "Küçülen sayıları çarp."]},
        "([[-2/3]]) · ([[-3/4]]) kaçtır": {"adimlar": [
            "Önce işaret: eksi · eksi → aynı işaret.", "Çapraz sadeleştir: üstteki 3 ile alttaki 3; üstteki 2 ile alttaki 4.", "Küçülen sayıları çarp."]},
        "Yiğit 600 TL": {"adimlar": [
            "Başlangıç: 600 TL. Harcamak eksidir: 600 · ([[-1/4]]).", "600'ün dörtte biri: 600 ÷ 4.", "İşareti unutma: önce − tuşu."]},
        "Bir halının alanı 12": {"adimlar": [
            "Ne isteniyor? Süpürülmeyen kısım.", "Süpürülen kısım: 12 · [[3/4]]. 12 ile 4'ü sadeleştir.", "Halının tamamından süpürülen kısmı çıkar."]},
        "24 · ([[3/8]] + [[1/3]]) kaçtır": {"adimlar": [
            "Dağılma özelliği: 24 · [[3/8]] + 24 · [[1/3]].", "24 · [[3/8]]: 24 ile 8'i sadeleştir.", "24 · [[1/3]]: 24 ile 3'ü sadeleştir.", "İki sonucu topla."]},
    },    "u1k10": {
        "2[[u:5]] kaçtır": {"adimlar": [
            "Taban 2, üs 5: 2 sayısını 5 kere yaz ve çarp.", "İkişer ikişer çarp: 2 · 2 = 4.", "Çıkan sayıyı her seferinde 2 ile çarp, toplam 5 tane 2 olana kadar."]},
        "([[1/2]])[[u:3]] kaçtır": {"adimlar": [
            "[[1/2]]'yi 3 kere çarp: [[1/2]] · [[1/2]] · [[1/2]].", "Payları çarp: 1 · 1 · 1.", "Paydaları çarp: 2 · 2 · 2. Önce pay, sonra / tuşu, sonra payda."]},
        f"({M}2)[[u:3]] kaçtır": {"adimlar": [
            "Önce işaret: üs 3. 3 tek mi, çift mi?", "Tek üs → sonuç eksi. Sayı doğrusunda 0'ın solunda.", "İşaretsiz değer: 2 · 2 · 2."]},
        "4[[u:3]] kaçtır": {"adimlar": [
            "Taban 4, üs 3: 4 · 4 · 4.", "Önce 4 · 4.", "Çıkan sayıyı 4 ile çarp."]},
        "([[2/3]])[[u:2]] kaçtır": {"adimlar": [
            "[[2/3]] · [[2/3]] demek.", "Payları çarp: 2 · 2.", "Paydaları çarp: 3 · 3. Önce pay, sonra / tuşu, sonra payda."]},
        f"{M}2[[u:4]] kaçtır": {"adimlar": [
            "Parantez var mı? Yok. Üs sadece 2'ye ait.", "Önce 2[[u:4]]: 2 · 2 · 2 · 2.", f"Eksi işareti en sonda başa gelir: önce {M} tuşu."]},
        "([[-1/2]])[[u:2]] kaçtır": {"adimlar": [
            "Önce işaret: üs 2 çift → artı. 0'ın sağında.", "Pay 1 · 1, payda 2 · 2.", "Sayı doğrusunda 0 ile 1 arası 4 parçaya bölünmüş. Kaçıncı çizgi?"]},
        "Bir bakteri her 30 dakikada": {"adimlar": [
            "3 saat = 180 dakika. 30 dakikalık kaç parça var? 180 ÷ 30.", "Her parçada bakteri sayısı 2 ile çarpılır: 6 parça → 2[[u:6]].", "2'yi 6 kere çarp: 2, 4, 8, … diye ikiye katla."]},
    },
    "u1k11": {
        "[[-4/9]] sayısının çarpma": {"adimlar": [
            "Pay ile paydanın yerini değiştir: üstteki 4 alta, alttaki 9 üste.", "İşaret değişmez: eksi kalır.", "Önce − tuşu, sonra pay, / ve payda."]},
        "[[3/5]] ÷ [[9/10]] kaçtır": {"adimlar": [
            "Koru: [[3/5]]. Çevir: ÷ yerine ·. Ters çevir: [[9/10]] → [[10/9]].", "Çapraz sadeleştir: üstteki 3 ile alttaki 9; üstteki 10 ile alttaki 5.", "Küçülen sayıları çarp: pay payla, payda paydayla."]},
        "[[9/8]] ÷ [[1/3]] kaçtır": {"adimlar": [
            "Koru, çevir, ters çevir: [[1/3]]'ün tersi 3.", "[[9/8]] · 3: 3'ü [[3/1]] gibi düşün.", "Payları çarp: 9 · 3. Payda 8 kalır."]},
        "Bir elektrik ustası [[3/4]]": {"adimlar": [
            "Ne isteniyor? Parça sayısı: [[3/4]]'ün içinde kaç tane [[1/8]] sığar?", "Bölmeyi çarpmaya çevir: [[3/4]] · [[8/1]].", "Çapraz sadeleştir: 4 ile 8'i 4 böler. Sonra çarp."]},
        "Esra'nın 5 m": {"adimlar": [
            "Ne isteniyor? 5 m'nin içinde kaç tane [[5/4]] m sığar?", "Koru, çevir, ters çevir: 5 · [[4/5]].", "Çapraz sadeleştir: üstteki 5 ile alttaki 5. Sonra çarp."]},
        "Derin dondurucudaki": {"adimlar": [
            "Başlangıç (0): ilk sıcaklık. Düşmek eksidir: [[-3/2]].", "1 dakika için 3'e paylaştır: ([[-3/2]]) ÷ 3 = ([[-3/2]]) · [[1/3]].", "3 ile 3 sadeleşir. 0 ile −1 arası 2 parçaya bölünmüş; kaçıncı çizgi?"]},
    },
    "u1k12": {
        "3 + 4 · 2 kaçtır": {"adimlar": [
            "İşlemde hangi işaretler var? Toplama ve çarpma.", "Merdivende çarpma, toplamadan önce gelir: önce 4 · 2.", "Bulduğun sayıyı 3 ile topla."]},
        "[(+9) + (+21)] ÷ 2": {"adimlar": [
            "Parantezin içinde işlem var: önce o.", "Parantezin içi: 9 + 21.", "Bulduğun sayıyı 2'ye böl."]},
        "(−1) + (−15) ÷ (−3)": {"adimlar": [
            "Merdivene bak: bölme, toplama ve çıkarmadan önce.", "(−15) ÷ (−3): aynı işaret → artı.", "Sonra soldan sağa: (−1) + bulduğun sayı.", "En son − (−2): çıkarmayı tersiyle toplamaya çevir."]},
        "Tuğba kilogramı": {"adimlar": [
            "Ne isteniyor? Para üstü: 200'den ödenen parayı çıkaracağız.", "1 kg elma + 1 kg mandalina kaç TL?", "2'şer kg aldı: bu toplamı 2 ile çarp.", "200'den çıkar."]},
        "Asansör 3. kattaydı": {"adimlar": [
            "Başlangıç: 3. kat. Aşağı eksi, yukarı artı.", "İniş: 2 kez 4 kat → 2 · (−4).", "3'e bunu ekle, sonra 1 kat yukarı çık."]},
        "Bir depoda 40 litre": {"adimlar": [
            "Başlangıç: 40 litre. Dolan artı (+2), boşalan eksi (−6).", "1 saatteki değişim: 2 + (−6).", "5 saatlik değişim: 5 ile çarp.", "40 ile topla."]},
    },
    "u1t5": {
        "Selin'in yemek kartında": {"adimlar": [
            "Başlangıç: 600 TL. Yön: yemek parası düşüyor, bakiye −30 TL'ye iniyor.",
            "Kaç birim? 600'den 0'a ve 0'dan −30'a: iki parçayı topla.",
            "Toplam harcamanın içinde kaç tane 90 TL var? Böl."]},
        "Dört şehrin ocak": {"adimlar": [
            "Ortalama 1 ve 4 şehir var: toplam = 4 · 1.",
            "Bilinen üç sıcaklığı topla: 6 + (−3) + 5.",
            "Bilinmeyen = toplam − bilinenlerin toplamı. 0'ın altına iniyor musun?"]},
        "Bir ipin [[3/4]]'ü": {"adimlar": [
            "Bütün ip 1. [[3/4]]'ü gidince kalan: 1 − [[3/4]].",
            "Kalan parçanın yarısı da gidiyor; elde yarısı kalıyor: çarp.",
            "0 ile 1 arası 8 parçaya bölünmüş; kaçıncı çizgi?"]},
        "([[1/2]] − 2)": {"adimlar": [
            "Önce parantez. 2'yi paydası 2 olan kesir yap.",
            "Paydalar eşit: payları çıkar. İşaret ne oldu?",
            "Şimdi [[2/3]] ile çarp: önce çapraz sadeleştir."]},
        "−0,25 + [[3/4]] · 2": {"adimlar": [
            "İşlem sırası: çarpma toplamadan önce.",
            "[[3/4]] · 2: payı 2 ile çarp, sadeleştir, ondalığa çevir.",
            "Farklı işaretli iki sayıyı topla: büyükten küçüğü çıkar, büyüğün işaretini koy."]},
    },
}


def yardim_uygula(d):
    kv_adlari = {k["ad"] for k in d.get("kavramlar", [])}
    tk = TEST_KAVRAM.get(d["id"])
    if tk:
        assert len(tk) == len(d["sorular"]), d["id"] + ": TEST_KAVRAM sayısı test sayısına eşit değil"
        for q, k in zip(d["sorular"], tk):
            if k:
                assert k in kv_adlari, f"{d['id']}: kavram yok: {k}"
                q["kavram"] = k
    sorular = [k["soru"] for k in d.get("kavramlar", []) if k.get("soru")] + d["sorular"]
    for bas, y in YARDIM.get(d["id"], {}).items():
        es = [q for q in sorular if q["soru"].startswith(bas)]
        assert len(es) == 1, f"{d['id']}: '{bas}' {len(es)} soruyla eşleşti"
        es[0]["yardim"] = y
    return d


import re


def bosluk(x):
    """Sayı ile birimi ayrı satıra düşmesin: '−8 m' → '−8\u00a0m' (bölünmez boşluk)."""
    if isinstance(x, str):
        return x if x.lstrip().startswith("<svg") else re.sub(r"(\d) (m|km|cm|dm|mm|mL|dL|cL|L|TL|°C|kat|birim|br|MB|metre|derece|g|gram|dakika)([²³]?)(?![\w²³])", "\\1\u00a0\\2\\3", x)
    if isinstance(x, list):
        return [bosluk(v) for v in x]
    if isinstance(x, dict):
        return {k: bosluk(v) for k, v in x.items()}
    return x


if __name__ == "__main__":
    for f in KONULAR:
        d = bosluk(yardim_uygula(f()))
        json.dump(d, open(f"public/mat1/konular/{d['id']}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(d["id"], "yazıldı")
