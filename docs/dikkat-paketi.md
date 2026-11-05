# Dikkat paketi — başka bir derse / konuya uygulama rehberi

Motor ortak (`public/ortak/defter.js`), yani paket her derste aynı çalışır; bir konuya uygulamak için **yalnız veri** yazılır ve konu dosyasına `dikkat: true` girer. Ne yaptığı: `docs/motor-notlari.md` → "Dikkat paketi".

## Konu başına yazılacak veri (`araclar/dikkat/<kod>/<konu>.py`)
| Sözlük | Ne | Miktar |
|---|---|---|
| `TEKRAR` | Hatırla ve Tekrarla cümleleri: `("… {doğru\|çeldirici\|çeldirici} …", "s. N")` | 6–7 cümle (en az 4) |
| `KISA` | Kısa cevap soruları (soru, tetik, parcalar, kisa, cevap, anahtarlar, sayfa) | 2 |
| `OKUT` | Her kısa cevap için "Soru senden ne istiyor?" şıkları: doğru ilk, "…-manı/-meni"; yanlışlar tipik yanlış okumalar (sorunun yarısı, konuyu alıp isteneni kaçırmak) | 2 × 3 |
| `METINLI` | Metinli sorular: kısa (2–3 cümle) + uzun (4–6 cümle; kitabın örnek olayından). `bolge`, `serit`, `kanit`, 3 şık, `tuzak`, ipucu, kanitIpucu, sayfalı açıklama, `kavram` | 2 |
| `ELLE` / `BOLGE` | Kalıpla bulunamayan soru kelimesi / otomatik "sorunun kalbi" bölgesinin elle düzeltilmesi | gerektikçe |

Kurallar: her bilgi kitaptan ve sayfalı (`[s. N]` işaretinin ÜSTÜNDEKİ metin N. sayfadadır); çeldiriciler bağlamda açıkça yanlış; tuzak şık metindeki kelimeleri içerir ama soruyu cevaplamaz; kitap dışı bağlam kullanılırsa açıklamada belirtilir.

## Adımlar (bir oturumda)
1. `taslak` dalı; konunun kitap sayfalarını oku.
2. `araclar/dikkat/<kod>/<konu>.py` yaz.
3. `python3 -I araclar/dikkat/uret.py <kod> <konu…>` → doğrulayıcı hata vermezse JSON yazılır. `GOSTER=1` ile bütün "sorunun kalbi" bölgelerini yazdır ve gözden geçir: bölge yalnız "hangisidir/nedir" olmamalı, anlamı taşımalı; değilse `BOLGE` ile düzelt.
4. Ders farklıysa kontrol et: soruların düz metin olması gerekir (`[[kesir]]`, `<b>` içeren sorularda bulma adımı atlanır — Matematik'te çoğu soru böyle; orada önce bu sınır ele alınmalı). İngilizce derslerde soru kelimesi kalıbı (`GEN`) Türkçedir; İngilizce sorular için `ELLE`/`BOLGE` ya da kalıp genişletmesi gerekir.
5. `python3 araclar/dikkat/test_dikkat.py <kod> <konu>` (Playwright): Öğren → Hatırla ve Tekrarla → Kısa Cevap → Test (metinli) → çalışma kâğıdı; Ela'nın ayarlarıyla, konsol hatası yok, 390 px taşma yok.
6. Commit → `taslak`; Kemal "yayınla" demedikçe `main`'e gitmez.

## Derse göre notlar (tahmin; uygularken doğrulanmalı)
- **Sosyal, Din, Türkçe, Teknoloji:** doğrudan uygulanabilir. Türkçe'de metinli sorular zaten var (`metin` + `kanit`); onlara `bolge` + `serit` eklemek yeterli.
- **Matematik:** sorular çoğunlukla kesir/üs işaretli ve "tuş takımı" türünde; "sorunun kalbi" yalnız düz metinli sözel problemlerde çalışır. Kısa Cevap yerine işlem adımı daha uygun olabilir.
- **İngilizce:** kalıplar İngilizce soru kelimelerine (what, which, why…) göre genişletilmeli; ön soru şıkları Türkçe kalabilir.
- **Rozet:** her dersin MEB konu-soru dağılım tablosundan `ders.json` → `yaziliRozet` yazılır.
