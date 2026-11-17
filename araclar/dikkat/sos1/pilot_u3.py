"""Sosyal Bilgiler (sos1) okuma yaklaşımı — 3. ünite u3k1–u3k12 (18 Kasım 2026, Kemal'le anlaşılan ilk dönem kapsamı).
Konu başına 3 ikiz çift; "Bu soru senden ne istiyor?" (NE) yalnız ikizlere. Testte sorulan sayı eskisi gibi
(TESTSORU = havuz büyümeden önceki soru sayısı; motor bunun 2'sini metinli sorulara ayırır).
İkiz kuralı: eşin doğru cevabı çeldiricilerden birinde (gerekirse eski sorunun çeldiricisi _eski ile değiştirildi); ipucu eşin cevabını söylemez.
Bazı çiftlerde iki soru da eski sorudur (ör. cihan hâkimiyeti öncesi/sonrası).
Ayrıca 117 eski test sorusundan 116'sına `kavram` (İpucu'nun Hatırla kısmı): KAVRAM listesi; bir kez uygulamak için
`python3 araclar/dikkat/sos1/pilot_u3.py` (üretici bu bölümü çalıştırmaz). Bilgi ve sayfalar kitaptan (kaynaklar/sos1/unite3.md)."""
import json

def _konu(konu): return json.load(open(f"public/sos1/konular/{konu}.json", encoding="utf-8"))

def _q(konu, bas):
    l = [q for q in _konu(konu)["sorular"] if q["soru"].startswith(bas)]
    # Üretici çalıştıktan sonra ikiz de aynı ön ekle başlayabilir; ikizler sona eklendiği için ilk eşleşme asıl sorudur.
    assert l and (len(l) == 1 or all(q.get("ikiz") for q in l)), (konu, bas, len(l))
    return l[0]

def _S(konu, bas): return _q(konu, bas)["soru"]

def _R(s, eski, yeni):
    assert eski in s, (eski, s)
    return s.replace(eski, yeni, 1)

def _eski(konu, bas, degis, ipucu=None, aciklama=None, hatirla=None):
    """Eski sorunun bir çeldiricisini ikiz eşinin cevabıyla değiştirir (doğru şık aynı kalır); gerekirse ipucu/açıklama da."""
    q = _q(konu, bas)
    y = {k: q[k] for k in ("soru", "secenekler", "dogru", "ipucu", "aciklama", "kavram", "yardim") if k in q}
    for a, b in degis.items(): assert a in q["secenekler"] or b in q["secenekler"], (konu, a)   # yeniden çalıştırınca zaten değişmiş olabilir
    y["secenekler"] = [degis.get(s, s) for s in q["secenekler"]]
    assert y["secenekler"][y["dogru"]] == q["secenekler"][q["dogru"]]
    if ipucu: y["ipucu"] = ipucu
    if aciklama: y["aciklama"] = aciklama
    if hatirla: y["yardim"] = dict(y.get("yardim") or {}, hatirla=hatirla)   # İpucu'nun Hatırla kısmı kartın yerine bu metni gösterir
    return y

def Y(soru, secenekler, dogru, ipucu, aciklama, kavram, hatirla=None):
    e = {"soru": soru, "secenekler": secenekler, "dogru": dogru, "ipucu": ipucu, "aciklama": aciklama, "kavram": kavram}
    if hatirla: e["yardim"] = {"hatirla": hatirla}   # kartın açıklaması ikizin cevabını söylüyorsa
    return e

# ---------- kavram (soru sırasıyla; None = kavram kartıyla uyuşmuyor, boş kalır) ----------
KAVRAM = {
 "u3k1": ["Malazgirt ve Türk Beylikleri", "Orhan Bey ve I. Murad Dönemleri", "Orhan Bey ve I. Murad Dönemleri", "Fatih, Yavuz ve Kanuni Dönemleri",
          "Orhan Bey ve I. Murad Dönemleri", "Osmanlı Beyliği'nin Kuruluşu", "Tarih Bilinci ve Millî Kimlik", "Cihan Devleti", "Cihan Devleti", "Merkezî Otorite"],
 "u3k2": ["Fetih Politikası", "Fetih Politikası", "İskân Politikası", "İmar ve Yeni Şehirler", "İstimalet Politikası", "İstimalet Politikası",
          "İstimalet Politikası", "İstimalet Politikası"],
 "u3k3": ["Fethin Nedenleri", "Fethin Nedenleri", "Doğu Roma'nın Savunması", "Doğu Roma'nın Savunması", "Gemilerin Karadan Yürütülmesi",
          "Fethin Sonuçları", "Gemilerin Karadan Yürütülmesi", "Fethin Sonuçları", "Fethin Sonuçları", None],
 "u3k4": ["Yavuz Sultan Selim", "Memlük Devleti", "Mercidabık ve Ridaniye", "Mercidabık ve Ridaniye", "Mısır Seferi'nin Sonuçları",
          "Halifelik ve Kutsal Emanetler", "Barbaros Hayreddin Paşa", "Preveze Deniz Zaferi", "Preveze Deniz Zaferi", "Preveze Deniz Zaferi"],
 "u3k5": ["Sömürgecilik", "Deniz Seyahatlerinin Nedenleri", "Deniz Seyahatlerinin Nedenleri", "Ümit Burnu ve Hindistan Yolu", "Amerika ve Dünya Turu",
          "Amerika ve Dünya Turu", "Avrupa İçin Sonuçlar", "Yerli Halklar İçin Sonuçlar", "Osmanlı İçin Sonuçlar", "Osmanlı İçin Sonuçlar"],
 "u3k6": ["Rönesans", "Rönesans'ın Nedenleri", "Rönesans'ın Sonuçları", "Rönesans'ın Sonuçları", "Martin Luther", "Martin Luther",
          "Aydınlanma Çağı", "Aydınlanma Çağı", "Osmanlı'ya Etkileri", "Osmanlı'ya Etkileri"],
 "u3k7": ["Sanayi İnkılabı", "Sanayi İnkılabı", "Sanayi İnkılabı", "İşçi Sınıfı", "Sanayi İnkılabı ve Osmanlı", "Fransız İhtilali",
          "Fransız İhtilali", "İhtilalin Sonuçları", "Fransız İhtilali ve Osmanlı", "Fransız İhtilali ve Osmanlı"],
 "u3k8": ["Lale Devri", "Batı ile Yakın İlişkiler", "Lale Devri", "Batı ile Yakın İlişkiler", "Tulumbacılar Ocağı", "Tulumbacılar Ocağı",
          "Nizâm-ı Cedîd", "III. Selim'in Diğer Yenilikleri", "III. Selim'in Diğer Yenilikleri", "Nizâm-ı Cedîd Ordusu"],
 "u3k9": ["II. Mahmud", "Vaka-i Hayriye", "Vaka-i Hayriye", "Nazırlıklar", "II. Mahmud", "Tanzimat Fermanı", "Tanzimat Fermanı",
          "Takvim-i Vekayi", "Sanayileşme Çabaları", "Türk Modası"],
 "u3k10": ["Külliye", "Külliye", "Osmanlı'nın Yaşayan İzleri", "Merkez ve Taşra Yönetimi", "Padişah", "Divan-ı Hümayun", "Divan Üyeleri",
           "Divan Üyeleri", "Divan Üyeleri"],
 "u3k11": ["Sıbyan Mektebi", "Medrese", "Enderun Mektebi", "Batı Tarzı Okullar", "Batı Tarzı Okullar", "Meslek Okulları", "Şer'i ve Örfi Hukuk",
           "Kanunname", "Mecelle ve Kanun-ı Esasi", "Mecelle ve Kanun-ı Esasi"],
 "u3k12": ["Osmanlı Mimarisi", "Süsleme Sanatları", "Mehter Takımı", "Günlük Hayat", "Günlük Hayat", "Vakıf", "Vakıf", "Ahilik", "Lonca", "Vakıf"],
}

