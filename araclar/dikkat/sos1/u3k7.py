TEKRAR = {"u3k7": [
 ("Sanayi İnkılabı XVIII. yüzyılın ikinci yarısında {İngiltere|İspanya|Portekiz} topraklarında başladı.", "s. 121"),
 ("James Watt'ın geliştirdiği {buhar makinesi|pusula|matbaa} üretimi değiştirdi.", "s. 121"),
 ("El emeğine dayalı küçük atölyelerin yerini {makineli fabrikalar|kervansaraylar|medreseler} aldı.", "s. 121"),
 ("Kırsal alanlardan şehirlere göç arttı ve fabrikalarda çalışan {işçi sınıfı|soylu sınıfı|din görevlisi sınıfı} ortaya çıktı.", "s. 121"),
 ("Ham madde ihtiyacı artınca Avrupa devletleri {sömürgecilik|istimalet|iskân} faaliyetlerini hızlandırdı.", "s. 121"),
 ("Fransız İhtilali {1789|1839|1919}'da başladı. 14 Temmuz'da halk {Bastille Hapishanesini|Topkapı Sarayını|Wittenberg Kilisesini} ele geçirdi.", "s. 123"),
 ("İhtilalden sonra yayılan {milliyetçilik|hümanizm|sömürgecilik} akımı Osmanlı'da özellikle {Balkanlardaki|Mısır'daki|Anadolu'daki} gayrimüslim toplulukları etkiledi.", "s. 124"),
]}
KISA = {"u3k7": [
 {"soru": "Sanayi İnkılabı'nın Avrupa'da üretimde ve şehirlerde yol açtığı birer değişikliği yazınız.",
  "tetik": ["birer değişikliği"],
  "okut": ["", "", ""],
  "parcalar": [
   {"bas": "Üretimde:", "ornek": "Küçük atölyelerin yerini makineli fabrikalar aldı.", "havuz": ["Şehirlere göç arttı.", "İşçi sınıfı ortaya çıktı."], "k": ["fabrika", "makine"]},
   {"bas": "Şehirlerde:", "ornek": "Köylerden şehirlere göç arttı, şehirler hızla büyüdü.", "havuz": ["Fabrikalarda makineler kullanıldı.", "Buhar makinesi geliştirildi."], "k": ["göç", "büyü", "işçi"]}],
  "kisa": "Üretimde fabrikalar kuruldu; şehirlere göç arttı.",
  "cevap": "Üretimde el emeğine dayalı küçük atölyelerin yerini makinelerin kullanıldığı fabrikalar aldı. Şehirlerde ise kırsal alanlardan göç arttı, şehirler hızla büyüdü ve işçi sınıfı ortaya çıktı.",
  "anahtarlar": [{"ad": "üretim: fabrikalar / makineler", "k": ["fabrika", "makine"]}, {"ad": "şehirler: göç arttı / şehirler büyüdü", "k": ["göç", "büyü", "işçi"]}],
  "sayfa": "s. 121"},
 {"soru": "Fransız İhtilali'nden önce Fransa'da halkın değişim isteğini artıran iki nedeni yazınız.",
  "tetik": ["iki nedeni"],
  "okut": ["", "", ""],
  "parcalar": [
   {"bas": "Birinci neden:", "ornek": "Soylular ve din görevlileri vergi vermezken vergi yükü halkın üzerindeydi.", "havuz": ["Halk Bastille Hapishanesini ele geçirdi.", "Kralın yetkileri sınırlandırıldı."], "k": ["vergi"]},
   {"bas": "İkinci neden:", "ornek": "Aydınlanma ile özgürlük, eşitlik ve adalet düşünceleri yayıldı.", "havuz": ["Fransa yeni sömürgeler kurdu.", "Halk krala çok güveniyordu."], "k": ["özgür", "eşit", "aydınlanma"]}],
  "kisa": "Vergi yükü halktaydı; özgürlük ve eşitlik düşünceleri yayıldı.",
  "cevap": "Soylular ve din görevlileri vergi vermezken vergi yükü halkın üzerindeydi; savaş harcamaları da ekonomiyi zayıflatmıştı. Ayrıca Aydınlanma Çağı ile yayılan özgürlük, eşitlik ve adalet düşünceleri halkın değişim isteğini artırdı.",
  "anahtarlar": [{"ad": "vergi yükü halkın üzerindeydi", "k": ["vergi"]}, {"ad": "özgürlük, eşitlik düşünceleri", "k": ["özgür", "eşit", "aydınlanma"]}],
  "sayfa": "s. 123"},
]}
OKUT = {"u3k7": [
 ["Sanayi İnkılabı'nın üretimde ve şehirlerde yaptığı birer değişikliği yazmanı", "Sanayi İnkılabı'nın hangi ülkede başladığını söylemeni", "buhar makinesini kimin geliştirdiğini yazmanı"],
 ["ihtilalden önce halkın değişim isteğini artıran iki nedeni yazmanı", "ihtilalin sonuçlarını sıralamanı", "ihtilalin hangi yıl başladığını söylemeni"]]}
