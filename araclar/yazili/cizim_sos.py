"""Yazılıya Hazırlık görselleri (Sosyal Bilgiler). Koyu zemin (#1b2340) üstüne açık renkli çizim; attribute'larda tek tırnak."""

C = {"zemin": "#1b2340", "yazi": "#f5f6fa", "soluk": "#a3abc6", "altin": "#f2c14e", "yesil": "#5fd08f", "kirmizi": "#ff8a8a",
     "mavi": "#6fb3ff", "mor": "#b197fc", "turuncu": "#ffa26b", "cizgi": "#59627f"}
F = "Nunito, sans-serif"


def svg(w, h, ic, etiket=""):
    return (f"<svg viewBox='0 0 {w} {h}' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='{etiket}' font-family='{F}'>"
            f"{ic}</svg>")


def yazi(x, y, t, boy=12, renk=None, kalin=700, hiza="middle"):
    return f"<text x='{x}' y='{y}' text-anchor='{hiza}' font-size='{boy}' font-weight='{kalin}' fill='{renk or C['yazi']}'>{t}</text>"


def balon(x, y, w, h, renk, kuyruk="sol"):
    kx = x + 26 if kuyruk == "sol" else x + w - 26
    return (f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='14' fill='{renk}' fill-opacity='.16' stroke='{renk}' stroke-width='2'/>"
            f"<path d='M{kx - 8} {y + h} L{kx} {y + h + 14} L{kx + 8} {y + h}' fill='{C['zemin']}' stroke='{renk}' stroke-width='2' stroke-linejoin='round'/>"
            f"<line x1='{kx - 7}' y1='{y + h}' x2='{kx + 7}' y2='{y + h}' stroke='{C['zemin']}' stroke-width='3'/>")


def ok(x1, y1, x2, y2, renk, kal=2.5):
    import math
    a = math.atan2(y2 - y1, x2 - x1); L = 8
    p1 = (x2 - L * math.cos(a - .45), y2 - L * math.sin(a - .45)); p2 = (x2 - L * math.cos(a + .45), y2 - L * math.sin(a + .45))
    return (f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{renk}' stroke-width='{kal}' stroke-linecap='round'/>"
            f"<polygon points='{x2},{y2} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}' fill='{renk}'/>")


def h_iletisim():
    """Sen dili ✗ / ben dili ✓ / empati."""
    s = (balon(12, 10, 196, 46, C["kirmizi"]) + yazi(110, 30, "Sen hep geç kalıyorsun!", 12, C["kirmizi"]) + yazi(110, 47, "✗ sen dili: suçlar", 11, C["soluk"], 600)
         + balon(232, 10, 196, 46, C["yesil"], "sag") + yazi(330, 30, "Geç kaldığında üzülüyorum.", 12, C["yesil"]) + yazi(330, 47, "✓ ben dili: duygumu söylerim", 11, C["soluk"], 600)
         + balon(60, 86, 320, 46, C["altin"]) + yazi(220, 106, "Seni anlıyorum. İstersen birlikte …", 12, C["altin"]) + yazi(220, 123, "✓ empati: onun yerine kendimi koyarım", 11, C["soluk"], 600))
    return svg(440, 146, s, "Sen dili, ben dili ve empati cümleleri")


def h_firsat():
    """Merdiven + rampa: fırsat eşitliği; kaldırımda takip şeridi."""
    s = f"<line x1='14' y1='118' x2='426' y2='118' stroke='{C['cizgi']}' stroke-width='2'/>"
    for i in range(4):   # merdiven
        s += f"<rect x='{40 + i * 22}' y='{96 - i * 18}' width='{(4 - i) * 22}' height='18' fill='#5c677d' stroke='{C['zemin']}' stroke-width='1'/>"
    s += f"<rect x='128' y='26' width='70' height='92' rx='4' fill='none' stroke='{C['soluk']}' stroke-width='2'/>" + yazi(163, 76, "PARK", 12, C["soluk"])
    s += f"<polygon points='198,46 330,118 198,118' fill='{C['yesil']}' fill-opacity='.35' stroke='{C['yesil']}' stroke-width='2'/>"
    s += yazi(84, 20, "yalnız merdiven ✗", 11, C["kirmizi"]) + yazi(300, 70, "rampa ✓", 13, C["yesil"]) + yazi(300, 86, "fırsat eşitliği", 11, C["yesil"], 600)
    s += f"<rect x='340' y='108' width='80' height='8' rx='2' fill='{C['altin']}'/>" + yazi(380, 100, "takip şeridi", 11, C["altin"])
    s += yazi(220, 140, "Herkes aynı haklara sahip; ihtiyaca göre düzenleme yapılır.", 11, C["soluk"], 600)
    return svg(440, 150, s, "Merdivenin yanına rampa: fırsat eşitliği")


