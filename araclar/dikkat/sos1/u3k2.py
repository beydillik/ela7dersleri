TEKRAR = {"u3k2": [
 ("Osmanlı fetihlerini daha çok {batıya|doğuya|güneye}, zayıflayan Doğu Roma ve Balkanlar üzerine yoğunlaştırdı.", "s. 94"),
 ("Osmanlı'nın büyük bir cihan devleti olmasında {gaza ve cihat|ticaret ve sanayi|keşif ve sömürge} anlayışı önemli rol oynadı.", "s. 94"),
 ("{Ahiler|Abdallar|Memlükler} bir esnaf teşkilatıydı; Türkmenlerle birlikte Osmanlı'ya destek verdi.", "s. 94"),
 ("Fethedilen yerlere halkı yerleştirmeye {iskân|istimalet|sömürgecilik} denir. Yeni topraklara ağırlıklı olarak {Anadolu'dan|Avrupa'dan|Afrika'dan} getirilen Türk-Müslüman topluluklar yerleştirildi.", "s. 94"),
 ("İskânın yarattığı nüfus hareketleriyle birçok yeni {kasaba ve şehir|okyanus yolu|sömürge} doğdu.", "s. 94"),
 ("Halkla barış ve düzeni sağlamayı amaçlayan {istimalet|iskân|fetih} politikası özellikle {gayrimüslim|konargöçer|Türkmen} halka ılımlı davranmayı esas aldı.", "s. 95"),
 ("{Derviş ve abdallar|Haçlı askerleri|Avrupalı tüccarlar} halkın güvenini kazanarak istimalet politikasının uygulanmasına katkı sağladı.", "s. 95"),
]}
KISA = {"u3k2": [
 {"soru": "İskân politikası ile istimalet politikası arasındaki farkı yazınız.",
  "tetik": ["farkı"],
  "okut": ["", "", ""],
  "parcalar": [
   {"bas": "İskân:", "ornek": "Fethedilen yerlere Anadolu'dan getirilen Türk-Müslüman halkı yerleştirmektir.", "havuz": ["Halka ılımlı davranıp gönlünü kazanmaktır.", "Fethedilen yerleri boşaltmaktır."], "k": ["yerleş"]},
   {"bas": "İstimalet:", "ornek": "Halka adaletli ve ılımlı davranarak gönlünü kazanmaktır.", "havuz": ["Halkı yeni topraklara taşımaktır.", "Ticaret yollarını kontrol etmektir."], "k": ["gönl", "ılımlı", "adalet"]}],
  "kisa": "İskân: halkı yerleştirmek. İstimalet: halka ılımlı davranıp gönlünü kazanmak.",
  "cevap": "İskân, fethedilen yerlerde kalıcı olmak için Anadolu'dan getirilen Türk-Müslüman toplulukları oraya yerleştirmektir. İstimalet ise fethedilen yerlerdeki halka adaletli ve ılımlı davranarak gönlünü kazanmaktır.",
  "anahtarlar": [{"ad": "iskân: yerleştirme", "k": ["yerleş"]}, {"ad": "istimalet: ılımlı davranıp gönül kazanma", "k": ["gönl", "ılımlı", "adalet"]}],
  "sayfa": "s. 94–95"},
 {"soru": "Derviş ve abdallar istimalet politikasına nasıl katkı sağlamıştır? Yazınız.",
  "tetik": ["nasıl"],
  "okut": ["", "", ""],
  "parcalar": [
   {"bas": "Ne yaptılar:", "ornek": "Gayrimüslim halkın güvenini kazandılar, Türk kültürünü ve İslamiyet'i tanıttılar.", "havuz": ["Halka ağır vergiler koydular.", "Halkı bölgeden çıkardılar."], "k": ["güven"]},
   {"bas": "Sonucu:", "ornek": "Halkın devlete bağlılığı arttı.", "havuz": ["Bölgede isyanlar çoğaldı.", "Halk yeni yönetimden uzaklaştı."], "k": ["bağlı"]}],
  "kisa": "Halkın güvenini kazandılar; halkın devlete bağlılığı arttı.",
  "cevap": "Derviş ve abdallar fethedilen yerlerdeki gayrimüslim halkın güvenini kazandılar ve onlara Türk kültürünü ve İslamiyet'i tanıttılar. Böylece huzur ve güven ortamı oluştu, halkın devlete bağlılığı arttı.",
  "anahtarlar": [{"ad": "halkın güvenini kazandılar", "k": ["güven"]}, {"ad": "devlete bağlılık arttı", "k": ["bağlı"]}],
  "sayfa": "s. 95"},
]}
OKUT = {"u3k2": [
 ["iki politikayı ayrı ayrı anlatıp farkını göstermeni", "yalnız iskân politikasının amaçlarını sıralamanı", "Osmanlı'nın hangi yöne ilerlediğini söylemeni"],
 ["derviş ve abdalların ne yaptığını ve bunun sonucunu anlatmanı", "derviş ve abdalların kim olduğunu tanımlamanı", "istimalet politikasının adını yazmanı"]]}
