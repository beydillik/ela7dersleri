"""Matematik (mat1) okuma yaklaşımı — 2., 3., 4. tema u2k1–u4k4 (17 Kasım 2026, Kemal'le anlaşılan ilk dönem kapsamı).
Konu başına 3 ikiz çift, yalnız seçmeli sorularda (tuş takımı / sayı doğrusu sorularında sorunun kalbine dokunma kalır).
"Bu soru senden ne istiyor?" (NE) yalnız ikizlere. Testte sorulan sayı eskisi gibi (TESTSORU = havuz büyümeden önceki soru sayısı;
motor bunun 2'sini metinli sorulara ayırır).
İkiz kuralı: eşin doğru cevabı çeldiricilerden birinde (gerekirse eski sorunun çeldiricisi _eski ile değiştirildi); ipucu eşin cevabını söylemez.
Matematik'te anlatım kitaba bağlı değil; sayfalar kavram kartlarından (kaynaklar/mat1/unite2..4.md)."""
import json, re

def bosluk(x):
    """gen_mat1.py ile aynı: sayı ile birim arasına bölünmez boşluk."""
    return re.sub(r"(\d) (m|km|cm|dm|mm|mL|dL|cL|L|TL|°C|kat|birim|br|MB|metre|derece|g|gram|dakika)([²³]?)(?![\w²³])", "\\1\u00a0\\2\\3", x)

def _konu(konu): return json.load(open(f"public/mat1/konular/{konu}.json", encoding="utf-8"))

def _q(konu, bas):
    l = [q for q in _konu(konu)["sorular"] if q["soru"].startswith(bosluk(bas))]
    # Üretici çalıştıktan sonra ikiz de aynı ön ekle başlar; ikizler sona eklendiği için ilk eşleşme asıl sorudur.
    # İlk yazımda (17 Kasım 2026) her ön ek tek soruyla eşleşiyordu.
    assert l and (len(l) == 1 or all(q.get("ikiz") for q in l)), (konu, bas, len(l))
    return l[0]

def _S(konu, bas): return _q(konu, bas)["soru"]

def _R(s, eski, yeni):
    """Eski sorudan ikizini türetir (bölünmez boşluklar korunur)."""
    eski, yeni = bosluk(eski), bosluk(yeni)
    assert eski in s, (eski, s)
    return s.replace(eski, yeni, 1)

def _eski(konu, bas, degis, sayfa=None, ipucu=None, aciklama=None):
    """Eski sorunun bir çeldiricisini ikiz eşinin cevabıyla değiştirir (doğru şık ve öteki alanlar aynı kalır).
    sayfa: eski açıklamada sayfa yoksa sona eklenir (ör. "s. 172")."""
    q = _q(konu, bas)
    y = {k: q[k] for k in ("soru", "secenekler", "dogru", "ipucu", "aciklama", "kavram", "yardim", "svg") if k in q}
    if ipucu: y["ipucu"] = bosluk(ipucu)
    if aciklama: y["aciklama"] = bosluk(aciklama)
    if sayfa and not re.search(r"s\. \d+", y["aciklama"]): y["aciklama"] = y["aciklama"].rstrip() + f" ({sayfa})"
    degis = {bosluk(a): bosluk(b) for a, b in degis.items()}
    for a, b in degis.items(): assert a in q["secenekler"] or b in q["secenekler"], (konu, a)   # yeniden çalıştırınca zaten değişmiş olabilir
    y["secenekler"] = [degis.get(s, s) for s in q["secenekler"]]
    assert y["secenekler"][y["dogru"]] == q["secenekler"][q["dogru"]]
    return y

def Y(soru, secenekler, dogru, ipucu, aciklama, kavram, svg_kaynak=None):
    """Yeni ikiz sorusu; svg_kaynak = (konu, soru başı) → aynı grafik/çizim kullanılır."""
    e = {"soru": soru if "\u00a0" in soru else bosluk(soru), "secenekler": [bosluk(s) for s in secenekler], "dogru": dogru,
         "ipucu": bosluk(ipucu), "aciklama": bosluk(aciklama), "kavram": bosluk(kavram)}
    if svg_kaynak: e["svg"] = _q(*svg_kaynak)["svg"]
    return e

# ================= 2. TEMA =================
# u2k1 Cisimlerin Farklı Yönlerden Görünümleri
A1a = _S("u2k1", "Bir yapının ön tarafının tam karşısında"); A1b = _R(A1a, "ön tarafının", "sağ tarafının")
A1c = _S("u2k1", "Görseldeki yapıdan en üstteki küp çıkarılırsa"); A1d = _R(A1c, "değişmez", "değişir")
A1e = "Üst üste duran 2 küpe üstten bakınca kaç kare görürsün?"; A1f = "Yan yana duran 2 küpe üstten bakınca kaç kare görürsün?"
# u2k2 Prizma ve Açınımı
A2a = _S("u2k2", "Dikdörtgenler prizmasının kaç yüzü"); A2b = _R(A2a, "kaç yüzü", "bir yüzünün kaç köşesi")   # "kaç köşesi" Öğren'de tuş takımıyla soruluyor
A2c = _S("u2k2", "Açınımda aynı renkle boyanan"); A2d = _R(A2c, "aynı renkle boyanan", "yan yana duran")
A2e = _S("u2k2", "Hangisi dikdörtgenler prizması biçiminde değildir"); A2f = _R(A2e, "biçiminde değildir", "biçimindedir")
# u2k3 Yüzey Alanı
A3a = _S("u2k3", "Hangisi yüzey alanı için uygun"); A3b = _R(A3a, "uygun bir birimdir", "uygun bir birim değildir")
A3c = _S("u2k3", "Bir dikdörtgenler prizmasının birbirinden farklı üç yüzünün"); A3d = _R(A3c, "Yüzey alanı kaç", "Bu üç yüzün alanları toplamı kaç")
A3e = _S("u2k3", "Bir küpün bütün ayrıtlarının uzunlukları toplamı"); A3f = _R(A3e, "yüzey alanı kaç cm²'dir", "bir ayrıtı kaç cm'dir")
# u2k4 Hacim ve Birim Küp
A4a = _S("u2k4", "Hangisinde hacmi bulmamız"); A4b = _R(A4a, "hacmi bulmamız", "yüzey alanını bulmamız")
A4c = _S("u2k4", "Mert kutusuna"); A4d = _R(A4c, "hacmi daha büyük", "hacmi daha küçük")
A4e = _S("u2k4", "Cam bir kap"); A4f = _R(A4e, "hangisi daha uygun", "hangisi daha az uygun")
# u2k5 Dikdörtgenler Prizmasının Hacmi
A5a = _S("u2k5", "Bir ayrıtı 5 br olan küpün hacmi"); A5b = _R(A5a, "küpün hacmi kaç br³'tür", "küpün bir yüzünün alanı kaç br²'dir")
A5c = _S("u2k5", "Hangisi 18 eş birim küpten"); A5d = _R(A5c, "yapılmış bir prizmanın ayrıtları olamaz", "yapılabilen bir prizmanın ayrıtlarıdır")   # "…olabilir?" Öğren'de var
A5e = _S("u2k5", "Ayrıtları 3 br, 4 br ve 5 br olan bir prizmanın yalnızca"); A5f = _R(A5e, "2 katına çıkarıldı", "yarıya indirildi")
# u2k6 Hacim Ölçme Birimleri
A6a = _S("u2k6", "Bir yüzme havuzundaki"); A6b = _R(A6a, "Bir yüzme havuzundaki suyun hacmi", "Bir silginin hacmi")
A6c = _S("u2k6", "cm³'ü m³'e çevirirken"); A6d = _R(A6c, "cm³'ü m³'e", "m³'ü cm³'e")
A6e = _S("u2k6", "Her ayrıtı 1 m olan küpün"); A6f = _R(A6e, "1 m olan", "1 dm olan")
# u2k7 Sıvı Ölçme Birimleri
A7a = _S("u2k7", "1 L kaç cL"); A7b = _R(A7a, "kaç cL", "kaç dL")
A7c = _S("u2k7", "Hacmi 500 cm³ olan bir kap"); A7d = _R(A7c, "kaç mL su alır", "kaç L su alır")
A7e = _S("u2k7", "1,5 L, 1200 mL"); A7f = _R(A7e, "en az su alan", "en çok su alan")
# u2k8 Yüzey Alanı ve Hacim Problemleri
A8a = _S("u2k8", "Bir problemi çözmeye başlarken"); A8b = "Bir problemi çözerken en son ne yaparız?"
A8c = _S("u2k8", "Bir kolinin ayrıtları"); A8d = _R(A8c, "Kaç kutu sığar?", "Kolinin hacmi kaç dm³?")
A8e = _S("u2k8", "Tabanları aynı iki akvaryumdan")
A8f = "Su miktarları aynı olan iki akvaryumdan ikincisinin taban alanı birincinin taban alanının 2 katı. İkinci akvaryumdaki suyun yüksekliği için ne söylenebilir?"

