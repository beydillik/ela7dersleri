"""Yazılıya Hazırlık soru görselleri (Matematik). Koyu zemin (#1b2340) üstüne açık renkli çizim; attribute'larda tek tırnak.
Renk kodu (Matematik'in her yerinde aynı): negatif = mavi, pozitif = turuncu, sıfır = altın."""

C = {"zemin": "#1b2340", "yazi": "#f5f6fa", "soluk": "#a3abc6", "neg": "#6fb3ff", "pos": "#ffa26b", "sifir": "#f2c14e",
     "yesil": "#5fd08f", "kirmizi": "#ff8a8a", "mor": "#b197fc", "cizgi": "#59627f", "tebesir": "#e9f2e4"}
F = "Lexend, Nunito, sans-serif"


def svg(w, h, ic, etiket=""):
    return (f"<svg viewBox='0 0 {w} {h}' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='{etiket}' font-family='{F}'>"
            f"{ic}</svg>")


def yazi(x, y, t, boy=12, renk=None, kalin=600, hiza="middle"):
    return f"<text x='{x}' y='{y}' text-anchor='{hiza}' font-size='{boy}' font-weight='{kalin}' fill='{renk or C['yazi']}'>{t}</text>"


def renk_sayi(t):
    t = str(t)
    if t.startswith("−") or t.startswith("-"): return C["neg"]
    if t.startswith("+"): return C["pos"]
    return C["yazi"]


def kesir(x, y, t, boy=12, renk=None):
    """t: '−45/44', '7/20', '−1 3/4', '−5' gibi. (x, y) = kesir çizgisinin ortası."""
    t = str(t).replace("-", "−"); renk = renk or renk_sayi(t)
    if "/" not in t: return yazi(x, y + boy * .35, t, boy, renk)
    isaret = "−" if t.startswith("−") else ""
    g = t.lstrip("−")
    tam, kes = (g.split(" ") if " " in g else ("", g))
    a, b = kes.split("/")
    w = max(len(a), len(b)) * boy * .62 + 4
    s, x0 = "", x
    on = isaret + tam
    if on:
        ow = len(on) * boy * .62
        x0 = x + ow / 2 + 1
        s += yazi(x - w / 2 + 1, y + boy * .35, on, boy, renk, hiza="end")
    s += (yazi(x0, y - 3, a, boy, renk) + f"<line x1='{x0 - w / 2:.1f}' y1='{y + 1}' x2='{x0 + w / 2:.1f}' y2='{y + 1}' stroke='{renk}' stroke-width='1.4'/>"
          + yazi(x0, y + boy + 2, b, boy, renk))
    return s


def hucre(x, y, t, boy=12, renk=None):
    return kesir(x, y, t, boy, renk) if "/" in str(t) else yazi(x, y + boy * .35, t, boy, renk or renk_sayi(t))


def tablo(basliklar, satirlar, gen, w=340, sat_h=28, bas_h=30, boy=12, baslik=None, ust=8, ilk_sol=False):
    """Basit tablo. gen: sütun genişlikleri (toplam ≤ w - 16). Hücrede 'a/b' kesir olarak çizilir."""
    x0 = (w - sum(gen)) / 2; y = ust; s = ""
    if baslik: s += yazi(w / 2, y + 14, baslik, 12, C["soluk"]); y += 22
    xs = [x0 + sum(gen[:i]) for i in range(len(gen) + 1)]
    s += f"<rect x='{x0}' y='{y}' width='{sum(gen)}' height='{bas_h}' rx='6' fill='#2b3560'/>"
    for i, b in enumerate(basliklar): s += yazi((xs[i] + xs[i + 1]) / 2, y + bas_h / 2 + 4, b, boy - 1, C["sifir"], 700)
    y += bas_h
    for r in satirlar:
        h = sat_h
        for i, c in enumerate(r): s += hucre((xs[i] + xs[i + 1]) / 2, y + h / 2 - (2 if "/" in str(c) else 0), c, boy)
        s += f"<line x1='{x0}' y1='{y + h}' x2='{x0 + sum(gen)}' y2='{y + h}' stroke='{C['cizgi']}' stroke-width='1'/>"
        y += h
    for xx in xs[1:-1]: s += f"<line x1='{xx}' y1='{ust + (22 if baslik else 0)}' x2='{xx}' y2='{y}' stroke='{C['cizgi']}' stroke-width='1'/>"
    return s, y


