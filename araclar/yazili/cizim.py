"""Yazılıya Hazırlık soru görselleri (Fen). Koyu zemin (#1b2340) üstüne açık renkli çizim; attribute'larda tek tırnak."""

C = {"zemin": "#1b2340", "yazi": "#f5f6fa", "soluk": "#a3abc6", "kuvvet": "#ff7a33", "hareket": "#8ee3d6", "altin": "#f2c14e",
     "mor": "#b197fc", "kirmizi": "#ff8a8a", "yesil": "#5fd08f", "mavi": "#6fb3ff"}


def svg(w, h, ic, etiket=""):
    return (f"<svg viewBox='0 0 {w} {h}' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='{etiket}' "
            f"font-family='Nunito, sans-serif'>{ic}</svg>")


def yazi(x, y, t, boy=11, renk=None, kalin=700, hiza="middle"):
    renk = renk or C["yazi"]
    satir = t.split("\n")
    y0 = y - (len(satir) - 1) * boy * 0.55
    ts = "".join(f"<tspan x='{x}' y='{y0 + i * boy * 1.1:.1f}'>{s}</tspan>" for i, s in enumerate(satir))
    return f"<text text-anchor='{hiza}' font-size='{boy}' font-weight='{kalin}' fill='{renk}'>{ts}</text>"


def ok(x1, y1, x2, y2, renk, kal=3, kesik=False):
    import math
    a = math.atan2(y2 - y1, x2 - x1); L = 9
    p1 = (x2 - L * math.cos(a - .45), y2 - L * math.sin(a - .45)); p2 = (x2 - L * math.cos(a + .45), y2 - L * math.sin(a + .45))
    d = " stroke-dasharray='6 5'" if kesik else ""
    return (f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{renk}' stroke-width='{kal}' stroke-linecap='round'{d}/>"
            f"<polygon points='{x2},{y2} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}' fill='{renk}'/>")


def kutu(x, y, w, h, t, renk, boy=10):
    return (f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='8' fill='{renk}' fill-opacity='.18' stroke='{renk}' stroke-width='2'/>"
            + yazi(x + w / 2, y + h / 2 + boy * .35, t, boy))


def insan(x, y, s=1, kollar="ileri"):
    """Basit çöp adam; (x, y) ayak hizası ortası."""
    r = C["yazi"]
    k = {"ileri": f"<path d='M{x} {y - 48 * s} l{18 * s} {6 * s} M{x} {y - 48 * s} l{18 * s} {12 * s}' stroke='{r}' stroke-width='3' stroke-linecap='round' fill='none'/>",
         "yukari": f"<path d='M{x} {y - 50 * s} l{-10 * s} {-22 * s} M{x} {y - 50 * s} l{10 * s} {-22 * s}' stroke='{r}' stroke-width='3' stroke-linecap='round' fill='none'/>",
         "asagi": f"<path d='M{x} {y - 48 * s} l{-12 * s} {18 * s} M{x} {y - 48 * s} l{12 * s} {18 * s}' stroke='{r}' stroke-width='3' stroke-linecap='round' fill='none'/>"}[kollar]
    return (f"<circle cx='{x}' cy='{y - 64 * s}' r='{8 * s}' fill='none' stroke='{r}' stroke-width='3'/>"
            f"<path d='M{x} {y - 56 * s} V{y - 26 * s} M{x} {y - 26 * s} l{-9 * s} {26 * s} M{x} {y - 26 * s} l{9 * s} {26 * s}' stroke='{r}' stroke-width='3' stroke-linecap='round' fill='none'/>" + k)


# ---------- Yıldızların yaşam şeması ----------
DONGU = {"b": "Bulutsu", "k1": "Küçük kütleli\nyıldız", "k2": "Kırmızı dev", "k3": "Gezegenimsi\nbulutsu", "k4": "Beyaz cüce",
         "b1": "Büyük kütleli\nyıldız", "b2": "Kırmızı\nsüperdev", "b3": "Süpernova", "b4": "Nötron yıldızı\nveya kara delik"}


def dongu(gizle=None, etiket="Yıldızların yaşam süreci şeması"):
    """gizle: {"k2": "1", ...} → o kutuda ad yerine numara/soru işareti."""
    gizle = gizle or {}
    ad = lambda k: gizle.get(k, DONGU[k])
    w, h = 460, 190
    ic = kutu(8, 72, 64, 46, ad("b"), C["mor"], 10)
    xs = [92, 184, 276, 368]
    for row, (ks, renk, y) in enumerate([(["k1", "k2", "k3", "k4"], C["altin"], 22), (["b1", "b2", "b3", "b4"], C["kirmizi"], 122)]):
        ic += ok(72, 95, xs[0] - 4, y + 23, C["soluk"], 2)
        for i, k in enumerate(ks):
            bw = 84
            ic += kutu(xs[i], y, bw, 46, ad(k), renk if k not in gizle else C["hareket"], 10 if "\n" in ad(k) or len(ad(k)) < 13 else 9)
            if i < 3: ic += ok(xs[i] + bw + 1, y + 23, xs[i + 1] - 3, y + 23, C["soluk"], 2)
    ic += yazi(230, 182, "Üst yol: küçük kütleli yıldız · Alt yol: büyük kütleli yıldız", 10, C["soluk"], 600)
    return svg(w, h, ic, etiket)


