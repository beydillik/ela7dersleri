# Dikkat paketi — başka bir derse / konuya uygulama rehberi

Motor ortak (`public/ortak/defter.js`), yani paket her derste aynı çalışır; bir konuya uygulamak için **yalnız veri** yazılır ve konu dosyasına `dikkat: true` girer. Ne yaptığı: `docs/motor-notlari.md` → "Dikkat paketi".

## Konu başına yazılacak veri (`araclar/dikkat/<kod>/<konu>.py`)
| Sözlük | Ne | Miktar |
|---|---|---|
| `TEKRAR` | Hatırla ve Tekrarla cümleleri: `("… {doğru\|çeldirici\|çeldirici} …", "s. N")` | 6–7 cümle (en az 4) |
| `KISA` | Kısa cevap soruları (soru, tetik, parcalar, kisa, cevap, anahtarlar, sayfa) | 2 |
| `OKUT` | Her kısa cevap için "Soru senden ne istiyor?" şıkları: doğru ilk, "…-manı/-meni"; yanlışlar tipik yanlış okumalar (sorunun yarısı, konuyu alıp isteneni kaçırmak) | 2 × 3 |
| `METINLI` | Metinli sorular: kısa (2–3 cümle) + uzun (4–6 cümle; kitabın örnek olayından). `bolge`, `serit`, `kanit`, 3 şık, `tuzak`, ipucu, kanitIpucu, sayfalı açıklama, `kavram` | 2 |
| `SERIT` | Konuda zaten var olan kanıtlı (metinli) sorular için "Aradığın: …" şeridi (doğrulayıcı eksikse uyarır) | var olan her kanıtlı soru |
| `BOLGE` | **Her soru için elle** "sorunun kalbi" (kavram soruları, Test soruları, kısa cevaplar); `"TUM"` = bulma adımı yok. Ayrı dosya: `bolge.py` | her soru |
| `ELLE` | Kalıpla bulunamayan soru kelimesi | gerektikçe |

## Sorunun kalbi ilkeleri (Kemal onayı, 5 Kasım 2026)
- Bölge **ne soruyor** kısmıdır: soru kelimesi + yüklemi + ona doğrudan bağlı sözcükler ("nerede başlar", "hangi organda tamamlanır", "sindirim olur mu").
- **Anlamı değiştiren sözcükler dahil:** en az / en çok, ilk, sonraki, iki, değildir, ARANMAZ, doğrudur / hatalıdır, karşıt eşler (Çocukların / Yetişkinlerin, gövdesi / yaprakları, alırken / verirken).
- **Konu ve bağlam hariç:** "Yutak ve yemek borusunda **sindirim olur mu**?" — konu bölgeye girmez.
- **Söz öbeği bölünmez:** "yemek borusu", "yapı taşları", "soluk alıp verme hızımız" ya bütün girer ya hiç. Araç kelimeyi ortadan kesen bölgeyi hata sayar; öbek bölünmesini araç yakalayamaz, elle bakılır.
- **4 kelime ve daha kısa sorular `"TUM"`:** her yere dokunmak doğru olacağı için bulma adımı yok (düşünmeden dokunma alışkanlığı yapmasın). Olumsuz ve doğru/yanlış/hatalı soruları hariç: onlarda bölge o sözcüğü kapsar, bulma kalır.
- Metinli sorularda bölge `"TUM"` olamaz (akış önce bulmayı ister).
- Fen 1. dönemde 237 sorunun 216'sı bulmalı, 21'i bulmasız.

Kurallar: her bilgi kitaptan ve sayfalı (`[s. N]` işaretinin ÜSTÜNDEKİ metin N. sayfadadır); çeldiriciler bağlamda açıkça yanlış; tuzak şık metindeki kelimeleri içerir ama soruyu cevaplamaz; kitap dışı bağlam kullanılırsa açıklamada belirtilir.

## Kapsam
Bir sohbette bir tema/ünite (8–10 konu) yapılabilir. İki tema birden bağlamı zorlar; ikinci temayı aynı sohbette "devam" diyerek ya da yeni sohbette iste. Ara Duraklar bu paketin dışında.

