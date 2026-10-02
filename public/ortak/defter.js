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
    yavas: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 16h13a3 3 0 0 0 3-3v-1"/><path d="M5 16a6 6 0 0 1 12 0"/><circle cx="20" cy="10" r="2"/><path d="M7 16v2M15 16v2"/></svg>',
    ses: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 10v4h4l5 4V6L8 10z"/><path d="M16 9a4 4 0 0 1 0 6"/><path d="M18.5 6.5a8 8 0 0 1 0 11"/></svg>'
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
    },
    // Karışık metni parçalara ayırıp sırayla okur.
    say(text) {
      if (!tts.voice && !tts.en) return;
      speechSynthesis.cancel();
      String(text).split(EN_RE).forEach((part, i) => {
        part = part.trim(); if (!part || !/[\p{L}\p{N}]/u.test(part)) return;
        const en = i % 2 === 1, v = en ? (tts.en || tts.voice) : (tts.voice || tts.en);
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
  // Metin içi {{İngilizce}} parçaları: renkli gösterilir, dokununca okunur.
  const rx = s => esc(s).replace(EN_RE, (m, t) => `<span class="en" lang="en" role="button" tabindex="0" data-say-en="${t}">${t}</span>`);
  const plain = s => String(s ?? "").replace(EN_RE, "$1");
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
  const adHTML = (k, big) => `${esc(k.ad)}${isEn() ? enBtns(k.ad, big) : ""}`;
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
  function questionHTML(o, idx) {
    return `<div class="q">
      <p class="q-text">${idx ? `<span class="qn">${idx}.</span>` : ""}<span>${rx(o.soru)}</span></p>
      ${o.dinle ? `<div class="q-listen"><button class="say-en big" data-say-en="${esc(o.dinle)}" ${tts.en ? "" : "hidden"}>${ICON.ses}<span>Dinle</span></button><button class="say-en slow" data-say-en="${esc(o.dinle)}" data-slow ${tts.en ? "" : "hidden"}>${ICON.yavas}<span>Yavaş</span></button></div>` : ""}
      <div class="opts">${o.secenekler.map((s, j) => `<button class="opt" data-o="${j}">${"abcd"[j]}) ${esc(plain(s))}</button>`).join("")}</div>
      <div class="fb" hidden></div></div>`;
  }
  function wireQuestion(el, o, opts = {}) {
    let tries = 0, finished = false, picked = null;
    const state = opts.state || { wrong: [], result: undefined };
    const fb = $(".fb", el);
    const finish = (result, silent) => {
      finished = true; state.result = result;
      $$(".opt", el).forEach((b, j) => { b.disabled = true; if (j === o.dogru) b.classList.add("right"); });
      fb.hidden = false;
      if (result === 0) {
        fb.className = "fb show";
        fb.innerHTML = `<div><b>${pick(PRAISE.shown)}</b></div><div>${rx(o.aciklama)}</div>`;
      } else {
        fb.className = "fb ok";
        fb.innerHTML = `<div><b>${pick(result === 1 ? PRAISE.first : PRAISE.second)}</b></div><div>${rx(o.aciklama)}</div>`;
      }
      if (!silent) opts.onDone && opts.onDone(result);
    };
    const answer = j => {
      if (finished) return;
      if (j === o.dogru) return finish(tries === 0 ? 1 : 2);
      tries++; if (!state.wrong.includes(j)) state.wrong.push(j);
      const b = $$(".opt", el)[j]; b.classList.add("wrong"); b.disabled = true;
      if (tries >= 2) return finish(0);
      fb.hidden = false; fb.className = "fb hint";
      fb.innerHTML = `<div><b>Henüz değil.</b> ${rx(o.ipucu || "Bilgiyi bir kez daha düşün.")}</div>` +
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
            if (picked === o.dogru) finish(1); else { $$(".opt", el)[picked].classList.add("wrong"); finish(0); } }; }
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
    const steps = [{ t: "giris" }];
    d.kavramlar.forEach((k, i) => {
      steps.push({ t: "bilgi", k: i });
      if (k.soru) steps.push({ t: "soru", k: i });
      if ((i + 1) % 3 === 0 && i < d.kavramlar.length - 1) steps.push({ t: "hatirla", from: i - 2, to: i });
    });
    const n = d.kavramlar.length;
    if (n) { const from = n % 3 === 0 ? n - 3 : n - (n % 3); steps.push({ t: "hatirla", from, to: n - 1 }); }
    steps.push({ t: "ozet" });
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
      if (st.t === "giris") {
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
          <p class="big">${rx(k.aciklama)}</p>${k.ek ? `<p class="ek">${rx(k.ek)}</p>` : ""}${ornekHTML(k)}
          <div class="row"><span class="key"><b>Akılda kalsın</b>${rx(k.akilda)}</span>${listenBtn(kSay(k))}</div>
          </div></div>${nav(k.soru ? "Anladım, soru gelsin" : "Devam")}</div>`;
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
          state: qstate[pos],
          onDone: res => { results.set(k.ad, res); $("[data-next]", stage).disabled = false; },
          backToInfo: () => go(pos - 1)
        });
      }
      $$("[data-reveal]", stage).forEach(b => b.onclick = () => { $(".ans", b).hidden = false; $(".q-mark", b).hidden = true; });
      if (st.t === "yaz") wireWrite(stage, d.dusunVeYaz[0]);
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
    h.push(`<section><div class="sec-title"><h3>Kavramlar</h3><span>${d.kavramlar.length} kavram</span></div><div class="cards">` +
      d.kavramlar.map(k => `<article class="card">${k.svg}<div><h4 style="color:${esc(k.renk || "inherit")}"${isEn() ? ' lang="en"' : ""}>${adHTML(k)}</h4>
        <p>${rx(k.aciklama)}</p>${k.ek ? `<p class="ek">${rx(k.ek)}</p>` : ""}${ornekHTML(k)}<span class="key"><b>Akılda kalsın</b>${rx(k.akilda)}</span></div></article>`).join("") + `</div></section>`);
    if (d.gruplar && d.gruplar.length) h.push(`<section><div class="sec-title"><h3>Gruplar</h3></div><div class="groups">` +
      d.gruplar.map(g => `<div class="group"><h4>${esc(g.soru)}</h4><div class="boxes">` + g.kutular.map(b => `<div class="box"><div class="lbl">${esc(b.etiket)}</div><div class="chips">` +
        b.uyeler.map(m => `<span class="chip">${icon[m] || ""}${esc(m)}</span>`).join("") + `</div></div>`).join("") + `</div></div>`).join("") + `</div></section>`);
    if (d.biliyorMusun && d.biliyorMusun.length) h.push(`<section class="facts"><div class="eyebrow">Biliyor musun?</div>${d.biliyorMusun.map(f => `<p>${rx(f)}</p>`).join("")}</section>`);
    h.push(`<section><div class="sec-title"><h3>Akılda Kalsın</h3></div><ul class="remember">${d.akildaKalsin.map(a => `<li>${rx(a)}</li>`).join("")}</ul></section>`);
    if (d.merakKutusu && d.merakKutusu.length) h.push(`<section><div class="sec-title"><h3>Merak Kutusu</h3><span>Soruya dokun, cevabı aç</span></div><div class="merak">` +
      d.merakKutusu.map(m => `<details><summary>${rx(m.soru)}</summary><p>${rx(m.cevap)}</p></details>`).join("") + `</div></section>`);
    h.push(`<p class="src">Kaynak: ${esc(S.ders.kaynak || `MEB ${S.ders.ders} ${S.ders.sinif} Ders Kitabı`)}, ${esc(d.sayfalar)}.<br>Hazırlayan: Kemal BEYDİLLİ - Eylül 2026</p>`);
    root.innerHTML = h.join("");
  }

  // ---------- Tekrar ----------
  function renderTekrar(root) {
    const d = S.data;
    const games = [["kart", "Hafıza Kartları"], ["eslestir", "Eşleştir"]];
    if (d.gruplar && d.gruplar.length) games.push(["grupla", "Gruplayalım"]);
    if (isEn()) games.push(["dinle", "Dinle ve Bul"], ["kur", "Kelimeyi Kur"]);
    let g = store.get(key("oyun"), "kart"); if (!games.some(x => x[0] === g)) g = "kart";
    root.innerHTML = `<div class="subtabs">${games.map(([k, n]) => `<button class="subtab" data-g="${k}" aria-pressed="${k === g}">${n}</button>`).join("")}</div><div id="game"></div>`;
    $$(".subtab", root).forEach(b => b.onclick = () => { g = b.dataset.g; store.set(key("oyun"), g); $$(".subtab", root).forEach(x => x.setAttribute("aria-pressed", x === b)); run(); });
    const run = () => { const box = $("#game", root); ({ kart: gameCards, eslestir: gameMatch, grupla: gameGroup, dinle: gameListen, kur: gameSpell })[g](box); };
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

  // ---------- Test ----------
  function renderTest(root) {
    const d = S.data, cls = document.body.classList.contains("sinif");
    root.innerHTML = `<div class="scorebar"><span id="score"></span><div class="meter"><i id="meter"></i></div><button class="btn" id="qreset">Baştan başla</button></div>
      ${cls ? '<p class="ek" style="margin:0">Sınıf modu: seçenek seçilince cevap gizli kalır, "Cevabı göster" ile açılır.</p>' : '<p class="ek" style="margin:0">Her soruda 2 hakkın var. İlk yanlışta ipucu gelir.</p>'}
      <div class="tests">${d.sorular.map((q, i) => `<div class="card-q" data-q="${i}">${questionHTML(q, i + 1)}</div>`).join("")}</div>`;
    let first = 0, answered = 0;
    const upd = () => { $("#score", root).textContent = `${first} / ${d.sorular.length} ilk denemede doğru · ${answered} cevaplandı`; $("#meter", root).style.width = (first / d.sorular.length * 100) + "%"; };
    $$(".card-q", root).forEach(el => wireQuestion($(".q", el), d.sorular[+el.dataset.q], { classMode: cls, onDone: r => { answered++; if (r === 1) first++; upd(); } }));
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
    $("#topics").innerHTML = u.konular.length ? u.konular.map((k, i) => `<button class="topic" data-id="${esc(k.id)}" ${k.hazir ? "" : "disabled"} aria-current="${S.konu === k.id}">
      <span class="num">${i + 1}</span><span>${esc(k.baslik)}</span>${k.hazir ? "" : '<span class="soon">yakında</span>'}</button>`).join("")
      : `<div class="empty-unit">Bu ünitenin konuları sırası gelince eklenecek.</div>`;
    const cur = $(".topic[aria-current='true']"); if (cur) cur.scrollIntoView({ block: "nearest", inline: "nearest" });
  }

  function setTab(t) {
    tts.stop(); S.tab = t; store.set(key("sekme:" + S.konu), t); // sekme her konu için ayrı hatırlanır
    $$(".tab").forEach(b => b.setAttribute("aria-selected", b.dataset.tab === t));
    const p = $("#panel");
    ({ ogren: renderOgren, bak: renderBak, tekrar: renderTekrar, test: renderTest })[t](p);
  }

  function renderKonu(no) {
    const d = S.data;
    $("#content").innerHTML = `<section class="konu-head"><div class="meta"><span>${esc(d.unite)}</span><span class="pill">Konu ${no}</span><span class="pill">${esc(d.sayfalar)}</span></div>
      <h2>${esc(d.baslik)}</h2>
      <div class="tabs" role="tablist">
        <button class="tab" role="tab" data-tab="ogren">${ICON.ogren}Öğren</button>
        <button class="tab" role="tab" data-tab="bak">${ICON.bak}Konuya Bak</button>
        <button class="tab" role="tab" data-tab="tekrar">${ICON.tekrar}Tekrar</button>
        <button class="tab" role="tab" data-tab="test">${ICON.test}Test</button></div></section>
      <div class="panel" id="panel"></div>`;
    $$(".tab").forEach(b => b.onclick = () => setTab(b.dataset.tab));
    setTab(store.get(key("sekme:" + S.konu), "ogren")); // hiç açılmamış konu Öğren'den başlar
    S.onKonu && S.onKonu();
  }

  async function openKonu(id, scroll) {
    const t = allTopics().find(k => k.id === id && k.hazir); if (!t) return;
    S.konu = id; S.unit = t.ui; renderNav(); store.set(key("son"), id);
    if (location.hash.slice(1) !== id) history.replaceState(null, "", "#" + id);
    try {
      if (!S.cache[id]) { const r = await fetch("konular/" + id + ".json", { cache: "no-cache" }); if (!r.ok) throw 0; S.cache[id] = await r.json(); }
      S.data = S.cache[id]; renderKonu(t.ki + 1);
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
    $("#topics").onclick = e => { const b = e.target.closest(".topic"); if (b && !b.disabled) openKonu(b.dataset.id, true); };
    addEventListener("hashchange", () => openKonu(location.hash.slice(1), true));
    const ready = allTopics().filter(k => k.hazir);
    const want = [location.hash.slice(1), store.get(key("son"))].find(id => ready.some(k => k.id === id));
    const first = want || (ready.length ? ready[ready.length - 1].id : null);
    renderNav(); setupBot();
    if (first) openKonu(first, false); else $("#content").innerHTML = `<div class="notice">Henüz eklenmiş konu yok.</div>`;
  }
  boot();
})();
