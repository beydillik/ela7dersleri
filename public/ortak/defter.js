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
  const fx = h => h.replace(DV_RE, '<span class="devir">$1</span>').replace(FR_RE, (m, s, w, a, b) => `<span class="kesir-w">${s ? "−" : ""}${w || ""}<span class="kesir"><span>${a.replace("-", "−")}</span><span>${b.replace("-", "−")}</span></span></span>`);
  // Metin içi {{İngilizce}} parçaları: renkli gösterilir, dokununca okunur.
  const rx = s => fx(esc(s).replace(EN_RE, (m, t) => `<span class="en" lang="en" role="button" tabindex="0" data-say-en="${t}">${t}</span>`));
  const plain = s => String(s ?? "").replace(EN_RE, "$1").replace(DV_RE, (m, d) => d.replace(/\d/g, "$&\u0305")).replace(FR_RE, (m, s_, w, a, b) => `${s_}${w ? w + " " : ""}${a}/${b}`);
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

  // ---------- Çoklu deneme soru bileşeni ----------
  // o: {soru, secenekler, dogru, ipucu, aciklama}; opts: {onDone(result), backToInfo, classMode}
  // Soru türleri: seçenekli (secenekler + dogru), sayı doğrusunda nokta seçme (nokta + sayiDogrusu),
  // sayı yazma (cevap; tuş takımıyla). sayiDogrusu seçenekli ve yazmalı sorularda da yalnızca gösterim olarak eklenebilir.
  const qKind = o => o.nokta !== undefined ? "nokta" : o.cevap !== undefined ? "girdi" : "secim";
  function questionHTML(o, idx) {
    const kind = qKind(o);
    const body = kind === "nokta" ? `<div class="sd-wrap sd-pick">${sdHTML(o.sayiDogrusu || {}, true)}</div>`
      : kind === "girdi" ? `${o.sayiDogrusu ? `<div class="sd-wrap">${sdHTML(o.sayiDogrusu)}</div>` : ""}${keypadHTML(o)}`
      : `${o.sayiDogrusu ? `<div class="sd-wrap">${sdHTML(o.sayiDogrusu)}</div>` : ""}<div class="opts">${o.secenekler.map((s, j) => `<button class="opt" data-o="${j}">${"abcd"[j]}) ${fx(esc(String(s).replace(EN_RE, "$1")))}</button>`).join("")}</div>`;
    return `<div class="q q-${kind}">
      <p class="q-text">${idx ? `<span class="qn">${idx}.</span>` : ""}<span>${rx(o.soru)}</span></p>
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
    if (kind !== "secim") return wireMathQuestion(el, o, opts, kind);
    let tries = 0, finished = false, picked = null;
    const state = opts.state || { wrong: [], result: undefined };
    const fb = $(".fb", el), yr = wireYardim(el, o, opts, state);
    const finish = (result, silent) => {
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

    root.innerHTML = `<div class="stepper"><div class="progress"><span id="pgTxt"></span><div class="bar"><i id="pgBar"></i></div></div><div id="stage"></div></div>`;
    const go = p => { tts.stop(); pos = Math.max(0, Math.min(steps.length - 1, p)); store.set(posKey, pos); draw(); $("#stage").scrollIntoView({ block: "nearest", behavior: "smooth" }); };

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
      if (st.t === "duvar") renderWall($("#wallBox", stage), wordsOf(d), { baslik: `${d.unite} — ${d.baslik}` });
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
    if (isEn()) renderWall($("#bakWall", root), wordsOf(d), { baslik: `${d.unite} — ${d.baslik}` });
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
    const run = () => { const box = $("#game", root); ({ kart: gameCards, eslestir: gameMatch, grupla: gameGroup, dinle: gameListen, kur: gameSpell, cumle: gameSentence, resim: gamePicture, hata: gameErrors })[g](box); };
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
    let sel = null, done = 0;
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
          if (done === ks.length) { const b = document.createElement("button"); b.className = "btn"; b.textContent = "Yeniden oyna"; b.onclick = () => gameMatch(box); box.appendChild(b); }
        } else { r.classList.add("shake"); setTimeout(() => r.classList.remove("shake"), 400); $("#mmsg", box).textContent = "Bu ikisi eşleşmiyor. Bilgiyi hatırla ve tekrar dene."; }
      }
    };
  }

  function gameGroup(box) {
    const d = S.data, icon = {}; d.kavramlar.forEach(k => icon[k.ad] = k.svg);
    let gi = 0;
    const play = () => {
      const g = d.gruplar[gi], items = shuffle(g.kutular.flatMap((b, bi) => b.uyeler.map(m => ({ m, bi }))));
      let sel = null, placed = 0;
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
              $("#gnext", box).innerHTML = gi < d.gruplar.length - 1 ? `<button class="btn primary">Sonraki gruplama</button>` : `<button class="btn">Baştan oyna</button>`;
              $("#gnext button", box).onclick = () => { gi = gi < d.gruplar.length - 1 ? gi + 1 : 0; play(); };
            }
          } else { chip.classList.add("shake"); setTimeout(() => chip.classList.remove("shake"), 400); $("#gmsg", box).textContent = "Bu kutu değil. Kavramın özelliğini hatırla."; }
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
          <p class="game-msg">${tur.length} kelimenin ${ilk} tanesini ilk dinleyişte buldun. Kulağın alışıyor!</p>
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
          tries++; b.classList.add("shake"); b.disabled = true; setTimeout(() => b.classList.remove("shake"), 400);
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
          <button class="btn ghost" data-print>${ICON.yazdir}Afişi yazdır</button></div>
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
          deneme++; b.disabled = true; b.classList.add("shake"); setTimeout(() => b.classList.remove("shake"), 400);
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
        } else { yanlis.add(sel); r.classList.add("shake"); setTimeout(() => r.classList.remove("shake"), 400); $("#pmsg", box).textContent = "Bu resim o kelime değil. Tekrar dene."; }
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
          bulDeneme++; t.classList.add("shake"); setTimeout(() => t.classList.remove("shake"), 400);
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
    h.push(`<section><p class="lead">${rx(d.giris)}</p>${kayit ? durakDurum(kayit) : ""}</section>`);
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
    const d = S.data; S.durakOyun = S.durakOyun || {};
    let st = S.durakOyun[S.konu];
    const toplam = (d.sorular || []).length + (d.eskiSoru ?? 4);
    const basla = () => { st = S.durakOyun[S.konu] = { liste: durakSorulari(d), i: 0, sonuc: [], q: {} }; ciz(); };
    const giris = () => {
      const kayit = durakKayit.get(S.konu);
      root.innerHTML = `<div class="stage"><div class="kicker">Tarama testi</div><h3>${kayit ? "Tekrar tarayalım" : "Neler aklında kalmış?"}</h3>
        <p class="big">${toplam} soru var. Bazıları konulardaki sorulardan, bazıları konuları birleştiren yeni sorular. Her soruda 2 hakkın var. Not yok; sonunda hangi konuya tekrar bakman gerektiğini göstereceğim.</p>
        ${kayit ? durakDurum(kayit) : ""}
        <div class="row"><button class="btn primary" data-basla>Başla</button>${kayit ? `<button class="btn ghost" data-rapor>Son sonucu gör</button>` : ""}</div></div>`;
      $("[data-basla]", root).onclick = basla;
      const rb = $("[data-rapor]", root); if (rb) rb.onclick = () => rapor(kayit);
    };
    // Yanlış ya da ipucuyla bulunan soruda: ilgili kavramın kısa hatırlatması ve konuya dönüş düğmesi
    const hatirlat = (box, it) => {
      const parca = it.kaynak.slice(0, 2).map(x => {
        const k = S.cache[x.konu]; if (!k) return "";
        const kv = x.kavram && k.kavramlar.find(y => y.ad === x.kavram);
        return kv ? `<div class="dk-hat-ic">${kv.svg}<div><b>${esc(kv.ad)}</b> <small>· ${konuNoOf(x.konu)}. konu</small><p>${rx(kv.aciklama)}</p>
            <div class="row"><span class="key"><b>Akılda kalsın</b>${rx(kv.akilda)}</span><button class="btn ghost" data-git="${esc(x.konu)}" data-kv="${esc(kv.ad)}">Konuda bak</button></div></div></div>`
          : `<div class="dk-hat-ic"><div><b>${esc(k.baslik)}</b> <small>· ${konuNoOf(x.konu)}. konu</small><ul class="remember">${k.akildaKalsin.slice(0, 2).map(a => `<li>${rx(a)}</li>`).join("")}</ul>
            <div class="row"><button class="btn ghost" data-git="${esc(x.konu)}">Konuya bak</button></div></div></div>`;
      }).join("");
      box.innerHTML = parca ? `<div class="dk-hat"><div class="kicker">Hatırlatma</div>${parca}</div>` : "";
      $$("[data-git]", box).forEach(b => b.onclick = () => gitKonu(b.dataset.git, b.dataset.kv));
    };
    const ciz = () => {
      const it = st.liste[st.i], son = st.i === st.liste.length - 1;
      const konular = [...new Set(it.kaynak.map(x => x.konu))].map(id => `${konuNoOf(id)}. konu`).join(" + ");
      root.innerHTML = `<div class="stage"><div class="progress"><span>Soru ${st.i + 1} / ${st.liste.length}</span><div class="bar"><i style="width:${(st.i + 1) / st.liste.length * 100}%"></i></div></div>
        <div class="kicker">${it.kaynak.length > 1 ? "Konuları birleştir" : "Hatırla"}${konular ? " · " + esc(konular) : ""}</div>
        <div id="dq">${questionHTML(it.q)}</div><div id="dkHat"></div>
        <div class="stage-nav"><button class="btn ghost" data-bitir>Testi bırak</button><button class="btn primary" data-sonraki disabled>${son ? "Sonucu gör" : "Sonraki soru"}</button></div></div>`;
      st.q[st.i] = st.q[st.i] || { wrong: [], result: undefined };
      const qs = st.q[st.i], sonraki = $("[data-sonraki]", root);
      const k0 = it.kaynak.find(x => x.kavram) || {}, kv0 = k0.konu && S.cache[k0.konu] ? S.cache[k0.konu].kavramlar.find(y => y.ad === k0.kavram) : (it.q.kavram && S.cache[(it.kaynak[0] || {}).konu] ? S.cache[it.kaynak[0].konu].kavramlar.find(y => y.ad === it.q.kavram) : null);
      wireQuestion($("#dq .q", root), it.q, { state: qs, kavram: kv0, onDone: r => { st.sonuc[st.i] = { r, kaynak: it.kaynak }; sonraki.disabled = false; if (r !== 1) hatirlat($("#dkHat", root), it); } });
      if (qs.result !== undefined) { sonraki.disabled = false; if (qs.result !== 1) hatirlat($("#dkHat", root), it); }
      sonraki.onclick = () => {
        tts.stop();
        if (!son) { st.i++; ciz(); root.scrollIntoView({ block: "start", behavior: "smooth" }); return; }
        const kayit = durakKayit.kaydet(S.konu, st.sonuc.map(x => ({ r: x.r, kaynak: x.kaynak })));
        delete S.durakOyun[S.konu]; renderNav(); rapor(kayit);
      };
      $("[data-bitir]", root).onclick = () => { delete S.durakOyun[S.konu]; giris(); };
    };
    const rapor = kayit => {
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
        : eksikVar ? "Çok iyi çalıştın. Aşağıda ! olan konulara kısa bir tekrar yapalım. Sonra testi yeniden dene; ikinci seferde çok daha kolay gelecek."
        : "İpuçlarını kullanarak hepsini buldun. Bu, iyi çalışmanın işareti. Turuncu kavramlara bir göz atman yeter.";
      root.innerHTML = `<div class="stage"><div class="kicker">Ara Durak · Sonuç</div><h3>${iyi ? "Aklında kalmış!" : "Neredeyse tamam!"}</h3><p class="big">${mesaj}</p>
        <div class="done-stats"><div class="stat"><b>${c(1)}</b><span>ilk denemede doğru</span></div><div class="stat"><b>${c(2)}</b><span>ipucuyla doğru</span></div><div class="stat"><b>${c(0)}</b><span>birlikte öğrendik</span></div></div>
        <div class="hz-rapor">${satirlar}</div>
        ${zayif.length ? `<div><div class="kicker">Tekrar bakman gereken kavramlar</div><div class="dk-liste">${zayif.map(z => `<button data-git="${esc(z.konu)}" data-kv="${esc(z.kavram)}">${konuNoOf(z.konu)}. konu · ${esc(z.kavram)}</button>`).join("")}</div></div>` : ""}
        <p class="dk-sonraki">${ICON.tekrar}<span>Bu durağı <b>${tarihYaz(kayit.n)}</b> tekrar tara. Zamanı gelince konu listesinde haber vereceğim.</span></p>
        <div class="row"><button class="btn primary" data-yeniden>Testi yeniden yap</button><button class="btn ghost" data-goto="hatirla">Hatırla'ya dön</button></div></div>`;
      $$("[data-git]", root).forEach(b => b.onclick = () => gitKonu(b.dataset.git, b.dataset.kv));
      $("[data-yeniden]", root).onclick = basla;
      $("[data-goto]", root).onclick = () => setTab("hatirla");
    };
    if (st) ciz(); else giris();
  }

  // ---------- Test ----------
  function renderTest(root) {
    const d = S.data, cls = document.body.classList.contains("sinif");
    root.innerHTML = `<div class="scorebar"><span id="score"></span><div class="meter"><i id="meter"></i></div><button class="btn" id="qreset">Baştan başla</button></div>
      ${cls ? '<p class="ek" style="margin:0">Sınıf modu: seçenek seçilince cevap gizli kalır, "Cevabı göster" ile açılır.</p>' : '<p class="ek" style="margin:0">Her soruda 2 hakkın var. İlk yanlışta ipucu gelir.</p>'}
      <div class="tests">${d.sorular.map((q, i) => `<div class="card-q" data-q="${i}">${questionHTML(q, i + 1)}</div>`).join("")}</div>`;
    let first = 0, answered = 0;
    const upd = () => { $("#score", root).textContent = `${first} / ${d.sorular.length} ilk denemede doğru · ${answered} cevaplandı`; $("#meter", root).style.width = (first / d.sorular.length * 100) + "%"; };
    const kvBul = q => q.kavram ? d.kavramlar.find(k => k.ad === q.kavram) : null;
    $$(".card-q", root).forEach(el => wireQuestion($(".q", el), d.sorular[+el.dataset.q], { kavram: kvBul(d.sorular[+el.dataset.q]), classMode: cls && qKind(d.sorular[+el.dataset.q]) === "secim", onDone: r => { answered++; if (r === 1) first++; upd(); } }));
    $("#qreset", root).onclick = () => renderTest(root);
    upd();
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
      add("bot", b.karsilama.replace("{konu}", S.data ? S.data.baslik : ""));
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

    let busy = false;
    async function send(text) {
      if (busy) return; busy = true; input.value = "";
      const h = hist[S.konu] = hist[S.konu] || [];
      h.push({ rol: "user", metin: text }); add("me", text);
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
    tts.stop(); S.tab = t; store.set(key("sekme:" + S.konu), t); // sekme her konu için ayrı hatırlanır
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
    S.konu = id; S.unit = t.ui; renderNav(); store.set(key("son"), id);
    if (location.hash.slice(1) !== id) history.replaceState(null, "", "#" + id);
    try {
      if (!S.cache[id]) { const r = await fetch("konular/" + id + ".json", { cache: "no-cache" }); if (!r.ok) throw 0; S.cache[id] = await r.json(); }
      S.data = S.cache[id];
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
    sb.onclick = () => { const on = !document.body.classList.contains("sinif"); store.set("ela7:sinif", on); applyClass(on); if (S.data) setTab(S.tab); };
    $("#units").onclick = e => { const b = e.target.closest(".unit-btn"); if (b) openUnit(+b.dataset.u); };
    $("#topics").onclick = e => { const b = e.target.closest(".topic"); if (b && !b.disabled) { S.donus = null; openKonu(b.dataset.id, true); } };
    const yol = h => h === "gunluk" && isEn() ? openGunluk() : h === "defter" && isEn() ? openDefter() : openKonu(h, true);
    addEventListener("hashchange", () => yol(location.hash.slice(1)));
    if (isEn()) {
      $(".head-actions").insertAdjacentHTML("afterbegin", `<a class="head-btn" href="#gunluk">Günün Tekrarı</a><a class="head-btn" href="#defter">Kelime Defterim</a>`);
      $$(".head-actions a").forEach(l => l.onclick = e => { const h = l.getAttribute("href").slice(1); if (location.hash.slice(1) === h) { e.preventDefault(); yol(h); } });
    }
    const ready = allTopics().filter(k => k.hazir);
    const want = [location.hash.slice(1), store.get(key("son"))].find(id => ready.some(k => k.id === id));
    const first = want || (ready.length ? ready[ready.length - 1].id : null);
    renderNav(); setupBot();
    const ozel = location.hash.slice(1);
    if (isEn() && (ozel === "gunluk" || ozel === "defter")) yol(ozel);
    else if (first) openKonu(first, false); else $("#content").innerHTML = `<div class="notice">Henüz eklenmiş konu yok.</div>`;
  }
  boot();
})();