# ================= 3. TEMA =================
B1a = _S("u3k1", "Bir sınıftaki öğrencilerin kardeş sayıları"); B1b = _R(B1a, "kardeş sayıları", "boy uzunlukları")
B1c = _S("u3k1", "Hangisinin cevabı kategorik"); B1d = _R(B1c, "kategorik", "nicel")
B1e = _S("u3k1", "Melis verilerini grafikle"); B1f = "Melis anket sorusunu hazırlayıp sınıftaki arkadaşlarına sordu ve cevapları tabloya yazdı. Melis hangi adımdadır?"
B2a = _S("u3k2", "“İzmir'deki ortaokulların"); B2b = _R(B2a, "evreni hangisidir", "örneklemi hangisi olabilir")
B2c = _S("u3k2", "Bir araştırmada evren"); B2d = _R(B2c, "temsil etmez", "temsil eder")
B2e = _S("u3k2", "Hangisi iyi bir araştırma sorusunun özelliği değildir"); B2f = _R(B2e, "özelliği değildir", "özelliğidir")
B3a = _S("u3k3", "Hangisi anket sorusudur"); B3b = _R(B3a, "anket sorusudur", "araştırma sorusudur")
B3c = _S("u3k3", "Veri toplama planında"); B3d = _R(B3c, "“Ne zaman?”", "“Nerede?”")
B3e = _S("u3k3", "Hangisinin cevabı kişisel veri içerir"); B3f = _R(B3e, "içerir?", "içermez?")
B4a = _S("u3k4", "Altın grafiğine göre en düşük"); B4b = _R(B4a, "en düşük", "en yüksek")
B4c = _S("u3k4", "Fidan grafiğinde en az uzama"); B4d = _R(B4c, "en az uzama", "en çok uzama")
B4e = _S("u3k4", "Hangi veri seti için çizgi grafiği"); B4f = _R(B4e, "çizgi grafiği", "nokta grafiği")
B5a = _S("u3k5", "9 aylık bir bebeğin baş çevresi"); B5b = _R(B5a, "baş çevresi 44,9 cm.", "baş çevresi 45,8 cm.")
B5c = _S("u3k5", "3, 4, 6, 7 verilerinin"); B5d = _R(B5c, "Hangisi doğrudur?", "Hangisi yanlıştır?")
B5e = _S("u3k5", "Bir pil üreticisi"); B5f = _R(B5e, "en az 10 saat", "en az 12 saat")
B6a = _S("u3k6", "Hangisi bir yayılım ölçüsüdür"); B6b = _R(B6a, "yayılım ölçüsüdür", "yayılım ölçüsü değildir")
B6c = _S("u3k6", "Veriler: 3, 5, 7, 9"); B6d = _R(B6c, "Ortalama mutlak sapma kaçtır?", "Uzaklıkların toplamı kaçtır?")
B6e = _S("u3k6", "Bir koşucunun süreleri"); B6f = _R(B6e, "birbirine çok yakın", "çok değişiyor")
B7a = _S("u3k7", "Ayşe'nin 5 sınav notunun"); B7b = _R(B7a, "Hangisi doğrudur?", "Hangisi yanlıştır?")
B7c = _S("u3k7", "Mehtap'ın sıcaklık tablosuna"); B7d = _R(B7c, "söylenebilir", "söylenemez")
B7e = _S("u3k7", "Bir dükkânın satışları"); B7f = _R(B7e, "art arda artmış", "art arda azalmış")
B8a = _S("u3k8", "Bir araştırmacı Türkiye'deki"); B8b = _R(B8a, "Hangisi doğrudur?", "Hangisi yanlıştır?")
B8c = _S("u3k8", "Ali'nin günlük adım sayısı"); B8d = _R(B8c, "6 gün art arda artıp 7. gün biraz düşmüş", "6 gün art arda azalıp 7. gün biraz artmış")
B8e = _S("u3k8", "Göl grafiğine göre hangisi"); B8f = _R(B8e, "doğrudur", "yanlıştır")

# ================= 4. TEMA =================
C1a = _S("u4k1", "C noktası simetri doğrusunun tam üzerinde"); C1b = _R(C1a, "tam üzerinde", "1 kare solunda")
C1c = _S("u4k1", "Bir dörtgenin görüntüsünü çizmek için"); C1d = "Bir dörtgenin görüntüsünü çizerken köşelerin görüntülerini bulduktan sonra ne yaparız?"
C1e = "Simetri doğrusu dikeyse bir nokta ile görüntüsü nasıl durur?"; C1f = "Simetri doğrusu yataysa bir nokta ile görüntüsü nasıl durur?"
C2a = _S("u4k2", "Hangisinin simetri doğrusu yoktur"); C2b = _R(C2a, "yoktur", "vardır")
C2c = _S("u4k2", "İkizkenar dik üçgeni uzun kenarına"); C2d = _R(C2c, "İkizkenar dik üçgeni uzun kenarına", "Dik üçgeni dik kenarına")
C2e = "Yarım dairenin kaç simetri doğrusu vardır?"; C2f = "Paralelkenarın kaç simetri doğrusu vardır?"   # eşkenar üçgen Öğren'de tuş takımıyla soruluyor
C3a = _S("u4k3", "Hangisi orta dikmenin özelliğidir"); C3b = _R(C3a, "özelliğidir", "özelliği değildir")
C3c = _S("u4k3", "AB 10 cm. Hangi pergel"); C3d = _R(C3c, "inşa edilebilir", "inşa edilemez")
C3e = _S("u4k3", "İnşada hangisi yapılmaz"); C3f = _R(C3e, "yapılmaz", "yapılır")
C4a = _S("u4k4", "Açıortay için hangisi doğrudur"); C4b = _R(C4a, "doğrudur", "yanlıştır")
C4c = _S("u4k4", "Bir doğru parçasının simetri doğrusunu inşa"); C4d = _R(C4c, "Bir doğru parçasının", "Bir açının")
C4e = "Açıortay 80°'lik bir açıyı ikiye ayırdı. Oluşan açılardan biri kaç derecedir?"
C4f = "Açıortay bir açıyı ikiye ayırdı. Oluşan açılardan biri 80°'dir. Bütün açı kaç derecedir?"

