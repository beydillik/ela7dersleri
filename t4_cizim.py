# -*- coding: utf-8 -*-
"""Tema 4 (Dönüşüm) çizim yardımcıları. gen_mat1.py ve araclar/sinav/mat1_u4.py içinden içe aktarılır.
Renk kodu bütün temada sabit (kitap dışı karar): şekil yeşil, görüntü turuncu, simetri doğrusu altın kesikli,
pergel yayları mavi, inşa sonucu (orta dikme / açıortay) pembe.
Kareli zemin koordinatı: (sütun, satır), satır aşağı doğru artar."""
import math
from t2_cizim import gsvg, _t, ACIK, SOLUK

SEK, GOR, ALT, PER, SON, IZ = "#4fc3a1", "#ffa26b", "#f2c14e", "#6fb3ff", "#f783ac", "#2f3a63"
LAC = "#1b2340"


def _p(pts):
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)


# ---------- Kareli zemin ----------
class Kare:
    def __init__(self, x0, y0, s, sutun, satir):
        self.x0, self.y0, self.s, self.C, self.R = x0, y0, s, sutun, satir

    def p(self, c, r):
        return self.x0 + c * self.s, self.y0 + r * self.s

    def zemin(self, renk=IZ):
        g = "".join(f"<line x1='{self.x0 + i * self.s:.1f}' y1='{self.y0:.1f}' x2='{self.x0 + i * self.s:.1f}' y2='{self.y0 + self.R * self.s:.1f}' stroke='{renk}' stroke-width='1'/>"
                    for i in range(self.C + 1))
        g += "".join(f"<line x1='{self.x0:.1f}' y1='{self.y0 + j * self.s:.1f}' x2='{self.x0 + self.C * self.s:.1f}' y2='{self.y0 + j * self.s:.1f}' stroke='{renk}' stroke-width='1'/>"
                     for j in range(self.R + 1))
        return g

    def dikey(self, c, renk=ALT, sw=2.5, uzat=6):
        x, _ = self.p(c, 0)
        return f"<line x1='{x:.1f}' y1='{self.y0 - uzat:.1f}' x2='{x:.1f}' y2='{self.y0 + self.R * self.s + uzat:.1f}' stroke='{renk}' stroke-width='{sw}' stroke-dasharray='6 4'/>"

    def yatay(self, r, renk=ALT, sw=2.5, uzat=6):
        _, y = self.p(0, r)
        return f"<line x1='{self.x0 - uzat:.1f}' y1='{y:.1f}' x2='{self.x0 + self.C * self.s + uzat:.1f}' y2='{y:.1f}' stroke='{renk}' stroke-width='{sw}' stroke-dasharray='6 4'/>"

    def cokgen(self, pts, renk=SEK, op=0.55, sw=2.2):
        P = [self.p(c, r) for c, r in pts]
        return f"<polygon points='{_p(P)}' fill='{renk}' fill-opacity='{op}' stroke='{renk}' stroke-width='{sw}' stroke-linejoin='round'/>"

    def parca(self, a, b, renk=ACIK, sw=2, kesik=False):
        (x1, y1), (x2, y2) = self.p(*a), self.p(*b)
        k = " stroke-dasharray='4 3'" if kesik else ""
        return f"<line x1='{x1:.1f}' y1='{y1:.1f}' x2='{x2:.1f}' y2='{y2:.1f}' stroke='{renk}' stroke-width='{sw}' stroke-linecap='round'{k}/>"

    def nokta(self, c, r, renk=SEK, etiket=None, dx=0, dy=-8, boy=12, rr=4.5):
        x, y = self.p(c, r)
        g = f"<circle cx='{x:.1f}' cy='{y:.1f}' r='{rr}' fill='{renk}' stroke='{LAC}' stroke-width='1.5'/>"
        if etiket:
            g += _t(x + dx, y + dy, etiket, renk, boy)
        return g

    def rozet(self, c, r, yazi, renk=ALT, rr=9, boy=12):
        x, y = self.p(c, r)
        return f"<circle cx='{x:.1f}' cy='{y:.1f}' r='{rr}' fill='{renk}' stroke='{LAC}' stroke-width='1.5'/>" + _t(x, y + boy * 0.36, yazi, LAC, boy)


def yans_d(pts, c):
    """Dikey doğruya (x = c) göre yansıma."""
    return [(2 * c - x, y) for x, y in pts]


