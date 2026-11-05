TEKRAR = {"u3k4": [
 ("Yavuz Sultan Selim {1512|1520|1453} yılında Osmanlı tahtına çıktı ve 1514'te {Çaldıran|Preveze|Ridaniye} Savaşı'nı kazandı.", "s. 103"),
 ("Memlükler {Baharat Yolu|Atlas Okyanusu|Ümit Burnu} ticaretinden büyük gelir elde ediyordu.", "s. 103"),
 ("Osmanlı ordusu 1516'da {Mercidabık|Turnadağ|Çaldıran}, 1517'de {Ridaniye|Preveze|Malazgirt} Savaşı'nı kazanarak Memlük Devleti'ne son verdi.", "s. 103"),
 ("Mısır Seferi'nden sonra Osmanlı'nın {güney|batı|kuzey} sınırları güvence altına alındı.", "s. 104"),
 ("Yavuz'dan sonra Osmanlı padişahları {halife|kaptanıderya|tekfur} unvanını taşımaya başladı. Kutsal emanetler {Topkapı Sarayı|Rumeli Hisarı|Edirne Sarayı}'nda koruma altına alındı.", "s. 104"),
 ("Barbaros Hayreddin Paşa 1534'te {kaptanıderya|halife|tekfur} görevine getirildi.", "s. 105"),
 ("1538'de Preveze'de Barbaros donanmasını {hilal|kare|tek sıra} şeklinde dizdi. Bu zaferden sonra Akdeniz âdeta bir {Türk gölü|Haçlı gölü|Venedik gölü} oldu.", "s. 105"),
]}
KISA = {"u3k4": [
 {"soru": "Mısır Seferi'nin Osmanlı'ya siyasi ve ekonomik sonuçlarından birer tane yazınız.",
  "tetik": ["birer tane"],
  "okut": ["", "", ""],
  "parcalar": [
   {"bas": "Siyasi sonuç:", "ornek": "Güney sınırları güvence altına alındı.", "havuz": ["Baharat Yolu Osmanlı denetimine geçti.", "Mısır'dan alınan vergiler ekonomiyi güçlendirdi."], "k": ["sınır", "akdeniz"]},
   {"bas": "Ekonomik sonuç:", "ornek": "Baharat Yolu Osmanlı denetimine geçti.", "havuz": ["Güney sınırları güvenceye alındı.", "Padişahlar halife unvanını aldı."], "k": ["baharat", "vergi"]}],
  "kisa": "Siyasi: güney sınırları güvende. Ekonomik: Baharat Yolu denetimi.",
  "cevap": "Siyasi sonuç: Osmanlı'nın güney sınırları güvence altına alındı ve Doğu Akdeniz'de hâkimiyeti güçlendi. Ekonomik sonuç: Baharat Yolu Osmanlı denetimine geçti; Mısır'dan alınan vergiler ekonomiyi güçlendirdi.",
  "anahtarlar": [{"ad": "siyasi: güney sınırları / Doğu Akdeniz", "k": ["sınır", "akdeniz"]}, {"ad": "ekonomik: Baharat Yolu / vergiler", "k": ["baharat", "vergi"]}],
  "sayfa": "s. 104"},
 {"soru": "Barbaros Preveze'de Haçlı donanmasını hangi taktikle yenmiştir? Yazınız.",
  "tetik": ["hangi taktikle"],
  "okut": ["", "", ""],
  "parcalar": [
   {"bas": "Diziliş:", "ornek": "Donanmasını hilal şeklinde dizdi.", "havuz": ["Donanmasını tek sıra hâlinde dizdi.", "Gemileri karadan yürüttü."], "k": ["hilal"]},
   {"bas": "Saldırı:", "ornek": "Hızlı kadırgalar ve uzun menzilli toplarla ağır Haçlı gemilerini etkisiz hâle getirdi.", "havuz": ["Ağır gemilerle yavaşça ilerledi.", "Haçlı gemileriyle anlaşma yaptı."], "k": ["kadırga", "menzil"]}],
  "kisa": "Hilal düzeni; hızlı kadırgalar ve uzun menzilli toplar.",
  "cevap": "Barbaros donanmasını hilal şeklinde dizdi. Hızlı kadırgalarla saldırdı ve uzun menzilli toplarla büyük ve ağır Haçlı gemilerini etkisiz hâle getirdi.",
  "anahtarlar": [{"ad": "hilal şeklinde diziliş", "k": ["hilal"]}, {"ad": "hızlı kadırgalar / uzun menzilli toplar", "k": ["kadırga", "menzil"]}],
  "sayfa": "s. 105"},
]}
OKUT = {"u3k4": [
 ["Mısır Seferi'nin bir siyasi ve bir ekonomik sonucunu yazmanı", "Mısır Seferi'nde yapılan savaşları sıralamanı", "Mısır Seferi'nin nedenlerini anlatmanı"],
 ["Barbaros'un Preveze'de uyguladığı taktiği anlatmanı", "Haçlı donanmasını hangi devletlerin kurduğunu sıralamanı", "Preveze Zaferi'nin tarihini söylemeni"]]}
