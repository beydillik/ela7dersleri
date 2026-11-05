TEKRAR = {"u3k11": [
 ("Sıbyan mekteplerinde çocuklar {5-6|10-11|14-15} yaşında başlar, okuma-yazma ve basit dinî bilgiler öğrenirdi.", "s. 142"),
 ("Daha üst düzey eğitimin verildiği {medreseler|sıbyan mektepleri|loncalar} kadı, müderris ve din görevlisi yetiştirdi.", "s. 142"),
 ("Saray içinde kurulan {Enderun Mektebi|Darülfünun|Telgraf Mektebi} devletin üst düzey yöneticilerini yetiştirdi.", "s. 142"),
 ("Batı tarzı ilk okullar özellikle {askerî|tarım|sanat} alanındaki eksikleri gidermek için açıldı.", "s. 142"),
 ("Modern meslek okullarından önce gençlere meslek ve ahlakı {lonca teşkilatları|medreseler|elçilikler} öğretirdi.", "s. 143"),
 ("İslam dininin kurallarına dayanan hukuka {Şer'i Hukuk|Örfi Hukuk|Kanunname} denir. Osmanlı'da adalet işlerini {kadılar|defterdarlar|loncalar} yürüttü.", "s. 144"),
 ("{Mecelle|Kanun-ı Esasi|Kanunname} İslam dünyasının medeni kanun niteliğindeki ilk hukuk metnidir. İlk anayasa olan {Kanun-ı Esasi|Mecelle|Tanzimat Fermanı} II. Abdülhamit Dönemi'nde ilan edildi.", "s. 144"),
]}
KISA = {"u3k11": [
 {"soru": "Sıbyan mektebi ile medrese arasındaki farkı yazınız.",
  "tetik": ["farkı"],
  "okut": ["", "", ""],
  "parcalar": [
   {"bas": "Sıbyan mektebi:", "ornek": "Çocuklara okuma-yazma ve basit dinî bilgiler öğretilirdi.", "havuz": ["Kadı ve müderris yetiştirilirdi.", "Astronomi ve matematik okutulurdu."], "k": ["okuma"]},
   {"bas": "Medrese:", "ornek": "Üst düzey eğitim verilir, kadı ve müderris yetiştirilirdi.", "havuz": ["Çocuklara okuma-yazma öğretilirdi.", "Gençlere meslek öğretilirdi."], "k": ["üst düzey", "kadı", "müderris", "astronomi", "matematik"]}],
  "kisa": "Sıbyan: okuma-yazma. Medrese: üst düzey eğitim, kadı ve müderris.",
  "cevap": "Sıbyan mekteplerinde 5-6 yaşındaki çocuklara okuma-yazma, basit dinî bilgiler ve Kur'an öğretilirdi. Medreselerde ise daha üst düzey eğitim verilir; matematik, astronomi gibi dersler okutulur ve kadı, müderris yetiştirilirdi.",
  "anahtarlar": [{"ad": "sıbyan: okuma-yazma", "k": ["okuma"]}, {"ad": "medrese: üst düzey eğitim, kadı/müderris", "k": ["üst düzey", "kadı", "müderris", "astronomi", "matematik"]}],
  "sayfa": "s. 142"},
 {"soru": "Şer'i Hukuk ile Örfi Hukuk arasındaki farkı yazınız.",
  "tetik": ["farkı"],
  "okut": ["", "", ""],
  "parcalar": [
   {"bas": "Şer'i Hukuk:", "ornek": "İslam dininin kurallarına dayanır.", "havuz": ["Padişahların koyduğu kurallardan oluşur.", "Geleneksel uygulamalara dayanır."], "k": ["islam", "din"]},
   {"bas": "Örfi Hukuk:", "ornek": "Padişahların koyduğu kurallar ve geleneksel uygulamalardan oluşur.", "havuz": ["İslam dininin kurallarına dayanır.", "Kilisenin kurallarına dayanır."], "k": ["padişah", "gelenek"]}],
  "kisa": "Şer'i: İslam dininin kuralları. Örfi: padişahın kuralları ve gelenekler.",
  "cevap": "Şer'i Hukuk İslam dininin kurallarına dayanır. Örfi Hukuk ise padişahların devlet düzenini sağlamak için koyduğu kurallar ve geleneksel uygulamalardan oluşur.",
  "anahtarlar": [{"ad": "Şer'i: İslam dininin kuralları", "k": ["islam", "din"]}, {"ad": "Örfi: padişahın kuralları, gelenek", "k": ["padişah", "gelenek"]}],
  "sayfa": "s. 144"},
]}
OKUT = {"u3k11": [
 ["iki okulu ayrı ayrı anlatıp farkını göstermeni", "Enderun Mektebi'nin nerede kurulduğunu söylemeni", "Batı tarzı okulların adlarını sıralamanı"],
 ["iki hukuku ayrı ayrı anlatıp farkını göstermeni", "Osmanlı'da adalet işlerini kimin yürüttüğünü söylemeni", "Mecelle'yi kimin hazırladığını yazmanı"]]}
