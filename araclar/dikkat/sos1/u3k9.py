TEKRAR = {"u3k9": [
 ("Sultan II. Mahmud {1808|1839|1856} yılında tahta çıktı ve bozulan kurumları {tamamen yenilemeyi|olduğu gibi korumayı|yabancılara bırakmayı} tercih etti.", "s. 128"),
 ("1826'da Yeniçeri Ocağı'nın kaldırılmasına {Vaka-i Hayriye|Nizâm-ı Cedîd|Tanzimat} denir. Bu ad {Hayırlı Olay|Yeni Düzen|Büyük Ferman} anlamına gelir.", "s. 128"),
 ("1831'de ilk resmî gazete olan {Takvim-i Vekayi|Tercümân-ı Ahvâl|Tasvîr-i Efkâr} çıkarıldı.", "s. 128"),
 ("Tanzimat Fermanı {3 Kasım 1839|14 Temmuz 1789|1826} tarihinde ilan edildi ve {Mustafa Reşid Paşa|Damat İbrahim Paşa|İbrahim Müteferrika} tarafından hazırlandı.", "s. 129"),
 ("Tanzimat Fermanı ile padişah ilk kez {kendi yetkilerini|yeniçerilerin yetkilerini|elçilerin yetkilerini} kendi eliyle sınırladı.", "s. 129"),
 ("Osmanlı sanayileşmesi sermaye, teknoloji ve {nitelikli iş gücü|kütüphane|çeşme} eksikliği yüzünden tam başarıya ulaşamadı.", "s. 130"),
 ("XVIII. yüzyılda Osmanlı kültürüne duyulan ilgiyle {Avrupa|Mısır|Hindistan}'da ortaya çıkan akıma {Türk Modası|Rönesans|Reform} denir.", "s. 133"),
]}
KISA = {"u3k9": [
 {"soru": "II. Mahmud'un askerî alanda ve yönetim alanında yaptığı birer yeniliği yazınız.",
  "tetik": ["birer yeniliği"],
  "okut": ["", "", ""],
  "parcalar": [
   {"bas": "Askerî alanda:", "ornek": "Yeniçeri Ocağı'nı kaldırıp yerine Asâkir-i Mansûre-i Muhammediye'yi kurdu.", "havuz": ["Divan'ı kaldırıp nazırlıkları kurdu.", "İlk resmî gazeteyi çıkardı."], "k": ["yeniçeri", "asâkir", "harbiye"]},
   {"bas": "Yönetim alanında:", "ornek": "Divan teşkilatını kaldırıp yerine nazırlıkları kurdu.", "havuz": ["Yeniçeri Ocağı'nı kaldırdı.", "Mekteb-i Harbiye'yi açtı."], "k": ["nazır", "bakanlık", "nüfus", "posta", "takvim", "gazete"]}],
  "kisa": "Askerî: Yeniçeri Ocağı kaldırıldı. Yönetim: nazırlıklar kuruldu.",
  "cevap": "Askerî alanda 1826'da Yeniçeri Ocağı'nı kaldırdı ve yerine Asâkir-i Mansûre-i Muhammediye adlı düzenli bir ordu kurdu. Yönetim alanında Divan teşkilatını kaldırıp yerine nazırlıkları (bakanlıkları) kurdu.",
  "anahtarlar": [{"ad": "askerî: Yeniçeri Ocağı kaldırıldı / yeni ordu", "k": ["yeniçeri", "asâkir", "harbiye"]}, {"ad": "yönetim: nazırlıklar (nüfus sayımı, posta, gazete)", "k": ["nazır", "bakanlık", "nüfus", "posta", "takvim", "gazete"]}],
  "sayfa": "s. 128"},
 {"soru": "Osmanlı'nın sanayileşme çabaları neden tam başarıya ulaşamamıştır? İki neden yazınız.",
  "tetik": ["neden"],
  "okut": ["", "", ""],
  "parcalar": [
   {"bas": "Birinci neden:", "ornek": "Sermaye ve teknoloji eksikti.", "havuz": ["Osmanlı'da hiç fabrika kurulmadı.", "Sanayi mektepleri hiç açılmadı."], "k": ["sermaye", "teknoloji"]},
   {"bas": "İkinci neden:", "ornek": "Nitelikli iş gücü azdı ve ulaşım ağları yetersizdi.", "havuz": ["Avrupa malları çok pahalıydı.", "Fabrikalara hiç ham madde gelmedi."], "k": ["iş gücü", "ulaşım"]}],
  "kisa": "Sermaye, teknoloji ve nitelikli iş gücü eksikti; ulaşım yetersizdi.",
  "cevap": "Osmanlı'da sermaye, teknoloji ve nitelikli iş gücü eksikliği vardı. Ayrıca ulaşım ağları yetersizdi. Bu yüzden kurulan fabrikalar sanayileşmeyi tam başarıya ulaştıramadı.",
  "anahtarlar": [{"ad": "sermaye / teknoloji eksikliği", "k": ["sermaye", "teknoloji"]}, {"ad": "nitelikli iş gücü / ulaşım eksikliği", "k": ["iş gücü", "ulaşım"]}],
  "sayfa": "s. 130"},
]}
OKUT = {"u3k9": [
 ["II. Mahmud'un askerî alanda ve yönetimde yaptığı birer yeniliği yazmanı", "II. Mahmud'un hangi yıl tahta çıktığını söylemeni", "II. Mahmud'un açtığı okulları sıralamanı"],
 ["sanayileşmenin tam başarılı olamamasının iki nedenini yazmanı", "Osmanlı'da hangi fabrikaların kurulduğunu sıralamanı", "sanayi mekteplerinde ne öğretildiğini söylemeni"]]}