def h_milli():
    """Zaman şeridi: yenilgi → Mondros → işgal → 19 Mayıs 1919 → halk birlik oldu."""
    kutu = lambda x, y, w, a, b, r: (f"<rect x='{x}' y='{y}' width='{w}' height='48' rx='10' fill='{r}' fill-opacity='.16' stroke='{r}' stroke-width='2'/>"
                                     + yazi(x + w / 2, y + 21, a, 12, r) + yazi(x + w / 2, y + 38, b, 12, r))
    s = yazi(14, 18, "1) NEDEN: Samsun'dan önce ne oldu?", 12, C["soluk"], 700, "start")
    s += kutu(10, 26, 124, "Birinci Dünya", "Savaşı'nda yenilgi", C["kirmizi"]) + ok(136, 50, 156, 50, C["soluk"])
    s += kutu(158, 26, 124, "Mondros Ateşkes", "Antlaşması", C["turuncu"]) + ok(284, 50, 304, 50, C["soluk"])
    s += kutu(306, 26, 124, "Anadolu", "işgal edildi", C["kirmizi"])
    s += f"<path d='M368 76 L368 92 L72 92 L72 104' fill='none' stroke='{C['soluk']}' stroke-width='2.5'/>" + ok(72, 100, 72, 110, C["soluk"])
    s += kutu(10, 112, 150, "19 Mayıs 1919", "Samsun'a çıkış", C["altin"]) + ok(162, 136, 196, 136, C["soluk"])
    s += kutu(198, 112, 232, "Halk birlik oldu,", "imkânlarını orduyla paylaştı", C["yesil"])
    s += yazi(314, 106, "2) TUTUM: halk ne yaptı?", 12, C["soluk"], 700)
    s += yazi(220, 182, "15 Temmuz 2016 ve 6 Şubat 2023'te de millet birlik oldu.", 11, C["soluk"], 600)
    return svg(440, 192, s, "Millî Mücadele zaman şeridi: neden ve tutum")


def h_kuresel():
    """Eskiden mektup günler sürerdi → şimdi genel ağ ile anında."""
    zarf = (f"<rect x='40' y='34' width='90' height='58' rx='4' fill='none' stroke='{C['soluk']}' stroke-width='2.5'/>"
            f"<path d='M40 34 L85 70 L130 34' fill='none' stroke='{C['soluk']}' stroke-width='2.5'/>")
    tel = (f"<rect x='316' y='22' width='48' height='84' rx='9' fill='none' stroke='{C['mavi']}' stroke-width='2.5'/>"
           f"<circle cx='340' cy='96' r='4' fill='{C['mavi']}'/>"
           f"<rect x='323' y='34' width='34' height='22' rx='6' fill='{C['mavi']}' fill-opacity='.3'/>"
           f"<rect x='323' y='60' width='26' height='18' rx='6' fill='{C['yesil']}' fill-opacity='.35'/>")
    s = (zarf + yazi(85, 18, "ESKİDEN", 12, C["soluk"]) + yazi(85, 112, "mektup: günler sürerdi", 11, C["soluk"], 600)
         + ok(160, 64, 290, 64, C["altin"], 3) + yazi(225, 54, "küreselleşme", 11, C["altin"])
         + tel + yazi(340, 14, "ŞİMDİ", 12, C["mavi"]) + yazi(340, 122, "genel ağ: anında", 11, C["mavi"], 600))
    return svg(440, 132, s, "Eskiden mektup, şimdi genel ağ ile anında iletişim")
