# -*- coding: utf-8 -*-
"""Tema 2 (Geometrik Nicelikler) çizim yardımcıları. gen_mat1.py içinden içe aktarılır.
Eğik izdüşüm: i sağa, j arkaya (sağ-yukarı çapraz), k yukarı.
Ayrıt renkleri bütün temada sabit (kitap dışı karar): en yeşil, boy (derinlik) mor, yükseklik pembe."""

EN, BOY, YUK = "#5fd08f", "#b197fc", "#f783ac"
KUP = ("#9fe6cf", "#4fc3a1", "#2f8f73")          # küp yüzleri: üst, ön, yan
YUZ = ("#ffd166", "#6fb3ff", "#ff8fab")           # açınımda eş yüz çiftleri: üst-alt, ön-arka, sağ-sol
ACIK, SOLUK = "#f5f6fa", "#9aa3bf"


def _t(x, y, t, renk=ACIK, boy=14, kalin=800, hiza="middle"):
    return f"<text x='{x:.1f}' y='{y:.1f}' text-anchor='{hiza}' font-family='Lexend, Baloo 2, sans-serif' font-weight='{kalin}' font-size='{boy}' fill='{renk}'>{t}</text>"


def _poly(pts, fill, stroke="#1b2340", sw=1.6, ek=""):
    p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return f"<polygon points='{p}' fill='{fill}' stroke='{stroke}' stroke-width='{sw}' stroke-linejoin='round'{ek}/>"


def gsvg(w, h, ic):
    """Soru ve adım görseli: şeffaf zemin (motor .q-gorsel kutusu koyu zemini verir)."""
    return f"<svg viewBox='0 0 {w} {h}' xmlns='http://www.w3.org/2000/svg' role='img'>{ic}</svg>"


# ---------- Eş küplerden yapı ----------
def kupler(kup, x0, y0, s, d=None, renk=KUP, cizgi="#1b2340"):
    """kup: (i, j, k) listesi. (x0, y0): (0, 0, 0) küpünün ön-alt-sol köşesi."""
    d = s * 0.5 if d is None else d
    out = ""
    for i, j, k in sorted(set(kup), key=lambda c: (-c[1], c[2], c[0])):
        x, y = x0 + i * s + j * d, y0 - k * s - j * d
        out += _poly([(x, y), (x + s, y), (x + s, y - s), (x, y - s)], renk[1], cizgi)
        out += _poly([(x, y - s), (x + s, y - s), (x + s + d, y - s - d), (x + d, y - s - d)], renk[0], cizgi)
        out += _poly([(x + s, y), (x + s + d, y - d), (x + s + d, y - s - d), (x + s, y - s)], renk[2], cizgi)
    return out


def yapi_boyut(kup, s, d=None):
    d = s * 0.5 if d is None else d
    I = max(c[0] for c in kup) + 1; J = max(c[1] for c in kup) + 1; Kk = max(c[2] for c in kup) + 1
    return I * s + J * d, Kk * s + J * d          # genişlik, yükseklik


def yapi(kup, cx, alt, s, yonler=True, d=None):
    """Yapıyı yatayda cx'e ortalar, tabanı alt çizgisine oturtur; isteğe bağlı Ön ve Sağ etiketleri."""
    d = s * 0.5 if d is None else d
    w, _ = yapi_boyut(kup, s, d)
    x0 = cx - w / 2
    g = kupler(kup, x0, alt, s, d)
    if yonler:
        I = max(c[0] for c in kup) + 1
        g += _t(x0 + I * s / 2, alt + 14, "Ön", SOLUK, 11, 700)
        g += _t(x0 + w + 4, alt - 4, "Sağ", SOLUK, 11, 700, "start")
    return g


