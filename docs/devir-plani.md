# Ela 7 Ders Defteri — Devir Planı (17 Ekim 2026)

Yeni sohbet bu dosyayı okuyarak devam eder. Çalışma yöntemi `ela-ders-defteri` skill'indedir (özellikle bölüm 9–10 ve Yayın kuralı). Depo `beydillik/ela7dersleri`, çalışma dalı `taslak`.

## Durum
- Bütün dersler (tr1, mat1, fen1, ing1, own1, sos1) `taslak` dalında. 17 Ekim'de taslak canlıya alındı (`main` = `taslak`, 1e04e85).
- Faz 1 ✅ izleme/robot koç. Faz 2 ✅ Sınav Provası (anında sonuç, inceleme, yeniden çözme), okuma beklemesi + "Neden yanlış yaptın?", bütün derslerin soru havuzları (374 soru). Faz 3 ✅ kod (Firebase Veli Paneli + eşitleme) — **canlı Firebase denemesi yapılmadı**.
- Ela'nın ilerlemesi tarayıcıda taslak adresine bağlı; canlıya kendiliğinden geçmez (taşıma: bulut ya da Veli Paneli → Tam yedek).

## Kararlaştırılan sıra (Kemal onayladı, 17 Ekim)
1. ✅ Faz 3 denemesi taslakta (17 Ekim, Kemal yaptı)
2. ✅ Yayın: taslak → main (17 Ekim 17:51, 128 değişiklik, 15 kredi; kalan ~23,6). Canlıda cihaz bağlama ve robot kontrolü Kemal'de.
3. Din Kültürü + Bilişim (taslakta, ara duraksız, yalnız ünite sonu taraması + Sınav Provası havuzu; her ders ayrı Claude projesi) → ikinci yayın 25 Ekim kredi yenilemesinden sonra (yayın dışı tüketim nedeniyle; Kemal ile kararlaştırıldı)
4. Faz 4: KVKK ve diğer velilere açılış

## 1. Faz 3 denemesi (Kemal için adımlar)
Firebase konsolu: https://console.firebase.google.com → proje **ela7dersleri**.
1. **Giriş yöntemleri:** Sol menü → Security (eski arayüzde Build) → **Authentication**. İlk kez açılıyorsa "Get started". Üstte **Sign-in method** sekmesi → **Add new provider** → **Email/Password** → ilk anahtarı (Email/Password) aç → **Save**. Yine **Add new provider** → **Anonymous** → aç → **Save**. Listede ikisi "Enabled" görünmeli.
2. **Güvenlik kuralları:** Sol menü → Databases & Storage (eski arayüzde Build) → **Firestore Database** → üstte **Rules** sekmesi → kutudaki her şeyi sil → aşağıdaki kuralları yapıştır → **Publish**. ("Database yok" derse daha önce oluşturulmuş olmalı: Create database → europe-west3 → Production mode.)
3. **Veli hesabı (taslakta):** Ela'nın bilgisayarında https://taslak--ela7dersleri.netlify.app/veli/ → e-posta + en az 6 karakter şifre → **Yeni hesap aç** → takma ad "Ela" → **Ekle**.
4. **Cihazı bağla:** Genel sekmesi en altta **Cihazlar** → **Bu cihazı Ela için bağla**. Üstte "1 bağlı cihaz" görünmeli; Ela'nın eski kayıtları panele gelmeli (biraz sürebilir).
5. **Kontrol:** Ela bir ders sayfası açsın, birkaç soru çözsün; 3–5 dk sonra panelde Çıkış → Giriş → yeni kayıt görünmeli. İstersen telefondan aynı adrese girip hesabınla bak. Konsolda Firestore → Data sekmesinde `ogrenciler` koleksiyonu görünür.
6. Hata olursa panelin yazdığı mesajı aynen Claude'a yaz (ör. "İzin yok: Firestore kuralları yayımlanmamış", "Bu giriş yöntemi Firebase'de açık değil").

