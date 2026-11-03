"""Yazılıya Hazırlık görselleri (İngilizce MEB). Koyu zemin (#1b2340) üstüne açık renkli çizim; attribute'larda tek tırnak.
Kişi çizimleri özgündür (MEB örneğindeki fotoğrafların yerine aynı ayırt edici özellikler: saç, göz, gözlük, beden)."""

C = {"zemin": "#1b2340", "kart": "#26305a", "yazi": "#f5f6fa", "soluk": "#a3abc6", "altin": "#f2c14e", "yesil": "#5fd08f",
     "kirmizi": "#ff8a8a", "mavi": "#6fb3ff", "mor": "#b197fc", "turuncu": "#ffa26b", "cizgi": "#59627f"}
F = "Fredoka, Nunito, sans-serif"
SAC = {"blonde": "#f2d16b", "brown": "#9a6233", "dark": "#33281f", "black": "#1e1a17", "ginger": "#e2672b", "gray": "#c9ccd6"}
GOZ = {"blue": "#4dabf7", "brown": "#7a4a22", "green": "#40c057"}
TEN = "#f1c592"


def svg(w, h, ic, etiket=""):
    return (f"<svg viewBox='0 0 {w} {h}' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='{etiket}' font-family='{F}'>"
            f"{ic}</svg>")


def yazi(x, y, t, boy=12, renk=None, kalin=600, hiza="middle"):
    return f"<text x='{x}' y='{y}' text-anchor='{hiza}' font-size='{boy}' font-weight='{kalin}' fill='{renk or C['yazi']}'>{t}</text>"


