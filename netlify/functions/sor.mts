/**
 * Ders robotu (Kuark, Pisi, ...) — /api/sor
 *
 * Sayfadan gelen soruyu, açık konunun ders kitabı sayfalarıyla birlikte yapay zekâya gönderir.
 * - API anahtarları Netlify ortam değişkenlerindedir; sayfanın kodunda yoktur.
 * - MODEL_ZINCIRI sırasıyla denenir; hata / yoğunluk / zaman aşımında sıradakine geçilir.
 *   Örnek: "gemini:gemini-3.5-flash,gemini:gemini-2.5-flash,openrouter:google/gemini-3.8-flash"
 * - GUNLUK_LIMIT: tüm site için günlük en fazla soru sayısı (varsayılan 300).
 */
import type { Context, Config } from "@netlify/functions";
import { getStore } from "@netlify/blobs";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";

type Mesaj = { rol: "user" | "bot"; metin: string };
type Halka = { saglayici: "gemini" | "openrouter"; model: string };

const VARSAYILAN_ZINCIR = "gemini:gemini-3.5-flash,gemini:gemini-2.5-flash,gemini:gemini-2.5-flash-lite";
const MODEL_SURESI_MS = 12000;   // bir modeli en fazla bu kadar bekle
const TOPLAM_SURE_MS = 24000;    // tüm zincir için üst sınır

const json = (veri: unknown, durum = 200) =>
  new Response(JSON.stringify(veri), { status: durum, headers: { "Content-Type": "application/json; charset=utf-8" } });

function zinciriOku(): Halka[] {
  const ham = Netlify.env.get("MODEL_ZINCIRI") || VARSAYILAN_ZINCIR;
  return ham.split(",").map(s => s.trim()).filter(Boolean).map(s => {
    const i = s.indexOf(":");
    const saglayici = s.slice(0, i).trim() as Halka["saglayici"];
    return { saglayici, model: s.slice(i + 1).trim() };
  }).filter(h => (h.saglayici === "gemini" || h.saglayici === "openrouter") && h.model);
}

// Kitap metninden yalnızca konunun sayfalarını al ("[s. N]" işareti, üstündeki metnin sayfasıdır)
function sayfalariSec(metin: string, araliklar: number[][]): string {
  const parcalar = metin.split(/\n\[s\. (\d+)\]\n/);
  const sayfa = new Map<number, string>();
  for (let i = 1; i < parcalar.length; i += 2) sayfa.set(Number(parcalar[i]), parcalar[i - 1].trim());
  const secilen: string[] = [];
  for (const [a, b] of araliklar) for (let n = a; n <= b; n++) if (sayfa.has(n)) secilen.push(`[${n >= 1000 ? `Workbook sayfası ${n - 1000}` : `Kitap sayfası ${n}`}]\n${sayfa.get(n)}`); // 1000+ = Workbook (Own It)
  return secilen.join("\n\n").slice(0, 60000);
}

async function kaynakHazirla(origin: string, dersKod: string, konuId: string) {
  const dersRes = await fetch(`${origin}/${dersKod}/ders.json`);
  if (!dersRes.ok) throw new Error("ders bulunamadı");
  const ders = await dersRes.json();
  let unite = 0, konuMeta: any = null;
  for (const u of ders.uniteler) for (const k of u.konular) if (k.id === konuId) { unite = u.no; konuMeta = k; }
  if (!konuMeta) throw new Error("konu bulunamadı");

  const konuRes = await fetch(`${origin}/${dersKod}/konular/${konuId}.json`);
  const konu = konuRes.ok ? await konuRes.json() : null;
  let ozet = "";
  if (konu && konu.tur === "tarama") {   // Ara Durak: kapsanan konuların özetleri birlikte
    const alt = await Promise.all((konu.kapsar || []).map(async (id: string) => {
      try { const r = await fetch(`${origin}/${dersKod}/konular/${id}.json`); return r.ok ? await r.json() : null; } catch { return null; }
    }));
    ozet = [`Ara Durak (tekrar ve tarama): ${konu.baslik}. Öğrenci şu konuları birlikte tekrar ediyor:`,
      ...alt.filter(Boolean).map((k: any) => `- ${k.baslik} (${k.sayfalar}): ` + k.kavramlar.map((x: any) => `${x.ad}: ${x.akilda}`).join("; ") + ". Akılda kalsın: " + k.akildaKalsin.join(" / "))
    ].join("\n");
  } else if (konu) {
    ozet = [
      `Konu: ${konu.baslik} (${konu.sayfalar})`, konu.giris,
      ...konu.kavramlar.map((k: any) => `- ${k.ad}: ${k.aciklama} ${k.ek || ""} (Akılda kalsın: ${k.akilda})`),
      "Akılda kalsın: " + konu.akildaKalsin.join(" / ")
    ].join("\n");
  }

  // Kitap dosyası fonksiyona "included_files" ile eklenir; çalışma klasörü ortama göre değişebildiği için birkaç yer denenir
  let kitap = "";
  const kokler = [process.cwd(), process.env.LAMBDA_TASK_ROOT || "", "/var/task"].filter(Boolean);
  for (const kok of kokler) {
    try {
      const metin = await readFile(resolve(kok, `kaynaklar/${dersKod}/unite${unite}.md`), "utf-8");
      kitap = sayfalariSec(metin, konuMeta.kaynakSayfalar || []);
      break;
    } catch { /* sıradaki klasörü dene */ }
  }

  return { ders, konuMeta, ozet, kitap };
}

