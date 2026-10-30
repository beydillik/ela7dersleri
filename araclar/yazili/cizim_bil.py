"""Yazılıya Hazırlık çizimleri (Teknoloji ve Tasarım). Koyu zemin (#1b2340) üstüne açık renk; tek tırnak.
Ortak yardımcılar cizim.py'den (svg, yazi, kutu, ok, C)."""
from cizim import svg, yazi, kutu, ok, C


def bulus_icat():
    """Keşif (var olanı bulmak) ↔ icat (var olanları birleştirip yeni şey yapmak)."""
    ic = (yazi(90, 22, "KEŞİF / BULUŞ", 13, C["altin"], 800)
          # büyüteç altında yer çekimi: düşen elma
          + "<circle cx='78' cy='92' r='34' fill='none' stroke='#f5f6fa' stroke-width='4'/>"
          + "<line x1='102' y1='116' x2='126' y2='140' stroke='#f5f6fa' stroke-width='7' stroke-linecap='round'/>"
          + "<circle cx='78' cy='86' r='11' fill='#ff8a8a'/><path d='M78 75 q4 -8 10 -8' stroke='#5fd08f' stroke-width='3' fill='none'/>"
          + ok(78, 100, 78, 116, C["hareket"], 3)
          + yazi(90, 168, "Vardı, bilinmiyordu:\nbulundu", 11, C["soluk"], 700)
          + "<line x1='180' y1='18' x2='180' y2='182' stroke='#a3abc6' stroke-width='2' stroke-dasharray='5 6'/>"
          + yazi(270, 22, "İCAT", 13, C["mavi"], 800)
          # iki parça → yeni ürün
          + kutu(200, 50, 46, 30, "tahta", C["hareket"], 10) + yazi(256, 70, "+", 18, C["yazi"], 800) + kutu(266, 50, 46, 30, "ateş", C["kuvvet"], 10)
          + ok(256, 88, 256, 112, C["altin"], 3)
          + kutu(216, 118, 80, 30, "kibrit", C["altin"], 11)
          + yazi(270, 168, "Var olanlar birleşti:\nyeni şey yapıldı", 11, C["soluk"], 700))
    return svg(360, 190, ic, "Keşif var olanı bulmak, icat var olanları birleştirip yeni bir şey yapmaktır")


def tasarim_dallari():
    """Üç uygulamalı tasarım dalı: endüstri, çevre, grafik."""
    ic = (yazi(180, 22, "TASARIM DALLARI", 13, C["altin"], 800)
          # endüstri: tencere (seri üretim)
          + "<rect x='22' y='62' width='76' height='46' rx='8' fill='none' stroke='#8ee3d6' stroke-width='4'/>"
          + "<line x1='12' y1='70' x2='22' y2='70' stroke='#8ee3d6' stroke-width='4'/><line x1='98' y1='70' x2='108' y2='70' stroke='#8ee3d6' stroke-width='4'/>"
          + "<rect x='30' y='52' width='60' height='10' rx='4' fill='#8ee3d6'/>"
          + yazi(60, 136, "Endüstriyel\ntasarım", 12, C["yazi"], 800) + yazi(60, 170, "seri üretim ürün", 10, C["soluk"], 600)
          # çevre: ev + ağaç
          + "<path d='M140 108 v-34 l30 -24 l30 24 v34 z' fill='none' stroke='#ffa26b' stroke-width='4' stroke-linejoin='round'/>"
          + "<rect x='162' y='86' width='16' height='22' fill='#ffa26b'/>"
          + "<circle cx='214' cy='80' r='12' fill='#5fd08f'/><line x1='214' y1='92' x2='214' y2='108' stroke='#5fd08f' stroke-width='4'/>"
          + yazi(180, 136, "Çevre\ntasarımı", 12, C["yazi"], 800) + yazi(180, 170, "bina, peyzaj, iç mekân", 10, C["soluk"], 600)
          # grafik: afiş
          + "<rect x='268' y='48' width='56' height='64' rx='4' fill='none' stroke='#b197fc' stroke-width='4'/>"
          + "<circle cx='296' cy='70' r='9' fill='#f2c14e'/><line x1='278' y1='92' x2='314' y2='92' stroke='#b197fc' stroke-width='4'/><line x1='278' y1='102' x2='304' y2='102' stroke='#b197fc' stroke-width='3'/>"
          + yazi(296, 136, "Grafik\ntasarım", 12, C["yazi"], 800) + yazi(296, 170, "afiş, broşür, kitap", 10, C["soluk"], 600))
    return svg(360, 190, ic, "Endüstriyel tasarım, çevre tasarımı ve grafik tasarım")


