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


def N(soru, nokta, sd, ipucu, aciklama):             # sayı doğrusunda noktaya dokunma
    return {"soru": soru, "nokta": nokta, "sayiDogrusu": sd, "ipucu": ipucu, "aciklama": aciklama}


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


KONULAR = [u1k1]

import re


def bosluk(x):
    """Sayı ile birimi ayrı satıra düşmesin: '−8 m' → '−8\u00a0m' (bölünmez boşluk)."""
    if isinstance(x, str):
        return x if x.lstrip().startswith("<svg") else re.sub(r"(\d) (m|km|TL|°C|kat|birim|MB|metre|derece)\b", "\\1\u00a0\\2", x)
    if isinstance(x, list):
        return [bosluk(v) for v in x]
    if isinstance(x, dict):
        return {k: bosluk(v) for k, v in x.items()}
    return x


if __name__ == "__main__":
    for f in KONULAR:
        d = bosluk(f())
        json.dump(d, open(f"public/mat1/konular/{d['id']}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(d["id"], "yazıldı")