def kapsama(adlar=("Evren", "Galaksi", "Yıldız"), etiket="İç içe kavramlar"):
    ic = (f"<ellipse cx='180' cy='100' rx='170' ry='92' fill='{C['mor']}' fill-opacity='.15' stroke='{C['mor']}' stroke-width='2.5'/>"
          f"<ellipse cx='200' cy='112' rx='110' ry='62' fill='{C['mavi']}' fill-opacity='.18' stroke='{C['mavi']}' stroke-width='2.5'/>"
          f"<circle cx='232' cy='124' r='30' fill='{C['altin']}' fill-opacity='.25' stroke='{C['altin']}' stroke-width='2.5'/>"
          + yazi(70, 40, adlar[0], 15) + yazi(150, 82, adlar[1], 14) + yazi(232, 129, adlar[2], 13))
    return svg(360, 200, ic, etiket)


def uzay_copu():
    ic = (f"<circle cx='180' cy='100' r='46' fill='{C['mavi']}' fill-opacity='.35' stroke='{C['mavi']}' stroke-width='2'/>"
          + yazi(180, 104, "Dünya", 13)
          + f"<ellipse cx='180' cy='100' rx='130' ry='62' fill='none' stroke='{C['soluk']}' stroke-width='1.5' stroke-dasharray='4 5'/>")
    import random
    random.seed(4)
    import math
    for i in range(26):
        a = random.uniform(0, 2 * math.pi); rr = random.uniform(.85, 1.15)
        x, y = 180 + 130 * rr * math.cos(a), 100 + 62 * rr * math.sin(a)
        ic += f"<rect x='{x:.0f}' y='{y:.0f}' width='{random.choice([3, 4, 6])}' height='{random.choice([3, 4])}' fill='{random.choice([C['soluk'], C['kirmizi'], C['altin']])}' transform='rotate({random.randint(0, 80)} {x:.0f} {y:.0f})'/>"
    ic += (f"<g transform='translate(282 52)'><rect x='-6' y='-6' width='12' height='12' fill='{C['yazi']}'/><rect x='-26' y='-4' width='18' height='8' fill='{C['mavi']}'/><rect x='8' y='-4' width='18' height='8' fill='{C['mavi']}'/></g>"
           + yazi(300, 30, "çalışan uydu", 10, C["soluk"], 600) + yazi(74, 182, "uzay çöpleri (eski uydu, roket parçası)", 10, C["soluk"], 600, "start"))
    return svg(360, 195, ic, "Dünya çevresinde dolanan uzay çöpleri")


def itme_tasima():
    sandik = f"<rect x='92' y='96' width='54' height='44' rx='4' fill='{C['altin']}' fill-opacity='.3' stroke='{C['altin']}' stroke-width='2.5'/><path d='M92 96 L146 140 M146 96 L92 140' stroke='{C['altin']}' stroke-width='1.5'/>"
    ic = (f"<line x1='10' y1='140' x2='350' y2='140' stroke='{C['soluk']}' stroke-width='2'/>"
          + insan(70, 140, 1, "ileri") + sandik + ok(96, 82, 140, 82, C["kuvvet"]) + ok(100, 158, 150, 158, C["hareket"], 3, True)
          + yazi(90, 186, "Görsel 1: Sandığı itiyor", 11)
          + f"<line x1='180' y1='10' x2='180' y2='180' stroke='{C['soluk']}' stroke-opacity='.4'/>"
          + insan(262, 140, 1, "asagi")
          + f"<path d='M246 106 h10 v18 h-10z M268 106 h10 v18 h-10z' fill='{C['mavi']}' fill-opacity='.4' stroke='{C['mavi']}' stroke-width='2'/>"
          + ok(298, 128, 298, 92, C["kuvvet"]) + ok(232, 158, 300, 158, C["hareket"], 3, True)
          + yazi(270, 186, "Görsel 2: Poşetleri taşıyor", 11)
          + yazi(316, 112, "kuvvet", 10, C["kuvvet"], 800, "start") + yazi(148, 76, "kuvvet", 10, C["kuvvet"], 800, "start") + yazi(156, 162, "hareket", 10, C["hareket"], 800, "start"))
    return svg(360, 196, ic, "Sandığı iten kişi ve poşet taşıyan kişi; kuvvet ve hareket okları")


