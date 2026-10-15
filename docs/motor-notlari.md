# Motor notları (Faz 1 eki ve Faz 2) — ela-ders-defteri skill'inin 9. bölümüne ek

Bu dosya, skill'e henüz eklenmemiş motor kurallarını toplar. Faz 2 bitince skill'e taşınacak.

## Veli Paneli (`public/veli/`)
- Ana sayfanın alt bilgisinde küçük "Veli" bağlantısı. Ders sayfalarındaki `#rapor` buraya yönlenir.
- Kod `ortak/defter.js` içinde (`bootVeli`, `veliGenel`, `veliDers`, `konuDurumu`, `raporIndir`). `veli/index.html` gövdesinde `data-sayfa="veli"`.
- Sekmeler: Genel (son 7 gün, 14 günlük grafik, günler, oturumlar, yanlış sorular, rapor indirme, ayarlar, tam yedek) + her ders.
- Rapor JSON: `konuDurumu` (konu konu Öğren, test ilk/son, zorlandığı kavramlar, Ara Durak tarama ve sınav provası), `oturumlar`, `olaylar`, `sozluk`.

## Tasarım
- `.nav` sabit değil. Kaydırınca `.serit` (☰ Konular açılır listesi + konu adı + sekmeler) üstte belirir (`setupSerit`). Fareyle üzerine gelince açılmaz (bilerek).
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
