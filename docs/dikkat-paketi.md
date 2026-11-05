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
- **Türkçe:** her konuda zaten 3 kanıtlı metinli soru var → yeni `METINLI` yazma (Test'te kısa soruların yerini alır, metinli oranı fazla artar); var olanlara `SERIT` yaz. Olumsuz kökler (`olumsuzVurgu`) seri ödülünde de bulmalı kalır.
- **Sosyal, Din, Teknoloji:** doğrudan uygulanabilir; metinli sorular `METINLI` ile yazılır.
- **Matematik:** sorular çoğunlukla kesir/üs işaretli ve "tuş takımı" türünde; "sorunun kalbi" yalnız düz metinli sözel problemlerde çalışır. Kısa Cevap yerine işlem adımı daha uygun olabilir.
- **İngilizce:** kalıplar İngilizce soru kelimelerine (what, which, why…) göre genişletilmeli; ön soru şıkları Türkçe kalabilir.
- **Rozet:** her dersin MEB konu-soru dağılım tablosundan `ders.json` → `yaziliRozet` yazılır.