function sistemMetni(ders: any, konuMeta: any, ozet: string, kitap: string) {
  const bot = ders.bot?.ad || "Ders Robotu";
  return `Sen ${bot}'sın: ${ders.sinif} ${ders.ders} dersinin yardımcı robotusun. 12-13 yaşındaki ortaokul öğrencileriyle Türkçe konuşuyorsun.

KURALLAR
1. Yalnızca aşağıdaki DERS KİTABI SAYFALARI ve KONU ÖZETİ'ne dayanarak cevap ver. Kitapta olmayan bilgiyi uydurma. Cevap kitapta yoksa "Bu bilgi kitabımızda yok, öğretmenine sorabilirsin." de.
2. Soruyu üç gruptan birine ayır:
   a) Açık konuyla ya da kitap sayfalarıyla bağlantısı varsa (örneğin kitapta geçen bir kelime: hava durumu, navigasyon, GPS) önce kitaptaki bağlantıyı sayfasıyla anlat, sonra gerekirse "Bunun ayrıntısı bu konunun dışında" de.
   b) ${ders.ders} dersiyle ilgili ama bu konuda ve kitap sayfalarında yoksa: "Bu, şu an çalıştığımız konunun dışında. Öğretmenine sorabilir ya da ilgili konuya geldiğimizde bakabiliriz." de.
   c) ${ders.ders} dersiyle hiç ilgisi yoksa (oyun, spor, dizi, başka ders vb.) şunu söyle: "Ben ${ders.ders} dersinin robotu ${bot}'ım, bu konuda yardım edemem. ${ders.ders} ile ilgili ne merak ediyorsun?"
3. Kısa cevap ver: en fazla 4-5 kısa cümle. Basit kelimeler kullan. Gerekirse günlük hayattan bir benzetme yap.
4. Mümkünse kitap sayfasını parantez içinde yaz, örnek: (s. 17).
5. Ödev ya da test sorusunun cevabını hemen verme: önce bir ipucu ver ve düşünmesini iste. Öğrenci iki kez denedikten sonra açıkla.
6. "Bana soru sor" denirse konudan tek bir kolay soru sor, 3 seçenek ver, cevabı bekle.
7. Ad soyad, adres, telefon, okul, şifre gibi kişisel bilgi isteme. Öğrenci yazarsa bunları paylaşmaması gerektiğini nazikçe hatırlat.
8. Öğrenci üzgün ya da korkmuş görünürse veya kendine ya da başkasına zarar vermekten söz ederse nazik ol ve hemen öğretmenine veya ailesine anlatmasını söyle.
9. Övgü kullanma; tek istisna: öğrenci senin sorduğun bir soruyu cevapladığında ya da kendi fikrini yazdığında kısa, çabaya yönelik bir övgü ("Dikkatli düşünmüşsün"). Bilgi sorularına doğrudan cevapla başla.
10. Yaşa uygun olmayan, korkutucu ya da şiddet içeren konulara girme.
11. Başlık, tablo ya da kalın yazı kullanma. Gerekirse en fazla 3 kısa madde yaz.
${ders.bot?.ekTalimat ? `12. ${ders.bot.ekTalimat}\n` : ""}
Açık konu: ${konuMeta.baslik} (${konuMeta.sayfalar})

KONU ÖZETİ
${ozet}

DERS KİTABI SAYFALARI (${ders.kaynak || `MEB ${ders.sinif} ${ders.ders} ders kitabı`})
${kitap || "(Kitap metni yüklenemedi; yalnızca konu özetini kullan.)"}`;
}

