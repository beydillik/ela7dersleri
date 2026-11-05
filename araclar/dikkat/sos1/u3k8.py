TEKRAR = {"u3k8": [
 ("Lale Devri 1718'de {Pasarofça Antlaşması|Paris Antlaşması|Tanzimat Fermanı} ile başladı, 1730'da {Patrona Halil İsyanı|Fransız İhtilali|Vaka-i Hayriye} ile sona erdi.", "s. 125"),
 ("Lale Devri'nde {Yirmisekiz Mehmed Çelebi|İbrahim Müteferrika|Barbaros Hayreddin} elçi olarak Fransa'ya gönderildi.", "s. 125"),
 ("1727'de {İbrahim Müteferrika|Yirmisekiz Mehmed Çelebi|Patrona Halil} ilk Türk matbaasını açtı.", "s. 125"),
 ("1720'de kurulan {Tulumbacılar Ocağı|Yeniçeri Ocağı|Lağımcı Ocağı} Osmanlı'nın ilk itfaiye teşkilatıdır.", "s. 126"),
 ("III. Selim'in yenilik çalışmalarına {Nizâm-ı Cedîd|Vaka-i Hayriye|Tanzimat} denir. Bu ad {Yeni Düzen|Hayırlı Olay|Büyük Ferman} anlamına gelir.", "s. 126"),
 ("Nizâm-ı Cedîd Ordusu {Avrupa usullerine|eski yeniçeri usullerine|Memlük usullerine} göre eğitildi.", "s. 127"),
 ("Islahatların giderlerini karşılamak için {İrâd-ı Cedîd Hazinesi|Tulumbacılar Ocağı|Kara Mühendishanesi} kuruldu. Londra, Paris, Berlin ve Viyana'da ilk {daimî elçilikler|fabrikalar|matbaalar} açıldı.", "s. 127"),
]}
KISA = {"u3k8": [
 {"soru": "Lale Devri'nde yapılan yeniliklerden iki tanesini yazınız.",
  "tetik": ["iki tanesini"],
  "okut": ["", "", ""],
  "parcalar": [
   {"bas": "Birinci yenilik:", "ornek": "1727'de İbrahim Müteferrika ilk Türk matbaasını açtı.", "havuz": ["Yeniçeri Ocağı kaldırıldı.", "Tanzimat Fermanı ilan edildi."], "k": ["matbaa", "elçi", "kütüphane"]},
   {"bas": "İkinci yenilik:", "ornek": "1720'de ilk itfaiye teşkilatı olan Tulumbacılar Ocağı kuruldu.", "havuz": ["Nizâm-ı Cedîd Ordusu kuruldu.", "İlk resmî gazete çıkarıldı."], "k": ["tulumba", "itfaiye", "çiçek"]}],
  "kisa": "Matbaa açıldı; Tulumbacılar Ocağı kuruldu.",
  "cevap": "1727'de İbrahim Müteferrika ilk Türk matbaasını açtı. 1720'de ise ilk itfaiye teşkilatı olan Tulumbacılar Ocağı kuruldu. Ayrıca çiçek aşısı yaygınlaştı ve Fransa'ya elçi gönderildi.",
  "anahtarlar": [{"ad": "bir yenilik (matbaa, elçi, kütüphane)", "k": ["matbaa", "elçi", "kütüphane"]}, {"ad": "bir yenilik (Tulumbacılar Ocağı, çiçek aşısı)", "k": ["tulumba", "itfaiye", "çiçek"]}],
  "sayfa": "s. 125–126"},
 {"soru": "Nizâm-ı Cedîd Ordusu neden kurulmuş ve nasıl eğitilmiştir? Yazınız.",
  "tetik": ["neden", "nasıl"],
  "okut": ["", "", ""],
  "parcalar": [
   {"bas": "Neden:", "ornek": "Yeniçeri Ocağı disiplinini yitirmişti.", "havuz": ["Avrupa'ya elçi göndermek gerekiyordu.", "İstanbul'da yangınlar çıkıyordu."], "k": ["disiplin"]},
   {"bas": "Nasıl:", "ornek": "Avrupa usullerine göre eğitildi ve modern silahlarla donatıldı.", "havuz": ["Eski yeniçeri usulleriyle eğitildi.", "Hiç eğitim almadı."], "k": ["avrupa", "modern"]}],
  "kisa": "Yeniçeriler disiplinsizdi; Avrupa usulüyle eğitildi.",
  "cevap": "Yeniçeri Ocağı disiplinini yitirdiği ve devlet eski gücünü kaybettiği için III. Selim yeni bir ordu kurdu. Nizâm-ı Cedîd Ordusu Avrupa usullerine göre eğitildi ve modern silahlarla donatıldı.",
  "anahtarlar": [{"ad": "neden: yeniçeriler disiplinini yitirdi", "k": ["disiplin"]}, {"ad": "nasıl: Avrupa usulleri", "k": ["avrupa", "modern"]}],
  "sayfa": "s. 126–127"},
]}
OKUT = {"u3k8": [
 ["Lale Devri'nde yapılan iki yeniliği yazmanı", "Lale Devri'nin hangi yıllar arasında olduğunu söylemeni", "Lale Devri'nin adını nereden aldığını anlatmanı"],
 ["Nizâm-ı Cedîd Ordusu'nun neden kurulduğunu ve nasıl eğitildiğini anlatmanı", "III. Selim'in diğer yeniliklerini sıralamanı", "Nizâm-ı Cedîd'in ne demek olduğunu söylemeni"]]}
