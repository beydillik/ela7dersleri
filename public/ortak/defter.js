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
    ses: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 10v4h4l5 4V6L8 10z"/><path d="M16 9a4 4 0 0 1 0 6"/><path d="M18.5 6.5a8 8 0 0 1 0 11"/></svg>'
  };

  const PRAISE = {
    first: ["Doğru! Dikkatlice okudun.", "Doğru! Bilgiyi güzel hatırladın.", "Doğru! Acele etmeden düşündün."],
    second: ["Doğru! İpucunu iyi kullandın.", "Doğru! İkinci denemede buldun, pes etmedin.", "Doğru! Bilgi kartını hatırlaman işe yaradı."],
    shown: ["Olsun, şimdi öğrendin. Açıklamayı bir kez daha oku.", "Bunu birlikte öğrendik. Tekrar bölümünde yine karşına çıkacak."]
  };

  // ---------- Sesli okuma ----------
  const tts = {
    voice: null,
    init() {
      if (!("speechSynthesis" in window)) return;
      const pickVoice = () => {
        const v = speechSynthesis.getVoices().filter(x => /^tr/i.test(x.lang));
        tts.voice = v.find(x => /tolga|emel|yelda|google/i.test(x.name)) || v[0] || null;
        document.body.classList.toggle("no-tts", !tts.voice);
        $$(".listen").forEach(b => b.hidden = !tts.voice);
      };
      pickVoice();
      speechSynthesis.onvoiceschanged = pickVoice;
    },
    say(text) {
      if (!tts.voice) return;
      speechSynthesis.cancel();
      const u = new SpeechSynthesisUtterance(text);
      u.voice = tts.voice; u.lang = tts.voice.lang; u.rate = .95;
      speechSynthesis.speak(u);
    },
    stop() { if ("speechSynthesis" in window) speechSynthesis.cancel(); }
  };
  const listenBtn = text => `<button class="listen" data-say="${esc(text)}" ${tts.voice ? "" : "hidden"}>${ICON.ses}Dinle</button>`;
  document.addEventListener("click", e => { const b = e.target.closest("[data-say]"); if (b) tts.say(b.dataset.say); });

  // ---------- Durum ----------
  const S = { ders: null, konu: null, data: null, unit: 0, tab: "ogren", cache: {} };
  const key = k => `ela7:${S.ders.kod}:${k}`;

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
      <p class="q-text">${idx ? `<span class="qn">${idx}.</span>` : ""}<span>${esc(o.soru)}</span></p>
      <div class="opts">${o.secenekler.map((s, j) => `<button class="opt" data-o="${j}">${"abcd"[j]}) ${esc(s)}</button>`).join("")}</div>
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
        fb.innerHTML = `<div><b>${pick(PRAISE.shown)}</b></div><div>${esc(o.aciklama)}</div>`;
      } else {
        fb.className = "fb ok";
        fb.innerHTML = `<div><b>${pick(result === 1 ? PRAISE.first : PRAISE.second)}</b></div><div>${esc(o.aciklama)}</div>`;
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
      fb.innerHTML = `<div><b>Henüz değil.</b> ${esc(o.ipucu || "Bilgiyi bir kez daha düşün.")}</div>` +
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
          <p class="big">${esc(d.giris)}</p>
          <div class="chips">${d.kavramlar.map(k => `<span class="chip">${k.svg}${esc(k.ad)}</span>`).join("")}</div>
          <div class="row">${listenBtn(d.baslik + ". " + d.giris)}</div>
          ${nav("Başlayalım")}</div>`;
      } else if (st.t === "bilgi") {
        const k = d.kavramlar[st.k];
        html = `<div class="stage"><div class="info-grid">${k.svg}<div class="stage-body">
          <div class="kicker">Kavram ${st.k + 1} / ${d.kavramlar.length}</div>
          <h3 style="color:${esc(k.renk || "inherit")}">${esc(k.ad)}</h3>
          <p class="big">${esc(k.aciklama)}</p>${k.ek ? `<p class="ek">${esc(k.ek)}</p>` : ""}
          <div class="row"><span class="key"><b>Akılda kalsın</b>${esc(k.akilda)}</span>${listenBtn(`${k.ad}. ${k.aciklama} ${k.ek || ""} Akılda kalsın: ${k.akilda}.`)}</div>
          </div></div>${nav(k.soru ? "Anladım, soru gelsin" : "Devam")}</div>`;
      } else if (st.t === "soru") {
        const k = d.kavramlar[st.k];
        html = `<div class="stage"><div class="kicker">Soru · ${esc(k.ad)}</div><div id="qbox">${questionHTML(k.soru)}</div>${nav("Devam", !!(qstate[pos] && qstate[pos].result !== undefined))}</div>`;
      } else if (st.t === "hatirla") {
        const ks = d.kavramlar.slice(st.from, st.to + 1);
        html = `<div class="stage"><div class="kicker">Hatırlayalım</div><h3>Aklında kaldı mı?</h3>
          <p class="big">Her karta dokun. Önce kendin hatırlamaya çalış, sonra cevabı gör.</p>
          <div class="recall">${ks.map(k => `<button data-reveal>${k.svg}<span>${esc(k.ad)} → <span class="ans" hidden>${esc(k.akilda)}</span><span class="q-mark">?</span></span></button>`).join("")}</div>
          ${nav("Devam")}</div>`;
      } else if (st.t === "ozet") {
        html = `<div class="stage"><div class="kicker">Özet</div><h3>Akılda Kalsın</h3>
          <ul class="remember">${d.akildaKalsin.map(a => `<li>${esc(a)}</li>`).join("")}</ul>
          <div class="row">${listenBtn(d.akildaKalsin.join(". "))}</div>${nav("Devam")}</div>`;
      } else if (st.t === "yaz") {
        const y = d.dusunVeYaz[0];
        html = `<div class="stage"><div class="kicker">Düşün ve Yaz · isteğe bağlı</div><h3>${esc(y.soru)}</h3>
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
      out.innerHTML = `<div class="model"><b>Örnek cevap:</b> ${esc(y.ornekCevap)}</div>
        <p class="ek" style="margin:8px 0 6px">Bu anahtar kelimeleri kullandın mı? Yeşil olanları yazmışsın.</p>
        <div class="kw">${y.anahtarlar.map(a => `<span class="${txt.includes(lower(a)) ? "hit" : ""}">${esc(a)}</span>`).join("")}</div>`;
    };
  }

  // ---------- Konuya Bak ----------
  function renderBak(root) {
    const d = S.data, icon = {}; d.kavramlar.forEach(k => icon[k.ad] = k.svg);
    const h = [];
    h.push(`<section><p class="lead">${esc(d.giris)}</p></section>`);
    h.push(`<section><div class="sec-title"><h3>Kavramlar</h3><span>${d.kavramlar.length} kavram</span></div><div class="cards">` +
      d.kavramlar.map(k => `<article class="card">${k.svg}<div><h4 style="color:${esc(k.renk || "inherit")}">${esc(k.ad)}</h4>
        <p>${esc(k.aciklama)}</p>${k.ek ? `<p class="ek">${esc(k.ek)}</p>` : ""}<span class="key"><b>Akılda kalsın</b>${esc(k.akilda)}</span></div></article>`).join("") + `</div></section>`);
    if (d.gruplar && d.gruplar.length) h.push(`<section><div class="sec-title"><h3>Gruplar</h3></div><div class="groups">` +
      d.gruplar.map(g => `<div class="group"><h4>${esc(g.soru)}</h4><div class="boxes">` + g.kutular.map(b => `<div class="box"><div class="lbl">${esc(b.etiket)}</div><div class="chips">` +
        b.uyeler.map(m => `<span class="chip">${icon[m] || ""}${esc(m)}</span>`).join("") + `</div></div>`).join("") + `</div></div>`).join("") + `</div></section>`);
    if (d.biliyorMusun && d.biliyorMusun.length) h.push(`<section class="facts"><div class="eyebrow">Biliyor musun?</div>${d.biliyorMusun.map(f => `<p>${esc(f)}</p>`).join("")}</section>`);
    h.push(`<section><div class="sec-title"><h3>Akılda Kalsın</h3></div><ul class="remember">${d.akildaKalsin.map(a => `<li>${esc(a)}</li>`).join("")}</ul></section>`);
    if (d.merakKutusu && d.merakKutusu.length) h.push(`<section><div class="sec-title"><h3>Merak Kutusu</h3><span>Soruya dokun, cevabı aç</span></div><div class="merak">` +
      d.merakKutusu.map(m => `<details><summary>${esc(m.soru)}</summary><p>${esc(m.cevap)}</p></details>`).join("") + `</div></section>`);
    h.push(`<p class="src">Kaynak: MEB Fen Bilimleri 7. Sınıf Ders Kitabı, ${esc(d.sayfalar)}.</p>`);
    root.innerHTML = h.join("");
  }

  // ---------- Tekrar ----------
  function renderTekrar(root) {
    const d = S.data;
    const games = [["kart", "Hafıza Kartları"], ["eslestir", "Eşleştir"]];
    if (d.gruplar && d.gruplar.length) games.push(["grupla", "Gruplayalım"]);
    let g = store.get(key("oyun"), "kart"); if (!games.some(x => x[0] === g)) g = "kart";
    root.innerHTML = `<div class="subtabs">${games.map(([k, n]) => `<button class="subtab" data-g="${k}" aria-pressed="${k === g}">${n}</button>`).join("")}</div><div id="game"></div>`;
    $$(".subtab", root).forEach(b => b.onclick = () => { g = b.dataset.g; store.set(key("oyun"), g); $$(".subtab", root).forEach(x => x.setAttribute("aria-pressed", x === b)); run(); });
    const run = () => { const box = $("#game", root); ({ kart: gameCards, eslestir: gameMatch, grupla: gameGroup })[g](box); };
    run();
  }

  function gameCards(box) {
    const d = S.data; let order = results.weakFirst(d.kavramlar), pos = 0;
    box.innerHTML = `<div class="flash"><p class="ek" style="margin:0">Zorlandığın kavramlar önce gelir.</p>
      <button class="fcard" id="fcard" aria-label="Kartı çevir"><div class="inner"><div class="face front" id="ffront"></div><div class="face back" id="fback"></div></div></button>
      <div class="row" style="justify-content:center"><button class="btn" id="fprev">Önceki</button><span class="count" id="fcount"></span><button class="btn" id="fnext">Sonraki</button><button class="btn ghost" id="fmix">Karıştır</button></div></div>`;
    const card = $("#fcard", box);
    const show = () => {
      const k = order[pos]; card.classList.remove("flipped");
      $("#ffront", box).innerHTML = `${k.svg}<div class="fname">${esc(k.ad)}</div>${results.isWeak(k.ad) ? '<div class="weak">Tekrar et</div>' : ""}<div class="hintline">Önce hatırla, sonra dokun</div>`;
      $("#fback", box).innerHTML = `<div class="bigk">${esc(k.akilda)}</div><p>${esc(k.aciklama)}</p>`;
      $("#fcount", box).textContent = `${pos + 1} / ${order.length}`;
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
      <div class="col">${right.map(i => `<button class="mitem" data-r="${i}">${esc(ks[i].akilda)}</button>`).join("")}</div></div>
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
    fab.className = "bot-fab"; fab.innerHTML = `${b.svg}<span>${esc(b.ad)}'a sor</span>`;
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
    tts.stop(); S.tab = t; store.set(key("sekme"), t);
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
    setTab(store.get(key("sekme"), "ogren"));
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

  function drawStars() {
    const cv = $("#stars"); if (!cv) return;
    const r = cv.getBoundingClientRect(), dpr = window.devicePixelRatio || 1;
    cv.width = r.width * dpr; cv.height = r.height * dpr;
    const g = cv.getContext("2d"); g.scale(dpr, dpr);
    let seed = 7; const rnd = () => (seed = (seed * 9301 + 49297) % 233280) / 233280;
    for (let i = 0; i < Math.round(r.width / 6); i++) { g.globalAlpha = .35 + rnd() * .6; g.fillStyle = "#fff"; g.beginPath(); g.arc(rnd() * r.width, rnd() * r.height, rnd() * 1.4 + .3, 0, 7); g.fill(); }
  }

  async function boot() {
    tts.init(); drawStars(); addEventListener("resize", drawStars);
    try {
      const r = await fetch("ders.json", { cache: "no-cache" }); if (!r.ok) throw 0;
      S.ders = await r.json();
    } catch (e) { $("#content").innerHTML = `<div class="notice">Ders bilgisi açılamadı. Sayfayı yenile.</div>`; return; }
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
