TEKRAR = {"u3k3": [
 ("II. Mehmed {1451|1453|1071} yılında Osmanlı tahtına çıktı.", "s. 96"),
 ("İstanbul'un İpek Yolu gibi ticaret yolları üzerinde olması fethin {ekonomik|dinî|kültürel} nedenidir.", "s. 97"),
 ("Doğu Roma'ya denizden yardım gelmesini engellemek için Anadolu Hisarı'nın karşısına {Rumeli Hisarı|Topkapı Sarayı|Galata Kulesi} yaptırıldı.", "s. 98"),
 ("Macar ustabaşı Urban'a {şahi|grejuva|kadırga} adı verilen büyük toplar döktürüldü.", "s. 98"),
 ("Doğu Roma, Osmanlı donanması girmesin diye {Haliç|Marmara|Karadeniz} girişine büyük bir demir zincir çekti.", "s. 99"),
 ("Zincir aşılamayınca gemiler {kızaklarla karadan|denizin altından|zinciri kırarak} Haliç'e indirildi.", "s. 101"),
 ("{53|7|1000} gün süren kuşatmanın ardından şehir fethedildi ve II. Mehmed {Fatih|Kanuni|Yavuz} unvanını aldı.", "s. 101"),
]}
KISA = {"u3k3": [
 {"soru": "İstanbul'un fethinin siyasi ve ekonomik nedenlerinden birer tane yazınız.",
  "tetik": ["birer tane"],
  "okut": ["", "", ""],
  "parcalar": [
   {"bas": "Siyasi neden:", "ornek": "İstanbul, Osmanlı topraklarının arasında kalıp toprak bütünlüğüne engel oluyordu.", "havuz": ["İstanbul ticaret yolları üzerindeydi.", "Şehir üç katmanlı surlarla çevriliydi."], "k": ["bütünl", "kışkırt"]},
   {"bas": "Ekonomik neden:", "ornek": "İstanbul, İpek Yolu gibi ticaret yolları üzerindeydi.", "havuz": ["Doğu Roma, beylikleri Osmanlı'ya karşı kışkırtıyordu.", "Şehir üç katmanlı surlarla çevriliydi."], "k": ["ticaret", "ipek"]}],
  "kisa": "Siyasi: toprak bütünlüğü. Ekonomik: ticaret yolları.",
  "cevap": "Siyasi neden: İstanbul, Anadolu ile Balkanlardaki Osmanlı toprakları arasında kalıyor ve toprak bütünlüğüne engel oluyordu. Ekonomik neden: İstanbul, İpek Yolu gibi önemli ticaret yolları üzerindeydi.",
  "anahtarlar": [{"ad": "siyasi: toprak bütünlüğü / beylikleri kışkırtma", "k": ["bütünl", "kışkırt"]}, {"ad": "ekonomik: ticaret yolları", "k": ["ticaret", "ipek"]}],
  "sayfa": "s. 97"},
 {"soru": "Osmanlı gemileri neden karadan yürütülmüş ve Haliç'e nasıl indirilmiştir? Yazınız.",
  "tetik": ["neden", "nasıl"],
  "okut": ["", "", ""],
  "parcalar": [
   {"bas": "Neden:", "ornek": "Haliç girişindeki demir zincir aşılamadı.", "havuz": ["Şahi topları çok ağırdı.", "Denizde fırtına vardı."], "k": ["zincir"]},
   {"bas": "Nasıl:", "ornek": "Gemiler Galata surları önünden kızaklarla kaydırılarak indirildi.", "havuz": ["Gemiler denizin altından geçirildi.", "Gemiler parçalanıp taşındı."], "k": ["kızak", "kaydır"]}],
  "kisa": "Zincir aşılamadığı için; kızaklarla kaydırılarak.",
  "cevap": "Doğu Roma Haliç girişine demir zincir çektiği için Osmanlı donanması Haliç'e giremedi. Bu yüzden gemiler Galata surları önünden kızaklarla kaydırılarak karadan Haliç'e indirildi.",
  "anahtarlar": [{"ad": "neden: zincir aşılamadı", "k": ["zincir"]}, {"ad": "nasıl: kızaklarla kaydırılarak", "k": ["kızak", "kaydır"]}],
  "sayfa": "s. 99–101"},
]}
OKUT = {"u3k3": [
 ["fethin bir siyasi ve bir ekonomik nedenini yazmanı", "fethin sonuçlarını sıralamanı", "İstanbul'un hangi yıl fethedildiğini söylemeni"],
 ["gemilerin neden karadan yürütüldüğünü ve nasıl indirildiğini anlatmanı", "Haliç'e zinciri kimin çektiğini söylemeni", "kuşatmanın kaç gün sürdüğünü yazmanı"]]}
METINLI = {"u3k3": [
 {"metin": ["Doğu Roma, şehri çevreleyen surları onardı.", "Osmanlı donanması girmesin diye Haliç girişine büyük bir demir zincir çekti.", "Ayrıca su üzerinde yanabilen grejuvayı stokladı."],
  "soru": "Metne göre Haliç girişine zincir çekilmesinin amacı nedir?", "bolge": ["zincir çekilmesinin amacı nedir"],
  "serit": "Zincirin çekilme amacı", "kanit": [1],
  "secenekler": ["Osmanlı donanmasının Haliç'e girmesini önlemek", "Şehri çevreleyen surları onarmak", "Grejuva stoklarını korumak"], "dogru": 0, "tuzak": [1, 2],
  "ipucu": "“zincir” kelimesinin geçtiği cümlede “diye” sözcüğünden önce ne yazıyor?", "kanitIpucu": "Zincirden söz eden cümle hangisi?",
  "aciklama": "Doğu Roma, Osmanlı donanmasının Haliç'e girmesini önlemek için Haliç girişine büyük bir demir zincir çekti (s. 99).", "kavram": "Doğu Roma'nın Savunması"},
 {"metin": ["Osmanlı ordusu 6 Nisan 1453'te İstanbul önüne gelerek surların önünde mevzilendi.", "9 Nisan'da Haliç'teki zinciri aşma girişimi başarısız oldu.", "II. Mehmed'in hocası Akşemsettin, verdiği manevi destekle ordunun azmini güçlendirdi.", "Padişah, donanmanın bir kısmının Galata surları önünden kızaklarla kaydırılmasını emretti.", "Askerler gemileri bir gece boyunca karadan yürüterek Haliç'e indirdi.", "29 Mayıs'ta başlayan son hücumla 53 gün süren kuşatma sona erdi ve şehir fethedildi."],
  "soru": "Metne göre gemiler karadan yürütülmeden önce Haliç'te ne olmuştur?", "bolge": ["karadan yürütülmeden önce", "ne olmuştur"],
  "serit": "Gemiler karadan yürütülmeden önce Haliç'te olan", "kanit": [1],
  "secenekler": ["Zinciri aşma girişimi başarısız oldu.", "Son büyük hücum başladı.", "Şehir fethedildi."], "dogru": 0, "tuzak": [1, 2],
  "ipucu": "Olayları sırayla düşün: gemilerin karadan yürütüldüğü cümleden önceki cümlelere bak.", "kanitIpucu": "Haliç'teki zinciri anlatan cümle hangisi?",
  "aciklama": "9 Nisan'da Haliç'teki zinciri aşma girişimi başarısız olunca gemiler kızaklarla karadan Haliç'e indirildi. Son hücum ve fetih bundan sonra gerçekleşti (s. 101).", "kavram": "Gemilerin Karadan Yürütülmesi"}]}
