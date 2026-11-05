TEKRAR = {"u3k5": [
 ("İhtiyaç duyulan kanın gönüllü ve sağlıklı kişiler tarafından verilmesine {kan bağışı|organ nakli|kan nakli} denir.", "s. 111"),
 ("18-65 yaş aralığında ve {50|30|80} kg üzerindeki sağlıklı her birey kan bağışçısı olabilir.", "s. 111"),
 ("Kadınlar {dört|üç|altı} ayda, erkekler {üç|dört|iki} ayda bir kan verebilir.", "s. 111"),
 ("Türk Kızılay, ülkemizin ihtiyacı olan kanın tamamını {gönüllü ve sürekli|parayla çalışan|zorunlu} bağışçılardan karşılamayı hedefler.", "s. 111"),
 ("Kişinin hayattayken ya da yaşamı sona erdikten sonra ailesinin rızasıyla doku ve organlarının başkalarının tedavisi için kullanılmasına izin vermesine {organ bağışı|kan bağışı|organ nakli} denir.", "s. 111"),
 ("Görevini yapamayan bir organın yerine yeni ve sağlam bir organın ameliyatla yerleştirilmesine {organ nakli|organ bağışı|kan bağışı} denir.", "s. 111"),
 ("Organ bağışında önce kan ve doku uyumuna, sonra hastanın {tıbbi aciliyet durumuna|zenginliğine|yaşına} bakılır. Organlar cinsiyet, ırk, din ve maddi durum ayrımı {yapılmadan|yapılarak} nakledilir.", "s. 112"),
]}
KISA = {"u3k5": [
 {"soru": "Kan bağışı ile organ bağışı arasındaki farkı yazınız.",
  "tetik": ["farkı"],
  "okut": ["İki bağışı ayrı ayrı tanımla (iki parça).", "Sebep ve sonuç yaz: “… çünkü …”", "Yalnız bir organın adını yaz."],
  "parcalar": [
   {"bas": "Kan bağışı:", "ornek": "İhtiyaç duyulan kanın gönüllü ve sağlıklı kişilerce verilmesidir.", "havuz": ["Doku ve organların başkalarının tedavisi için kullanılmasına izin vermektir.", "Yeni bir organın ameliyatla yerleştirilmesidir."], "k": ["gönüllü"]},
   {"bas": "Organ bağışı:", "ornek": "Kişinin doku ve organlarının başkalarının tedavisi için kullanılmasına izin vermesidir.", "havuz": ["İhtiyaç duyulan kanın gönüllü kişilerce verilmesidir.", "Bozulan organın ameliyatla yenisiyle değiştirilmesidir."], "k": ["doku"]}],
  "kisa": "Kan bağışı: gönüllü kişilerin kan vermesi. Organ bağışı: doku ve organların başkalarının tedavisi için kullanılmasına izin vermek.",
  "cevap": "Kan bağışı, ihtiyaç duyulan kanın gönüllü ve sağlıklı kişiler tarafından verilmesidir. Organ bağışı ise kişinin doku ve organlarının başka hastaların tedavisi için kullanılmasına izin vermesidir.",
  "anahtarlar": [{"ad": "kan bağışı: gönüllü kan verme", "k": ["gönüllü"]}, {"ad": "organ bağışı: doku ve organlar", "k": ["doku"]}],
  "sayfa": "s. 111"},
 {"soru": "Kan bağışında bulunabilmek için gereken iki şartı yazınız.",
  "tetik": ["iki şartı"],
  "okut": ["İki ayrı şart yaz (iki parça).", "Neden ve sonuç yaz.", "Evet ya da hayır yaz."],
  "parcalar": [
   {"bas": "Yaş:", "ornek": "18-65 yaş aralığında olmak.", "havuz": ["10-15 yaş aralığında olmak.", "70 yaşından büyük olmak."], "k": ["18"]},
   {"bas": "Kilo ve sağlık:", "ornek": "50 kg üzerinde ve sağlıklı olmak.", "havuz": ["30 kg üzerinde olmak.", "Hasta ya da zayıf olmak."], "k": ["50"]}],
  "kisa": "18-65 yaş arası olmak; 50 kg üzerinde ve sağlıklı olmak.",
  "cevap": "18-65 yaş aralığında olmak ve 50 kg üzerinde, sağlıklı bir birey olmak gerekir.",
  "anahtarlar": [{"ad": "18-65 yaş", "k": ["18"]}, {"ad": "50 kg üzerinde ve sağlıklı", "k": ["50"]}],
  "sayfa": "s. 111"},
]}
ELLE = {"Kan bağışı kimler tarafından yapılır?": "kimler", "'Kan bağışı ülkemizde yalnızca Türk Kızılaya yapılır.' ifadesi için ne söylenebilir?": "ne söylenebilir", "Kan verdikten sonra ne kadar dinlenmek faydalıdır?": "ne kadar"}
OKUT = {"u3k5": [
 ["kan bağışının ve organ bağışının ne olduğunu ayrı ayrı yazıp farkını göstermeni", "kan bağışının nereye yapıldığını söylemeni", "organ bağışının neden önemli olduğunu anlatmanı"],
 ["kan verebilmek için gereken iki şartı yazmanı", "kan vermenin faydalarını anlatmanı", "kan bağışının kaç adımda yapıldığını söylemeni"]]}
