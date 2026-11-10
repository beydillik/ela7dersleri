"""Yazılıya Hazırlık görselleri (İngilizce Own It, d1y1). Koyu zemin üstüne açık renk; attribute'larda tek tırnak.
Yonca: öğretmenin kâğıdındaki sıklık simgesinin özgün çizimi — dolu yaprak sayısı sıklığı gösterir
(4 always, 3 usually, 2 often, 1 sometimes, 0 dolu ama yaprak çizgisi var = rarely, yalnız sap/çizgi = never)."""
from cizim_ing import C, svg, yazi, tablo_svg

YESIL = "#5fd08f"
SIRA = [(4, "Always"), (3, "Usually"), (2, "Often"), (1, "Sometimes"), (0, "Rarely"), (-1, "Never")]


def yonca(cx, cy, n, r=7):
    """n dolu yaprak (saat yönünde sağ üstten); n = -1 → never (yalnız çizgiler)."""
    s = f"<line x1='{cx}' y1='{cy}' x2='{cx + r * .9}' y2='{cy + r * 2.4}' stroke='{YESIL}' stroke-width='2' stroke-linecap='round'/>"
    if n < 0:
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            s += f"<line x1='{cx}' y1='{cy}' x2='{cx + dx * r * 1.6}' y2='{cy + dy * r * 1.6}' stroke='{YESIL}' stroke-width='2' stroke-dasharray='3 2'/>"
        return s
    yer = [(1, -1), (1, 1), (-1, 1), (-1, -1)]   # sağ üst, sağ alt, sol alt, sol üst
    for i, (dx, dy) in enumerate(yer):
        dolu = i < n
        kesik = "" if dolu else " stroke-dasharray='3 2'"
        s += (f"<circle cx='{cx + dx * r * .85}' cy='{cy + dy * r * .85}' r='{r}' fill='{YESIL if dolu else 'none'}' "
              f"stroke='{YESIL}' stroke-width='1.6'{kesik}/>")
    return s


def lejant(w=340):
    s = yazi(w / 2, 16, "Dolu yaprak sayısı = sıklık", 12, C["altin"], 700)
    for i, (n, ad) in enumerate(SIRA):
        x = 30 + (i % 3) * 105; y = 42 + (i // 3) * 46
        s += yonca(x, y, n) + yazi(x + 22, y + 5, ad, 12, C["yazi"], 600, "start")
        s += yazi(x + 22, y + 19, "yalnız çizgi" if n < 0 else f"{n} dolu", 9.5, C["soluk"], 500, "start")
    return svg(w, 120, s, "Yonca lejantı: 4 dolu always, 3 usually, 2 often, 1 sometimes, 0 dolu rarely, yalnız çizgi never")


def tablo6(w=340):
    """Soru 6 tablosu: yalnız sorulan kutular (a örneği dahil); diğerleri boş."""
    hucre = {("Amanda", "Tennis"): 4, ("Amanda", "Cycling"): 2, ("Amanda", "Powerlifting"): 3,
             ("Patty", "Golfing"): 3, ("Patty", "Cycling"): -1, ("Stephen", "Tennis"): 1, ("Stephen", "Golfing"): 4}
    kisiler, sporlar = ["Amanda", "Patty", "Stephen"], ["Tennis", "Golfing", "Cycling", "Powerlifting"]
    x0, gen, y0, sh = 8, 82, 40, 44
    s = f"<rect x='{x0 + 96}' y='8' width='{gen * 3 - 6}' height='26' rx='6' fill='#2b3560'/>"
    for j, k in enumerate(kisiler): s += yazi(x0 + 96 + gen * j + gen / 2 - 3, 26, k, 12, C["altin"], 700)
    for i, sp in enumerate(sporlar):
        y = y0 + i * sh
        s += yazi(x0, y + sh / 2 + 4, sp, 12, C["mavi"], 700, "start")
        s += f"<line x1='{x0}' y1='{y + sh}' x2='{w - 8}' y2='{y + sh}' stroke='{C['cizgi']}' stroke-width='1'/>"
        for j, k in enumerate(kisiler):
            n = hucre.get((k, sp))
            cx = x0 + 96 + gen * j + gen / 2 - 3
            s += yonca(cx, y + sh / 2 - 6, n) if n is not None else yazi(cx, y + sh / 2 + 4, "·", 14, C["cizgi"], 700)
    return svg(w, y0 + 4 * sh + 6, s, "Soru 6 tablosu: Amanda tennis 4, cycling 2, powerlifting 3 dolu yaprak; Patty golf 3, cycling yalnız çizgi; Stephen tennis 1, golf 4")


def tablo8():
    return tablo_svg(["City", "Yesterday", "Today"], [["Antalya", "29", "34"], ["Ağrı", "11", "15"], ["İstanbul", "24", "20"]],
                     [110, 110, 100], etiket="Soru 8 tablosu: Antalya dün 29 bugün 34, Ağrı dün 11 bugün 15, İstanbul dün 24 bugün 20")