## Adımlar (bir oturumda)
1. `taslak` dalı; konunun kitap sayfalarını oku.
2. `araclar/dikkat/<kod>/<konu>.py` yaz.
3. `TASLAK=1 python3 -I araclar/dikkat/uret.py <kod> <konu…>` → eksik bölgeler için taslak satırlar basılır; bunları `araclar/dikkat/<kod>/bolge.py`'ye koy ve **her birini ilkelere göre elle düzelt** (taslak yalnız soru kelimesinden soru işaretine kadar keser). Sonra `python3 -I araclar/dikkat/uret.py <kod> <konu…>` → doğrulayıcı hata vermezse JSON yazılır. `GOSTER=1` ile son hali yazdırıp bir kez daha oku.
4. Ders farklıysa kontrol et: soruların düz metin olması gerekir (`[[kesir]]`, `<b>` içeren sorularda bulma adımı atlanır — Matematik'te çoğu soru böyle; orada önce bu sınır ele alınmalı). İngilizce derslerde soru kelimesi kalıbı (`GEN`) Türkçedir; İngilizce sorular için `ELLE`/`BOLGE` ya da kalıp genişletmesi gerekir.
5. `python3 araclar/dikkat/test_dikkat.py <kod> <konu>` (Playwright): Öğren → Hatırla ve Tekrarla → Kısa Cevap → Test (metinli) → çalışma kâğıdı; Ela'nın ayarlarıyla, konsol hatası yok, 390 px taşma yok.
6. Commit → `taslak`; Kemal "yayınla" demedikçe `main`'e gitmez.

## Derse göre notlar (tahmin; uygularken doğrulanmalı)
- **Türkçe (uygulandı: tr1 u3k1–u3k8, 5 Kasım 2026; veri `araclar/dikkat/tr1/`):** her konuda zaten 3 kanıtlı metinli soru var → yeni `METINLI` yazılmadı; var olanlara `SERIT` yazıldı. Kanıtlı sorularda bölge `"TUM"` olamaz (motor bulma adımını atlarsa önce-soru-sonra-metin akışı ve şerit de atlanır). Olumsuz kökler (`olumsuzVurgu`) seri ödülünde de bulmalı kalır. Türkçe'de "ne demektir, ne zaman, ne katar, ne gösterir…" gibi soru kelimeleri `GEN` kalıbında yok → `ELLE`'ye yazıldı. "Hazır mısın?" ve "Sıra sende" soruları üreticinin kapsamında değil, bulmasız kalır. `OKUT` şıkları harfle başlamalı (motor ilk harfi büyütür; tırnak ya da parantezle başlayan şık küçük harfle görünür). 145 sorunun 135'i bulmalı, 10'u bulmasız.
- **Test betiği** (`test_dikkat.py`) "Hazır mısın?", "Birlikte çözelim / Sıra sende" adımlarını, konudaki kanıtlı test sorularını (Türkçe) ve Matematik'in tuş takımı / sayı doğrusu sorularını da geçer (aynı metinli, görseli farklı sorularda şıklara göre doğru soruyu seçer).
- **Sosyal, Din, Teknoloji:** doğrudan uygulanabilir; metinli sorular `METINLI` ile yazılır.
- **Matematik (uygulandı: mat1 Tema 2–4, u2k1–u4k4 = 20 konu, 6 Kasım 2026; veri `araclar/dikkat/mat1/tema2.py`, `tema3.py`, `tema4.py`, bölgeler `bolge.py`):**
  - Tema 2–4 sorularında `[[ ]]`/`<b>` yok, sorunun kalbi her soruda çalışır. Tema 1 (kesir, üs, devirli sayı) paketsiz; uygulanacaksa önce sembollü sorular ele alınmalı.
  - **Motor (Kemal onayı):** tuş takımı (`cevap`) ve sayı doğrusu (`nokta`) sorularında da cevap alanı sorunun kalbi bulununca açılır; yanlışta "Sorunun kalbine tekrar bak" (`wireMathQuestion`, yalnız `d.dikkat`). Paketsiz konular değişmez.
  - Bölge = istenen ölçü + birimi ("yüzey alanı kaç cm²", "kaç dm yüksekliğe çıkar"); verilen sayılar hariç; "en az, kapaksız, yalnızca, bütün, önden/arkadan" dahil. Birim çevirme soruları ("3 L kaç mL?") `TUM`.
  - Soru metinleri bölünmez boşluk (`\xa0`, `bosluk()`) içerir: `BOLGE` anahtarlarını `TASLAK=1` çıktısından kopyala.
  - Elle bölgesi yazılmış soruda soru kelimesi (tetik) gerekmez ("Açıklığa sayı doğrusunda dokun.") — `uret.py` artık bunu hata saymaz.
  - Kısa Cevap hesap değil kavram açıklatır ("kaplamak için neden yüzey alanı?", hata bulma). Metinli sorular yeni nesil problem metni; kanıt = istenen ölçüyü veren cümle; tuzak yalnız şık metindeki kelimeleri gerçekten içeriyorsa (yalın sayı şıkları tuzak değil, motor "metindeki kelimeler var" der).
  - **`gen_mat1.py` konu dosyalarını baştan yazar ve sonunda `uret.py mat1`'i çalıştırır**; soru metni değiştiyse "elle bölge eksik" uyarısı çıkar → `bolge.py`'yi güncelle.
  - 20 konu: sorunun kalbi 361 soru (321 kavram/test + 40 kısa cevap; 323 bulmalı, 38 bulmasız), 40 metinli soru, 136 Hatırla ve Tekrarla cümlesi.
- **İngilizce (uygulandı: ing1 u3k1–u5k2 = 8 konu, 6 Kasım 2026; veri `araclar/dikkat/ing1/u3.py`, `u4.py`, `u5.py`, bölgeler `bolge.py`). Kemal'in isteği: aynı parçaları kullanmak zorunlu değil, yalnız gerçekten lazım olan yerde.**
  - **Motor (Kemal onayı):** `kalpCiz` soru metnindeki `{{İngilizce}}` parçasını tek blok çizer (renkli, dokununca okunur, sorunun kalbi olamaz); `kalpTum` bu parçanın kelimelerini saymaz. Kanıtlı metinde `{{…}}` cümle dokununca okunmaz (dokunuş kanıt seçimi), "Dinle" metnin tamamını İngilizce okur. `uret.py` bölgenin `{{…}}` içine girmesini hata sayar (`"TUM"` hariç).
  - Bölge yalnız Türkçe soru kısmında. Türkçe kısmı 4 kelime ve kısa sorular `"TUM"` ("Dinle. Hangi cümleyi duydun?", "Boşluğa ne gelir?", "Ne yaptı?"); istisna olumsuz / doğru-yanlış ("memeli değildir", "doğru yazılmış") ve tuzak şıklı ayrıntı sorusu ("Oliver öldüğünde **kaç yaşındaydı**", şıkta 2010). 141 sorunun 42'si bulmalı + 16 metinli soru.
  - Hatırla ve Tekrarla: kitaptan İngilizce cümle, boşluk karışan yerde (born/died, in/on + tarih, should + yalın fiil, prefer … to). **Düz metin** — `{{ }}` yazılmaz (`{a|b}` boşluk sözdizimiyle çakışır).
  - Kısa Cevap konu başına **1** (İngilizce yazmak yavaş; Öğren'de Kelime Duvarı da var). Soru Türkçe ve `{{ }}` içermez; cümle başları İngilizce ("I was", "We shouldn't"); anahtarlar Ela'nın yazdığı kısımda olmalı (kontrol cümle başını katmaz). Ön soru şıkları Türkçe.
  - Metinli sorular: kitabın İngilizce metni, cümleler `{{…}}` içinde (ses için), kök Türkçe, şıklar İngilizce (tuzak denetimi metinle ortak kelime arar; Türkçe şık tuzak olamaz). MEB İngilizce yazılısının "metinden bul" biçimine uygun.
  - Tekrar sekmesinde İngilizce oyunlar (Dinle ve Bul, Kelimeyi Kur, Cümle Kur, Hatayı Bul, Resim Eşleştir) kalır; yalnız Hafıza Kartları ve Gruplayalım çıkar. Rozet yok (1. yazılı Senaryo 1 yalnız Ünite 1–2).
  - Test betiği İngilizce derste Kelime Duvarı adımını ve aynı metinli soruları (şıklarla) ayırır.
- **Rozet:** her dersin MEB konu-soru dağılım tablosundan `ders.json` → `yaziliRozet` yazılır.