Kurallar (`araclar/bulut/firestore.rules` ile aynı):
```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    function giris() { return request.auth != null; }
    function ogrenci(ogr) { return get(/databases/$(database)/documents/ogrenciler/$(ogr)).data; }
    function veliMi(ogr) { return giris() && ogrenci(ogr).veli == request.auth.uid; }
    function cihazMi(ogr) { return giris() && request.auth.uid in ogrenci(ogr).cihazlar; }
    function kod(k) { return get(/databases/$(database)/documents/eslestirme/$(k)).data; }

    match /ogrenciler/{ogr} {
      allow create: if giris() && request.resource.data.veli == request.auth.uid
                    && request.resource.data.cihazlar.size() == 0;
      allow list: if giris() && resource.data.veli == request.auth.uid;
      allow get: if giris() && (resource.data.veli == request.auth.uid || request.auth.uid in resource.data.cihazlar);
      allow delete: if giris() && resource.data.veli == request.auth.uid;
      allow update: if giris() && (
        (resource.data.veli == request.auth.uid && request.resource.data.veli == resource.data.veli)
        || (request.resource.data.diff(resource.data).affectedKeys().hasOnly(['cihazlar', 'sonKod'])
            && request.resource.data.cihazlar.hasAll(resource.data.cihazlar)
            && request.resource.data.cihazlar.toSet().difference(resource.data.cihazlar.toSet()) == [request.auth.uid].toSet()
            && kod(request.resource.data.sonKod).ogr == ogr
            && kod(request.resource.data.sonKod).son > request.time)
      );
      match /{alt=**} {
        allow read, write: if veliMi(ogr) || cihazMi(ogr);
      }
    }

    match /eslestirme/{k} {
      allow create: if giris() && request.resource.data.veli == request.auth.uid
                    && ogrenci(request.resource.data.ogr).veli == request.auth.uid;
      allow get, delete: if giris();
      allow list, update: if false;
    }
  }
}
```

## 2. Yayın
- Kemal "yayınla" deyince skill'deki onay sorusu (15 kredi + değişiklik listesi `git log --oneline origin/main..origin/taslak` özeti) → `git checkout main && git pull && git merge --ff-only origin/taslak && git push origin main`.
- Yayından sonra (1–2 dk): https://ela7dersleri.netlify.app/veli/ → veli girişi → Cihazlar → **Bu cihazı Ela için bağla** (canlı adres ayrı site sayılır; ilerleme buluttan gelir). Bundan sonra Ela yalnızca canlı adresi kullanır.
- Kontrol: canlıda bir derste robota soru sor. Cevap gelmezse Netlify → Project configuration → Environment variables → `GEMINI_API_KEY` vb. kapsamı "All deploy contexts" olmalı (değişirse yeniden yayın gerekir, 15 kredi).
- Kredi: her ayın 25'inde yenilenir; kalan kredi Netlify → Team overview → Usage/Billing.

## 3. Din Kültürü ve Bilişim
- Skill iş akışı D (yeni ders aç): kitap metni (A), konulara bölme (B, Kemal onayı), tema/robot, konular (C).
- Ara Durak yok; her ünite sonunda yalnız "Ünite Sonu Taraması" + Sınav Provası havuzu (`araclar/sinav/<kod>_u<no>.py`, konu başına 5–7 soru).
- Ders kodu önerisi: `din1`, `bil1` (robot regex `^[a-z]{2,8}[12]$` ile uyumlu). Ana sayfa `DERSLER` sırasına Kemal'in istediği yere eklenir (sorulacak). Kitap PDF'leri/konu listesi Kemal'den istenir (Bilişim'de MEB kitabı yoksa okulun konu listesi).
- Taslakta hazırlanır, ayrı yayınla canlıya alınır.