async function geminiSor(model: string, sistem: string, mesajlar: Mesaj[], sinyal: AbortSignal) {
  const anahtar = Netlify.env.get("GEMINI_API_KEY");
  if (!anahtar) throw new Error("GEMINI_API_KEY yok");
  const r = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${encodeURIComponent(model)}:generateContent`, {
    method: "POST", signal: sinyal,
    headers: { "Content-Type": "application/json", "x-goog-api-key": anahtar },
    body: JSON.stringify({
      systemInstruction: { parts: [{ text: sistem }] },
      contents: mesajlar.map(m => ({ role: m.rol === "user" ? "user" : "model", parts: [{ text: m.metin }] })),
      generationConfig: { temperature: 0.4, maxOutputTokens: 2048 },
      safetySettings: ["HARM_CATEGORY_HARASSMENT", "HARM_CATEGORY_HATE_SPEECH", "HARM_CATEGORY_SEXUALLY_EXPLICIT", "HARM_CATEGORY_DANGEROUS_CONTENT"]
        .map(category => ({ category, threshold: "BLOCK_LOW_AND_ABOVE" }))
    })
  });
  if (!r.ok) throw new Error(`gemini ${model} ${r.status}`);
  const j: any = await r.json();
  const metin = (j.candidates?.[0]?.content?.parts || []).filter((p: any) => !p.thought).map((p: any) => p.text || "").join("").trim();
  if (!metin) throw new Error(`gemini ${model} boş cevap (${j.candidates?.[0]?.finishReason || j.promptFeedback?.blockReason || "?"})`);
  return metin;
}

async function openrouterSor(model: string, sistem: string, mesajlar: Mesaj[], sinyal: AbortSignal) {
  const anahtar = Netlify.env.get("OPENROUTER_API_KEY");
  if (!anahtar) throw new Error("OPENROUTER_API_KEY yok");
  const r = await fetch("https://openrouter.ai/api/v1/chat/completions", {
    method: "POST", signal: sinyal,
    headers: { "Content-Type": "application/json", Authorization: `Bearer ${anahtar}`, "X-Title": "Ela 7 Dersleri" },
    body: JSON.stringify({
      model, temperature: 0.4, max_tokens: 1200,
      messages: [{ role: "system", content: sistem }, ...mesajlar.map(m => ({ role: m.rol === "user" ? "user" : "assistant", content: m.metin }))]
    })
  });
  if (!r.ok) throw new Error(`openrouter ${model} ${r.status}`);
  const j: any = await r.json();
  const metin = (j.choices?.[0]?.message?.content || "").trim();
  if (!metin) throw new Error(`openrouter ${model} boş cevap`);
  return metin;
}

const sade = (t: string) => t.replace(/\*\*(.+?)\*\*/g, "$1").replace(/^#+\s*/gm, "").replace(/^\s*[*-]\s+/gm, "• ").trim();

async function limitKontrol(): Promise<boolean> {
  const limit = Number(Netlify.env.get("GUNLUK_LIMIT") || 300);
  try {
    const depo = getStore("bot-sayac");
    const gun = new Date().toISOString().slice(0, 10);
    const sayi = Number((await depo.get(gun)) || 0);
    if (sayi >= limit) return false;
    await depo.set(gun, String(sayi + 1));
  } catch { /* sayaç çalışmazsa soruyu engelleme */ }
  return true;
}

export default async (req: Request, context: Context) => {
  if (req.method !== "POST") return json({ hata: "Yalnızca POST" }, 405);
  const url = new URL(req.url);
  const origin = req.headers.get("origin");
  if (origin && new URL(origin).host !== url.host) return json({ hata: "İzin yok" }, 403);

  let govde: any;
  try { govde = await req.json(); } catch { return json({ hata: "Geçersiz istek" }, 400); }
  const dersKod = String(govde?.ders || ""), konuId = String(govde?.konu || "");
  if (!/^[a-z]{2,8}[12]$/.test(dersKod) || !/^u\d{1,2}[kt]\d{1,2}$/.test(konuId)) return json({ hata: "Geçersiz ders veya konu" }, 400);
  const mesajlar: Mesaj[] = (Array.isArray(govde.mesajlar) ? govde.mesajlar : []).slice(-8)
    .filter((m: any) => (m?.rol === "user" || m?.rol === "bot") && typeof m.metin === "string" && m.metin.trim())
    .map((m: any) => ({ rol: m.rol, metin: m.metin.slice(0, 600) }));
  while (mesajlar.length && mesajlar[0].rol !== "user") mesajlar.shift();
  if (!mesajlar.length || mesajlar[mesajlar.length - 1].rol !== "user") return json({ hata: "Soru bulunamadı" }, 400);

  if (!(await limitKontrol())) return json({ hata: "Bugünlük soru hakkı doldu. Yarın tekrar sorabilirsin. Bu arada Merak Kutusu'na bakabilirsin." }, 429);

  let kaynak;
  try { kaynak = await kaynakHazirla(url.origin, dersKod, konuId); } catch (e: any) { return json({ hata: "Konu bilgisi bulunamadı." }, 404); }
  const sistem = sistemMetni(kaynak.ders, kaynak.konuMeta, kaynak.ozet, kaynak.kitap);

  const baslangic = Date.now(), hatalar: string[] = [];
  for (const h of zinciriOku()) {
    const kalan = TOPLAM_SURE_MS - (Date.now() - baslangic);
    if (kalan < 3000) break;
    const kontrol = new AbortController();
    const zamanlayici = setTimeout(() => kontrol.abort(), Math.min(MODEL_SURESI_MS, kalan));
    try {
      const cevap = h.saglayici === "gemini"
        ? await geminiSor(h.model, sistem, mesajlar, kontrol.signal)
        : await openrouterSor(h.model, sistem, mesajlar, kontrol.signal);
      return json({ cevap: sade(cevap), model: `${h.saglayici}:${h.model}` });
    } catch (e: any) {
      hatalar.push(e?.name === "AbortError" ? `${h.model} zaman aşımı` : String(e?.message || e));
    } finally { clearTimeout(zamanlayici); }
  }
  console.log("Tüm modeller başarısız:", hatalar.join(" | "));
  return json({ hata: "" }, 503);
};

export const config: Config = { path: "/api/sor" };
