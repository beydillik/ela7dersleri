TEKRAR = {"u3k4": [
 ("Kan; vücutta madde iletiminden sorumlu, kalp tarafından pompalanan {kırmızı|mavi|sarı} renkli sıvıdır.", "s. 107"),
 ("Kan, kan plazması ve kan hücrelerinden oluşur. Kan hücreleri alyuvar, akyuvar ve {kan pulcukları|plazma|enzim} olmak üzere üç gruba ayrılır.", "s. 107"),
 ("Kanın sıvı kısmına {plazma|alyuvar|akyuvar} denir; büyük bölümünü {su|yağ|protein} oluşturur.", "s. 107"),
 ("Kana kırmızı rengi veren ve sayısı en fazla olan hücreler {alyuvarlardır|akyuvarlardır|kan pulcuklarıdır}. Alyuvarlar {oksijen ve karbon dioksidin|besinlerin ve suyun|mikropların} taşınmasında görevlidir.", "s. 107"),
 ("Beyaz kan hücreleri olan {akyuvarlar|alyuvarlar} kanda en az sayıda bulunur; vücudu {mikroplara karşı savunur|oksijen taşır|pıhtı oluşturur}.", "s. 107"),
 ("Yaralanmalarda {kan pulcukları|akyuvarlar|alyuvarlar} damarların iç yüzeyinde pıhtılaşarak zedelenen kısmı tıkar ve kan kaybını önler.", "s. 107"),
 ("Kan hücrelere besin, oksijen ve hormon taşır; hücrelerdeki {atık maddeleri|vitaminleri} ilgili organlara taşır. Ayrıca vücut {sıcaklığını|ağırlığını|boyunu} düzenler.", "s. 107"),
]}
KISA = {"u3k4": [
 {"soru": "Alyuvar ile akyuvar arasındaki farkı yazınız.",
  "tetik": ["farkı"],
  "okut": ["İki hücreyi ayrı ayrı tanımla (iki parça).", "Sebep ve sonuç yaz: “… çünkü …”", "Yalnız bir organın adını yaz."],
  "parcalar": [
   {"bas": "Alyuvar:", "ornek": "Kana kırmızı rengi verir; oksijen ve karbon dioksit taşır.", "havuz": ["Mikroplara karşı savunma yapar.", "Pıhtılaşmayı sağlar."], "k": ["oksijen"]},
   {"bas": "Akyuvar:", "ornek": "Vücudu mikroplara karşı savunur.", "havuz": ["Oksijen taşır.", "Kana kırmızı rengi verir."], "k": ["mikrop", "savun"]}],
  "kisa": "Alyuvar oksijen ve karbon dioksit taşır; akyuvar mikroplara karşı savunur.",
  "cevap": "Alyuvarlar kana kırmızı rengi verir ve oksijen ile karbon dioksidin taşınmasında görevlidir. Akyuvarlar ise vücudu mikroplara karşı savunur ve kanda en az sayıda bulunur.",
  "anahtarlar": [{"ad": "alyuvar: oksijen / karbon dioksit taşır", "k": ["oksijen"]}, {"ad": "akyuvar: mikroplara karşı savunur", "k": ["mikrop", "savun"]}],
  "sayfa": "s. 107"},
 {"soru": "Yaralanmalarda kan kaybı nasıl önlenir? Yazınız.",
  "tetik": ["nasıl"],
  "okut": ["Hangi hücre ve ne yaptığını yaz (iki parça).", "Benzerlik ve fark yaz.", "Evet ya da hayır yaz."],
  "parcalar": [
   {"bas": "Görevli hücre:", "ornek": "Kan pulcukları.", "havuz": ["Alyuvarlar.", "Akyuvarlar."], "k": ["pulcuk"]},
   {"bas": "Ne yapar:", "ornek": "Damarların iç yüzeyinde pıhtılaşır ve zedelenen kısmı tıkar.", "havuz": ["Mikropları yok eder.", "Oksijeni yaralı bölgeye taşır."], "k": ["pıhtı", "tıka"]}],
  "kisa": "Kan pulcukları pıhtılaşarak zedelenen kısmı tıkar.",
  "cevap": "Yaralanmalarda kan pulcukları damarların iç yüzeyinde pıhtılaşır ve zedelenen kısmı tıkayarak kan kaybını önler.",
  "anahtarlar": [{"ad": "kan pulcukları", "k": ["pulcuk"]}, {"ad": "pıhtılaşarak yarayı tıkar", "k": ["pıhtı", "tıka"]}],
  "sayfa": "s. 107"},
]}
ELLE = {"Kanın sıvı kısmına ne ad verilir?": "ne ad verilir"}
OKUT = {"u3k4": [
 ["alyuvarın ve akyuvarın her birinin ne işe yaradığını ayrı ayrı yazmanı", "kanda hangisinin daha çok bulunduğunu söylemeni", "kanın ne renk olduğunu anlatmanı"],
 ["kan kaybını hangi hücrelerin, ne yaparak durdurduğunu yazmanı", "yaralanınca ne yapman gerektiğini anlatmanı", "kanın kaç bölümden oluştuğunu söylemeni"]]}
METINLI = {"u3k4": [
 {"metin": ["Kanın büyük bir kısmı sıvıdır.", "Kanın bu sıvı kısmına plazma denir.", "Plazmada besin, atık madde, enzim ve hormonlar bulunur."],
  "soru": "Kanda besin ve hormonları taşıyan sıvı kısmın adı nedir?", "bolge": ["sıvı kısmın adı nedir"],
  "serit": "Kanın sıvı kısmının adı", "kanit": [1],
  "secenekler": ["Plazma", "Alyuvar", "Enzim"], "dogru": 0, "tuzak": [2],
  "ipucu": "“Sıvı kısmına … denir” diyen cümleyi oku.", "kanitIpucu": "Sıvı kısmın adını veren cümleyi bul.",
  "aciklama": "Kanın sıvı kısmı plazmadır. Büyük bölümü sudur; içinde besin, atık madde, enzim ve hormon bulunur (s. 107).", "kavram": "Plazma"},
 {"metin": ["Zeynep bahçede koşarken düştü ve dizi kanadı.", "Annesi yarayı temiz bir bezle hafifçe bastırdı.", "Bir süre sonra kanama durdu ve yaranın üstünde koyu renkli bir tabaka oluştu.", "Zeynep bu tabakanın kandaki bazı yapılar sayesinde oluştuğunu derste öğrenmişti.", "Bu yapılar damarın zedelenen yerinde pıhtılaşarak yarayı tıkar."],
  "soru": "Zeynep'in kanamasının durmasını sağlayan kan yapıları hangileridir?", "bolge": ["durmasını sağlayan kan yapıları hangileridir"],
  "serit": "Kanamayı durduran kan yapıları", "kanit": [4],
  "secenekler": ["Kan pulcukları", "Akyuvarlar", "Alyuvarlar"], "dogru": 0, "tuzak": [],
  "ipucu": "Metin bu yapıların ne yaptığını söylüyor: pıhtılaşmak. Pıhtılaşmayı hangi yapılar sağlar?", "kanitIpucu": "Yapıların ne yaptığını anlatan cümleyi bul.",
  "aciklama": "Yaralanmalarda kan pulcukları damarların iç yüzeyinde pıhtılaşır, zedelenen kısmı tıkayarak kan kaybını önler (s. 107). (Zeynep'in hikâyesi kitap dışı bir örnektir; bilgi kitaptandır.)", "kavram": "Kan Pulcukları"}]}