EKSORU = {
 "u2k1": [
  _eski("u2k1", "Bir yapının ön tarafının", {"Sağ": "Sol"}, aciklama="Ön ile arka karşılıklıdır; ön tarafın tam karşısında arka taraf vardır (s. 121–122)."),
  Y(A1b, ["Sol", "Arka", "Alt"], 0, "Yönler çiftler hâlindedir. Sağın eşini düşün.",
    "Sağ ile sol karşılıklıdır; sağ tarafın tam karşısında sol taraf vardır (s. 121–122).", "Altı Yön"),
  Y(A1d, ["Üstten görünüm", "Önden görünüm", "Alttan görünüm"], 1,
    "Üstteki küp kalkınca hangi yönden bakan biri bir karenin kaybolduğunu görür?",
    "Üstteki küp kalkınca önden bakınca o kare kaybolur. Altında küp olduğu için üstten ve alttan yine aynı kareler görünür (s. 124).",
    "Görünüm Kare Gösterir", ("u2k1", "Görseldeki yapıdan en üstteki küp")),
  Y(A1e, ["1", "2", "3"], 0, "Yukarıdan bakınca üstteki küp alttakini görmeni engeller mi?",
    "Üstteki küp alttakini örter; yukarıdan yalnız 1 kare görünür (s. 120–121).", "Görünüm Kare Gösterir"),
  Y(A1f, ["1", "2", "3"], 1, "İki küp de yerde mi? Yukarıdan bakınca her küpün üst yüzü görünür mü?",
    "İki küp de yerde; yukarıdan iki kare yan yana görünür (s. 120–121).", "Görünüm Kare Gösterir"),
 ],
 "u2k2": [
  Y(A2b, ["4", "6", "8"], 0, "Prizmanın her yüzü hangi şekil? O şeklin köşelerini say.",
    "Her yüz bir dikdörtgendir; dikdörtgenin 4 köşesi vardır (s. 128).", "Yüz, Ayrıt, Köşe"),
  _eski("u2k2", "Açınımda aynı renkle boyanan", {"Yan yana": "Komşu"}),
  Y(A2d, ["Komşu", "Karşılıklı", "Üst üste"], 0, "Açınımda bir kenarı ortak olan iki yüz, kutuda da o kenarda birleşir.",
    "Açınımda yan yana duran iki yüz, kutu kapanınca komşu olur (s. 127).", "Açınım Kapanır mı?"),
  Y(A2f, ["Ayakkabı kutusu", "Konserve kutusu", "Top"], 0, "Hangisinin 6 yüzünün hepsi dikdörtgen?",
    "Ayakkabı kutusunun 6 yüzü de dikdörtgendir; dikdörtgenler prizmasıdır (s. 128).", "Dikdörtgenler Prizması"),
 ],
 "u2k3": [
  Y(A3b, ["cm²", "m²", "cm"], 2, "Yüzey alanı bir alandır. Hangisi uzunluk birimi?",
    "cm bir uzunluk birimidir; yüzey alanı için uygun değildir (s. 129).", "Yüzey Alanı"),
  Y(A3d, ["90", "180", "60"], 0, "Soru yalnız bu üç yüzün toplamını istiyor. Verilen üç sayıyı topla.",
    "20 + 30 + 40 = 90 cm². Bu, üç farklı yüzün toplamıdır; yüzey alanı değildir (s. 129).", "Üç Çift Eş Yüz"),
  _eski("u2k3", "Bir küpün bütün ayrıtlarının", {"360": "5"}),
  Y(A3f, ["5", "150", "10"], 0, "Küpün kaç eş ayrıtı var? Toplamı ayrıt sayısına böl.",
    "Küpün 12 eş ayrıtı var: 60 ÷ 12 = 5 cm (s. 132).", "Küp"),
 ],
 "u2k4": [
  Y(A4b, ["Kutuyu paket kâğıdıyla kaplamak", "Kutuya kaç oyuncak sığacağını bulmak", "Kutunun bir kenarını ölçmek"], 0,
    "Kaplamak mı, doldurmak mı? Yüzey alanı kutunun dışıyla ilgilidir.",
    "Paket kâğıdı kutunun dışını kaplar; bunun için yüzey alanı gerekir. Hacim ise kutunun içine ne kadar şey sığacağını anlatır (s. 136).", "Kaplamak mı, Doldurmak mı?"),
  Y(A4d, ["Mert'in", "Elif'in", "İkisi eşit"], 0, "Tahtalar aynı. Her kutuya kaç tahta sığdığını bul ve karşılaştır.",
    "Mert 6 · 5 = 30, Elif 4 · 8 = 32 tahta. 30 < 32: Mert'in kutusu daha küçük (s. 136).", "Eş Nesnelerle Ölçme"),
  Y(A4f, ["Eş küpler", "Kibrit kutuları", "İkisi de aynı sonucu verir"], 1, "Hangisi kabı doldururken boşluk bıraktı?",
    "Kibrit kutuları arada boşluk bıraktı; boşluk kalınca hacim yanlış ölçülür (s. 138).", "Daha Uygun Birim"),
 ],
 "u2k5": [
  Y(A5b, ["25", "125", "15"], 0, "Küpün bir yüzü karedir. Karenin alanı: kenar × kenar.",
    "Bir yüz 5 br × 5 br'lik karedir: 5 · 5 = 25 br² (s. 142).", "Kare Prizma ve Küp"),
  Y(A5d, ["2 br, 2 br, 4 br", "1 br, 1 br, 9 br", "1 br, 2 br, 9 br"], 2, "Her birinde üç sayıyı çarp. Hangisi 18 ediyor?",
    "1 · 2 · 9 = 18. Öbürleri 2 · 2 · 4 = 16 ve 1 · 1 · 9 = 9 (s. 141).", "Aynı Hacim, Farklı Prizma"),
  _eski("u2k5", "Ayrıtları 3 br, 4 br ve 5 br olan bir prizmanın yalnızca", {"480": "30"}),
  Y(A5f, ["30", "120", "60"], 0, "Önce eski hacmi bul. Yükseklik yarıya inince hacim ne olur?",
    "Eski hacim 3 · 4 · 5 = 60 br³. Yükseklik yarıya inince hacim de yarıya iner: 60 ÷ 2 = 30 br³ (s. 143).", "Ayrıt Değişince Hacim"),
 ],
 "u2k6": [
  Y(A6b, ["m³", "cm³", "dm³"], 1, "Silgi küçük mü, büyük mü? Küçük cisme küçük birim.",
    "Silgi küçük bir cisimdir; küçük birim cm³ uygundur (s. 144).", "Hangi Birim Uygun?"),
  Y(A6d, ["Her basamakta 1000 ile çarparız.", "Her basamakta 1000'e böleriz.", "Her basamakta 10'a böleriz."], 0,
    "m³ büyük, cm³ küçük birim. Merdivende aşağı mı iniyoruz, yukarı mı çıkıyoruz?",
    "Aşağı iniyoruz: her basamakta 1000 ile çarparız (s. 146).", "Hacim Basamakları"),
  _eski("u2k6", "Her ayrıtı 1 m olan küpün", {"3 m": "1 dm³"}),
  Y(A6f, ["1 dm³", "1 m³", "1 dm²"], 0, "Ayrıtın birimine bak. Hacim küp birimle yazılır.",
    "1 dm · 1 dm · 1 dm = 1 dm³ (s. 146).", "Metreküp"),
 ],
 "u2k7": [
  Y(A7b, ["10", "100", "1000"], 0, "L → dL: bir basamak aşağı.",
    "Sıvıda her basamak 10 katıdır: 1 L = 10 dL (s. 148).", "Sıvı Basamakları"),
  _eski("u2k7", "Hacmi 500 cm³ olan bir kap", {"5000": "0,5"}),
  Y(A7d, ["0,5", "500", "5"], 0, "Önce cm³'ü mL'ye çevir. Sonra 1 L = 1000 mL'yi düşün.",
    "500 cm³ = 500 mL. 500 ÷ 1000 = 0,5 L (s. 147–148).", "1 mL = 1 cm³"),
  Y(A7f, ["140 cL", "1,5 L", "1200 mL"], 1, "Hepsini mL'ye çevir, sonra karşılaştır.",
    "1,5 L = 1500 mL, 140 cL = 1400 mL. En büyüğü 1500 mL, yani 1,5 L (s. 151).", "Aynı Birime Çevir, Sırala"),
 ],
 "u2k8": [
  _eski("u2k8", "Bir problemi çözmeye başlarken", {"Bütün sayıları toplarız.": "Hesaplayıp birimi yazarız."}, "s. 152–155"),
  Y(A8b, ["Hesaplayıp birimi yazarız.", "Ne verildiğini ve ne istendiğini buluruz.", "Bütün sayıları toplarız."], 0,
    "Dört sorunun sonuncusu.",
    "Problem iskeletinin son adımı: hesapla ve birimi yaz (s. 152–155).", "Problem İskeleti"),
  _eski("u2k8", "Bir kolinin ayrıtları", {"16": "32"}),
  Y(A8d, ["32", "4", "8"], 0, "Yalnız kolinin üç ayrıtını çarp.",
    "Koli 4 · 4 · 2 = 32 dm³. (Kaç kutu sığacağı ayrı bir sorudur.) (s. 152)", "Kaç Kutu Sığar?"),
  Y(A8f, ["Aynı kalır.", "Yarısı olur.", "2 katı olur."], 1, "Yükseklik = hacim ÷ taban alanı. Hangisi değişti: su mu, taban mı?",
    "Su aynı, taban alanı 2 katı: suyun yüksekliği yarıya iner (s. 154).", "Suyun Yüksekliği"),
 ],
 # ---------- 3. Tema ----------
 "u3k1": [
  Y(B1b, ["Sürekli veri", "Kategorik veri", "Kesikli veri"], 0, "Boyu sayar mıyız, ölçer miyiz?",
    "Boy ölçülür; iki ölçüm arasında sınırsız değer olabilir: sürekli veri (s. 163).", "Sürekli Veri"),
  Y(B1d, ["Hangi sporu seversin?", "Göz rengin ne?", "Boyun kaç cm?"], 2, "Cevabı sayı olan soruyu bul.",
    "Boy sayıyla söylenir (148 cm gibi): nicel veri (s. 163).", "Nicel Veri"),
  Y(B1f, ["Veri analizi", "Veri toplama", "Yorumlama ve karar verme"], 1, "Anket sorup cevapları kaydetmek hangi adımda yapılır?",
    "Anket sorup cevapları tabloya yazmak 2. adım olan veri toplamadır (s. 164).", "Araştırmanın 4 Adımı"),
 ],
 "u3k2": [
  _eski("u3k2", "“İzmir'deki ortaokulların", {"Bir okulun kütüphanesi": "İzmir'in her ilçesinden seçilen birkaç ortaokulun kütüphanesi"}),
  Y(B2b, ["İzmir'deki bütün ortaokulların kütüphaneleri", "İzmir'in her ilçesinden seçilen birkaç ortaokulun kütüphanesi", "Türkiye'deki bütün kütüphaneler"], 1,
    "Örneklem, en geniş gruptan seçilen daha küçük bir gruptur.",
    "Her ilçeden seçilen birkaç okul, İzmir'deki bütün ortaokulları temsil eden küçük bir gruptur: örneklem (s. 165).", "Örneklem"),
  Y(B2d, ["Sadece basketbol takımındaki öğrenciler", "Her sınıftan rastgele seçilen öğrenciler", "Sadece 7/A sınıfındaki öğrenciler"], 1,
    "Bütün okula benzeyen grubu bul.",
    "Her sınıftan rastgele seçilen öğrenciler bütün okula benzer; evreni temsil eder (s. 166).", "Örneklem Evreni Temsil Etmeli"),
  _eski("u3k2", "Hangisi iyi bir araştırma sorusunun özelliği değildir", {"Amacı nettir.": "Cevapları kişiden kişiye değişir."},
         ipucu="Herkes aynı cevabı verirse veri toplamanın anlamı kalır mı?", aciklama="Cevabı herkes için aynı olan soru araştırmaya uygun değildir (s. 165)."),
  Y(B2f, ["Cevabı herkes için aynıdır.", "Cevabı evet ya da hayırdır.", "Cevapları kişiden kişiye değişir."], 2,
    "Bilgi kartındaki iyi soru özelliklerini hatırla.",
    "İyi araştırma sorusunun cevapları kişiden kişiye değişir (s. 165).", "İyi Araştırma Sorusu"),
 ],
 "u3k3": [
  Y(B3b, ["Okulumuzdaki öğrencilerin uyku sürelerinin eğilimi nasıldır?", "Dün gece kaç saat uyudun?", "Uyku neden önemlidir?"], 0,
    "Bir grubun verileriyle cevaplanan soruyu bul.",
    "Araştırma sorusu bütün grubun verisiyle cevaplanır; çoğu zaman “… eğilimi nasıldır?” diye yazılır (s. 169).", "Anket Sorusu"),
  Y(B3d, ["Mezurayla", "Salı günü ilk derste", "Okul bahçesinde"], 2, "Yer bildiren cevabı bul.",
    "“Okul bahçesinde” yeri söyler (s. 169).", "Veri Toplama Planı"),
  Y(B3f, ["Ailenizin gelir düzeyi nasıldır?", "Ev adresiniz nedir?", "Bir yılda kaç ay vardır?"], 2,
    "Herkes için aynı olan, kişiye ait olmayan bilgiyi soran soruyu bul.",
    "Bir yıldaki ay sayısı herkes için aynıdır; kişiye ait bilgi değildir (s. 170).", "Kişisel Veri"),
 ],
 "u3k4": [
  _eski("u3k4", "Altın grafiğine göre en düşük", {"27 Ekim": "11 Kasım"}),
  Y(B4b, ["28 Ekim", "11 Kasım", "31 Ekim"], 1, "En üstteki noktayı bul.",
    "En üstteki nokta 11.11: 5 624 TL (s. 172).", "Çizgi Grafiği", ("u3k4", "Altın grafiğine göre en düşük")),
  _eski("u3k4", "Fidan grafiğinde en az uzama", {"1. ve 2. hafta": "2. ve 3. hafta"}, "s. 172"),
  Y(B4d, ["3. ve 4. hafta", "2. ve 3. hafta", "5. ve 6. hafta"], 1, "En dik parçayı bul ya da farkları hesapla.",
    "12 → 17: 5 cm. En dik parça burası (s. 172).", "Artış, Azalış, Sabit", ("u3k4", "Fidan grafiğinde en az uzama")),
  _eski("u3k4", "Hangi veri seti için çizgi grafiği", {"Sınıftaki öğrencilerin göz renkleri": "Sınıftaki öğrencilerin kardeş sayıları"}),
  Y(B4f, ["Bir bebeğin 12 ay boyunca her ay ölçülen boyu", "Sınıftaki öğrencilerin kardeş sayıları", "Bir şehrin 10 yıl boyunca her yıl ölçülen yağışı"], 1,
    "Nokta grafiğinde aynı değerler üst üste yığılır. Hangi veride değerler tekrar eder?",
    "Kardeş sayıları sayarak bulunur ve tekrar eder; noktalar yığılır. Zamanla değişen veriler için çizgi grafiği uygundur (s. 172).", "Hangi Grafik?"),
 ],
 "u3k5": [
  Y(B5b, ["P25 değerinde", "P50 değerinde", "P75'in üstünde"], 1, "Baş çevresini üç referans değeriyle tek tek karşılaştır.",
    "45,8 cm, 9 ayda P50 değerine eşit (s. 177).", "Referans Değeri"),
  Y(B5d, ["5 veri setinde olmadığı için temsil değeri olamaz.", "Ortalama doğru hesaplanmıştır.", "5 veri setinde olmasa da temsil değeri olabilir."], 0,
    "Önce ortalamayı kendin hesapla. Sonra temsil değeri veri setinde olmak zorunda mı, düşün.",
    "3 + 4 + 6 + 7 = 20, 20 ÷ 4 = 5: ortalama doğru. Temsil değeri veri setinde olmayabilir; “olamaz” demek yanlıştır (s. 176).", "Temsil Değeri Listede Olmayabilir"),
  _eski("u3k5", "Bir pil üreticisi", {"İddia kesinlikle yanlıştır.": "Ortalama iddiadaki sayıdan az; iddiayı desteklemiyor."}),
  Y(B5f, ["Ortalama iddiadaki sayıdan az; iddiayı desteklemiyor.", "Ortalama iddiayı destekliyor ama 9 saatlik bir pil var; daha çok veri gerekebilir.", "Veriler iddiayla ilgili değildir."], 0,
    "İddiadaki sayıyı ortalamayla karşılaştır.",
    "Ortalama 11 saat, iddia en az 12 saat: 11 < 12, ortalama iddiayı desteklemiyor (s. 176).", "Veriyle İddiayı Sınama"),
 ],
 "u3k6": [
  Y(B6b, ["Açıklık", "Ortalama mutlak sapma", "Ortanca"], 2, "Merkez ölçülerini hatırla: ortalama, ortanca, tepe değer.",
    "Ortanca bir merkez ölçüsüdür, yayılım ölçüsü değildir (s. 181).", "Yayılım Ölçüsü"),
  Y(B6d, ["8", "2", "4"], 0, "Yalnızca uzaklıkları topla. Bölme yok.",
    "3 + 1 + 1 + 3 = 8 (s. 181).", "Ortalama Mutlak Sapma"),
  _eski("u3k6", "Bir koşucunun süreleri", {"Çok büyük olur.": "Büyük olur."}),
  _eski("u3k6", "Veriler: 3, 5, 7, 9", {}, aciklama="3 + 1 + 1 + 3 = 8; 8 ÷ 4 = 2 (s. 181)."),
  Y(B6f, ["Küçük olur.", "Ortalamaya eşit olur.", "Büyük olur."], 2, "Veriler çok değişiyorsa ortalamadan uzaklıklar nasıl olur?",
    "Uzaklıklar büyük olur; sapma büyüktür. Koşucu dalgalıdır (s. 182).", "İstikrarlı ve Dalgalı"),
 ],
 "u3k7": [
  Y(B7b, ["Burak'ın notları daha çok değişmiştir.", "Ayşe'nin notları daha çok değişmiştir.", "Burak'ın notları birbirine daha yakındır."], 0,
    "Önce kimin açıklığının büyük olduğuna bak. Sonra her şıkkı tek tek kontrol et.",
    "Açıklığı küçük olan Burak'ın notları birbirine yakındır; daha çok değişen Burak değildir (s. 184).", "Değişkenliği Karşılaştırma"),
  _eski("u3k7", "Mehtap'ın sıcaklık tablosuna", {"Mehtap ilaç içmiştir.": "Mehtap ilaç içtiği için ateşi düşmüştür."}),
  Y(B7d, ["12.00'den 15.00'e ateşi düşmüştür.", "Mehtap ilaç içtiği için ateşi düşmüştür.", "15.00'te ateşi 37,5 °C'dir."], 1,
    "Burada yalnızca saat ve sıcaklık var. Hangisi burada olmayan bir bilgiye dayanıyor?",
    "Verilerde ilaçla ilgili bilgi yok; ateşin neden düştüğünü söyleyemeyiz (s. 185).", "Veriye Dayalı Yorum", ("u3k7", "Mehtap'ın sıcaklık tablosuna")),
  _eski("u3k7", "Bir dükkânın satışları", {"Satışlar yarın kesinlikle sıfır olacak.": "Satışlar azalmaya devam edebilir; kesin değildir."}, "s. 185"),
  Y(B7f, ["Satışlar azalmaya devam edebilir; kesin değildir.", "Satışlar artmaya devam edebilir; kesin değildir.", "Satışlar kesinlikle hep azalacak."], 0,
    "Eğilim hangi yönde? Tahmin kesin mi?",
    "Eğilim azalış; “devam edebilir” deriz. Tahmin kesin değildir (s. 185).", "Tahminin Sınırı"),
 ],
 "u3k8": [
  Y(B8b, ["Örneklem Türkiye'yi temsil etmeyebilir; sonuç dikkatle genellenmelidir.", "Sonuç bütün Türkiye için kesindir.", "Evren Türkiye'deki bütün öğrencilerdir."], 1,
    "Her şıkkı tek tek kontrol et. Bir okul bütün Türkiye'yi temsil eder mi?",
    "Tek okul Türkiye'deki bütün öğrencileri temsil etmeyebilir; sonuç kesin değildir (s. 190).", "Örneklemden Genellemek"),
  _eski("u3k8", "Ali'nin günlük adım sayısı", {"Adım sayısı hiç değişmemiştir.": "Adım sayısı azalma eğilimindedir."}, "s. 191"),
  Y(B8d, ["Adım sayısı sürekli azalmıştır.", "Adım sayısı azalma eğilimindedir.", "Adım sayısı artma eğilimindedir."], 1,
    "Arada bir artış varsa “sürekli” denir mi? Genel yön hangisi?",
    "7. gün artış var; doğru yorum “azalma eğiliminde” (s. 191).", "Eğilimi Doğru Söylemek"),
  Y(B8f, ["Su seviyesi her yıl azalmıştır.", "2016'dan 2024'e su seviyesi azalmıştır.", "Su seviyesi azalma eğilimindedir ama bazı yıllar artmıştır."], 0,
    "Her yıla tek tek bak: hiç artış var mı?",
    "2018 ve 2021'de küçük artışlar var; “her yıl azalmıştır” demek yanlıştır (s. 191).", "Eğilimi Doğru Söylemek", ("u3k8", "Göl grafiğine göre hangisi")),
 ],
 # ---------- 4. Tema ----------
 "u4k1": [
  Y(C1b, ["Doğrunun 1 kare solunda", "C ile aynı yerde", "Doğrunun 1 kare sağında"], 2,
    "Nokta ile görüntüsü doğrunun iki yanındadır ve doğruya eşit uzaklıktadır.",
    "C doğrunun 1 kare solunda; görüntüsü öbür yanda, 1 kare sağda (s. 205).", "Eşit Uzaklık"),
  _eski("u4k1", "Bir dörtgenin görüntüsünü çizmek için", {"Dörtgeni boyarız.": "Bu noktaları sırayla birleştiririz."}, aciklama="Önce her köşenin görüntüsünü buluruz (s. 204)."),
  Y(C1d, ["Her köşenin görüntüsünü buluruz.", "Bu noktaları sırayla birleştiririz.", "Simetri doğrusunu sileriz."], 1,
    "Köşeler bulundu. Şekli tamamlamak için ne kaldı?",
    "Köşelerin görüntüleri bulununca bu noktaları sırayla birleştiririz (s. 204).", "Köşe Köşe Yansıt"),
  Y(C1e, ["Aynı yatay hizada", "Aynı dikey hizada", "Çapraz hizada"], 0,
    "Simetri doğrusu, nokta ile görüntüsünü birleştiren parçayı dik keser.",
    "Doğru dikeyse onu dik kesen parça yataydır: nokta ile görüntüsü aynı yatay hizada durur (s. 205).", "Dik Ortalar"),
  Y(C1f, ["Aynı yatay hizada", "Aynı dikey hizada", "Çapraz hizada"], 1,
    "Simetri doğrusu, nokta ile görüntüsünü birleştiren parçayı dik keser.",
    "Doğru yataysa onu dik kesen parça dikeydir: nokta ile görüntüsü aynı dikey hizada durur (s. 205).", "Dik Ortalar"),
 ],
 "u4k2": [
  Y(C2b, ["Paralelkenar", "Çeşitkenar üçgen", "Dikdörtgen"], 2, "Katlayınca iki yarısı üst üste gelen şekli bul.",
    "Simetri doğrusu olan şekil katlanınca iki yarısı üst üste gelir (s. 205). Dikdörtgen, kenarlarının orta noktalarından katlanınca böyle olur.", "Birden Çok Simetri Doğrusu"),
  _eski("u4k2", "İkizkenar dik üçgeni uzun kenarına", {"Eşkenar üçgen": "İkizkenar üçgen"}),
  Y(C2d, ["Kare", "İkizkenar üçgen", "Çeşitkenar üçgen"], 1, "Üçgen ile görüntüsü dik kenarda birleşir. Yeni şeklin kaç kenarı olur, hangi kenarlar eş olur?",
    "Dik üçgen dik kenarına göre yansıtılınca iki eş kenarlı bir üçgen oluşur: ikizkenar üçgen (s. 208).", "Kenara Göre Yansıtma"),
  Y(C2e, ["0", "1", "2"], 1, "Yarım daireyi katlayarak iki yarısını üst üste getirebileceğin kaç yol var?",
    "Yarım daire simetrik bir şekildir; tek simetri doğrusu düz kenarını dik ortalar (s. 205).", "Simetrik Şekil"),
  Y(C2f, ["0", "1", "2"], 0, "Bilgi kartındaki simetrik olmayan şekilleri hatırla.",
    "Paralelkenar hiçbir doğrudan katlanınca üst üste gelmez: 0 simetri doğrusu (s. 205).", "Simetri Doğrusu Olmayan Şekiller"),
 ],
 "u4k3": [
  Y(C3b, ["Doğru parçasını dik keser ve tam ortadan böler.", "Doğru parçasına paraleldir.", "Üzerindeki her nokta iki uca eşit uzaktır."], 1,
    "Her şıkkı orta dikmenin tanımıyla karşılaştır.",
    "Orta dikme doğru parçasını dik keser; paralel değildir (s. 212–213).", "Orta Dikme"),
  Y(C3d, ["6 cm", "12 cm", "4 cm"], 2, "Açıklık AB'nin yarısından uzun olmalı. Yarısından kısa olan hangisi?",
    "Yarısı 5 cm; 4 cm yarıdan kısa, yaylar birbirine değmez (s. 212).", "Eş Çemberler"),
  Y(C3f, ["Cetvelle uzunluk ölçmek", "Açıölçerle açı ölçmek", "Pergelle yay çizmek"], 2, "İnşada ölçme yoktur.",
    "İnşada pergelle yay, ölçüsüz cetvelle düz çizgi çizilir (s. 211).", "Pergel ve Ölçüsüz Cetvel"),
 ],
 "u4k4": [
  Y(C4b, ["Açının köşesinden geçer.", "Açıyı iki eş açıya ayırır.", "Açının köşesinden geçmez."], 2,
    "Tanımı hatırla, sonra her şıkkı tek tek kontrol et.",
    "Açıortay açının köşesinden geçer; “geçmez” yanlıştır (s. 214).", "Açıortay"),
  Y(C4d, ["Köşegen", "Orta dikme", "Açıortay"], 2, "Şekil bir açı.",
    "Açının simetri doğrusu açıortaydır (s. 215).", "Orta Dikme mi, Açıortay mı?"),
  Y(C4e, ["40°", "80°", "160°"], 0, "Açıortay açıyı iki eş parçaya böler. Bütün açı verildi.",
    "80 ÷ 2 = 40°. Oluşan her açı bütün açının yarısıdır (s. 214).", "İki Eş Açı"),
  Y(C4f, ["160°", "40°", "80°"], 0, "Açıortay açıyı iki eş parçaya böler. Parçalardan biri verildi.",
    "İki eş açı: 80 + 80 = 160° (s. 214).", "İki Eş Açı"),
 ],
}

