---
name: ela-yazili-hazirlik
description: Ela'nın ders defteri sitesine herhangi bir dersin (Fen, Matematik, Sosyal, Din, Türkçe, İngilizce, Teknoloji…) yazılı sınavı için Yazılıya Hazırlık bölümü kurma, güncelleme ve Ela'nın kullanımına göre iyileştirme.
---

# Yazılıya Hazırlık — çalışma yöntemi

Site, depo (`beydillik/ela7dersleri`), **yayın kuralı** (her şey `taslak` dalına; `main` = 15 Netlify kredisi, yalnız Kemal'in açık onayıyla), kaynak/sayfa kuralı ve Ela için genel öğretim ilkeleri **ela-ders-defteri** becerisindedir; önce onu da yükle. Bu beceri yazılı hazırlığına özgüdür. Depodaki `docs/SKILL-ela-yazili-hazirlik.md` bu dosyanın kopyasıdır; değişince ikisini birlikte güncelle. Yanıtlar Türkçe.

Oturum başka bir dersin Claude projesine bağlıysa (ör. "Ela 7 – Sosyal Bilgiler") depo yine aynıdır: `add_repo` ile ekle, kitap metni `kaynaklar/<kod>/uniteN.md`'de ve o projenin dosyalarında.

## 1. Amaç ve Kemal'in kararları (Ekim–Kasım 2026; değiştirme, gerekirse sor)
- **Hedef:** Ela yazılıda MEB'in örneğine *benzer* soruyu gördüğünde, burada çalıştığı soruyla bağlantı kurup en azından anladığını gösterecek kadar yazabilsin. Ela'da dikkat eksikliği ve hiperaktivite var; birebir aynı soruyu tekrarlamak ona kolay gelir, benzerine aktarmak zordur. Her karar buna hizmet eder.
- **Kapsam:** Yalnız okulun seçtiği senaryodaki öğrenme çıktıları (kazanımlar). Senaryoda olmayan kazanımın sorusu, konusu, kartı Ela'ya hiç gösterilmez; `kapsamDisi` listesiyle "bunlara çalışma" denir. Senaryo yoksa (öğretmen çalışma kâğıdı verdiyse) kâğıttaki sorular esastır (bkz. 6).
- **Kaynak önceliği:** 1) MEB "Yazılıya Hazırlanıyorum" örnek soruları (yalnız senaryoya girenler; çözümleri doğrula), 2) ders kitabı (sayfa atıflı), 3) internet/okul yazılı örnekleri yalnız soru *kalıbı* olarak, senaryoya uyanlar yeniden yazılarak. Kitap dışı bilgi eklenmez.
- **Kısa cevap (en önemli kural):** Ela uzun cevabı ezberleyemiyor; ya hepsini ya çok azını hatırlıyor. Her madde için puanın büyük kısmını (en az %70) getiren **en kısa cümle/kelimeler** `kisaCevap` olarak yazılır ve Ela'nın hedefi odur. Uzun örnek cevap kontrol ekranında katlı durur. (Fen'de kısa cevaplar ortalama 51 harf, uzun örnekler 138.)
- **Yazarken cevap görünmez.** Cevaba bakıp kopyalamak öğrenme değil. Takılınca geri basamağa gidilmez, aynı ekranda kademeli **ipucu** açılır; ipucu açıkken yazı kutusu gizlidir, Ela "Anladım, şimdi yazacağım" deyince kapanır ve aklında kalanla yazar (bakarak kopyalamasın); yazdığı metin korunur.
- **Odak:** Yazılı bölümünde sitenin üst bandı, konu menüsü, sohbet robotu, koç balonları gizli. Robot (Kuark, Fikri…) yalnız anlatıcı balonunda. Ders defterine bağlantı yalnız "Hatırla kartında yoksa", yeni sekmede.
- **Görünüm:** ANKUZEF Defteri gibi: solda kara tahta menü (tebeşir yazısı, Caveat), sağda çizgili, kırmızı kenarlı, spiralli defter sayfası; telefonda ☰ çekmece.
- **Yapay zekâ ile değerlendirme yok.** Açık uçlu cevaplar anahtar köklerle otomatik işaretlenir, Ela onaylar.

## 2. Akış (motor, `public/ortak/defter.js` "Yazılıya Hazırlık")
Menü/yol: **Başlangıç** → 1 **Hatırla** → 2 **MEB Soruları** (adı veriden: `soruBaslik`) → 3 **Konu Tekrarı** (ikizler varsa) → **Kısa Cevap Kartları** (kisaCevap varsa) → **Kuark'ın Cevabını Düzelt** (eski biçimde "…'in Hatası") → **Prova Yazılıları**. Numaralar menüde sırayla verilir (olmayan adım atlanır). Araçlar: **Yanlış Defterim**, **Sınav Öncesi Özet**. Başlangıçta ilk bitmemiş adım "Sıradaki" diye vurgulanır.