METINLI = {"u3k7": [
 {"metin": ["Avrupa'da makinelerle seri ve ucuz üretim yapılmaya başlandı.", "Avrupa'dan gelen ucuz mallar, Osmanlı'daki el tezgâhlarını ve küçük imalathaneleri zor duruma düşürdü.", "Yerli üretim azaldı, birçok imalathane kapandı ve işsizlik arttı."],
  "soru": "Metne göre Osmanlı'da birçok imalathanenin kapanmasının nedeni nedir?", "bolge": ["kapanmasının nedeni nedir"],
  "serit": "İmalathanelerin kapanma nedeni", "kanit": [1],
  "secenekler": ["Avrupa'dan gelen ucuz mallar", "Yerli üretimin azalması", "Osmanlı'da makinelerle seri üretim yapılması"], "dogru": 0, "tuzak": [1, 2],
  "ipucu": "İmalathaneleri zor duruma düşüren şeyi anlatan cümleyi bul.", "kanitIpucu": "“zor duruma düşürdü” ifadesi hangi cümlede?",
  "aciklama": "Avrupa'dan gelen ucuz mallar yerli üretimin azalmasına ve birçok imalathanenin kapanmasına yol açtı. Yerli üretimin azalması bunun sonucudur; seri üretim ise Avrupa'da yapılıyordu (s. 122).", "kavram": "Sanayi İnkılabı ve Osmanlı"},
 {"metin": ["Fransa'da savaş harcamaları ekonomiyi zayıflatmıştı.", "Soylular ve din görevlileri vergi vermezken vergi yükü büyük ölçüde halkın üzerindeydi.", "Aydınlanma ile yayılan özgürlük, eşitlik ve adalet düşünceleri halkın değişim isteğini artırdı.", "Kral XVI. Louis yeni vergiler koymak istedi.", "14 Temmuz 1789'da halk Bastille Hapishanesini ele geçirdi.", "İhtilal sürecinde İnsan ve Yurttaş Hakları Bildirgesi yayımlandı."],
  "soru": "Metne göre ihtilalden önce Fransa'da vergi vermeyenler kimlerdi?", "bolge": ["vergi vermeyenler kimlerdi"],
  "serit": "Vergi vermeyenler", "kanit": [1],
  "secenekler": ["Soylular ve din görevlileri", "Halk", "Kral XVI. Louis'nin askerleri"], "dogru": 0, "tuzak": [1, 2],
  "ipucu": "“vergi vermezken” ifadesinin geçtiği cümleyi bul. Vergi yükünü taşıyanlarla karıştırma.", "kanitIpucu": "“vergi vermezken” hangi cümlede?",
  "aciklama": "Soylular ve din görevlileri vergi vermezken vergi yükü büyük ölçüde halkın üzerindeydi (s. 123).", "kavram": "Fransız İhtilali"}]}