IKIZ = {
 "u2k1": [[A1a, A1b], [A1c, A1d], [A1e, A1f]], "u2k2": [[A2a, A2b], [A2c, A2d], [A2e, A2f]],
 "u2k3": [[A3a, A3b], [A3c, A3d], [A3e, A3f]], "u2k4": [[A4a, A4b], [A4c, A4d], [A4e, A4f]],
 "u2k5": [[A5a, A5b], [A5c, A5d], [A5e, A5f]], "u2k6": [[A6a, A6b], [A6c, A6d], [A6e, A6f]],
 "u2k7": [[A7a, A7b], [A7c, A7d], [A7e, A7f]], "u2k8": [[A8a, A8b], [A8c, A8d], [A8e, A8f]],
 "u3k1": [[B1a, B1b], [B1c, B1d], [B1e, B1f]], "u3k2": [[B2a, B2b], [B2c, B2d], [B2e, B2f]],
 "u3k3": [[B3a, B3b], [B3c, B3d], [B3e, B3f]], "u3k4": [[B4a, B4b], [B4c, B4d], [B4e, B4f]],
 "u3k5": [[B5a, B5b], [B5c, B5d], [B5e, B5f]], "u3k6": [[B6a, B6b], [B6c, B6d], [B6e, B6f]],
 "u3k7": [[B7a, B7b], [B7c, B7d], [B7e, B7f]], "u3k8": [[B8a, B8b], [B8c, B8d], [B8e, B8f]],
 "u4k1": [[C1a, C1b], [C1c, C1d], [C1e, C1f]], "u4k2": [[C2a, C2b], [C2c, C2d], [C2e, C2f]],
 "u4k3": [[C3a, C3b], [C3c, C3d], [C3e, C3f]], "u4k4": [[C4a, C4b], [C4c, C4d], [C4e, C4f]],
}