METINLI = {"u3k4": [
 {"metin": ["Yavuz Sultan Selim 1514'te Çaldıran Savaşı'nda Safevi Devleti'ni yendi.", "Ardından Memlük Devleti üzerine yürüdü.", "1516'da Mercidabık, 1517'de Ridaniye Savaşı'nı kazandı."],
  "soru": "Metne göre Yavuz, Memlük Devleti üzerine yürümeden önce hangi devleti yenmiştir?", "bolge": ["yürümeden önce hangi devleti yenmiştir"],
  "serit": "Memlüklerden önce yenilen devlet", "kanit": [0],
  "secenekler": ["Safevi Devleti", "Memlük Devleti", "Doğu Roma"], "dogru": 0, "tuzak": [1],
  "ipucu": "Olayları sırayla düşün: Memlüklerden önce ne olduğunu anlatan cümleyi bul.", "kanitIpucu": "Memlüklerden önceki savaşı anlatan cümle hangisi?",
  "aciklama": "Yavuz önce 1514'te Çaldıran'da Safevileri yendi, sonra Memlük Devleti üzerine yürüdü (s. 103).", "kavram": "Yavuz Sultan Selim"},
 {"metin": ["Osmanlı'nın denizlerde güçlenmesi Avrupa devletlerini rahatsız etti.", "İspanya, Portekiz, Venedik ve Papalık birleşerek bir Haçlı donanması kurdu.", "Bu donanmanın başına Andrea Doria getirildi.", "1538'de Barbaros, donanmasını Preveze açıklarında hilal şeklinde dizdi.", "Hızlı kadırgalar ve uzun menzilli toplar, ağır Haçlı gemilerini etkisiz hâle getirdi.", "Bu zaferden sonra Akdeniz'de Osmanlı hâkimiyeti pekişti."],
  "soru": "Metne göre Haçlı donanmasının kurulmasının nedeni nedir?", "bolge": ["kurulmasının nedeni nedir"],
  "serit": "Haçlı donanmasının kurulma nedeni", "kanit": [0],
  "secenekler": ["Osmanlı'nın denizlerde güçlenmesi", "Andrea Doria'nın donanmanın başına getirilmesi", "Akdeniz'de Osmanlı hâkimiyetinin pekişmesi"], "dogru": 0, "tuzak": [1, 2],
  "ipucu": "Donanma kurulmadan önce ne olduğunu anlatan cümleyi bul.", "kanitIpucu": "Avrupa devletlerinin neden rahatsız olduğunu anlatan cümle hangisi?",
  "aciklama": "Osmanlı'nın denizlerde güçlenmesinden rahatsız olan İspanya, Portekiz, Venedik ve Papalık birleşerek Haçlı donanması kurdu (s. 105).", "kavram": "Preveze Deniz Zaferi"}]}