METINLI = {"u3k2": [
 {"metin": ["Osmanlı, fethettiği yerlerde halka adaletli davrandı.", "Halkın can, mal ve inanç güvenliğini korudu.", "Bu politikaya istimalet adı verilir."],
  "soru": "Metne göre Osmanlı fethettiği yerlerde halkın hangi güvenliklerini korumuştur?", "bolge": ["halkın hangi güvenliklerini korumuştur"],
  "serit": "Korunan güvenlikler", "kanit": [1],
  "secenekler": ["Can, mal ve inanç güvenliğini", "Yalnızca sınır güvenliğini", "Ticaret yollarının güvenliğini"], "dogru": 0, "tuzak": [1, 2],
  "ipucu": "“korudu” kelimesinin geçtiği cümleyi bul.", "kanitIpucu": "Hangi cümlede “güvenliğini korudu” yazıyor?",
  "aciklama": "İstimalet politikasıyla halkın can, mal ve inanç güvenliğini korumak, farklı din ve kültürlere saygı göstermek amaçlandı (s. 95).", "kavram": "İstimalet Politikası"},
 {"metin": ["Orhan Gazi Bursa'yı fethettikten sonra, Hisar'ın tesliminde yardımcı olan Saroz'a Hisar'ı neden verdiklerini sordu.", "Saroz, Osmanlı Devleti'nin günden güne büyüdüğünü söyledi.", "Kendi devletlerinde ağır vergiler ve adaletsizlik altında ezildiklerini anlattı.", "Osmanlı'ya itaat eden köylerin rahat yaşadığını gördüklerini belirtti.", "Bu yüzden kendilerinin de o rahatlığa heves ettiğini söyledi."],
  "soru": "Metne göre Saroz, kendi devletlerinde nasıl bir yönetim altında yaşadıklarını söylemiştir?", "bolge": ["kendi devletlerinde", "nasıl bir yönetim altında yaşadıklarını"],
  "serit": "Saroz'un kendi devletindeki yönetim", "kanit": [2],
  "secenekler": ["Ağır vergiler ve adaletsizlik altında", "Günden güne büyüyen güçlü bir devlette", "Rahat ve huzurlu bir köy hayatında"], "dogru": 0, "tuzak": [1, 2],
  "ipucu": "Saroz'un kendi devletini anlattığı cümleyi bul; Osmanlı'yı anlattığı cümlelerle karıştırma.", "kanitIpucu": "“Kendi devletlerinde” ifadesi hangi cümlede?",
  "aciklama": "Saroz, kendi devletlerinde ağır vergiler ve adaletsizlik altında ezildiklerini söyledi. Günden güne büyüyen ve köyleri rahat olan devlet ise Osmanlı'ydı (s. 95).", "kavram": "İstimalet Politikası"}]}