# Testte sorulan sayı eskisi gibi (havuz büyümeden önceki soru sayısı; 2'si metinli)
TESTSORU = {k: (11 if k == "u2k2" else 10) for k in IKIZ}   # 17 Kasım 2026 öncesi soru sayıları (u2k2 11, ötekiler 10)

NE = {
 A1a: ["Ön tarafın karşısındaki tarafı", "Sağ tarafın karşısındaki tarafı"], A1b: ["Sağ tarafın karşısındaki tarafı", "Ön tarafın karşısındaki tarafı"],
 A1c: ["Değişmeyen görünümü", "Değişen görünümü"], A1d: ["Değişen görünümü", "Değişmeyen görünümü"],
 A1e: ["Üst üste duran küplerin üstten görünümünü", "Yan yana duran küplerin üstten görünümünü"], A1f: ["Yan yana duran küplerin üstten görünümünü", "Üst üste duran küplerin üstten görünümünü"],
 A2a: ["Prizmanın yüz sayısını", "Bir yüzün köşe sayısını"], A2b: ["Bir yüzün köşe sayısını", "Prizmanın yüz sayısını"],
 A2c: ["Aynı renkli iki yüzün kutudaki yerini", "Yan yana duran iki yüzün kutudaki yerini"], A2d: ["Yan yana duran iki yüzün kutudaki yerini", "Aynı renkli iki yüzün kutudaki yerini"],
 A2e: ["Dikdörtgenler prizması olmayanı", "Dikdörtgenler prizması olanı"], A2f: ["Dikdörtgenler prizması olanı", "Dikdörtgenler prizması olmayanı"],
 A3a: ["Yüzey alanına uygun birimi", "Yüzey alanına uygun olmayan birimi"], A3b: ["Yüzey alanına uygun olmayan birimi", "Yüzey alanına uygun birimi"],
 A3c: ["Prizmanın yüzey alanını", "Üç yüzün alanları toplamını"], A3d: ["Üç yüzün alanları toplamını", "Prizmanın yüzey alanını"],
 A3e: ["Küpün yüzey alanını", "Küpün bir ayrıtının uzunluğunu"], A3f: ["Küpün bir ayrıtının uzunluğunu", "Küpün yüzey alanını"],
 A4a: ["Hacim gereken durumu", "Yüzey alanı gereken durumu"], A4b: ["Yüzey alanı gereken durumu", "Hacim gereken durumu"],
 A4c: ["Hacmi daha büyük olan kutuyu", "Hacmi daha küçük olan kutuyu"], A4d: ["Hacmi daha küçük olan kutuyu", "Hacmi daha büyük olan kutuyu"],
 A4e: ["Hacmi ölçmeye daha uygun olanı", "Hacmi ölçmeye daha az uygun olanı"], A4f: ["Hacmi ölçmeye daha az uygun olanı", "Hacmi ölçmeye daha uygun olanı"],
 A5a: ["Küpün hacmini", "Küpün bir yüzünün alanını"], A5b: ["Küpün bir yüzünün alanını", "Küpün hacmini"],
 A5c: ["18 küple yapılamayan prizmayı", "18 küple yapılabilen prizmayı"], A5d: ["18 küple yapılabilen prizmayı", "18 küple yapılamayan prizmayı"],
 A5e: ["Yükseklik 2 katı olunca yeni hacmi", "Yükseklik yarıya inince yeni hacmi"], A5f: ["Yükseklik yarıya inince yeni hacmi", "Yükseklik 2 katı olunca yeni hacmi"],
 A6a: ["Havuzdaki su için uygun birimi", "Silgi için uygun birimi"], A6b: ["Silgi için uygun birimi", "Havuzdaki su için uygun birimi"],
 A6c: ["cm³'ten m³'e çevirme yolunu", "m³'ten cm³'e çevirme yolunu"], A6d: ["m³'ten cm³'e çevirme yolunu", "cm³'ten m³'e çevirme yolunu"],
 A6e: ["Ayrıtı 1 m olan küpün hacmini", "Ayrıtı 1 dm olan küpün hacmini"], A6f: ["Ayrıtı 1 dm olan küpün hacmini", "Ayrıtı 1 m olan küpün hacmini"],
 A7a: ["1 L'nin kaç cL olduğunu", "1 L'nin kaç dL olduğunu"], A7b: ["1 L'nin kaç dL olduğunu", "1 L'nin kaç cL olduğunu"],
 A7c: ["Kabın aldığı suyu mL olarak", "Kabın aldığı suyu L olarak"], A7d: ["Kabın aldığı suyu L olarak", "Kabın aldığı suyu mL olarak"],
 A7e: ["En az su alan şişeyi", "En çok su alan şişeyi"], A7f: ["En çok su alan şişeyi", "En az su alan şişeyi"],
 A8a: ["Problemde ilk yapılacak işi", "Problemde en son yapılacak işi"], A8b: ["Problemde en son yapılacak işi", "Problemde ilk yapılacak işi"],
 A8c: ["Koliye sığan kutu sayısını", "Kolinin hacmini"], A8d: ["Kolinin hacmini", "Koliye sığan kutu sayısını"],
 A8e: ["Su 2 katı olunca suyun yüksekliğini", "Taban 2 katı olunca suyun yüksekliğini"], A8f: ["Taban 2 katı olunca suyun yüksekliğini", "Su 2 katı olunca suyun yüksekliğini"],
 B1a: ["Kardeş sayısının veri türünü", "Boy uzunluğunun veri türünü"], B1b: ["Boy uzunluğunun veri türünü", "Kardeş sayısının veri türünü"],
 B1c: ["Cevabı kategorik veri olan soruyu", "Cevabı nicel veri olan soruyu"], B1d: ["Cevabı nicel veri olan soruyu", "Cevabı kategorik veri olan soruyu"],
 B1e: ["Grafik çizip temsil değeri bulmanın adımını", "Anket sorup cevapları yazmanın adımını"], B1f: ["Anket sorup cevapları yazmanın adımını", "Grafik çizip temsil değeri bulmanın adımını"],
 B2a: ["Araştırmanın evrenini", "Araştırmanın örneklemini"], B2b: ["Araştırmanın örneklemini", "Araştırmanın evrenini"],
 B2c: ["Evreni temsil etmeyen grubu", "Evreni temsil eden grubu"], B2d: ["Evreni temsil eden grubu", "Evreni temsil etmeyen grubu"],
 B2e: ["İyi soruda olmayan özelliği", "İyi soruda olan özelliği"], B2f: ["İyi soruda olan özelliği", "İyi soruda olmayan özelliği"],
 B3a: ["Anket sorusu olanı", "Araştırma sorusu olanı"], B3b: ["Araştırma sorusu olanı", "Anket sorusu olanı"],
 B3c: ["“Ne zaman?” sorusunun cevabını", "“Nerede?” sorusunun cevabını"], B3d: ["“Nerede?” sorusunun cevabını", "“Ne zaman?” sorusunun cevabını"],
 B3e: ["Kişisel veri isteyen soruyu", "Kişisel veri istemeyen soruyu"], B3f: ["Kişisel veri istemeyen soruyu", "Kişisel veri isteyen soruyu"],
 B4a: ["Fiyatın en düşük olduğu günü", "Fiyatın en yüksek olduğu günü"], B4b: ["Fiyatın en yüksek olduğu günü", "Fiyatın en düşük olduğu günü"],
 B4c: ["En az uzadığı iki haftayı", "En çok uzadığı iki haftayı"], B4d: ["En çok uzadığı iki haftayı", "En az uzadığı iki haftayı"],
 B4e: ["Çizgi grafiğine uygun veriyi", "Nokta grafiğine uygun veriyi"], B4f: ["Nokta grafiğine uygun veriyi", "Çizgi grafiğine uygun veriyi"],
 B5a: ["44,9 cm'lik baş çevresinin yerini", "45,8 cm'lik baş çevresinin yerini"], B5b: ["45,8 cm'lik baş çevresinin yerini", "44,9 cm'lik baş çevresinin yerini"],
 B5c: ["Doğru olan yargıyı", "Yanlış olan yargıyı"], B5d: ["Yanlış olan yargıyı", "Doğru olan yargıyı"],
 B5e: ["“En az 10 saat” iddiasıyla ilgili doğru yorumu", "“En az 12 saat” iddiasıyla ilgili doğru yorumu"], B5f: ["“En az 12 saat” iddiasıyla ilgili doğru yorumu", "“En az 10 saat” iddiasıyla ilgili doğru yorumu"],
 B6a: ["Yayılım ölçüsü olanı", "Yayılım ölçüsü olmayanı"], B6b: ["Yayılım ölçüsü olmayanı", "Yayılım ölçüsü olanı"],
 B6c: ["Ortalama mutlak sapmayı", "Uzaklıkların toplamını"], B6d: ["Uzaklıkların toplamını", "Ortalama mutlak sapmayı"],
 B6e: ["Süreleri birbirine yakın koşucunun sapmasını", "Süreleri çok değişen koşucunun sapmasını"], B6f: ["Süreleri çok değişen koşucunun sapmasını", "Süreleri birbirine yakın koşucunun sapmasını"],
 B7a: ["Doğru olan yargıyı", "Yanlış olan yargıyı"], B7b: ["Yanlış olan yargıyı", "Doğru olan yargıyı"],
 B7c: ["Grafiğe göre söylenebilecek yorumu", "Grafiğe göre söylenemeyecek yorumu"], B7d: ["Grafiğe göre söylenemeyecek yorumu", "Grafiğe göre söylenebilecek yorumu"],
 B7e: ["Artan satışlarla ilgili uygun yorumu", "Azalan satışlarla ilgili uygun yorumu"], B7f: ["Azalan satışlarla ilgili uygun yorumu", "Artan satışlarla ilgili uygun yorumu"],
 B8a: ["Doğru olan yargıyı", "Yanlış olan yargıyı"], B8b: ["Yanlış olan yargıyı", "Doğru olan yargıyı"],
 B8c: ["Sonunda düşen adım sayısının yorumunu", "Sonunda artan adım sayısının yorumunu"], B8d: ["Sonunda artan adım sayısının yorumunu", "Sonunda düşen adım sayısının yorumunu"],
 B8e: ["Grafiğe göre doğru olan yargıyı", "Grafiğe göre yanlış olan yargıyı"], B8f: ["Grafiğe göre yanlış olan yargıyı", "Grafiğe göre doğru olan yargıyı"],
 C1a: ["Doğrunun üzerindeki noktanın görüntüsünü", "Doğrunun solundaki noktanın görüntüsünü"], C1b: ["Doğrunun solundaki noktanın görüntüsünü", "Doğrunun üzerindeki noktanın görüntüsünü"],
 C1c: ["Görüntü çizmenin ilk adımını", "Köşeler bulunduktan sonraki adımı"], C1d: ["Köşeler bulunduktan sonraki adımı", "Görüntü çizmenin ilk adımını"],
 C1e: ["Doğru dikeyken nokta ile görüntüsünün hizasını", "Doğru yatayken nokta ile görüntüsünün hizasını"], C1f: ["Doğru yatayken nokta ile görüntüsünün hizasını", "Doğru dikeyken nokta ile görüntüsünün hizasını"],
 C2a: ["Simetri doğrusu olmayan şekli", "Simetri doğrusu olan şekli"], C2b: ["Simetri doğrusu olan şekli", "Simetri doğrusu olmayan şekli"],
 C2c: ["Uzun kenara göre yansıtınca oluşan şekli", "Dik kenara göre yansıtınca oluşan şekli"], C2d: ["Dik kenara göre yansıtınca oluşan şekli", "Uzun kenara göre yansıtınca oluşan şekli"],
 C2e: ["Yarım dairenin simetri doğrusu sayısını", "Paralelkenarın simetri doğrusu sayısını"], C2f: ["Paralelkenarın simetri doğrusu sayısını", "Yarım dairenin simetri doğrusu sayısını"],
 C3a: ["Orta dikmenin bir özelliğini", "Orta dikmenin özelliği olmayanı"], C3b: ["Orta dikmenin özelliği olmayanı", "Orta dikmenin bir özelliğini"],
 C3c: ["İnşaya uygun pergel açıklığını", "İnşaya uygun olmayan pergel açıklığını"], C3d: ["İnşaya uygun olmayan pergel açıklığını", "İnşaya uygun pergel açıklığını"],
 C3e: ["İnşada yapılmayan işi", "İnşada yapılan işi"], C3f: ["İnşada yapılan işi", "İnşada yapılmayan işi"],
 C4a: ["Açıortayla ilgili doğru yargıyı", "Açıortayla ilgili yanlış yargıyı"], C4b: ["Açıortayla ilgili yanlış yargıyı", "Açıortayla ilgili doğru yargıyı"],
 C4c: ["Doğru parçası için çizilecek doğruyu", "Açı için çizilecek doğruyu"], C4d: ["Açı için çizilecek doğruyu", "Doğru parçası için çizilecek doğruyu"],
 C4e: ["Oluşan açılardan birinin ölçüsünü", "Bütün açının ölçüsünü"], C4f: ["Bütün açının ölçüsünü", "Oluşan açılardan birinin ölçüsünü"],
}

