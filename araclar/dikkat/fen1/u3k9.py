TEKRAR = {"u3k9": [
 ("Kanı süzerek kandaki atıkları ve fazla suyu vücuttan atan sisteme {boşaltım sistemi|solunum sistemi|sindirim sistemi} denir.", "s. 130"),
 ("Boşaltım sistemini böbrekler, üreter (idrar borusu), mesane (idrar kesesi) ve {üretra (idrar kanalı)|gırtlak|mide} oluşturur.", "s. 130"),
 ("Böbrekler kanı {süzer|pompalar|depolar}; yararlı maddeleri tekrar kana geçirir, fazla su, tuz, üre gibi atık maddeleri kandan uzaklaştırır.", "s. 132"),
 ("Kandan süzülen atık maddeler {idrarı|safrayı|tükürüğü} oluşturur. Üreter, böbreklerde oluşan idrarı {mesaneye|akciğere|mideye} ileten boru şeklindeki yapıdır.", "s. 132"),
 ("Mesane (idrar kesesi) idrarın vücut dışına atılıncaya kadar {depolandığı|üretildiği|süzüldüğü} kaslı bir yapıdır.", "s. 132"),
 ("Üretra (idrar kanalı), idrar kesesinde biriken idrarı {vücut dışına|kana|mideye} taşır.", "s. 132"),
 ("Karaciğer, sindirim sonucu oluşan zararlı maddeleri {daha az zararlı|daha çok zararlı} maddelere dönüştürür. Deri, terleme yoluyla vücuttaki {su ve tuzun bir kısmını|besin maddelerini} uzaklaştırır.", "s. 133"),
]}
KISA = {"u3k9": [
 {"soru": "Böbreklerin görevi nedir? Yazınız.",
  "tetik": ["nedir"],
  "okut": ["Görevini ve sonucunu yaz (iki parça).", "Benzerlik ve fark yaz.", "Evet ya da hayır yaz."],
  "parcalar": [
   {"bas": "Kana yaptığı:", "ornek": "Kanı süzerek yararlı maddeleri tekrar kana geçirir.", "havuz": ["Besinleri sindirir.", "Havadaki oksijeni kana geçirir."], "k": ["süz"]},
   {"bas": "Fazlalıklara yaptığı:", "ornek": "Fazla su, tuz, üre gibi atık maddeleri kandan uzaklaştırır; bunlar idrarı oluşturur.", "havuz": ["Kanı vücuda pompalar.", "Kan hücrelerini üretir."], "k": ["atık", "idrar"]}],
  "kisa": "Kanı süzer; atık maddeleri kandan uzaklaştırır, bunlar idrarı oluşturur.",
  "cevap": "Böbrekler kanı süzerek yararlı maddelerin tekrar kana geçmesini sağlar. Fazla su, tuz, üre gibi atık maddeleri kandan uzaklaştırır; bu atıklar idrarı oluşturur.",
  "anahtarlar": [{"ad": "kanı süzer", "k": ["süz"]}, {"ad": "atık maddeleri uzaklaştırır / idrar", "k": ["atık", "idrar"]}],
  "sayfa": "s. 132"},
 {"soru": "İdrar böbrekte oluştuktan sonra hangi yapılardan geçerek vücut dışına atılır? Yazınız.",
  "tetik": ["hangi yapılardan"],
  "okut": ["Yapıları sırasıyla yaz (üç parça).", "Benzerlik ve fark yaz.", "Evet ya da hayır yaz."],
  "parcalar": [
   {"bas": "Önce:", "ornek": "Üreter (idrar borusu) ile iletilir.", "havuz": ["Üretra ile iletilir.", "Mesane ile iletilir."], "k": ["üreter", "idrar borusu"]},
   {"bas": "Sonra:", "ornek": "Mesanede (idrar kesesinde) depolanır.", "havuz": ["Üreterde depolanır.", "Böbrekte depolanır."], "k": ["mesane", "idrar kesesi"]},
   {"bas": "En son:", "ornek": "Üretra (idrar kanalı) ile vücut dışına atılır.", "havuz": ["Üreter ile vücut dışına atılır.", "Mesane ile vücut dışına atılır."], "k": ["üretra", "idrar kanalı"]}],
  "kisa": "Üreter ile mesaneye iletilir, mesanede depolanır, üretra ile vücut dışına atılır.",
  "cevap": "Böbrekte oluşan idrar üreter (idrar borusu) ile mesaneye (idrar kesesi) iletilir, mesanede depolanır ve üretra (idrar kanalı) ile vücut dışına atılır.",
  "anahtarlar": [{"ad": "üreter (idrar borusu)", "k": ["üreter", "idrar borusu"]}, {"ad": "mesane (idrar kesesi)", "k": ["mesane", "idrar kesesi"]}, {"ad": "üretra (idrar kanalı)", "k": ["üretra", "idrar kanalı"]}],
  "sayfa": "s. 132"},
]}
ELLE = {"Boşaltım sistemi kandaki neleri vücuttan atar?": "neleri", "Terleme ile vücuttan ne atılır?": "ne atılır", "İdrarın vücut dışına atılıncaya kadar depolandığı yer neresidir?": "neresidir", "Bora maçta çok terledi. Çok su içmesine rağmen idrara sıkışmadı. Bunun nedeni ne olabilir?": "nedeni ne olabilir"}
OKUT = {"u3k9": [
 ["böbreklerin ne iş yaptığını, kana ve atıklara ne yaptığını yazmanı", "böbreklerin vücutta nerede olduğunu söylemeni", "kaç tane böbreğimiz olduğunu yazmanı"],
 ["idrarın böbrekten sonra sırayla hangi yapılardan geçtiğini yazmanı", "idrarın neden oluştuğunu anlatmanı", "günde ne kadar su içmen gerektiğini söylemeni"]]}
