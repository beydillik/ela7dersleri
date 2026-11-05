TEKRAR = {"u3k5": [
 ("Bir devletin sınırları dışındaki toprakları ele geçirip oradaki kaynakları kendi çıkarı için kullanmasına {sömürgecilik|istimalet|iskân} denir.", "s. 113"),
 ("Osmanlı Devleti {İpek ve Baharat Yollarını|Atlas Okyanusu yollarını|Ümit Burnu'nu} kontrol ettiği için Avrupalılar yeni ticaret yolları aramaya başladı.", "s. 113"),
 ("Avrupalılar pusula ve haritacılığı {Müslümanlardan|Amerika yerlilerinden|Aborjinlerden} öğrendi.", "s. 113"),
 ("Bartolomeu Dias 1487'de {Ümit Burnu'na|Amerika'ya|Avustralya'ya} ulaştı. Vasco da Gama 1497'de deniz yoluyla {Hindistan'a|Amerika'ya|Avustralya'ya} vardı.", "s. 114"),
 ("Kristof Kolomb 1492'de Amerika'nın doğusundaki adalara ulaştı ama burayı {Hindistan|Afrika|Avrupa} sandı.", "s. 114"),
 ("Macellan'ın başlatıp Del Cano'nun tamamladığı yolculuk Dünya'nın {yuvarlak|düz|sabit} olduğunu kanıtladı.", "s. 114"),
 ("Yeni yollar bulununca Osmanlı'nın kontrolündeki ticaret yolları önemini kaybetti ve devletin gelirleri {azaldı|arttı|hiç değişmedi}.", "s. 116"),
]}
KISA = {"u3k5": [
 {"soru": "Coğrafi keşiflerin Avrupa için ve yerli halklar için birer sonucunu yazınız.",
  "tetik": ["birer sonucunu"],
  "okut": ["", "", ""],
  "parcalar": [
   {"bas": "Avrupa için:", "ornek": "Altın, gümüş ve yeni ürünlerle kısa sürede zenginleşti.", "havuz": ["Salgın hastalıklarla nüfusu azaldı.", "Kültürü zorla değiştirildi."], "k": ["zengin", "altın", "gümüş"]},
   {"bas": "Yerli halklar için:", "ornek": "Salgın hastalıklarla nüfusları çok azaldı, kültürleri zarar gördü.", "havuz": ["Kısa sürede zenginleştiler.", "Yeni ticaret yolları buldular."], "k": ["salgın", "nüfus", "kültür", "zarar"]}],
  "kisa": "Avrupa zenginleşti; yerli halkların nüfusu azaldı.",
  "cevap": "Avrupalı devletler sömürgelerden aldıkları altın, gümüş ve tarım ürünleriyle kısa sürede zenginleşti. Yerli halklar ise salgın hastalıklarla karşılaştı, nüfusları çok azaldı ve kültürleri zarar gördü.",
  "anahtarlar": [{"ad": "Avrupa: zenginleşme", "k": ["zengin", "altın", "gümüş"]}, {"ad": "yerli halklar: nüfus azaldı / kültür zarar gördü", "k": ["salgın", "nüfus", "kültür", "zarar"]}],
  "sayfa": "s. 115"},
 {"soru": "Coğrafi keşifler Osmanlı ekonomisini nasıl etkilemiştir? Yazınız.",
  "tetik": ["nasıl"],
  "okut": ["", "", ""],
  "parcalar": [
   {"bas": "Ne oldu:", "ornek": "İpek ve Baharat Yolları önemini kaybetti.", "havuz": ["Osmanlı yeni kıtalar keşfetti.", "Osmanlı sömürgeler kurdu."], "k": ["önem"]},
   {"bas": "Sonucu:", "ornek": "Devletin gelirleri büyük oranda azaldı.", "havuz": ["Osmanlı liman şehirleri büyüdü.", "Ticaret canlandı."], "k": ["gelir"]}],
  "kisa": "Ticaret yolları önemini kaybetti, gelirler azaldı.",
  "cevap": "Yeni ticaret yolları bulununca Osmanlı'nın kontrolündeki İpek ve Baharat Yolları önemini kaybetti. Karadeniz ve Akdeniz ticareti azaldı, liman şehirleri eski önemini yitirdi ve devletin gelirleri büyük oranda azaldı.",
  "anahtarlar": [{"ad": "ticaret yolları önemini kaybetti", "k": ["önem"]}, {"ad": "gelirler azaldı", "k": ["gelir"]}],
  "sayfa": "s. 116"},
]}
OKUT = {"u3k5": [
 ["keşiflerin Avrupa için ve yerli halklar için birer sonucunu yazmanı", "keşiflerin nedenlerini sıralamanı", "Amerika'ya ilk kimin ulaştığını söylemeni"],
 ["keşiflerin Osmanlı ekonomisine etkisini (ne olduğunu ve sonucunu) anlatmanı", "Avrupalıların neden yeni yol aradığını söylemeni", "Osmanlı'nın Avrupalılara ne verdiğini yazmanı"]]}
