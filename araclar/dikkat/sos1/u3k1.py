TEKRAR = {"u3k1": [
 ("26 Ağustos {1071|1453|1517}'de yapılan Malazgirt Savaşı'ndan sonra Anadolu'da Türk beylikleri kuruldu.", "s. 86"),
 ("Osmanlı Beyliği, Osman Bey Dönemi'nde Anadolu'nun kuzeybatısında {Söğüt|Edirne|Kahire} ve çevresinde kuruldu.", "s. 88"),
 ("Orhan Bey Dönemi'nde {Bursa|Edirne|İstanbul} başkent oldu. I. Murad Dönemi'nde ise {Edirne|Bursa|İznik} başkent oldu.", "s. 89"),
 ("{Karesioğulları|Dulkadiroğulları|Germiyanoğulları} Beyliği'nin katılmasıyla Osmanlı'da denizcilik faaliyetleri başladı.", "s. 89"),
 ("Kanuni Sultan Süleyman Dönemi'nde Osmanlı {Avrupa, Asya ve Afrika|yalnız Anadolu|yalnız Avrupa}'da geniş bir coğrafyaya hâkim oldu.", "s. 89"),
 ("Tarih, bir milletin {ortak hafızasıdır|günlük haberidir|ders kitabıdır}.", "s. 92"),
 ("Dünya çapında büyük bir güce ve etkiye sahip devlete {cihan devleti|beylik|sömürge} denir. Güçlü {merkezî otorite|kilise otoritesi|yabancı yardım} sayesinde Osmanlı uzun yıllar ayakta kaldı.", "s. 93"),
]}
KISA = {"u3k1": [
 {"soru": "Küçük bir beylik olan Osmanlı'nın kısa sürede büyümesinde etkili olan iki etkeni yazınız.",
  "tetik": ["iki etkeni"],
  "okut": ["", "", ""],
  "parcalar": [
   {"bas": "Birinci etken:", "ornek": "Farklı dönemlerde gerçekleştirilen fetihler etkili oldu.", "havuz": ["Başka devletler toprak hediye etti.", "Yalnızca şans etkili oldu."], "k": ["fetih"]},
   {"bas": "İkinci etken:", "ornek": "Coğrafi konumun sağladığı avantajlar etkili oldu.", "havuz": ["Beylik denizden çok uzaktaydı.", "Beyliğin hiç komşusu yoktu."], "k": ["coğraf", "konum", "politika"]}],
  "kisa": "Fetihler ve coğrafi konumun avantajları.",
  "cevap": "Osmanlı farklı dönemlerde yaptığı fetihlerle topraklarını genişletti. Ayrıca izlediği politikalar ve coğrafi konumunun sağladığı avantajlar da büyümesinde etkili oldu.",
  "anahtarlar": [{"ad": "fetihler", "k": ["fetih"]}, {"ad": "coğrafi konum / izlenen politikalar", "k": ["coğraf", "konum", "politika"]}],
  "sayfa": "s. 88"},
 {"soru": "Cihan devleti ne demektir ve Türk devletleri bu anlayışla neyi amaçlamıştır? Yazınız.",
  "tetik": ["ne demektir", "neyi amaçlamıştır"],
  "okut": ["", "", ""],
  "parcalar": [
   {"bas": "Anlamı:", "ornek": "Dünya çapında büyük bir güce ve etkiye sahip olan devlettir.", "havuz": ["Yalnız bir şehri yöneten küçük devlettir.", "Başka bir devlete bağlı olan topraktır."], "k": ["güç", "etki"]},
   {"bas": "Amacı:", "ornek": "Dünyada adalet ve düzeni sağlamayı amaçladılar.", "havuz": ["Yeni okyanuslar keşfetmeyi amaçladılar.", "Sadece ticaret yapmayı amaçladılar."], "k": ["adalet", "düzen"]}],
  "kisa": "Dünya çapında güçlü ve etkili devlet; amaç adalet ve düzen.",
  "cevap": "Cihan devleti, dünya çapında büyük bir güce ve etkiye sahip olan devlettir. Türk devletleri bu anlayışla dünyada adalet ve düzeni sağlamayı amaçlamıştır. İslamiyet'in kabulünden sonra buna İslam dinini yayma düşüncesi de eklenmiştir.",
  "anahtarlar": [{"ad": "büyük güç ve etki", "k": ["güç", "etki"]}, {"ad": "adalet ve düzen", "k": ["adalet", "düzen"]}],
  "sayfa": "s. 93"},
]}
OKUT = {"u3k1": [
 ["Osmanlı'nın kısa sürede büyümesini sağlayan iki etkeni yazmanı", "Osmanlı Beyliği'nin nerede kurulduğunu söylemeni", "Osmanlı'nın hangi şehirleri başkent yaptığını sıralamanı"],
 ["cihan devletinin anlamını ve bu anlayışın amacını yazmanı", "Osmanlı'nın hangi kıtalara yayıldığını söylemeni", "cihan devletine bir örnek ad vermeni"]]}