def gor(kup, yon):
    """Bir yönden görünümde görülen kareler: {(sütun, satır)}, satır 0 = en alt. Kurallar:
    ön (i, k); arka ön'ün aynası; sağ (j, k) ön taraf solda; sol sağ'ın aynası;
    üst (i, j) ön taraf altta; alt üst'ün yatay aynası (BK s. 122: ön-arka, sağ-sol dikey; üst-alt yatay doğruya göre simetrik)."""
    f = {"on": lambda i, j, k: (i, k), "arka": lambda i, j, k: (-i, k), "sag": lambda i, j, k: (j, k),
         "sol": lambda i, j, k: (-j, k), "ust": lambda i, j, k: (i, j), "alt": lambda i, j, k: (i, -j)}[yon]
    ks = {f(*c) for c in kup}
    mc, mr = min(c for c, r in ks), min(r for c, r in ks)
    return frozenset((c - mc, r - mr) for c, r in ks)


def izgara(kareler, x, alt, s, renk="#4fc3a1", cizgi="#1b2340"):
    """Görünüm çizimi: kareler {(sütun, satır)}; (x, alt) sol-alt köşe."""
    return "".join(f"<rect x='{x + c * s:.1f}' y='{alt - (r + 1) * s:.1f}' width='{s}' height='{s}' fill='{renk}' stroke='{cizgi}' stroke-width='1.6'/>"
                   for c, r in sorted(kareler))


def izgara_orta(kareler, cx, alt, s, renk="#4fc3a1"):
    w = (max(c for c, r in kareler) + 1) * s
    return izgara(kareler, cx - w / 2, alt, s, renk)


def secenekler3(cizimler, w=330, h=150, etiket_y=None):
    """Üç seçenek paneli: cizimler[i] = f(cx, alt) → svg parçası. Altında A, B, C."""
    g = ""
    for n, f in enumerate(cizimler):
        cx = w / 6 + n * w / 3
        g += f(cx, h - 30)
        g += f"<circle cx='{cx:.1f}' cy='{h - 12}' r='10' fill='#f2c14e'/>" + _t(cx, h - 7, "ABC"[n], "#1b2340", 13)
        if n:
            g += f"<line x1='{n * w / 3:.1f}' y1='8' x2='{n * w / 3:.1f}' y2='{h - 28}' stroke='#3a4570' stroke-width='1.5' stroke-dasharray='4 4'/>"
    return gsvg(w, h, g)


# ---------- Dikdörtgenler prizması ----------
def prizma(x, y, A, B, C, et=None, dolgu=True, gizli=True, vurgu=None):
    """(x, y) ön-alt-sol köşe; A en, B derinlik (eğik, yarı ölçek), C yükseklik (piksel).
    et = (en, boy, yükseklik) etiketleri; vurgu: 'ayrit' | 'kose' | 'yuz' (bir öğeyi sarıyla işaretle)."""
    D = B * 0.5
    g = ""
    if dolgu:
        g += _poly([(x, y), (x + A, y), (x + A, y - C), (x, y - C)], "#33406e", "none", 0)
        g += _poly([(x, y - C), (x + A, y - C), (x + A + D, y - C - D), (x + D, y - C - D)], "#3f4f86", "none", 0)
        g += _poly([(x + A, y), (x + A + D, y - D), (x + A + D, y - C - D), (x + A, y - C)], "#283258", "none", 0)
    if vurgu == "yuz":
        g += _poly([(x, y), (x + A, y), (x + A, y - C), (x, y - C)], "#f2c14e", "none", 0, " fill-opacity='0.55'")
    if gizli:
        g += (f"<path d='M{x + D:.1f} {y - D:.1f} H{x + A + D:.1f} M{x + D:.1f} {y - D:.1f} V{y - C - D:.1f} M{x + D:.1f} {y - D:.1f} L{x:.1f} {y:.1f}' "
              f"stroke='{SOLUK}' stroke-width='1.5' stroke-dasharray='4 3' fill='none'/>")
    g += (f"<path d='M{x:.1f} {y:.1f} H{x + A:.1f} V{y - C:.1f} H{x:.1f} Z M{x:.1f} {y - C:.1f} L{x + D:.1f} {y - C - D:.1f} H{x + A + D:.1f} L{x + A:.1f} {y - C:.1f} "
          f"M{x + A + D:.1f} {y - C - D:.1f} V{y - D:.1f} L{x + A:.1f} {y:.1f}' stroke='{ACIK}' stroke-width='2' fill='none' stroke-linejoin='round'/>")
    if et:
        e, b, c = et
        g += f"<line x1='{x:.1f}' y1='{y:.1f}' x2='{x + A:.1f}' y2='{y:.1f}' stroke='{EN}' stroke-width='3.5'/>" + _t(x + A / 2, y + 16, e, EN, 13)
        g += f"<line x1='{x:.1f}' y1='{y:.1f}' x2='{x:.1f}' y2='{y - C:.1f}' stroke='{YUK}' stroke-width='3.5'/>" + _t(x - 5, y - C / 2 + 5, c, YUK, 13, 800, "end")
        g += f"<line x1='{x + A:.1f}' y1='{y:.1f}' x2='{x + A + D:.1f}' y2='{y - D:.1f}' stroke='{BOY}' stroke-width='3.5'/>" + _t(x + A + D / 2 + 6, y - D / 2 + 9, b, BOY, 13, 800, "start")
    if vurgu == "ayrit":
        g += f"<line x1='{x + A:.1f}' y1='{y:.1f}' x2='{x + A:.1f}' y2='{y - C:.1f}' stroke='#f2c14e' stroke-width='5' stroke-linecap='round'/>"
    if vurgu == "kose":
        g += f"<circle cx='{x + A:.1f}' cy='{y - C:.1f}' r='6' fill='#f2c14e' stroke='#1b2340' stroke-width='1.5'/>"
    return g