METINLI = {"u3k11": [
 {"metin": ["Mecelle, Ahmet Cevdet Paşa öncülüğünde hazırlandı.", "Mecelle, İslam dünyasının medeni kanun niteliğindeki ilk hukuk metnidir.", "Kanun-ı Esasi ise II. Abdülhamit Dönemi'nde ilan edilen ilk anayasadır."],
  "soru": "Metne göre Osmanlı'nın ilk anayasası hangisidir?", "bolge": ["ilk anayasası hangisidir"],
  "serit": "Osmanlı'nın ilk anayasası", "kanit": [2],
  "secenekler": ["Kanun-ı Esasi", "Mecelle", "Ahmet Cevdet Paşa'nın kanunnamesi"], "dogru": 0, "tuzak": [1, 2],
  "ipucu": "“anayasa” kelimesinin geçtiği cümleyi bul.", "kanitIpucu": "“anayasa” hangi cümlede?",
  "aciklama": "Mecelle ilk medeni kanun niteliğindeki hukuk metnidir; ilk anayasa ise II. Abdülhamit Dönemi'nde ilan edilen Kanun-ı Esasi'dir (s. 144).", "kavram": "Mecelle ve Kanun-ı Esasi"},
 {"metin": ["Osmanlı'da çocuklar ilk eğitimi sıbyan mekteplerinde alırdı.", "Burada okuma-yazma, basit dinî bilgiler ve Kur'an öğretilirdi.", "Daha üst düzey eğitim ise medreselerde verilirdi.", "Devletin sınırları genişledikçe idari, askerî ve mali alanlarda yetişmiş insana ihtiyaç arttı.", "Bu ihtiyacı karşılamak için saray içinde Enderun Mektebi açıldı.", "Enderun'daki başarılı öğrenciler devlet görevlisi, komutan veya yönetici oldu."],
  "soru": "Metne göre Enderun Mektebi hangi ihtiyacı karşılamak için açılmıştır?", "bolge": ["hangi ihtiyacı karşılamak için açılmıştır"],
  "serit": "Enderun'un açılma nedeni", "kanit": [3, 4],
  "secenekler": ["Yetişmiş devlet insanına duyulan ihtiyacı", "Çocuklara okuma-yazma öğretme ihtiyacını", "Üst düzey medrese eğitimi ihtiyacını"], "dogru": 0, "tuzak": [1, 2],
  "ipucu": "“ihtiyaç” kelimesinin geçtiği cümleleri oku.", "kanitIpucu": "“ihtiyaç arttı” ifadesi hangi cümlede?",
  "aciklama": "Devletin sınırları genişledikçe idari, askerî ve mali alanlarda yetişmiş insana ihtiyaç arttı; Enderun Mektebi bu ihtiyacı karşılamak için saray içinde açıldı (s. 142).", "kavram": "Enderun Mektebi"}]}