def yans_y(pts, r):
    """Yatay doğruya (y = r) göre yansıma."""
    return [(x, 2 * r - y) for x, y in pts]


# ---------- Pergel ve inşa ----------
def yay(cx, cy, r, a1, a2, renk=PER, sw=2.2):
    """Merkez (cx, cy), yarıçap r; a1 → a2 derece (matematik yönü: saat yönünün tersi, y yukarı)."""
    x1, y1 = cx + r * math.cos(math.radians(a1)), cy - r * math.sin(math.radians(a1))
    x2, y2 = cx + r * math.cos(math.radians(a2)), cy - r * math.sin(math.radians(a2))
    buyuk = 1 if (a2 - a1) % 360 > 180 else 0
    return f"<path d='M{x1:.1f} {y1:.1f} A{r:.1f} {r:.1f} 0 {buyuk} 0 {x2:.1f} {y2:.1f}' stroke='{renk}' stroke-width='{sw}' fill='none' stroke-linecap='round'/>"


def cizgi(x1, y1, x2, y2, renk=ACIK, sw=2.2, kesik=False):
    k = " stroke-dasharray='6 4'" if kesik else ""
    return f"<line x1='{x1:.1f}' y1='{y1:.1f}' x2='{x2:.1f}' y2='{y2:.1f}' stroke='{renk}' stroke-width='{sw}' stroke-linecap='round'{k}/>"


def nokta(x, y, renk=ACIK, etiket=None, dx=0, dy=-9, boy=12, rr=4):
    g = f"<circle cx='{x:.1f}' cy='{y:.1f}' r='{rr}' fill='{renk}' stroke='{LAC}' stroke-width='1.5'/>"
    return g + (_t(x + dx, y + dy, etiket, renk, boy) if etiket else "")


def dik_isareti(x, y, ux, uy, k=8, renk=ACIK):
    """(x, y) köşesinde dik açı karesi; (ux, uy) birinci kolun birim yönü (ekran koordinatı); ikinci kol buna dik."""
    vx, vy = -uy, ux
    a = (x + ux * k, y + uy * k); b = (x + ux * k + vx * k, y + uy * k + vy * k); c = (x + vx * k, y + vy * k)
    return f"<path d='M{a[0]:.1f} {a[1]:.1f} L{b[0]:.1f} {b[1]:.1f} L{c[0]:.1f} {c[1]:.1f}' stroke='{renk}' stroke-width='1.6' fill='none'/>"


def esit_isareti(x1, y1, x2, y2, n=1, renk=ACIK, k=5):
    """Doğru parçasının ortasına n tane eşitlik çizgisi."""
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L; vx, vy = -uy, ux
    g = ""
    for i in range(n):
        o = (i - (n - 1) / 2) * 4
        cx, cy = mx + ux * o, my + uy * o
        g += f"<line x1='{cx - vx * k:.1f}' y1='{cy - vy * k:.1f}' x2='{cx + vx * k:.1f}' y2='{cy + vy * k:.1f}' stroke='{renk}' stroke-width='2'/>"
    return g


def orta_dikme_cizim(adim, ax, ay, bx, by, r=None, etiket=("A", "B"), kes=("K", "L"), boy=12, uzat=1.25):
    """Yatay ya da eğik AB doğru parçası üzerinde orta dikme inşası; adim 1–4:
    1 doğru parçası · 2 A merkezli yaylar · 3 B merkezli yaylar ve kesişim noktaları · 4 orta dikme, dik açı ve eşitlik işaretleri."""
    d = math.hypot(bx - ax, by - ay); r = r or d * 0.62
    ux, uy = (bx - ax) / d, (by - ay) / d; nx, ny = uy, -ux          # n: ekranda "yukarı" yana dik
    mx, my = (ax + bx) / 2, (ay + by) / 2; h = math.sqrt(r * r - (d / 2) ** 2)
    K = (mx + nx * h, my + ny * h); L = (mx - nx * h, my - ny * h)
    tA = math.degrees(math.atan2(-(K[1] - ay), K[0] - ax)); tB = math.degrees(math.atan2(-(K[1] - by), K[0] - bx))
    g = ""
    if adim >= 2:
        g += yay(ax, ay, r, tA - 16, tA + 16) + yay(ax, ay, r, -tA - 16, -tA + 16)
    if adim >= 3:
        g += yay(bx, by, r, tB - 16, tB + 16) + yay(bx, by, r, -tB - 16, -tB + 16)
    if adim >= 4:
        e = h * uzat
        g += cizgi(mx + nx * e, my + ny * e, mx - nx * e, my - ny * e, SON, 3)
        g += dik_isareti(mx, my, ux, uy, 8) + esit_isareti(ax, ay, mx, my, 1) + esit_isareti(mx, my, bx, by, 1)
    g += cizgi(ax, ay, bx, by, ACIK, 3)
    g += nokta(ax, ay, ACIK, etiket[0], -10 * ux, 18 if abs(uy) < 0.5 else -8, boy) + nokta(bx, by, ACIK, etiket[1], 10 * ux, 18 if abs(uy) < 0.5 else -8, boy)
    if adim >= 3:
        g += nokta(K[0], K[1], PER, kes[0], 10, -4, boy, 3.5) + nokta(L[0], L[1], PER, kes[1], 10, 12, boy, 3.5)
    return g


