TEKRAR = {"u3k12": [
 ("Süleymaniye ve Selimiye Camilerini {Mimar Sinan|Ahi Evran|Ahmet Cevdet Paşa} yaptı.", "s. 145"),
 ("Güzel yazı yazma sanatına {hat|tezhip|ebru} denir. Minyatürlerde {tarihî olaylar ve saray hayatı|haritalar ve gemiler|yalnızca çiçekler} resmedildi.", "s. 146"),
 ("{Mehter Takımı|Tulumbacılar Ocağı|Enderun Mektebi} Osmanlı ordusunun resmî müzik topluluğuydu.", "s. 146"),
 ("Osmanlı şehirlerinde ticaretin kalbi {bedesten|medrese|imaret} denilen korunaklı çarşılarda atardı.", "s. 147"),
 ("Vakfedilen mallar {satılamaz|satılabilir|kiraya verilip geri alınabilir}, devredilemez ve miras bırakılamaz.", "s. 148"),
 ("Ahi teşkilatının kurucusu {Ahi Evran|Mimar Sinan|Mustafa Reşid Paşa}'dır.", "s. 149"),
 ("Ahi teşkilatı yetersiz kalınca yerini {loncalara|medreselere|vakıflara} bıraktı.", "s. 150"),
]}
KISA = {"u3k12": [
 {"soru": "Vakıf nedir ve vakıf yapılarının giderleri nasıl karşılanırdı? Yazınız.",
  "tetik": ["nedir", "nasıl"],
  "okut": ["", "", ""],
  "parcalar": [
   {"bas": "Vakıf:", "ornek": "Kişilerin mal veya mülklerini toplum yararına süresiz olarak bağışlamasıdır.", "havuz": ["Devletin topladığı vergidir.", "Aynı meslekten esnafın örgütüdür."], "k": ["bağış", "toplum"]},
   {"bas": "Giderler:", "ornek": "Vakfa bağışlanan dükkân, tarla, bahçe gelirlerinden karşılanırdı.", "havuz": ["Devlet hazinesinden karşılanırdı.", "Yabancı devletlerin yardımıyla karşılanırdı."], "k": ["dükkân", "tarla", "bahçe", "gelir"]}],
  "kisa": "Toplum yararına bağış; giderler dükkân, tarla gelirlerinden.",
  "cevap": "Vakıf, kişilerin mal veya mülklerini toplum yararına kullanılmak üzere süresiz olarak bağışlamasıdır. Vakıf yapılarının giderleri vakfa bağışlanan dükkân, tarla, bahçe gibi yerlerin gelirlerinden karşılanırdı; böylece devlet hazinesine yük olunmazdı.",
  "anahtarlar": [{"ad": "vakıf: toplum yararına bağış", "k": ["bağış", "toplum"]}, {"ad": "giderler: bağışlanan yerlerin gelirleri", "k": ["dükkân", "tarla", "bahçe", "gelir"]}],
  "sayfa": "s. 148"},
 {"soru": "Loncaların görevlerinden iki tanesini yazınız.",
  "tetik": ["iki tanesini"],
  "okut": ["", "", ""],
  "parcalar": [
   {"bas": "Birinci görev:", "ornek": "Kaliteyi denetlemek.", "havuz": ["Fetva vermek.", "Donanmayı yönetmek."], "k": ["kalite", "dayanışma"]},
   {"bas": "İkinci görev:", "ornek": "Fiyatları kontrol altında tutmak.", "havuz": ["Kadı atamak.", "Antlaşma yazışmalarını yürütmek."], "k": ["fiyat", "üretim"]}],
  "kisa": "Kaliteyi denetlemek, fiyatları kontrol etmek.",
  "cevap": "Loncalar esnaf arasında dayanışmayı sağlar, üretimi düzenler, kaliteyi denetler ve fiyatları kontrol altında tutardı.",
  "anahtarlar": [{"ad": "bir görev (kalite / dayanışma)", "k": ["kalite", "dayanışma"]}, {"ad": "bir görev (fiyat / üretim)", "k": ["fiyat", "üretim"]}],
  "sayfa": "s. 150"},
]}
OKUT = {"u3k12": [
 ["vakfın ne olduğunu ve giderlerinin nasıl karşılandığını anlatmanı", "vakıflarla hangi yapıların yapıldığını sıralamanı", "vakıf anlayışının temelini kimin attığını söylemeni"],
 ["loncaların görevlerinden ikisini yazmanı", "Ahi teşkilatının kurucusunu söylemeni", "loncaların neden ortaya çıktığını anlatmanı"]]}
METINLI = {"u3k12": [
 {"metin": ["Ahilik, halkı meslek alanında yetiştiren ve ahlaki yönden eğiten bir örgütlenmedir.", "Ticaret gelişip şehirler büyüyünce Ahi teşkilatı bazı yönlerden yetersiz kaldı.", "Ahiliğin yerini loncalar aldı."],
  "soru": "Metne göre Ahi teşkilatı neden yetersiz kalmıştır?", "bolge": ["neden yetersiz kalmıştır"],
  "serit": "Ahi teşkilatının yetersiz kalma nedeni", "kanit": [1],
  "secenekler": ["Ticaret gelişip şehirler büyüdüğü için", "Loncalar kurulduğu için", "Halkı ahlaki yönden eğittiği için"], "dogru": 0, "tuzak": [1, 2],
  "ipucu": "“yetersiz kaldı” ifadesinin geçtiği cümlenin başını oku.", "kanitIpucu": "“yetersiz” kelimesi hangi cümlede?",
  "aciklama": "Ticaret gelişip şehirler büyüyünce Ahi teşkilatı bazı yönlerden yetersiz kaldı ve yerini loncalara bıraktı (s. 150).", "kavram": "Lonca"},
 {"metin": ["Osmanlı'da günlük hayat dinî inançlar, gelenekler ve yaşanılan yere göre şekillendi.", "Şehirlerde yaşam cami, çarşı ve mahalle etrafında örgütlendi.", "Misafir güler yüzle karşılanır, sofraya önce büyükler otururdu.", "Ticaretin kalbi bedesten denilen korunaklı çarşılarda atardı.", "Halkın büyük bölümünün yaşadığı köylerde ise geçim kaynağı tarım ve hayvancılıktı."],
  "soru": "Metne göre şehirlerde yaşam hangi yerlerin etrafında örgütlenmiştir?", "bolge": ["şehirlerde yaşam", "hangi yerlerin etrafında örgütlenmiştir"],
  "serit": "Şehir hayatının örgütlendiği yerler", "kanit": [1],
  "secenekler": ["Cami, çarşı ve mahalle", "Tarla ve hayvan ağılları", "Bedesten ve köyler"], "dogru": 0, "tuzak": [1, 2],
  "ipucu": "“Şehirlerde” kelimesiyle başlayan cümleyi bul; köylerle karıştırma.", "kanitIpucu": "“örgütlendi” kelimesi hangi cümlede?",
  "aciklama": "Osmanlı şehirlerinde yaşam cami, çarşı ve mahalle etrafında örgütlendi. Tarım ve hayvancılık köylerin geçim kaynağıydı (s. 147).", "kavram": "Günlük Hayat"}]}
