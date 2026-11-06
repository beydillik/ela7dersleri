"""Yazılıya Hazırlık görselleri (Türkçe). Koyu zemin (#1b2340) üstüne açık renkli çizim; attribute'larda tek tırnak.
Yardımcılar cizim_sos'tan (svg, yazi, balon, ok, C)."""
from cizim_sos import C, svg, yazi, balon, ok


def kutu(x, y, w, h, renk, dolgu=.14):
    return f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='12' fill='{renk}' fill-opacity='{dolgu}' stroke='{renk}' stroke-width='2'/>"


def h_anlam():
    """Bilinmeyen kelime → çevresindeki ipucu kelimeler → anlam (T.O.7.21)."""
    s = (kutu(20, 16, 400, 44, C["cizgi"], .25)
         + yazi(220, 43, "… eğitim ve <tspan fill='#f2c14e'>keşif</tspan> görevleri için tasarlanmış …", 14, C["yazi"], 600)
         + ok(150, 66, 120, 92, C["mavi"]) + ok(290, 66, 320, 92, C["mavi"])
         + kutu(30, 96, 170, 40, C["mavi"]) + yazi(115, 121, "İpucu: eğitim, görev", 12, C["mavi"])
         + kutu(240, 96, 170, 40, C["yesil"]) + yazi(325, 121, "Anlamı: inceleme", 12, C["yesil"])
         + yazi(220, 156, "Kelimeyi başka kelimelerle açıkla.", 12, C["soluk"], 600))
    return svg(440, 166, s, "Bilinmeyen kelimenin anlamını çevresindeki kelimelerden bulma")


def h_konu():
    """Konu: neyi anlatıyor (kısa) · Ana düşünce: ne demek istiyor (cümle) (T.O.7.5)."""
    s = (kutu(16, 14, 196, 108, C["altin"])
         + yazi(114, 38, "KONU", 15, C["altin"], 800) + yazi(114, 60, "Metin neyi anlatıyor?", 12, C["yazi"], 600)
         + yazi(114, 84, "kısa: birkaç kelime", 11, C["soluk"], 600) + yazi(114, 106, "“Arıların doğadaki önemi”", 11, C["altin"])
         + kutu(228, 14, 196, 108, C["mor"])
         + yazi(326, 38, "ANA DÜŞÜNCE", 15, C["mor"], 800) + yazi(326, 60, "Yazar ne demek istiyor?", 12, C["yazi"], 600)
         + yazi(326, 84, "bir cümle, ders verir", 11, C["soluk"], 600) + yazi(326, 106, "“Arıları korumalıyız.”", 11, C["mor"])
         + yazi(220, 146, "Konu ≠ ana düşünce", 12, C["soluk"], 600))
    return svg(440, 156, s, "Konu ve ana düşünce farkı")


def h_tahmin():
    """Tahmin + gerekçe: iki parça (T.O.7.4)."""
    s = (kutu(16, 14, 408, 40, C["cizgi"], .25)
         + yazi(220, 39, "İhtiyarlamış, çok <tspan fill='#f2c14e'>bitap</tspan> düşmüştü. Kolları kuvvetini kaybetmiş…", 12.5, C["yazi"], 600)
         + kutu(16, 70, 196, 62, C["yesil"]) + yazi(114, 93, "1) TAHMİNİM", 13, C["yesil"], 800) + yazi(114, 116, "yorgun, güçsüz", 12, C["yazi"], 600)
         + kutu(228, 70, 196, 62, C["mavi"]) + yazi(326, 93, "2) GEREKÇEM", 13, C["mavi"], 800) + yazi(326, 116, "“kuvvetini kaybetmiş”", 12, C["yazi"], 600)
         + yazi(220, 154, "Gerekçe = metinden ipucu cümlesi (kendi fikrin değil)", 12, C["soluk"], 600))
    return svg(440, 164, s, "Kelimenin anlamını tahmin edip metinden gerekçe yazma")


def h_yazim():
    """İkileme ayrı ve çizgisiz · noktalı virgül · üç nokta (T.Y.7.21)."""
    s = (kutu(16, 12, 408, 40, C["kirmizi"]) + yazi(220, 37, "apar-topar ✗   hızlıhızlı ✗   →   apar topar ✓   hızlı hızlı ✓", 12.5, C["yazi"], 700)
         + kutu(16, 62, 200, 84, C["altin"]) + yazi(116, 84, ";  noktalı virgül", 14, C["altin"], 800)
         + yazi(116, 103, "• özneden sonra", 11, C["yazi"], 600) + yazi(116, 119, "• virgüllü sıralı cümleler", 11, C["yazi"], 600)
         + yazi(116, 135, "• virgüllü gruplar", 11, C["yazi"], 600)
         + kutu(224, 62, 200, 84, C["mavi"]) + yazi(324, 84, "…  üç nokta", 14, C["mavi"], 800)
         + yazi(324, 103, "• cümle yarım kaldı", 11, C["yazi"], 600) + yazi(324, 119, "• eksik bırakılan cevap", 11, C["yazi"], 600)
         + yazi(324, 135, "• seslenmeyi pekiştirme", 11, C["yazi"], 600)
         + yazi(220, 166, "İşaret + amacı: ikisini de yaz.", 12, C["soluk"], 600))
    return svg(440, 176, s, "İkilemelerin yazımı, noktalı virgül ve üç nokta")


def h_taslak():
    """Giriş → gelişme → sonuç taslağı (T.Y.7.3)."""
    s = (kutu(16, 14, 128, 92, C["yesil"]) + yazi(80, 38, "GİRİŞ", 14, C["yesil"], 800) + yazi(80, 62, "konuyu", 11, C["yazi"], 600) + yazi(80, 78, "tanıt", 11, C["yazi"], 600)
         + ok(148, 60, 166, 60, C["soluk"])
         + kutu(170, 14, 128, 92, C["altin"]) + yazi(234, 38, "GELİŞME", 14, C["altin"], 800) + yazi(234, 62, "açıkla,", 11, C["yazi"], 600) + yazi(234, 78, "örnek ver", 11, C["yazi"], 600)
         + ok(302, 60, 320, 60, C["soluk"])
         + kutu(324, 14, 100, 92, C["mor"]) + yazi(374, 38, "SONUÇ", 14, C["mor"], 800) + yazi(374, 62, "toparla:", 11, C["yazi"], 600) + yazi(374, 78, "Sonuç olarak…", 11, C["yazi"], 600)
         + yazi(220, 132, "Önce 3 satır taslak, sonra her bölüme 1–2 cümle.", 12, C["soluk"], 600))
    return svg(440, 144, s, "Giriş, gelişme ve sonuç taslağı")
