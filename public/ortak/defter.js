/* Ela'nın 7. Sınıf Defteri — ortak motor.
   Her ders klasörü (ör. /fen1/) bu dosyayı yükler; ders ayarlarını ./ders.json'dan,
   konuları ./konular/<id>.json'dan okur. Yeni konu eklemek için bu dosyaya dokunulmaz. */
(() => {
  "use strict";
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const store = {
    get(k, d = null) { try { const v = localStorage.getItem(k); return v === null ? d : JSON.parse(v); } catch (e) { return d; } },
    set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
  };
  const lower = s => String(s).toLocaleLowerCase("tr");
  const shuffle = a => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  const pick = a => a[Math.floor(Math.random() * a.length)];

  const ICON = {
    ogren: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 5h7a3 3 0 0 1 3 3v11a2 2 0 0 0-2-2H4z"/><path d="M20 5h-4a2 2 0 0 0-2 2"/><path d="M20 5v12h-6"/></svg>',
    bak: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="6"/><path d="m20 20-4.5-4.5"/></svg>',
    tekrar: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 12a8 8 0 0 1 14-5.3L20 9"/><path d="M20 4v5h-5"/><path d="M20 12a8 8 0 0 1-14 5.3L4 15"/><path d="M4 20v-5h5"/></svg>',
    test: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="5" y="3" width="14" height="18" rx="2"/><path d="m9 12 2 2 4-4"/></svg>',
    mik: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></svg>',
    yazdir: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 9V3h10v6"/><rect x="3" y="9" width="18" height="8" rx="2"/><path d="M7 14h10v7H7z"/></svg>',
    okuma: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M3 5h6a3 3 0 0 1 3 3v12a2 2 0 0 0-2-2H3z"/><path d="M21 5h-6a3 3 0 0 0-3 3v12a2 2 0 0 1 2-2h7z"/></svg>',
    yavas: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 16h13a3 3 0 0 0 3-3v-1"/><path d="M5 16a6 6 0 0 1 12 0"/><circle cx="20" cy="10" r="2"/><path d="M7 16v2M15 16v2"/></svg>',
    ses: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 10v4h4l5 4V6L8 10z"/><path d="M16 9a4 4 0 0 1 0 6"/><path d="M18.5 6.5a8 8 0 0 1 0 11"/></svg>',
    ampul: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.6 10.8c.7.6 1.1 1.3 1.1 2.2h5c0-.9.4-1.6 1.1-2.2A6 6 0 0 0 12 3z"/></svg>',
    durak: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M6 21V4"/><path d="M6 4h11l-2.5 4L17 12H6"/></svg>'
  };

  const PRAISE = {
    first: ["Doğru! Dikkatlice okudun.", "Doğru! Bilgiyi güzel hatırladın.", "Doğru! Acele etmeden düşündün."],
    second: ["Doğru! İpucunu iyi kullandın.", "Doğru! İkinci denemede buldun, pes etmedin.", "Doğru! Bilgi kartını hatırlaman işe yaradı."],
    shown: ["Olsun, şimdi öğrendin. Açıklamayı bir kez daha oku.", "Bunu birlikte öğrendik. Tekrar bölümünde yine karşına çıkacak."]
  };

  // ---------- Sesli okuma ----------
  // İki ses: Türkçe metin Türkçe sesle, {{...}} içindeki İngilizce parçalar ABD İngilizcesi sesle okunur.
  // Ses önceliği: doğal (Natural) sesler önce, eski Windows sesleri (Tolga, Zira) en son.
  const VOICE_PREF = {
    tr: [/emel.*natural/i, /ahmet.*natural/i, /google türkçe/i, /türkçe.*natural/i, /yelda/i, /cem/i, /tolga/i],
    en: [/jenny.*natural/i, /ava.*natural/i, /aria.*natural/i, /emma.*natural/i, /andrew.*natural/i, /google us english/i,
         /us english.*natural/i, /samantha/i, /\bava\b/i, /zira/i, /david/i]
  };
  const EN_RE = /\{\{(.+?)\}\}/g;
  // Matematik ifadelerini Türkçe okunuşa çevirir: -3 → eksi 3, [[3/4]] → 4'te 3, < → küçüktür.
  const BULUNMA = n => { const s = String(n), son = s.replace(/0+$/, "") || "0", z = s.length - son.length, d = +son.slice(-1);
    if (z === 1) return ({ 1: "da", 2: "de", 3: "da", 4: "ta", 5: "de", 6: "ta", 7: "te", 8: "de", 9: "da" })[d] || "da";
    if (z >= 2) return z === 2 ? "de" : "de";
    return ({ 0: "da", 1: "de", 2: "de", 3: "te", 4: "te", 5: "te", 6: "da", 7: "de", 8: "de", 9: "da" })[d]; };
  const mathSay = s => String(s)
    .replace(/(\d*),(\d*)\[\[d:(\d+)\]\]/g, (m, a, b, c) => `${a || "0"} virgül ${b ? b + " " : ""}devreden ${c}`).replace(/\[\[d:(\d+)\]\]/g, " devreden $1")
    .replace(/\[\[u:(\d+|n)\]\]/g, " üssü $1")
    .replace(/\[\[(-?)(?:(\d+) )?([-−]?\d+)\/(-?\d+)\]\]/g, (m, sg, w, a, b) => `${sg ? "eksi " : ""}${w ? w + " tam " : ""}${b.replace("-", "eksi ")}'${BULUNMA(b.replace("-", ""))} ${a.replace(/[-−]/, "eksi ")}`)
    .replace(/\|([^|]{1,12})\|/g, "mutlak değer $1")
    .replace(/(^|[\s(=:,;])[-−](\d)/g, "$1eksi $2").replace(/(^|[\s(=:,;])\+(\d)/g, "$1artı $2")
    .replace(/(\d)[\s\u00a0]?°C/g, "$1 derece").replace(/(\d)[\s\u00a0]m\b/g, "$1 metre").replace(/\s*→\s*/g, ", ")
    .replace(/\s<\s/g, " küçüktür ").replace(/\s>\s/g, " büyüktür ").replace(/\s=\s/g, " eşittir ")
    .replace(/(\d)\s[-−]\s/g, "$1 eksi ").replace(/(\d|\))\s\+\s/g, "$1 artı ").replace(/\s[×·]\s/g, " çarpı ").replace(/\s÷\s/g, " bölü ");
  const tts = {
    voice: null, en: null,
    init() {
      if (!("speechSynthesis" in window)) return;
      const best = (list, prefs) => { for (const r of prefs) { const v = list.find(x => r.test(x.name)); if (v) return v; } return list[0] || null; };
      const pickVoice = () => {
        const all = speechSynthesis.getVoices(), L = x => x.lang.replace("_", "-");
        tts.voice = best(all.filter(x => /^tr/i.test(L(x))), VOICE_PREF.tr);
        const us = all.filter(x => /^en-US/i.test(L(x)));
        tts.en = best(us.length ? us : all.filter(x => /^en/i.test(L(x))), VOICE_PREF.en);
        document.body.classList.toggle("no-tts", !tts.voice);
        document.body.classList.toggle("no-tts-en", !tts.en);
        $$(".listen").forEach(b => b.hidden = !tts.voice);
        $$(".say-en").forEach(b => b.hidden = !tts.en);
      };
      pickVoice();
      speechSynthesis.onvoiceschanged = pickVoice;
    },
    utter(text, v, rate) {
      const u = new SpeechSynthesisUtterance(text);
      u.voice = v; u.lang = v.lang.replace("_", "-"); u.rate = rate; speechSynthesis.speak(u);
      return u;
    },
    // Karışık metni parçalara ayırıp sırayla okur.
    say(text) {
      if (!tts.voice && !tts.en) return;
      speechSynthesis.cancel();
      String(text).split(EN_RE).forEach((part, i) => {
        const en = i % 2 === 1;
        if (!en) part = mathSay(part);
        part = part.trim(); if (!part || !/[\p{L}\p{N}]/u.test(part)) return;
        const v = en ? (tts.en || tts.voice) : (tts.voice || tts.en);
        tts.utter(part, v, en ? .85 : .95);
      });
    },
    // Yalnızca İngilizce metin (kelime, örnek cümle). slow: yavaş okuma.
    sayEn(text, slow) {
      if (!tts.en) return;
      speechSynthesis.cancel(); tts.utter(String(text).replace(EN_RE, "$1"), tts.en, slow ? .6 : .85);
    },
    stop() { if ("speechSynthesis" in window) speechSynthesis.cancel(); }
  };
  const listenBtn = text => `<button class="listen" data-say="${esc(text)}" ${tts.voice ? "" : "hidden"}>${ICON.ses}Dinle</button>`;
  // İngilizce dinleme düğmeleri: normal hız ve yavaş (kaplumbağa)
  const enBtns = (text, big) => `<span class="say-en-row"><button class="say-en${big ? " big" : ""}" data-say-en="${esc(text)}" aria-label="İngilizcesini dinle" ${tts.en ? "" : "hidden"}>${ICON.ses}</button><button class="say-en slow" data-say-en="${esc(text)}" data-slow aria-label="Yavaş dinle" ${tts.en ? "" : "hidden"}>${ICON.yavas}</button></span>`;
  // Matematik: metin içinde [[3/4]], [[-3/4]], [[2 3/4]], [[-2 3/4]] alt alta kesir olarak gösterilir.
  const FR_RE = /\[\[(-?)(?:(\d+) )?([-−]?\d+)\/(-?\d+)\]\]/g;  // [[-9/3]] eksi kesrin önünde, [[−9/3]] (U+2212) payda, [[9/-3]] paydada
  // Devirli ondalık: 0,1[[d:6]] → devreden rakamların üstü çizili (0,16̄); sesli okumada "0 virgül 1 devreden 6".
  const DV_RE = /\[\[d:(\d+)\]\]/g;
  // Üs: 5[[u:4]], ([[2/3]])[[u:5]] → üst simge; sesli okumada "5 üssü 4"; oyunlarda Unicode üst simge (5⁴).
  const US_RE = /\[\[u:(\d+|n)\]\]/g, USTK = { 0: "⁰", 1: "¹", 2: "²", 3: "³", 4: "⁴", 5: "⁵", 6: "⁶", 7: "⁷", 8: "⁸", 9: "⁹", n: "ⁿ" };
  const fx = h => h.replace(US_RE, '<sup class="us">$1</sup>').replace(DV_RE, '<span class="devir">$1</span>').replace(FR_RE, (m, s, w, a, b) => `<span class="kesir-w">${s ? "−" : ""}${w || ""}<span class="kesir"><span>${a.replace("-", "−")}</span><span>${b.replace("-", "−")}</span></span></span>`);
  // Metin içi {{İngilizce}} parçaları: renkli gösterilir, dokununca okunur.
  const rx = s => fx(esc(s).replace(EN_RE, (m, t) => `<span class="en" lang="en" role="button" tabindex="0" data-say-en="${t}">${t}</span>`));
  const plain = s => String(s ?? "").replace(EN_RE, "$1").replace(US_RE, (m, u) => [...u].map(c => USTK[c]).join("")).replace(DV_RE, (m, d) => d.replace(/\d/g, "$&\u0305")).replace(FR_RE, (m, s_, w, a, b) => `${s_}${w ? w + " " : ""}${a}/${b}`);
  document.addEventListener("click", e => {
    const e1 = e.target.closest("[data-say-en]"); if (e1) { e.stopPropagation(); tts.sayEn(e1.dataset.sayEn, e1.hasAttribute("data-slow")); return; }
    const b = e.target.closest("[data-say]"); if (b) tts.say(b.dataset.say);
  }, true);

  // ---------- Durum ----------
  const S = { ders: null, konu: null, data: null, unit: 0, tab: "ogren", cache: {} };
  const key = k => `ela7:${S.ders.kod}:${k}`;
  const isEn = () => !!(S.ders && S.ders.dil === "en");          // İngilizce dersi: kavram adları İngilizce
  const adSay = k => isEn() ? `{{${k.ad}}}` : k.ad;              // sesli okumada kavram adı
  const kSay = k => `${adSay(k)}. ${k.aciklama} ${k.ek || ""} ${k.ornek ? `Örnek: {{${plain(k.ornek)}}}.` : ""} Akılda kalsın: ${k.akilda}.`;
  const adHTML = (k, big) => `${esc(k.ad)}${isEn() ? enBtns(k.ad, big) + (big ? recBtn(k.ad) : "") : ""}`;
  const ornekHTML = k => k.ornek ? `<div class="ornek"><div class="ornek-en"><span lang="en">${esc(plain(k.ornek))}</span>${enBtns(plain(k.ornek))}</div>${k.ornekTr ? `<div class="ornek-tr">${rx(k.ornekTr)}</div>` : ""}</div>` : "";

  // Kavram bazında sonuç: 1 = ilk denemede, 2 = ikinci denemede, 0 = gösterildi
  const results = {
    all() { return store.get(key("sonuc:" + S.konu), {}); },
    set(ad, v) { const r = results.all(); r[ad] = v; store.set(key("sonuc:" + S.konu), r); },
    weakFirst(list) {
      const r = results.all(), score = k => (k.ad in r ? r[k.ad] : 3);
      const w = x => x === 0 ? 0 : x === 2 ? 1 : 2;
      return list.slice().sort((a, b) => w(score(a)) - w(score(b)));
    },
    isWeak(ad) { const r = results.all(); return ad in r && r[ad] !== 1; }
  };

  // =================================================================
  // ---------- Etkinlik kaydı (v1) ----------
  // Her olay bir satır olarak tarayıcının IndexedDB'sine ("ela7kayit" → "olaylar") yazılır; son 90 gün tutulur.
  // Bütün dersler aynı kaydı paylaşır (aynı site). Alanların anlamı KAYIT_SOZLUK'te; yedek dosyasına da yazılır.
  // Oturum: 30 dakikadan uzun ara verilince yeni oturum başlar. Aktif süre olaylar arası boşluklardan (en çok 3 dk) hesaplanır.
  // =================================================================
  const KAYIT_V = 1, OTURUM_ARA = 30 * 60e3, KAYIT_GUN = 90, BOSLUK_TAVAN = 3 * 60e3;
  const simdi = () => Date.now();
  const p2 = n => String(n).padStart(2, "0");
  const yerelZaman = ts => { const d = new Date(ts); return `${d.getFullYear()}-${p2(d.getMonth() + 1)}-${p2(d.getDate())}T${p2(d.getHours())}:${p2(d.getMinutes())}:${p2(d.getSeconds())}`; };
  const kisa = (s, n = 60) => { const t = plain(String(s ?? "")).replace(/\s+/g, " ").trim(); return t.length > n ? t.slice(0, n - 1) + "…" : t; };
  const kelimeSay = x => typeof x === "string" ? (plain(x).match(/[\p{L}\p{N}]+/gu) || []).length
    : Array.isArray(x) ? x.reduce((a, y) => a + kelimeSay(y), 0) : x && typeof x === "object" ? kelimeSay(Object.values(x)) : 0;
  const soruKelime = o => kelimeSay([o.soru, o.secenekler || [], o.metin || [], o.tablo ? [o.tablo.basliklar, o.tablo.satirlar] : []]);
  // Hızlı cevap eşiği: saniyede 4,5 kelimeden hızlı okunamaz (7. sınıf için cömert bir sınır), en az 2 sn.
  const okumaEsik = kelime => Math.max(2, kelime / 4.5);
  const cihazId = (() => { let c = store.get("ela7:cihaz"); if (!c) { c = Math.random().toString(36).slice(2, 10); store.set("ela7:cihaz", c); } return c; })();

  const KAYIT_SOZLUK = {
    _aciklama: "Ela'nın Defteri etkinlik kaydı. Her satır bir olay. Zamanlar cihazın yerel saatiyle (Türkiye).",
    alanlar: {
      v: "Kayıt biçimi sürümü (1)", k: "Olayın benzersiz kimliği", ts: "Zaman damgası (ms)", t: "Yerel tarih-saat (YYYY-AA-GGTss:dd:ss)",
      cihaz: "Cihaz kimliği (tarayıcıya özgü rastgele)", oturum: "Oturum kimliği (30 dk ara → yeni oturum)",
      ders: "Ders kodu (tr1 Türkçe, mat1 Matematik, fen1 Fen, ing1 İngilizce MEB, own1 İngilizce Own It, sos1 Sosyal)",
      konu: "Konu kimliği (u1k2 = 1. ünite 2. konu; u1t1 = 1. ünite Ara Durak 1; atolye:<metin> = Okuma Atölyesi)", konuBaslik: "Konunun adı",
      bolum: "Ekran: ogren (Öğren), bak (Konuya Bak), tekrar (Tekrar oyunları), test (Test), okuma (Oku ve Dinle), hatirla / tarama / oyunlar (Ara Durak), atolye, rapor",
      olay: "Olay türü (aşağıdaki 'olaylar' listesi)",
      soru: "Soru metninin başı (en çok 60 harf)", tur: "Soru türü: secim (şıklı), nokta (sayı doğrusunda seçme), girdi (sayı yazma); test olaylarında test / tarama",
      sonuc: "1 = ilk denemede doğru, 2 = ipucuyla ya da ikinci denemede doğru, 0 = iki yanlıştan sonra cevap gösterildi",
      sureSn: "Soruda ya da adımda geçen toplam süre (sn)", ilkSn: "Soru açıldıktan sonra ilk cevaba kadar geçen süre (sn)",
      esikSn: "Bu sorunun okunması için gereken en kısa süre tahmini (kelime / 4,5, en az 2 sn). ilkSn bundan küçükse 'hizli' bayrağı",
      ipucu: "Açılan ipucu adımı sayısı", yanlis: "Seçilen yanlış şıklar (sırayla)", kanit: "Kanıtı bul: 1 ilk dokunuşta, 2 ikinci dokunuşta, 0 gösterildi",
      tekrar: "true: yanlıştan sonra testin sonuna doğru yeniden gelen soru", kavram: "Sorunun bağlı olduğu kavram",
      bayrak: "Uyarı işaretleri: hizli (okumadan cevap), hizli-gecis (Öğren kartını okumadan geçti)",
      adim: "Öğren adım no", toplam: "Toplam adım / soru sayısı", adimTur: "Öğren adımının türü: giris, hazir, bilgi, cozum, soru, hatirla, ozet, yaz, bitis",
      oyun: "Oyun adı (kart, eslestir, grupla, dinle, kur, cumle, resim, hata, gunluk)", oge: "Oyundaki öğe sayısı",
      mesaj: "Robotun gösterdiği mesajın türü", metin: "Mesaj ya da robota sorulan sorunun başı", secim: "Robot mesajında Ela'nın dokunduğu düğme",
      ilk1: "Testte ilk denemede doğru sayısı", ilk2: "Testte ipucuyla/ikinci denemede doğru sayısı", ilk0: "Testte cevabı gösterilen (sonra tekrar gelen) soru sayısı",
      tekrarSoru: "Testte yeniden gelen soru sayısı", sureDk: "Test süresi (dk)", seviye: "Okuma Atölyesi seviyesi", dogru: "Doğru sayısı"
    },
    olaylar: {
      "konu-ac": "Konu ya da Ara Durak açıldı", sekme: "Ekran (sekme) değişti", adim: "Öğren'de bir adımdan çıkıldı (sureSn o adımda geçen süre)",
      "ogren-bitti": "Öğren'in son adımına gelindi", atlama: "Öğren bitmeden Test'e geçildi", soru: "Bir soru cevaplandı (her soru türü, her ekran)",
      "test-basla": "Test ya da Ara Durak taraması başladı", "test-bitti": "Test ya da tarama bitti (ilk1/ilk2/ilk0 ilk deneme sonuçları)",
      "oyun-ac": "Tekrar oyunu açıldı", oyun: "Oyun turu bitti (yanlis = yanlış dokunuş sayısı)", "oyun-rastgele": "Oyunda 1,5 sn'den kısa arayla art arda yanlış dokunuş",
      robot: "Robot (Hece, Kuark…) bir uyarı ya da yönlendirme gösterdi", "robot-cevap": "Ela robot mesajındaki bir düğmeye dokundu",
      "robot-soru": "Ela robota (yapay zekâ) bir soru yazdı", "atolye-tur": "Okuma Atölyesi turu bitti", "rapor-ac": "Veli raporu açıldı"
    }
  };

  // IndexedDB sarmalayıcı (açılamazsa kayıt sessizce atlanır; site çalışmaya devam eder)
  const KDB = {
    hazir: null,
    ac() {
      if (this.hazir) return this.hazir;
      this.hazir = new Promise(res => {
        try {
          const r = indexedDB.open("ela7kayit", 1);
          r.onupgradeneeded = () => { const db = r.result; if (!db.objectStoreNames.contains("olaylar")) db.createObjectStore("olaylar", { keyPath: "k" }).createIndex("ts", "ts"); };
          r.onsuccess = () => res(r.result);
          r.onerror = r.onblocked = () => res(null);
        } catch (e) { res(null); }
      });
      return this.hazir;
    },
    async yaz(liste) {
      const db = await this.ac(); if (!db || !liste.length) return;
      try { const tx = db.transaction("olaylar", "readwrite"), os = tx.objectStore("olaylar"); liste.forEach(o => os.put(o)); } catch (e) {}
    },
    async hepsi() {
      const db = await this.ac(); if (!db) return [];
      return new Promise(res => { try { const q = db.transaction("olaylar").objectStore("olaylar").getAll(); q.onsuccess = () => res((q.result || []).sort((a, b) => a.ts - b.ts)); q.onerror = () => res([]); } catch (e) { res([]); } });
    },
    async temizle() {     // 90 günden eski olayları sil (günde bir kez)
      if (store.get("ela7:temizlik") === gun()) return; store.set("ela7:temizlik", gun());
      const db = await this.ac(); if (!db) return;
      try { const tx = db.transaction("olaylar", "readwrite"); tx.objectStore("olaylar").index("ts").openCursor(IDBKeyRange.upperBound(simdi() - KAYIT_GUN * 864e5)).onsuccess = e => { const c = e.target.result; if (c) { c.delete(); c.continue(); } }; } catch (e) {}
    }
  };

  // Oturum bilgisi ve sayaçlar localStorage'da ("ela7:oturum"): sayfalar (dersler) arasında aynı oturum sürer.
  const OT = { kuyruk: [], zam: null, seq: 0 };
  const KAYIT = {
    oturum(ts) {
      const o = store.get("ela7:oturum", null);
      const yeni = !o || ts - o.son >= OTURUM_ARA;
      const v = yeni ? { id: `${yerelZaman(ts).replace(/[-:]/g, "").replace("T", "-").slice(0, 13)}-${cihazId.slice(0, 4)}`, bas: ts, son: ts, sayac: { soru: 0, ilk: 0, ipucu: 0 }, plan: [] } : { ...o, son: ts };
      store.set("ela7:oturum", v); return v;
    },
    olay(olay, ek = {}) {
      const ts = simdi(), o = this.oturum(ts);
      const ev = { v: KAYIT_V, k: `${cihazId}-${ts}-${++OT.seq}`, ts, t: yerelZaman(ts), cihaz: cihazId, oturum: o.id,
        ders: S.ders ? S.ders.kod : "", konu: S.konu || "", konuBaslik: S.data ? S.data.baslik || "" : S.botBaslik || "",
        bolum: S.konu && String(S.konu).startsWith("atolye") ? "atolye" : S.tab || "", olay, ...ek };
      OT.kuyruk.push(ev); clearTimeout(OT.zam); OT.zam = setTimeout(() => this.bosalt(), 700);
      return ev;
    },
    sayac(f) { const o = store.get("ela7:oturum", null); if (!o) return {}; f(o.sayac = o.sayac || {}); store.set("ela7:oturum", o); return o.sayac; },
    bosalt() { const q = OT.kuyruk.splice(0); if (q.length) KDB.yaz(q); }
  };
  addEventListener("pagehide", () => KAYIT.bosalt());
  document.addEventListener("visibilitychange", () => { if (document.hidden) KAYIT.bosalt(); });

  // Veli ayarları (PIN'li rapor ekranından değiştirilir). Varsayılan: robot uyarıları açık, kilitler kapalı.
  const AYAR_VARSAYILAN = { robotUyari: true, sikBekle: false, oyunKilit: false, ogrenKilit: false };
  const ayar = () => ({ ...AYAR_VARSAYILAN, ...(store.get("ela7:ayar", {}) || {}) });

  // =================================================================
  // ---------- Robot koç: dersin robotu (Hece, Kuark, Pisi…) kısa uyarı ve yönlendirme baloncukları gösterir ----------
  // Mesajlar hazır cümlelerdir (yapay zekâ kullanılmaz, kota harcamaz). Aynı tür mesaj 3 dakikada bir kereden fazla çıkmaz.
  // =================================================================
  const KOC_ARA = 3 * 60e3;
  const KOC = {
    son: {}, hizliDogru: 0,
    goster(tur, metin, dugmeler = [], sure = 10000) {
      if (!ayar().robotUyari) return null;
      const t = simdi(); if (this.son[tur] && t - this.son[tur] < KOC_ARA) return null; this.son[tur] = t;
      this.kapat();
      const b = (S.ders && S.ders.bot) || {}, el = document.createElement("div");
      el.className = "koc"; el.setAttribute("role", "status"); el.setAttribute("aria-live", "polite");
      el.innerHTML = `<div class="koc-mask">${b.svg || ""}</div><div class="koc-ic"><b>${esc(b.ad || "Robot")}</b><p>${metin}</p>
        ${dugmeler.length ? `<div class="koc-dug">${dugmeler.map((d, i) => `<button class="btn${d.birincil ? " primary" : " ghost"}" data-kd="${i}">${esc(d.etiket)}</button>`).join("")}</div>` : ""}</div>
        <button class="koc-x" aria-label="Kapat">×</button>`;
      document.body.appendChild(el);
      requestAnimationFrame(() => el.classList.add("acik"));
      $(".koc-x", el).onclick = () => this.kapat();
      $$("[data-kd]", el).forEach(x => x.onclick = () => { const d = dugmeler[+x.dataset.kd]; KAYIT.olay("robot-cevap", { mesaj: tur, secim: d.etiket }); this.kapat(); d.fn && d.fn(); });
      if (!dugmeler.length) this.zam = setTimeout(() => this.kapat(), sure);
      KAYIT.olay("robot", { mesaj: tur, metin: kisa(metin.replace(/<[^>]+>/g, ""), 80) });
      return el;
    },
    kapat() { clearTimeout(this.zam); $$(".koc").forEach(x => x.remove()); },
    // Her soru bittiğinde çağrılır (izle → onDone)
    soruSonrasi(o, r, bayrak, opts) {
      if (bayrak.includes("hizli") && r !== 1) return this.goster("hizli", "Biraz hızlı gittin. Bir sonraki soruda önce soruyu sonuna kadar oku, sonra şıklara bak. Acele yok!");
      if (r === 0 && opts.davet) return this.goster("davet", "Bu soru zor geldi. İstersen birlikte bakalım; neden bu cevap olduğunu adım adım anlatırım.",
        [{ etiket: "Birlikte bakalım", birincil: true, fn: () => S.botSor && S.botSor(davetMetni(o)) }, { etiket: "Şimdilik geç" }]);
      if (r === 1 && bayrak.includes("hizli") && ++this.hizliDogru % 3 === 0) return this.goster("nasil", "Çok çabuk buldun! Bu cevabı nasıl buldun?", [
        { etiket: "Kartta / metinde gördüm" }, { etiket: "Hatırladım" },
        { etiket: "Tahmin ettim", fn: () => setTimeout(() => this.goster("tahmin", "Dürüst cevabın için teşekkürler! Açıklamayı bir kez oku; bir dahakine bilerek bulursun."), 300) }]);
    },
    // Oturumdaki çalışmanın kısa özeti (çabaya övgü)
    ozet() {
      const s = (store.get("ela7:oturum", null) || {}).sayac || {};
      if (!s.soru) return;
      const ip = s.ipucu ? `, ${s.ipucu} kez ipucunu iyi kullandın` : "";
      setTimeout(() => this.goster("ozet", `Bugün ${s.soru} soru çözdün: ${s.ilk} tanesini ilk denemede buldun${ip}. Emeğine sağlık!`), 600);
    },
    // Oturum başı planı: bu derste ilk açılışta, tekrar zamanı gelen durak ya da son konuda zorlanılan kavramlar
    plan() {
      const o = store.get("ela7:oturum", null); if (!o || (o.plan || []).includes(S.ders.kod)) return;
      o.plan = [...(o.plan || []), S.ders.kod]; store.set("ela7:oturum", o);
      const vade = allTopics().filter(k => isDurak(k) && k.hazir && durakKayit.zaman(k.id));
      const son = store.get(key("son")), r = son ? sonucOf(son) : {}, zor = Object.keys(r).filter(a => r[a] !== 1).slice(0, 2);
      setTimeout(() => {
        if (vade.length) this.goster("plan", `Hoş geldin! Bugün için önerim: <b>${esc(vade[0].baslik)}</b> için tekrar zamanı geldi. Kısa bir tarama yapalım mı?`,
          [{ etiket: "Açalım", birincil: true, fn: () => openKonu(vade[0].id, true) }, { etiket: "Sonra" }]);
        else if (zor.length && son && son !== S.konu) this.goster("plan", `Hoş geldin! Geçen sefer <b>${zor.map(esc).join("</b> ve <b>")}</b> kavramında zorlanmıştın. Önce bir göz atalım mı?`,
          [{ etiket: "Bakalım", birincil: true, fn: () => { store.set(key("sekme:" + son), "bak"); openKonu(son, true); } }, { etiket: "Sonra" }]);
        else if (zor.length) this.goster("plan", `Hoş geldin! Geçen sefer <b>${zor.map(esc).join("</b> ve <b>")}</b> kavramında zorlanmıştın. Konuya Bak'ta bir göz atabilirsin.`,
          [{ etiket: "Bakalım", birincil: true, fn: () => setTab("bak") }, { etiket: "Sonra" }]);
      }, 1200);
    }
  };
  const davetMetni = o => {
    const dogru = qKind(o) === "secim" ? (o.secenekler || [])[o.dogru] : qKind(o) === "nokta" ? o.nokta : o.cevap;
    return `Bu soruyu anlamadım: "${kisa(o.soru, 200)}" Doğru cevap: "${kisa(dogru, 120)}". Bu cevap neden doğru, kısaca ve adım adım açıklar mısın?`;
  };

  // Her soruyu izler: süre, ilk cevap, ipucu, yanlış şıklar; sonucu kaydeder ve robot koça haber verir.
  function izle(el, o, opts) {
    const st = opts.state = opts.state || { wrong: [], result: undefined };
    if (opts.izlendi || st.result !== undefined) return;          // geri yüklenen (zaten kaydedilmiş) soru
    opts.izlendi = true;
    const t0 = simdi(); let ilk = null;
    el.addEventListener("click", e => {
      if (ilk === null && e.target.closest(".opt, .cumle, .kp-k, .kp-ok, .sd-hit")) ilk = simdi();
    }, true);
    const asil = opts.onDone;
    opts.onDone = r => {
      const sn = (simdi() - t0) / 1000, ilkSn = ilk ? (ilk - t0) / 1000 : sn, esik = okumaEsik(soruKelime(o));
      const bayrak = ilkSn < esik ? ["hizli"] : [];
      KAYIT.olay("soru", { soru: kisa(o.soru), tur: qKind(o), sonuc: r, sureSn: +sn.toFixed(1), ilkSn: +ilkSn.toFixed(1), esikSn: +esik.toFixed(1),
        ipucu: st.yardim || 0, yanlis: (st.wrong || []).map(j => kisa((o.secenekler || [])[j], 40)), kanit: st.kanit,
        tekrar: !!opts.tekrar, kavram: (opts.kavram && opts.kavram.ad) || o.kavram || "", bayrak });
      KAYIT.sayac(s => { s.soru = (s.soru || 0) + 1; if (r === 1) s.ilk = (s.ilk || 0) + 1; if (r === 2 && st.yardim) s.ipucu = (s.ipucu || 0) + 1; });
      asil && asil(r);
      KOC.soruSonrasi(o, r, bayrak, opts);
    };
  }

  // Oyunlarda art arda hızlı yanlış dokunuş → "Dur, düşün" (+ veli ayarıyla 3 sn düşünme molası)
  const OYUN = { son: 0, art: 0 };
  function oyunHata(box, oyun) {
    const t = simdi(), hizli = t - OYUN.son < 1500; OYUN.son = t;
    OYUN.art = hizli ? OYUN.art + 1 : 0;
    if (OYUN.art < 1) return;
    OYUN.art = 0; KAYIT.olay("oyun-rastgele", { oyun });
    KOC.goster("rastgele", "Dur, önce düşün. Kartı oku, eşini zihninde bul, sonra dokun. Rastgele dokunmak yıldız kazandırmaz.");
    if (ayar().oyunKilit && box) { box.classList.add("dusun-mola"); setTimeout(() => box.classList.remove("dusun-mola"), 3000); }
  }

  // ---------- Çoklu deneme soru bileşeni ----------
  // o: {soru, secenekler, dogru, ipucu, aciklama}; opts: {onDone(result), backToInfo, classMode}
  // Soru türleri: seçenekli (secenekler + dogru), sayı doğrusunda nokta seçme (nokta + sayiDogrusu),
  // sayı yazma (cevap; tuş takımıyla). sayiDogrusu seçenekli ve yazmalı sorularda da yalnızca gösterim olarak eklenebilir.
  const qKind = o => o.nokta !== undefined ? "nokta" : o.cevap !== undefined ? "girdi" : "secim";
  // ---------- Paragraf ve "Kanıtı bul" (Okuma Dedektifi) ----------
  // Soruya isteğe bağlı: "metin" (cümle dizisi; paragraflı metinde dizi dizisi; diyalogda {"kim", "s"}),
  // "tablo" ({baslik?, basliklar, satirlar}), "metinBaslik", "kanit" (kanıt cümlelerinin sırası, 0'dan; tablo satırı "t0", "t1"…),
  // "kanitIpucu". kanit varsa önce kanıt cümlesine dokunulur, sonra şıklar açılır (2 hak; 2. yanlışta kanıt gösterilir).
  // "ima": true → seçenekler "açıkça yazıyor / ima ediliyor" olur (secenekler verilmezse).
  const IMA_SEC = ["Metinde açıkça yazıyor.", "Metinde yazmıyor, ima ediliyor."];
  const cumleMetin = c => typeof c === "string" ? c : (c && c.s) || "";
  const paragraflar = m => !m || !m.length ? [] : Array.isArray(m[0]) ? m : [m];
  const kanitli = o => !!(o.kanit && o.kanit.length && (o.metin || o.tablo));
  // ders.json "olumsuzVurgu": true → soru kökündeki olumsuz ifadeler kırmızı işaretlenir
  const OLUMSUZ_RE = /(?<!\p{L})(değildir|değinilmemiştir|değinilmez|söz edilmemiştir|bahsedilmemiştir|yer verilmemiştir|çıkarılamaz|ulaşılamaz|söylenemez|yer almaz|bulunmaz|yoktur|olamaz|yanlıştır|gösterilemez|desteklemez|yapmaz|söylenmemiştir|yer almamaktadır)(?!\p{L})/giu;
  const soruMetni = o => { const h = rx(o.soru); return S.ders && S.ders.olumsuzVurgu ? h.replace(OLUMSUZ_RE, '<mark class="olumsuz">$1</mark>') : h; };
  function pasajHTML(o) {
    if (!o.metin && !o.tablo) return "";
    const kl = kanitli(o), dk = kl ? ' role="button" tabindex="0"' : "", ps = paragraflar(o.metin);
    let i = 0;
    const cm = c => `<span class="cumle" data-c="${i++}"${dk}>${rx(cumleMetin(c))}</span>`;
    const govde = ps.map(p => p.some(c => c && c.kim) ? `<div class="diyalog">${p.map(c => `<p>${c.kim ? `<b class="kim">${esc(c.kim)}:</b> ` : ""}${cm(c)}</p>`).join("")}</div>`
      : `<p class="pasaj-p">${p.map(cm).join(" ")}</p>`).join("");
    const t = o.tablo, tablo = t ? `<div class="tablo-wrap"><table class="pasaj-tablo">${t.baslik ? `<caption>${esc(t.baslik)}</caption>` : ""}<thead><tr>${t.basliklar.map(h => `<th>${esc(h)}</th>`).join("")}</tr></thead>
      <tbody>${t.satirlar.map((r, j) => `<tr class="cumle" data-c="t${j}"${dk}>${r.map(x => `<td>${esc(x)}</td>`).join("")}</tr>`).join("")}</tbody></table></div>` : "";
    const oku = [o.metinBaslik, ...ps.flat().map(c => (c && c.kim ? c.kim + ": " : "") + cumleMetin(c))].filter(Boolean).join(" ");
    return `<div class="pasaj${kl ? " kanitli" : ""}">${o.metinBaslik ? `<div class="pasaj-bas">${esc(o.metinBaslik)}</div>` : ""}${govde}${tablo}${o.metin ? `<div class="row">${listenBtn(oku)}</div>` : ""}</div>`;
  }
  function questionHTML(o, idx) {
    const kind = qKind(o);
    if (o.ima && !o.secenekler) o.secenekler = IMA_SEC;
    const kl = kind === "secim" && kanitli(o);
    const body = kind === "nokta" ? `<div class="sd-wrap sd-pick">${sdHTML(o.sayiDogrusu || {}, true)}</div>`
      : kind === "girdi" ? `${o.sayiDogrusu ? `<div class="sd-wrap">${sdHTML(o.sayiDogrusu)}</div>` : ""}${keypadHTML(o)}`
      : `${o.sayiDogrusu ? `<div class="sd-wrap">${sdHTML(o.sayiDogrusu)}</div>` : ""}${kl ? `<div class="kanit-adim" aria-live="polite">${ICON.bak}<span><b>Kanıtı bul:</b> ${o.tablo ? "Metinde ya da tabloda cevabı gösteren yere dokun." : "Metinde cevabı gösteren cümleye dokun."}</span></div>` : ""}<div class="opts"${kl ? " hidden" : ""}>${o.secenekler.map((s, j) => `<button class="opt" data-o="${j}">${"abcd"[j]}) ${fx(esc(String(s).replace(EN_RE, "$1")))}</button>`).join("")}</div>`;
    return `<div class="q q-${kind}">${pasajHTML(o)}
      <p class="q-text">${idx ? `<span class="qn">${idx}.</span>` : ""}<span>${soruMetni(o)}</span></p>
      <div class="yardim-satir"><button class="yardim-btn" type="button" data-yardim hidden>${ICON.ampul}İpucu</button></div><div class="yardim" hidden></div>
      ${o.dinle ? `<div class="q-listen"><button class="say-en big" data-say-en="${esc(o.dinle)}" ${tts.en ? "" : "hidden"}>${ICON.ses}<span>Dinle</span></button><button class="say-en slow" data-say-en="${esc(o.dinle)}" data-slow ${tts.en ? "" : "hidden"}>${ICON.yavas}<span>Yavaş</span></button></div>` : ""}
      ${body}
      <div class="fb" hidden></div></div>`;
  }
  // ---------- İpucu (soru cevaplanmadan önce isteğe bağlı yardım) ----------
  // Sırayla açılır: 1) Hatırla: bağlı kavramın kısa anlatımı (o.yardim.hatirla ya da opts.kavram),
  // 2) çözüme yönlendiren adımlar (o.yardim.adimlar; yoksa o.ipucu). Cevabı söylemez.
  // İpucu kullanılırsa doğru cevap "ipucuyla doğru" (2) sayılır. İlk yanlışta açılmamış sıradaki adım kendiliğinden açılır.
  function wireYardim(el, o, opts, state) {
    const btn = $("[data-yardim]", el), box = $(".yardim", el);
    const none = { used: false, yanlis: () => false, bitti() {} };
    if (!btn || !box) return none;
    const kv = opts.kavram, y = o.yardim || {};
    const hat = y.hatirla ? { metin: y.hatirla } : kv && (kv.aciklama || kv.akilda) ? { ad: kv.ad, metin: kv.aciklama || "", akilda: kv.akilda, svg: kv.svg } : null;
    const adim = y.adimlar && y.adimlar.length ? y.adimlar : o.ipucu ? [o.ipucu] : [];
    const parca = [...(hat ? [{ t: "hat", ...hat }] : []), ...adim.map((m, i) => ({ t: "adim", m, i, n: adim.length }))];
    if (!parca.length) return none;
    state.yardim = state.yardim || 0;
    const ciz = () => {
      box.hidden = !state.yardim;
      box.innerHTML = `<div class="y-kicker">${ICON.ampul}İpucu</div>` + parca.slice(0, state.yardim).map(p => p.t === "hat"
        ? `<div class="y-hat">${p.svg || ""}<div><b>Hatırla${p.ad ? ": " + (isEn() ? `<span lang="en">${esc(p.ad)}</span>` : esc(p.ad)) : ""}</b>${p.metin ? `<p>${rx(p.metin)}</p>` : ""}${p.akilda ? `<span class="key"><b>Akılda kalsın</b>${rx(p.akilda)}</span>` : ""}</div></div>`
        : `<div class="y-adim">${p.n > 1 ? `<span class="y-no">${p.i + 1}</span>` : ""}<p>${rx(p.m)}</p></div>`).join("")
        + (state.yardim ? `<div class="row">${listenBtn(parca.slice(0, state.yardim).map(p => p.t === "hat" ? `${p.ad || ""}. ${p.metin} ${p.akilda || ""}` : p.m).join(". "))}</div>` : "");
      btn.hidden = !!state.bitti || state.yardim >= parca.length;
      btn.innerHTML = `${ICON.ampul}${state.yardim ? "Bir ipucu daha" : "İpucu"}`;
    };
    btn.onclick = () => { state.yardim++; ciz(); box.scrollIntoView({ block: "nearest", behavior: "smooth" }); };
    ciz();
    return {
      get used() { return state.yardim > 0; },
      // "yeni": panelde yeni bir adım açıldı; "hepsi": ipuçlarının hepsi zaten açık; false: ipucu hiç kullanılmadı
      yanlis() { if (!state.yardim) return false; if (state.yardim < parca.length) { state.yardim++; ciz(); return "yeni"; } return "hepsi"; },
      bitti() { state.bitti = true; btn.hidden = true; }
    };
  }
  const yanlisMetin = (o, yr) => yr === "yeni" ? "İpucuna yeni bir adım ekledim. Ona bak ve tekrar dene."
    : yr === "hepsi" ? "İpucunu bir kez daha, adım adım oku. Sonra tekrar dene." : rx(o.ipucu || "Bilgiyi bir kez daha düşün.");

  function wireQuestion(el, o, opts = {}) {
    const kind = qKind(o);
    izle(el, o, opts);
    if (kind !== "secim") return wireMathQuestion(el, o, opts, kind);
    let tries = 0, finished = false, picked = null;
    const state = opts.state || { wrong: [], result: undefined };
    // Veli ayarı "sikBekle": şıklar, soru okunacak kadar (en çok 5 sn) bekledikten sonra açılır (Kanıtı bul sorularında gerekmez).
    if (ayar().sikBekle && !kanitli(o) && state.result === undefined && !state.wrong.length && !opts.classMode) {
      const ob = $(".opts", el), ms = Math.min(5000, Math.max(1200, okumaEsik(kelimeSay(o.soru)) * 1000));
      ob.classList.add("bekle"); $$(".opt", ob).forEach(b => b.disabled = true);
      setTimeout(() => { ob.classList.remove("bekle"); $$(".opt", ob).forEach(b => { if (!b.classList.contains("wrong") && !finished) b.disabled = false; }); }, ms);
    }
    const fb = $(".fb", el), yr = wireYardim(el, o, opts, state);
    // Kanıt adımı: önce kanıt cümlesi, sonra şıklar. state.kanit: 1 ilk denemede, 2 ikinci denemede, 0 gösterildi.
    const kl = kanitli(o) && $(".pasaj.kanitli", el), kb = $(".kanit-adim", el);
    if (kl) {
      const dogruK = o.kanit.map(String);
      state.kanitSecilen = state.kanitSecilen || [];
      const kanitBitti = () => {
        dogruK.forEach(c => { const x = $(`.cumle[data-c="${c}"]`, el); if (x) x.classList.add("kanit-ok"); });
        kl.classList.remove("kanitli"); kl.classList.add("kanit-tamam");
        kb.classList.add("tamam");
        kb.innerHTML = `${ICON.bak}<span><b>${state.kanit === 0 ? "Kanıt cümlesi bu." : state.kanit === 1 ? "Kanıtı buldun!" : "Kanıtı buldun, pes etmedin!"}</b> Şimdi şıkları ele: metinde yazan, metinden çıkarılabilen, metinde olmayan.</span>`;
        $(".opts", el).hidden = false; fb.hidden = true;
      };
      const sec = c => {
        if (state.kanit !== undefined || finished) return;
        const x = $(`.cumle[data-c="${c}"]`, el); if (!x || x.classList.contains("kanit-yanlis")) return;
        if (dogruK.includes(c)) { state.kanit = state.kanitSecilen.length ? 2 : 1; return kanitBitti(); }
        x.classList.add("kanit-yanlis"); state.kanitSecilen.push(c);
        if (state.kanitSecilen.length >= 2) { state.kanit = 0; return kanitBitti(); }
        const y = yr.yanlis();
        fb.hidden = false; fb.className = "fb hint";
        fb.innerHTML = `<div><b>Bu cümle cevabı göstermiyor.</b> ${y === "yeni" ? "İpucuna yeni bir adım ekledim. Ona bak ve tekrar dene." : rx(o.kanitIpucu || "Soru kökündeki anahtar kelimeyi metinde ara. O kelimenin geçtiği cümleyi oku.")}</div>`;
      };
      kl.addEventListener("click", e => { if (e.target.closest("[data-say-en], .listen")) return; const c = e.target.closest(".cumle"); if (c) sec(c.dataset.c); });
      kl.addEventListener("keydown", e => { if (e.key !== "Enter" && e.key !== " ") return; const c = e.target.closest(".cumle"); if (c) { e.preventDefault(); sec(c.dataset.c); } });
      state.kanitSecilen.forEach(c => { const x = $(`.cumle[data-c="${c}"]`, el); if (x) x.classList.add("kanit-yanlis"); });
      if (state.kanit !== undefined) kanitBitti();
    }
    const finish = (result, silent) => {
      if (kl && state.kanit === 0 && result === 1) result = 2;   // kanıt gösterildiyse "ilk denemede" sayılmaz
      finished = true; state.result = result; yr.bitti();
      $$(".opt", el).forEach((b, j) => { b.disabled = true; if (j === o.dogru) b.classList.add("right"); });
      fb.hidden = false;
      if (result === 0) {
        fb.className = "fb show";
        fb.innerHTML = `<div><b>${pick(PRAISE.shown)}</b></div><div>${rx(o.aciklama)}</div>`;
      } else {
        fb.className = "fb ok";
        fb.innerHTML = `<div><b>${result === 1 ? pick(PRAISE.first) : tries === 0 ? "Doğru! İpucunu iyi kullandın." : pick(PRAISE.second)}</b></div><div>${rx(o.aciklama)}</div>`;
      }
      if (!silent) opts.onDone && opts.onDone(result);
    };
    const answer = j => {
      if (finished) return;
      if (j === o.dogru) return finish(tries === 0 && !yr.used ? 1 : 2);
      tries++; if (!state.wrong.includes(j)) state.wrong.push(j);
      const b = $$(".opt", el)[j]; b.classList.add("wrong"); b.disabled = true;
      if (tries >= 2) return finish(0);
      fb.hidden = false; fb.className = "fb hint";
      fb.innerHTML = `<div><b>Henüz değil.</b> ${yanlisMetin(o, yr.yanlis())}</div>` +
        (opts.backToInfo ? `<div><button class="btn ghost" data-back>Bilgi kartına bak</button></div>` : "");
      const bk = $("[data-back]", fb); if (bk) bk.onclick = opts.backToInfo;
    };
    $(".opts", el).addEventListener("click", e => {
      const b = e.target.closest(".opt"); if (!b || b.disabled || finished) return;
      const j = +b.dataset.o;
      if (opts.classMode) {           // sınıf modu: önce seç, sonra "Cevabı göster"
        $$(".opt", el).forEach(x => x.classList.remove("picked")); b.classList.add("picked"); picked = j;
        let rv = $(".reveal", el);
        if (!rv) { rv = document.createElement("div"); rv.className = "row reveal"; rv.innerHTML = `<button class="btn primary">Cevabı göster</button>`; el.appendChild(rv);
          $("button", rv).onclick = () => { rv.remove(); $$(".opt", el).forEach(x => x.classList.remove("picked"));
            if (picked === o.dogru) finish(yr.used ? 2 : 1); else { $$(".opt", el)[picked].classList.add("wrong"); finish(0); } }; }
        return;
      }
      answer(j);
    });
    // önceki denemeleri geri yükle (bilgi kartına dönüp gelince soru sıfırlanmasın)
    if (state.result !== undefined) { state.wrong.forEach(j => $$(".opt", el)[j].classList.add("wrong")); finish(state.result, true); }
    else if (state.wrong.length) { const w = state.wrong.slice(); state.wrong = []; w.forEach(j => answer(j)); }
    return { get finished() { return finished; } };
  }

  // ---------- Öğren (adım adım) ----------
  function buildSteps(d) {
    const steps = d.hazirlik && d.hazirlik.maddeler && d.hazirlik.maddeler.length ? [{ t: "hazir" }, { t: "giris" }] : [{ t: "giris" }];
    d.kavramlar.forEach((k, i) => {
      steps.push({ t: "bilgi", k: i });
      if (k.cozum) steps.push({ t: "cozum", k: i, f: "cozum" });
      if (k.sende) steps.push({ t: "cozum", k: i, f: "sende" });
      if (k.soru) steps.push({ t: "soru", k: i });
      if ((i + 1) % 3 === 0 && i < d.kavramlar.length - 1) steps.push({ t: "hatirla", from: i - 2, to: i });
    });
    const n = d.kavramlar.length;
    if (n) { const from = n % 3 === 0 ? n - 3 : n - (n % 3); steps.push({ t: "hatirla", from, to: n - 1 }); }
    steps.push({ t: "ozet" });
    if (isEn()) steps.push({ t: "duvar" });
    if (d.dusunVeYaz && d.dusunVeYaz.length) steps.push({ t: "yaz" });
    steps.push({ t: "bitis" });
    return steps;
  }

  function renderOgren(root) {
    const d = S.data, steps = buildSteps(d);
    const posKey = key("adim:" + S.konu);
    let pos = Math.min(store.get(posKey, 0), steps.length - 1);
    const qstate = {};
    let adimT0 = simdi(), hizliGecis = 0;
    // Adımdan çıkarken süreyi kaydet; bilgi kartı okunacak kadar açık kalmadan geçildiyse "hizli-gecis" bayrağı.
    const adimBirak = yeni => {
      const st = steps[pos], sn = (simdi() - adimT0) / 1000; adimT0 = simdi();
      if (yeni === pos || !st) return;
      const k = st.k !== undefined ? d.kavramlar[st.k] : null, bayrak = [];
      if (st.t === "bilgi" && yeni > pos && sn < Math.max(3, okumaEsik(kelimeSay([k.aciklama, k.ek || "", k.akilda])))) bayrak.push("hizli-gecis");
      KAYIT.olay("adim", { adim: pos + 1, toplam: steps.length, adimTur: st.t, kavram: k ? k.ad : "", sureSn: +sn.toFixed(1), bayrak });
      if (bayrak.length) { if (++hizliGecis >= 2) { hizliGecis = 0; KOC.goster("hizli-gecis", "Kartları çok hızlı geçiyorsun. Her kartta önce açıklamayı oku, sonra “Akılda kalsın” kısmını kendine sesli söyle."); } }
      else if (st.t === "bilgi") hizliGecis = 0;
    };

    root.innerHTML = `<div class="stepper"><div class="progress"><span id="pgTxt"></span><div class="bar"><i id="pgBar"></i></div></div><div id="stage"></div></div>`;
    const go = p => { tts.stop(); p = Math.max(0, Math.min(steps.length - 1, p)); adimBirak(p); pos = p; store.set(posKey, pos); draw(); $("#stage").scrollIntoView({ block: "nearest", behavior: "smooth" }); };

    function nav(nextLabel, nextEnabled = true, extra = "") {
      return `<div class="stage-nav"><button class="btn ghost" data-prev ${pos === 0 ? "disabled" : ""}>Geri</button>${extra}
        <button class="btn primary" data-next ${nextEnabled ? "" : "disabled"}>${nextLabel}</button></div>`;
    }
    function draw() {
      const st = steps[pos], stage = $("#stage");
      $("#pgTxt").textContent = `Adım ${pos + 1} / ${steps.length}`;
      $("#pgBar").style.width = ((pos + 1) / steps.length * 100) + "%";
      let html = "";
      if (st.t === "hazir") {
        html = `<div class="stage hz"><div id="hzBox" class="stage-body"></div>${nav("Konuya başla")}</div>`;
      } else if (st.t === "cozum") {
        const k = d.kavramlar[st.k], c = k[st.f], sende = st.f === "sende";
        const doldu = qstate[pos] && qstate[pos].bitti;
        html = `<div class="stage"><div class="kicker">${sende ? "Sıra sende" : "Birlikte çözelim"} · ${esc(k.ad)}</div>
          <h3>${rx(c.baslik || (sende ? "Şimdi sen dene" : "Adım adım bakalım"))}</h3>
          ${sende ? `<p class="ek">Boş adımları sen dolduracaksın. Takılırsan bir önceki örneğe bakabilirsin.</p>` : ""}
          <div id="cozBox"></div>${nav("Devam", !!doldu)}</div>`;
      } else if (st.t === "giris") {
        html = `<div class="stage"><div class="kicker">Bu konuda neler var?</div><h3>${esc(d.baslik)}</h3>
          <p class="big">${rx(d.giris)}</p>
          <div class="chips">${d.kavramlar.map(k => `<span class="chip"${isEn() ? ` lang="en" role="button" tabindex="0" data-say-en="${esc(k.ad)}"` : ""}>${k.svg}${esc(k.ad)}</span>`).join("")}</div>
          <div class="row">${listenBtn(d.baslik + ". " + d.giris)}</div>
          ${nav("Başlayalım")}</div>`;
      } else if (st.t === "bilgi") {
        const k = d.kavramlar[st.k];
        html = `<div class="stage"><div class="info-grid">${k.svg}<div class="stage-body">
          <div class="kicker">Kavram ${st.k + 1} / ${d.kavramlar.length}</div>
          <h3 style="color:${esc(k.renk || "inherit")}"${isEn() ? ' lang="en"' : ""}>${adHTML(k, true)}</h3>
          <p class="big">${rx(k.aciklama)}</p>${formulHTML(k.formul)}${k.ek ? `<p class="ek">${rx(k.ek)}</p>` : ""}${ornekHTML(k)}
          <div class="row"><span class="key"><b>Akılda kalsın</b>${rx(k.akilda)}</span>${listenBtn(kSay(k))}</div>
          </div></div>${k.sayiDogrusu ? `<div class="sd-wrap">${sdHTML(k.sayiDogrusu)}</div>` : ""}${nav(k.cozum ? "Bir örnekle bakalım" : k.soru ? "Anladım, soru gelsin" : "Devam")}</div>`;
      } else if (st.t === "soru") {
        const k = d.kavramlar[st.k];
        html = `<div class="stage"><div class="kicker">Soru · ${esc(k.ad)}</div><div id="qbox">${questionHTML(k.soru)}</div>${nav("Devam", !!(qstate[pos] && qstate[pos].result !== undefined))}</div>`;
      } else if (st.t === "hatirla") {
        const ks = d.kavramlar.slice(st.from, st.to + 1);
        html = `<div class="stage"><div class="kicker">Hatırlayalım</div><h3>Aklında kaldı mı?</h3>
          <p class="big">Her karta dokun. Önce kendin hatırlamaya çalış, sonra cevabı gör.</p>
          <div class="recall">${ks.map(k => `<button data-reveal>${k.svg}<span>${esc(k.ad)} → <span class="ans" hidden>${esc(plain(k.akilda))}</span><span class="q-mark">?</span></span></button>`).join("")}</div>
          ${nav("Devam")}</div>`;
      } else if (st.t === "ozet") {
        html = `<div class="stage"><div class="kicker">Özet</div><h3>Akılda Kalsın</h3>
          <ul class="remember">${d.akildaKalsin.map(a => `<li>${rx(a)}</li>`).join("")}</ul>
          <div class="row">${listenBtn(d.akildaKalsin.join(". "))}</div>${nav("Devam")}</div>`;
      } else if (st.t === "duvar") {
        html = `<div class="stage"><div class="kicker">Kelime Duvarı</div><h3>Bu konunun kelimeleri</h3>
          <p class="big">Her kutuya dokun: kart döner, kelimeyi duyarsın. Biliyorsan ✓, zorlanıyorsan ↻ işaretle. 🎤 ile kendi sesini kaydedip karşılaştırabilirsin.</p>
          <div id="wallBox"></div>${nav("Devam")}</div>`;
      } else if (st.t === "yaz") {
        const y = d.dusunVeYaz[0];
        html = `<div class="stage"><div class="kicker">Düşün ve Yaz · isteğe bağlı</div><h3>${rx(y.soru)}</h3>
          <p class="ek">Not verilmez. Kendi cümlelerinle yaz, sonra örnek cevapla karşılaştır.</p>
          <textarea id="yazText" placeholder="Cevabını buraya yaz…"></textarea>
          <div class="row"><button class="btn" id="yazCheck">Örnek cevabı göster</button></div>
          <div id="yazOut" hidden></div>${nav("Devam", true)}</div>`;
      } else if (st.t === "bitis") {
        if (!store.get(key("ogren-bitti:" + S.konu), false)) { store.set(key("ogren-bitti:" + S.konu), true); KAYIT.olay("ogren-bitti", { toplam: steps.length }); KOC.ozet(); }
        const r = results.all(), vals = d.kavramlar.filter(k => k.soru).map(k => r[k.ad]);
        const c1 = vals.filter(v => v === 1).length, c2 = vals.filter(v => v === 2).length, c0 = vals.filter(v => v === 0).length;
        const msg = c0 === 0 && c2 === 0 ? "Harika bir dikkatle çalıştın!" : c0 === 0 ? "İpuçlarını kullanarak hepsini buldun. Bu, iyi çalışmanın işareti." : "Her yanlış, yeni bir şey öğrenmek demek. Tekrar bölümünde bunlar öne çıkacak.";
        html = `<div class="stage"><div class="kicker">Konu tamam</div><h3>Konuyu bitirdin!</h3><p class="big">${msg}</p>
          <div class="done-stats"><div class="stat"><b>${c1}</b><span>ilk denemede doğru</span></div>
          <div class="stat"><b>${c2}</b><span>ipucuyla doğru</span></div><div class="stat"><b>${c0}</b><span>birlikte öğrendik</span></div></div>
          <div class="row"><button class="btn primary" data-goto="tekrar">Tekrar'a geç</button><button class="btn" data-goto="test">Test'e geç</button>
          <button class="btn ghost" data-restart>Baştan başla</button></div></div>`;
      }
      stage.innerHTML = html;

      const prev = $("[data-prev]", stage), next = $("[data-next]", stage);
      if (prev) prev.onclick = () => go(pos - 1);
      if (next) next.onclick = () => go(pos + 1);
      if (st.t === "soru") {
        const k = d.kavramlar[st.k];
        qstate[pos] = qstate[pos] || { wrong: [], result: undefined };
        wireQuestion($("#qbox .q", stage), k.soru, {
          state: qstate[pos], kavram: k,
          onDone: res => { results.set(k.ad, res); $("[data-next]", stage).disabled = false; },
          backToInfo: () => go(pos - 1)
        });
      }
      $$("[data-reveal]", stage).forEach(b => b.onclick = () => { $(".ans", b).hidden = false; $(".q-mark", b).hidden = true; });
      if (st.t === "hazir") renderHazirlik($("#hzBox", stage), d.hazirlik, () => go(pos + 1));
      if (st.t === "cozum") {
        qstate[pos] = qstate[pos] || {};
        runCozum($("#cozBox", stage), d.kavramlar[st.k][st.f], qstate[pos], () => { const n = $("[data-next]", stage); if (n) n.disabled = false; }, d.kavramlar[st.k]);
      }
      if (st.t === "yaz") wireWrite(stage, d.dusunVeYaz[0]);
      if (st.t === "duvar") renderWall($("#wallBox", stage), wordsOf(d), { baslik: `${d.unite} — ${d.baslik}`, kartlar: kartlarOf(S.konu) });
      $$("[data-goto]", stage).forEach(b => b.onclick = () => setTab(b.dataset.goto));
      const rs = $("[data-restart]", stage); if (rs) rs.onclick = () => { for (const k in qstate) delete qstate[k]; go(0); };
    }
    draw();
  }

  function wireWrite(scope, y) {
    $("#yazCheck", scope).onclick = () => {
      const txt = lower($("#yazText", scope).value);
      const out = $("#yazOut", scope); out.hidden = false;
      out.innerHTML = `<div class="model"><b>Örnek cevap:</b> ${rx(y.ornekCevap)}</div>
        <p class="ek" style="margin:8px 0 6px">Bu anahtar kelimeleri kullandın mı? Yeşil olanları yazmışsın.</p>
        <div class="kw">${y.anahtarlar.map(a => `<span class="${txt.includes(lower(a)) ? "hit" : ""}">${esc(a)}</span>`).join("")}</div>`;
    };
  }

  // ---------- Konuya Bak ----------
  function renderBak(root) {
    const d = S.data, icon = {}; d.kavramlar.forEach(k => icon[k.ad] = k.svg);
    const h = [];
    h.push(`<section><p class="lead">${rx(d.giris)}</p></section>`);
    if (d.hazirlik && d.hazirlik.maddeler) h.push(`<section><div class="sec-title"><h3>Önce Hatırla</h3><span>Bu konu için gereken eski bilgiler</span></div><div class="merak hz-bak">` +
      d.hazirlik.maddeler.map(m => `<details><summary>${esc(m.ad)}${m.sinif ? ` <small>· ${esc(m.sinif)}</small>` : ""}</summary><p>${rx(m.anlatim)}</p>${m.sayiDogrusu ? `<div class="sd-wrap">${sdHTML(m.sayiDogrusu)}</div>` : ""}${m.ornek ? cozumStatik(m.ornek) : ""}</details>`).join("") + `</div></section>`);
    h.push(`<section><div class="sec-title"><h3>Kavramlar</h3><span>${d.kavramlar.length} kavram</span></div><div class="cards${d.kavramlar.some(k => k.sayiDogrusu || k.cozum) ? " genis" : ""}">` +
      d.kavramlar.map(k => `<article class="card" data-ad="${esc(k.ad)}">${k.svg}<div><h4 style="color:${esc(k.renk || "inherit")}"${isEn() ? ' lang="en"' : ""}>${adHTML(k)}</h4>
        <p>${rx(k.aciklama)}</p>${formulHTML(k.formul)}${k.ek ? `<p class="ek">${rx(k.ek)}</p>` : ""}${ornekHTML(k)}<span class="key"><b>Akılda kalsın</b>${rx(k.akilda)}</span>
        ${k.sayiDogrusu ? `<div class="sd-wrap">${sdHTML(k.sayiDogrusu)}</div>` : ""}${k.cozum ? `<details class="coz-ac"><summary>Örnek çözümü gör</summary>${cozumStatik(k.cozum)}</details>` : ""}</div></article>`).join("") + `</div></section>`);
    if (d.gruplar && d.gruplar.length) h.push(`<section><div class="sec-title"><h3>Gruplar</h3></div><div class="groups">` +
      d.gruplar.map(g => `<div class="group"><h4>${esc(g.soru)}</h4><div class="boxes">` + g.kutular.map(b => `<div class="box"><div class="lbl">${esc(b.etiket)}</div><div class="chips">` +
        b.uyeler.map(m => `<span class="chip">${icon[m] || ""}${esc(m)}</span>`).join("") + `</div></div>`).join("") + `</div></div>`).join("") + `</div></section>`);
    if (d.biliyorMusun && d.biliyorMusun.length) h.push(`<section class="facts"><div class="eyebrow">Biliyor musun?</div>${d.biliyorMusun.map(f => `<p>${rx(f)}</p>`).join("")}</section>`);
    if (isEn()) h.push(`<section><div class="sec-title"><h3>Kelime Duvarı</h3><span>Kutuya dokun, kart dönsün</span></div><div id="bakWall"></div></section>`);
    h.push(`<section><div class="sec-title"><h3>Akılda Kalsın</h3></div><ul class="remember">${d.akildaKalsin.map(a => `<li>${rx(a)}</li>`).join("")}</ul></section>`);
    if (d.merakKutusu && d.merakKutusu.length) h.push(`<section><div class="sec-title"><h3>Merak Kutusu</h3><span>Soruya dokun, cevabı aç</span></div><div class="merak">` +
      d.merakKutusu.map(m => `<details><summary>${rx(m.soru)}</summary><p>${rx(m.cevap)}</p></details>`).join("") + `</div></section>`);
    h.push(`<p class="src">Kaynak: ${esc(S.ders.kaynak || `MEB ${S.ders.ders} ${S.ders.sinif} Ders Kitabı`)}, ${esc(d.sayfalar)}.<br>Hazırlayan: Kemal BEYDİLLİ - Eylül 2026</p>`);
    root.innerHTML = h.join("");
    if (isEn()) renderWall($("#bakWall", root), wordsOf(d), { baslik: `${d.unite} — ${d.baslik}`, kartlar: kartlarOf(S.konu) });
    // Ara Durak'tan "Konuda bak" ile gelindiyse ilgili kavram kartını göster ve vurgula
    if (S.hedef) {
      const c = $$(".card", root).find(x => x.dataset.ad === S.hedef); S.hedef = null;
      if (c) { c.classList.add("vurgu"); setTimeout(() => c.scrollIntoView({ block: "center", behavior: "smooth" }), 200); setTimeout(() => c.classList.remove("vurgu"), 3500); }
    }
  }

  // ---------- Tekrar ----------
  function renderTekrar(root) {
    const d = S.data;
    const games = [["kart", "Hafıza Kartları"], ["eslestir", "Eşleştir"]];
    if (d.gruplar && d.gruplar.length) games.push(["grupla", "Gruplayalım"]);
    if (isEn() && d.kelimeOyunlari !== false) games.push(["dinle", "Dinle ve Bul"], ["kur", "Kelimeyi Kur"]); // dilbilgisi konularında kapatılır
    if (d.cumleler && d.cumleler.length) games.push(["cumle", "Cümle Kur"]);
    if (d.resimEslestir) games.push(["resim", "Resim Eşleştir"]);
    if (d.hatalar && d.hatalar.length) games.push(["hata", "Hatayı Bul"]);
    let g = store.get(key("oyun"), "kart"); if (!games.some(x => x[0] === g)) g = "kart";
    root.innerHTML = `<div class="subtabs">${games.map(([k, n]) => `<button class="subtab" data-g="${k}" aria-pressed="${k === g}">${n}</button>`).join("")}</div><div id="game"></div>`;
    $$(".subtab", root).forEach(b => b.onclick = () => { g = b.dataset.g; store.set(key("oyun"), g); $$(".subtab", root).forEach(x => x.setAttribute("aria-pressed", x === b)); run(); });
    const run = () => { const box = $("#game", root); KAYIT.olay("oyun-ac", { oyun: g }); ({ kart: gameCards, eslestir: gameMatch, grupla: gameGroup, dinle: gameListen, kur: gameSpell, cumle: gameSentence, resim: gamePicture, hata: gameErrors })[g](box); };
    run();
  }

  function gameCards(box) {
    const d = S.data; let order = results.weakFirst(d.kavramlar), pos = 0;
    box.innerHTML = `<div class="flash"><p class="ek" style="margin:0">Zorlandığın kavramlar önce gelir.</p>
      <button class="fcard" id="fcard" aria-label="Kartı çevir"><div class="inner"><div class="face front" id="ffront"></div><div class="face back" id="fback"></div></div></button>
      <div class="row" style="justify-content:center">${isEn() ? `<button class="btn" id="fsay" ${tts.en ? "" : "hidden"}>${ICON.ses}Dinle</button>` : ""}<button class="btn" id="fprev">Önceki</button><span class="count" id="fcount"></span><button class="btn" id="fnext">Sonraki</button><button class="btn ghost" id="fmix">Karıştır</button></div></div>`;
    const card = $("#fcard", box);
    const show = () => {
      const k = order[pos]; card.classList.remove("flipped");
      $("#ffront", box).innerHTML = `${k.svg}<div class="fname"${isEn() ? ' lang="en"' : ""}>${esc(k.ad)}</div>${results.isWeak(k.ad) ? '<div class="weak">Tekrar et</div>' : ""}<div class="hintline">Önce hatırla, sonra dokun</div>`;
      $("#fback", box).innerHTML = `<div class="bigk">${esc(plain(k.akilda))}</div><p>${esc(plain(k.aciklama))}</p>${k.ornek ? `<p class="ornek-en" lang="en">${esc(plain(k.ornek))}</p>` : ""}`;
      $("#fcount", box).textContent = `${pos + 1} / ${order.length}`;
      const fs = $("#fsay", box); if (fs) fs.dataset.sayEn = k.ad;
    };
    card.onclick = () => card.classList.toggle("flipped");
    $("#fprev", box).onclick = () => { pos = (pos - 1 + order.length) % order.length; show(); };
    $("#fnext", box).onclick = () => { pos = (pos + 1) % order.length; show(); };
    $("#fmix", box).onclick = () => { order = shuffle(d.kavramlar); pos = 0; show(); };
    show();
  }

  function gameMatch(box) {
    const d = S.data, ks = d.kavramlar;
    const left = shuffle(ks.map((k, i) => i)), right = shuffle(ks.map((k, i) => i));
    let sel = null, done = 0, yanlis = 0; const t0 = simdi();
    box.innerHTML = `<p class="ek" style="margin:0 0 10px">Soldan bir kavram seç, sonra sağdan ona uyan "akılda kalsın" ifadesine dokun.</p>
      <div class="match"><div class="col">${left.map(i => `<button class="mitem" data-l="${i}">${ks[i].svg}${esc(ks[i].ad)}</button>`).join("")}</div>
      <div class="col">${right.map(i => `<button class="mitem" data-r="${i}">${esc(plain(ks[i].akilda))}</button>`).join("")}</div></div>
      <p class="game-msg" id="mmsg"></p>`;
    box.onclick = e => {
      const l = e.target.closest("[data-l]"), r = e.target.closest("[data-r]");
      if (l && !l.classList.contains("done")) { $$("[data-l]", box).forEach(x => x.classList.remove("sel")); l.classList.add("sel"); sel = +l.dataset.l; }
      if (r && !r.classList.contains("done")) {
        if (sel === null) { $("#mmsg", box).textContent = "Önce soldan bir kavram seç."; return; }
        if (+r.dataset.r === sel) {
          r.classList.add("done"); const lb = $(`[data-l="${sel}"]`, box); lb.classList.remove("sel"); lb.classList.add("done"); sel = null; done++;
          $("#mmsg", box).textContent = done === ks.length ? "Hepsini eşleştirdin! Harika dikkat." : "Doğru eşleşme!";
          if (done === ks.length) { KAYIT.olay("oyun", { oyun: "eslestir", oge: ks.length, yanlis, sureSn: Math.round((simdi() - t0) / 1000) }); const b = document.createElement("button"); b.className = "btn"; b.textContent = "Yeniden oyna"; b.onclick = () => gameMatch(box); box.appendChild(b); }
        } else { yanlis++; oyunHata(box, "eslestir"); r.classList.add("shake"); setTimeout(() => r.classList.remove("shake"), 400); $("#mmsg", box).textContent = "Bu ikisi eşleşmiyor. Bilgiyi hatırla ve tekrar dene."; }
      }
    };
  }

  function gameGroup(box) {
    const d = S.data, icon = {}; d.kavramlar.forEach(k => icon[k.ad] = k.svg);
    let gi = 0;
    const play = () => {
      const g = d.gruplar[gi], items = shuffle(g.kutular.flatMap((b, bi) => b.uyeler.map(m => ({ m, bi }))));
      let sel = null, placed = 0, yanlis = 0; const t0 = simdi();
      box.innerHTML = `<p class="ek" style="margin:0 0 10px">Soru ${gi + 1} / ${d.gruplar.length}. Bir karta dokun, sonra doğru kutuya dokun.</p>
        <div class="group"><h4>${esc(g.soru)}</h4><div class="pool chips" id="pool">${items.map((it, i) => `<span class="chip pick" role="button" tabindex="0" data-i="${i}">${icon[it.m] || ""}${esc(it.m)}</span>`).join("")}</div>
        <div class="boxes" style="margin-top:12px">${g.kutular.map((b, bi) => `<div class="box" data-b="${bi}" role="button" tabindex="0"><div class="lbl">${esc(b.etiket)}</div><div class="chips"></div></div>`).join("")}</div></div>
        <p class="game-msg" id="gmsg"></p><div class="row" id="gnext"></div>`;
      const selChip = c => { $$(".chip.pick", box).forEach(x => x.classList.remove("sel")); if (c) { c.classList.add("sel"); sel = +c.dataset.i; $$(".box", box).forEach(b => b.classList.add("target")); } };
      box.onclick = e => {
        const c = e.target.closest(".chip.pick"); if (c && c.parentElement.id === "pool") { selChip(c); return; }
        const b = e.target.closest(".box");
        if (b && sel !== null) {
          const it = items[sel], chip = $(`[data-i="${sel}"]`, box);
          if (+b.dataset.b === it.bi) {
            chip.classList.remove("sel", "pick"); chip.classList.add("okc"); $(".chips", b).appendChild(chip); placed++;
            $("#gmsg", box).textContent = placed === items.length ? "Hepsi doğru kutuda!" : "Doğru!";
            if (placed === items.length) {
              KAYIT.olay("oyun", { oyun: "grupla", oge: items.length, yanlis, sureSn: Math.round((simdi() - t0) / 1000) });
              $("#gnext", box).innerHTML = gi < d.gruplar.length - 1 ? `<button class="btn primary">Sonraki gruplama</button>` : `<button class="btn">Baştan oyna</button>`;
              $("#gnext button", box).onclick = () => { gi = gi < d.gruplar.length - 1 ? gi + 1 : 0; play(); };
            }
          } else { yanlis++; oyunHata(box, "grupla"); chip.classList.add("shake"); setTimeout(() => chip.classList.remove("shake"), 400); $("#gmsg", box).textContent = "Bu kutu değil. Kavramın özelliğini hatırla."; }
          sel = null; selChip(null); $$(".box", box).forEach(x => x.classList.remove("target"));
        }
      };
    };
    play();
  }

  // ---------- İngilizce oyunları ----------
  // Dinle ve Bul: kelime okunur, 3 karttan doğrusu seçilir. Kısa tur: 6 kelime.
  function gameListen(box) {
    const d = S.data, ks = d.kavramlar, tur = shuffle(ks).slice(0, Math.min(6, ks.length));
    let i = 0, ilk = 0, tries = 0;
    if (!tts.en) { box.innerHTML = `<p class="game-msg">Bu cihazda İngilizce ses bulunamadı. Oyunu oynamak için siteyi Chrome ya da Edge ile aç.</p>`; return; }
    const draw = () => {
      if (i >= tur.length) {
        box.innerHTML = `<div class="game-end"><div class="stars">${"★".repeat(ilk)}${"☆".repeat(tur.length - ilk)}</div>
          <p class="game-msg">${KAYIT.olay("oyun", { oyun: "dinle", oge: tur.length, dogru: ilk }) && ""}${tur.length} kelimenin ${ilk} tanesini ilk dinleyişte buldun. Kulağın alışıyor!</p>
          <button class="btn primary" id="lagain">Yeni tur</button></div>`;
        $("#lagain", box).onclick = () => gameListen(box); return;
      }
      const k = tur[i], opts = shuffle([k, ...shuffle(ks.filter(x => x !== k)).slice(0, 2)]); tries = 0;
      box.innerHTML = `<p class="ek" style="margin:0 0 10px">Kelime ${i + 1} / ${tur.length}. Dinle, sonra duyduğun kelimeye dokun.</p>
        <div class="listen-play"><button class="say-en big" data-say-en="${esc(k.ad)}">${ICON.ses}<span>Dinle</span></button>
        <button class="say-en slow" data-say-en="${esc(k.ad)}" data-slow>${ICON.yavas}<span>Yavaş</span></button></div>
        <div class="listen-opts">${opts.map(o => `<button class="mitem lopt" data-a="${esc(o.ad)}">${o.svg}<span lang="en">${esc(o.ad)}</span></button>`).join("")}</div>
        <p class="game-msg" id="lmsg"></p>`;
      tts.sayEn(k.ad);
      box.onclick = e => {
        const b = e.target.closest(".lopt"); if (!b || b.disabled) return;
        if (b.dataset.a === k.ad) {
          b.classList.add("done"); if (tries === 0) ilk++;
          $("#lmsg", box).innerHTML = `${tries === 0 ? "Doğru! Dikkatle dinledin." : "Doğru! Tekrar dinlemen işe yaradı."} <b lang="en">${esc(k.ad)}</b> = ${esc(plain(k.akilda))}`;
          $$(".lopt", box).forEach(x => x.disabled = true); setTimeout(() => { i++; draw(); }, 1400);
        } else {
          tries++; oyunHata(box, "dinle"); b.classList.add("shake"); b.disabled = true; setTimeout(() => b.classList.remove("shake"), 400);
          $("#lmsg", box).textContent = tries >= 2 ? "Doğru kelime yeşil oldu. Bir kez daha dinle." : "Bu değil. Bir kez daha dinle, istersen yavaş dinle.";
          if (tries >= 2) { const r = $(`.lopt[data-a="${CSS.escape(k.ad)}"]`, box); r.classList.add("done"); tts.sayEn(k.ad, true); $$(".lopt", box).forEach(x => x.disabled = true); setTimeout(() => { i++; draw(); }, 2200); }
          else tts.sayEn(k.ad);
        }
      };
    };
    draw();
  }

  // Kelimeyi Kur: resim + Türkçe anlam verilir, karışık harflerden İngilizce kelime sırayla kurulur.
  function gameSpell(box) {
    const d = S.data, tur = shuffle(d.kavramlar.filter(k => k.ad.replace(/[^a-z]/gi, "").length <= 12)).slice(0, 5);
    let i = 0, temiz = 0;
    const draw = () => {
      if (i >= tur.length) {
        box.innerHTML = `<div class="game-end"><div class="stars">${"★".repeat(temiz)}${"☆".repeat(tur.length - temiz)}</div>
          <p class="game-msg">${tur.length} kelimeyi kurdun, ${temiz} tanesinde hiç hata yapmadın. Harika dikkat!</p>
          <button class="btn primary" id="sagain">Yeni tur</button></div>`;
        $("#sagain", box).onclick = () => gameSpell(box); return;
      }
      const k = tur[i], harf = [...k.ad], hedef = harf.filter(c => /\S/.test(c));
      let pos = 0, hata = 0, tiles = shuffle(hedef.map((c, j) => ({ c, j })));
      if (tiles.every((t, j) => t.j === j) && tiles.length > 1) tiles.reverse();
      box.innerHTML = `<p class="ek" style="margin:0 0 10px">Kelime ${i + 1} / ${tur.length}. Harflere sırayla dokun.</p>
        <div class="spell-q">${k.svg}<div><div class="bigk">${esc(plain(k.akilda))}</div>${enBtns(k.ad)}</div></div>
        <div class="slots" lang="en">${harf.map(c => /\S/.test(c) ? `<span class="slot"></span>` : `<span class="gap"></span>`).join("")}</div>
        <div class="tiles" lang="en">${tiles.map((t, n) => `<button class="tile" data-n="${n}">${esc(t.c)}</button>`).join("")}</div>
        <p class="game-msg" id="smsg"></p>`;
      const slots = $$(".slot", box);
      box.onclick = e => {
        const b = e.target.closest(".tile"); if (!b || b.disabled) return;
        const t = tiles[+b.dataset.n];
        if (t.c.toLowerCase() === hedef[pos].toLowerCase()) {
          slots[pos].textContent = hedef[pos]; slots[pos].classList.add("on"); b.disabled = true; b.classList.add("used"); pos++;
          if (pos === hedef.length) {
            if (!hata) temiz++;
            $("#smsg", box).textContent = hata ? "Kelimeyi kurdun! Pes etmedin." : "Hatasız kurdun! Çok dikkatliydin.";
            tts.sayEn(k.ad); setTimeout(() => { i++; draw(); }, 1600);
          } else $("#smsg", box).textContent = "";
        } else {
          hata++; b.classList.add("shake"); setTimeout(() => b.classList.remove("shake"), 400);
          $("#smsg", box).textContent = hata >= 3 ? `Sıradaki harf: "${hedef[pos]}"` : "Bu harf sırada değil. Kelimeyi dinleyip tekrar dene.";
        }
      };
    };
    draw();
  }

  // =================================================================
  // ---------- İngilizce pekiştirme modülü (yalnızca ders.json "dil": "en") ----------
  // Kelime Duvarı, Kelime Defterim, yazdırılabilir afiş, Günün Tekrarı (aralıklı tekrar),
  // Cümle Kur, Resim Eşleştir, Oku ve Dinle, kendi sesini kaydet.
  // =================================================================

  // Konunun kelimeleri: kavram kartları + "kelimeler" listesindeki ek kelimeler.
  function wordsOf(d) {
    const out = [], seen = new Set();
    const add = w => { const k = lower(w.en); if (!seen.has(k)) { seen.add(k); out.push(w); } };
    d.kavramlar.forEach(k => add({ en: k.ad, tr: plain(k.akilda), svg: k.svg, ornek: k.ornek ? plain(k.ornek) : "", ornekTr: k.ornekTr || "", konu: d.id, ana: true }));
    (d.kelimeler || []).forEach(w => add({ en: w.en, tr: w.tr, svg: w.svg || "", ornek: w.ornek || "", ornekTr: w.ornekTr || "", konu: d.id, ana: false }));
    return out;
  }
  // Resmi olmayan kelime için harf rozeti
  const RENK = ["#3cc47c", "#4ea8de", "#ff5a8a", "#ffb03a", "#9b7bff", "#ff7a33", "#2bb3a3"];
  const wordPic = w => w.svg || `<svg viewBox='0 0 120 120' xmlns='http://www.w3.org/2000/svg' role='img'><rect width='120' height='120' rx='22' fill='#1b2340'/><text x='60' y='80' text-anchor='middle' font-family='Baloo 2, sans-serif' font-weight='800' font-size='58' fill='${RENK[w.en.length % RENK.length]}'>${esc(w.en[0].toUpperCase())}${esc((w.en[1] || "").toLowerCase())}</text></svg>`;

  // ---------- Aralıklı tekrar (Leitner kutuları) ----------
  // Her kelime: k = kutu (0–5), n = bir sonraki tekrar günü (YYYY-MM-DD), z = zorlandı mı
  const ARALIK = [1, 1, 3, 7, 14, 30];
  const gun = (ek = 0) => { const t = new Date(); t.setDate(t.getDate() + ek); return `${t.getFullYear()}-${String(t.getMonth() + 1).padStart(2, "0")}-${String(t.getDate()).padStart(2, "0")}`; };
  const srs = {
    all() { return store.get(key("srs"), {}); },
    save(s) { store.set(key("srs"), s); },
    add(words) { const s = srs.all(); let ch = false; words.forEach(w => { if (!s[w.en]) { s[w.en] = { k: 0, n: gun(1) }; ch = true; } }); if (ch) srs.save(s); },
    get(en) { return srs.all()[en] || null; },
    grade(en, ok) {
      const s = srs.all(), e = s[en] || { k: 0, n: gun() };
      if (ok) { e.k = Math.min(e.k + 1, 5); e.n = gun(ARALIK[e.k]); e.z = false; } else { e.k = 0; e.n = gun(1); e.z = true; }
      s[en] = e; srs.save(s);
    },
    biliyorum(en) { const s = srs.all(), e = s[en] || { k: 0 }; e.k = Math.max(e.k, 2); e.n = gun(ARALIK[e.k]); e.z = false; s[en] = e; srs.save(s); },
    tekrarEt(en) { const s = srs.all(), e = s[en] || { k: 0 }; e.k = 0; e.n = gun(); e.z = true; s[en] = e; srs.save(s); },
    due() { const s = srs.all(), t = gun(); return Object.keys(s).filter(en => s[en].n <= t).sort((a, b) => s[a].n < s[b].n ? -1 : 1); }
  };

  // Hazır bütün konuları yükle (Defter ve Günün Tekrarı için)
  async function loadAll() {
    const ready = allTopics().filter(k => k.hazir && !isDurak(k));
    await Promise.all(ready.map(async t => {
      if (S.cache[t.id]) return;
      try { const r = await fetch("konular/" + t.id + ".json", { cache: "no-cache" }); if (r.ok) S.cache[t.id] = await r.json(); } catch (e) {}
    }));
    const map = new Map();
    ready.forEach(t => { const d = S.cache[t.id]; if (d) wordsOf(d).forEach(w => { if (!map.has(w.en)) map.set(w.en, { ...w, konuAd: d.baslik }); }); });
    return map;
  }

  // ---------- Kendi sesini kaydet ve karşılaştır ----------
  // Kayıt yalnızca bu cihazda tutulur; hiçbir yere gönderilmez.
  const recBtn = text => ("MediaRecorder" in window && navigator.mediaDevices) ? `<button class="say-en rec" data-rec="${esc(text)}" aria-label="Kendi sesini kaydet">${ICON.mik}</button>` : "";
  const rec = {
    panel: null, url: null, busy: false,
    show(text, html) {
      if (!rec.panel) { rec.panel = document.createElement("div"); rec.panel.className = "rec-panel"; document.body.appendChild(rec.panel); }
      rec.panel.innerHTML = `<div class="rec-word" lang="en">${esc(text)}</div><div class="rec-body">${html}</div><button class="rec-x" aria-label="Kapat">×</button>`;
      rec.panel.hidden = false;
      $(".rec-x", rec.panel).onclick = () => { rec.panel.hidden = true; tts.stop(); };
    },
    async start(text) {
      if (rec.busy) return; rec.busy = true; tts.stop();
      let stream;
      try { stream = await navigator.mediaDevices.getUserMedia({ audio: true }); }
      catch (e) { rec.busy = false; rec.show(text, `<p>Mikrofon açılamadı. Tarayıcı izin isterse <b>İzin ver</b>'e dokun, sonra tekrar dene.</p>`); return; }
      const parts = [], mr = new MediaRecorder(stream), sure = Math.min(6, 2 + Math.ceil(text.split(/\s+/).length * .5));
      mr.ondataavailable = e => e.data.size && parts.push(e.data);
      let kalan = sure;
      rec.show(text, `<p class="rec-live"><span class="dot"></span>Şimdi söyle… <b id="recSay">${kalan}</b></p>`);
      const tick = setInterval(() => { kalan--; const el = $("#recSay"); if (el) el.textContent = Math.max(kalan, 0); }, 1000);
      mr.onstop = () => {
        clearInterval(tick); stream.getTracks().forEach(t => t.stop()); rec.busy = false;
        if (rec.url) URL.revokeObjectURL(rec.url);
        rec.url = URL.createObjectURL(new Blob(parts, { type: mr.mimeType || "audio/webm" }));
        rec.show(text, `<p>Önce kendi sesini, sonra doğrusunu dinle. Benziyor mu?</p>
          <div class="row"><button class="btn" id="recMe">${ICON.ses}Benim sesim</button><button class="btn" id="recOk">${ICON.ses}Doğrusu</button><button class="btn ghost" id="recAgain">${ICON.mik}Tekrar söyle</button></div>`);
        const me = new Audio(rec.url);
        $("#recMe").onclick = () => { tts.stop(); me.currentTime = 0; me.play(); };
        $("#recOk").onclick = () => { me.pause(); tts.sayEn(text); };
        $("#recAgain").onclick = () => { me.pause(); rec.start(text); };
        me.onended = () => { if (!rec.panel.hidden && !me.dataset.done) { me.dataset.done = 1; setTimeout(() => tts.sayEn(text), 300); } };
        me.play().catch(() => {});
      };
      mr.start(); setTimeout(() => mr.state !== "inactive" && mr.stop(), sure * 1000);
    }
  };
  document.addEventListener("click", e => { const b = e.target.closest("[data-rec]"); if (b) { e.stopPropagation(); rec.start(b.dataset.rec); } }, true);

  // ---------- Kelime Duvarı (konu sonu) / Kelime Defterim (bütün ders) ----------
  // Kutuya dokun: kart döner, anlamı, örnek cümlesi, dinleme ve kayıt düğmeleri görünür.
  function renderWall(box, words, opts = {}) {
    const durum = en => { const e = srs.get(en); return !e ? "" : e.z ? "z" : e.k >= 2 ? "b" : ""; };
    let filtre = opts.filtre || "hepsi";
    const draw = () => {
      const list = words.filter(w => filtre === "hepsi" || (filtre === "zor" ? durum(w.en) === "z" : durum(w.en) !== "b"));
      const nB = words.filter(w => durum(w.en) === "b").length, nZ = words.filter(w => durum(w.en) === "z").length;
      box.innerHTML = `<div class="wall-bar"><span class="wall-say"><b>${words.length}</b> kelime · <b class="okc">${nB}</b> biliyorum · <b class="zc">${nZ}</b> tekrar edilecek</span>
          <div class="wall-filters">${[["hepsi", "Hepsi"], ["ogren", "Öğreneceklerim"], ["zor", "Zorlandıklarım"]].map(([k, n]) => `<button class="subtab" data-f="${k}" aria-pressed="${k === filtre}">${n}</button>`).join("")}</div>
          <button class="btn ghost" data-print>${ICON.yazdir}Afişi yazdır</button>${opts.kartlar ? kartlarBtn(opts.kartlar) : ""}</div>
        ${list.length ? `<div class="wall">${list.map(w => `<div class="wtile ${durum(w.en)}" data-w="${esc(w.en)}">
          <button class="wface" aria-label="${esc(w.en)} kartını çevir">${wordPic(w)}<span class="wen" lang="en">${esc(w.en)}</span>${opts.konuAdi && w.konuAd ? `<span class="wkonu">${esc(w.konuAd)}</span>` : ""}</button>
          <div class="wback"><div class="wtr">${esc(w.tr)}</div>
            ${w.ornek ? `<div class="wex" lang="en">${esc(w.ornek)}</div>` : ""}
            <div class="wbtns">${enBtns(w.en)}${recBtn(w.en)}</div>
            <div class="wmark"><button class="mk ok" data-bil>✓ Biliyorum</button><button class="mk z" data-tek>↻ Tekrar et</button></div></div></div>`).join("")}</div>`
        : `<p class="game-msg">${filtre === "zor" ? "Zorlandığın kelime yok. Harika!" : "Bu listede kelime kalmadı. Hepsini biliyorsun!"}</p>`}`;
    };
    box.onclick = e => {
      const f = e.target.closest("[data-f]"); if (f) { filtre = f.dataset.f; draw(); return; }
      if (e.target.closest("[data-print]")) { printPoster(opts.baslik || "Kelime Afişi", words); return; }
      const t = e.target.closest(".wtile"); if (!t) return;
      const en = t.dataset.w;
      if (e.target.closest("[data-bil]")) { srs.biliyorum(en); draw(); return; }
      if (e.target.closest("[data-tek]")) { srs.tekrarEt(en); draw(); return; }
      if (e.target.closest(".wface")) { const open = t.classList.toggle("open"); if (open) tts.sayEn(en); }
    };
    draw();
  }

  // ---------- Ünite kelime kartları (PDF) ----------
  // ders.json'da ünitenin "kartlar" alanı (ör. "kartlar/unite1.pdf"): kesip katlanan kelime kartları, önceden üretilmiş PDF.
  function kartlarOf(id) { const t = allTopics().find(k => k.id === id); return t ? S.ders.uniteler[t.ui].kartlar || "" : ""; }
  const kartlarBtn = url => `<a class="btn ghost" href="${esc(url)}" target="_blank" rel="noopener">${ICON.yazdir}Kelime kartları (PDF)</a>`;

  // ---------- Yazdırılabilir afiş (A4; tarayıcıda "PDF olarak kaydet" ile PDF olur) ----------
  function printPoster(baslik, words) {
    let area = $("#printArea"); if (!area) { area = document.createElement("div"); area.id = "printArea"; document.body.appendChild(area); }
    area.innerHTML = `<h1>${esc(baslik)}</h1><p class="psub">${esc(S.ders.ders)} · ${esc(S.ders.sinif)} — Ela'nın Ders Defteri</p>
      <div class="pgrid">${words.map(w => `<div class="pcell">${wordPic(w)}<div><b lang="en">${esc(w.en)}</b><span>${esc(w.tr)}</span>${w.ornek ? `<i lang="en">${esc(w.ornek)}</i>` : ""}</div></div>`).join("")}</div>`;
    document.body.classList.add("printing");
    const bitti = () => { document.body.classList.remove("printing"); removeEventListener("afterprint", bitti); };
    addEventListener("afterprint", bitti);
    setTimeout(() => window.print(), 50);
  }

  async function openDefter() {
    tts.stop(); S.data = null; S.konu = null; renderNav();
    $("#content").innerHTML = `<div class="notice">Kelimeler yükleniyor…</div>`;
    const map = await loadAll(), words = [...map.values()];
    srs.add(words.filter(w => store.get(key("acildi:" + w.konu), false)));
    $("#content").innerHTML = `<section class="konu-head"><div class="meta"><span>${esc(S.ders.ders)}</span><span class="pill">${words.length} kelime</span></div>
      <h2>Kelime Defterim</h2><p class="ek">Bütün konulardaki kelimeler burada. Kutuya dokun: kart döner, kelimeyi dinlersin. Biliyorsan ✓, zorlanıyorsan ↻ işaretle; ↻ işaretlediklerin Günün Tekrarı'nda öne gelir.</p></section>
      <div class="panel" id="wallPanel"></div>`;
    renderWall($("#wallPanel"), words, { baslik: `${S.ders.ders} — Kelime Defterim`, konuAdi: true });
  }

  // ---------- Günün Tekrarı ----------
  // Bugün sırası gelen kelimeler (en çok 8). Soru türleri sırayla değişir: dinle-bul, Türkçe→İngilizce, İngilizce→Türkçe.
  async function openGunluk(ekstra) {
    tts.stop(); S.data = null; S.konu = null; renderNav();
    const c = $("#content"); c.innerHTML = `<div class="notice">Kelimeler yükleniyor…</div>`;
    const map = await loadAll();
    srs.add([...map.values()].filter(w => store.get(key("acildi:" + w.konu), false)));
    let list = srs.due().filter(en => map.has(en)).slice(0, 8);
    if (ekstra) list = shuffle([...map.keys()].filter(en => srs.get(en))).slice(0, 5);
    const head = `<section class="konu-head"><div class="meta"><span>${esc(S.ders.ders)}</span><span class="pill">${gun().split("-").reverse().join(".")}</span></div><h2>Günün Tekrarı</h2></section>`;
    if (!list.length) {
      const hepsi = Object.keys(srs.all()).length;
      c.innerHTML = head + `<div class="stage"><h3>${hepsi ? "Bugünlük tekrar yok!" : "Henüz kelimen yok"}</h3>
        <p class="big">${hepsi ? "Bugün sırası gelen kelime kalmadı. Kelimeler 1, 3, 7 ve 14 gün arayla geri gelir; böyle tekrar etmek akılda kalmasını sağlar." : "Bir konu açıp öğrendiğinde kelimeleri ertesi gün burada tekrar edeceksin."}</p>
        ${hepsi ? `<div class="row"><button class="btn primary" id="gEkstra">Yine de 5 kelime çalış</button></div>` : ""}</div>`;
      const b = $("#gEkstra"); if (b) b.onclick = () => openGunluk(true);
      return;
    }
    const all = [...map.values()];
    let i = 0, ilk = 0;
    const draw = () => {
      if (i >= list.length) {
        const yarin = Object.values(srs.all()).filter(e => e.n <= gun(1)).length, kalan = srs.due().filter(en => map.has(en)).length;
        c.innerHTML = head + `<div class="stage game-end"><div class="stars">${"★".repeat(ilk)}${"☆".repeat(list.length - ilk)}</div>
          <h3>Bugünkü tekrar bitti!</h3><p class="big">${list.length} kelimenin ${ilk} tanesini ilk denemede bildin. Her gün biraz tekrar, kelimeleri kalıcı yapar.</p>
          <p class="ek">${kalan ? `Bugün ${kalan} kelime daha var. İstersen mola verip sonra devam et.` : `Yarın ${yarin} kelime seni bekliyor.`}</p>
          <div class="row" style="justify-content:center">${kalan ? `<button class="btn primary" data-tur>Bir tur daha</button>` : ""}<a class="btn" href="defter" data-defter>Kelime Defterim</a></div></div>`;
        const tb = $("[data-tur]", c); if (tb) tb.onclick = () => openGunluk();
        $("[data-defter]", c).onclick = e => { e.preventDefault(); location.hash = "defter"; };
        return;
      }
      const w = map.get(list[i]), tip = (!tts.en && i % 3 === 0) ? 1 : i % 3;
      const yan = shuffle(all.filter(x => x.en !== w.en)).slice(0, 2), sec = shuffle([w, ...yan]);
      const soru = tip === 0 ? `<p class="big">Dinle ve doğru kelimeyi seç.</p><div class="listen-play"><button class="say-en big" data-say-en="${esc(w.en)}">${ICON.ses}<span>Dinle</span></button><button class="say-en slow" data-say-en="${esc(w.en)}" data-slow>${ICON.yavas}<span>Yavaş</span></button></div>`
        : tip === 1 ? `<div class="spell-q">${wordPic(w)}<div><p class="ek" style="margin:0">Bunun İngilizcesi hangisi?</p><div class="bigk">${esc(w.tr)}</div></div></div>`
        : `<div class="spell-q">${wordPic(w)}<div><p class="ek" style="margin:0">Bu kelime ne demek?</p><div class="bigk" lang="en">${esc(w.en)}</div>${enBtns(w.en)}</div></div>`;
      const yazi = x => tip === 2 ? esc(x.tr) : `<span lang="en">${esc(x.en)}</span>`;
      c.innerHTML = head + `<div class="stage"><div class="progress"><span>Kelime ${i + 1} / ${list.length}</span><div class="bar"><i style="width:${(i + 1) / list.length * 100}%"></i></div></div>
        ${soru}<div class="listen-opts">${sec.map(x => `<button class="mitem gopt" data-a="${esc(x.en)}">${yazi(x)}</button>`).join("")}</div><p class="game-msg" id="gmsg"></p></div>`;
      if (tip === 0) tts.sayEn(w.en);
      let deneme = 0;
      c.onclick = e => {
        const b = e.target.closest(".gopt"); if (!b || b.disabled) return;
        if (b.dataset.a === w.en) {
          b.classList.add("done"); $$(".gopt", c).forEach(x => x.disabled = true);
          if (deneme === 0) ilk++; srs.grade(w.en, deneme === 0);
          $("#gmsg", c).innerHTML = `${deneme === 0 ? "Doğru! İyi hatırladın." : "Doğru! İkinci denemede buldun."} <b lang="en">${esc(w.en)}</b> = ${esc(w.tr)}`;
          tts.sayEn(w.en); setTimeout(() => { i++; draw(); }, 1500);
        } else {
          deneme++; oyunHata(c, "gunluk"); b.disabled = true; b.classList.add("shake"); setTimeout(() => b.classList.remove("shake"), 400);
          if (deneme >= 2) {
            srs.grade(w.en, false); $$(".gopt", c).forEach(x => { x.disabled = true; if (x.dataset.a === w.en) x.classList.add("done"); });
            $("#gmsg", c).innerHTML = `Doğrusu: <b lang="en">${esc(w.en)}</b> = ${esc(w.tr)}. Bu kelime yarın yine gelecek.`;
            tts.sayEn(w.en, true); setTimeout(() => { i++; draw(); }, 2400);
          } else $("#gmsg", c).textContent = tip === 0 ? "Bu değil. Bir daha dinle." : "Bu değil. Resme bakıp tekrar düşün.";
        }
      };
    };
    draw();
  }

  // ---------- Cümle Kur: kelimelere dokunarak (ya da sürükleyerek) cümle kurma ----------
  function gameSentence(box) {
    const tur = shuffle(S.data.cumleler).slice(0, 5);
    let i = 0, temiz = 0;
    const draw = () => {
      if (i >= tur.length) {
        box.innerHTML = `<div class="game-end"><div class="stars">${"★".repeat(temiz)}${"☆".repeat(tur.length - temiz)}</div>
          <p class="game-msg">${tur.length} cümle kurdun, ${temiz} tanesini ilk denemede doğru kurdun. Pes etmedin!</p><button class="btn primary" id="cagain">Yeni tur</button></div>`;
        $("#cagain", box).onclick = () => gameSentence(box); return;
      }
      const c = tur[i], hedef = c.en.split(/\s+/);
      let pool = shuffle(hedef.map((t, j) => ({ t, j })));
      if (pool.length > 1 && pool.every((p, j) => p.t === hedef[j])) pool.reverse();
      const placed = [], kilit = []; let hata = 0;
      box.innerHTML = `<p class="ek" style="margin:0 0 10px">Cümle ${i + 1} / ${tur.length}. Kelimelere sırayla dokun ya da sürükle. Yanlış yere koyduğuna dokunursan geri gelir.</p>
        <div class="cumle-tr">${rx(c.tr)}</div>
        <div class="cumle-hat" id="hat" lang="en"></div>
        <div class="cumle-havuz" id="havuz" lang="en"></div>
        <div class="row"><button class="btn" id="cDinle" hidden>${ICON.ses}İpucu: dinle</button></div>
        <p class="game-msg" id="cmsg"></p>`;
      const hat = $("#hat", box), havuz = $("#havuz", box);
      const ciz = () => {
        hat.innerHTML = placed.length ? placed.map((p, n) => `<button class="tok${kilit[n] ? " ok" : ""}" data-h="${n}" draggable="${!kilit[n]}">${esc(p.t)}</button>`).join("") : `<span class="hat-bos">Cümle burada oluşacak</span>`;
        havuz.innerHTML = pool.map((p, n) => `<button class="tok" data-p="${n}" draggable="true">${esc(p.t)}</button>`).join("");
      };
      const kontrol = () => {
        if (pool.length) return;
        const dogru = placed.every((p, n) => p.t === hedef[n]);
        if (dogru) {
          placed.forEach((p, n) => kilit[n] = true); ciz();
          if (!hata) temiz++;
          $("#cmsg", box).textContent = hata ? "Doğru! Denemeye devam ettin ve buldun." : "Harika! İlk denemede doğru kurdun.";
          tts.sayEn(c.en); setTimeout(() => { i++; draw(); }, 2200); return;
        }
        hata++;
        placed.forEach((p, n) => { kilit[n] = p.t === hedef[n] && placed.slice(0, n).every((q, m) => q.t === hedef[m]); });
        ciz(); $$(".tok:not(.ok)", hat).forEach(t => t.classList.add("bad"));
        $("#cmsg", box).textContent = hata >= 3 ? "Doğru cümle aşağıda. Dinle ve bir sonrakine geç." : "Yeşil kelimeler doğru yerde. Diğerleri havuza dönüyor, tekrar dene.";
        $("#cDinle", box).hidden = false;
        setTimeout(() => {
          if (hata >= 3) {
            placed.length = 0; hedef.forEach(t => placed.push({ t })); hedef.forEach((t, n) => kilit[n] = true); pool = []; ciz();
            tts.sayEn(c.en); const n = document.createElement("button"); n.className = "btn primary"; n.textContent = "Sonraki cümle"; n.onclick = () => { i++; draw(); }; $("#cmsg", box).after(n); return;
          }
          for (let n = placed.length - 1; n >= 0; n--) if (!kilit[n]) pool.push(...placed.splice(n, 1));
          ciz();
        }, 1100);
      };
      const koy = n => { const p = pool.splice(n, 1)[0]; if (p) { placed.push(p); ciz(); kontrol(); } };
      const geri = n => { if (kilit[n]) return; const p = placed.splice(n, 1)[0]; kilit.splice(n, 1); pool.push(p); ciz(); };
      box.onclick = e => {
        const p = e.target.closest("[data-p]"); if (p) return koy(+p.dataset.p);
        const h = e.target.closest("[data-h]"); if (h) return geri(+h.dataset.h);
        if (e.target.closest("#cDinle")) tts.sayEn(c.en);
      };
      // Sürükle-bırak (fare): havuzdan hatta, hattan havuza
      box.ondragstart = e => { const t = e.target.closest(".tok"); if (!t) return; e.dataTransfer.setData("text/plain", t.dataset.p !== undefined ? "p" + t.dataset.p : "h" + t.dataset.h); };
      [hat, havuz].forEach(z => { z.ondragover = e => { e.preventDefault(); z.classList.add("over"); }; z.ondragleave = () => z.classList.remove("over"); });
      hat.ondrop = e => { e.preventDefault(); hat.classList.remove("over"); const v = e.dataTransfer.getData("text/plain"); if (v[0] === "p") koy(+v.slice(1)); };
      havuz.ondrop = e => { e.preventDefault(); havuz.classList.remove("over"); const v = e.dataTransfer.getData("text/plain"); if (v[0] === "h") geri(+v.slice(1)); };
      ciz();
    };
    draw();
  }

  // ---------- Resim Eşleştir (somut kelimeli konular: "resimEslestir": true) ----------
  function gamePicture(box) {
    const ks = shuffle(S.data.kavramlar).slice(0, 6), left = shuffle(ks.map((k, i) => i)), right = shuffle(ks.map((k, i) => i));
    let sel = null, done = 0, ilk = 0, yanlis = new Set();
    box.innerHTML = `<p class="ek" style="margin:0 0 10px">Bir resme dokun, sonra ona uyan İngilizce kelimeye dokun.</p>
      <div class="pmatch"><div class="pics">${left.map(i => `<button class="pic" data-l="${i}" aria-label="Resim ${i + 1}">${ks[i].svg}</button>`).join("")}</div>
      <div class="col">${right.map(i => `<button class="mitem" data-r="${i}" lang="en">${esc(ks[i].ad)}</button>`).join("")}</div></div><p class="game-msg" id="pmsg"></p>`;
    box.onclick = e => {
      const l = e.target.closest("[data-l]"), r = e.target.closest("[data-r]");
      if (l && !l.classList.contains("done")) { $$("[data-l]", box).forEach(x => x.classList.remove("sel")); l.classList.add("sel"); sel = +l.dataset.l; }
      if (r && !r.classList.contains("done")) {
        if (sel === null) { $("#pmsg", box).textContent = "Önce bir resme dokun."; return; }
        if (+r.dataset.r === sel) {
          r.classList.add("done"); const lb = $(`[data-l="${sel}"]`, box); lb.classList.remove("sel"); lb.classList.add("done");
          if (!yanlis.has(sel)) ilk++; tts.sayEn(ks[sel].ad); sel = null; done++;
          $("#pmsg", box).textContent = done === ks.length ? `Hepsini eşleştirdin! ${ilk} tanesini ilk denemede buldun.` : "Doğru!";
          if (done === ks.length) { const b = document.createElement("button"); b.className = "btn"; b.textContent = "Yeniden oyna"; b.onclick = () => gamePicture(box); box.appendChild(b); }
        } else { yanlis.add(sel); oyunHata(box, "resim"); r.classList.add("shake"); setTimeout(() => r.classList.remove("shake"), 400); $("#pmsg", box).textContent = "Bu resim o kelime değil. Tekrar dene."; }
      }
    };
  }

  // ---------- Oku ve Dinle: kitaptaki okuma metni, cümle cümle sesli ve vurgulu ----------
  // Okuma metni: isteğe bağlı "bolumler" (uzun metin parçalara bölünür) ve "sozluk" (zor kelimeye dokununca Türkçesi).
  // Eski biçim (okuma.cumleler + okuma.sorular) tek bölüm olarak çalışır.
  const reEsc = x => x.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  function glossify(text, sozluk) {
    const keys = Object.keys(sozluk || {}).sort((a, b) => b.length - a.length);
    if (!keys.length) return esc(text);
    const map = {}; keys.forEach(k => map[lower(k)] = sozluk[k]);
    const re = new RegExp(`\\b(${keys.map(k => reEsc(esc(k))).join("|")})\\b`, "gi");
    return esc(text).replace(re, m => `<span class="gl" role="button" tabindex="0" data-tr="${esc(map[lower(m)] || "")}">${m}</span>`);
  }
  function renderOkuma(root) {
    const o = S.data.okuma;
    const bolumler = o.bolumler && o.bolumler.length ? o.bolumler : [{ cumleler: o.cumleler, sorular: o.sorular }];
    let bi = Math.min(store.get(key("okuma:" + S.konu), 0), bolumler.length - 1), yavas = false, tr = false, calan = -1, zaman = null;
    const ciz = () => {
      const bl = bolumler[bi], cs = bl.cumleler, qs = bl.sorular || [];
      root.innerHTML = `<div class="stage"><div class="kicker">Oku ve Dinle · ${esc(o.sayfa || "")}</div><h3 lang="en">${esc(o.baslik || "Reading")}</h3>
        ${bolumler.length > 1 ? `<div class="subtabs okuma-bol">${bolumler.map((x, n) => `<button class="subtab" data-b="${n}" aria-pressed="${n === bi}">Bölüm ${n + 1}${x.baslik ? ` · ${esc(x.baslik)}` : ""}</button>`).join("")}</div>` : ""}
        <p class="ek">Bir cümleye dokun, o cümle okunur. "Baştan oku" bu bölümü okur ve okunan cümle renklenir.${o.sozluk ? " Altı noktalı kelimeye dokunursan Türkçesi çıkar." : ""} Önce Türkçesine bakmadan anlamaya çalış.</p>
        <div class="row okuma-ctl"><button class="btn primary" id="oPlay">${ICON.ses}Baştan oku</button><button class="btn" id="oStop">Durdur</button>
          <button class="btn ghost" id="oSlow" aria-pressed="${yavas}">${ICON.yavas}Yavaş</button><button class="btn ghost" id="oTr" aria-pressed="${tr}">Türkçesini göster</button></div>
        <div class="okuma${tr ? " show-tr" : ""}" lang="en">${cs.map((c, n) => `<p class="oc" data-i="${n}"><span class="oen">${glossify(c.en, o.sozluk)}</span><span class="otr" lang="tr">${rx(c.tr)}</span></p>`).join("")}</div>
        ${bi < bolumler.length - 1 ? `<div class="row"><button class="btn" id="oNext">Bölüm ${bi + 2}'ye geç</button></div>` : ""}</div>
        ${qs.length ? `<div class="stage"><div class="kicker">${bolumler.length > 1 ? `Bölüm ${bi + 1}: ` : ""}Metni anladın mı?</div><div class="tests">${qs.map((q, n) => `<div class="card-q" data-q="${n}">${questionHTML(q, n + 1)}</div>`).join("")}</div></div>` : ""}`;
      const isaretle = n => $$(".oc", root).forEach((p, j) => p.classList.toggle("now", j === n));
      const dur = () => { calan = -1; clearTimeout(zaman); tts.stop(); isaretle(-1); };
      const oku = (n, devam) => {
        if (!tts.en || n >= cs.length) { dur(); return; }
        calan = n; isaretle(n); speechSynthesis.cancel();
        const txt = cs[n].en, u = tts.utter(txt, tts.en, yavas ? .6 : .85);
        let gitti = false;
        const sonraki = () => { if (gitti || calan !== n) return; gitti = true; clearTimeout(zaman); if (devam) setTimeout(() => calan === n && oku(n + 1, true), 350); else isaretle(-1); };
        u.onend = sonraki;
        zaman = setTimeout(sonraki, (txt.split(/\s+/).length * 520 + 1200) / (yavas ? .6 : .85)); // bazı seslerde onend gelmeyebilir
      };
      const git = n => { dur(); bi = n; store.set(key("okuma:" + S.konu), n); ciz(); };
      $("#oPlay", root).onclick = () => oku(0, true);
      $("#oStop", root).onclick = dur;
      $("#oSlow", root).onclick = e => { yavas = !yavas; e.currentTarget.setAttribute("aria-pressed", yavas); };
      $("#oTr", root).onclick = e => { tr = !tr; e.currentTarget.setAttribute("aria-pressed", tr); root.querySelector(".okuma").classList.toggle("show-tr", tr); };
      $$(".okuma-bol .subtab", root).forEach(x => x.onclick = () => git(+x.dataset.b));
      const nx = $("#oNext", root); if (nx) nx.onclick = () => { git(bi + 1); root.scrollIntoView({ behavior: "smooth", block: "start" }); };
      $(".okuma", root).onclick = e => {
        const g = e.target.closest(".gl");
        if (g) { const ac = !g.classList.contains("open"); $$(".gl.open", root).forEach(x => x.classList.remove("open")); if (ac) { g.classList.add("open"); tts.sayEn(g.textContent); } return; }
        if (e.target.closest(".en")) return;
        const p = e.target.closest(".oc"); if (p) { p.classList.add("peek"); oku(+p.dataset.i, false); }
      };
      $$(".card-q", root).forEach(el => wireQuestion($(".q", el), qs[+el.dataset.q], {}));
      if (!tts.en) $(".okuma-ctl", root).insertAdjacentHTML("afterend", `<p class="game-msg">Bu cihazda İngilizce ses bulunamadı; metni okuyabilirsin ama dinleyemezsin.</p>`);
    };
    ciz();
  }

  // ---------- Formül şeridi (dilbilgisi kalıbı renkli bloklarla) ----------
  // kavram.formul = [[{t, r, alt?}, …], …] — her iç dizi bir satır. r (rol): ozne, yard, fiil, ek, kelime, sonuc, olumsuz, diger.
  // Bloklar arasında "+", "sonuc" bloğundan önce "=" yazılır.
  function formulHTML(f) {
    if (!f || !f.length) return "";
    return `<div class="formul" aria-label="Kalıp">${f.map(row => `<div class="frow">${row.map((b, n) =>
      `${n ? `<span class="fop">${b.r === "sonuc" ? "=" : "+"}</span>` : ""}<span class="fblok fr-${esc(b.r || "diger")}"><b lang="en">${esc(b.t)}</b>${b.alt ? `<small>${esc(b.alt)}</small>` : ""}</span>`).join("")}</div>`).join("")}</div>`;
  }

  // =================================================================
  // ---------- Matematik modülü (yalnızca konu dosyasında ilgili alan varsa çalışır) ----------
  // sayiDogrusu: sayı doğrusu çizimi · nokta / cevap: sayı doğrusunda seçme ve tuş takımıyla yazma soruları
  // cozum / sende: adım adım çözüm ve boşluklu "sıra sende" örneği · hazirlik: konu başı "Hazır mısın?" kontrolü
  // =================================================================
  const sayiYaz = (v, isaretli) => { const n = Number(v), t = Number.isInteger(n) ? String(Math.abs(n)) : String(Math.abs(n)).replace(".", ","); return n < 0 ? "−" + t : n > 0 && isaretli ? "+" + t : t; };
  // Kesirli yazımı sayıya çevirir: 2,5 · "-13/5" · "9/-3" · "−2 3/5" (tam sayılı kesir; eksi bütüne aittir)
  const kesirSayi = v => {
    if (typeof v === "number") return v;
    const s = String(v).trim().replace(/[−–]/g, "-").replace(",", ".");
    const m = s.match(/^(-?)(?:(\d+)\s+)?(-?\d+)\/(-?\d+)$/);
    if (!m) return s === "" || s === "-" ? NaN : Number(s);
    if (+m[4] === 0) return NaN;
    return (m[1] ? -1 : 1) * ((m[2] ? +m[2] : 0) + (+m[3]) / (+m[4]));
  };
  const ayniSayi = (a, b) => { const x = kesirSayi(a), y = kesirSayi(b); return isFinite(x) && isFinite(y) && Math.abs(x - y) < 1e-6; };
  // Ara çizgideki noktayı tam sayılı kesir olarak yazar: -2.6 (bolme 5) → "−2 3/5"
  const kesirYaz = (v, bol) => { const a = Math.abs(v), t = Math.floor(a + 1e-9), p = Math.round((a - t) * bol);
    return p === 0 || p === bol ? sayiYaz(Math.round(v)) : `${v < 0 ? "−" : ""}${t ? t + " " : ""}${p}/${bol}`; };
  let sdSay = 0;
  // c: {min, max, dikey, bolme, isaretli, sifirEtiketi, isaretler:[{x, etiket, renk}], oklar:[{bas, son, etiket, renk}], gizle:[sayı]}
  // bolme > 1 (yatay): ara çizgiler çizilir; seçme sorusunda ara çizgilere de dokunulur (nokta: -2.6 ya da "-13/5").
  function sdHTML(c, pick) {
    const min = c.min ?? -5, max = c.max ?? 5, n = Math.max(1, max - min), dikey = !!c.dikey, bol = c.bolme || 1;
    const is = c.isaretler || [], ok = c.oklar || [], gizle = new Set(c.gizle || []), id = "sd" + (++sdSay);
    const renk = r => r || "#ff7a33";
    const defs = `<defs>${ok.map((o, i) => `<marker id="${id}m${i}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="${esc(renk(o.renk))}"/></marker>`).join("")}</defs>`;
    const cls = v => v < 0 ? "sd-neg" : v > 0 ? "sd-pos" : "sd-0";
    const tam = []; for (let v = min; v <= max; v++) tam.push(v);
    if (!dikey) {
      const dar = window.innerWidth < 640, U0 = dar ? Math.max(27, Math.min(44, 340 / n)) : Math.max(30, Math.min(58, 640 / n)), pad = dar ? 22 : 26;  // telefonda yazılar küçülmesin
      const U = bol > 1 ? Math.max(U0, Math.min((dar ? 340 : 640) / n, bol * (dar ? 26 : 40))) : U0;  // ara çizgiler parmakla seçilebilecek kadar aralıklı
      const archMax = ok.reduce((m, o) => Math.max(m, Math.min(52, 16 + Math.abs(o.son - o.bas) * U * .22)), 0);
      const Ly = (ok.length ? archMax + 22 : 0) + (is.some(p => p.etiket) ? 30 : 14), W = n * U + pad * 2, H = Ly + (c.sifirEtiketi ? 52 : 36);
      const X = v => pad + (v - min) * U;
      let g = `<line x1="${pad - 16}" y1="${Ly}" x2="${W - pad + 16}" y2="${Ly}" class="sd-line"/><path d="M${pad - 22} ${Ly}l9-5v10z M${W - pad + 22} ${Ly}l-9-5v10z" class="sd-uc"/>`;
      if (bol > 1) for (let v = min; v < max; v++) for (let k = 1; k < bol; k++) g += `<line x1="${X(v + k / bol)}" y1="${Ly - 4}" x2="${X(v + k / bol)}" y2="${Ly + 4}" class="sd-tick"/>`;
      tam.forEach(v => { g += `<line x1="${X(v)}" y1="${Ly - 8}" x2="${X(v)}" y2="${Ly + 8}" class="sd-tick${v === 0 ? " sd-tick0" : ""}"/>`;
        if (!gizle.has(v)) g += `<text x="${X(v)}" y="${Ly + 27}" text-anchor="middle" class="sd-num ${cls(v)}">${sayiYaz(v, c.isaretli)}</text>`; });
      if (c.sifirEtiketi && min <= 0 && max >= 0) g += `<text x="${X(0)}" y="${Ly + 45}" text-anchor="middle" class="sd-lbl">${esc(c.sifirEtiketi)}</text>`;
      ok.forEach((o, i) => { const a = X(o.bas), b = X(o.son), h = Math.min(52, 16 + Math.abs(o.son - o.bas) * U * .22), m = (a + b) / 2;
        g += `<path d="M${a} ${Ly - 9} Q${m} ${Ly - 9 - h * 2} ${b} ${Ly - 9}" fill="none" stroke="${esc(renk(o.renk))}" stroke-width="3" stroke-linecap="round" marker-end="url(#${id}m${i})"/>`;
        if (o.etiket) g += `<text x="${m}" y="${Ly - 13 - h}" text-anchor="middle" class="sd-ok" fill="${esc(renk(o.renk))}">${esc(o.etiket)}</text>`; });
      is.forEach(p => { g += `<circle cx="${X(p.x)}" cy="${Ly}" r="7.5" fill="${esc(renk(p.renk))}" class="sd-pt"/>`;
        if (p.etiket) g += `<text x="${X(p.x)}" y="${Ly - 15}" text-anchor="middle" class="sd-ptl" fill="${esc(renk(p.renk))}">${esc(p.etiket)}</text>`; });
      if (pick) tam.forEach(v => { for (let k = 0; k < bol && (k === 0 || v < max); k++) {
        const x = +(v + k / bol).toFixed(6), w = U / bol;
        g += `<g class="sd-hit" data-x="${x}" role="button" tabindex="0" aria-label="${k ? kesirYaz(x, bol) : sayiYaz(v)}"><rect x="${X(x) - w / 2}" y="0" width="${w}" height="${H}" fill="transparent"/><circle cx="${X(x)}" cy="${Ly}" r="${k ? 8 : 12}" class="sd-ring"/></g>`; } });
      return `<svg class="sd" viewBox="0 0 ${W} ${H}" style="max-width:${Math.round(W * 1.15)}px" role="img" aria-label="Sayı doğrusu">${defs}${g}</svg>`;
    }
    // Dikey sayı doğrusu: pozitifler yukarıda (deniz seviyesi, termometre, asansör)
    const U = c.birim || 30, pad = 18, Lx = 58, uzun = Math.max(0, ...is.map(p => String(p.etiket || "").length), String(c.sifirEtiketi || "").length), W = Math.max(200, Lx + 30 + uzun * 9.5 + (ok.length ? 70 : 0)), H = n * U + pad * 2;
    const Y = v => pad + (max - v) * U;
    let g = `<line x1="${Lx}" y1="${pad - 12}" x2="${Lx}" y2="${H - pad + 12}" class="sd-line"/><path d="M${Lx} ${pad - 18}l-5 9h10z M${Lx} ${H - pad + 18}l-5-9h10z" class="sd-uc"/>`;
    if (c.sifirEtiketi && min <= 0 && max >= 0) g += `<line x1="${Lx}" y1="${Y(0)}" x2="${W - 4}" y2="${Y(0)}" class="sd-sifir"/><text x="${W - 6}" y="${Y(0) - 6}" class="sd-lbl" text-anchor="end">${esc(c.sifirEtiketi)}</text>`;
    tam.forEach(v => { g += `<line x1="${Lx - 8}" y1="${Y(v)}" x2="${Lx + 8}" y2="${Y(v)}" class="sd-tick${v === 0 ? " sd-tick0" : ""}"/>`;
      if (!gizle.has(v)) g += `<text x="${Lx - 14}" y="${Y(v) + 6}" class="sd-num ${cls(v)}" text-anchor="end">${sayiYaz(v, c.isaretli)}</text>`; });
    ok.forEach((o, i) => { const a = Y(o.bas), b = Y(o.son), h = Math.min(46, 14 + Math.abs(o.son - o.bas) * U * .2), m = (a + b) / 2;
      g += `<path d="M${Lx + 10} ${a} Q${Lx + 10 + h * 2} ${m} ${Lx + 10} ${b}" fill="none" stroke="${esc(renk(o.renk))}" stroke-width="3" stroke-linecap="round" marker-end="url(#${id}m${i})"/>`;
      if (o.etiket) g += `<text x="${Lx + 18 + h}" y="${m + 5}" class="sd-ok" text-anchor="start" fill="${esc(renk(o.renk))}">${esc(o.etiket)}</text>`; });
    is.forEach(p => { g += `<circle cx="${Lx}" cy="${Y(p.x)}" r="7.5" fill="${esc(renk(p.renk))}" class="sd-pt"/>`;
      if (p.etiket) g += `<text x="${Lx + 16}" y="${Y(p.x) + 6}" class="sd-ptl" text-anchor="start" fill="${esc(renk(p.renk))}">${esc(p.etiket)}</text>`; });
    if (pick) tam.forEach(v => { g += `<g class="sd-hit" data-x="${v}" role="button" tabindex="0" aria-label="${sayiYaz(v)}"><rect x="0" y="${Y(v) - U / 2}" width="${W}" height="${U}" fill="transparent"/><circle cx="${Lx}" cy="${Y(v)}" r="11" class="sd-ring"/></g>`; });
    return `<svg class="sd sd-dikey" viewBox="0 0 ${W} ${H}" style="max-width:${W}px" role="img" aria-label="Dikey sayı doğrusu">${defs}${g}</svg>`;
  }

  // Tuş takımı: tablette klavye açılmadan, büyük tuşlarla sayı yazma (eksi işareti ve virgül dahil)
  function keypadHTML(o) {
    const t = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "−", "0", o.kesir ? "/" : ","];  // kesir: true → virgül yerine kesir çizgisi
    return `<div class="kp"><div class="kp-ekran" tabindex="0" role="textbox" aria-label="Cevabın">${o.onEk ? `<span class="kp-ek">${esc(o.onEk)}</span>` : ""}<span class="kp-txt"></span><span class="kp-imlec"></span>${o.birim ? `<span class="kp-ek">${esc(o.birim)}</span>` : ""}</div>
      <div class="kp-tus">${t.map(k => `<button class="kp-k${k === "−" ? " kp-eksi" : ""}" data-k="${k}">${k}</button>`).join("")}
      <button class="kp-k kp-sil" data-k="sil" aria-label="Sil">⌫</button><button class="btn primary kp-ok" data-k="ok">Kontrol et</button></div></div>`;
  }
  const normSayi = s => String(s).replace(/\s/g, "").replace(/[−–]/g, "-").replace(/\./g, ",").replace(/^\+/, "").replace(/^-0$/, "0");

  function wireMathQuestion(el, o, opts, kind) {
    let tries = 0, finished = false, buf = "";
    const state = opts.state || { wrong: [], result: undefined };
    const fb = $(".fb", el), txt = $(".kp-txt", el), ekran = $(".kp-ekran", el), yr = wireYardim(el, o, opts, state);
    // denk: true → değeri aynı olan her yazım kabul (2/4 = 1/2); yoksa yalnızca cevap ve kabul listesi
    const dogruMu = v => kind === "nokta" ? ayniSayi(v, o.nokta) : [o.cevap, ...(o.kabul || [])].some(c => normSayi(c) === normSayi(v) || (o.denk && ayniSayi(c, v)));
    const dogruYazi = kind === "nokta" ? (typeof o.nokta === "string" ? o.nokta.replace(/-/g, "−") : sayiYaz(o.nokta)) : String(o.cevap).replace(/-/g, "−");
    const ciz = () => { if (txt) txt.textContent = buf.replace(/^-/, "−"); };
    const finish = (result, silent) => {
      finished = true; state.result = result; yr.bitti();
      if (kind === "nokta") { $$(".sd-hit", el).forEach(g => { g.classList.add("kapali"); if (ayniSayi(g.dataset.x, o.nokta)) g.classList.add("on"); }); }
      else { buf = String(o.cevap); ciz(); ekran.classList.add(result === 0 ? "goster" : "dogru"); $$(".kp-k, .kp-ok", el).forEach(b => b.disabled = true); }
      fb.hidden = false;
      fb.className = result === 0 ? "fb show" : "fb ok";
      fb.innerHTML = `<div><b>${result === 0 ? pick(PRAISE.shown) : result === 1 ? pick(PRAISE.first) : tries === 0 ? "Doğru! İpucunu iyi kullandın." : pick(PRAISE.second)}</b>${result === 0 ? ` Doğru cevap: <b class="dc">${esc(dogruYazi)}</b>` : ""}</div><div>${rx(o.aciklama || "")}</div>`;
      if (!silent) opts.onDone && opts.onDone(result);
    };
    const answer = v => {
      if (finished) return;
      if (dogruMu(v)) return finish(tries === 0 && !yr.used ? 1 : 2);
      tries++;
      if (kind === "nokta") { const g = $(`.sd-hit[data-x="${v}"]`, el); if (g) g.classList.add("bad"); }
      else { ekran.classList.add("shake", "yanlis"); setTimeout(() => ekran.classList.remove("shake"), 400); }
      if (tries >= 2) return finish(0);
      fb.hidden = false; fb.className = "fb hint";
      fb.innerHTML = `<div><b>Henüz değil.</b> ${yanlisMetin(o, yr.yanlis())}</div>` +
        (opts.backToInfo ? `<div><button class="btn ghost" data-back>Bilgi kartına bak</button></div>` : "");
      const bk = $("[data-back]", fb); if (bk) bk.onclick = opts.backToInfo;
      if (kind === "girdi") { buf = ""; setTimeout(() => { ekran.classList.remove("yanlis"); ciz(); }, 700); }
    };
    if (kind === "nokta") {
      const svg = $(".sd", el);
      svg.addEventListener("click", e => { const g = e.target.closest(".sd-hit"); if (g && !g.classList.contains("bad")) answer(+g.dataset.x); });
      svg.addEventListener("keydown", e => { const g = e.target.closest(".sd-hit"); if (g && (e.key === "Enter" || e.key === " ")) { e.preventDefault(); answer(+g.dataset.x); } });
    } else {
      const bas = k => {
        if (finished) return;
        if (k === "ok") { if (!buf || buf === "-" || buf.endsWith("/")) { fb.hidden = false; fb.className = "fb hint"; fb.innerHTML = "<div><b>Önce cevabını yaz.</b> Tuşlara dokunarak sayıyı yaz.</div>"; return; } return answer(buf); }
        if (k === "sil") buf = buf.slice(0, -1);
        else if (k === "−" || k === "-") buf = buf.startsWith("-") ? buf.slice(1) : "-" + buf;
        else if (k === "," || k === ".") { if (!buf.includes(",") && !buf.includes("/")) buf += (buf === "" || buf === "-" ? "0" : "") + ","; }
        else if (k === "/") { if (o.kesir && /\d$/.test(buf) && !buf.includes("/") && !buf.includes(",")) buf += "/"; }
        else if (/^\d$/.test(k) && buf.replace(/[-,/]/g, "").length < 7) buf += k;
        ekran.classList.remove("yanlis"); ciz();
      };
      $(".kp-tus", el).addEventListener("click", e => { const b = e.target.closest("[data-k]"); if (b && !b.disabled) bas(b.dataset.k); });
      ekran.addEventListener("keydown", e => {
        const m = { Enter: "ok", Backspace: "sil" }[e.key] || e.key;
        if (/^[\d,.\-−/]$/.test(m) || m === "ok" || m === "sil") { e.preventDefault(); bas(m); }
      });
      ekran.addEventListener("click", () => ekran.focus());
    }
    if (state.result !== undefined) finish(state.result, true);
    return { get finished() { return finished; } };
  }

  // Adım adım çözüm. c: {baslik, problem, sayiDogrusu, adimlar:[{metin, islem, sayiDogrusu, soru}], sonuc}
  // Adımda "soru" varsa (Sıra sende) adım boş gelir; öğrenci cevaplayınca işlem satırı açılır ve sonraki adıma geçilir.
  function adimHTML(a, n, acik) {
    return `<li class="adim${a.soru ? " bos" : ""}" data-n="${n}"><div class="adim-no">${n + 1}</div><div class="adim-ic">
      <p>${rx(a.metin || "")}</p>${a.sayiDogrusu ? `<div class="sd-wrap">${sdHTML(a.sayiDogrusu)}</div>` : ""}
      ${a.soru ? `<div class="adim-soru">${questionHTML(a.soru)}</div>` : ""}
      ${a.islem ? `<div class="islem"${a.soru && !acik ? " hidden" : ""}>${rx(a.islem)}</div>` : ""}</div></li>`;
  }
  function cozumStatik(c) {
    return `<div class="cozum statik">${c.problem ? `<div class="problem">${rx(c.problem)}</div>` : ""}${c.sayiDogrusu ? `<div class="sd-wrap">${sdHTML(c.sayiDogrusu)}</div>` : ""}
      <ol class="adimlar">${c.adimlar.map((a, n) => adimHTML({ ...a, soru: null }, n, true)).join("")}</ol>${c.sonuc ? `<div class="sonuc">${rx(c.sonuc)}</div>` : ""}</div>`;
  }
  // st: {acik: kaç adım açıldı, q: {adım: soru durumu}}; bitti(): bütün adımlar açılınca bir kez çağrılır
  function runCozum(box, c, st, bitti, kavram) {
    const yan = c.sayiDogrusu && c.sayiDogrusu.dikey;   // dikey sayı doğrusu adımların yanında durur (geniş ekranda)
    box.innerHTML = `<div class="cozum${yan ? " yan" : ""}">${c.problem ? `<div class="problem">${rx(c.problem)}</div>` : ""}
      <div class="coz-govde">${c.sayiDogrusu ? `<div class="sd-wrap">${sdHTML(c.sayiDogrusu)}</div>` : ""}<div class="coz-adim">
      <ol class="adimlar"></ol><div class="row"><button class="btn primary" data-adim>Sonraki adım</button>${listenBtn([c.problem, ...c.adimlar.map(a => `${a.metin || ""} ${a.islem || ""}`)].join(". "))}</div>
      <div class="sonuc" hidden>${rx(c.sonuc || "")}</div></div></div></div>`;
    const ol = $(".adimlar", box), btn = $("[data-adim]", box);
    st.q = st.q || {};
    const guncelle = () => {
      const son = c.adimlar[st.acik - 1], bekliyor = son && son.soru && !(st.q[st.acik - 1] && st.q[st.acik - 1].result !== undefined);
      btn.hidden = st.acik >= c.adimlar.length || bekliyor;
      if (st.acik >= c.adimlar.length && !bekliyor) { if (c.sonuc) $(".sonuc", box).hidden = false; if (!st.bitti) { st.bitti = true; bitti && bitti(); } }
    };
    const ac = n => {
      const a = c.adimlar[n]; ol.insertAdjacentHTML("beforeend", adimHTML(a, n, false));
      const li = ol.lastElementChild;
      if (a.soru) {
        st.q[n] = st.q[n] || { wrong: [], result: undefined };
        wireQuestion($(".q", li), a.soru, { state: st.q[n], kavram, onDone: () => { const i = $(".islem", li); if (i) i.hidden = false; li.classList.remove("bos"); guncelle(); } });
        if (st.q[n].result !== undefined) { const i = $(".islem", li); if (i) i.hidden = false; li.classList.remove("bos"); }
      }
    };
    st.acik = Math.max(1, st.acik || 0);
    for (let n = 0; n < st.acik; n++) ac(n);
    btn.onclick = () => { ac(st.acik); st.acik++; guncelle(); ol.lastElementChild.scrollIntoView({ block: "nearest", behavior: "smooth" }); };
    guncelle();
  }

  // ---------- Hazır mısın? (konu başı ön koşul kontrolü) ----------
  // d.hazirlik = {baslik, giris, maddeler:[{ad, sinif, svg, anlatim, akilda, sayiDogrusu, ornek: cozum, sorular:[soru, yedek soru]}]}
  // Her madde için bir soru sorulur; sonuçta eksik görülen maddeler için kısa hatırlatma + yeni soru önerilir.
  function renderHazirlik(box, h, ilerle) {
    const sk = key("hazirlik:" + S.konu);
    let kayit = store.get(sk, null);     // {r: [1|2|0], t: [true: tekrar edip doğru yaptı]}
    const ms = h.maddeler, kaydet = () => store.set(sk, kayit);
    const durum = i => kayit.t[i] ? "tamam" : kayit.r[i] === 1 ? "tamam" : kayit.r[i] === 2 ? "orta" : "eksik";
    const giris = () => {
      box.innerHTML = `<div class="kicker">Başlamadan önce</div><h3>${esc(h.baslik || "Hazır mısın?")}</h3>
        <p class="big">${rx(h.giris || "Bu konu, daha önce öğrendiğin bazı bilgilerin üzerine kuruluyor. Önce onları hatırlıyor musun bakalım. Not yok; sadece nereden başlayacağımızı bulacağız.")}</p>
        <div class="hz-liste">${ms.map((m, i) => `<span class="hz-chip">${m.svg || ""}<span><b>${esc(m.ad)}</b>${m.sinif ? `<small>${esc(m.sinif)}</small>` : ""}</span></span>`).join("")}</div>
        <div class="row"><button class="btn primary" data-hz-basla>Kontrol edelim (${ms.length} soru)</button><button class="btn ghost" data-hz-atla>Bu bölümü geç</button></div>`;
      $("[data-hz-basla]", box).onclick = () => { kayit = { r: [], t: [] }; soru(0); };
      $("[data-hz-atla]", box).onclick = ilerle;
    };
    const soru = i => {
      if (i >= ms.length) { kaydet(); return rapor(); }
      const m = ms[i], q = m.sorular[0];
      box.innerHTML = `<div class="kicker">Hazır mısın? · Soru ${i + 1} / ${ms.length}</div><h3>${esc(m.ad)}</h3>
        <div id="hzq">${questionHTML(q)}</div><div class="row"><button class="btn primary" data-hz-devam hidden>${i < ms.length - 1 ? "Sonraki soru" : "Sonucu gör"}</button></div>`;
      wireQuestion($("#hzq .q", box), q, { kavram: { ad: m.ad, aciklama: m.anlatim, akilda: m.akilda, svg: m.svg }, onDone: r => { kayit.r[i] = r; $("[data-hz-devam]", box).hidden = false; } });
      $("[data-hz-devam]", box).onclick = () => soru(i + 1);
    };
    const rapor = () => {
      const eksik = ms.filter((m, i) => durum(i) === "eksik"), orta = ms.filter((m, i) => durum(i) === "orta");
      const adlar = l => { const a = l.map(m => `"${m.ad}"`); return a.length > 1 ? a.slice(0, -1).join(", ") + " ve " + a[a.length - 1] : a[0]; };
      const mesaj = eksik.length ? `Önce şunlara birlikte tekrar bakalım: <b>${esc(adlar(eksik))}</b>. Her birinde kısa bir hatırlatma ve yeni bir soru var. Hazır hissedince bu yılki konuya başla.`
        : orta.length ? `Hazırsın! Yalnızca <b>${esc(adlar(orta))}</b> konusuna bir göz atmak iyi olur. İstersen hemen başlayabilirsin.`
        : "Hazırsın! Gereken bilgileri hatırlıyorsun. Bu yılki konuya başlayabilirsin.";
      box.innerHTML = `<div class="kicker">Hazır mısın? · Sonuç</div><h3>${eksik.length ? "Biraz hatırlayalım" : "Harika, hazırsın!"}</h3>
        <p class="big">${mesaj}</p>
        <div class="hz-rapor">${ms.map((m, i) => { const d_ = durum(i);
          return `<div class="hz-satir ${d_}"><span class="hz-ik" aria-hidden="true">${d_ === "tamam" ? "✓" : d_ === "orta" ? "~" : "!"}</span>
          <span class="hz-ad"><b>${esc(m.ad)}</b><small>${kayit.t[i] ? "Tekrar ettin, şimdi biliyorsun" : d_ === "tamam" ? "Biliyorsun" : d_ === "orta" ? "İpucuyla buldun" : "Tekrar etmek iyi olur"}${m.sinif ? ` · ${esc(m.sinif)}` : ""}</small></span>
          <button class="btn${d_ === "eksik" ? " primary" : " ghost"}" data-hz-tekrar="${i}">${d_ === "tamam" ? "Hatırlatmayı aç" : "Tekrar bak"}</button></div>`; }).join("")}</div>
        <div class="row"><button class="btn${eksik.length ? "" : " primary"}" data-hz-ilerle>${eksik.length ? "Yine de konuya başla" : "Konuya başla"}</button><button class="btn ghost" data-hz-yeniden>Kontrolü baştan yap</button></div>`;
      $$("[data-hz-tekrar]", box).forEach(b => b.onclick = () => tekrar(+b.dataset.hzTekrar));
      $("[data-hz-ilerle]", box).onclick = ilerle;
      $("[data-hz-yeniden]", box).onclick = () => { kayit = { r: [], t: [] }; soru(0); };
    };
    const tekrar = i => {
      const m = ms[i], q2 = m.sorular[1] || m.sorular[0];
      box.innerHTML = `<div class="kicker">Hatırlayalım · ${esc(m.sinif || "")}</div>
        <div class="info-grid">${m.svg || ""}<div class="stage-body"><h3>${esc(m.ad)}</h3><p class="big">${rx(m.anlatim)}</p>
        ${m.akilda ? `<div class="row"><span class="key"><b>Akılda kalsın</b>${rx(m.akilda)}</span>${listenBtn(m.ad + ". " + m.anlatim)}</div>` : ""}</div></div>
        ${m.sayiDogrusu ? `<div class="sd-wrap">${sdHTML(m.sayiDogrusu)}</div>` : ""}
        ${m.ornek ? `<div class="kicker">Örnek</div><div id="hzOrnek"></div>` : ""}
        <div id="hzSoru" ${m.ornek ? "hidden" : ""}><div class="kicker">Şimdi sen dene</div>${questionHTML(q2)}</div>
        <div class="row"><button class="btn ghost" data-hz-geri>Listeye dön</button></div>`;
      if (m.ornek) runCozum($("#hzOrnek", box), m.ornek, {}, () => { $("#hzSoru", box).hidden = false; });
      wireQuestion($("#hzSoru .q", box), q2, { kavram: { ad: m.ad, aciklama: m.anlatim, akilda: m.akilda, svg: m.svg }, onDone: r => { if (r) { kayit.t[i] = true; kaydet(); } } });
      $("[data-hz-geri]", box).onclick = rapor;
      box.scrollIntoView({ block: "start", behavior: "smooth" });
    };
    if (kayit && kayit.r && kayit.r.length === ms.length) rapor(); else giris();
  }

  // ---------- Hatayı Bul: cümledeki yanlış kelime(ler)e dokun, sonra doğrusunu seç ----------
  // d.hatalar = [{cumle, yanlis, secenekler[3], dogru, tr?, aciklama}] — "yanlis" cümlede birebir geçen parça.
  function gameErrors(box) {
    const tur = shuffle(S.data.hatalar).slice(0, 6);
    let i = 0, temiz = 0;
    const draw = () => {
      if (i >= tur.length) {
        box.innerHTML = `<div class="game-end"><div class="stars">${"★".repeat(temiz)}${"☆".repeat(tur.length - temiz)}</div>
          <p class="game-msg">${tur.length} hatayı düzelttin, ${temiz} tanesini hiç yanılmadan buldun. Dedektif gibi dikkatliydin!</p><button class="btn primary" id="hagain">Yeni tur</button></div>`;
        $("#hagain", box).onclick = () => gameErrors(box); return;
      }
      const h = tur[i], k = h.cumle.indexOf(h.yanlis);
      const once = h.cumle.slice(0, k).split(/\s+/).filter(Boolean), sonra = h.cumle.slice(k + h.yanlis.length).split(/\s+/).filter(Boolean);
      const parca = [...once.map(t => ({ t })), { t: h.yanlis, hedef: true }, ...sonra.map(t => ({ t }))];
      let bulDeneme = 0, secDeneme = 0;
      box.innerHTML = `<p class="ek" style="margin:0 0 10px">Cümle ${i + 1} / ${tur.length}. Bu cümlede bir hata var. Yanlış olan kelimeye dokun.</p>
        <div class="hata-cumle" lang="en">${parca.map((p, n) => !p.hedef && /^[^\p{L}\p{N}]+$/u.test(p.t) ? `<span class="hpunc">${esc(p.t)}</span>` : `<button class="tok htok" data-n="${n}">${esc(p.t)}</button>`).join("")}</div>
        ${h.tr ? `<p class="ek hata-tr" hidden>${rx(h.tr)}</p>` : ""}
        <div id="hsec"></div><p class="game-msg" id="hmsg"></p>`;
      const msg = t => $("#hmsg", box).innerHTML = t;
      box.onclick = e => {
        const t = e.target.closest(".htok"); if (!t || t.disabled || $("#hsec .opts", box)) return;
        const p = parca[+t.dataset.n];
        if (!p.hedef) {
          bulDeneme++; oyunHata(box, "hata"); t.classList.add("shake"); setTimeout(() => t.classList.remove("shake"), 400);
          if (bulDeneme >= 2) { const tr = $(".hata-tr", box); if (tr) tr.hidden = false; $(`.htok[data-n="${once.length}"]`, box).classList.add("ipucu"); msg("İpucu: Türkçesini oku. Hatalı kelime parlayan kutuda."); }
          else msg("Bu kelime doğru. Cümleyi bir daha oku, hangi kelime yanlış duruyor?");
          return;
        }
        t.classList.add("bad"); t.classList.remove("ipucu");
        msg(bulDeneme ? "Buldun! Şimdi doğrusunu seç." : "Harika, hatayı hemen buldun! Şimdi doğrusunu seç.");
        $("#hsec", box).innerHTML = `<div class="opts">${h.secenekler.map((s, j) => `<button class="opt" data-o="${j}" lang="en">${"abc"[j]}) ${esc(s)}</button>`).join("")}</div>`;
        $("#hsec .opts", box).onclick = ev => {
          const b = ev.target.closest(".opt"); if (!b || b.disabled) return;
          const j = +b.dataset.o;
          const bitir = ok => {
            $$("#hsec .opt", box).forEach((x, n) => { x.disabled = true; if (n === h.dogru) x.classList.add("right"); });
            t.textContent = h.secenekler[h.dogru]; t.classList.remove("bad"); t.classList.add("ok");
            if (ok && !bulDeneme && !secDeneme) temiz++;
            msg(`<b>${ok ? (secDeneme ? "Doğru! İkinci denemede buldun." : "Doğru!") : "Doğrusu yeşil olan."}</b> ${rx(h.aciklama || "")}`);
            tts.sayEn(h.cumle.slice(0, k) + h.secenekler[h.dogru] + h.cumle.slice(k + h.yanlis.length));
            const n = document.createElement("button"); n.className = "btn primary"; n.textContent = "Sonraki cümle"; n.onclick = () => { i++; draw(); }; $("#hmsg", box).after(n);
          };
          if (j === h.dogru) return bitir(true);
          secDeneme++; b.classList.add("wrong"); b.disabled = true;
          if (secDeneme >= 2) return bitir(false);
          msg("Henüz değil. Cümlenin anlamını ve kuralı düşün, bir daha dene.");
        };
      };
    };
    draw();
  }

  // ---------- Ara Durak (konu tarama ve gözden geçirme) ----------
  // ders.json'da konu listesine {"id": "u1t1", "tur": "tarama", ...} olarak girer; konu dosyası:
  // {id, tur: "tarama", unite, baslik, sayfalar, giris, buyukResim?, kapsar: [konu id],
  //  hatirla?: [{konu, maddeler: [3 kısa özet]}]  (yoksa konunun ilk 3 "akildaKalsin" maddesi),
  //  eskiSoru?: 4 (kapsanan konuların kendi sorularından seçilecek soru sayısı; zorlanılan kavramlar önce),
  //  sorular: [konuları birleştiren yeni sorular; her biri "kaynak": [{konu, kavram?}]]}
  // Sonuç cihazda tutulur; başarı ≥ %80 ise tekrar 3 → 10 → 30 gün sonra, değilse 2 gün sonra önerilir.
  const isDurak = k => !!(k && k.tur === "tarama");
  const DURAK_ARALIK = [3, 10, 30];
  const AYLAR = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"];
  const tarihYaz = s => { if (s === gun()) return "bugün"; const [, a, g] = String(s).split("-"); return `${+g} ${AYLAR[+a - 1]}`; };
  const sonucOf = id => store.get(key("sonuc:" + id), {});
  const durakKayit = {
    get(id) { return store.get(key("durak:" + id), null); },
    zaman(id) { const r = durakKayit.get(id); return !!(r && r.n && r.n <= gun()); },
    kaydet(id, sonuc) {
      const eski = durakKayit.get(id) || {}, dogru = sonuc.filter(x => x.r === 1).length, iyi = dogru / sonuc.length >= .8;
      const k = iyi ? Math.min((eski.k ?? -1) + 1, DURAK_ARALIK.length - 1) : 0;
      const r = { t: gun(), sonuc, dogru, toplam: sonuc.length, k, n: gun(iyi ? DURAK_ARALIK[k] : 2), kez: (eski.kez || 0) + 1 };
      store.set(key("durak:" + id), r); return r;
    }
  };
  // Ünite içindeki konu sırası (ara duraklar sayılmaz)
  const konuNoOf = id => { const t = allTopics().find(k => k.id === id); if (!t) return ""; return S.ders.uniteler[t.ui].konular.slice(0, t.ki + 1).filter(k => !isDurak(k)).length; };
  const durakDurum = r => `<div class="dk-durum"><b>Son tarama:</b> ${tarihYaz(r.t)} · ${r.dogru} / ${r.toplam} ilk denemede doğru<br><b>Sonraki tekrar:</b> ${r.n <= gun() ? "<span class=\"dk-simdi\">şimdi</span>" : tarihYaz(r.n)}</div>`;

  // Ara Durak'tan bir konuya (ve kavramına) git; konuda "Ara Durak'a dön" düğmesi görünür.
  function gitKonu(id, kavram) { store.set(key("sekme:" + id), "bak"); S.hedef = kavram || null; S.donus = S.konu; openKonu(id, true); }

  async function yukleKonular(ids) {
    await Promise.all(ids.map(async id => {
      if (S.cache[id]) return;
      try { const r = await fetch("konular/" + id + ".json", { cache: "no-cache" }); if (r.ok) S.cache[id] = await r.json(); } catch (e) {}
    }));
  }

  function renderDurak() {
    const d = S.data;
    $("#content").innerHTML = `<section class="konu-head durak-head"><div class="meta"><span>${esc(d.unite)}</span><span class="pill">${ICON.durak}Ara Durak</span><span class="pill">${esc(d.sayfalar)}</span></div>
      <h2>${esc(d.baslik)}</h2>
      <div class="tabs" role="tablist">
        <button class="tab" role="tab" data-tab="hatirla">${ICON.bak}Hatırla</button>
        <button class="tab" role="tab" data-tab="tarama">${ICON.test}Tarama Testi</button>${d.oyunlar === false ? "" : `<button class="tab" role="tab" data-tab="oyunlar">${ICON.tekrar}Oyunlar</button>`}</div></section>
      <div class="panel" id="panel"></div>`;
    $$(".tab").forEach(b => b.onclick = () => setTab(b.dataset.tab));
    S.durakAsil = d;
    let sk = store.get(key("sekme:" + S.konu), "hatirla"); if (sk !== "tarama" && !(sk === "oyunlar" && d.oyunlar !== false)) sk = "hatirla";
    setTab(sk);
    S.onKonu && S.onKonu();
  }

  // Oyunlar sekmesi: kapsanan konuların tekrar oyunları karışık oynanır (kart, eşleştir, gruplama; İngilizcede kelime ve cümle oyunları).
  // Kavramlardan "oyunKavram" kadarı (varsayılan 8) seçilir: zorlanılanlar önce, konulara dengeli dağıtılarak.
  function durakOyunVerisi(d) {
    const ks = d.kapsar.map(id => S.cache[id]).filter(Boolean), n = d.oyunKavram || 8;
    const havuz = ks.map(k => { const r = sonucOf(k.id), zor = x => x.ad in r && r[x.ad] !== 1; return [...shuffle(k.kavramlar.filter(zor)), ...shuffle(k.kavramlar.filter(x => !zor(x)))]; });
    const sec = []; for (let t = 0; sec.length < n && havuz.some(h => h.length); t++) { const h = havuz[t % havuz.length]; if (h.length) sec.push(h.shift()); }
    const hepsi = f => ks.flatMap(k => k[f] || []);
    return { ...d, kavramlar: shuffle(sec), gruplar: [...(d.gruplar || []), ...hepsi("gruplar")],   // durağın kendi (konular arası) gruplamaları önce
      cumleler: hepsi("cumleler"), hatalar: hepsi("hatalar"), kelimeler: hepsi("kelimeler"),
      resimEslestir: ks.some(k => k.resimEslestir), kelimeOyunlari: ks.every(k => k.kelimeOyunlari !== false) };
  }

  function renderHatirla(root) {
    const d = S.data, kayit = durakKayit.get(S.konu), h = [];
    const kart = kartlarOf(S.konu);
    h.push(`<section><p class="lead">${rx(d.giris)}</p>${kayit ? durakDurum(kayit) : ""}${kart ? `<div class="row dk-kart">${kartlarBtn(kart)}<span class="ek">Yazdır, kes, ortadan katla: önde İngilizce, arkada Türkçe.</span></div>` : ""}</section>`);
    if (d.buyukResim) h.push(`<section class="facts"><div class="eyebrow">Büyük resim</div><p>${rx(d.buyukResim)}</p></section>`);
    d.kapsar.forEach(id => {
      const k = S.cache[id]; if (!k) return;
      const hm = (d.hatirla || []).find(x => x.konu === id), maddeler = hm ? hm.maddeler : k.akildaKalsin.slice(0, 3), r = sonucOf(id);
      h.push(`<section class="durak-konu"><div class="sec-title"><h3><span class="dk-no">${konuNoOf(id)}</span>${esc(k.baslik)}</h3>
        <button class="btn ghost" data-git="${esc(id)}">Konuya git</button></div>
        <ul class="remember">${maddeler.map(a => `<li>${rx(a)}</li>`).join("")}</ul>
        <p class="ek dk-ipucu">Kartlara dokun. Önce kendin hatırlamaya çalış, sonra cevabı gör.</p>
        <div class="recall">${k.kavramlar.map(kv => `<button data-reveal>${kv.svg}<span>${esc(kv.ad)}${kv.ad in r && r[kv.ad] !== 1 ? ' <small class="dk-zor">zorlanmıştın</small>' : ""} → <span class="ans" hidden>${rx(kv.akilda)}</span><span class="q-mark">?</span></span></button>`).join("")}</div></section>`);
    });
    h.push(`<div class="row"><button class="btn primary" data-goto="tarama">Tarama testine geç</button></div>`);
    root.innerHTML = h.join("");
    $$("[data-reveal]", root).forEach(b => b.onclick = () => { $(".ans", b).hidden = false; $(".q-mark", b).hidden = true; });
    $$("[data-git]", root).forEach(b => b.onclick = () => gitKonu(b.dataset.git));
    $$("[data-goto]", root).forEach(b => b.onclick = () => setTab(b.dataset.goto));
  }

  // Soru listesi: kapsanan konuların kendi sorularından (zorlanılan kavramlar önce, konulara dağıtılarak) + yeni sorular, sırayla karışık.
  function durakSorulari(d) {
    const yeni = (d.sorular || []).map(q => ({ q, kaynak: q.kaynak || [] }));
    const havuz = d.kapsar.map(id => {
      const k = S.cache[id]; if (!k) return [];
      const r = sonucOf(id), zor = ad => ad in r && r[ad] !== 1;
      const kv = k.kavramlar.filter(x => x.soru).map(x => ({ q: x.soru, kaynak: [{ konu: id, kavram: x.ad }], zor: zor(x.ad) }));
      const ts = (k.sorular || []).map(q => ({ q, kaynak: [{ konu: id }] }));
      return [...shuffle(kv.filter(x => x.zor)), ...shuffle([...kv.filter(x => !x.zor), ...ts])];
    });
    const eski = [], n = d.eskiSoru ?? 4;
    for (let t = 0; eski.length < n && havuz.some(h => h.length); t++) { const h = havuz[t % havuz.length]; if (h.length) eski.push(h.shift()); }
    const e = shuffle(eski), liste = [];
    while (e.length || yeni.length) { if (e.length) liste.push(e.shift()); if (yeni.length) liste.push(yeni.shift()); }
    return liste;
  }

  function renderTarama(root) {
    const d = S.data;
    const toplam = (d.sorular || []).length + (d.eskiSoru ?? 4);
    // Yanlış ya da ipucuyla bulunan soruda: ilgili kavramın kısa hatırlatması ve konuya dönüş düğmesi
    const hatirlat = (box, it) => {
      const parca = (it.kaynak || []).slice(0, 2).map(x => {
        const k = S.cache[x.konu]; if (!k) return "";
        const kv = x.kavram && k.kavramlar.find(y => y.ad === x.kavram);
        return kv ? `<div class="dk-hat-ic">${kv.svg}<div><b>${esc(kv.ad)}</b> <small>· ${konuNoOf(x.konu)}. konu</small><p>${rx(kv.aciklama)}</p>
            <div class="row"><span class="key"><b>Akılda kalsın</b>${rx(kv.akilda)}</span><button class="btn ghost" data-git="${esc(x.konu)}" data-kv="${esc(kv.ad)}">Konuda bak</button></div></div></div>`
          : `<div class="dk-hat-ic"><div><b>${esc(k.baslik)}</b> <small>· ${konuNoOf(x.konu)}. konu</small><ul class="remember">${k.akildaKalsin.slice(0, 2).map(a => `<li>${rx(a)}</li>`).join("")}</ul>
            <div class="row"><button class="btn ghost" data-git="${esc(x.konu)}">Konuya bak</button></div></div></div>`;
      }).join("");
      if (parca) box.insertAdjacentHTML("beforeend", `<div class="dk-hat"><div class="kicker">Hatırlatma</div>${parca}</div>`);
      $$("[data-git]", box).forEach(b => b.onclick = () => gitKonu(b.dataset.git, b.dataset.kv));
    };
    const rapor = (kayit, basla) => {
      const sonuc = kayit.sonuc, c = v => sonuc.filter(x => x.r === v).length;
      const satirlar = d.kapsar.map(id => {
        const k = S.cache[id], ilgili = sonuc.filter(x => x.kaynak.some(y => y.konu === id));
        if (!k || !ilgili.length) return "";
        const bir = ilgili.filter(x => x.r === 1).length, durum = ilgili.some(x => x.r === 0) ? "eksik" : ilgili.some(x => x.r === 2) ? "orta" : "tamam";
        return `<div class="hz-satir ${durum}"><span class="hz-ik" aria-hidden="true">${durum === "tamam" ? "✓" : durum === "orta" ? "~" : "!"}</span>
          <span class="hz-ad"><b>${konuNoOf(id)}. ${esc(k.baslik)}</b><small>${bir} / ${ilgili.length} ilk denemede · ${durum === "tamam" ? "İyi hatırlıyorsun" : durum === "orta" ? "İpuçlarıyla buldun" : "Kısa bir tekrar iyi olur"}</small></span>
          <button class="btn${durum === "eksik" ? " primary" : " ghost"}" data-git="${esc(id)}">Konuya git</button></div>`;
      }).join("");
      const zayif = []; sonuc.filter(x => x.r !== 1).forEach(x => x.kaynak.forEach(y => { if (y.kavram && !zayif.some(z => z.konu === y.konu && z.kavram === y.kavram)) zayif.push(y); }));
      const eksikVar = sonuc.some(x => x.r === 0), iyi = kayit.dogru / kayit.toplam >= .8;
      const mesaj = iyi ? "Harika! Bu konuları iyi hatırlıyorsun. Öğrendiklerin yerine oturmuş."
        : eksikVar ? "Çok iyi çalıştın; yanlış yaptığın soruları tekrar geldiğinde düzelttin. Aşağıda ! olan konulara kısa bir tekrar yapalım."
        : "İpuçlarını kullanarak hepsini buldun. Bu, iyi çalışmanın işareti. Turuncu kavramlara bir göz atman yeter.";
      root.innerHTML = `<div class="stage"><div class="kicker">Ara Durak · Sonuç</div><h3>${iyi ? "Aklında kalmış!" : "Neredeyse tamam!"}</h3><p class="big">${mesaj}</p>
        <div class="done-stats"><div class="stat"><b>${c(1)}</b><span>ilk denemede doğru</span></div><div class="stat"><b>${c(2)}</b><span>ipucuyla doğru</span></div><div class="stat"><b>${c(0)}</b><span>tekrar gelince çalıştın</span></div></div>
        <div class="hz-rapor">${satirlar}</div>
        ${zayif.length ? `<div><div class="kicker">Tekrar bakman gereken kavramlar</div><div class="dk-liste">${zayif.map(z => `<button data-git="${esc(z.konu)}" data-kv="${esc(z.kavram)}">${konuNoOf(z.konu)}. konu · ${esc(z.kavram)}</button>`).join("")}</div></div>` : ""}
        <p class="dk-sonraki">${ICON.tekrar}<span>Bu durağı <b>${tarihYaz(kayit.n)}</b> tekrar tara. Zamanı gelince konu listesinde haber vereceğim.</span></p>
        <div class="row"><button class="btn primary" data-yeniden>Testi yeniden yap</button><button class="btn ghost" data-goto="hatirla">Hatırla'ya dön</button></div></div>`;
      $$("[data-git]", root).forEach(b => b.onclick = () => gitKonu(b.dataset.git, b.dataset.kv));
      $("[data-yeniden]", root).onclick = basla;
      $("[data-goto]", root).onclick = () => setTab("hatirla");
    };
    soruAkisi(root, {
      anahtar: "akis:" + S.konu, tur: "tarama", birak: "Sonra devam et",
      hazirla: () => durakSorulari(d).map((it, n) => ({ q: it.q, n, kaynak: it.kaynak })),
      kicker: it => { const konular = [...new Set(it.kaynak.map(x => x.konu))].map(id => `${konuNoOf(id)}. konu`).join(" + "); return `${it.kaynak.length > 1 ? "Konuları birleştir" : "Hatırla"}${konular ? " · " + esc(konular) : ""}`; },
      kavram: it => { const k0 = it.kaynak.find(x => x.kavram) || {}; if (k0.konu && S.cache[k0.konu]) return S.cache[k0.konu].kavramlar.find(y => y.ad === k0.kavram) || null;
        const k1 = (it.kaynak[0] || {}).konu; return it.q.kavram && S.cache[k1] ? S.cache[k1].kavramlar.find(y => y.ad === it.q.kavram) || null : null; },
      sonuc: (box, it, r) => { if (r !== 1) hatirlat(box, it); },
      giris: (basla, devam) => {
        const kayit = durakKayit.get(S.konu);
        root.innerHTML = `<div class="stage"><div class="kicker">Tarama testi</div><h3>${devam ? "Yarım kalan tarama" : kayit ? "Tekrar tarayalım" : "Neler aklında kalmış?"}</h3>
          <p class="big">${devam ? "Taramayı yarıda bırakmıştın. Kaldığın yerden devam edelim." : `${toplam} soru var. Bazıları konulardaki sorulardan, bazıları konuları birleştiren yeni sorular. Her soruda 2 hakkın var. Yanlış yaptığın soru birkaç soru sonra yeniden gelir. Not yok; sonunda hangi konuya tekrar bakman gerektiğini göstereceğim.`}</p>
          ${kayit && !devam ? durakDurum(kayit) : ""}
          <div class="row">${devam ? `<button class="btn primary" data-devam>Kaldığın yerden devam et</button>` : `<button class="btn primary" data-basla>Başla</button>`}${kayit && !devam ? `<button class="btn ghost" data-rapor>Son sonucu gör</button>` : ""}</div></div>`;
        const bb = $("[data-basla]", root); if (bb) bb.onclick = basla;
        const dv = $("[data-devam]", root); if (dv) dv.onclick = devam;
        const rb = $("[data-rapor]", root); if (rb) rb.onclick = () => rapor(kayit, basla);
      },
      bitis: (st, oz, basla) => {
        const asil = st.liste.filter(x => !x.tekrar).sort((a, b) => a.n - b.n);
        const kayit = durakKayit.kaydet(S.konu, asil.map(x => ({ r: st.ilk[x.n] ?? 0, kaynak: x.kaynak })));
        renderNav(); rapor(kayit, basla);
      }
    });
  }

  // ---------- Soru akışı (Test ve Ara Durak taraması) ----------
  // Sorular tek tek gelir; soru ve şık sırası her başlangıçta karışır. İki yanlıştan sonra cevap açıklamasıyla gösterilir ve
  // soru 3 soru sonra şıkları yeniden karışmış olarak tekrar gelir (en çok 2 kez). "Baştan başla" yalnızca bitişte.
  // Durum cihazda tutulur: sayfa yenilense ya da sekme değişse de kaldığı yerden devam eder (baştan başlatarak "hepsi doğru" yapılamaz).
  // İlk deneme sonucu (st.ilk[n]) kalıcıdır; tekrar gelen sorunun sonucu yalnızca st.son'a yazılır.
  const karistir = q => {
    if (qKind(q) !== "secim" || q.ima || !Array.isArray(q.secenekler) || q.secenekler.length < 2) return { ...q };
    const p = shuffle(q.secenekler.map((x, j) => j));
    return { ...q, secenekler: p.map(j => q.secenekler[j]), dogru: p.indexOf(q.dogru) };
  };
  function soruAkisi(root, c) {
    const k = key(c.anahtar);
    let st = store.get(k, null);
    const kaydet = () => store.set(k, st);
    const basla = () => {
      st = { v: 1, bas: simdi(), liste: shuffle(c.hazirla()).map(it => ({ ...it, q: karistir(it.q), tekrar: 0 })), i: 0, ilk: {}, son: {}, q: {} };
      kaydet(); KAYIT.olay("test-basla", { tur: c.tur, toplam: st.liste.length }); ciz();
    };
    const ciz = () => {
      const it = st.liste[st.i];
      root.innerHTML = `<div class="stage akis"><div class="progress"><span>Soru ${st.i + 1} / ${st.liste.length}</span><div class="bar"><i style="width:${(st.i + 1) / st.liste.length * 100}%"></i></div></div>
        <div class="kicker">${it.tekrar ? `<span class="tekrar-etiket">${ICON.tekrar}Tekrar geldi · şıklar yer değiştirdi</span>` : c.kicker ? c.kicker(it) : "Soru"}</div>
        <div id="sq">${questionHTML(it.q)}</div><div id="sqEk"></div>
        <div class="stage-nav">${c.birak ? `<button class="btn ghost" data-birak>${esc(c.birak)}</button>` : "<span></span>"}<button class="btn primary" data-sonraki disabled>${st.i === st.liste.length - 1 ? "Sonucu gör" : "Sonraki soru"}</button></div></div>`;
      const qs = st.q[st.i] = st.q[st.i] || { wrong: [], result: undefined }, sonraki = $("[data-sonraki]", root), ek = $("#sqEk", root);
      const bitti = (r, yeni) => {
        sonraki.disabled = false;
        if (yeni) {
          if (!(it.n in st.ilk)) st.ilk[it.n] = r;
          st.son[it.n] = r;
          if (r === 0 && it.tekrar < 2) st.liste.splice(Math.min(st.i + 3, st.liste.length), 0, { ...it, q: karistir(it.q), tekrar: it.tekrar + 1 });
          kaydet();
          sonraki.textContent = st.i === st.liste.length - 1 ? "Sonucu gör" : "Sonraki soru";
        }
        if (r === 0 && it.tekrar < 2) ek.insertAdjacentHTML("afterbegin", `<p class="tekrar-not">${ICON.tekrar}<span>Bu soru birkaç soru sonra yeniden gelecek. Açıklamayı dikkatle oku.</span></p>`);
        c.sonuc && c.sonuc(ek, it, r);
      };
      wireQuestion($("#sq .q", root), it.q, { state: qs, kavram: c.kavram ? c.kavram(it) : null, tekrar: !!it.tekrar, davet: true, onDone: r => bitti(r, true) });
      $("#sq", root).addEventListener("click", () => setTimeout(kaydet, 0));   // yanlış şık / kanıt / ipucu durumu da saklansın
      if (qs.result !== undefined) bitti(qs.result, false);
      sonraki.onclick = () => {
        tts.stop();
        if (st.i < st.liste.length - 1) { st.i++; kaydet(); ciz(); root.scrollIntoView({ block: "start", behavior: "smooth" }); return; }
        bitir();
      };
      const bk = $("[data-birak]", root); if (bk) bk.onclick = () => { kaydet(); tts.stop(); S.akisBirak = c.anahtar; c.giris(basla, devam); };
    };
    const devam = () => { S.akisBirak = null; ciz(); };
    const bitir = () => {
      const v = Object.values(st.ilk), say = x => v.filter(y => y === x).length;
      const oz = { toplam: v.length, ilk1: say(1), ilk2: say(2), ilk0: say(0), tekrarSoru: st.liste.filter(x => x.tekrar).length, sureDk: +((simdi() - st.bas) / 60000).toFixed(1) };
      const son = st; st = null; try { localStorage.removeItem(k); } catch (e) {}
      KAYIT.olay("test-bitti", { tur: c.tur, ...oz });
      c.bitis(son, oz, basla);
      KOC.ozet();
      root.scrollIntoView({ block: "start", behavior: "smooth" });
    };
    if (st && st.liste && st.i < st.liste.length) {
      if (S.akisBirak === c.anahtar) return c.giris(basla, devam);
      ciz();
      if (st.i > 0 || st.q[0] && st.q[0].wrong && st.q[0].wrong.length) KOC.goster("devam", "Kaldığın yerden devam ediyoruz. Baştan başlamana gerek yok; yanlış yaptığın soru birazdan yine gelecek.");
    } else c.giris(basla, null);
  }

  // ---------- Test ----------
  // Öğrenci modu: sorular tek tek (soruAkisi). Sınıf modu: bütün sorular tek sayfada, "Cevabı göster" ile (öğretmen tahtada kullanır).
  const ogrenBitti = id => { if (store.get(key("ogren-bitti:" + id), false)) return true; const d = S.cache[id]; return !!d && store.get(key("adim:" + id), 0) >= buildSteps(d).length - 1; };
  function renderTest(root) {
    const d = S.data;
    if (document.body.classList.contains("sinif")) return renderTestListe(root);
    if (!d.sorular || !d.sorular.length) { root.innerHTML = `<div class="notice">Bu konunun testi yok.</div>`; return; }
    if (ayar().ogrenKilit && !ogrenBitti(S.konu)) {
      root.innerHTML = `<div class="stage"><div class="kicker">Test</div><h3>Önce Öğren'i bitirelim</h3><p class="big">Test, Öğren bölümünü bitirince açılır. Kaldığın adımdan devam edebilirsin.</p><div class="row"><button class="btn primary" data-goto="ogren">Öğren'e git</button></div></div>`;
      $("[data-goto]", root).onclick = () => setTab("ogren"); return;
    }
    soruAkisi(root, {
      anahtar: "akis:test:" + S.konu, tur: "test",
      hazirla: () => d.sorular.map((q, n) => ({ q, n })),
      kicker: () => "Konu testi",
      kavram: it => it.q.kavram ? d.kavramlar.find(x => x.ad === it.q.kavram) || null : null,
      giris: (basla, devam) => {
        const gec = store.get(key("testler:" + S.konu), []), ilk = gec[0], son = gec[gec.length - 1];
        root.innerHTML = `<div class="stage"><div class="kicker">Konu testi</div><h3>${d.sorular.length} soru</h3>
          <p class="big">Sorular tek tek gelecek. Her soruda 2 hakkın var; ilk yanlışta ipucu gelir. Yanlış yaptığın soru birkaç soru sonra, şıkları yer değiştirmiş olarak yeniden gelir. Test, hepsini doğru yapınca biter.</p>
          ${son ? `<div class="dk-durum"><b>İlk çözüşün:</b> ${tarihYaz(ilk.t)} · ${ilk.ilk1} / ${ilk.toplam} ilk denemede doğru${gec.length > 1 ? `<br><b>Son çözüşün:</b> ${tarihYaz(son.t)} · ${son.ilk1} / ${son.toplam} ilk denemede doğru` : ""}</div>` : ""}
          <div class="row">${devam ? `<button class="btn primary" data-devam>Kaldığın yerden devam et</button>` : `<button class="btn primary" data-basla>${son ? "Testi yeniden çöz" : "Başla"}</button>`}</div></div>`;
        const bb = $("[data-basla]", root); if (bb) bb.onclick = basla;
        const dv = $("[data-devam]", root); if (dv) dv.onclick = devam;
      },
      bitis: (st, oz, basla) => {
        const gec = store.get(key("testler:" + S.konu), []); gec.push({ t: gun(), ...oz }); store.set(key("testler:" + S.konu), gec.slice(-20));
        const msg = !oz.ilk0 && !oz.ilk2 ? "Hepsini ilk denemede buldun. Çok dikkatli çalıştın!"
          : !oz.ilk0 ? "Hepsini buldun! Bazılarında ipucunu ya da ikinci hakkını iyi kullandın."
          : "Hepsini tamamladın! Yanlış yaptığın sorular tekrar geldiğinde üzerinde çalıştın. Düzeltmek de öğrenmek.";
        root.innerHTML = `<div class="stage"><div class="kicker">Konu testi · Sonuç</div><h3>${oz.toplam} sorunun hepsini tamamladın!</h3><p class="big">${msg}</p>
          <div class="done-stats"><div class="stat"><b>${oz.ilk1}</b><span>ilk denemede doğru</span></div><div class="stat"><b>${oz.ilk2}</b><span>ipucuyla / ikinci denemede</span></div><div class="stat"><b>${oz.ilk0}</b><span>tekrar gelince çalıştın</span></div></div>
          ${gec.length > 1 ? `<p class="ek">İlk çözüşünde ${gec[0].ilk1} / ${gec[0].toplam} soruyu ilk denemede bulmuştun.</p>` : ""}
          <div class="row"><button class="btn primary" data-goto="tekrar">Tekrar'a geç</button><button class="btn ghost" data-yeniden>Testi yeniden çöz</button></div></div>`;
        $("[data-goto]", root).onclick = () => setTab("tekrar");
        $("[data-yeniden]", root).onclick = basla;
      }
    });
  }
  function renderTestListe(root) {
    const d = S.data;
    root.innerHTML = `<div class="scorebar"><span id="score"></span><div class="meter"><i id="meter"></i></div><button class="btn" id="qreset">Baştan başla</button></div>
      <p class="ek" style="margin:0">Sınıf modu: seçenek seçilince cevap gizli kalır, "Cevabı göster" ile açılır.</p>
      <div class="tests">${d.sorular.map((q, i) => `<div class="card-q" data-q="${i}">${questionHTML(q, i + 1)}</div>`).join("")}</div>`;
    let first = 0, answered = 0;
    const upd = () => { $("#score", root).textContent = `${first} / ${d.sorular.length} ilk denemede doğru · ${answered} cevaplandı`; $("#meter", root).style.width = (first / d.sorular.length * 100) + "%"; };
    const kvBul = q => q.kavram ? d.kavramlar.find(k => k.ad === q.kavram) : null;
    $$(".card-q", root).forEach(el => wireQuestion($(".q", el), d.sorular[+el.dataset.q], { kavram: kvBul(d.sorular[+el.dataset.q]), classMode: qKind(d.sorular[+el.dataset.q]) === "secim", onDone: r => { answered++; if (r === 1) first++; upd(); } }));
    $("#qreset", root).onclick = () => renderTestListe(root);
    upd();
  }

  // ---------- Okuma Atölyesi (ders.json "atolye": true → ./atolye.json; adres #atolye) ----------
  // Dersten bağımsız okuma becerisi: 4 uzunluk seviyesi; bir turda seviyenin "turMetin" kadar metni (en az oynananlar önce).
  // Uzun metin "bolumler" ile parça parça okunur (her parçadan sonra durak sorusu), "sorular" bütün metin için sorulur.
  // Seviye açma: o seviyede en az 2 tur ve son 2 turda doğru oranı (ipucuyla doğru dahil) ≥ %80. Kayıt cihazda: ela7:<kod>:atolye.
  const ATOLYE_KV = { ad: "Okuma Dedektifi", aciklama: "1) Soru ne istiyor? 2) Anahtar kelime ne? 3) Kanıt nerede? 4) Şıkları ele.", akilda: "Sor, bul, kanıtla, ele" };
  const ATOLYE_ESIK = .8, ATOLYE_MIN_TUR = 2;
  const atolyeKayit = {
    get() { const k = store.get(key("atolye"), null) || {}; return { sev: k.sev || {}, metin: k.metin || {} }; },
    set(v) { store.set(key("atolye"), v); }
  };
  const sonIki = s => { const t = (s && s.turlar || []).slice(-ATOLYE_MIN_TUR), d = t.reduce((a, x) => a + x.d, 0), n = t.reduce((a, x) => a + x.n, 0); return { tur: (s && s.turlar || []).length, oran: n ? d / n : null }; };
  const sevAcik = (A, k, i) => i === 0 || !!(k.sev[A.seviyeler[i - 1].no] || {}).gecti;
  const yuzde = x => "%" + Math.round(x * 100);
  const sEk = (n, ek) => "S" + n + ({ i: { 1: "'i", 2: "'yi", 3: "'ü", 4: "'ü" }, de: { 1: "'de", 2: "'de", 3: "'te", 4: "'te" } }[ek][n] || "");

  async function openAtolye() {
    tts.stop();
    if (!S.atolye) {
      try { const r = await fetch("atolye.json", { cache: "no-cache" }); if (!r.ok) throw 0; S.atolye = await r.json(); }
      catch (e) { $("#content").innerHTML = `<div class="notice">Okuma Atölyesi açılamadı. İnternet bağlantını kontrol edip sayfayı yenile.</div>`; return; }
    }
    S.konu = "atolye"; S.data = null; S.durakAsil = null; S.botBaslik = "Okuma Atölyesi"; renderNav();
    if (location.hash.slice(1) !== "atolye") history.replaceState(null, "", "#atolye");
    $$(".head-actions a[href='#atolye']").forEach(a => a.setAttribute("aria-pressed", "true"));
    $("#content").innerHTML = `<section class="konu-head atolye-head"><div class="meta"><span>${esc(S.ders.ders)}</span><span class="pill">${ICON.okuma}Her gün biraz</span></div>
      <h2>${esc(S.atolye.baslik || "Okuma Atölyesi")}</h2></section><div class="panel" id="panel"></div>`;
    atolyeAna($("#panel"));
    S.onKonu && S.onKonu();
  }

  function atolyeAna(root) {
    const A = S.atolye, k = atolyeKayit.get();
    S.konu = "atolye"; S.botBaslik = "Okuma Atölyesi"; S.onKonu && S.onKonu();
    const kart = (sv, i) => {
      const acik = sevAcik(A, k, i), s = k.sev[sv.no] || {}, si = sonIki(s), n = sv.metinler.length;
      const durum = s.gecti ? `<span class="sev-rozet">✓ Geçtin</span>` : !acik ? `<span class="sev-rozet kilit">Kilitli</span>` : "";
      const bilgi = !acik ? `${sEk(A.seviyeler[i - 1].no, "de")} 2 tur ve ${yuzde(ATOLYE_ESIK)} doğruya ulaşınca açılır.`
        : si.tur === 0 ? "Henüz tur yok. Hadi başlayalım!"
        : `${si.tur} tur · son ${Math.min(si.tur, ATOLYE_MIN_TUR)} turda ${yuzde(si.oran)} doğru${s.gecti ? "" : si.tur < ATOLYE_MIN_TUR ? ` · bir tur daha` : si.oran < ATOLYE_ESIK ? ` · hedef ${yuzde(ATOLYE_ESIK)}` : ""}`;
      return `<div class="sev-kart${acik ? "" : " kilitli"}${s.gecti ? " gecti" : ""}">
        <div class="sev-no">S${sv.no}</div>
        <div class="sev-bilgi"><div class="sev-ad"><b>${esc(sv.ad)}</b>${durum}</div><small>${esc(sv.uzunluk)} · ${n} metin · turda ${Math.min(sv.turMetin || 3, n)} metin</small>
          ${acik && si.oran !== null ? `<div class="sev-bar" aria-hidden="true"><i style="width:${Math.round(si.oran * 100)}%"></i><b style="left:${ATOLYE_ESIK * 100}%"></b></div>` : ""}
          <span class="sev-not">${bilgi}</span></div>
        ${acik ? `<button class="btn${s.gecti ? " ghost" : " primary"}" data-sev="${i}">Tur başlat</button>` : ""}</div>`;
    };
    root.innerHTML = `<section><p class="lead">${rx(A.giris || "")}</p></section>
      <section class="facts atolye-adim"><div class="eyebrow">Okuma Dedektifi · Sor, bul, kanıtla, ele</div>
        <ol><li><b>Soru ne istiyor?</b> Soru kökünü oku. Kırmızı kelimeler olumsuz: dikkat!</li><li><b>Anahtar kelime ne?</b></li><li><b>Kanıt nerede?</b> Cevabı gösteren cümleye dokun.</li><li><b>Şıkları ele:</b> metinde yazan / metinden çıkarılabilen / metinde olmayan.</li></ol></section>
      <div class="sev-liste">${A.seviyeler.map(kart).join("")}</div>`;
    $$("[data-sev]", root).forEach(b => b.onclick = () => atolyeTur(root, +b.dataset.sev));
  }

  function atolyeTur(root, si) {
    const A = S.atolye, sv = A.seviyeler[si], k = atolyeKayit.get();
    const say = id => k.metin[id] || 0;
    const metinler = shuffle(sv.metinler).sort((a, b) => say(a.id) - say(b.id)).slice(0, sv.turMetin || 3);
    const liste = [];
    metinler.forEach((m, mi) => {
      const ust = { metin: mi, toplamMetin: metinler.length, m };
      if (m.bolumler) {
        m.bolumler.forEach((b, bi) => (b.sorular || []).forEach(q => liste.push({ ...ust, etiket: `Bölüm ${bi + 1} / ${m.bolumler.length} · durak sorusu`,
          o: { ...q, metin: b.metin, tablo: b.tablo, metinBaslik: `${m.baslik} · Bölüm ${bi + 1}` } })));
        (m.sorular || []).forEach(q => liste.push({ ...ust, etiket: "Bütün metin", o: { ...q, metin: m.bolumler.map(b => b.metin), tablo: m.tablo || (m.bolumler.find(b => b.tablo) || {}).tablo, metinBaslik: m.baslik } }));
      } else (m.sorular || []).forEach(q => liste.push({ ...ust, etiket: "", o: { ...q, metin: m.metin, tablo: m.tablo, metinBaslik: m.baslik } }));
    });
    const st = { i: 0, q: [], sonuc: [] };
    const ciz = () => {
      const it = liste[st.i], son = st.i === liste.length - 1, m = it.m;
      S.konu = "atolye:" + m.id; S.botBaslik = "Okuma Atölyesi: " + m.baslik; S.onKonu && S.onKonu();
      root.innerHTML = `<div class="stage atolye-stage"><div class="progress"><span>Soru ${st.i + 1} / ${liste.length}</span><div class="bar"><i style="width:${(st.i + 1) / liste.length * 100}%"></i></div></div>
        <div class="kicker">S${sv.no} · Metin ${it.metin + 1} / ${it.toplamMetin}${m.alan ? " · " + esc(m.alan) : ""}${it.etiket ? " · " + esc(it.etiket) : ""}</div>
        <div id="aq">${questionHTML(it.o)}</div>
        <div class="stage-nav"><button class="btn ghost" data-bitir>Turu bırak</button><button class="btn primary" data-sonraki disabled>${son ? "Sonucu gör" : "Sonraki soru"}</button></div></div>`;
      st.q[st.i] = st.q[st.i] || { wrong: [], result: undefined };
      const qs = st.q[st.i], sonraki = $("[data-sonraki]", root);
      wireQuestion($("#aq .q", root), it.o, { state: qs, kavram: ATOLYE_KV, onDone: r => { st.sonuc[st.i] = { r, kanit: qs.kanit }; sonraki.disabled = false; } });
      if (qs.result !== undefined) sonraki.disabled = false;
      sonraki.onclick = () => { tts.stop(); if (!son) { st.i++; ciz(); root.scrollIntoView({ block: "start", behavior: "smooth" }); } else bitir(); };
      $("[data-bitir]", root).onclick = () => { tts.stop(); atolyeAna(root); };
    };
    const bitir = () => {
      const kk = atolyeKayit.get(), s = kk.sev[sv.no] = kk.sev[sv.no] || { turlar: [], gecti: false };
      const d = st.sonuc.filter(x => x && x.r > 0).length, n = liste.length, c = v => st.sonuc.filter(x => x && x.r === v).length;
      const kn = st.sonuc.filter(x => x && x.kanit !== undefined), k1 = kn.filter(x => x.kanit === 1).length;
      s.turlar = [...s.turlar, { t: Date.now(), d, n }].slice(-10);
      metinler.forEach(m => kk.metin[m.id] = (kk.metin[m.id] || 0) + 1);
      const si2 = sonIki(s), yeniAcildi = !s.gecti && si2.tur >= ATOLYE_MIN_TUR && si2.oran >= ATOLYE_ESIK;
      if (yeniAcildi) s.gecti = true;
      atolyeKayit.set(kk); KAYIT.olay("atolye-tur", { seviye: sv.no, dogru: d, toplam: n });
      const sonraki = A.seviyeler[si + 1], oran = d / n;
      const mesaj = yeniAcildi ? (sonraki ? `Harika! ${sEk(sv.no, "i")} geçtin, S${sonraki.no} açıldı. Daha uzun metinlere hazırsın.` : "Harika! En uzun metinleri de geçtin. Artık gerçek bir okuma dedektifisin.")
        : oran >= ATOLYE_ESIK ? (si2.tur < ATOLYE_MIN_TUR ? "Çok iyi! Bir tur daha bu kadar dikkatli okursan sonraki seviye açılacak." : "Çok iyi! Dikkatlice okudun.")
        : "İyi çalıştın. Kanıt cümlesini bulmak zaman ister. Bir tur daha yaparsan daha kolay gelecek.";
      root.innerHTML = `<div class="stage"><div class="kicker">Okuma Atölyesi · S${sv.no} · Tur sonucu</div><h3>${yeniAcildi ? "Yeni seviye açıldı!" : oran >= ATOLYE_ESIK ? "Dikkatli okudun!" : "Tur bitti!"}</h3><p class="big">${mesaj}</p>
        <div class="done-stats"><div class="stat"><b>${c(1)}</b><span>ilk denemede doğru</span></div><div class="stat"><b>${c(2)}</b><span>ipucuyla doğru</span></div><div class="stat"><b>${c(0)}</b><span>birlikte öğrendik</span></div>${kn.length ? `<div class="stat"><b>${k1} / ${kn.length}</b><span>kanıtı ilk dokunuşta buldun</span></div>` : ""}</div>
        <p class="ek">Bu seviyede ${si2.tur} tur · son ${Math.min(si2.tur, ATOLYE_MIN_TUR)} turda ${yuzde(si2.oran)} doğru${s.gecti ? "" : ` · sonraki seviye için 2 tur ve ${yuzde(ATOLYE_ESIK)}`}.</p>
        <div class="row">${yeniAcildi && sonraki ? `<button class="btn primary" data-yeni>${sEk(sonraki.no, "i")} dene</button>` : ""}<button class="btn${yeniAcildi && sonraki ? " ghost" : " primary"}" data-tekrar>Bir tur daha</button><button class="btn ghost" data-ana>Seviyelere dön</button></div></div>`;
      $("[data-tekrar]", root).onclick = () => atolyeTur(root, si);
      $("[data-ana]", root).onclick = () => atolyeAna(root);
      const yb = $("[data-yeni]", root); if (yb) yb.onclick = () => atolyeTur(root, si + 1);
      root.scrollIntoView({ block: "start", behavior: "smooth" });
    };
    ciz();
  }

  // ---------- Kuark / ders botu ----------
  function setupBot() {
    const b = S.ders.bot; if (!b) return;
    const hist = {};
    const fab = document.createElement("button");
    fab.className = "bot-fab"; fab.innerHTML = `${b.svg}<span>${esc(b.dugme || b.ad + "'a sor")}</span>`;
    const panel = document.createElement("section");
    panel.className = "bot-panel"; panel.hidden = true; panel.setAttribute("aria-label", b.ad);
    panel.innerHTML = `<div class="bot-head">${b.svg}<div class="t"><b>${esc(b.ad)}</b><small>${esc(S.ders.ders)} robotu</small></div><button aria-label="Kapat" id="botClose">×</button></div>
      <div class="bot-note">Yapay zekâ ile çalışır (Google Gemini). Kişisel bilgi yazma. Cevaplar yanlış olabilir, kitapla kontrol et.</div>
      <div class="bot-msgs" id="botMsgs" aria-live="polite"></div>
      <div class="bot-sugg" id="botSugg"></div>
      <form class="bot-form" id="botForm"><input id="botIn" maxlength="500" autocomplete="off" placeholder="Sorunu yaz…"><button class="btn primary" type="submit">Sor</button></form>`;
    document.body.append(fab, panel);

    const msgs = $("#botMsgs"), input = $("#botIn");
    const add = (cls, text) => { const m = document.createElement("div"); m.className = "msg " + cls; m.textContent = text; msgs.appendChild(m); msgs.scrollTop = msgs.scrollHeight; return m; };
    const drawHist = () => {
      msgs.innerHTML = ""; const h = hist[S.konu] || [];
      add("bot", b.karsilama.replace("{konu}", S.data ? S.data.baslik : S.botBaslik || ""));
      h.forEach(x => add(x.rol === "user" ? "me" : "bot", x.metin));
      $("#botSugg").innerHTML = (b.oneriler || []).map(s => `<button type="button">${esc(s)}</button>`).join("");
    };
    const open = () => {
      if (!store.get("ela7:bot-onay", false)) return consent(open);
      panel.hidden = false; fab.hidden = true; drawHist(); input.focus();
    };
    const close = () => { panel.hidden = true; fab.hidden = false; };
    fab.onclick = open; $("#botClose").onclick = close;
    $("#botSugg").onclick = e => { const s = e.target.closest("button"); if (s) send(s.textContent); };
    $("#botForm").onsubmit = e => { e.preventDefault(); const t = input.value.trim(); if (t) send(t); };
    S.onKonu = () => { if (!panel.hidden) drawHist(); };
    // Robot koçun "Birlikte bakalım" düğmesi: paneli açar ve soruyu bağlamıyla gönderir
    S.botSor = text => { const go = () => { KOC.kapat(); panel.hidden = false; fab.hidden = true; drawHist(); send(text); }; if (!store.get("ela7:bot-onay", false)) return consent(go); go(); };

    let busy = false;
    async function send(text) {
      if (busy) return; busy = true; input.value = "";
      const h = hist[S.konu] = hist[S.konu] || [];
      h.push({ rol: "user", metin: text }); add("me", text); KAYIT.olay("robot-soru", { metin: kisa(text, 80) });
      const w = add("bot wait", `${b.ad} düşünüyor…`);
      try {
        const r = await fetch("/api/sor", { method: "POST", headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ ders: S.ders.kod, konu: S.konu, mesajlar: h.slice(-8) }) });
        const j = await r.json().catch(() => ({}));
        w.remove();
        if (!r.ok || !j.cevap) throw new Error(j.hata || "hata");
        h.push({ rol: "bot", metin: j.cevap }); add("bot", j.cevap);
      } catch (err) {
        w.remove(); h.pop();
        add("bot err", err.message && err.message !== "hata" ? err.message : `${b.ad} şu an cevap veremiyor. Biraz sonra tekrar dene. Bu arada "Konuya Bak" bölümündeki Merak Kutusu'na bakabilirsin.`);
      }
      busy = false;
    }
    function consent(then) {
      const m = document.createElement("div"); m.className = "modal";
      m.innerHTML = `<div class="modal-box" role="dialog" aria-modal="true"><h3>${esc(b.ad)} ile konuşmadan önce</h3>
        <ul><li>${esc(b.ad)} bir yapay zekâ robotudur, insan değildir.</li>
        <li>Google Gemini ile çalışır. Yazdıkların Google tarafından ürünlerini geliştirmek için kullanılabilir ve Google çalışanları tarafından okunabilir.</li>
        <li>Adını, soyadını, adresini, telefonunu, okulunu ve şifreni yazma.</li>
        <li>Sadece ${esc(S.ders.ders)} dersiyle ilgili sorulara cevap verir. Cevaplar bazen yanlış olabilir, kitabınla kontrol et.</li></ul>
        <div class="row"><button class="btn primary" id="okBot">Anladım</button><button class="btn ghost" id="noBot">Vazgeç</button></div></div>`;
      document.body.appendChild(m);
      $("#okBot", m).onclick = () => { store.set("ela7:bot-onay", true); m.remove(); then(); };
      $("#noBot", m).onclick = () => m.remove();
      $("#okBot", m).focus();
    }
  }

  // =================================================================
  // ---------- Veli raporu (#rapor, PIN'li) — geçici rapor; ileride Veli Paneli'ne taşınacak ----------
  // Son 7 günün oturumları, gün özeti, zorlanılan sorular, ayarlar ve yedek (indir / geri yükle / CSV).
  // =================================================================
  const sha = async t => { try { const b = await crypto.subtle.digest("SHA-256", new TextEncoder().encode("ela7:" + t)); return [...new Uint8Array(b)].map(x => x.toString(16).padStart(2, "0")).join(""); } catch (e) { return "x" + t; } };
  const DERS_AD = { tr1: "Türkçe", mat1: "Matematik", fen1: "Fen Bilimleri", ing1: "İngilizce (MEB)", own1: "İngilizce (Own It)", sos1: "Sosyal Bilgiler" };
  const dersAd = k => DERS_AD[k] || k || "—";
  const saat = ts => { const d = new Date(ts); return `${p2(d.getHours())}:${p2(d.getMinutes())}`; };
  const GUNLER = ["Pazar", "Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi"];
  const gunAdi = ts => { const d = new Date(ts); return `${d.getDate()} ${AYLAR[d.getMonth()]} ${GUNLER[d.getDay()]}`; };
  const dk = ms => Math.round(ms / 60000);

  // Olaylardan oturum özetleri (yedek dosyasına da yazılır)
  function ozetle(olaylar) {
    const m = new Map();
    olaylar.forEach(o => {
      let z = m.get(o.oturum);
      if (!z) m.set(o.oturum, z = { oturum: o.oturum, cihaz: o.cihaz, bas: o.ts, bit: o.ts, aktifMs: 0, dersler: {}, soru: 0, ilk1: 0, ilk2: 0, ilk0: 0, ipucu: 0, hizli: 0, hizliYanlis: 0, rastgele: 0, hizliGecis: 0, atlama: 0, robot: 0, robotSoru: 0, nasil: {}, testler: [], _son: o.ts });
      const ara = o.ts - z._son; if (ara > 0) z.aktifMs += Math.min(ara, BOSLUK_TAVAN); z._son = o.ts; z.bit = o.ts;
      if (o.ders && o.olay !== "rapor-ac") { const dd = z.dersler[o.ders] = z.dersler[o.ders] || {}; if (o.konuBaslik) dd[o.konuBaslik] = (dd[o.konuBaslik] || 0) + 1; }
      if (o.olay === "soru") { z.soru++; z["ilk" + o.sonuc]++; if (o.ipucu) z.ipucu++; if ((o.bayrak || []).includes("hizli")) { z.hizli++; if (o.sonuc !== 1) z.hizliYanlis++; } }
      if (o.olay === "oyun-rastgele") z.rastgele++;
      if (o.olay === "adim" && (o.bayrak || []).includes("hizli-gecis")) z.hizliGecis++;
      if (o.olay === "atlama") z.atlama++;
      if (o.olay === "robot") z.robot++;
      if (o.olay === "robot-soru") z.robotSoru++;
      if (o.olay === "robot-cevap" && o.mesaj === "nasil") z.nasil[o.secim] = (z.nasil[o.secim] || 0) + 1;
      if (o.olay === "test-bitti") z.testler.push({ ders: o.ders, konu: o.konuBaslik, tur: o.tur, ilk1: o.ilk1, toplam: o.toplam, sureDk: o.sureDk });
    });
    return [...m.values()].map(z => { const { _son, ...r } = z; return { ...r, basT: yerelZaman(z.bas), aktifDk: dk(z.aktifMs) }; });
  }

  const indir = (ad, icerik, tip) => { const a = document.createElement("a"); a.href = URL.createObjectURL(new Blob([icerik], { type: tip })); a.download = ad; document.body.appendChild(a); a.click(); setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 500); };
  const CSV_ALAN = ["t", "ders", "konu", "konuBaslik", "bolum", "olay", "soru", "tur", "sonuc", "sureSn", "ilkSn", "esikSn", "ipucu", "yanlis", "kanit", "tekrar", "bayrak", "kavram", "adim", "adimTur", "oyun", "yanlis", "mesaj", "secim", "metin", "ilk1", "ilk2", "ilk0", "toplam", "oturum", "cihaz"];
  async function yedekIndir() {
    KAYIT.bosalt(); await new Promise(r => setTimeout(r, 300));
    const olaylar = await KDB.hepsi(), ilerleme = {};
    try { for (let i = 0; i < localStorage.length; i++) { const k = localStorage.key(i); if (k.startsWith("ela7:") && k !== "ela7:pin") ilerleme[k] = localStorage.getItem(k); } } catch (e) {}
    const veri = { tur: "ela7dersleri-yedek", v: KAYIT_V, olusturma: yerelZaman(simdi()), kaynak: location.origin, cihaz: cihazId,
      okuma: "Claude için: önce 'sozluk'u oku. 'oturumlar' her çalışma oturumunun özeti, 'olaylar' ayrıntılı kayıt, 'ilerleme' sitenin cihazda tuttuğu durum (geri yükleme için).",
      sozluk: KAYIT_SOZLUK, oturumlar: ozetle(olaylar), olaylar, ilerleme };
    indir(`ela7-yedek-${gun()}.json`, JSON.stringify(veri, null, 1), "application/json");
  }
  async function csvIndir() {
    KAYIT.bosalt(); await new Promise(r => setTimeout(r, 300));
    const alan = [...new Set(CSV_ALAN)], h = v => { const t = Array.isArray(v) ? v.join(" | ") : v ?? ""; return /[;"\n]/.test(String(t)) ? `"${String(t).replace(/"/g, '""')}"` : String(t); };
    const satir = (await KDB.hepsi()).map(o => alan.map(a => h(o[a])).join(";"));
    indir(`ela7-kayit-${gun()}.csv`, "﻿" + [alan.join(";"), ...satir].join("\r\n"), "text/csv");
  }
  async function yedekYukle(dosya, durum) {
    try {
      const v = JSON.parse(await dosya.text());
      if (v.tur !== "ela7dersleri-yedek") throw new Error("Bu dosya bir Ela'nın Defteri yedeği değil.");
      if (!confirm(`${v.olusturma} tarihli yedek yüklenecek. Bu cihazdaki ilerleme yedektekiyle değiştirilecek, kayıtlar birleştirilecek. Devam edilsin mi?`)) return;
      Object.entries(v.ilerleme || {}).forEach(([k, x]) => { try { localStorage.setItem(k, x); } catch (e) {} });
      const var_ = new Set((await KDB.hepsi()).map(o => o.k));
      await KDB.yaz((v.olaylar || []).filter(o => o && o.k && !var_.has(o.k)));
      durum.textContent = "Yedek yüklendi. Sayfa yenileniyor…"; setTimeout(() => location.reload(), 900);
    } catch (e) { durum.textContent = "Yüklenemedi: " + (e.message || "dosya okunamadı"); }
  }

  async function openRapor() {
    tts.stop(); KOC.kapat(); S.konu = "rapor"; S.data = null; S.durakAsil = null; S.tab = "rapor"; renderNav();
    const c = $("#content");
    const pin = store.get("ela7:pin", null);
    const acik = (() => { try { return sessionStorage.getItem("ela7:pin-ok") === pin && !!pin; } catch (e) { return false; } })();
    if (!acik) {
      c.innerHTML = `<section class="konu-head"><div class="meta"><span>Veli</span></div><h2>Veli raporu</h2></section>
        <div class="stage rp-pin"><p class="big">${pin ? "Veli PIN'ini yaz." : "Bu cihaz için bir veli PIN'i belirle (4–8 rakam). Ela bu ekranı ve ayarları PIN olmadan açamaz."}</p>
        <form id="pinF" class="row"><input id="pin1" type="password" inputmode="numeric" pattern="[0-9]{4,8}" maxlength="8" placeholder="PIN" autocomplete="off" required>
        ${pin ? "" : `<input id="pin2" type="password" inputmode="numeric" pattern="[0-9]{4,8}" maxlength="8" placeholder="PIN tekrar" autocomplete="off" required>`}
        <button class="btn primary">${pin ? "Aç" : "Belirle ve aç"}</button></form><p class="ek" id="pinMsg"></p></div>`;
      $("#pinF").onsubmit = async e => {
        e.preventDefault(); const a = $("#pin1").value, b = $("#pin2") ? $("#pin2").value : a;
        if (!/^\d{4,8}$/.test(a)) return $("#pinMsg").textContent = "PIN 4–8 rakam olmalı.";
        if (a !== b) return $("#pinMsg").textContent = "İki PIN aynı değil.";
        const hs = await sha(a);
        if (pin && hs !== pin) return $("#pinMsg").textContent = "PIN yanlış.";
        if (!pin) store.set("ela7:pin", hs);
        try { sessionStorage.setItem("ela7:pin-ok", hs); } catch (e) {}
        openRapor();
      };
      $("#pin1").focus(); return;
    }
    KAYIT.olay("rapor-ac"); KAYIT.bosalt(); await new Promise(r => setTimeout(r, 250));
    const olaylar = (await KDB.hepsi()).filter(o => o.olay !== "rapor-ac"), sinir = simdi() - 7 * 864e5;
    const son7 = olaylar.filter(o => o.ts >= sinir), otur = ozetle(son7).sort((a, b) => b.bas - a.bas);
    const gunler = new Map(); otur.forEach(z => { const g = yerelZaman(z.bas).slice(0, 10); const x = gunler.get(g) || { ts: z.bas, aktifDk: 0, soru: 0, ilk1: 0, hizli: 0, rastgele: 0, hizliGecis: 0, atlama: 0, dersler: new Set() }; x.aktifDk += z.aktifDk; ["soru", "ilk1", "hizli", "rastgele", "hizliGecis", "atlama"].forEach(f => x[f] += z[f]); Object.keys(z.dersler).forEach(d_ => x.dersler.add(dersAd(d_))); gunler.set(g, x); });
    const yuz = (a, b) => b ? `%${Math.round(a / b * 100)}` : "—";
    const bay = (n, t) => n ? `<span class="rp-bay" title="${esc(t)}">${n}</span>` : `<span class="rp-sifir">0</span>`;
    const zor = son7.filter(o => o.olay === "soru" && o.sonuc === 0).slice(-15).reverse();
    const ay = ayar();
    const olaySatir = o => {
      const ne = o.olay === "soru" ? `Soru ${o.sonuc === 1 ? "✓" : o.sonuc === 2 ? "~" : "✗"} ${esc(o.soru || "")} <small>${o.ilkSn ?? ""} sn${o.ipucu ? ` · ipucu ${o.ipucu}` : ""}${(o.bayrak || []).length ? ` · <b class="rp-k">${o.bayrak.join(", ")}</b>` : ""}${o.tekrar ? " · tekrar" : ""}</small>`
        : o.olay === "adim" ? `Öğren adım ${o.adim}/${o.toplam} (${esc(o.adimTur)}${o.kavram ? ": " + esc(o.kavram) : ""}) <small>${o.sureSn} sn${(o.bayrak || []).length ? ` · <b class="rp-k">hızlı geçiş</b>` : ""}</small>`
        : o.olay === "sekme" ? `Sekme: ${esc(o.bolum)}` : o.olay === "konu-ac" ? `<b>Konu açıldı: ${esc(o.konuBaslik)}</b>`
        : o.olay === "robot" ? `🤖 Robot: ${esc(o.metin || o.mesaj)}` : o.olay === "robot-cevap" ? `🤖 Ela'nın seçimi: “${esc(o.secim)}”` : o.olay === "robot-soru" ? `💬 Robota sordu: ${esc(o.metin)}`
        : o.olay === "test-bitti" ? `<b>${o.tur === "tarama" ? "Tarama" : "Test"} bitti: ${o.ilk1}/${o.toplam} ilk denemede, ${o.sureDk} dk</b>` : o.olay === "test-basla" ? `${o.tur === "tarama" ? "Tarama" : "Test"} başladı (${o.toplam} soru)`
        : o.olay === "oyun" ? `Oyun bitti: ${esc(o.oyun)}${o.yanlis !== undefined ? ` · ${o.yanlis} yanlış dokunuş` : ""}${o.sureSn ? ` · ${o.sureSn} sn` : ""}` : o.olay === "oyun-ac" ? `Oyun: ${esc(o.oyun)}`
        : o.olay === "oyun-rastgele" ? `<b class="rp-k">Rastgele dokunuş (${esc(o.oyun)})</b>` : o.olay === "atlama" ? `<b class="rp-k">Öğren bitmeden Test'e geçti</b>`
        : o.olay === "ogren-bitti" ? `<b>Öğren bitti</b>` : o.olay === "atolye-tur" ? `Okuma Atölyesi S${o.seviye}: ${o.dogru}/${o.toplam}` : esc(o.olay);
      return `<li><time>${saat(o.ts)}</time><span class="rp-d">${esc(dersAd(o.ders))}</span><span>${ne}</span></li>`;
    };
    c.innerHTML = `<section class="konu-head"><div class="meta"><span>Veli</span><span class="pill">Son 7 gün · bu cihaz</span></div><h2>Veli raporu</h2></section>
      <section><div class="sec-title"><h3>Günler</h3><span>Aktif süre: olaylar arası boşluklar (en çok 3 dk) toplanır</span></div>
      ${gunler.size ? `<div class="rp-tablo-wrap"><table class="rp-tablo"><thead><tr><th>Gün</th><th>Aktif</th><th>Dersler</th><th>Soru</th><th>İlk denemede</th><th>Hızlı cevap</th><th>Rastgele dokunuş</th><th>Hızlı kart geçişi</th><th>Öğren'i atladı</th></tr></thead><tbody>
        ${[...gunler.values()].map(x => `<tr><td>${gunAdi(x.ts)}</td><td>${x.aktifDk} dk</td><td>${[...x.dersler].map(esc).join(", ")}</td><td>${x.soru}</td><td>${yuz(x.ilk1, x.soru)}</td><td>${bay(x.hizli, "Okuma süresinden kısa cevap")}</td><td>${bay(x.rastgele, "Oyunda art arda hızlı yanlış")}</td><td>${bay(x.hizliGecis, "Öğren kartını okumadan geçti")}</td><td>${bay(x.atlama, "Öğren bitmeden Test")}</td></tr>`).join("")}
      </tbody></table></div>` : `<div class="notice">Son 7 günde bu cihazda kayıt yok. Kayıt bu güncellemeyle başladı.</div>`}</section>
      ${otur.length ? `<section><div class="sec-title"><h3>Oturumlar</h3><span>Ayrıntı için oturuma dokun</span></div><div class="rp-otur">
        ${otur.map(z => { const ev = son7.filter(o => o.oturum === z.oturum); const nas = Object.entries(z.nasil).map(([k, v]) => `${esc(k)}: ${v}`).join(", ");
          return `<details><summary><b>${gunAdi(z.bas)} · ${saat(z.bas)}–${saat(z.bit)}</b> <span>${z.aktifDk} dk aktif · ${Object.keys(z.dersler).map(dersAd).map(esc).join(", ")} · ${z.soru} soru, ${yuz(z.ilk1, z.soru)} ilk denemede${z.hizli ? ` · <b class="rp-k">${z.hizli} hızlı cevap</b>` : ""}${z.rastgele ? ` · <b class="rp-k">${z.rastgele} rastgele</b>` : ""}</span></summary>
            <div class="rp-ic">${Object.entries(z.dersler).map(([d_, ks]) => `<p><b>${esc(dersAd(d_))}:</b> ${Object.keys(ks).map(esc).join(" · ")}</p>`).join("")}
            ${z.testler.length ? `<p><b>Testler:</b> ${z.testler.map(t => `${esc(t.konu)} ${t.ilk1}/${t.toplam}`).join(" · ")}</p>` : ""}
            ${nas ? `<p><b>“Nasıl buldun?” cevapları:</b> ${nas}</p>` : ""}${z.robotSoru ? `<p><b>Robota ${z.robotSoru} soru sordu.</b></p>` : ""}
            <ol class="rp-olay">${ev.filter(o => o.olay !== "sekme" || ev.length < 150).map(olaySatir).join("")}</ol></div></details>`; }).join("")}</div></section>` : ""}
      ${zor.length ? `<section><div class="sec-title"><h3>Cevabı gösterilen sorular</h3><span>Son 7 gün · iki yanlıştan sonra</span></div><ul class="rp-zor">${zor.map(o => `<li><span class="rp-d">${esc(dersAd(o.ders))} · ${esc(o.konuBaslik)}</span>${esc(o.soru)}${o.yanlis && o.yanlis.length ? `<small>Seçtiği: ${o.yanlis.map(esc).join(" → ")}</small>` : ""}</li>`).join("")}</ul></section>` : ""}
      <section><div class="sec-title"><h3>Ayarlar</h3><span>Bu cihaz için</span></div><div class="rp-ayar">
        ${[["robotUyari", "Robot uyarıları ve yönlendirmeleri", "Hız uyarısı, “Dur, düşün”, Öğren'i atlama yönlendirmesi, “Nasıl buldun?”, oturum başı planı ve özet."],
           ["sikBekle", "Şıklar biraz beklesin", "Seçmeli sorularda şıklar, soru okunacak kadar (en çok 5 sn) sonra açılır."],
           ["oyunKilit", "Oyunda düşünme molası", "Art arda hızlı yanlış dokunuşta oyun 3 saniye durur."],
           ["ogrenKilit", "Öğren bitmeden Test kilitli", "Test sekmesi, Öğren'in son adımına gelinince açılır."]].map(([k, a, t]) => `<label class="rp-sw"><input type="checkbox" data-ayar="${k}" ${ay[k] ? "checked" : ""}><span><b>${a}</b><small>${t}</small></span></label>`).join("")}
      </div></section>
      <section><div class="sec-title"><h3>Yedek</h3><span>Taslak siteden canlı siteye ya da başka cihaza geçerken</span></div>
        <p class="ek">Taslak ve canlı site tarayıcı için ayrı sitelerdir; ilerleme kendiliğinden taşınmaz. Burada yedeği indir, diğer sitede bu ekrandan geri yükle. Yedek dosyası Claude'a da verilebilir (alan sözlüğü içinde).</p>
        <div class="row"><button class="btn primary" id="rpYedek">Yedeği indir (JSON)</button><button class="btn" id="rpCsv">Kayıtları indir (Excel / CSV)</button>
        <label class="btn ghost rp-dosya">Yedekten geri yükle<input type="file" id="rpYukle" accept=".json,application/json" hidden></label></div><p class="ek" id="rpDurum"></p></section>
      <section><div class="row"><button class="btn ghost" id="rpPin">PIN'i değiştir</button><button class="btn ghost" id="rpKilit">Raporu kilitle</button></div>
        <p class="src">Toplam kayıt: ${olaylar.length} olay · cihaz ${esc(cihazId)} · kayıtlar bu tarayıcıda ${KAYIT_GUN} gün tutulur.</p></section>`;
    $$("[data-ayar]", c).forEach(x => x.onchange = () => { const a = store.get("ela7:ayar", {}) || {}; a[x.dataset.ayar] = x.checked; store.set("ela7:ayar", a); });
    $("#rpYedek").onclick = yedekIndir; $("#rpCsv").onclick = csvIndir;
    $("#rpYukle").onchange = e => { const f = e.target.files[0]; if (f) yedekYukle(f, $("#rpDurum")); };
    $("#rpPin").onclick = () => { store.set("ela7:pin", null); try { sessionStorage.removeItem("ela7:pin-ok"); } catch (e) {} openRapor(); };
    $("#rpKilit").onclick = () => { try { sessionStorage.removeItem("ela7:pin-ok"); } catch (e) {} openRapor(); };
  }

  // ---------- Sayfa iskeleti ----------
  function allTopics() { return S.ders.uniteler.flatMap((u, ui) => u.konular.map((k, ki) => ({ ...k, ui, ki }))); }

  function renderNav() {
    $("#units").innerHTML = S.ders.uniteler.map((u, i) => `<button class="unit-btn" data-u="${i}" aria-pressed="${i === S.unit}">${esc(u.ad)}</button>`).join("");
    const u = S.ders.uniteler[S.unit];
    let no = 0;
    $("#topics").innerHTML = u.konular.length ? u.konular.map(k => { const dk = isDurak(k); if (!dk) no++;
      const ek = !k.hazir ? '<span class="soon">yakında</span>' : dk && durakKayit.zaman(k.id) ? '<span class="due">tekrar zamanı</span>' : "";
      return `<button class="topic${dk ? " durak" : ""}" data-id="${esc(k.id)}" ${k.hazir ? "" : "disabled"} aria-current="${S.konu === k.id}">
      <span class="num">${dk ? ICON.durak : no}</span><span>${esc(k.baslik)}</span>${ek}</button>`; }).join("")
      : `<div class="empty-unit">Bu ünitenin konuları sırası gelince eklenecek.</div>`;
    const cur = $(".topic[aria-current='true']"); if (cur) cur.scrollIntoView({ block: "nearest", inline: "nearest" });
  }

  function setTab(t) {
    const once = S.tab;
    tts.stop(); S.tab = t; store.set(key("sekme:" + S.konu), t); // sekme her konu için ayrı hatırlanır
    if (once !== t || !S.sekmeKayit) KAYIT.olay("sekme"); S.sekmeKayit = true;
    // Öğren bitmeden Test'e geçildiyse robot kibarca yönlendirir (veli ayarı "ogrenKilit" açıksa Test zaten kilitli)
    if (t === "test" && S.data && !isDurak(S.data) && !ogrenBitti(S.konu) && !document.body.classList.contains("sinif")) {
      KAYIT.olay("atlama");
      if (!ayar().ogrenKilit) KOC.goster("atlama", "Öğren bölümünde henüz görmediğin kartlar var. Önce onlara bakalım mı? Kartları gördükten sonra test çok daha kolay gelir.",
        [{ etiket: "Öğren'e dön", birincil: true, fn: () => setTab("ogren") }, { etiket: "Teste devam" }]);
    }
    if (S.durakAsil) S.data = t === "oyunlar" ? durakOyunVerisi(S.durakAsil) : S.durakAsil;   // Ara Durak oyunları birleşik veriyle çalışır
    $$(".tab").forEach(b => b.setAttribute("aria-selected", b.dataset.tab === t));
    const p = $("#panel");
    ({ ogren: renderOgren, bak: renderBak, tekrar: renderTekrar, test: renderTest, okuma: renderOkuma, hatirla: renderHatirla, tarama: renderTarama, oyunlar: renderTekrar })[t](p);
  }

  function renderKonu(no) {
    const d = S.data; S.durakAsil = null;
    const donus = S.donus && allTopics().find(k => k.id === S.donus && isDurak(k));
    const vade = !donus && allTopics().find(k => isDurak(k) && k.hazir && durakKayit.zaman(k.id));
    $("#content").innerHTML = `<section class="konu-head"><div class="meta"><span>${esc(d.unite)}</span><span class="pill">Konu ${no}</span><span class="pill">${esc(d.sayfalar)}</span>${donus ? `<button class="btn ghost dk-don" data-donus>← Ara Durak'a dön</button>` : ""}</div>
      ${vade ? `<div class="dk-vade">${ICON.tekrar}<span><b>${esc(vade.baslik)}</b> için tekrar zamanı geldi.</span><button class="btn" data-vade="${esc(vade.id)}">Aç</button></div>` : ""}
      <h2>${esc(d.baslik)}</h2>
      <div class="tabs" role="tablist">
        <button class="tab" role="tab" data-tab="ogren">${ICON.ogren}Öğren</button>
        <button class="tab" role="tab" data-tab="bak">${ICON.bak}Konuya Bak</button>
        <button class="tab" role="tab" data-tab="tekrar">${ICON.tekrar}Tekrar</button>
        <button class="tab" role="tab" data-tab="test">${ICON.test}Test</button>${d.okuma ? `<button class="tab" role="tab" data-tab="okuma">${ICON.okuma}Oku ve Dinle</button>` : ""}</div></section>
      <div class="panel" id="panel"></div>`;
    $$(".tab").forEach(b => b.onclick = () => setTab(b.dataset.tab));
    const db = $("[data-donus]"); if (db) db.onclick = () => { const id = S.donus; S.donus = null; openKonu(id, true); };
    const vb = $("[data-vade]"); if (vb) vb.onclick = () => openKonu(vb.dataset.vade, true);
    let sk = store.get(key("sekme:" + S.konu), "ogren"); if (sk === "okuma" && !d.okuma) sk = "ogren";
    setTab(sk); // hiç açılmamış konu Öğren'den başlar
    S.onKonu && S.onKonu();
  }

  async function openKonu(id, scroll) {
    const t = allTopics().find(k => k.id === id && k.hazir); if (!t) return;
    S.konu = id; S.unit = t.ui; S.botBaslik = null; renderNav(); store.set(key("son"), id);
    $$(".head-actions a[href='#atolye']").forEach(a => a.removeAttribute("aria-pressed"));
    if (location.hash.slice(1) !== id) history.replaceState(null, "", "#" + id);
    try {
      if (!S.cache[id]) { const r = await fetch("konular/" + id + ".json", { cache: "no-cache" }); if (!r.ok) throw 0; S.cache[id] = await r.json(); }
      S.data = S.cache[id];
      KAYIT.olay("konu-ac"); S.sekmeKayit = false;
      if (isDurak(S.data)) { S.donus = null; await yukleKonular(S.data.kapsar || []); if (S.konu !== id) return; renderDurak(); }
      else renderKonu(konuNoOf(id));
      if (isEn() && !isDurak(S.data)) { store.set(key("acildi:" + id), true); srs.add(wordsOf(S.data)); }
      if (scroll) $("#content").scrollIntoView({ behavior: "smooth", block: "start" });
    } catch (e) { $("#content").innerHTML = `<div class="notice">Bu konu açılamadı. İnternet bağlantını kontrol edip sayfayı yenile.</div>`; }
  }

  // Ünite seçimi: açık konu bu ünitedeyse dokunma; ünitede hazır konu varsa ilkini aç; yoksa "Yakında" göster.
  function openUnit(ui) {
    S.unit = ui; renderNav();
    const cur = allTopics().find(k => k.id === S.konu);
    if (cur && cur.ui === ui) { if (!S.data) openKonu(cur.id, false); return; }
    const ready = S.ders.uniteler[ui].konular.find(k => k.hazir);
    if (ready) { openKonu(ready.id, false); return; }
    tts.stop(); S.data = null;
    const u = S.ders.uniteler[ui];
    const liste = u.konular.length
      ? `<ol class="yakinda-liste">${u.konular.map(k => `<li>${esc(k.baslik)}</li>`).join("")}</ol>` : "";
    $("#content").innerHTML = `<section class="konu-head"><div class="meta"><span>${esc(u.ad)}</span><span class="pill">Yakında</span></div>
      <h2>Bu ünite yakında geliyor</h2></section>
      <div class="notice"><p>Bu ünitenin konuları hazırlanıyor. Hazır olan konular, konu listesinden açılabilir hâle gelecek.</p>
      ${liste ? `<p>Bu ünitede öğreneceklerimiz:</p>${liste}` : ""}</div>`;
  }

  // Başlık bandı deseni: varsayılan yıldızlar; ders.json "tema.desen" ile değişir (ör. "harita").
  const DESEN = {
    yildiz(g, w, h, rnd) {
      for (let i = 0; i < Math.round(w / 6); i++) { g.globalAlpha = .35 + rnd() * .6; g.fillStyle = "#fff"; g.beginPath(); g.arc(rnd() * w, rnd() * h, rnd() * 1.4 + .3, 0, 7); g.fill(); }
    },
    // İngilizce (MEB) — "Airmail": süzülen konuşma balonları
    balon(g, w, h, rnd) {
      const sozler = ["Hello!", "Hi!", "?", "Yes!", "ABC", "Wow!", "OK", "Bye!", "!", "Aa"];
      const n = Math.max(5, Math.round(w / 150)), x0 = w > 700 ? w * .36 : 0;
      for (let i = 0; i < n; i++) {
        const x = x0 + (i + .15 + rnd() * .7) * (w - x0) / n, y = h * (.18 + rnd() * .62), s = .7 + rnd() * .7, t = sozler[Math.floor(rnd() * sozler.length)];
        g.save(); g.translate(x, y); g.rotate((rnd() - .5) * .35); g.scale(s, s);
        g.font = "800 15px 'Fredoka', 'Baloo 2', sans-serif"; const tw = g.measureText(t).width, bw = tw + 22, bh = 30;
        g.globalAlpha = .09 + rnd() * .1; g.fillStyle = "#fff"; g.beginPath();
        if (g.roundRect) g.roundRect(-bw / 2, -bh / 2, bw, bh, 14); else g.rect(-bw / 2, -bh / 2, bw, bh);
        g.moveTo(-6, bh / 2 - 1); g.lineTo(-12, bh / 2 + 9); g.lineTo(2, bh / 2 - 1); g.fill();
        g.globalAlpha = Math.min(.5, g.globalAlpha * 2.4); g.fillStyle = i % 3 === 0 ? "#ff8a7a" : "#bfe0ff"; g.textAlign = "center"; g.textBaseline = "middle"; g.fillText(t, 0, 1);
        g.restore();
      }
      for (let i = 0; i < Math.round(w / 40); i++) { g.globalAlpha = .2 + rnd() * .35; g.fillStyle = "#fff"; g.beginPath(); g.arc(rnd() * w, rnd() * h, rnd() * 1.2 + .3, 0, 7); g.fill(); }
    },
    // İngilizce (Own It) — "Explorer notebook": ünite kelimeleri, yıldız ve ok karalamaları
    kelime(g, w, h, rnd) {
      const kel = ["inspire", "art", "words", "healthy", "planet", "create", "celebrate", "school", "travel", "brave", "music", "idea", "explore", "smile"];
      const n = Math.max(6, Math.round(w / 120));
      for (let i = 0; i < n; i++) {
        const x0 = w > 700 ? w * .36 : 0, x = x0 + (i + .1 + rnd() * .8) * (w - x0) / n, y = h * (.2 + rnd() * .65), sz = 13 + rnd() * 16; // geniş ekranda başlığın sağında
        g.save(); g.translate(x, y); g.rotate((rnd() - .5) * .5);
        g.globalAlpha = .1 + rnd() * .14; g.fillStyle = i % 4 === 0 ? "#ffd166" : "#e9e0ff";
        g.font = `700 ${sz}px 'Fredoka', 'Baloo 2', sans-serif`; g.textAlign = "center"; g.fillText(kel[Math.floor(rnd() * kel.length)], 0, 0);
        g.restore();
      }
      g.strokeStyle = "rgba(255,209,102,.35)"; g.lineWidth = 2; g.lineCap = "round"; g.lineJoin = "round";
      for (let i = 0; i < Math.max(2, Math.round(w / 420)); i++) {   // yıldız karalaması
        const cx = rnd() * w, cy = h * (.2 + rnd() * .6), r = 7 + rnd() * 6; g.beginPath();
        for (let k = 0; k <= 10; k++) { const a = -Math.PI / 2 + k * Math.PI / 5, rr = k % 2 ? r * .45 : r; g.lineTo(cx + rr * Math.cos(a), cy + rr * Math.sin(a)); }
        g.stroke();
      }
      g.strokeStyle = "rgba(233,224,255,.22)";                          // kıvrımlı ok
      const y0 = h * .78; g.beginPath(); g.moveTo(w * .05, y0); g.bezierCurveTo(w * .25, y0 - 30, w * .4, y0 + 25, w * .58, y0 - 8); g.stroke();
      g.beginPath(); g.moveTo(w * .58 - 10, y0 - 14); g.lineTo(w * .58, y0 - 8); g.lineTo(w * .58 - 9, y0 + 2); g.stroke();
    },
    // Matematik — "Kareli defter": ince kare ızgara, süzülen sayılar/işaretler, altta sayı doğrusu
    sayi(g, w, h, rnd) {
      g.strokeStyle = "rgba(255,255,255,.06)"; g.lineWidth = 1;
      for (let x = 0; x < w; x += 22) { g.beginPath(); g.moveTo(x + .5, 0); g.lineTo(x + .5, h); g.stroke(); }
      for (let y = 0; y < h; y += 22) { g.beginPath(); g.moveTo(0, y + .5); g.lineTo(w, y + .5); g.stroke(); }
      const ks = ["−3", "+5", "0", "½", "−1", "+2", "¾", "−7", "×", "÷", "=", "+", "−", "|−4|", "0,5", "<", ">"];
      const x0 = w > 700 ? w * .38 : 0, n = Math.max(5, Math.round((w - x0) / 95));
      for (let i = 0; i < n; i++) {
        const x = x0 + (i + .15 + rnd() * .7) * (w - x0) / n, y = h * (.18 + rnd() * .5), sz = 16 + rnd() * 18, t = ks[Math.floor(rnd() * ks.length)];
        g.save(); g.translate(x, y); g.rotate((rnd() - .5) * .3);
        g.globalAlpha = .14 + rnd() * .16; g.fillStyle = t.startsWith("−") ? "#9fd8ff" : t.startsWith("+") ? "#ffb48a" : i % 3 ? "#ffffff" : "#ffd166";
        g.font = `700 ${sz}px 'Lexend', 'Baloo 2', sans-serif`; g.textAlign = "center"; g.fillText(t, 0, 0); g.restore();
      }
      const ly = h - 16, x1 = w > 700 ? w * .4 : w * .06, x2 = w - 20, adim = 34;   // sayı doğrusu
      g.globalAlpha = .45; g.strokeStyle = "#ffffff"; g.lineWidth = 2; g.beginPath(); g.moveTo(x1, ly); g.lineTo(x2, ly); g.stroke();
      const orta = Math.round(((x1 + x2) / 2 - x1) / adim) * adim + x1;
      for (let x = orta, k = 0; x > x1 + 4; x -= adim, k++) { g.beginPath(); g.moveTo(x, ly - 5); g.lineTo(x, ly + 5); g.strokeStyle = k ? "rgba(159,216,255,.85)" : "#fff"; g.stroke(); }
      for (let x = orta + adim; x < x2 - 4; x += adim) { g.beginPath(); g.moveTo(x, ly - 5); g.lineTo(x, ly + 5); g.strokeStyle = "rgba(255,180,138,.85)"; g.stroke(); }
      g.globalAlpha = 1;
    },
    // Türkçe — "Bal kovanı defteri": süzülen harfler ve noktalama işaretleri, petek altıgenleri, kesikli arı uçuşu
    harf(g, w, h, rnd) {
      const ks = ["Aa", "Çç", "Ğğ", "Şş", "İi", "Öö", "Üü", ";", "…", "!", "?", "“ ”", "he-ce", "kelime", "anlam", ","];
      const x0 = w > 700 ? w * .38 : 0, n = Math.max(5, Math.round((w - x0) / 100));
      for (let i = 0; i < n; i++) {
        const x = x0 + (i + .15 + rnd() * .7) * (w - x0) / n, y = h * (.2 + rnd() * .55), sz = 15 + rnd() * 17, t = ks[Math.floor(rnd() * ks.length)];
        g.save(); g.translate(x, y); g.rotate((rnd() - .5) * .3);
        g.globalAlpha = .13 + rnd() * .15; g.fillStyle = i % 3 === 0 ? "#f5c53d" : "#fbf6e6";
        g.font = `700 ${sz}px 'Andika', 'Baloo 2', sans-serif`; g.textAlign = "center"; g.fillText(t, 0, 0); g.restore();
      }
      const hx = (cx, cy, r) => { g.beginPath(); for (let k = 0; k < 6; k++) { const a = Math.PI / 3 * k; g.lineTo(cx + r * Math.cos(a), cy + r * Math.sin(a)); } g.closePath(); g.stroke(); };
      g.strokeStyle = "rgba(245,197,61,.28)"; g.lineWidth = 1.4;                     // petek kümesi (sağ alt)
      const r = 11, bx = w > 700 ? w * .66 : w - 30, by = h - 14;
      for (let c = 0; c < 4; c++) for (let rr = 0; rr < 2; rr++) hx(bx - c * r * 1.5, by - rr * r * 1.73 - (c % 2) * r * .87, r);
      g.strokeStyle = "rgba(251,246,230,.32)"; g.lineWidth = 1.6; g.setLineDash([3, 6]); g.lineCap = "round";   // arı uçuşu
      const y0 = h * .7, xa = w > 700 ? w * .4 : w * .05, xb = w * .82;
      g.beginPath(); g.moveTo(xa, y0); g.bezierCurveTo(xa + (xb - xa) * .3, y0 - 40, xa + (xb - xa) * .55, y0 + 30, xb, y0 - 14); g.stroke(); g.setLineDash([]);
      g.globalAlpha = .7; g.fillStyle = "#f5c53d"; g.beginPath(); g.ellipse(xb + 6, y0 - 16, 6, 4.5, 0, 0, 7); g.fill();
      g.fillStyle = "#3a2a12"; g.fillRect(xb + 4, y0 - 20, 2, 8); g.fillRect(xb + 8, y0 - 20, 2, 8);
      g.fillStyle = "rgba(234,246,255,.8)"; g.beginPath(); g.ellipse(xb + 4, y0 - 23, 3, 4.5, -.4, 0, 7); g.ellipse(xb + 9, y0 - 23, 3, 4.5, .4, 0, 7); g.fill();
      g.globalAlpha = 1;
    },
    harita(g, w, h, rnd) {
      const cream = "245,236,215";
      g.strokeStyle = `rgba(${cream},.07)`; g.lineWidth = 1; g.setLineDash([3, 5]);       // enlem-boylam ızgarası
      for (let x = 40; x < w; x += 90) { g.beginPath(); g.moveTo(x, 0); g.lineTo(x, h); g.stroke(); }
      for (let y = 30; y < h; y += 45) { g.beginPath(); g.moveTo(0, y); g.lineTo(w, y); g.stroke(); }
      g.setLineDash([]);
      const n = Math.max(2, Math.round(w / 380));                                          // eş yükselti eğrileri
      for (let c = 0; c < n; c++) {
        const cx = (c + .3 + rnd() * .5) * w / n, cy = h * (.25 + rnd() * .6), p1 = rnd() * 6, p2 = rnd() * 6, base = 18 + rnd() * 16;
        for (let k = 0; k < 6; k++) {
          const R = base + k * 16; g.beginPath();
          for (let a = 0; a <= 6.3; a += .08) { const rr = R * (1 + .16 * Math.sin(3 * a + p1) + .07 * Math.sin(5 * a + p2)); const x = cx + rr * 1.5 * Math.cos(a), y = cy + rr * .8 * Math.sin(a); a ? g.lineTo(x, y) : g.moveTo(x, y); }
          g.closePath(); g.strokeStyle = `rgba(${cream},${.2 - k * .025})`; g.lineWidth = k === 0 ? 1.6 : 1.1; g.stroke();
        }
      }
      g.strokeStyle = `rgba(233,178,74,${w > 640 ? .75 : .5})`; g.lineWidth = 2.2; g.setLineDash([2, 7]); g.lineCap = "round";   // kesikli rota
      const pts = [[-10, h * .82], [w * .18, h * .55], [w * .38, h * .78], [w * .6, h * .4], [w + 10, h * .62]];
      g.beginPath(); g.moveTo(...pts[0]);
      for (let i = 1; i < pts.length; i++) { const [x0, y0] = pts[i - 1], [x1, y1] = pts[i]; g.quadraticCurveTo((x0 + x1) / 2, y0 - 22, x1, y1); }
      g.stroke(); g.setLineDash([]);
      g.fillStyle = "rgba(233,178,74,.9)";
      pts.slice(1, -1).forEach(([x, y]) => { g.beginPath(); g.arc(x, y, 3.2, 0, 7); g.fill(); });
      if (w > 640) {                                                                        // pusula gülü
        const cx = w * .72, cy = h * .45, R = Math.min(38, h * .36); g.save(); g.translate(cx, cy); g.globalAlpha = .38;
        g.strokeStyle = `rgb(${cream})`; g.lineWidth = 1.2; g.beginPath(); g.arc(0, 0, R * .78, 0, 7); g.stroke();
        for (let i = 0; i < 8; i++) { const L = i % 2 ? R * .55 : R, s = i % 2 ? 3 : 5; g.rotate(Math.PI / 4); g.beginPath(); g.moveTo(0, -L); g.lineTo(s, 0); g.lineTo(-s, 0); g.closePath(); g.fillStyle = i === 7 ? "rgb(200,85,61)" : `rgb(${cream})`; g.fill(); }
        g.restore();
      }
    }
  };
  function drawStars() {
    const cv = $("#stars"); if (!cv) return;
    const r = cv.getBoundingClientRect(), dpr = window.devicePixelRatio || 1;
    cv.width = r.width * dpr; cv.height = r.height * dpr;
    const g = cv.getContext("2d"); g.scale(dpr, dpr);
    let seed = 7; const rnd = () => (seed = (seed * 9301 + 49297) % 233280) / 233280;
    const desen = DESEN[S.ders && S.ders.tema && S.ders.tema.desen] || DESEN.yildiz;
    desen(g, r.width, r.height, rnd);
  }

  // Derse özgü tema: ders.json'da "tema": {"ad": "...", "desen": "...", "font": "<Google Fonts family parametresi>"}.
  // Tema yoksa (ör. fen1) hiçbir şey değişmez.
  function applyTema(t) {
    if (!t || !t.ad) return;
    document.documentElement.dataset.tema = t.ad;
    if (t.font) { const l = document.createElement("link"); l.rel = "stylesheet"; l.href = `https://fonts.googleapis.com/css2?family=${t.font}&display=swap`; document.head.appendChild(l); }
  }

  async function boot() {
    tts.init(); addEventListener("resize", drawStars);
    try {
      const r = await fetch("ders.json", { cache: "no-cache" }); if (!r.ok) throw 0;
      S.ders = await r.json();
    } catch (e) { drawStars(); $("#content").innerHTML = `<div class="notice">Ders bilgisi açılamadı. Sayfayı yenile.</div>`; return; }
    applyTema(S.ders.tema); drawStars();
    document.title = `${S.ders.ders} · ${S.ders.donem} — Ela'nın Defteri`;
    $("#dersBaslik").textContent = S.ders.ders;
    $("#dersEtiket").textContent = `${S.ders.sinif} · ${S.ders.donem}`;
    const sb = $("#sinifBtn");
    const applyClass = on => { document.body.classList.toggle("sinif", on); sb.setAttribute("aria-pressed", on); };
    applyClass(store.get("ela7:sinif", false));
    sb.onclick = () => { const on = !document.body.classList.contains("sinif"); store.set("ela7:sinif", on); applyClass(on); if (S.data && $("#panel")) setTab(S.tab); };
    $("#units").onclick = e => { const b = e.target.closest(".unit-btn"); if (b) openUnit(+b.dataset.u); };
    $("#topics").onclick = e => { const b = e.target.closest(".topic"); if (b && !b.disabled) { S.donus = null; openKonu(b.dataset.id, true); } };
    const yol = h => h === "rapor" ? openRapor() : h === "gunluk" && isEn() ? openGunluk() : h === "defter" && isEn() ? openDefter() : h === "atolye" && S.ders.atolye ? openAtolye() : openKonu(h, true);
    addEventListener("hashchange", () => yol(location.hash.slice(1)));
    if (isEn()) $(".head-actions").insertAdjacentHTML("afterbegin", `<a class="head-btn" href="#gunluk">Günün Tekrarı</a><a class="head-btn" href="#defter">Kelime Defterim</a>`);
    if (S.ders.atolye) $(".head-actions").insertAdjacentHTML("afterbegin", `<a class="head-btn" href="#atolye">${ICON.okuma}Okuma Atölyesi</a>`);
    $$(".head-actions a").forEach(l => l.onclick = e => { const h = l.getAttribute("href").slice(1); if (location.hash.slice(1) === h) { e.preventDefault(); yol(h); } });
    const ready = allTopics().filter(k => k.hazir);
    const want = [location.hash.slice(1), store.get(key("son"))].find(id => ready.some(k => k.id === id));
    const first = want || (ready.length ? ready[ready.length - 1].id : null);
    renderNav(); setupBot();
    const ozel = location.hash.slice(1);
    KDB.temizle();
    if (ozel === "rapor" || (isEn() && (ozel === "gunluk" || ozel === "defter")) || (S.ders.atolye && ozel === "atolye")) yol(ozel);
    else if (first) openKonu(first, false); else $("#content").innerHTML = `<div class="notice">Henüz eklenmiş konu yok.</div>`;
    if (ozel !== "rapor") KOC.plan();
  }
  boot();
})();