def halter():
    bar = lambda x, y: f"<line x1='{x - 34}' y1='{y}' x2='{x + 34}' y2='{y}' stroke='{C['yazi']}' stroke-width='4'/><rect x='{x - 44}' y='{y - 12}' width='10' height='24' rx='3' fill='{C['altin']}'/><rect x='{x + 34}' y='{y - 12}' width='10' height='24' rx='3' fill='{C['altin']}'/>"
    ic = (f"<line x1='10' y1='160' x2='350' y2='160' stroke='{C['soluk']}' stroke-width='2'/>"
          + insan(90, 160, 1, "yukari") + bar(90, 92) + ok(140, 132, 140, 88, C["kuvvet"]) + ok(30, 132, 30, 88, C["hareket"], 3, True)
          + yazi(150, 112, "kuvvet", 10, C["kuvvet"], 800, "start") + yazi(26, 146, "hareket", 10, C["hareket"], 800)
          + yazi(90, 186, "Durum 1: Kaldırma anı", 11)
          + f"<line x1='180' y1='10' x2='180' y2='180' stroke='{C['soluk']}' stroke-opacity='.4'/>"
          + insan(270, 160, 1, "yukari") + bar(270, 74) + ok(326, 112, 326, 72, C["kuvvet"])
          + yazi(318, 128, "kuvvet", 10, C["kuvvet"], 800) + yazi(270, 40, "hareket yok (sabit)", 10, C["hareket"], 800)
          + yazi(270, 186, "Durum 2: Sabit tutma anı", 11))
    return svg(360, 196, ic, "Halterci: kaldırma anı ve sabit tutma anı")


def elma():
    ic = (f"<line x1='10' y1='176' x2='350' y2='176' stroke='{C['yesil']}' stroke-width='3'/>"
          f"<rect x='82' y='70' width='18' height='106' fill='#8a6a4a'/>"
          f"<ellipse cx='110' cy='60' rx='86' ry='44' fill='{C['yesil']}' fill-opacity='.35' stroke='{C['yesil']}' stroke-width='2'/>"
          f"<circle cx='170' cy='86' r='8' fill='{C['kirmizi']}'/>" + yazi(170, 112, "dalda duran\nelma", 10, C["yazi"], 700)
          + f"<circle cx='250' cy='120' r='8' fill='{C['kirmizi']}'/>" + ok(250, 132, 250, 166, C["hareket"], 3, True)
          + yazi(298, 124, "düşmekte\nolan elma", 10, C["yazi"], 700)
          + ok(196, 172, 196, 92, C["altin"], 2) + yazi(204, 140, "h", 13, C["altin"], 800, "start"))
    return svg(360, 190, ic, "Daldaki elma ve düşen elma")


def kaykay():
    ic = (f"<path d='M10 40 C 90 40, 110 150, 190 150 S 290 150, 350 95' fill='none' stroke='{C['soluk']}' stroke-width='4'/>"
          f"<line x1='10' y1='176' x2='350' y2='176' stroke='{C['soluk']}' stroke-opacity='.5'/>"
          f"<circle cx='26' cy='40' r='6' fill='{C['altin']}'/><circle cx='190' cy='150' r='6' fill='{C['altin']}'/><circle cx='330' cy='106' r='6' fill='{C['altin']}'/>"
          + yazi(26, 26, "K", 14) + yazi(190, 136, "M", 14) + yazi(330, 92, "L", 14))
    return svg(360, 186, ic, "Kaykay parkuru: K en yüksek, L orta, M en alçak nokta")


def grafik():
    ic = (ok(50, 170, 50, 20, C["yazi"], 2) + ok(50, 170, 330, 170, C["yazi"], 2)
          + f"<line x1='50' y1='170' x2='300' y2='40' stroke='{C['kuvvet']}' stroke-width='4'/>"
          + yazi(60, 22, "Çekim potansiyel enerjisi", 11, C["yazi"], 800, "start") + yazi(334, 166, "a", 14, C["altin"], 800, "start") + yazi(40, 184, "0", 11))
    return svg(360, 192, ic, "Çekim potansiyel enerjisi a arttıkça doğru orantılı artıyor")