# ---------------------------------------------------------------- kişi
def kisi(x, y, no=None, sac="brown", stil="kisa", goz="brown", gozluk=False, beden="normal", tisort="#5c7cfa", w=100, h=128):
    """Göğüs hizasında basit kişi kartı. stil: kisa (kısa düz), dalgali (kısa dalgalı), kivircik (kısa kıvırcık),
    uzun_duz, uzun_dalgali, uzun_kivircik. beden: ince, normal, kilolu."""
    cx, s = x + w / 2, ""
    s += f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='14' fill='{C['kart']}'/>"
    hy = y + 52                                    # baş merkezi
    rx_ = {"ince": 19, "normal": 21, "kilolu": 26}[beden]; ry_ = 24 if beden != "kilolu" else 25
    om = {"ince": 26, "normal": 33, "kilolu": 44}[beden]   # omuz yarı genişliği
    sc = SAC[sac]
    # arka saç (uzun stiller)
    if stil == "uzun_duz":
        s += f"<path d='M{cx - rx_ - 4} {hy - 6} Q{cx} {hy - 40} {cx + rx_ + 4} {hy - 6} L{cx + rx_ + 6} {hy + 38} L{cx - rx_ - 6} {hy + 38} Z' fill='{sc}'/>"
    elif stil == "uzun_dalgali":
        s += (f"<path d='M{cx - rx_ - 4} {hy - 8} Q{cx} {hy - 42} {cx + rx_ + 4} {hy - 8} q8 10 2 20 q8 10 2 20 q6 6 -2 10 "
              f"L{cx - rx_ - 4} {hy + 42} q-8 -4 -2 -10 q-8 -10 -2 -20 q-8 -10 2 -20 Z' fill='{sc}'/>")
    elif stil == "uzun_kivircik":
        for dx, dy in ((-24, -4), (24, -4), (-27, 14), (27, 14), (-25, 32), (25, 32), (-14, 40), (14, 40)):
            s += f"<circle cx='{cx + dx}' cy='{hy + dy}' r='10' fill='{sc}'/>"
    # gövde
    s += f"<path d='M{cx - om} {y + h} Q{cx - om} {hy + 34} {cx} {hy + 32} Q{cx + om} {hy + 34} {cx + om} {y + h} Z' fill='{tisort}'/>"
    s += f"<rect x='{cx - 6}' y='{hy + 18}' width='12' height='14' fill='{TEN}'/>"
    # baş
    s += f"<ellipse cx='{cx}' cy='{hy}' rx='{rx_}' ry='{ry_}' fill='{TEN}'/>"
    if beden == "kilolu":
        s += f"<ellipse cx='{cx - 13}' cy='{hy + 9}' rx='5' ry='3.5' fill='#f08f7a' opacity='.6'/><ellipse cx='{cx + 13}' cy='{hy + 9}' rx='5' ry='3.5' fill='#f08f7a' opacity='.6'/>"
    # ön saç
    if stil in ("kisa", "uzun_duz"):
        s += f"<path d='M{cx - rx_ - 1} {hy - 2} Q{cx - rx_} {hy - ry_ - 8} {cx} {hy - ry_ - 6} Q{cx + rx_} {hy - ry_ - 8} {cx + rx_ + 1} {hy - 2} Q{cx + 6} {hy - 18} {cx - rx_ - 1} {hy - 2} Z' fill='{sc}'/>"
    elif stil in ("dalgali", "uzun_dalgali"):
        s += (f"<path d='M{cx - rx_ - 2} {hy} Q{cx - rx_ - 2} {hy - ry_ - 8} {cx} {hy - ry_ - 7} Q{cx + rx_ + 2} {hy - ry_ - 8} {cx + rx_ + 2} {hy} "
              f"q-5 -8 -9 -10 q-4 6 -10 0 q-5 6 -10 0 q-5 6 -10 0 q-4 4 -8 10 Z' fill='{sc}'/>")
    elif stil in ("kivircik", "uzun_kivircik"):
        for dx, dy in ((-18, -14), (-8, -22), (4, -24), (15, -19), (22, -8), (-23, -3)):
            s += f"<circle cx='{cx + dx}' cy='{hy + dy}' r='9' fill='{sc}'/>"
    # yüz
    gz = GOZ[goz]
    for d in (-8, 8):
        s += f"<circle cx='{cx + d}' cy='{hy + 1}' r='4.2' fill='#fff'/><circle cx='{cx + d}' cy='{hy + 1.5}' r='2.6' fill='{gz}'/><circle cx='{cx + d + .8}' cy='{hy + .6}' r='.8' fill='#fff'/>"
    if gozluk:
        s += (f"<circle cx='{cx - 8}' cy='{hy + 1}' r='7' fill='none' stroke='#1b2340' stroke-width='2'/><circle cx='{cx + 8}' cy='{hy + 1}' r='7' fill='none' stroke='#1b2340' stroke-width='2'/>"
              f"<line x1='{cx - 1}' y1='{hy + 1}' x2='{cx + 1}' y2='{hy + 1}' stroke='#1b2340' stroke-width='2'/>")
    s += f"<path d='M{cx - 6} {hy + 11} Q{cx} {hy + 16} {cx + 6} {hy + 11}' fill='none' stroke='#9c3d2e' stroke-width='2' stroke-linecap='round'/>"
    if no is not None:
        s += f"<circle cx='{x + 16}' cy='{y + 16}' r='11' fill='{C['altin']}'/>" + yazi(x + 16, y + 20.5, str(no), 13, "#1b2340", 700)
    return s


def kisiler(liste, etiket="Resimler", w=None):
    """liste: kisi() argüman sözlükleri; numara sırayla 1, 2, 3…"""
    n = len(liste); gen = 100; ara = 8; sut = 3 if n > 3 else n   # telefonda büyük görünsün: satırda en çok 3 kişi
    sat = (n + sut - 1) // sut
    W = w or sut * gen + (sut - 1) * ara + 8
    s = ""
    for i, k in enumerate(liste):
        r, c = divmod(i, sut); kalan = n - r * sut; x0 = (W - (min(sut, kalan) * gen + (min(sut, kalan) - 1) * ara)) / 2
        s += kisi(x0 + c * (gen + ara), 4 + r * 136, no=i + 1, **k)
    return svg(W, sat * 136 + 4, s, etiket)