METINLI = {"u3k5": [
 {"metin": ["Yeni ticaret yolları bulununca İpek ve Baharat Yolları önemini kaybetti.", "Karadeniz ve Akdeniz ticaretinin canlılığı azaldı.", "Osmanlı liman şehirleri eski önemini yitirdi ve devletin gelirleri büyük oranda azaldı."],
  "soru": "Metne göre Osmanlı liman şehirlerinin önemini yitirmesinin nedeni nedir?", "bolge": ["önemini yitirmesinin nedeni nedir"],
  "serit": "Liman şehirlerinin önem yitirme nedeni", "kanit": [0, 1],
  "secenekler": ["Ticaret yollarının önemini kaybetmesi", "Devletin gelirlerinin azalması", "Liman şehirlerinin çok kalabalık olması"], "dogru": 0, "tuzak": [1, 2],
  "ipucu": "Neden, sonuçtan önce gelir: ilk cümlelere bak.", "kanitIpucu": "Liman şehirlerinden önce neyin önemini kaybettiğini anlatan cümle hangisi?",
  "aciklama": "Yeni yollar bulununca İpek ve Baharat Yolları önemini kaybetti; ticaret azalınca liman şehirleri eski önemini yitirdi. Gelirlerin azalması ise bunun sonucudur (s. 116).", "kavram": "Osmanlı İçin Sonuçlar"},
 {"metin": ["Avrupalılar Doğu'nun zenginliklerine ulaşmak için yeni yollar aradı.", "Portekizli denizci Bartolomeu Dias 1487'de Ümit Burnu'na ulaştı.", "Kristof Kolomb 1492'de Amerika'nın doğusundaki adalara ayak bastı ama burayı Hindistan sandı.", "Vasco da Gama 1497'de Ümit Burnu'nu geçerek Hindistan'a ulaştı.", "Macellan sürekli batıya giderek Dünya'nın çevresini dolaşmaya çalıştı; yolculukta öldürülünce seferi Del Cano tamamladı."],
  "soru": "Metne göre deniz yoluyla Hindistan'a ulaşan ilk Avrupalı denizci kimdir?", "bolge": ["Hindistan'a ulaşan ilk Avrupalı denizci kimdir"],
  "serit": "Hindistan'a gerçekten ulaşan ilk denizci", "kanit": [3],
  "secenekler": ["Vasco da Gama", "Kristof Kolomb", "Bartolomeu Dias"], "dogru": 0, "tuzak": [1, 2],
  "ipucu": "Kolomb ulaştığı yeri ne sandı? Gerçekten Hindistan'a ulaşan denizciyi bul.", "kanitIpucu": "“Hindistan'a ulaştı” ifadesi hangi cümlede?",
  "aciklama": "Kolomb ulaştığı adaları Hindistan sandı ama orası Amerika'ydı. Vasco da Gama 1497'de Ümit Burnu'nu geçerek deniz yoluyla Hindistan'a ulaşan ilk Avrupalı denizci oldu (s. 114).", "kavram": "Ümit Burnu ve Hindistan Yolu"}]}
