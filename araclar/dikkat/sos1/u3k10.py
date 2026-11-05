TEKRAR = {"u3k10": [
 ("Cami, medrese, darüşşifa ve imaret gibi yapıların bir arada bulunduğu yapı topluluğuna {külliye|kervansaray|bedesten} denir.", "s. 136"),
 ("Süleymaniye Külliyesi 16. yüzyılda {Mimar Sinan|Ahi Evran|İbrahim Müteferrika} tarafından yapıldı.", "s. 136"),
 ("Kuzey Afrika ülkelerinin orkestralarında {kanun, ud, ney|piyano, keman, gitar|org, çello, arp} gibi Türk müziği sazları kullanılır.", "s. 138"),
 ("Ülkenin merkezden uzak eyalet ve sancaklarının yönetimine {taşra yönetimi|merkez yönetimi|Divan yönetimi} denir.", "s. 139"),
 ("En önemli yönetim kurumu olan {Divan-ı Hümayun|Tulumbacılar Ocağı|Enderun Mektebi}, Türkiye Selçukluları'ndaki Divan örnek alınarak kuruldu.", "s. 140"),
 ("Padişahtan sonra en yetkili devlet adamı olan {veziriazam|defterdar|nişancı} padişahın mührünü taşırdı.", "s. 141"),
 ("Devletin gelir ve giderlerini {defterdar|kazasker|kaptanıderya} denetlerdi. Donanmadan ise {kaptanıderya|defterdar|nişancı} sorumluydu.", "s. 141"),
]}
KISA = {"u3k10": [
 {"soru": "Merkez yönetimi ile taşra yönetimi arasındaki farkı yazınız.",
  "tetik": ["farkı"],
  "okut": ["", "", ""],
  "parcalar": [
   {"bas": "Merkez yönetimi:", "ornek": "Saray ve Divan-ı Hümayun'un bulunduğu, kararların alındığı başkent yönetimidir.", "havuz": ["Merkezden uzak eyalet ve sancakların yönetimidir.", "Köylerin yönetimidir."], "k": ["başkent", "saray", "divan"]},
   {"bas": "Taşra yönetimi:", "ornek": "Merkezden uzak eyalet ve sancakların yönetimidir.", "havuz": ["Saray ve Divan'ın bulunduğu başkent yönetimidir.", "Padişahın sarayının yönetimidir."], "k": ["uzak", "eyalet", "sancak"]}],
  "kisa": "Merkez: başkent yönetimi. Taşra: uzak eyalet ve sancaklar.",
  "cevap": "Merkez yönetimi, Saray ve Divan-ı Hümayun'un bulunduğu, tüm kararların alındığı başkent yönetimidir. Taşra yönetimi ise ülkenin merkezden uzak eyalet ve sancaklarının yönetimidir.",
  "anahtarlar": [{"ad": "merkez: başkent, Saray ve Divan", "k": ["başkent", "saray", "divan"]}, {"ad": "taşra: uzak eyalet ve sancaklar", "k": ["uzak", "eyalet", "sancak"]}],
  "sayfa": "s. 139"},
 {"soru": "Osmanlı kültürünün izlerinin bugün farklı ülkelerde yaşadığını gösteren iki örnek yazınız.",
  "tetik": ["iki örnek"],
  "okut": ["", "", ""],
  "parcalar": [
   {"bas": "Birinci örnek:", "ornek": "Balkan ülkelerinde baklava, pilav, dolma gibi yemek adları kullanılır.", "havuz": ["Avrupa'da fabrikalar kuruldu.", "Fransa'da ihtilal oldu."], "k": ["baklava", "pilav", "dolma", "kebap", "yemek"]},
   {"bas": "İkinci örnek:", "ornek": "Kuzey Afrika'daki orkestralarda kanun, ud, ney çalınır.", "havuz": ["Amerika'da yeni bir kıta bulundu.", "İngiltere'de buhar makinesi geliştirildi."], "k": ["kanun", "karagöz", "hamidiye", "çarşı", "orkestra"]}],
  "kisa": "Balkanlarda yemek adları; Kuzey Afrika'da kanun, ud, ney.",
  "cevap": "Balkan ülkelerinde baklava, pilav, kebap, dolma gibi yemek adları kullanılır. Kuzey Afrika'daki orkestralarda kanun, ud, ney gibi Türk müziği sazları çalınır. KKTC'de de Karagöz oyunları sahnelenir.",
  "anahtarlar": [{"ad": "bir örnek (yemek adları)", "k": ["baklava", "pilav", "dolma", "kebap", "yemek"]}, {"ad": "ikinci örnek (sazlar, Karagöz, Hamidiye Çarşısı)", "k": ["kanun", "karagöz", "hamidiye", "çarşı", "orkestra"]}],
  "sayfa": "s. 138"},
]}
OKUT = {"u3k10": [
 ["iki yönetimi ayrı ayrı anlatıp farkını göstermeni", "Divan-ı Hümayun'un üyelerini sıralamanı", "padişahın görevlerini yazmanı"],
 ["Osmanlı izlerinin bugün yaşadığını gösteren iki örnek yazmanı", "Osmanlı'nın hangi ülkeleri fethettiğini sıralamanı", "külliyenin ne olduğunu tanımlamanı"]]}