# ---------------------------------------------------------------- tablo (kesir çizmez)
def tablo_svg(basliklar, satirlar, gen, w=340, sat_h=31, bas_h=32, boy=13.5, etiket="Tablo", ilk_kalin=True):
    x0 = (w - sum(gen)) / 2; y = 6; s = ""
    xs = [x0 + sum(gen[:i]) for i in range(len(gen) + 1)]
    s += f"<rect x='{x0}' y='{y}' width='{sum(gen)}' height='{bas_h}' rx='6' fill='#2b3560'/>"
    for i, b in enumerate(basliklar): s += yazi((xs[i] + xs[i + 1]) / 2, y + bas_h / 2 + 4.5, b, boy, C["altin"], 700)
    y += bas_h
    for r in satirlar:
        for i, c in enumerate(r):
            s += yazi((xs[i] + xs[i + 1]) / 2, y + sat_h / 2 + 4.5, c, boy if i or not ilk_kalin else boy - 1, C["mavi"] if (i == 0 and ilk_kalin) else C["yazi"], 700 if i == 0 else 500)
        s += f"<line x1='{x0}' y1='{y + sat_h}' x2='{x0 + sum(gen)}' y2='{y + sat_h}' stroke='{C['cizgi']}' stroke-width='1'/>"
        y += sat_h
    for xx in xs[1:-1]: s += f"<line x1='{xx}' y1='6' x2='{xx}' y2='{y}' stroke='{C['cizgi']}' stroke-width='1'/>"
    return svg(w, y + 8, s, etiket)


# ---------------------------------------------------------------- sıklık piramidi (MEB grafiği)
SIKLIK = [("ALWAYS", "100%"), ("USUALLY", "90%"), ("OFTEN", "70%"), ("SOMETIMES", "50%"), ("RARELY", "10%"), ("NEVER", "0%")]


def piramit(w=340, gizle=False, etiket="How often? Sıklık zarfları grafiği"):
    """MEB'in grafiği: her zaman %100 … asla %0. gizle=True → zarf adları yerine '?' (Hatırla'da değil, yalnız alıştırmada)."""
    s = yazi(w / 2, 18, "HOW OFTEN?", 13, C["altin"], 700)
    ust, alt, h, y = 230, 40, 26, 28
    renk = ["#3b5bdb", "#4263eb", "#4c6ef5", "#5c7cfa", "#748ffc", "#91a7ff"]
    for i, (ad, yz) in enumerate(SIKLIK):
        g1 = ust - (ust - alt) * i / 6; g2 = ust - (ust - alt) * (i + 1) / 6; cx = w / 2 + 20
        s += f"<path d='M{cx - g1 / 2:.1f} {y} L{cx + g1 / 2:.1f} {y} L{cx + g2 / 2:.1f} {y + h - 3} L{cx - g2 / 2:.1f} {y + h - 3} Z' fill='{renk[i]}'/>"
        s += yazi(cx, y + h / 2 + 3, "?" if gizle else ad, 11 if len(ad) < 8 else 10, "#fff", 700)
        s += yazi(cx - ust / 2 - 10, y + h / 2 + 3, yz, 11, C["soluk"], 700, "end")
        y += h
    return svg(w, y + 8, s, etiket)


# ---------------------------------------------------------------- Hatırla kartı çizimleri
def h_gorunus():
    s = kisi(8, 6, sac="ginger", stil="uzun_dalgali", goz="green", tisort="#e64980") + kisi(332, 6, sac="dark", stil="kivircik", goz="brown", gozluk=True, beden="kilolu", tisort="#2f9e44")
    s += yazi(220, 26, "What does she look like?", 13, C["altin"], 700) + yazi(220, 44, "long wavy ginger hair · green eyes", 11, C["yazi"], 500)
    s += yazi(220, 62, "(görünüş: boy, kilo, saç, göz)", 10, C["soluk"], 500)
    s += yazi(220, 92, "What is he like?", 13, C["mavi"], 700) + yazi(220, 110, "always on time → punctual", 11, C["yazi"], 500)
    s += yazi(220, 126, "(kişilik: davranıştan sıfat)", 10, C["soluk"], 500)
    return svg(440, 140, s, "Görünüş ve kişilik")