- **Hatırla:** Kazanım başına tek ekran: çizim, 5–6 madde (sayfa atıflı), puan getiren kelimeler, sık yapılan hatalar (✗/✓), dinle. Menüde kazanım halkaları (son 4 denemenin ortalaması).
- **MEB Soruları:** Madde madde. Soru metninde **tetik ifadeler** fosforla işaretli, altında tek satır **"Soru kelimesi → cevap kalıbı"** notu (ayrı "Cevap Kalıpları" sayfası yok; kalıp listesi yalnız Özet'te). Basamaklı maddede 4 basamak:
  1. **Tam cevabı tanı:** 3 cevaptan tam puanlık olanı seç (doğru kısa cevap / gerekçesi eksik / kavram yanılgısı). `wireQuestion`, 2 hak + ipucu.
  2. **Parça parça kur:** Cümle başları hazır ("Problem: … Nedeni: …"), Ela boşluğa 1–2 kelime yazar; "Kelime havuzu" (doğru + 2 çeldirici), 2. yanlışta doğrusu dolar; bitince "İşte cevabını kendin kurdun".
  3. **Kalıpla yaz:** Kutuda yalnız cümle başları; ipucu = kelime havuzu. Kontrol ekranı (anahtar listesi + kısa cevap) → "Şimdi kalıpsız yaz".
  4. **Sınavdaki gibi yaz:** Boş kutu; ipucu 1 = cümle başları, ipucu 2 = kelime havuzu. Kontrol: anahtar listesi (otomatik işaretli, Ela onaylar), "Bu kadarı yeter: <kısa cevap>", katlı uzun örnek, katlı Hatırla kartı.
  - Başlangıç basamağı kayıttan (`basamak["<soru>|<harf>"]`, ilk sefer 1). Sınavdaki hâlde ≥ %75 ve ipucusuz → bir üst; < %50 → bir alt.
  - Basamaksız madde: varsa iskele (Sınav Provası soru türleri, `sinavTek`; yalnız ilk çözümde) + yazma. Yalnız iskeleli madde (boşluk doldurma) iskeleyle puanlanır.
  - Sonuçta "Benzerini çöz" (ikizler, en az görülen önce), "Tekrar çöz", zayıfsa "Hatırla: …".
- **Konu Tekrarı** (Kemal, 1 Kasım 2026: "1 MEB + 2–3 benzer pekişme için yeter"): kazanım başına zincir: önce MEB sorusu normal basamaklarıyla (konunun birden çok MEB sorusu varsa en zayıfı, çözülmemiş önce), sonra 2–3 benzer soru (o sorunun 2 ikizi + konunun öbür MEB sorusundan 1; en az görülen önce). Aralarda tek ekran ("Benzer soruya geç →"), sonda soru halkaları + "Sıradaki konu". Benzer sorularda basamak yok: doğrudan sınavdaki gibi yazma, tetik vurgusu, kalıp notu, ipucu (cümle başları → kelime havuzu, "Anladım"); seviye kaydı değişmez. Kayıt `tekrar[kod] = {t, r, n}`; olay `yazili-tekrar`. `yzSoruCoz` ctx: `yer`, `baslik`, `sonra(r)` (zincir).
- **Kısa Cevap Kartları:** Soru (tetik vurgulu, görsel görünür, uzun metin katlı) → 3 kısa cevaptan doğrusunu seç: doğru, basamak 1'in eksik cevabı, aynı kazanımdan başka sorunun kısa cevabı (hangi cevap hangi soruya). "Hatırladım" düğmesi YOK (Ela okumadan dokunuyordu). Kutu 0–3 (ilk denemede doğru +1, değilse 0 ve turun sonunda bir kez daha); tur 8 kart, zayıf ve eski önce; "oturdu" = kutu ≥ 2.
- **Kuark'ın Cevabını Düzelt:** Çoğu madde **eksik cevap** (Kuark doğru ama yarım yazar: "Evet.", "Kütlesi."); **yanılgı** türü yalnız Hatırla kartlarının "sık hatalar"ında zaten geçen klasikler (Fen'de 4) — Ela'ya yeni yanlış öğretilmez (Kemal'in kaygısı). Ela eksiği/hatayı seçer → Kuark'ın cevabı çizilir ("yanlış") ya da "yarım" etiketi alır → Ela tam cevabın boşluğunu kendisi yazar (havuz, 2. yanlışta dolar) → en altta büyük "Tam puanlık cevap". Turda 6 madde, en çok 2 yanılgı. Eski biçim (`tamamla` yok, bil1) "…'in Hatası" olarak çalışır.
- **Prova Yazılıları:** Senaryo dağılımında; ekranda (tek sayfa, 40 dk yumuşak sayaç, taslak cihazda) ya da kâğıtta (yazdır → "Kâğıdı puanla"); "Cevap anahtarı" yazdırılır. **Sınav modu** (kutucuk): menü kapalı, geri yok, süre bitince otomatik teslim. Puanlama: madde puanı × işaretli anahtar oranı, 0,5'e yuvarlanır; sonuçta kazanım çubukları ve zayıf kazanıma "Hatırla". **Köprü:** her prova sorusunda `benzer` (MEB soru id) → ekranda çözerken "Hangi MEB sorusuna benziyor?" katlı kutusu (soru no + o sorunun kalıp notları, cevap yok; sınav modunda ve baskıda gizli); sonuçta %80 altı sorular için "N. soru → MEB Soru X" düğmesi (o MEB sorusunu basamaklarıyla açar).
- **Yanlış Defterim:** Tam puan almayan her madde (MEB, benzer, prova) `eksik["tur|id|…"]`; "Eksiklerimi yeniden yaz" 8'lik tur (ısınmasız; basamaklı maddede kayıtlı basamaktan); tam olunca silinir.
- **Sınav Öncesi Özet:** Bütün Hatırla kartları + cevap kalıpları, yazdırılabilir.
- Kayıt `ela7:<kod>:yazili:<id>` (kaz, meb, ikizGor, tekrar, prova, hatirla, kuark, kart, basamak, eksik, sinavModu), taslak `ela7:<kod>:yazili-taslak:<id>:<prova>`; bağlı cihazda buluta eşitlenir. Olaylar (KAYIT_SOZLUK'te): yazili-ac, yazili-madde, yazili-basamak, yazili-kart, yazili-kuark, yazili-prova, yazili-sure, yazili-yazdir, yazili-tekrar. Veli Paneli'nde ayrı tablo henüz yok.

## 3. Veri (JSON elle düzenlenmez)
`araclar/yazili/yazili.py` (ortak üretici + doğrulayıcı), `araclar/yazili/cizim*.py` (soru çizimleri: koyu `#1b2340` zemin, açık renkler, tek tırnak), `araclar/yazili/<kod>_<id>.py` (ders verisi; örnekler `fen1_d1y1.py` — tam yapı, `bil1_d1y1.py` — senaryosuz/ikizsiz). Çalıştır: `python3 araclar/yazili/<kod>_<id>.py` → `public/<kod>/yazili/<id>.json`; hata varsa yazmaz, sayıları yanıtta yaz. ders.json: `"yazili": [{"id": "d1y1", "baslik": "1. Dönem 1. Yazılı", "dosya": "yazili/d1y1.json"}]` (uniteler'den önce; indent=1).

- **Üst alanlar:** baslik, ders, senaryo, sure, tarih (YYYY-MM-DD/None → geri sayım), `dagilim` {kazanım: soru sayısı} (her prova birebir), giris (yalnız `<b>`), kapsamDisi, puanNotu ("Puanlar tahminidir"), kaynakNotu. İsteğe bağlı: soruBaslik / soruEtiket (ör. "Öğretmenin Soruları" / "Soru"), soruGiris, kazanimAd (ör. "konu"), ikizsiz.
- **Kazanım:** kod, ad (MEB metni), kisa, soru, renk, konular (defter konu kimlikleri), sayfa, svg, maddeler (5–6, `<b>`), kelimeler, hatalar [{yanlis, dogru}] (3; Kuark yanılgıları yalnız buradan seçilir).
- **Formüller (cevap kalıpları):** cunku, karsilastir, sira, problem, tahmin… (id, ad, kalip, ne, ornek). Madde `formul` ile bağlanır.
- **Madde:** harf, soru, formul?, iskele?, cevap (uzun örnek), anahtarlar [{ad, k:[kök]} | {ad, sira:[[kök],…]}], ve basamaklı maddede:
  - `kisaCevap` (anahtarların ≥ %70'i; örnekten kısa),
  - `tetik` [soru metninde birebir geçen ifadeler], `kalipNot` (tek satır, ör. "Evet/Hayır + çünkü."),
  - `basamak`: {sec: {secenekler: [doğru kısa, eksik, yanılgı], dogru: 0, ipucu, aciklama}, parcalar: [{bas, ornek, havuz: [2 çeldirici], k | hepsi: [[…],[…]] | sira | serbest}]}. **`bas` hiçbir anahtar kökünü içermez** (yoksa şablon kendiliğinden puan alır); çeldirici kökle eşleşmez (ör. "hava kirliliği" ↔ kök "kirlili" çakışır → "uzay kirlili").
  - Fen'de bir yardımcı: `BASAMAK[(soruId, harf)] = B(kisa, dogru, eksik, yanlis, ipucu, aciklama, P(bas, ornek, havuz, k=…), …)` ve `TETIK[(soruId, harf)] = ([ifadeler], not)`; basamaklı maddede `iskele` silinir.
- **MEB sorusu:** id, no, kazanim, metin [paragraf], svg?, maddeler, ikizler (2; aynı kalıp, farklı bağlam; `ikizsiz` derste yok).
  - **İkiz maddesi (Konu Tekrarı desteği):** kisaCevap, tetik, kalipNot ve `basamak: {parcalar}` — **`sec` YOK** (motor bunu "benzer soru" sayar, doğrudan yazmadan başlatır). Fen'de `IKIZ[(ikizId, harf)] = IK(kisa, [tetik], not, P(...), …)`; ortak parçalar (PROB, EVET, HAYIR) tekrar kullanılır. Doğrulayıcı aynı kuralları uygular (cümle başı anahtar kökü içermesin: "Çünkü alınan yol:" → "yol" kökünü tetikledi, "Çünkü:" yapıldı).
- **Kuark (yeni biçim):** `KH(kazanim, tur ["eksik"|"yanilgi"], soru, kuark, dogruSik, yanlis1, yanlis2, ipucu, aciklama, once, ornek, sonra, k, havuz)` → `tamamla` {once, ornek, sonra, k, havuz} ve dogruCevap. Yanılgı sayısı eksikten az (doğrulayıcı kontrol eder); 8 eksik + 4 yanılgı iyi denge.
- **Prova:** id, ad, sorular (dağılıma birebir, toplam 100, madde `puan`, `benzer`: MEB soru id); bağlamlar MEB ve ikizlerden farklı. Fen'de `BENZER = {provaId: [mebId, …]}`.
- **Anahtar eşleştirme:** harfler sadeleştirilir (ı→i, ş→s…), kök metinde geçiyorsa bulunur; `sira` anahtarında her öğe bir öncekinden sonra geçmeli (açgözlü arama; motordaki `yzSira` = yazili.py `sira_tamam`). Olumsuz/olumlu kökleri ayır ("yapılmış" / "yapılmamış" alt dize değil); "değil" ile kurulan olumsuzlar yakalanmaz, Ela düzeltir. Kökü kısa tutma (ör. "ağ" "ağır"ı da yakalar).
- **Kuark (eski biçim, bil1):** kazanim, soru, kuark, secenekler 3 (doğrusu ilk; motor karıştırır), ipucu, aciklama, dogruCevap; `tamamla` yok.
- **Doğrulayıcı kontrolleri:** örnek ve kısa cevap kendi anahtarlarını karşılar; parça örneği kendi kontrolünü geçer, çeldirici geçmez; cümle başları anahtarları tetiklemez; tetik ifadeleri soru metninde; basamak 1 = 3 farklı şık, doğru 0; iskele türü kuralları; prova dağılımı ve 100 puan; kazanım/konu kimlikleri.

## 4. Yeni yazılı ekleme (her ders)
1. Kemal'den: kılavuz, **tam** senaryo tablosu, okulun seçtiği senaryo, MEB örnek soruları (+ çözümleri), varsa ek örnekler, sınav tarihi. Senaryo tablosu kesikse sor. Ülke geneli ortak sınav kılavuzunun hangi dersleri kapsadığını kontrol et (2026-27: yalnız 6. Mat, 10. TDE ortak; diğerleri okulun, senaryoya göre).
2. Kaynakları süz: her soruyu kazanıma eşle; kapsam dışı/belirsiz olanları Kemal'e tabloyla göster.
3. Kitap sayfalarını oku (`[s. N]` üstündeki metin N. sayfa); defterdeki ilgili konu dosyalarının kavramlarına bak (dil ve terimler aynı olsun).
4. `<kod>_<id>.py`: kazanımlar → formüller → MEB soruları (+2 ikiz) → **her MEB maddesi için kisaCevap, tetik, kalipNot, basamak** → Kuark (eksik ağırlıklı) → 4 prova. Çalıştır.
5. Yerel test (Playwright; `ela7:ayar` = `{hataDur:false}`; Google Fonts isteğini kes): başlangıç → Hatırla → MEB sorusu 4 basamak (b1 doğru şık, b2 bir yanlış + havuz, b3 ipucu, b4 iki ipucu → seviye artmamalı) → boşluklu madde → kartlar (bir yanlış → tekrar gelir) → Kuark (seç + tamamla) → prova ekranda (yenilemede taslak kalır) → puanla → sınav modu (süre dolumu) → yanlış defteri turu → özet; ders defterine dönünce menü/robot geri gelir; 390 px'te yatay taşma yok; konsol hatası yok. Diğer derslerin yazılıları da açılıyor mu bak (motor ortak).
6. `taslak`'a gönder; önizleme `https://taslak--ela7dersleri.netlify.app/<kod>/#yazili`; canlı için Kemal'e sor (15 kredi).
7. Kemal Ela'yı çalıştırınca geri bildirim gelir; davranışa göre ayarla (ör. hızlı dokunuyorsa seçmeli doğrulama, sıkılıyorsa basamak atlama).

## 5. Derse göre uygulama
- **Fen:** Çizimlerde bilimsel doğruluk (yıldız yaşam yolu, kuvvet/hareket okları). İş sorularında kitabın ifadesi "aynı doğrultu"; belirsiz durumları (zıt yönlü dikey hareket) soru yapma.
- **Matematik:** Basamak 2 parçaları = işlem adımları ("Verilen: … İstenen: … İşlem: … Sonuç: …"); anahtarlar ara sonuç ve sonuç sayıları (`k` kökü olarak sayı; `−` ve `-` ikisini de kabul et); kısa cevap = kilit işlem + sonuç. Kalıp notu problem türüne göre ("Önce payda eşitle, sonra topla"). Kuark eksikleri: birimsiz sonuç, işlemsiz cevap, işaret hatası (yalnız Hatırla'daki sık hatalardan). Sayı yazma için motorun tuş takımı yok; metin kutusu yeterli.
- **Sosyal Bilgiler:** Soru türleri sebep–sonuç, kronoloji (önce/sonra → `sira` anahtarı), kavram–örnek, harita/kaynak yorumlama. Kalıp notları: "Sebep: … Sonuç: …", "Önce …, sonra …". Kısa cevaplarda tarih/kişi/yer adları anahtar; kaynak metinli sorularda tetik = "kaynağa göre", "metinde".
- **Din Kültürü:** ela-ders-defteri bölüm 8'deki dinî içerik kuralları geçerli (kitaptaki meal ve kaynak; tarafsız dil; kişisel ibadet sorusu yok). Kuark yanılgıları yalnız kitapta karışan çiftlerden (hac/umre, farz/vacip). Ayet/sure okunuşu kitaptaki Latin harfli yazımla.
- **Türkçe:** Metinli sorular; basamak 2 parçaları "Metne göre: … Kanıt: …"; anahtar = kavram + metindeki kanıt ifadesi; kalıp notu soru köküne göre ("ana düşünce → tek cümle", "çıkarılabilir mi → evet/hayır + metinden cümle"). Yazım/noktalama sorularında `k` kökü kesin yazım.
- **İngilizce (ing1/own1):** Cevaplar İngilizce; kısa cevap = kitaptaki kalıp cümle ("I'm going to …"); parçalar kalıbın öğeleri (özne / yardımcı / fiil); anahtarlar İngilizce kökler (sadeleştirme Türkçe harfleri etkiler, İngilizcede sorun yok). Yönerge ve kalıp notu Türkçe. `{{…}}` sesli okuma biçimini yazılı verisinde kullanma (motor bu bölümde desteklemiyor).
- **Teknoloji ve Tasarım (bil1):** Senaryo yok; öğretmenin 15 soruluk kâğıdı = "Öğretmenin Soruları" (`soruBaslik`, `ikizsiz`), provalar bu sorulardan seçilir. Kısa cevap/basamak henüz eklenmedi (eklenirse aynı şema).

## 6. Senaryosuz yazılı
Öğretmen çalışma kâğıdı verdiyse: yeni soru yazılmaz, kâğıttaki sorular MEB soruları yerine geçer (`soruBaslik`, `soruEtiket`, `soruGiris`, `ikizsiz: True`); `dagilim` kâğıdın konu dağılımı (varsayımsa puanNotu'nda yaz); provalar kâğıttaki sorulardan.