def tablo_svg(basliklar, satirlar, gen, w=340, etiket="Tablo", **k):
    s, y = tablo(basliklar, satirlar, gen, w, **k)
    return svg(w, y + 10, s, etiket)


def iki_tablo(t1, t2, w=340, etiket="Tablo"):
    """t1, t2 = (basliklar, satirlar, gen, k) — üst üste iki tablo."""
    s1, y1 = tablo(t1[0], t1[1], t1[2], w, **(t1[3] if len(t1) > 3 else {}))
    s2, y2 = tablo(t2[0], t2[1], t2[2], w, ust=y1 + 14, **(t2[3] if len(t2) > 3 else {}))
    return svg(w, y2 + 10, s1 + s2, etiket)


def hesap_makinesi(ekran):
    s = (f"<rect x='120' y='14' width='200' height='190' rx='14' fill='#10162b' stroke='{C['cizgi']}' stroke-width='2'/>"
         f"<rect x='134' y='26' width='172' height='36' rx='6' fill='#22305e'/>" + yazi(298, 51, ekran, 17, C["yazi"], 700, "end"))
    tus = [["C", "√", "÷", "×"], ["7", "8", "9", "−"], ["4", "5", "6", "+"], ["1", "2", "3", ","], ["0", "", "=", ""]]
    for r, sat in enumerate(tus):
        for c, t in enumerate(sat):
            if not t: continue
            x, y = 136 + c * 43, 72 + r * 26
            ww = 80 if t == "=" else 36
            renk = "#2f9e44" if t == "=" else "#2b3560"
            s += f"<rect x='{x}' y='{y}' width='{ww}' height='21' rx='5' fill='{renk}'/>" + yazi(x + ww / 2, y + 15, t, 11)
    return svg(440, 218, s, f"Hesap makinesi ekranı: {ekran}")


def sayi_dogrusu_svg(a, b, bolme, isaret=None, etiket="Sayı doğrusu", alt=None, w=440):
    """a ile b (tam sayı) arası; her birim 'bolme' eş parça. isaret = (parça sırası a'dan, ad)."""
    x1, x2, y = 50, w - 50, 70
    s = f"<line x1='{x1 - 22}' y1='{y}' x2='{x2 + 22}' y2='{y}' stroke='{C['yazi']}' stroke-width='2'/>"
    s += f"<polygon points='{x1 - 30},{y} {x1 - 20},{y - 5} {x1 - 20},{y + 5}' fill='{C['yazi']}'/><polygon points='{x2 + 30},{y} {x2 + 20},{y - 5} {x2 + 20},{y + 5}' fill='{C['yazi']}'/>"
    n = (b - a) * bolme
    for i in range(n + 1):
        x = x1 + (x2 - x1) * i / n
        tam = i % bolme == 0
        s += f"<line x1='{x:.1f}' y1='{y - (11 if tam else 7)}' x2='{x:.1f}' y2='{y + (11 if tam else 7)}' stroke='{C['yazi']}' stroke-width='{2 if tam else 1.5}'/>"
        if tam:
            v = a + i // bolme
            t = f"−{abs(v)}" if v < 0 else (f"+{v}" if v > 0 else "0")
            s += yazi(x, y + 30, t, 14, renk_sayi(t) if v else C["sifir"], 700)
    if isaret:
        j, ad = isaret
        x = x1 + (x2 - x1) * j / n
        s += f"<circle cx='{x:.1f}' cy='{y}' r='6' fill='{C['sifir']}'/>" + yazi(x, y - 20, ad, 15, C["sifir"], 700)
    if alt: s += yazi(w / 2, y + 56, alt, 11, C["soluk"], 500)
    return svg(w, 140 if alt else 120, s, etiket)


