"""Yazılıya Hazırlık görselleri (Din Kültürü). Koyu zemin (#1b2340) üstüne açık renkli çizim; attribute'larda tek tırnak.
Melekler figürle çizilmez (proje kuralı): yalnız adlar ve simge. Yardımcılar cizim_sos'tan (svg, yazi, ok, C)."""
from cizim_sos import C, svg, yazi, ok


def kutu(x, y, w, h, renk, dolgu=.14, rx=10):
    return f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='{rx}' fill='{renk}' fill-opacity='{dolgu}' stroke='{renk}' stroke-width='2'/>"


def sol(x, y, t, boy=12, renk=None, kalin=600):
    """Sola yaslı yazı; t içinde tspan olabilir."""
    return f"<text x='{x}' y='{y}' font-size='{boy}' font-weight='{kalin}' fill='{renk or C['yazi']}' font-family='inherit'>{t}</text>"


def alti(t):
    """MEB sorusundaki altı çizili ifade: altın renk + alt çizgi."""
    return f"<tspan fill='#f2c14e' font-weight='800' text-decoration='underline'>{t}</tspan>"


def h_melek():
    """Altı melek adı ve görevi (7.1.1)."""
    L = [("Cebrail", "vahiy getirir", C["mavi"]), ("Azrail", "can alır", C["mor"]), ("Mikâil", "tabiat olayları", C["yesil"]),
         ("İsrafil", "sûra üfler", C["altin"]), ("Kiramen Kâtibin", "iyilik, kötülük yazar", C["mavi"]), ("Münker ve Nekir", "kabirde sorgular", C["mor"])]
    s = ""
    for i, (a, g, r) in enumerate(L):
        x, y = 14 + (i % 3) * 139, 14 + (i // 3) * 76
        s += kutu(x, y, 132, 66, r) + yazi(x + 66, y + 28, a, 13, r, 800) + yazi(x + 66, y + 50, g, 11, C["yazi"], 600)
    return svg(440, 166, s, "Altı melek adı ve görevleri")


def h_asama():
    """Ahiret hayatının sırası (7.1.2)."""
    L = [("Ölüm", C["soluk"]), ("Kıyamet", C["mor"]), ("Baas", C["mavi"]), ("Mahşer", C["altin"]), ("Mizan", C["yesil"])]
    s = ""
    for i, (a, r) in enumerate(L):
        x = 10 + i * 86
        s += kutu(x, 18, 72, 40, r) + yazi(x + 36, 43, a, 12, r, 800)
        if i < 4: s += ok(x + 73, 38, x + 85, 38, C["soluk"])
    s += ok(390, 60, 390, 82, C["soluk"])
    s += kutu(250, 84, 180, 40, C["yesil"]) + yazi(340, 109, "Cennet / Cehennem", 13, C["yesil"], 800)
    s += yazi(116, 96, "İsrafil: 1. üfleyiş = kıyamet", 11, C["yazi"], 600) + yazi(116, 116, "2. üfleyiş = baas (diriliş)", 11, C["yazi"], 600)
    return svg(440, 136, s, "Ölüm, kıyamet, baas, mahşer, mizan, cennet ve cehennem sırası")


def h_kazanc():
    """İnanç → bilir → davranış (7.1.3): 5 Hazır Cümle'nin iskeleti."""
    L = [("Yazılıyor", "sorumlu olurum", C["mavi"]), ("Hesap var", "kötülükten uzak dururum", C["altin"]),
         ("Kimse görmese de", "vicdanlı davranırım", C["mor"]), ("Dünya imtihan", "pes etmem, sabrederim", C["yesil"]), ("Karşılığı var", "iyilik yaparım", C["mavi"])]
    s = ""
    for i, (a, g, r) in enumerate(L):
        y = 10 + i * 34
        s += kutu(14, y, 160, 28, r, rx=8) + yazi(94, y + 19, a, 12, r, 800) + ok(178, y + 14, 206, y + 14, C["soluk"]) + kutu(210, y, 216, 28, r, .08, 8) + yazi(318, y + 19, g, 12, C["yazi"], 700)
    return svg(440, 184, s, "Melek ve ahiret inancı, bilmek ve davranış: beş hazır cümle")


def tablo_gruplar():
    """MEB 2. soru: boş tablo."""
    L = ["Dört Büyük Melek", "Yazıcı Melekler", "Sorgu Melekleri"]
    s = ""
    for i, a in enumerate(L):
        y = 8 + i * 42
        s += kutu(8, y, 128, 36, C["altin"], .12, 4) + sol(16, y + 23, a, 12, C["altin"], 700) + kutu(136, y, 196, 36, C["soluk"], .06, 4)
    return svg(340, 136, s, "Dört büyük melek, yazıcı melekler ve sorgu meleklerinin boş tablosu")


def tablo_ayetler():
    """MEB 4. soru: ayetler; altı çizili ifadeler altın renk ve çizgili."""
    R = [["“... Muhakkak siz, kıyamet gününde", alti("diriltileceksiniz") + ".” (Müminun suresi 16. ayet)"],
         ["“Kıyamet günü için " + alti("adalet terazileri"), "kuracağız… ” (Enbiya suresi 47. ayet)"],
         ["“... Ancak " + alti("O’nun huzurunda toplanacaksınız") + ".”", "Mülk suresi 24. ayet."],
         ["“... Allah kendi katından büyük bir", alti("mükâfat verir.") + "” (Nisa suresi 40. ayet)"],
         ["“(O gün) " + alti("sûra üflenecek") + ".”", "(Zümer suresi 68. ayet)"]]
    s = ""
    for i, (a, b) in enumerate(R):
        y = 8 + i * 58
        s += kutu(8, y, 252, 52, C["soluk"], .06, 4) + sol(14, y + 21, a, 11) + sol(14, y + 41, b, 11) + kutu(260, y, 72, 52, C["altin"], .12, 4) + yazi(296, y + 31, f"{i + 1}. ?", 13, C["altin"], 800)
    return svg(340, 300, s, "Altı çizili ifadeleri olan beş ayet ve yanlarında boş kutucuklar")