METINLI = {"u3k8": [
 {"metin": ["Lale Devri'ne kadar yangınlara karakollardaki askerler ve halk müdahale ediyordu.", "İstanbul'da ahşap ev çok olduğu için büyük yangınlarda bu yetmiyordu.", "1720'de ilk itfaiye teşkilatı olan Tulumbacılar Ocağı kuruldu."],
  "soru": "Metne göre büyük yangınlarda askerlerin ve halkın müdahalesi neden yetmiyordu?", "bolge": ["neden yetmiyordu"],
  "serit": "Müdahalenin yetmeme nedeni", "kanit": [1],
  "secenekler": ["İstanbul'da ahşap ev çok olduğu için", "Tulumbacılar Ocağı kurulduğu için", "Karakollarda hiç asker olmadığı için"], "dogru": 0, "tuzak": [1, 2],
  "ipucu": "“yetmiyordu” kelimesinin geçtiği cümlede “için” sözcüğünden önce ne yazıyor?", "kanitIpucu": "“yetmiyordu” kelimesi hangi cümlede?",
  "aciklama": "İstanbul'da ahşap ev çok olduğu için büyük yangınlarda askerlerin ve halkın müdahalesi yetmiyordu; bu yüzden 1720'de Tulumbacılar Ocağı kuruldu (s. 126).", "kavram": "Tulumbacılar Ocağı"},
 {"metin": ["Sultan III. Ahmed ve sadrazam Damat İbrahim Paşa, Batı'yı örnek alarak yenilikler yapmak istedi.", "Bu dönemde Yirmisekiz Mehmed Çelebi Efendi elçi olarak Fransa'ya gönderildi.", "Ondan Avrupa'daki bilimsel, kültürel ve teknik gelişmeleri rapor etmesi istendi.", "Böylece Osmanlı yöneticileri Batı'daki ilerlemeleri yakından tanıdı.", "1727'de İbrahim Müteferrika ilk Türk matbaasını açtı ve kitap basımı hızlandı."],
  "soru": "Metne göre Yirmisekiz Mehmed Çelebi'den Fransa'da ne yapması istenmiştir?", "bolge": ["Fransa'da ne yapması istenmiştir"],
  "serit": "Mehmed Çelebi'den istenen görev", "kanit": [2],
  "secenekler": ["Avrupa'daki gelişmeleri rapor etmesi", "İlk Türk matbaasını açması", "Batı'yı örnek alarak yenilikler yapması"], "dogru": 0, "tuzak": [1, 2],
  "ipucu": "“istendi” kelimesinin geçtiği cümleyi bul.", "kanitIpucu": "Ondan ne istendiğini anlatan cümle hangisi?",
  "aciklama": "Yirmisekiz Mehmed Çelebi Efendi'den Avrupa'daki bilimsel, kültürel ve teknik gelişmeleri rapor etmesi istendi. Matbaayı ise İbrahim Müteferrika açtı (s. 125).", "kavram": "Batı ile Yakın İlişkiler"}]}