def tahta_defter(tahta, defter, w=440):
    """Tahtada kesirler (virgüllü), defterde öğrencinin sıralaması (< ile)."""
    s = (f"<rect x='30' y='14' width='380' height='96' rx='8' fill='#1f4d3a' stroke='#8a6a3a' stroke-width='5'/>"
         + yazi(220, 36, "Aşağıdaki rasyonel sayıları küçükten büyüğe sıralayınız.", 11, C["tebesir"], 500))
    n = len(tahta)
    for i, t in enumerate(tahta): s += kesir(220 + (i - (n - 1) / 2) * 90, 66, t, 15, C["tebesir"])
    s += f"<rect x='60' y='124' width='320' height='72' rx='6' fill='#f5f1e6'/>"
    for k in range(4): s += f"<line x1='60' y1='{140 + k * 16}' x2='380' y2='{140 + k * 16}' stroke='#c9d6ea' stroke-width='1'/>"
    m = len(defter); xs = [220 + (i - (m - 1) / 2) * 100 for i in range(m)]
    for i, t in enumerate(defter):
        s += kesir(xs[i], 156, t, 15, "#1d4fa0")
        if i < m - 1: s += yazi((xs[i] + xs[i + 1]) / 2, 162, "&lt;", 17, "#1d4fa0", 700)
    s += yazi(220, 192, "Öğrencinin defteri", 10, "#6b7385", 500)
    return svg(w, 210, s, "Tahta ve öğrencinin defteri")


def tahta_kesir(sayilar, ust="", w=440):
    """Tabloda/tahtada yan yana kesirler (MEB 5. ve 7. soru gibi)."""
    s = yazi(w / 2, 28, ust, 12, C["soluk"], 500) if ust else ""
    n = len(sayilar)
    for i, t in enumerate(sayilar):
        x = w / 2 + (i - (n - 1) / 2) * min(100, (w - 60) / n)
        s += f"<rect x='{x - 40:.0f}' y='42' width='80' height='56' rx='10' fill='#2b3560'/>" + kesir(x, 66, t, 17)
    return svg(w, 112, s, "Rasyonel sayılar")


# ---------- Hatırla kartı çizimleri ----------
def h_altust():
    """Deniz seviyesi: üstü +, altı −."""
    s = (f"<rect x='16' y='70' width='408' height='72' rx='8' fill='#1d4f8f' fill-opacity='.55'/>"
         f"<line x1='16' y1='70' x2='424' y2='70' stroke='{C['sifir']}' stroke-width='2' stroke-dasharray='6 4'/>"
         + yazi(360, 64, "0 (deniz seviyesi)", 11, C["sifir"], 700)
         + f"<polygon points='70,68 110,22 150,68' fill='#5c677d'/>" + yazi(110, 16, "+5137 (üstü)", 12, C["pos"], 700)
         + f"<circle cx='250' cy='118' r='9' fill='{C['neg']}'/>" + yazi(250, 104, "−18 (altı)", 12, C["neg"], 700)
         + yazi(110, 100, "üstü, gelir, alacak → +", 11, C["pos"]) + yazi(110, 128, "altı, borç, kayıp → −", 11, C["neg"]))
    return svg(440, 152, s, "Deniz seviyesinin üstü pozitif, altı negatif")