METINLI = {"u3k9": [
 {"metin": ["1826'da II. Mahmud Yeniçeri Ocağı'nı kaldırdı.", "Bu olaya Vaka-i Hayriye denir.", "Yeniçerilerin yerine Asâkir-i Mansûre-i Muhammediye adlı yeni bir ordu kuruldu."],
  "soru": "Metne göre Yeniçeri Ocağı'nın yerine ne kurulmuştur?", "bolge": ["yerine ne kurulmuştur"],
  "serit": "Yeniçerilerin yerine kurulan", "kanit": [2],
  "secenekler": ["Asâkir-i Mansûre-i Muhammediye", "Vaka-i Hayriye", "Nizâm-ı Cedîd Ordusu"], "dogru": 0, "tuzak": [1],
  "ipucu": "“yerine” kelimesinin geçtiği cümleyi bul.", "kanitIpucu": "“yerine” kelimesi hangi cümlede?",
  "aciklama": "Vaka-i Hayriye, Yeniçeri Ocağı'nın kaldırılması olayının adıdır. Yeniçerilerin yerine Asâkir-i Mansûre-i Muhammediye adlı ordu kuruldu (s. 128).", "kavram": "Vaka-i Hayriye"},
 {"metin": ["3 Kasım 1839'da Sultan Abdülmecid zamanında Tanzimat Fermanı ilan edildi.", "Fermanı Mustafa Reşid Paşa hazırladı.", "Fermanın diğer adı Gülhane-i Hatt-ı Hümâyunu'dur.", "Bu fermanla padişah ilk kez kendi yetkilerini kendi eliyle sınırladı.", "Devlet, halkına bazı temel hak ve güvenceler sağlamayı kabul etti.", "Eğitim işlerini düzenlemek için Meclis-i Maârif-i Umûmiye kuruldu."],
  "soru": "Metne göre Tanzimat Fermanı ile padişahın yetkilerine ne olmuştur?", "bolge": ["padişahın yetkilerine ne olmuştur"],
  "serit": "Padişahın yetkilerine olan", "kanit": [3],
  "secenekler": ["Padişah kendi yetkilerini ilk kez kendi eliyle sınırladı.", "Padişahın yetkileri arttı.", "Padişah, yetkilerini Mustafa Reşid Paşa'ya devretti."], "dogru": 0, "tuzak": [1, 2],
  "ipucu": "“yetkilerini” kelimesinin geçtiği cümleyi bul.", "kanitIpucu": "“yetkilerini” hangi cümlede?",
  "aciklama": "Tanzimat Fermanı ile padişah ilk kez kendi yetkilerini kendi eliyle sınırladı; devlet halkına temel hak ve güvenceler sağlamayı kabul etti (s. 129).", "kavram": "Tanzimat Fermanı"}]}