# ---------- Açınım ----------
def acinim(x, y, A, B, C, yazi=None, renk=YUZ, cizgi="#1b2340", boy=12):
    """Haç biçimli açınım. (x, y) üst yüzün sol-üst köşesi. Orta sütun: üst (A×B), ön (A×C), alt (A×B), arka (A×C);
    ön'ün solunda sol, sağında sağ (B×C). yazi: {'ust','on','alt','arka','sol','sag'} → yüzün içine yazı."""
    yuzler = {"ust": (x, y, A, B, renk[0]), "on": (x, y + B, A, C, renk[1]), "alt": (x, y + B + C, A, B, renk[0]),
              "arka": (x, y + 2 * B + C, A, C, renk[1]), "sol": (x - B, y + B, B, C, renk[2]), "sag": (x + A, y + B, B, C, renk[2])}
    g = ""
    for ad, (a, b, w, h, r) in yuzler.items():
        g += f"<rect x='{a:.1f}' y='{b:.1f}' width='{w:.1f}' height='{h:.1f}' fill='{r}' stroke='{cizgi}' stroke-width='1.8'/>"
        if yazi and yazi.get(ad):
            g += _t(a + w / 2, b + h / 2 + boy * 0.36, yazi[ad], "#1b2340", boy)
    return g


def kare_ag(hucreler, x, y, s, cizgi="#1b2340", boy=13):
    """Kareli açınım: hucreler [(sütun, satır, renk, yazı)], satır 0 en üstte; (x, y) sol-üst."""
    g = ""
    for c, r, renk, yz in hucreler:
        g += f"<rect x='{x + c * s:.1f}' y='{y + r * s:.1f}' width='{s}' height='{s}' fill='{renk}' stroke='{cizgi}' stroke-width='1.8'/>"
        if yz:
            g += _t(x + c * s + s / 2, y + r * s + s / 2 + boy * 0.36, yz, "#1b2340", boy)
    return g


def kare_ag_orta(hucreler, cx, alt, s, renk="#4fc3a1"):
    C = max(h[0] for h in hucreler) + 1; R = max(h[1] for h in hucreler) + 1
    hs = [(h[0], h[1], h[2] if len(h) > 2 else renk, h[3] if len(h) > 3 else "") for h in hucreler]
    return kare_ag(hs, cx - C * s / 2, alt - R * s, s)