METINLI = {"u3k10": [
 {"metin": ["İlk zamanlar Divan toplantılarına padişahlar başkanlık yapardı.", "Fatih ve ondan sonraki padişahlar bu görevi veziriazamlara bıraktı.", "Padişahlar bundan sonra toplantıları Kasr-ı Adl denilen pencereden izledi."],
  "soru": "Metne göre Fatih Dönemi'nden itibaren Divan toplantılarına kim başkanlık etmiştir?", "bolge": ["Fatih Dönemi'nden itibaren", "kim başkanlık etmiştir"],
  "serit": "Fatih'ten itibaren Divan'a başkanlık eden", "kanit": [1],
  "secenekler": ["Veziriazamlar", "Padişahlar", "Kasr-ı Adl'daki görevliler"], "dogru": 0, "tuzak": [1, 2],
  "ipucu": "“Fatih” kelimesinin geçtiği cümleyi bul; ilk zamanlarla karıştırma.", "kanitIpucu": "“Fatih” hangi cümlede geçiyor?",
  "aciklama": "İlk zamanlar Divan'a padişahlar başkanlık ediyordu. Fatih ve ondan sonraki padişahlar bu görevi veziriazamlara bıraktı ve toplantıları Kasr-ı Adl penceresinden izledi (s. 140).", "kavram": "Divan-ı Hümayun"},
 {"metin": ["Osmanlı kültürünün izleri bugün farklı ülkelerde hâlâ yaşamaktadır.", "Balkan ülkelerinde baklava, pilav, kebap, dolma gibi yemek adlarına sıkça rastlanır.", "Tunus, Cezayir, Libya, Mısır gibi ülkelerin orkestralarında kanun, ud, ney gibi Türk müziği sazları kullanılır.", "Şam'daki Hamidiye Çarşısı Osmanlı Dönemi'nde yapılmıştır.", "KKTC'de Karagöz oyunları sahnelenir."],
  "soru": "Metne göre Tunus ve Cezayir gibi ülkelerde Osmanlı izi hangi alanda görülür?", "bolge": ["Tunus ve Cezayir gibi ülkelerde", "hangi alanda görülür"],
  "serit": "Tunus ve Cezayir'deki Osmanlı izi", "kanit": [2],
  "secenekler": ["Müzikte", "Yemek adlarında", "Çarşı yapılarında"], "dogru": 0, "tuzak": [1, 2],
  "ipucu": "“Tunus” kelimesinin geçtiği cümleyi bul; orada hangi alan anlatılıyor?", "kanitIpucu": "Tunus ve Cezayir hangi cümlede geçiyor?",
  "aciklama": "Tunus, Cezayir, Libya, Mısır gibi ülkelerin orkestralarında kanun, ud, ney gibi Türk müziği sazları kullanılır; bu, müzikteki bir Osmanlı izidir (s. 138).", "kavram": "Osmanlı'nın Yaşayan İzleri"}]}