# İkizlerde farkı yaratan sözcük + soru kelimesi sarı (bölünmez boşluklar bosluk() ile)
_V = {
 A1a: ["ön tarafının", "hangi taraf"], A1b: ["sağ tarafının", "hangi taraf"],
 A1c: ["hangi görünüm değişmez"], A1d: ["hangi görünüm değişir"],
 A1e: ["Üst üste", "kaç kare"], A1f: ["Yan yana", "kaç kare"],
 A2a: ["kaç yüzü"], A2b: ["bir yüzünün kaç köşesi"],
 A2c: ["aynı renkle boyanan", "nasıl durur"], A2d: ["yan yana duran", "nasıl durur"],
 A2e: ["Hangisi", "değildir"], A2f: ["Hangisi", "biçimindedir"],
 A3a: ["Hangisi", "uygun bir birimdir"], A3b: ["Hangisi", "uygun bir birim değildir"],
 A3c: ["Yüzey alanı kaç"], A3d: ["alanları toplamı kaç"],
 A3e: ["yüzey alanı kaç"], A3f: ["bir ayrıtı kaç"],
 A4a: ["Hangisinde", "hacmi"], A4b: ["Hangisinde", "yüzey alanını"],
 A4c: ["Hangi kutunun", "daha büyük"], A4d: ["Hangi kutunun", "daha küçük"],
 A4e: ["hangisi daha uygun"], A4f: ["hangisi daha az uygun"],
 A5a: ["küpün hacmi kaç"], A5b: ["bir yüzünün alanı kaç"],
 A5c: ["Hangisi", "olamaz"], A5d: ["Hangisi", "yapılabilen"],
 A5e: ["2 katına çıkarıldı", "kaç br³"], A5f: ["yarıya indirildi", "kaç br³"],
 A6a: ["yüzme havuzundaki", "hangisidir"], A6b: ["silginin", "hangisidir"],
 A6c: ["cm³'ü m³'e", "ne yaparız"], A6d: ["m³'ü cm³'e", "ne yaparız"],
 A6e: ["1 m olan", "hangisidir"], A6f: ["1 dm olan", "hangisidir"],
 A7a: ["kaç cL'dir"], A7b: ["kaç dL'dir"],
 A7c: ["kaç mL"], A7d: ["kaç L"],
 A7e: ["en az su alan", "hangisidir"], A7f: ["en çok su alan", "hangisidir"],
 A8a: ["başlarken ilk", "ne yaparız"], A8b: ["en son", "ne yaparız"],
 A8c: ["Kaç kutu sığar"], A8d: ["Kolinin hacmi kaç"],
 A8e: ["2 katı su kondu", "ne söylenebilir"], A8f: ["taban alanı birincinin taban alanının 2 katı", "ne söylenebilir"],
 B1a: ["kardeş sayıları", "hangi veri türüdür"], B1b: ["boy uzunlukları", "hangi veri türüdür"],
 B1c: ["Hangisinin", "kategorik"], B1d: ["Hangisinin", "nicel"],
 B1e: ["grafikle gösterdi", "hangi adımdadır"], B1f: ["arkadaşlarına sordu", "hangi adımdadır"],
 B2a: ["evreni hangisidir"], B2b: ["örneklemi hangisi olabilir"],
 B2c: ["Hangisi", "temsil etmez"], B2d: ["Hangisi", "temsil eder"],
 B2e: ["Hangisi", "özelliği değildir"], B2f: ["Hangisi", "özelliğidir"],
 B3a: ["Hangisi", "anket sorusudur"], B3b: ["Hangisi", "araştırma sorusudur"],
 B3c: ["“Ne zaman?”", "hangisi olabilir"], B3d: ["“Nerede?”", "hangisi olabilir"],
 B3e: ["Hangisinin", "içerir"], B3f: ["Hangisinin", "içermez"],
 B4a: ["en düşük", "hangi gün"], B4b: ["en yüksek", "hangi gün"],
 B4c: ["en az uzama", "hangi iki hafta"], B4d: ["en çok uzama", "hangi iki hafta"],
 B4e: ["Hangi veri seti", "çizgi grafiği"], B4f: ["Hangi veri seti", "nokta grafiği"],
 B5a: ["44,9 cm", "hangisi doğrudur"], B5b: ["45,8 cm", "hangisi doğrudur"],
 B5c: ["Hangisi doğrudur"], B5d: ["Hangisi yanlıştır"],
 B5e: ["en az 10 saat", "Hangisi doğrudur"], B5f: ["en az 12 saat", "Hangisi doğrudur"],
 B6a: ["Hangisi", "yayılım ölçüsüdür"], B6b: ["Hangisi", "yayılım ölçüsü değildir"],
 B6c: ["Ortalama mutlak sapma kaçtır"], B6d: ["Uzaklıkların toplamı kaçtır"],
 B6e: ["birbirine çok yakın", "hangisi beklenir"], B6f: ["çok değişiyor", "hangisi beklenir"],
 B7a: ["Hangisi doğrudur"], B7b: ["Hangisi yanlıştır"],
 B7c: ["hangisi söylenebilir"], B7d: ["hangisi söylenemez"],
 B7e: ["art arda artmış", "Hangisi en uygun yorumdur"], B7f: ["art arda azalmış", "Hangisi en uygun yorumdur"],
 B8a: ["Hangisi doğrudur"], B8b: ["Hangisi yanlıştır"],
 B8c: ["art arda artıp", "biraz düşmüş", "Hangisi en doğru yorumdur"], B8d: ["art arda azalıp", "biraz artmış", "Hangisi en doğru yorumdur"],
 B8e: ["hangisi doğrudur"], B8f: ["hangisi yanlıştır"],
 C1a: ["tam üzerinde", "nerededir"], C1b: ["1 kare solunda", "nerededir"],
 C1c: ["çizmek için önce", "ne yaparız"], C1d: ["bulduktan sonra", "ne yaparız"],
 C1e: ["dikeyse", "nasıl durur"], C1f: ["yataysa", "nasıl durur"],
 C2a: ["Hangisinin", "yoktur"], C2b: ["Hangisinin", "vardır"],
 C2c: ["uzun kenarına", "hangi şekil oluşur"], C2d: ["dik kenarına", "hangi şekil oluşur"],
 C2e: ["Yarım dairenin", "kaç simetri doğrusu"], C2f: ["Paralelkenarın", "kaç simetri doğrusu"],
 C3a: ["Hangisi", "özelliğidir"], C3b: ["Hangisi", "özelliği değildir"],
 C3c: ["Hangi pergel açıklığıyla", "inşa edilebilir"], C3d: ["Hangi pergel açıklığıyla", "inşa edilemez"],
 C3e: ["hangisi yapılmaz"], C3f: ["hangisi yapılır"],
 C4a: ["hangisi doğrudur"], C4b: ["hangisi yanlıştır"],
 C4c: ["Bir doğru parçasının", "Ne çizeriz"], C4d: ["Bir açının", "Ne çizeriz"],
 C4e: ["Oluşan açılardan biri kaç derecedir"], C4f: ["Bütün açı kaç derecedir"],
}
# Öğren düzeltmesi (17 Kasım 2026): otomatik vurgu "nokta" kelimesinin başını ("no") sarı yapıyordu
_V[_konu("u3k4")["kavramlar"][1]["soru"]["soru"]] = ["nokta grafiğine uygun mu"]
VURGU = {s: [bosluk(p) for p in v] for s, v in _V.items()}

