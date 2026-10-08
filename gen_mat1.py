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


TARAMALAR = [u1t1, u1t2, u1t3, u1t4, u1t5]
KONULAR = [u1k1, u1k2, u1k3, u1k4, u1k5, u1k6, u1k7, u1k8, u1k9, u1k10, u1k11, u1k12] + TARAMALAR

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
        return x if x.lstrip().startswith("<svg") else re.sub(r"(\d) (m|km|cm|L|TL|°C|kat|birim|MB|metre|derece|g|gram|dakika)\b", "\\1\u00a0\\2", x)
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