def h_aralik():
    """Sıcaklık aralığı: en düşük ile en yüksek arası."""
    x = lambda v: 40 + (v + 50) * 6
    s = f"<line x1='30' y1='96' x2='420' y2='96' stroke='{C['yazi']}' stroke-width='2'/>"
    for v in range(-50, 21, 10):
        t = f"−{abs(v)}" if v < 0 else (f"+{v}" if v else "0")
        s += f"<line x1='{x(v)}' y1='90' x2='{x(v)}' y2='102' stroke='{C['yazi']}' stroke-width='1.5'/>" + yazi(x(v), 118, t, 11, renk_sayi(t) if v else C["sifir"], 700)
    s += f"<rect x='{x(-40)}' y='54' width='{x(10) - x(-40)}' height='14' rx='7' fill='{C['mor']}'/>" + yazi(x(-40) - 4, 65, "−40", 10, C["neg"], 700, "end") + yazi(x(10) + 4, 65, "+10", 10, C["pos"], 700, "start")
    s += f"<line x1='{x(-45)}' y1='26' x2='{x(-45)}' y2='96' stroke='{C['kirmizi']}' stroke-width='2' stroke-dasharray='4 3'/>" + yazi(x(-45), 20, "−45 dışarıda ✗", 11, C["kirmizi"], 700)
    s += f"<line x1='{x(-10)}' y1='34' x2='{x(-10)}' y2='96' stroke='{C['yesil']}' stroke-width='2' stroke-dasharray='4 3'/>" + yazi(x(-10), 28, "−10 içeride ✓", 11, C["yesil"], 700)
    return svg(440, 134, s, "En düşük ile en yüksek sıcaklık arasındaysa ✓")


def h_mutlak():
    x = lambda v: 220 + v * 15
    s = f"<line x1='30' y1='80' x2='410' y2='80' stroke='{C['yazi']}' stroke-width='2'/>"
    for v in (-11, 0, 11):
        t = f"−{abs(v)}" if v < 0 else (f"+{v}" if v else "0")
        s += f"<line x1='{x(v)}' y1='72' x2='{x(v)}' y2='88' stroke='{C['yazi']}' stroke-width='2'/>" + yazi(x(v), 108, t, 14, renk_sayi(t) if v else C["sifir"], 700)
    s += (f"<path d='M{x(0)} 66 Q{x(-5.5)} 30 {x(-11)} 66' fill='none' stroke='{C['neg']}' stroke-width='2.5'/>" + yazi(x(-5.5), 36, "11 birim", 12, C["neg"], 700)
          + f"<path d='M{x(0)} 66 Q{x(5.5)} 30 {x(11)} 66' fill='none' stroke='{C['pos']}' stroke-width='2.5'/>" + yazi(x(5.5), 36, "11 birim", 12, C["pos"], 700)
          + yazi(220, 134, "|−11| = |+11| = 11 · aradaki uzaklık 11 + 11 = 22", 12, C["sifir"], 700))
    return svg(440, 150, s, "Mutlak değer sıfıra uzaklıktır")


def h_kumeler():
    s = (f"<ellipse cx='220' cy='90' rx='200' ry='76' fill='{C['mor']}' fill-opacity='.18' stroke='{C['mor']}' stroke-width='2'/>"
         f"<ellipse cx='190' cy='96' rx='130' ry='54' fill='{C['neg']}' fill-opacity='.18' stroke='{C['neg']}' stroke-width='2'/>"
         f"<ellipse cx='165' cy='102' rx='62' ry='32' fill='{C['pos']}' fill-opacity='.22' stroke='{C['pos']}' stroke-width='2'/>"
         + yazi(370, 40, "Rasyonel", 13, C["mor"], 700) + kesir(370, 66, "21/4", 12, C["mor"]) + yazi(370, 108, "−1,8", 12, C["mor"])
         + yazi(268, 70, "Tam", 13, C["neg"], 700) + yazi(275, 96, "−5", 13, C["neg"]) + yazi(275, 120, "−7/7=−1", 11, C["neg"])
         + yazi(165, 94, "Doğal", 12, C["pos"], 700) + yazi(165, 114, "0  3  12/4=3", 11, C["pos"])
         + yazi(220, 182, "3/0 → tanımsız (hiçbir kümede değil)", 11, C["kirmizi"], 700))
    return svg(440, 196, s, "Doğal sayılar tam sayıların, tam sayılar rasyonel sayıların içinde")


