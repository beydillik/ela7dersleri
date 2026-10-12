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
- Okul koşulları: ipucu yok, tek cevap, sorular arasında gezinme, sonuç sonda (konu tablosu + soru soru çözüm + "Konuda bak").
- Olaylar: `sinav-basla`, `sinav-soru`, `sinav-bitti`. Kayıt: `ela7:<kod>:sinav:<durak>` (yarım), `sinavlar:<durak>` (geçmiş), `sinav-gor` (soru görülme sayısı; az görülen önce).
- Havuz yazarken: biçimler okul testlerinden (Banko, Arı) örnek alınır, sorular kitaba dayanarak yazılır; kopyalanmaz. Konu başına 4–7 soru, türler karışık, doğru şık dağılsın. Doğrulama: `gen_fen_sinav.py` benzeri betikle kavram adı, şık sayısı, `___` sayısı.
- Fen Ünite 1: 40 soru (secim 15 — 6'sı öncüllü —, dy 7, kisa 7, bosluk 4, eslestir 4, dytablo 3).