METINLI = {"u3k5": [
 {"metin": ["Kan bağışı için 18-65 yaş arasında olmak gerekir.", "Ayrıca 50 kg'ın üzerinde ve sağlıklı olmak gerekir.", "Kadınlar dört ayda, erkekler üç ayda bir kan verebilir."],
  "soru": "Aşağıdakilerden hangisi kan bağışı yapabilir?", "bolge": ["hangisi kan bağışı yapabilir"],
  "serit": "Kan bağışı yapabilecek kişi", "kanit": [0, 1],
  "secenekler": ["25 yaşında, 60 kg, sağlıklı bir yetişkin", "16 yaşında, 55 kg, sağlıklı bir genç", "30 yaşında, 45 kg, sağlıklı bir yetişkin"], "dogru": 0, "tuzak": [],
  "ipucu": "Her şıkta yaşı ve kiloyu metindeki şartlarla karşılaştır.", "kanitIpucu": "Yaş ya da kilo şartını söyleyen cümleye dokun.",
  "aciklama": "18-65 yaş aralığında ve 50 kg üzerindeki sağlıklı her birey kan bağışçısı olabilir (s. 111).", "kavram": "Kimler Kan Verebilir?"},
 {"metin": ["Özgür televizyonda Kızılay Kan Merkezinde kan stoklarının azaldığını duydu.", "Kan bağışı yapıp yapamayacağını annesine sordu.", "Annesi on sekiz yaşından küçüklerin kan bağışı yapamayacağını söyledi.", "Özgür'ün üzüldüğünü gören annesi Kızılay'a gidip kan bağışı yaptı.", "Bir hafta sonra annesinin telefonuna “Bağışladığınız kan, ihtiyaç sahibine ulaşmıştır.” mesajı geldi."],
  "soru": "Özgür'ün kan bağışı yapamamasının sebebi nedir?", "bolge": ["kan bağışı yapamamasının sebebi nedir"],
  "serit": "Özgür'ün kan veremeyişinin sebebi", "kanit": [2],
  "secenekler": ["On sekiz yaşından küçük olması", "Kan stoklarının azalması", "Annesinin kan bağışı yapması"], "dogru": 0, "tuzak": [1, 2],
  "ipucu": "Annesi Özgür'e ne söyledi?", "kanitIpucu": "Annesinin söylediği cümleyi bul.",
  "aciklama": "Kan bağışçısı olmak için 18-65 yaş aralığında olmak gerekir; Özgür on sekiz yaşından küçüktür (s. 111, 116).", "kavram": "Kimler Kan Verebilir?"}]}
