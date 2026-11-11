# Motor notları (Faz 1 eki, Faz 2–3)

Bu notlar 15 Ekim 2026'da ela-ders-defteri skill'inin 10. bölümüne taşındı (skill güncellemesi Kemal'in onayına sunuldu). Burada çalışma kopyası olarak duruyor.

## Veli Paneli (`public/veli/`)
- Ana sayfanın alt bilgisinde küçük "Veli" bağlantısı. Ders sayfalarındaki `#rapor` buraya yönlenir.
- Kod `ortak/defter.js` içinde (`bootVeli`, `veliGenel`, `veliDers`, `konuDurumu`, `raporIndir`). `veli/index.html` gövdesinde `data-sayfa="veli"`.
- Sekmeler: Genel (son 7 gün, 14 günlük grafik, günler, oturumlar, yanlış sorular, rapor indirme, ayarlar, tam yedek) + her ders.
- Rapor JSON: `konuDurumu` (konu konu Öğren, test ilk/son, zorlandığı kavramlar, Ara Durak tarama ve sınav provası), `oturumlar`, `olaylar`, `sozluk`.

## Tasarım
- **Konu menüsü (30 Ekim 2026):** eski üst menü (`.nav`, `#units`, `#topics`, `openUnit`) kaldırıldı. Ders sayfası iskeleti: `body.ders-sayfa` → ince `.masthead` (dar ekranda `#yanAc` ☰) + `.duzen` [`aside#yan.yan` (`.yan-tam` ağaç, `.yan-ray` dar şerit) | `.wrap > #content`] + `.yan-perde`.
  - Geniş ekran (≥ 900 px): solda yapışkan ağaç (`agacHTML`); yalnız açık ünite genişler (`S.agacUnit`; yeni konu açılınca onun ünitesi). Ünite başlığına dokunmak yalnız açar/kapar, konu açmaz; açık ünite başlığı liste içinde yapışkan.
  - Dar şerit `body.menu-dar` (`rayHTML`: ☰, ünite numaraları, açık konu numarası); ☰ ya da ünite numarası → `body.menu-goz` (menü üstte açılır, perde). Dar ekran (< 900 px): menü çekmece `body.cekmece-acik` (☰ bantta ve şeritte; Esc/perde kapatır).
  - Veli ayarı `menu`: `acik` (**varsayılan**, 11 Kasım 2026, Kemal'in kararı: menü kendiliğinden gizlenmez) / `otomatik` (Normal modda açık; Destekli, Odaklı, Özel modda konu açıkken dar) / `dar`. Eski sıra: / `acik` / `dar`; mod eşleşmesinin (`modBul`) dışında, değişince işaret (`tur: "menu"`). Ela'nın “« Daralt” / “Açık kalsın” seçimi `ela7:menu-el` = `{v, imza}` (cihaza özgü, `BULUT_HARIC`); imza = `menu|mod`, veli ayarı ya da mod değişince geçersiz. Olay `menu` (`secim`).
  - `.serit` korunur: kaydırınca konu adı + sekmeler; geniş ekranda menünün sağından başlar ve açık menüde ☰ gizlidir. Fareyle üzerine gelince açılmaz (bilerek).
  - Bant desenleri yazının arkasında silinir (`drawStars` sonunda `destination-out`); yeni desen eklerken ayrıca başlık boşluğu bırakmak gerekmez.
  - Playwright: tam sayfa görüntüde yapışkan menü sorun çıkarmaz; menü testinde `[data-dar]`, `[data-ac]`, `[data-ru]`, `[data-sabit]`, `[data-kapat]`, `.yan-unite`, `.yan-konular .topic` kullan.
- **Geniş ekran düzeni (11 Kasım 2026):** ≥ 900 px'de robot düğmesi (`.bot-fab`) dikey ve dar (76 px), içerik sağdan 104 px boşluk bırakır; düğme şıkların, Devam'ın ve Kısa Cevap düğmelerinin üstüne binmez. Koç balonu (`.koc`) üstte sağda (top 70 px). Konu başlığı küçüldü, "Yazılıda çıkacak/çıkabilir" rozeti meta satırında; 1366×768 ve 1280×720'de Öğren kartının düğmeleri ilk ekranda.
- Her sekmenin sonunda "Sıradaki" düğmesi: Öğren → Konuya Bak → Tekrar → Test → sıradaki konu. Ara Durak sekme sırası: Hatırla → Tarama Testi → Oyunlar → Sınav Provası (en sonda: bütün çalışmalardan sonra prova) → sıradaki konu.
- Dersin robotu anlatıcı (`robotDer(metin, "buyuk"|"kucuk")`): bütün giriş ve yönerge metinleri (konu girişi, Isınma, Hatırlayalım, Düşün ve Yaz, Konuya Bak girişi, oyun yönergeleri, test/tarama/sınav girişi ve sonuç mesajları, Hazır mısın?, Atölye) dersin maskotunun konuşma balonunda. Yeni ekranda yönerge yazarken `<p class="big">` yerine `robotDer` kullan.

## Serpiştirilmiş tekrar (`TEKRAR`)
- Ayrı "Günün Tekrarı" yok (İngilizce derslerindeki eski Günün Tekrarı kalıyor).
- Isınma: Öğren'in ilk adımı; aynı dersin önceki (en çok 12) konusundan 2–3 kavram sorusu (`kavramlar[].soru`). İlk konuda yok.
- Test: önceki konulardan 2 "Eski konudan" sorusu karışır.
- Seçim puanı: zayıf kavram (`ela7:<kod>:zayif`) > Öğren'de ilk denemede bulunamayan > uzun süredir sorulmayan (`ela7:<kod>:gor`).
- Zayıf kavram kaynakları: Isınma, Eski konudan, Tarama, Sınav Provası, Hatırla'da "Hatırlamadım".

## Ara Durak Hatırla — önce hatırla, sonra bak
- Kartlar kapalı; açınca "✓ Hatırladım / ✗ Hatırlamadım" (olay `hatirla`). Konu özeti kartların altında katlanmış.

## Sınav Provası
- Havuz: `public/<kod>/sinav/u<ünite no>.json` → `{"unite", "ders", "sorular": [...]}`. Durak sekmesi, kapsadığı konulardan en az 8 soru varsa görünür.
- Soru sayısı: durak `sinavSoru` alanı ya da 5+ konu kapsayan durakta 20, diğerlerinde 15.
- Her soruda `id` (ör. `f1-07`, benzersiz), `konu`, `kavram` (konunun `kavramlar[].ad` ile birebir), `tur`, `aciklama` (sayfa atıflı).
- Türler:
  - `secim`: `soru`, `secenekler` (4), `dogru`; isteğe bağlı `metin`/`tablo`/`metinBaslik`; öncüllü biçim için `onculler` (I–III) + `kok` ve `secenekler`: ["Yalnız I", "I ve II", "II ve III", "I, II ve III"]. Öncüllü sorularda şık sırası karışmaz, diğerlerinde karışır.
  - `dy`: `ifade`, `dogru` (true/false), isteğe bağlı `duzeltme`.
  - `dytablo`: `soru`, `ifadeler` [{`s`, `d`}].
  - `bosluk`: `cumleler` [{`c` (tek `___`), `cevap`}], `havuz` (yalnız çeldiriciler; cevaplar motorca eklenir).
  - `kisa`: `soru`, `yanit`, `kabul` []. Ek almış hâl (≤4 harf) ve 5+ harfli cevapta tek harf yazım hatası kabul.
  - `eslestir`: `soru`, `ciftler` [{`sol`, `sag`}] (3–5).
- İki biçim (veli ayarı `sinavAnlik`, varsayılan açık): **hemen göster** — tek tek, ipucu yok, tek hak; "Cevabı kontrol et" ya da "Bilmiyorum, geç" → renkli çözüm (`sinavKontrolHTML`), "Senin cevabın / Doğru cevap" ve robot balonunda "Neden?" (`sinavGeriHTML`), geri dönülmez. **sonda göster** — okuldaki gibi sorular arasında gezinme, sonuç sonda.
- Sonuç sayfası: puan + çaba övgüsü, "Yanlışların" kartı, konulara göre tablo, kapalı "Doğru yaptıkların". Sonda biçiminde önce "Yanlışlarını incele" (her ekranda bir yanlış), sonra "Yanlışlarını yeniden çöz" (şıklar karışık, tek hak; yine yanlışsa kavram zayıf listesine bir daha işlenir). Bekleyen yeniden çözme varken Sıradaki gizli. Son prova `ela7:<kod>:sinav-son:<durak>` (giriş ekranından dönülür).
- Açıklama (`aciklama`): Ela'nın anlayacağı 1–2 kısa cümle (en çok ~15 kelime) + sayfa. Çok parçalı türlerde doğrular zaten yeşil göründüğü için açıklama kısa bir ipucu olur.
- Olaylar: `sinav-basla`, `sinav-soru` (yeniden çözmede `yeniden: true`), `sinav-bitti` (`mod`), `sinav-inceleme`, `sinav-yeniden`. Kayıt: `ela7:<kod>:sinav:<durak>` (yarım), `sinavlar:<durak>` (geçmiş), `sinav-gor` (soru görülme sayısı; az görülen önce).
- Havuz yazarken: biçimler okul testlerinden (Banko, Arı) örnek alınır, sorular kitaba ve sitedeki konu anlatımına dayanarak yazılır; kopyalanmaz. Konu başına 5–7 soru, türler karışık, öncüllü sorularda doğru şık değişsin (çoktan seçmelide şıklar zaten karışır).
- Üretici: `araclar/sinav/<kod>_u<no>.py` (ortak modül `araclar/sinav/ortak.py`: `H = Havuz(kod, ünite, önek)`, `H.add(...)`, `H.yaz()`; yazmadan önce doğrular: kavram adı, şık sayısı, öncül/kök, `___` sayısı, havuzda cevap olmaması, açıklama ≤ 20 kelime). Konu içeriğini okumak için `python3 araclar/sinav/dok.py <kod> <ünite>`. JSON elle düzenlenmez; betik düzenlenip yeniden çalıştırılır.
- `kisa` + `sayi: true`: sayısal cevap; yalnız değeri aynı olan kabul (12 ≠ 125; 3/4 = 0,75; −8 = -8). Sözel kısa cevapta Türkçe harfsiz yazım (caldiran) yazım uyarısıyla kabul. İngilizce derslerde küçük harfe İngilizce kuralıyla çevrilir.
- Metinli soru: `metin` cümle listesi (dizi); çoktan seçmeli şıklarda `{{…}}` kullanma (şıklar düz yazılır), kesir `[[3/4]]` ve üs `[[u:2]]` şıklarda da çalışır. Boşluk doldurma kelime havuzunda biçimlendirme yok (düz kelime/sayı).
- Havuzlar (15 Ekim 2026): fen1 u1 40, u2 28, u3 50; tr1 u1 45; mat1 u1 60; sos1 u1 30, u2 25, u3 60; ing1 u1 18; own1 u1 18 (yalnız durağın kapsadığı u1k1, u1k2, u1k4). Toplam 374.

## Bulut (Faz 3, Firebase)
- Firebase projesi `ela7dersleri` (Spark, Firestore europe-west3). Giriş: veli e-posta/şifre, öğrenci cihazı anonim.
- Kaynak `araclar/bulut/bulut.mjs` → derlenmiş `public/ortak/bulut.js` (`cd araclar/bulut && npm install && npm run derle`). İki ayrı Firebase oturumu: "ogrenci" ve "veli"; veli Ela'nın bilgisayarında girip çıksa da cihaz bağlantısı kopmaz.
- Kurallar `araclar/bulut/firestore.rules` (konsolda Firestore → Rules'a yapıştırılıp Publish). Kurallar değişirse yeniden yayımlanmalı.
- Veri: `ogrenciler/{ogr}` {veli, takmaAd, cihazlar[], ayar}; `oturumlar/{oturum~parça}` {bit, olaylar[]}; `ilerleme/durum` {veri{anahtar:{v,t}}}; `eslestirme/{kod}` (24 saat).
- Motor (`BULUT` defter.js): yalnızca `ela7:bulut` kaydı olan (bağlanmış) cihazda bulut.js yüklenir. Bağlı olmayan cihaz (öğretmenler) hiçbir şey göndermez.
- Eşitleme: ders sayfası açılınca (3 sn sonra), test/sınav/Öğren/Atölye bitince, 2 dk'da bir (yeni olay varsa), sayfa gizlenince. Olaylar `son` zamanından sonrakiler; ilerleme: son eşitlemeden beri bu cihazda değişen anahtar gider, değişmeyen anahtar buluttakiyle güncellenir (silinen anahtar v:null). Hariç: `BULUT_HARIC` (cihaz, oturum, pin, sekme, oyun, ayar…). Ayar buluttan gelir (bağlı cihazda yerel ayar kutuları kilitli).
- Veli Paneli: giriş ekranı (Veli girişi / Öğrenci cihazı kodla bağlama / "Bu cihazın kaydını aç (PIN'le, bulutsuz)"). Veli hesabında: öğrenci ekle (takma ad), öğrenci seçimi, buluttaki son 90 gün, Cihazlar (bu cihazı bağla, kod üret, bağlantıları kaldır). Görünüm yerel modla aynı (`VELI.olaylar`, `VELI.oku`, `VELI.ayar/ayarYaz`).

## Yanlıştan sonra okuma beklemesi (`hataDurak`, veli ayarı `hataDur`, varsayılan açık)
- Cevabı gösterilen yanlışta (Test ve Tarama'da iki yanlıştan sonra, Sınav Provası'nda her yanlışta ve incelemede) ilerleme düğmeleri açıklamanın uzunluğuna göre 5–12 sn kilitli (sayı yok, dolan çubuk).
- Sonra "Neden yanlış yaptın?": Bilmiyordum / Soruyu yanlış okudum / İki şeyi karıştırdım / Acele ettim. Seçmeden geçilmez; robot seçime göre kısa yanıt verir. Erken dokunuşta robot uyarır (3 dk'da bir) ve kutu sallanır.
- Olaylar: `hata-neden` (neden, sureSn), `hata-acele`. Veli Paneli'nde "Yanlışların nedeni" dağılımı (Genel ve her ders, son 30 gün).

## Soru ve adım görseli (16 Ekim 2026, Matematik Tema 2 için, Kemal onayıyla)
- İsteğe bağlı `svg` alanı: soruda (`sorular`, kavram `soru`, `sende` adım sorusu), `cozum`/`sende` gövdesinde ve adımında, Sınav Provası `secim`/`kisa`/`dytablo`/`dy` sorusunda. Motor `gorselHTML()` ile `.q-gorsel` kutusunda gösterir (koyu `--svgbg` zemin, en çok 440×300 px).
- Görsel SVG'si 120×120 kavram çizimi değildir: geniş viewBox (ör. `0 0 320 160`), zemin dikdörtgeni yok (şeffaf), açık renkli çizim, attribute'larda tek tırnak.
- Resimli şık yok: A/B/C etiketli çizimler soru görselinde, şıklar metin "A", "B", "C" (şık karıştırma etiketleri bozmaz).

## Dikkat paketi (Kemal onayıyla, 5 Kasım 2026; Fen u1k1–u1k2 ve u3k1–u3k10)
Amaç: Ela soruyu anlayarak cevaplara baksın (asıl sorulan yerde durup düşünsün), ama sıkılmasın. Bütün davranış konu verisindeki `dikkat: true` ile açılır; diğer konular ve dersler değişmez. Ayrıntılı uygulama rehberi: `docs/dikkat-paketi.md`.
- **Sorunun kalbi:** soru vurgusuz gelir, şıklar gizli; Ela asıl sorulan kısma (`bolge`, yoksa `tetik`) dokunur → bölge kırmızı, şıklar açılır. Yanlış yer → yön ipucu (en yakın bölge kelimesine göre); 2. yanlışta bölge kendiliğinden gösterilir. Bekleme çubuğu yok. Yanlış cevapta "Sorunun kalbine tekrar bak", cevap gösterilince "Sorunun kalbi: …". Olumsuz sorular (DEĞİL, ARANMAZ, yanlıştır, önermedi, yapılmaz…; ayrıca `OLUMSUZ_RE` kökleri) seri ödülünde de bulmalı. Yalnız düz metinli sorularda (`<` ya da `[[` içermeyen). Bölge sorunun bütün kelimelerini kapsıyorsa (`kalpTum`, veride `"TUM"`) bulma adımı yok, şıklar doğrudan açılır. Bölgeler elle yazılır (`araclar/dikkat/<kod>/bolge.py`; ilkeler `docs/dikkat-paketi.md`).
- **Matematik (6 Kasım 2026):** tuş takımı ve sayı doğrusu sorularında da cevap alanı (`.kp`, `.sd-pick`) sorunun kalbi bulununca açılır; yanlış cevapta `kalpHatirlat` (`wireMathQuestion`). Uygulanan: mat1 u2k1–u4k4.
- **İngilizce (6 Kasım 2026):** soru metnindeki `{{…}}` sorunun kalbinde tek, dokunulmaz blok (renkli, dokununca okunur); `kalpTum` İngilizce kelimeleri saymaz. Kanıtlı metinde `{{…}}` cümleler dokununca okunmaz (kanıt seçimi), "Dinle" düğmesi okur. Uygulanan: ing1 u3k1–u5k2.
- **Seri ödülü:** 5 soruda üst üste ilk dokunuşta bulursa sonraki 3 soru bulmasız (konu başına, oturum içinde; Öğren'den Test'e taşınır). Olumsuz sorular hariç.
- **Metinli soru** (`metinli`, konu başına 2, Test'in sonunda, 2 kısa sorunun yerine; toplam soru sayısı aynı): önce yalnız soru (sorunun kalbi) → metin + sabit "Aradığın: …" şeridi (`serit`) → "Kanıtı bul" (mevcut kanıt mekanizması, `kanit`) → şıklar. `tuzak` şık (metindeki kelimeleri içeren yanlış) seçilince "Bu bir tuzak şık!". `karistir` tuzak indekslerini taşır.
- **Kısa Cevap:** önce sorunun kalbi, sonra "Soru senden ne istiyor?" — şıklar sorunun yeniden söylenmiş halleri (`okut[0]` doğru; "…-manı/-meni" biçiminde; yanlışlar Ela'nın tipik yanlış okumaları). Yanlış şık kapanır. Kalıpla yaz → kontrol; "Kalıpsız dene" düğmesi yok.
- **Hatırla ve Tekrarla** (`tekrar`): Öğren sonunda, Özet yerine; kart kilidi/çubuğu yok; görünmez "çok hızlı seçim" koruması kalır (max(1,5 sn; 0,4×okuma), yanlıştan sonra 1,5 sn).
- **Çıkarılanlar (dikkat konusunda):** ara "Hatırlayalım" adımları; "Neden yanlış yaptın?" (66 cevabın 65'i "Bilmiyordum"); bilgi kartı ve şık bekleme çubukları (bilgi kartında görünmez süre kalır, erken dokunuşta kısa not); önceki konudan Isınma ve "Eski konudan" soruları; Tekrar'da Hafıza Kartları ve Gruplayalım (yalnız Eşleştir).
- **Test sonu kartı:** sorunun kalbini ilk seferde bulduğu en az 4 sorunun en az %70'ini ilk denemede doğru yaptıysa "Soruyu anlayınca doğru cevap geliyor!" (veri göstermiyorsa çıkmaz).
- **Rozet:** `ders.json` → `yaziliRozet[konuId] = {kod, y1, y2}` (MEB konu-soru dağılım tablosu). Ela'ya yalnız "Yazılıda çıkacak" (y1) ya da "Yazılıda çıkabilir" (y2 dolu); senaryo ayrıntısı `title`'da. Fen tablosu 7.3.6'dan sonra kesikti: u3k8–u3k10'a rozet yok.
- **Çalışma kâğıdı:** Konuya Bak → "Çalışma kâğıdı (yazdır)"; bölge altı çizili, "Soru senden şunu istiyor: …".
- **Analiz alanları:** `soru` olayında (dikkat konusunda) `dikkat: true`, `kalp` (1 ilk dokunuşta, 2 ikinci, 0 gösterildi, -1 seri ödülüyle bulmasız, yok = kısa soru/bulma yok), `metinli`, `tuzak` (seçilen tuzak şık sayısı). Taslak önizlemede tutulan kayıtlar ayrı sitede durur; canlı Veli Paneli görmez.
- **Olaylar:** kalp-bul (sonuc 1/2/0, yanlis, sureSn), kalp-seri, ogren-ht, ogren-kisa, ogren-kisa-oku, hizli-tik, konu-kagit.
- **Veri:** `araclar/dikkat/uret.py <kod> [konu…]` + `araclar/dikkat/<kod>/*.py`. JSON elle düzenlenmez.
- **Test:** `araclar/dikkat/test_dikkat.py <kod> <konu>` (Playwright, sahte saat; Ela'nın ayarları: kartBekle, hataDur, sikBekle açık). Şık seçerken tam metin eşleştir (has_text kısmi ve harf duyarsızdır: "Doğrudur" ↔ "…doğrudur"). Açık Kuark balonları (.koc) tıklamayı engeller; testte kapat.
- Eşikler (5/3 seri, %70, 1,5 sn) kalibre edilmedi; Ela kullandıktan sonra `kalp-bul` ve `hizli-tik` olaylarıyla ayarlanmalı.

## Okuma pilotu (11 Kasım 2026; Kemal'in kararı; ilk kullanım fen1 — `ders.json` → `"okuPilot": true`)
Gözden geçirmede görüldü: Fen'deki 194 bulmalı sorunun 194'ünde sorunun kalbi cümlenin sonundaydı; dokunma adımı "sona dokun" refleksine dönebiliyordu. Pilot derste (yalnız dikkat paketli konularda):
- **Öğren (kavram soruları):** bulma adımı yok. Soru kelimesi (`vurgu`, yoksa `tetik`: "nerede", "hangi organ", "ne denir") **sarı fosforlu** gelir, şıklar açıktır (`vurguCiz`, `.kk-run.vurgu`). Yanlış cevapta "Sarı kelimeye tekrar bak". Kayıt: `soru` olayında `kalp: -2`. Metinli sorular ve Kısa Cevap eskisi gibi.
- **Test:** `ne: [doğru, yanlış]` olan soruda dokunma yerine iki seçenekli **"Bu soru senden ne istiyor?"** (`neAdim`). Doğru seçilince "Soruyu çok iyi okudun" (yalnız ilk seçimde), soru kelimesi sarı olur, şıklar açılır. Kayıt: `ne` (1/2), olay `ne-bul`. `ne` yoksa eski sorunun kalbi adımı (yön ipucundan "asıl soru çoğu zaman sondadır" çıkarıldı — bütün derslerde).
- **İkiz sorular:** `ikiz` değeri aynı iki soru (aynı kök, tek kelime farkı) testte art arda gelir (`ikizYanyana`); tekrar gelen soru çiftin arasına girmez. `testSoru` → testte sorulan sayı; `testSec` havuzdan en çok ⌊n/3⌋ çift + tek sorular seçer (havuz büyük olduğu için her çözüşte sorular değişir; seçilmeyen çiftin bir üyesi tek soru olarak gelebilir).
- **Veri:** `araclar/dikkat/<kod>/pilot.py` → `VURGU`, `NE`, `EKSORU`, `IKIZ`, `TESTSORU` (açıklamalar `uret.py` başlığında). Uygulanan: fen1'in bütün paketli konularında Öğren vurgusu; u3k1 (4 çift, havuz 15, testte 11) ve u3k2 (3 çift, havuz 12, testte 9) testlerinde `ne` + ikiz.
- **Analiz:** `ne === 1` olan sorularda ilk deneme doğruluğu ile `ne === 2` karşılaştırması; ikizlerde ikinci sorunun doğruluğu; Öğren'de `kalp: -2` sorularında ilk deneme doğruluğu ve `hizli` oranı (dokunma kalkınca düştü mü).

## Kaldığın yer (11 Kasım 2026; bütün dersler)
- Ders adreste konu olmadan açılınca (`/fen1/`): son çalışılan konu (`son`); o konu tamam (yeşil tik) ise sıradaki tamamlanmamış hazır konu/durak; hiç kayıt yoksa ilk tamamlanmamış konu (eskiden son hazır konu açılıyordu). Sekme: yarım test → Test; Öğren bitmediyse Öğren (kaldığı adım); Öğren bitti ve son sekme Öğren ise Test (`kaldiginYer`).
- Başlıkta robotlu tek satır not (`kalYerNot`, `.kal-yer`, × ile kapanır); olay `kal-yer`. Adreste konu varsa (ana sayfadaki ünite bağlantısı, menü) not çıkmaz.
- Oturum başı `KOC.plan` önerisi ("önce şuna bakalım mı?") **çağrılmıyor**: tek öneri budur. Tekrar zamanı gelen Ara Durak başlıktaki şeritte ve menü rozetinde görünmeye devam eder.