# Yeni soruların "sorunun kalbi" bölgeleri (eski soruların bölgeleri bolge.py'de)
_B = {
 A1b: ["tam karşısında hangi taraf vardır"], A1d: ["hangi görünüm değişir"],
 A1e: ["üstten bakınca kaç kare görürsün"], A1f: ["üstten bakınca kaç kare görürsün"],
 A2b: ["bir yüzünün kaç köşesi vardır"], A2d: ["kutu kapanınca nasıl durur"], A2f: ["dikdörtgenler prizması biçimindedir"],
 A3b: ["uygun bir birim değildir"], A3d: ["Bu üç yüzün alanları toplamı kaç cm²'dir"], A3f: ["bir ayrıtı kaç cm'dir"],
 A4b: ["yüzey alanını bulmamız gerekir"], A4d: ["Hangi kutunun hacmi daha küçük"], A4f: ["hangisi daha az uygun"],
 A5b: ["bir yüzünün alanı kaç br²'dir"], A5d: ["yapılabilen bir prizmanın ayrıtlarıdır"], A5f: ["Yeni hacim kaç br³"],
 A6b: ["en uygun birim hangisidir"], A6d: ["m³'ü cm³'e çevirirken ne yaparız"], A6f: ["küpün hacmi hangisidir"],
 A7b: "TUM", A7d: ["kaç L su alır"], A7f: ["en çok su alan hangisidir"],
 A8b: ["en son ne yaparız"], A8d: ["Kolinin hacmi kaç dm³"], A8f: ["suyun yüksekliği için ne söylenebilir"],
 B1b: ["hangi veri türüdür"], B1d: ["cevabı nicel veri olur"], B1f: ["Melis hangi adımdadır"],
 B2b: ["örneklemi hangisi olabilir"], B2d: ["Hangisi bu evreni temsil eder"], B2f: ["özelliğidir"],
 B3b: "TUM", B3d: ["sorusunun cevabı hangisi olabilir"], B3f: ["cevabı kişisel veri içermez"],
 B4b: ["en yüksek fiyat hangi gün"], B4d: ["en çok uzama hangi iki hafta arasında"], B4f: ["nokta grafiği en uygundur"],
 B5b: ["hangisi doğrudur"], B5d: ["Hangisi yanlıştır"], B5f: ["Hangisi doğrudur"],
 B6b: ["yayılım ölçüsü değildir"], B6d: ["Uzaklıkların toplamı kaçtır"], B6f: ["Ortalama mutlak sapması için hangisi beklenir"],
 B7b: ["Hangisi yanlıştır"], B7d: ["hangisi söylenemez"], B7f: ["Hangisi en uygun yorumdur"],
 B8b: ["Hangisi yanlıştır"], B8d: ["Hangisi en doğru yorumdur"], B8f: ["hangisi yanlıştır"],
 C1b: ["C′ nerededir"], C1d: ["bulduktan sonra ne yaparız"], C1e: ["nokta ile görüntüsü nasıl durur"], C1f: ["nokta ile görüntüsü nasıl durur"],
 C2b: ["simetri doğrusu vardır"], C2d: ["hangi şekil oluşur"], C2e: ["kaç simetri doğrusu vardır"], C2f: ["kaç simetri doğrusu vardır"],
 C3b: ["orta dikmenin özelliği değildir"], C3d: ["orta dikme inşa edilemez"], C3f: ["İnşada hangisi yapılır"],
 C4b: ["hangisi yanlıştır"], C4d: ["Ne çizeriz"], C4e: ["Oluşan açılardan biri kaç derecedir"], C4f: ["Bütün açı kaç derecedir"],
}
BOLGE = {s: (v if v == "TUM" else [bosluk(p) for p in v]) for s, v in _B.items()}