METINLI = {"u3k9": [
 {"metin": ["Böbrekler kanı süzer.", "Kandan süzülen fazla su, tuz ve üre gibi atıklar idrarı oluşturur.", "İdrar, üreterle idrar kesesine taşınır."],
  "soru": "İdrar hangi organda oluşur?", "bolge": ["hangi organda oluşur"],
  "serit": "İdrarın oluştuğu organ", "kanit": [0, 1],
  "secenekler": ["Böbreklerde", "İdrar kesesinde", "Üreterde"], "dogru": 0, "tuzak": [1, 2],
  "ipucu": "İdrar nerede taşınıyor, nerede oluşuyor? İkisini karıştırma.", "kanitIpucu": "İdrarın nasıl oluştuğunu söyleyen cümleyi bul.",
  "aciklama": "Böbrekler kanı süzer; kandan süzülen atıklar idrarı oluşturur. Üreter idrarı yalnızca idrar kesesine taşır (s. 132).", "kavram": "Böbrekler"},
 {"metin": ["Bora beden eğitimi dersinde futbol oynadı ve çok su içti.", "Maçtan sonra dinlenirken çok terlediğini fark etti.", "Ders bitince arkadaşları tuvalete gitmek istedi.", "Bora onlardan daha çok su içtiği hâlde idrara sıkışmadığını fark etti."],
  "soru": "Bora'nın çok su içtiği hâlde idrara sıkışmamasının sebebi nedir?", "bolge": ["idrara sıkışmamasının sebebi nedir"],
  "serit": "Bora'nın idrara sıkışmama sebebi", "kanit": [1],
  "secenekler": ["Vücudundaki suyun bir kısmının terle atılması", "Arkadaşlarının tuvalete gitmesi", "Futbol oynarken çok su içmesi"], "dogru": 0, "tuzak": [1, 2],
  "ipucu": "Vücuttaki su idrardan başka hangi yolla atılabilir?", "kanitIpucu": "Bora'nın maçtan sonra fark ettiği şeyi anlatan cümleyi bul.",
  "aciklama": "Deri, vücuttaki su ve tuzun bir kısmını terleme yoluyla uzaklaştırır; bu yüzden Bora'nın idrarı az oldu (s. 129, 133).", "kavram": "Deri"}]}
