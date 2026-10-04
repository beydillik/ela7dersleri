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


TARAMALAR = [u1t1]
KONULAR = [u1k1, u1k2, u1k3] + TARAMALAR

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
    "u1t1": {
        "Bir dalgıç deniz seviyesinin 12": {"adimlar": [
            f"Deniz seviyesi 0. Dalgıç altında ({M}12), martı üstünde (+5).", "Dalgıçtan deniz seviyesine kaç metre?", "Deniz seviyesinden martıya kaç metre?", "İki parçayı topla."]},
        "Meryem'in aklındaki": {"adimlar": [
            f"Mutlak değeri 3 olan sayılar: 3 ve {M}3. Mutlak değeri 2 olanlar: 2 ve {M}2.",
            f"En uzak olmaları için biri 0'ın solunda, biri sağında olmalı: {M}3 ile +2 gibi.", f"{M}3'ten 0'a kaç birim? 0'dan +2'ye kaç birim? Topla."]},
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
        return x if x.lstrip().startswith("<svg") else re.sub(r"(\d) (m|km|TL|°C|kat|birim|MB|metre|derece|g|gram|dakika)\b", "\\1\u00a0\\2", x)
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