def aciortay_cizim(adim, vx, vy, a1, a2, kol=110, r1=None, r2=None, etiket="A", kl=("K", "L"), e_ad="E", boy=12, olcu=None):
    """Köşe (vx, vy), kollar a1 ve a2 derecede (matematik yönü). adim 1–4:
    1 açı · 2 köşe merkezli yay → K, L · 3 K ve L merkezli eş yaylar → E · 4 açıortay ve eş açı işaretleri.
    olcu: (bütün açı, yarım açı) yazıları, ör. ("80°", "40°")."""
    r1 = r1 or kol * 0.5
    u1 = (math.cos(math.radians(a1)), -math.sin(math.radians(a1))); u2 = (math.cos(math.radians(a2)), -math.sin(math.radians(a2)))
    K = (vx + u1[0] * r1, vy + u1[1] * r1); L = (vx + u2[0] * r1, vy + u2[1] * r1)
    am = (a1 + a2) / 2; b = (math.cos(math.radians(am)), -math.sin(math.radians(am)))
    yar = math.radians(abs(a2 - a1) / 2); hc = r1 * math.sin(yar)
    r2 = r2 or max(hc * 1.25, r1 * 0.75)
    t = r1 * math.cos(yar) + math.sqrt(r2 * r2 - hc * hc)
    E = (vx + b[0] * t, vy + b[1] * t)
    g = cizgi(vx, vy, vx + u1[0] * kol, vy + u1[1] * kol, ACIK, 3) + cizgi(vx, vy, vx + u2[0] * kol, vy + u2[1] * kol, ACIK, 3)
    if olcu and adim < 4:
        g += yay(vx, vy, 18, a1, a2, ALT, 2) + _t(vx + b[0] * 32, vy + b[1] * 32 + 4, olcu[0], ALT, 11)
    if adim >= 2:
        g += yay(vx, vy, r1, a1 - 8, a2 + 8)
    if adim >= 3:
        tK = math.degrees(math.atan2(-(E[1] - K[1]), E[0] - K[0])); tL = math.degrees(math.atan2(-(E[1] - L[1]), E[0] - L[0]))
        g += yay(K[0], K[1], r2, tK - 18, tK + 18) + yay(L[0], L[1], r2, tL - 18, tL + 18)
    if adim >= 4:
        g += cizgi(vx, vy, vx + b[0] * kol * 1.05, vy + b[1] * kol * 1.05, SON, 3)
        g += yay(vx, vy, 22, a1, am, ALT, 2) + yay(vx, vy, 27, am, a2, ALT, 2)
        if olcu:
            for aa in ((a1 + am) / 2, (am + a2) / 2):
                c = (math.cos(math.radians(aa)), -math.sin(math.radians(aa)))
                g += _t(vx + c[0] * 42, vy + c[1] * 42 + 4, olcu[1], ALT, 11)
    g += nokta(vx, vy, ACIK, etiket, -10, 5, boy)
    if adim >= 2:
        # etiketler kolun dışına: K (alt kol) aşağıda, L (üst kol) solda
        g += nokta(K[0], K[1], PER, kl[0], 0, 17, boy, 3.5) + nokta(L[0], L[1], PER, kl[1], -11, 2, boy, 3.5)
    if adim >= 3:
        g += nokta(E[0], E[1], PER, e_ad, 11, 14, boy, 3.5)
    return g