METINLI = {"u3k1": [
 {"metin": ["Osmanlı Beyliği, Osman Bey Dönemi'nde Söğüt ve çevresinde kuruldu.", "Orhan Bey Dönemi'nde Bursa fethedildi ve başkent oldu.", "I. Murad Dönemi'nde ise Edirne başkent oldu."],
  "soru": "Metne göre Orhan Bey Dönemi'nde hangi şehir başkent olmuştur?", "bolge": ["Orhan Bey Dönemi'nde", "hangi şehir başkent olmuştur"],
  "serit": "Orhan Bey Dönemi'nde başkent olan şehir", "kanit": [1],
  "secenekler": ["Bursa", "Edirne", "Söğüt"], "dogru": 0, "tuzak": [1, 2],
  "ipucu": "Orhan Bey'in adının geçtiği cümleyi bul.", "kanitIpucu": "“Orhan Bey” hangi cümlede geçiyor?",
  "aciklama": "Orhan Bey Dönemi'nde Bursa fethedildi ve başkent oldu. Edirne ise I. Murad Dönemi'nde başkent oldu (s. 89).", "kavram": "Orhan Bey ve I. Murad Dönemleri"},
 {"metin": ["Osman Bey Dönemi'nde küçük bir beylik olarak kurulan Osmanlı, Doğu Roma sınırındaki fetihlerle büyümeye başladı.", "Orhan Bey Dönemi'nde Karesioğulları Beyliği'nin katılmasıyla denizcilik faaliyetleri başladı.", "Böylece Rumeli'ye geçildi ve Avrupa'daki ilk fetihler yapıldı.", "I. Murad Dönemi'nde Anadolu beyliklerinden çeyiz ve satın alma yoluyla topraklar kazanıldı.", "Yavuz Sultan Selim Dönemi'nde Mısır'ın fethiyle kutsal toprakların yönetimi Osmanlı'ya geçti.", "Kanuni Dönemi'nde ise devlet Avrupa, Asya ve Afrika'da geniş bir coğrafyaya hâkim oldu."],
  "soru": "Metne göre Osmanlı'nın Rumeli'ye geçebilmesini sağlayan gelişme hangisidir?", "bolge": ["Rumeli'ye geçebilmesini sağlayan gelişme hangisidir"],
  "serit": "Rumeli'ye geçişi sağlayan gelişme", "kanit": [1, 2],
  "secenekler": ["Denizcilik faaliyetlerinin başlaması", "Çeyiz ve satın alma yoluyla toprak kazanılması", "Mısır'ın fethedilmesi"], "dogru": 0, "tuzak": [1, 2],
  "ipucu": "“Rumeli” kelimesinin geçtiği cümleye ve ondan önceki cümleye bak.", "kanitIpucu": "Rumeli'ye geçişi anlatan cümle ya da hemen öncesindeki cümle hangisi?",
  "aciklama": "Karesioğulları Beyliği'nin katılmasıyla denizcilik faaliyetleri başladı ve Rumeli'ye geçildi (s. 89).", "kavram": "Orhan Bey ve I. Murad Dönemleri"}]}