if __name__ == "__main__":   # yalnız elle çalıştırınca: eski test sorularına kavram yazar (üretici exec ile okur, burası çalışmaz)
    n = 0
    for k, l in KAVRAM.items():
        yol = f"public/sos1/konular/{k}.json"; d = json.load(open(yol, encoding="utf-8"))
        adlar = {x["ad"] for x in d["kavramlar"]}
        for q, kv in zip(d["sorular"], l):
            if kv: assert kv in adlar, (k, kv); q["kavram"] = kv; n += 1
        open(yol, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
    print("kavram yazıldı:", n)

# ---------- ikiz soruları ----------
D1a = _S("u3k1", "İslamiyet'ten önce Türk devletlerinin"); D1b = _S("u3k1", "İslamiyet'in kabulünden sonra")
D1c = _S("u3k1", "Hangi padişah döneminde kutsal"); D1d = "Hangi padişah döneminde İstanbul fethedilip başkent oldu?"
D1e = "Orhan Bey Dönemi'nde hangi şehir fethedilip başkent oldu?"; D1f = "I. Murad Dönemi'nde hangi şehir fethedilip başkent oldu?"
D2a = _S("u3k2", "Hangisi iskân politikasının"); D2b = "Hangisi iskân politikasının amaçlarından biridir?"
D2c = _S("u3k2", "Hangisi istimalet politikasının"); D2d = "Hangisi istimalet politikasının amaçlarından biri DEĞİLDİR?"
D2e = _S("u3k2", "İstimalet politikası fetihten ÖNCE"); D2f = _R(D2e, "ÖNCE", "SONRA")
D3a = _S("u3k3", "Doğu Roma'nın Anadolu'daki"); D3b = "İstanbul'un ticaret yolları üzerinde bulunması fethin hangi nedenidir?"
D3c = _S("u3k3", "Aşağıdakilerden hangisi Osmanlı'nın fetih için"); D3d = _R(D3c, "biri DEĞİLDİR", "biridir")
D3e = _S("u3k3", "Osmanlı ordusu İstanbul önüne"); D3f = "Osmanlı ordusu son büyük hücuma hangi tarihte başladı?"
D4a = _S("u3k4", "Aşağıdaki savaşlardan hangisi en önce"); D4b = _R(D4a, "en önce", "en son")
D4c = _S("u3k4", "Aşağıdakilerden hangisi Mısır Seferi'nin ekonomik"); D4d = _R(D4c, "ekonomik", "dinî")
D4e = _S("u3k4", "Mısır Seferi'nden önce Yavuz"); D4f = "Mısır Seferi ile Osmanlı hangi sınırını güvence altına aldı?"
D5a = _S("u3k5", "Bartolomeu Dias"); D5b = "Kristof Kolomb 1492'de nereye ulaştı?"
D5c = _S("u3k5", "Ulaşılan toprakların yeni bir kıta"); D5d = "Ümit Burnu'nu geçerek Hindistan'a ulaşan denizci kimdir?"
D5e = _S("u3k5", "Deniz seyahatlerinden sonra Osmanlı liman"); D5f = _R(D5e, "Osmanlı liman şehirlerine", "Atlas Okyanusu kıyısındaki liman kentlerine")
D6a = _S("u3k6", "Rönesans'la birlikte kilisenin"); D6b = "Reform hareketleriyle birlikte kralların otoritesine ne oldu?"
D6c = _S("u3k6", "Reform hareketleri ilk olarak"); D6d = _R(D6c, "Reform hareketleri", "Rönesans")
D6e = _S("u3k6", "Hangisi Reform hareketlerinin sonuçlarından"); D6f = "Hangisi Rönesans'ın sonuçlarından biridir?"
D7a = _S("u3k7", "Sanayi İnkılabı'ndan önce üretim"); D7b = "Sanayi İnkılabı'ndan sonra üretim nerede yapılmaya başlandı?"
D7c = _S("u3k7", "1856'da gayrimüslimlere"); D7d = "1839'da herkesin can ve mal güvenliğinin korunacağını açıklayan belge hangisidir?"
D7e = _S("u3k7", "İhtilalden önce Fransa'da vergi"); D7f = "İhtilalden önce Fransa'da kimler vergi vermiyordu?"
D8a = _S("u3k8", "Lale Devri'nde Batı ile yakın"); D8b = "Nizâm-ı Cedîd adlı yenilik çalışmalarını başlatan padişah kimdir?"
D8c = _S("u3k8", "Islahatların giderlerini"); D8d = "Yangınlarla mücadele etmek için ne kuruldu?"
D8e = _S("u3k8", "Lale Devri'nde İstanbul'da hangi"); D8f = "III. Selim Dönemi'nde Azatlı ve Beykoz'da hangi yapılar kuruldu?"
D9a = _S("u3k9", "Subay yetiştirmek için II. Mahmud"); D9b = _R(D9a, "Subay", "Doktor")
D9c = _S("u3k9", "Tanzimat Dönemi'nde yayımlanan özel"); D9d = "1831'de çıkarılan ilk resmî gazete hangisidir?"
D9e = _S("u3k9", "II. Mahmud hangi yıl"); D9f = "Tanzimat Fermanı hangi yıl ilan edildi?"
DAa = _S("u3k10", "Kadı ve müderrislerin"); DAb = "Mali işleri hangi Divan üyesi yürütürdü?"
DAc = _S("u3k10", "Diğer devletlerle yapılan antlaşmaların"); DAd = "Kararların İslam dinine uygunluğu konusunda kim fetva verirdi?"
DAe = _S("u3k10", "Saray ve Divan-ı Hümayun'un"); DAf = "Ülkenin merkezden uzak eyalet ve sancaklarının yönetimine ne denir?"
DBa = _S("u3k11", "Mühendishane-i Berri-i Hümayun'un"); DBb = _R(DBa, "Berri", "Bahri")
DBc = _S("u3k11", "Rüştiyeler hangi düzeyde"); DBd = _R(DBc, "Rüştiyeler", "İdadîler")
DBe = _S("u3k11", "Osmanlı'da adalet işlerini kim"); DBf = "Osmanlı'da gençlere başlangıçta meslek ve ahlakı kim öğretiyordu?"
DCa = _S("u3k12", "Hangisi loncaların görevlerinden"); DCb = "Hangisi loncaların görevlerinden biri değildir?"
DCc = _S("u3k12", "Ahilikte \"kapısı açık olmalı\""); DCd = _R(DCc, "\"kapısı açık olmalı\"", "\"eli açık olmalı\"")
DCe = _S("u3k12", "Vakıf anlayışının temelleri"); DCf = "Vakıf anlayışı hangi devlet zamanında altın çağını yaşadı?"

EKSORU = {
 "u3k1": [
  _eski("u3k1", "İslamiyet'ten önce Türk devletlerinin", {"Yeni okyanuslar keşfetmek": "İslam dinini yaymak"}),
  _eski("u3k1", "İslamiyet'in kabulünden sonra", {"Fabrika kurma düşüncesi": "Dünyada adalet ve düzeni sağlama düşüncesi"},
        ipucu="Soru önceden var olan amacı değil, sonradan eklenen düşünceyi soruyor."),
  _eski("u3k1", "Hangi padişah döneminde kutsal", {"Osman Bey": "Fatih Sultan Mehmed"}, hatirla="Mısır'ı fetheden padişah döneminde kutsal toprakların yönetimi Osmanlı'ya geçti."),
  Y(D1d, ["Osman Bey", "Fatih Sultan Mehmed", "Yavuz Sultan Selim"], 1, "Fethi 1453'te gerçekleştiren padişahı düşün.",
    "Fatih Sultan Mehmed 1453'te İstanbul'u fethetti ve şehir başkent oldu (s. 89).", "Fatih, Yavuz ve Kanuni Dönemleri",
    hatirla="İstanbul 1453'te fethedildi ve Osmanlı'nın başkenti oldu."),
  Y(D1e, ["Bursa", "Edirne", "İstanbul"], 0, "Orhan Bey, I. Murad'dan önce padişah oldu. Önce fethedilen başkenti düşün.",
    "Orhan Bey Dönemi'nde Bursa fethedildi ve başkent oldu (s. 89).", "Orhan Bey ve I. Murad Dönemleri",
    hatirla="Orhan Bey ve I. Murad dönemlerinde fethedilen iki şehir sırayla başkent oldu."),
  Y(D1f, ["Bursa", "Edirne", "İstanbul"], 1, "I. Murad, Orhan Bey'den sonra padişah oldu. Rumeli'ye geçildikten sonra fethedilen başkenti düşün.",
    "I. Murad Dönemi'nde Edirne fethedildi ve başkent oldu (s. 89).", "Orhan Bey ve I. Murad Dönemleri",
    hatirla="Orhan Bey ve I. Murad dönemlerinde fethedilen iki şehir sırayla başkent oldu."),
 ],
 "u3k2": [
  _eski("u3k2", "Hangisi iskân politikasının", {}, aciklama="İskânla kalıcı hâkimiyet ve güvenlik amaçlandı; fethedilen yerleri boşaltmak amaç değildi (s. 94)."),
  Y(D2b, ["Fethedilen yerleri boşaltmak", "Konargöçer toplulukları yerleşik hayata geçirmek", "Ticareti durdurmak"], 1,
    "İskân “yerleştirmek” demek. Hangi seçenek yerleştirmeyle ilgili?",
    "İskânın amaçlarından biri konargöçer toplulukları yerleşik hayata geçirmektir (s. 94).", "İskân Politikası"),
  Y(D2d, ["Halkın can, mal ve inanç güvenliğini korumak", "Farklı dinlere ve kültürlere baskı yapmak", "Yerel halkın gönlünü kazanmak"], 1,
    "İstimalet halkla barışı amaçlar. Hangi seçenek barışa uymuyor?",
    "İstimalet farklı din ve kültürlere saygı göstermeyi amaçlar; baskı yapmak amacı değildir (s. 95).", "İstimalet Politikası"),
  _eski("u3k2", "İstimalet politikası fetihten ÖNCE", {"Halk bölgeden çıkarıldı": "Adaletli ve anlayışlı bir yönetim sergilendi"},
        aciklama="İstimalet politikası fetihten önce halkı yeni yönetime alıştırmak şeklinde uygulandı (s. 95)."),
  Y(D2f, ["Halk yeni yönetime alıştırıldı", "Adaletli ve anlayışlı bir yönetim sergilendi", "Vergiler artırıldı"], 1,
    "İstimalet Politikası kartının ek kısmında “fetihten sonra” ile başlayan kısmı bul.",
    "Fetihten sonra adaletli ve anlayışlı bir yönetim sergilendi (s. 95).", "İstimalet Politikası"),
 ],
 "u3k3": [
  Y(D3b, ["Ekonomik", "Siyasi", "Dinî"], 0, "Ticaret yolu para kazanmakla mı, devletler arası ilişkilerle mi ilgili?",
    "Ticaret yolları üzerinde bulunmak ekonomik bir nedendir (s. 97).", "Fethin Nedenleri"),
  Y(D3d, ["Surları onarmak", "Haliç girişine zincir çekmek", "Şahi topları döktürmek"], 2,
    "Önce her hazırlığı hangi tarafın yaptığını düşün: Osmanlı mı, Doğu Roma mı?",
    "Şahi toplarını Osmanlı, Macar usta Urban'a döktürdü. Surları onarmak Doğu Roma'nın savunmasıydı (s. 98–99).", "Şahi Topları"),
  Y(D3f, ["29 Mayıs 1453", "6 Nisan 1453", "1451"], 0, "Fethin Sonuçları kartının ilk cümlesine bak.",
    "Son büyük hücum 29 Mayıs 1453'te başladı ve şehir fethedildi (s. 101).", "Fethin Sonuçları"),
 ],
 "u3k4": [
  Y(D4b, ["Ridaniye", "Mercidabık", "Turnadağ"], 0, "Üç savaşın yıllarını sırala; en büyük yıl hangisi?",
    "Turnadağ 1515, Mercidabık 1516, Ridaniye 1517: en son Ridaniye (s. 103).", "Mercidabık ve Ridaniye"),
  Y(D4d, ["Halife unvanı alındı.", "Mısır'dan alınan vergiler ekonomiyi güçlendirdi.", "Güney sınırları güvenceye alındı."], 0,
    "Din ve İslam dünyasıyla ilgili olan seçeneği bul.",
    "Halife unvanının Osmanlı padişahlarına geçmesi dinî bir sonuçtur (s. 104).", "Halifelik ve Kutsal Emanetler"),
  _eski("u3k4", "Mısır Seferi'nden önce Yavuz", {"Kuzey sınırını": "Güney sınırını"}),
  Y(D4f, ["Doğu sınırını", "Güney sınırını", "Batı sınırını"], 1, "Mısır, Osmanlı'nın hangi yönündeydi?",
    "Mısır Seferi ile Suriye, Mısır ve Arap Yarımadası katıldı; güney sınırları güvence altına alındı (s. 104).", "Mısır Seferi'nin Sonuçları"),
 ],
 "u3k5": [
  Y(D5b, ["Amerika'ya", "Ümit Burnu'na", "Avustralya'ya"], 0, "Kolomb vardığı yeri başka bir yer sanmıştı. Gerçekte neredeydi?",
    "Kolomb 1492'de Amerika'nın doğusundaki adalara ulaştı ama burayı Hindistan sandı (s. 114).", "Amerika ve Dünya Turu"),
  Y(D5d, ["Kristof Kolomb", "Vasco da Gama", "Amerigo Vespucci"], 1, "Ümit Burnu ve Hindistan Yolu kartının ek kısmına bak.",
    "Vasco da Gama 1497'de Ümit Burnu'nu geçerek deniz yoluyla Hindistan'a ulaştı (s. 114).", "Ümit Burnu ve Hindistan Yolu"),
  _eski("u3k5", "Deniz seyahatlerinden sonra Osmanlı liman", {"Daha da büyüdüler": "Geliştiler"}),
  Y(D5f, ["Eski önemlerini yitirdiler", "Geliştiler", "Küçüldüler"], 1, "Yeni ticaret yolları hangi okyanustan geçiyordu?",
    "Atlas Okyanusu kıyısındaki ticaret yolları ve liman kentleri gelişti (s. 115).", "Avrupa İçin Sonuçlar"),
 ],
 "u3k6": [
  Y(D6b, ["Azaldı", "Arttı", "Hiç değişmedi"], 1, "Martin Luther kartındaki sonuçlarda Papa ve krallar ayrı ayrı geçiyor.",
    "Reform sonucunda kralların otoritesi güçlendi (s. 119).", "Martin Luther"),
  Y(D6d, ["İtalya", "Almanya", "İspanya"], 0, "Rönesans kartının ek kısmının ilk cümlesine bak.",
    "Rönesans İtalya'da başladı, sonra başka ülkelere yayıldı (s. 116).", "Rönesans"),
  _eski("u3k6", "Hangisi Reform hareketlerinin sonuçlarından", {"Papa'nın gücü arttı": "Modern bilimlerin temelleri atıldı"}),
  Y(D6f, ["Yeni mezhepler ortaya çıktı", "Modern bilimlerin temelleri atıldı", "Kilisenin etkisi arttı"], 1,
    "Rönesans'ın Sonuçları kartında akıl, deney ve gözlemle ilgili cümleyi bul.",
    "Rönesans ile akıl, deney ve gözlem öne çıktı; modern bilimlerin temelleri atıldı (s. 117).", "Rönesans'ın Sonuçları"),
 ],
 "u3k7": [
  _eski("u3k7", "Sanayi İnkılabı'ndan önce üretim", {"Büyük fabrikalarda": "Makineli fabrikalarda"}),
  Y(D7b, ["Küçük atölyelerde", "Makineli fabrikalarda", "Gemilerde"], 1, "Buhar makinesi üretimi nereye taşıdı?",
    "Küçük atölyelerin yerini makinelerin kullanıldığı fabrikalar aldı (s. 121).", "Sanayi İnkılabı"),
  Y(D7d, ["Islahat Fermanı", "Tanzimat Fermanı", "Kanun-i Esasi"], 1, "Kartın çizimindeki ilk yılı düşün.",
    "1839'da Tanzimat Fermanı ile herkesin can ve mal güvenliğinin korunacağı açıklandı (s. 124).", "Fransız İhtilali ve Osmanlı"),
  _eski("u3k7", "İhtilalden önce Fransa'da vergi", {"Din görevlilerinin": "Soyluların ve din görevlilerinin"},
        ipucu="Fransız İhtilali kartının ek kısmında “vergi yükü” sözünü bul.", aciklama="Vergi yükü büyük ölçüde halkın üzerindeydi (s. 123)."),
  Y(D7f, ["Halk", "Soylular ve din görevlileri", "Yalnızca kral"], 1, "Fransız İhtilali kartının ek kısmında vergiyle ilgili cümleyi bul.",
    "Soylular ve din görevlileri vergi vermiyordu (s. 123).", "Fransız İhtilali"),
 ],
 "u3k8": [
  Y(D8b, ["III. Selim", "II. Mahmud", "III. Ahmed"], 0, "Nizâm-ı Cedîd kartının ilk cümlesine bak.",
    "Nizâm-ı Cedîd, Sultan III. Selim'in başlattığı yenilik çalışmalarının adıdır (s. 126).", "Nizâm-ı Cedîd"),
  Y(D8d, ["Tulumbacılar Ocağı", "Kara Mühendishanesi", "İrâd-ı Cedîd Hazinesi"], 0, "Osmanlı'nın ilk itfaiye teşkilatını hatırla.",
    "1720'de kurulan Tulumbacılar Ocağı Osmanlı'nın ilk itfaiye teşkilatıdır (s. 126).", "Tulumbacılar Ocağı"),
  _eski("u3k8", "Lale Devri'nde İstanbul'da hangi", {"Fabrikalar ve tersaneler": "Fabrikalar"}),
  Y(D8f, ["Kütüphaneler, çeşmeler, köşkler", "Fabrikalar", "Demir yolları ve köprüler"], 1,
    "III. Selim'in Diğer Yenilikleri kartında kumaş ve kâğıtla ilgili cümleyi bul.",
    "Azatlı'da kumaş, Beykoz'da kâğıt fabrikası kuruldu (s. 127).", "III. Selim'in Diğer Yenilikleri"),
 ],
 "u3k9": [
  _eski("u3k9", "Tanzimat Dönemi'nde yayımlanan özel", {},
        ipucu="Özel gazeteler Tanzimat Dönemi'nde çıktı. Takvim-i Vekayi kartının ek kısmında adları geçiyor.",
        aciklama="Tanzimat Dönemi'nde Tercümân-ı Ahvâl, Tasvîr-i Efkâr gibi özel gazeteler yayımlandı (s. 129).",
        hatirla="Tanzimat Dönemi'nde resmî gazetenin yanında özel gazeteler de yayımlanmaya başladı."),
  Y(D9b, ["Mekteb-i Tıbbiye", "Muzıka-yi Hümâyun", "Mekteb-i Harbiye"], 0, "Doktor tıpla ilgilidir. Adında tıp geçen okulu bul.",
    "Doktor yetiştirmek için Mekteb-i Tıbbiye açıldı (s. 128).", "II. Mahmud"),
  Y(D9d, ["Takvim-i Vekayi", "Nizâm-ı Cedîd", "Tercümân-ı Ahvâl"], 0, "Takvim-i Vekayi kartının ilk cümlesine bak.",
    "1831'de çıkarılan Takvim-i Vekayi ilk resmî gazetedir (s. 128).", "Takvim-i Vekayi"),
  Y(D9f, ["1789", "1808", "1839"], 2, "Tanzimat Fermanı kartının ilk cümlesine bak.",
    "Tanzimat Fermanı 3 Kasım 1839'da ilan edildi (s. 129).", "Tanzimat Fermanı"),
 ],
 "u3k10": [
  _eski("u3k10", "Kadı ve müderrislerin", {"Kaptanıderya": "Defterdar"}),
  Y(DAb, ["Kazasker", "Defterdar", "Nişancı"], 1, "Divan Üyeleri kartında “gelir ve gider” sözünü bul.",
    "Defterdar devletin gelir ve giderlerini denetler, mali işleri yürütürdü (s. 141).", "Divan Üyeleri"),
  Y(DAd, ["Nişancı", "Şeyhülislam", "Defterdar"], 1, "Fetva dinî bir görüştür. Dinî konulardan sorumlu üyeyi düşün.",
    "Şeyhülislam kararların İslam dinine uygunluğu konusunda fetva verirdi (s. 141).", "Divan Üyeleri"),
  Y(DAf, ["Taşra yönetimi", "Merkez yönetimi", "Saray yönetimi"], 0, "Merkez ve Taşra Yönetimi kartında başkentten uzak yerleri bul.",
    "Ülkenin merkezden uzak eyalet ve sancaklarının yönetimine taşra yönetimi denir (s. 139).", "Merkez ve Taşra Yönetimi"),
 ],
 "u3k11": [
  _eski("u3k11", "Mühendishane-i Berri-i Hümayun'un", {},
        ipucu="Adındaki “Berri” kelimesine bak: “berr” kara (deniz olmayan yer) demektir."),
  Y(DBb, ["Deniz Mühendislik Okulu", "Güzel Sanatlar Okulu", "Kara Mühendislik Okulu"], 0,
    "Adındaki “Bahri” kelimesine bak: “bahr” deniz demektir.",
    "Mühendishane-i Bahri-i Hümayun, Deniz Mühendislik Okulu'dur (s. 142).", "Batı Tarzı Okullar"),
  _eski("u3k11", "Rüştiyeler hangi düzeyde", {"İlkokul": "Lise"}, aciklama="Rüştiyeler ortaokul düzeyinde okullardı (s. 143)."),
  Y(DBd, ["Ortaokul", "Lise", "Üniversite"], 1, "Batı Tarzı Okullar kartında parantez içine bak.",
    "İdadîler lise düzeyinde okullardı (s. 143).", "Batı Tarzı Okullar"),
  Y(DBf, ["Kadılar", "Loncalar", "Defterdarlar"], 1, "Meslek Okulları kartının ek kısmının ilk cümlesine bak.",
    "Başlangıçta gençlere meslek ve ahlakı lonca teşkilatları öğretiyordu (s. 143).", "Meslek Okulları"),
 ],
 "u3k12": [
  Y(DCb, ["Kaliteyi denetlemek", "Fiyatları kontrol altında tutmak", "Fetva vermek"], 2, "Lonca bir meslek örgütüdür. Hangisi meslekle ilgili değil?",
    "Loncalar meslekle ilgili işler yapardı; fetva vermek onların görevi değildi (s. 150).", "Lonca"),
  Y(DCd, ["Cömert olmak", "Kusur görmemek", "Misafirperver olmak"], 0, "Eli açık olan kişi sahip olduklarını paylaşır.",
    "Eli açık olmalı: cömert olmak (s. 150).", "Ahilik"),
  _eski("u3k12", "Vakıf anlayışının temelleri", {"Memlükler": "Osmanlı"}),
  Y(DCf, ["Selçuklular", "Osmanlı", "Bizans"], 1, "Temelleri atıldıktan sonra vakıf anlayışını en çok geliştiren devleti düşün.",
    "Vakıf anlayışı Osmanlı Devleti zamanında altın çağını yaşadı (s. 148).", "Vakıf"),
 ],
}

IKIZ = {
 "u3k1": [[D1a, D1b], [D1c, D1d], [D1e, D1f]], "u3k2": [[D2a, D2b], [D2c, D2d], [D2e, D2f]],
 "u3k3": [[D3a, D3b], [D3c, D3d], [D3e, D3f]], "u3k4": [[D4a, D4b], [D4c, D4d], [D4e, D4f]],
 "u3k5": [[D5a, D5b], [D5c, D5d], [D5e, D5f]], "u3k6": [[D6a, D6b], [D6c, D6d], [D6e, D6f]],
 "u3k7": [[D7a, D7b], [D7c, D7d], [D7e, D7f]], "u3k8": [[D8a, D8b], [D8c, D8d], [D8e, D8f]],
 "u3k9": [[D9a, D9b], [D9c, D9d], [D9e, D9f]], "u3k10": [[DAa, DAb], [DAc, DAd], [DAe, DAf]],
 "u3k11": [[DBa, DBb], [DBc, DBd], [DBe, DBf]], "u3k12": [[DCa, DCb], [DCc, DCd], [DCe, DCf]],
}

# Testte sorulan sayı eskisi gibi (18 Kasım 2026 öncesi soru sayıları; 2'si metinli)
TESTSORU = {k: (8 if k == "u3k2" else 9 if k == "u3k10" else 10) for k in IKIZ}

NE = {
 D1a: ["İslamiyet'ten önceki amacı", "Sonradan eklenen düşünceyi"], D1b: ["Sonradan eklenen düşünceyi", "İslamiyet'ten önceki amacı"],
 D1c: ["Kutsal toprakların geçtiği dönemi", "İstanbul'un fethedildiği dönemi"], D1d: ["İstanbul'un fethedildiği dönemi", "Kutsal toprakların geçtiği dönemi"],
 D1e: ["Orhan Bey Dönemi'ndeki başkenti", "I. Murad Dönemi'ndeki başkenti"], D1f: ["I. Murad Dönemi'ndeki başkenti", "Orhan Bey Dönemi'ndeki başkenti"],
 D2a: ["İskânın amacı olmayanı", "İskânın amacı olanı"], D2b: ["İskânın amacı olanı", "İskânın amacı olmayanı"],
 D2c: ["İstimaletin amacı olanı", "İstimaletin amacı olmayanı"], D2d: ["İstimaletin amacı olmayanı", "İstimaletin amacı olanı"],
 D2e: ["Fetihten önce yapılanı", "Fetihten sonra yapılanı"], D2f: ["Fetihten sonra yapılanı", "Fetihten önce yapılanı"],
 D3a: ["Beylikleri kışkırtmanın neden türünü", "Ticaret yollarının neden türünü"], D3b: ["Ticaret yollarının neden türünü", "Beylikleri kışkırtmanın neden türünü"],
 D3c: ["Osmanlı'nın yapmadığı hazırlığı", "Osmanlı'nın yaptığı hazırlığı"], D3d: ["Osmanlı'nın yaptığı hazırlığı", "Osmanlı'nın yapmadığı hazırlığı"],
 D3e: ["Kuşatmanın başladığı tarihi", "Son hücumun başladığı tarihi"], D3f: ["Son hücumun başladığı tarihi", "Kuşatmanın başladığı tarihi"],
 D4a: ["En önce yapılan savaşı", "En son yapılan savaşı"], D4b: ["En son yapılan savaşı", "En önce yapılan savaşı"],
 D4c: ["Ekonomik sonucu", "Dinî sonucu"], D4d: ["Dinî sonucu", "Ekonomik sonucu"],
 D4e: ["Mısır Seferi'nden önce güçlenen sınırı", "Mısır Seferi'yle güvenceye alınan sınırı"], D4f: ["Mısır Seferi'yle güvenceye alınan sınırı", "Mısır Seferi'nden önce güçlenen sınırı"],
 D5a: ["Dias'ın ulaştığı yeri", "Kolomb'un ulaştığı yeri"], D5b: ["Kolomb'un ulaştığı yeri", "Dias'ın ulaştığı yeri"],
 D5c: ["Yeni kıtayı fark eden kişiyi", "Hindistan'a deniz yoluyla ulaşan kişiyi"], D5d: ["Hindistan'a deniz yoluyla ulaşan kişiyi", "Yeni kıtayı fark eden kişiyi"],
 D5e: ["Osmanlı limanlarına olanı", "Atlas Okyanusu limanlarına olanı"], D5f: ["Atlas Okyanusu limanlarına olanı", "Osmanlı limanlarına olanı"],
 D6a: ["Kilisenin etkisine olanı", "Kralların otoritesine olanı"], D6b: ["Kralların otoritesine olanı", "Kilisenin etkisine olanı"],
 D6c: ["Reform'un başladığı ülkeyi", "Rönesans'ın başladığı ülkeyi"], D6d: ["Rönesans'ın başladığı ülkeyi", "Reform'un başladığı ülkeyi"],
 D6e: ["Reform'un bir sonucunu", "Rönesans'ın bir sonucunu"], D6f: ["Rönesans'ın bir sonucunu", "Reform'un bir sonucunu"],
 D7a: ["Sanayi İnkılabı'ndan önceki üretim yerini", "Sanayi İnkılabı'ndan sonraki üretim yerini"], D7b: ["Sanayi İnkılabı'ndan sonraki üretim yerini", "Sanayi İnkılabı'ndan önceki üretim yerini"],
 D7c: ["1856'daki belgeyi", "1839'daki belgeyi"], D7d: ["1839'daki belgeyi", "1856'daki belgeyi"],
 D7e: ["Vergiyi ödeyenleri", "Vergi ödemeyenleri"], D7f: ["Vergi ödemeyenleri", "Vergiyi ödeyenleri"],
 D8a: ["Lale Devri'ndeki padişahı", "Nizâm-ı Cedîd'i başlatan padişahı"], D8b: ["Nizâm-ı Cedîd'i başlatan padişahı", "Lale Devri'ndeki padişahı"],
 D8c: ["Islahat giderleri için kurulanı", "Yangınlar için kurulanı"], D8d: ["Yangınlar için kurulanı", "Islahat giderleri için kurulanı"],
 D8e: ["Lale Devri'nde yapılanları", "III. Selim Dönemi'nde kurulanları"], D8f: ["III. Selim Dönemi'nde kurulanları", "Lale Devri'nde yapılanları"],
 D9a: ["Subay yetiştiren okulu", "Doktor yetiştiren okulu"], D9b: ["Doktor yetiştiren okulu", "Subay yetiştiren okulu"],
 D9c: ["Özel gazetelerden birini", "İlk resmî gazeteyi"], D9d: ["İlk resmî gazeteyi", "Özel gazetelerden birini"],
 D9e: ["II. Mahmud'un tahta çıktığı yılı", "Tanzimat Fermanı'nın ilan yılını"], D9f: ["Tanzimat Fermanı'nın ilan yılını", "II. Mahmud'un tahta çıktığı yılı"],
 DAa: ["Kadı ve müderris atayan üyeyi", "Mali işleri yürüten üyeyi"], DAb: ["Mali işleri yürüten üyeyi", "Kadı ve müderris atayan üyeyi"],
 DAc: ["Antlaşma yazışmalarını yürüteni", "Fetva vereni"], DAd: ["Fetva vereni", "Antlaşma yazışmalarını yürüteni"],
 DAe: ["Başkent yönetiminin adını", "Uzak yerlerin yönetiminin adını"], DAf: ["Uzak yerlerin yönetiminin adını", "Başkent yönetiminin adını"],
 DBa: ["“Berri” okulunun Türkçesini", "“Bahri” okulunun Türkçesini"], DBb: ["“Bahri” okulunun Türkçesini", "“Berri” okulunun Türkçesini"],
 DBc: ["Rüştiyelerin düzeyini", "İdadîlerin düzeyini"], DBd: ["İdadîlerin düzeyini", "Rüştiyelerin düzeyini"],
 DBe: ["Adalet işlerini yürütenleri", "Meslek ve ahlak öğretenleri"], DBf: ["Meslek ve ahlak öğretenleri", "Adalet işlerini yürütenleri"],
 DCa: ["Loncaların görevi olanı", "Loncaların görevi olmayanı"], DCb: ["Loncaların görevi olmayanı", "Loncaların görevi olanı"],
 DCc: ["“Kapısı açık” kuralının anlamını", "“Eli açık” kuralının anlamını"], DCd: ["“Eli açık” kuralının anlamını", "“Kapısı açık” kuralının anlamını"],
 DCe: ["Temellerin atıldığı devleti", "Altın çağın yaşandığı devleti"], DCf: ["Altın çağın yaşandığı devleti", "Temellerin atıldığı devleti"],
}

# İkizlerde farkı yaratan sözcük + soru kelimesi sarı
VURGU = {
 D1a: ["İslamiyet'ten önce", "amaç neydi"], D1b: ["kabulünden sonra", "hangi düşünce eklendi"],
 D1c: ["Hangi padişah", "kutsal toprakların"], D1d: ["Hangi padişah", "İstanbul"],
 D1e: ["Orhan Bey", "hangi şehir"], D1f: ["I. Murad", "hangi şehir"],
 D2a: ["Hangisi", "DEĞİLDİR"], D2b: ["Hangisi", "biridir"],
 D2c: ["Hangisi", "biridir"], D2d: ["Hangisi", "DEĞİLDİR"],
 D2e: ["ÖNCE", "nasıl uygulandı"], D2f: ["SONRA", "nasıl uygulandı"],
 D3a: ["kışkırtması", "hangi nedenidir"], D3b: ["ticaret yolları", "hangi nedenidir"],
 D3c: ["hangisi", "DEĞİLDİR"], D3d: ["hangisi", "biridir"],
 D3e: ["harekete geçti", "hangi tarihte"], D3f: ["son büyük hücuma", "hangi tarihte"],
 D4a: ["hangisi", "en önce"], D4b: ["hangisi", "en son"],
 D4c: ["hangisi", "ekonomik"], D4d: ["hangisi", "dinî"],
 D4e: ["Mısır Seferi'nden önce", "hangi sınırı"], D4f: ["Mısır Seferi ile", "hangi sınırını"],
 D5a: ["Bartolomeu Dias", "nereye"], D5b: ["Kristof Kolomb", "nereye"],
 D5c: ["yeni bir kıta", "kim fark etti"], D5d: ["Hindistan'a ulaşan", "kimdir"],
 D5e: ["Osmanlı liman şehirlerine", "ne oldu"], D5f: ["Atlas Okyanusu kıyısındaki", "ne oldu"],
 D6a: ["kilisenin", "ne oldu"], D6b: ["kralların", "ne oldu"],
 D6c: ["Reform", "hangi ülkede"], D6d: ["Rönesans", "hangi ülkede"],
 D6e: ["Hangisi", "Reform"], D6f: ["Hangisi", "Rönesans'ın"],
 D7a: ["önce", "nerede"], D7b: ["sonra", "nerede"],
 D7c: ["1856'da", "hangisidir"], D7d: ["1839'da", "hangisidir"],
 D7e: ["vergi yükü kimin üzerindeydi"], D7f: ["kimler vergi vermiyordu"],
 D8a: ["Lale Devri'nde", "kimdir"], D8b: ["Nizâm-ı Cedîd", "kimdir"],
 D8c: ["giderlerini karşılamak", "ne kuruldu"], D8d: ["Yangınlarla", "ne kuruldu"],
 D8e: ["Lale Devri'nde", "hangi yapılar"], D8f: ["III. Selim Dönemi'nde", "hangi yapılar"],
 D9a: ["Subay", "hangi okul"], D9b: ["Doktor", "hangi okul"],
 D9c: ["özel gazetelerden", "hangisidir"], D9d: ["ilk resmî gazete", "hangisidir"],
 D9e: ["II. Mahmud", "hangi yıl"], D9f: ["Tanzimat Fermanı", "hangi yıl"],
 DAa: ["Kadı ve müderrislerin", "hangi Divan üyesi"], DAb: ["Mali işleri", "hangi Divan üyesi"],
 DAc: ["antlaşmaların", "kim yürütürdü"], DAd: ["fetva", "kim"],
 DAe: ["başkent yönetimine", "ne denir"], DAf: ["merkezden uzak", "ne denir"],
 DBa: ["Berri", "Türkçesi nedir"], DBb: ["Bahri", "Türkçesi nedir"],
 DBc: ["Rüştiyeler", "hangi düzeyde"], DBd: ["İdadîler", "hangi düzeyde"],
 DBe: ["adalet işlerini", "kim yürütürdü"], DBf: ["meslek ve ahlakı", "kim öğretiyordu"],
 DCa: ["Hangisi", "biridir"], DCb: ["Hangisi", "biri değildir"],
 DCc: ["kapısı açık olmalı", "ne anlama gelir"], DCd: ["eli açık olmalı", "ne anlama gelir"],
 DCe: ["temelleri", "hangi devlet"], DCf: ["altın çağını", "hangi devlet"],
}

# Yeni soruların "sorunun kalbi" bölgeleri (eski soruların bölgeleri bolge.py'de)
BOLGE = {
 D1d: ["Hangi padişah döneminde"], D1e: ["hangi şehir fethedilip başkent oldu"], D1f: ["hangi şehir fethedilip başkent oldu"],
 D2b: ["amaçlarından biridir"], D2d: ["amaçlarından biri DEĞİLDİR"], D2f: ["fetihten SONRA nasıl uygulandı"],
 D3b: ["fethin hangi nedenidir"], D3d: ["hazırlıklardan biridir"], D3f: ["son büyük hücuma hangi tarihte başladı"],
 D4b: ["hangisi en son yapıldı"], D4d: ["dinî sonuçlarından biridir"], D4f: ["hangi sınırını güvence altına aldı"],
 D5b: ["nereye ulaştı"], D5d: ["Hindistan'a ulaşan denizci kimdir"], D5f: ["liman kentlerine ne oldu"],
 D6b: ["kralların otoritesine ne oldu"], D6d: ["hangi ülkede başladı"], D6f: ["Rönesans'ın sonuçlarından biridir"],
 D7b: ["sonra üretim nerede yapılmaya başlandı"], D7d: ["belge hangisidir"], D7f: ["kimler vergi vermiyordu"],
 D8b: ["başlatan padişah kimdir"], D8d: ["ne kuruldu"], D8f: ["hangi yapılar kuruldu"],
 D9b: ["hangi okul açıldı"], D9d: ["ilk resmî gazete hangisidir"], D9f: ["hangi yıl ilan edildi"],
 DAb: ["hangi Divan üyesi yürütürdü"], DAd: ["kim fetva verirdi"], DAf: ["yönetimine ne denir"],
 DBb: ["Türkçesi nedir"], DBd: ["hangi düzeyde okullardı"], DBf: ["kim öğretiyordu"],
 DCb: ["görevlerinden biri değildir"], DCd: ["ne anlama gelir"], DCf: ["hangi devlet zamanında altın çağını yaşadı"],
}