def h_sonlu():
    s = (f"<rect x='20' y='16' width='400' height='34' rx='8' fill='#2b3560'/>" + yazi(220, 38, "1) Sadeleştir  →  2) Paydayı çarpanlara ayır", 13, C["yazi"], 700)
         + f"<rect x='20' y='62' width='190' height='70' rx='10' fill='{C['yesil']}' fill-opacity='.18' stroke='{C['yesil']}' stroke-width='2'/>"
         + yazi(115, 84, "Yalnız 2 ve 5", 13, C["yesil"], 700) + yazi(115, 104, "20 = 2 · 2 · 5", 12) + yazi(115, 124, "SONLU", 13, C["yesil"], 700)
         + f"<rect x='230' y='62' width='190' height='70' rx='10' fill='{C['kirmizi']}' fill-opacity='.15' stroke='{C['kirmizi']}' stroke-width='2'/>"
         + yazi(325, 84, "3, 7, 11… var", 13, C["kirmizi"], 700) + yazi(325, 104, "18 = 2 · 3 · 3", 12) + yazi(325, 124, "DEVİRLİ", 13, C["kirmizi"], 700))
    return svg(440, 146, s, "Paydada yalnız 2 ve 5 varsa sonlu, başka asal çarpan varsa devirli")


def h_devir():
    s = (yazi(92, 62, "1,2", 22, C["yazi"], 700, "end") + yazi(100, 62, "3", 22, C["sifir"], 700)
         + f"<line x1='93' y1='40' x2='107' y2='40' stroke='{C['sifir']}' stroke-width='2.5'/>" + yazi(140, 62, "=", 22)
         + yazi(230, 50, "123 − 12", 18, C["yazi"], 700) + f"<line x1='180' y1='58' x2='280' y2='58' stroke='{C['yazi']}' stroke-width='2'/>" + yazi(230, 82, "90", 18, C["yazi"], 700)
         + yazi(300, 62, "=", 22) + kesir(345, 60, "111/90", 18) + yazi(390, 62, "=", 22) + kesir(418, 60, "37/30", 15, C["yesil"])
         + yazi(230, 112, "Pay: hepsi − devretmeyen kısım (123 − 12)", 11, C["soluk"], 500)
         + yazi(230, 130, "Payda: devreden basamak kadar 9, devretmeyen ondalık kadar 0 → 90", 11, C["soluk"], 500))
    return svg(440, 146, s, "Devirli ondalık gösterimi kesre çevirme")


def h_sirala():
    x = lambda v: 60 + (v + 3) * 85
    s = f"<line x1='30' y1='80' x2='410' y2='80' stroke='{C['yazi']}' stroke-width='2'/><polygon points='414,80 404,75 404,85' fill='{C['yazi']}'/>"
    for v in range(-3, 2):
        t = f"−{abs(v)}" if v < 0 else (f"+{v}" if v else "0")
        s += f"<line x1='{x(v)}' y1='72' x2='{x(v)}' y2='88' stroke='{C['yazi']}' stroke-width='2'/>" + yazi(x(v), 108, t, 13, renk_sayi(t) if v else C["sifir"], 700)
    for v, t in ((-7 / 3, "−7/3"), (-5 / 6, "−5/6"), (-2 / 3, "−2/3"), (.5, "1/2")):
        dx = -22 if t == "−5/6" else 22 if t == "−2/3" else 0
        s += f"<circle cx='{x(v):.1f}' cy='80' r='5' fill='{C['sifir']}'/>" + kesir(x(v) + dx, 40, t, 12)
    s += yazi(220, 134, "Sola gittikçe küçülür · negatiflerde mutlak değeri büyük olan küçük", 11, C["soluk"], 500)
    return svg(440, 146, s, "Sayı doğrusunda soldaki sayı daha küçüktür")