def h_karsilastir():
    s = ""
    for x, ad, boy_, yas in ((40, "Helen", 70, 17), (130, "Sally", 92, 15)):
        s += f"<rect x='{x}' y='{118 - boy_}' width='50' height='{boy_}' rx='8' fill='{C['mavi'] if ad == 'Helen' else C['turuncu']}' opacity='.85'/>"
        s += yazi(x + 25, 132, ad, 11) + yazi(x + 25, 112 - boy_, f"{yas} yaş", 10, C["soluk"], 500)
    s += yazi(318, 30, "Helen is older than Sally.", 12, C["mavi"], 700)
    s += yazi(318, 50, "Sally is taller than Helen.", 12, C["turuncu"], 700)
    s += yazi(318, 76, "kısa sıfat → -er than", 11, C["yazi"], 500)
    s += yazi(318, 96, "uzun sıfat → more … than", 11, C["yazi"], 500)
    s += yazi(318, 116, "good → better", 11, C["altin"], 600)
    return svg(440, 140, s, "Karşılaştırma: -er than, more … than")


def ikon_raket(x, y):
    return (f"<ellipse cx='{x}' cy='{y}' rx='13' ry='16' fill='none' stroke='{C['altin']}' stroke-width='3'/>"
            f"<line x1='{x}' y1='{y + 16}' x2='{x}' y2='{y + 32}' stroke='{C['altin']}' stroke-width='4' stroke-linecap='round'/>"
            f"<circle cx='{x + 20}' cy='{y - 10}' r='5' fill='#d8f5a2'/>")


def ikon_top(x, y, renk="#ffa26b"):
    return f"<circle cx='{x}' cy='{y}' r='14' fill='{renk}'/><path d='M{x - 14} {y} H{x + 14} M{x} {y - 14} V{y + 14}' stroke='#1b2340' stroke-width='1.6'/>"


def ikon_yay(x, y):
    return (f"<path d='M{x - 6} {y - 20} Q{x + 14} {y} {x - 6} {y + 20}' fill='none' stroke='{C['turuncu']}' stroke-width='3'/>"
            f"<line x1='{x - 6}' y1='{y - 20}' x2='{x - 6}' y2='{y + 20}' stroke='{C['yazi']}' stroke-width='1.2'/>"
            f"<line x1='{x - 16}' y1='{y}' x2='{x + 18}' y2='{y}' stroke='{C['yazi']}' stroke-width='2'/><path d='M{x + 18} {y} l-6 -4 v8 z' fill='{C['yazi']}'/>")


def ikon_dag(x, y):
    return f"<path d='M{x - 20} {y + 14} L{x - 4} {y - 14} L{x + 6} {y + 2} L{x + 12} {y - 6} L{x + 22} {y + 14} Z' fill='{C['yesil']}'/><path d='M{x - 8} {y - 7} L{x - 4} {y - 14} L{x} {y - 7} Z' fill='#fff'/>"


def h_spor():
    s = ""
    kutu = [(ikon_raket, "racket + net", "tennis"), (lambda x, y: ikon_top(x, y), "kick + goal", "football"),
            (ikon_yay, "bow + arrows", "archery"), (ikon_dag, "sneakers + mountains", "hiking")]
    for i, (f, ip, ad) in enumerate(kutu):
        x = 10 + i * 107
        s += f"<rect x='{x}' y='8' width='99' height='124' rx='14' fill='{C['kart']}'/>" + f(x + 50, 48)
        s += yazi(x + 50, 96, ip, 10, C["soluk"], 500) + yazi(x + 50, 118, "→ " + ad, 13, C["altin"], 700)
    return svg(440, 140, s, "Ekipmandan spor adı")


def h_siklik():
    return piramit(340, etiket="Sıklık zarfları: always %100, usually %90, often %70, sometimes %50, rarely %10, never %0")