## 4. Faz 4 — KVKK ve diğer veliler (hukuki tavsiye değildir; bir KVKK uzmanına teyit ettirilmeli)
Durum: Kemal kendi kızı için kullanırken KVKK yükümlülüğü pratikte doğmaz (kişisel/aile içi kullanım istisnası, KVKK md. 28/1-a — doğrulanmalı). Başka velilere açıldığında Kemal **veri sorumlusu** olur.
- **Aydınlatma metni (md. 10):** kim (veri sorumlusu: Kemal Beydilli, iletişim e-postası), hangi veri (veli e-postası; çocuğun takma adı, çalışma kayıtları: hangi konu, soru sonucu, süre, yanlış nedeni; cihaz kimliği), amaç (çocuğun çalışmasını veliye raporlamak), hukuki sebep (açık rıza), aktarım (Google Firebase, sunucu Frankfurt/AB → **yurt dışına aktarım**), saklama süresi (ör. 90 gün olay kaydı; hesap silinene kadar ilerleme), haklar (md. 11: bilgi isteme, düzeltme, silme, itiraz) ve başvuru yolu. Kayıt ekranında okunabilir bağlantı.
- **Açık rıza (md. 5):** kayıt olurken işaretlenmesi zorunlu, önceden işaretli olmayan kutu: "Aydınlatma metnini okudum; çocuğumun çalışma kayıtlarının bu amaçla işlenmesine ve Firebase (AB) sunucularında saklanmasına açık rıza veriyorum." Rıza tarihi ve metin sürümü öğrenci belgesine yazılır. Rıza geri alınabilmeli (hesabı sil).
- **Yurt dışına aktarım (md. 9, Mart 2024 değişikliği):** Firebase AB'de olduğu için yurt dışı aktarımdır. Değişiklikten sonra ana yol uygun güvenceler (ör. standart sözleşme; imzadan sonra 5 iş günü içinde Kurum'a bildirim); açık rıza yalnız arızi aktarımlar için. Google'ın Türkiye standart sözleşmesi sunup sunmadığı **doğrulanamadı** — Faz 4'te araştırılmalı. Kaynaklar: https://www.kvkk.gov.tr/Icerik/8043/Standart-Sozlesme-Bildirim-Modulu-Hakkinda-Kamuoyu-Duyurusu , https://www.hukukihaber.net/kvkk-yurt-disina-aktarim-kapsaminda-yapilan-kanun-degisikligi
- **VERBİS:** gerçek kişi, az çalışan/küçük bilanço ve ana faaliyeti özel nitelikli veri işleme olmayan veri sorumluları istisna olabilir (tahmin; güncel kriterler doğrulanmalı): https://www.erdem-erdem.av.tr/bilgi-bankasi/verbis-kayit-yukumlulugune-iliskin-yeni-istisnalarin-uygulama-esaslari-aciklandi , https://www.alomaliye.com/2025/10/01/ozel-nitelikli-kisisel-veri-isleme-veri-sorumlularinin-verbise-kayit-yukumlulugune-iliskin-istisna-kriteri/
- **Veri en aza indirme:** gerçek ad istenmez (takma ad zaten var); özel nitelikli veri (sağlık, örn. dikkat eksikliği bilgisi) **hiç toplanmaz**; robot sorularında çocuğun yazdığı metin Gemini'ye gider → aydınlatmada belirtilmeli ya da başka velilerde robot kapatılabilir (karar Kemal'in).
- **Teknik işler (Claude):** kayıt ekranına aydınlatma bağlantısı + rıza kutusu (`rıza: {tarih, surum}`), "Hesabımı ve bütün verilerimi sil" düğmesi (öğrenci, oturumlar, ilerleme, eşleştirme kodları; Firebase Auth hesabı), "Verilerimi indir" (zaten rapor JSON'u var), Firestore kurallarında veli başına sınır, Firebase'de bütçe uyarısı (Spark ücretsiz; Blaze'e geçilmez). Öğretmenler için: bağlanmamış cihaz veri göndermez — paylaşımda değişiklik gerekmez.
- **Kemal'in işleri:** aydınlatma ve rıza metnini bir KVKK uzmanına okutmak; iletişim e-postası belirlemek; yurt dışı aktarım yolunu netleştirmek.