def elemanlar():
    """Tasarım elemanları: nokta, çizgi, renk, doku, form."""
    ic = (yazi(180, 22, "TASARIM ELEMANLARI", 13, C["altin"], 800)
          + "<circle cx='36' cy='78' r='7' fill='#f5f6fa'/>" + yazi(36, 128, "nokta", 11, C["yazi"], 800)
          + "<circle cx='78' cy='66' r='4' fill='#8ee3d6'/><path d='M78 66 q22 -18 30 10 t32 4' fill='none' stroke='#8ee3d6' stroke-width='4' stroke-linecap='round'/>"
          + yazi(108, 128, "çizgi", 11, C["yazi"], 800)
          + "<rect x='160' y='56' width='16' height='40' fill='#ff7a33'/><rect x='176' y='56' width='16' height='40' fill='#f2c14e'/><rect x='192' y='56' width='16' height='40' fill='#6fb3ff'/>"
          + yazi(184, 128, "renk", 11, C["yazi"], 800)
          + "<rect x='226' y='56' width='44' height='40' rx='4' fill='none' stroke='#5fd08f' stroke-width='3'/>"
          + "".join(f"<path d='M{230 + i * 8} {60 + (i % 2) * 4} l6 6 m-6 10 l6 6 m-6 10 l6 6' stroke='#5fd08f' stroke-width='2'/>" for i in range(5))
          + yazi(248, 128, "doku", 11, C["yazi"], 800)
          + "<path d='M296 66 l20 -10 l20 10 v26 l-20 10 l-20 -10 z M296 66 l20 10 l20 -10 M316 76 v26' fill='none' stroke='#b197fc' stroke-width='3' stroke-linejoin='round'/>"
          + yazi(316, 128, "form", 11, C["yazi"], 800)
          + yazi(180, 166, "Ayrıca: şekil, valör (değer), yön, aralık,\nışık-gölge, oran, yazı, mekân", 10, C["soluk"], 600))
    return svg(360, 190, ic, "Nokta, çizgi, renk, doku ve form çizimleri")


def ilkeler():
    """Vurgu (odak noktası) ve zıtlık (karşıtlar yan yana)."""
    gri = "".join(f"<circle cx='{34 + (i % 4) * 30}' cy='{60 + (i // 4) * 30}' r='9' fill='#a3abc6'/>" for i in range(12) if i != 5)
    ic = (yazi(90, 22, "VURGU", 13, C["altin"], 800) + gri
          + "<circle cx='64' cy='90' r='13' fill='#ff7a33'/>"
          + yazi(90, 168, "Göz önce turuncuya gider:\nodak noktası", 11, C["soluk"], 700)
          + "<line x1='180' y1='18' x2='180' y2='182' stroke='#a3abc6' stroke-width='2' stroke-dasharray='5 6'/>"
          + yazi(270, 22, "ZITLIK", 13, C["mavi"], 800)
          + "<rect x='208' y='44' width='62' height='82' fill='#f5f6fa'/><rect x='270' y='44' width='62' height='82' fill='#0d1226' stroke='#f5f6fa' stroke-width='2'/>"
          + "<circle cx='239' cy='85' r='16' fill='#0d1226'/><circle cx='301' cy='85' r='8' fill='#f5f6fa'/>"
          + yazi(270, 168, "açık-koyu, büyük-küçük\nyan yana: güçlü etki", 11, C["soluk"], 700))
    return svg(360, 190, ic, "Vurgu: gri noktalar arasında turuncu nokta. Zıtlık: açık ve koyu yan yana")