def iki_kosul():
    ic = (yazi(90, 22, "İş VAR", 14, C["yesil"], 800) + yazi(270, 22, "İş YOK", 14, C["kirmizi"], 800)
          + f"<rect x='60' y='60' width='50' height='40' rx='4' fill='{C['altin']}' fill-opacity='.3' stroke='{C['altin']}' stroke-width='2'/>"
          + ok(20, 80, 58, 80, C["kuvvet"]) + ok(70, 122, 150, 122, C["hareket"], 3, True)
          + yazi(90, 150, "Kuvvet ve hareket\naynı doğrultuda", 11)
          + f"<line x1='180' y1='10' x2='180' y2='180' stroke='{C['soluk']}' stroke-opacity='.4'/>"
          + f"<rect x='214' y='60' width='40' height='40' rx='4' fill='{C['mavi']}' fill-opacity='.3' stroke='{C['mavi']}' stroke-width='2'/>"
          + ok(234, 56, 234, 30, C["kuvvet"]) + ok(214, 122, 290, 122, C["hareket"], 3, True)
          + f"<rect x='300' y='60' width='40' height='40' rx='4' fill='{C['altin']}' fill-opacity='.3' stroke='{C['altin']}' stroke-width='2'/>"
          + ok(330, 80, 302, 80, C["kuvvet"]) + yazi(320, 122, "hareket\nyok", 10, C["hareket"], 800)
          + yazi(270, 160, "dik doğrultu · ya da\nyer değiştirme yok", 11))
    return svg(360, 186, ic, "İş için iki koşul")


def enerji_iki():
    ic = (yazi(90, 22, "Kinetik enerji", 13, C["hareket"], 800) + yazi(270, 22, "Çekim potansiyel enerjisi", 13, C["altin"], 800)
          + f"<line x1='10' y1='150' x2='170' y2='150' stroke='{C['soluk']}' stroke-width='2'/><circle cx='60' cy='136' r='14' fill='{C['kuvvet']}'/>"
          + ok(80, 136, 140, 136, C["hareket"], 3, True) + yazi(90, 176, "hareket ediyor → kütle + hız", 11)
          + f"<line x1='180' y1='10' x2='180' y2='180' stroke='{C['soluk']}' stroke-opacity='.4'/>"
          + f"<line x1='190' y1='150' x2='350' y2='150' stroke='{C['soluk']}' stroke-width='2'/><rect x='240' y='60' width='70' height='8' fill='{C['soluk']}'/><circle cx='275' cy='46' r='14' fill='{C['kuvvet']}'/>"
          + ok(330, 148, 330, 64, C["altin"], 2) + yazi(338, 110, "h", 13, C["altin"], 800, "start") + yazi(270, 176, "yüksekte duruyor → kütle + yükseklik", 11))
    return svg(360, 186, ic, "Kinetik ve çekim potansiyel enerjisi")


def kizak():
    ic = (f"<path d='M10 170 L120 40 L230 170' fill='#ffffff' fill-opacity='.12' stroke='{C['yazi']}' stroke-width='2.5'/>"
          f"<rect x='108' y='26' width='24' height='8' rx='3' fill='{C['kuvvet']}'/>" + yazi(150, 30, "duran kızak", 10, C["yazi"], 700, "start")
          + f"<rect x='170' y='96' width='24' height='8' rx='3' fill='{C['kuvvet']}' transform='rotate(50 182 100)'/>" + ok(196, 116, 218, 142, C["hareket"], 3, True)
          + yazi(240, 108, "kayan kızak", 10, C["yazi"], 700, "start"))
    return svg(360, 186, ic, "Dağın zirvesinde duran kızak ve aşağı kayan kızak")


def yay_ok():
    ic = (f"<path d='M80 30 Q 30 100 80 170' fill='none' stroke='{C['altin']}' stroke-width='5'/>"
          f"<path d='M80 30 L50 100 L80 170' fill='none' stroke='{C['yazi']}' stroke-width='1.5'/>"
          + ok(50, 100, 120, 100, C["kuvvet"], 2) + yazi(85, 196, "gerilmiş yay", 11)
          + ok(190, 90, 330, 90, C["yazi"], 3) + ok(200, 120, 300, 120, C["hareket"], 3, True) + yazi(260, 150, "havada giden ok", 11))
    return svg(360, 205, ic, "Gerilmiş yay ve havada giden ok")


def kaydirak():
    ic = (f"<path d='M60 50 h40 L300 170' fill='none' stroke='{C['mavi']}' stroke-width='6'/><line x1='60' y1='50' x2='60' y2='176' stroke='{C['soluk']}' stroke-width='4'/>"
          f"<line x1='10' y1='176' x2='350' y2='176' stroke='{C['soluk']}' stroke-width='2'/>"
          f"<circle cx='82' cy='34' r='10' fill='{C['altin']}'/>" + yazi(120, 30, "tepede oturan çocuk", 10, C["yazi"], 700, "start")
          + f"<circle cx='200' cy='100' r='10' fill='{C['altin']}'/>" + ok(212, 112, 250, 134, C["hareket"], 3, True) + yazi(228, 98, "kayan çocuk", 10, C["yazi"], 700, "start"))
    return svg(360, 186, ic, "Kaydırak: tepede oturan ve kayan çocuk")
