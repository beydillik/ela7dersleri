// Ela'nın Defteri — bulut (Firebase) katmanı. Derlenmiş hâli: public/ortak/bulut.js (npm run derle).
// defter.js bu modülü yalnızca gerektiğinde (Veli Paneli ya da bağlı öğrenci cihazı) dinamik import ile yükler.
//
// Firestore yapısı:
//   ogrenciler/{ogr}                 {veli: uid, takmaAd, olusturma, cihazlar: [anonim uid], sonKod?, ayar?}
//   ogrenciler/{ogr}/oturumlar/{id}  {oturum, cihaz, bit, olaylar: [...]}   (id = oturum~parça; parça başına en çok 800 olay)
//   ogrenciler/{ogr}/ilerleme/durum  {veri: {"ela7:…": {v: değer (metin; null = silindi), t: ms}}, t}
//   eslestirme/{kod}                 {ogr, veli, son: Timestamp}   (24 saat geçerli, kullanılınca silinir)
// Erişim kuralları: araclar/bulut/firestore.rules (Firebase konsolunda Firestore → Rules'a yapıştırılır).
// İki ayrı Firebase oturumu tutulur: "ogrenci" (cihazın anonim kimliği) ve "veli" (e-posta/şifre).
// Böylece veli, Ela'nın bilgisayarında panele girip çıksa da cihazın bağlantısı kopmaz.
import { initializeApp } from "firebase/app";
import { initializeAuth, browserLocalPersistence, onAuthStateChanged, signInAnonymously, signInWithEmailAndPassword,
  createUserWithEmailAndPassword, signOut, sendPasswordResetEmail } from "firebase/auth";
import { initializeFirestore, doc, getDoc, setDoc, updateDoc, deleteDoc, collection, query, where, getDocs, arrayUnion, Timestamp } from "firebase/firestore/lite";

const AYAR = {
  apiKey: "AIzaSyD_hiij9e2vAbCnorNwuksTVb3epQm8ols",
  authDomain: "ela7dersleri.firebaseapp.com",
  projectId: "ela7dersleri",
  storageBucket: "ela7dersleri.firebasestorage.app",
  messagingSenderId: "878596565149",
  appId: "1:878596565149:web:195338abc0e74681d48c74"
};
const yap = ad => { const app = initializeApp(AYAR, ad);
  return { auth: initializeAuth(app, { persistence: browserLocalPersistence }), db: initializeFirestore(app, { ignoreUndefinedProperties: true }) }; };
const O = yap("ogrenci"), V = yap("veli");
const kim = r => r === "veli" ? V : O;

// Kayıtlı oturumlar geri gelince çözülür
const bekle = a => new Promise(r => { const k = onAuthStateChanged(a, u => { k(); r(u); }); });
export const hazir = Promise.all([bekle(O.auth), bekle(V.auth)]);
export const veli = () => V.auth.currentUser;
export const cihaz = () => O.auth.currentUser;

// ---------- Veli hesabı ----------
export const veliGiris = (e, p) => signInWithEmailAndPassword(V.auth, e, p);
export const veliKayit = (e, p) => createUserWithEmailAndPassword(V.auth, e, p);
export const sifreSifirla = e => sendPasswordResetEmail(V.auth, e);
export const cikis = () => signOut(V.auth);

export async function ogrenciler() {
  const u = V.auth.currentUser; if (!u) return [];
  const s = await getDocs(query(collection(V.db, "ogrenciler"), where("veli", "==", u.uid)));
  return s.docs.map(d => ({ id: d.id, ...d.data() }));
}
export async function ogrenciEkle(takmaAd) {
  const id = "o" + Date.now().toString(36) + Math.random().toString(36).slice(2, 6);
  await setDoc(doc(V.db, "ogrenciler", id), { veli: V.auth.currentUser.uid, takmaAd, olusturma: Date.now(), cihazlar: [] });
  return id;
}
export const ogrenciOku = async (ogr, r) => { const s = await getDoc(doc(kim(r).db, "ogrenciler", ogr)); return s.exists() ? { id: s.id, ...s.data() } : null; };
export const ayarYaz = (ogr, ayar) => updateDoc(doc(V.db, "ogrenciler", ogr), { ayar });
export const cihazlariSifirla = ogr => updateDoc(doc(V.db, "ogrenciler", ogr), { cihazlar: [] });

// Eşleştirme kodu: karışmayan harf ve rakamlardan 6 karakter, 24 saat geçerli
const KOD_HARF = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789";
export async function kodUret(ogr) {
  const a = new Uint32Array(6); crypto.getRandomValues(a);
  const kod = [...a].map(x => KOD_HARF[x % KOD_HARF.length]).join("");
  await setDoc(doc(V.db, "eslestirme", kod), { ogr, veli: V.auth.currentUser.uid, son: Timestamp.fromMillis(Date.now() + 864e5) });
  return kod;
}

// ---------- Öğrenci cihazı ----------
// Cihaz anonim kullanıcı olarak girer ve geçerli kodla öğrencinin cihaz listesine kendini ekler.
export async function cihazBagla(kod) {
  kod = String(kod || "").toUpperCase().replace(/[^A-Z0-9]/g, "");
  if (!O.auth.currentUser) await signInAnonymously(O.auth);
  const k = await getDoc(doc(O.db, "eslestirme", kod));
  if (!k.exists()) throw new Error("Kod bulunamadı. Kodu kontrol et ya da panelden yeni kod üret.");
  const { ogr, son } = k.data();
  if (son.toMillis() < Date.now()) throw new Error("Kodun süresi dolmuş. Panelden yeni kod üret.");
  try { await updateDoc(doc(O.db, "ogrenciler", ogr), { cihazlar: arrayUnion(O.auth.currentUser.uid), sonKod: kod }); }
  catch (e) { if (!(await ogrenciOku(ogr).catch(() => null))) throw e; }   // cihaz zaten listedeyse güncelleme gerekmez
  try { await deleteDoc(doc(O.db, "eslestirme", kod)); } catch (e) {}
  const o = await ogrenciOku(ogr);
  return { ogr, takmaAd: o ? o.takmaAd : "", uid: O.auth.currentUser.uid };
}

// Olayları oturum belgelerine ekler. parcalar: [{id, oturum, cihaz, bit, olaylar}]
export async function oturumYaz(ogr, parcalar) {
  for (const p of parcalar)
    await setDoc(doc(O.db, "ogrenciler", ogr, "oturumlar", p.id), { oturum: p.oturum, cihaz: p.cihaz, bit: p.bit, olaylar: arrayUnion(...p.olaylar) }, { merge: true });
}
export async function oturumlarOku(ogr, sinirMs, r = "veli") {
  const s = await getDocs(query(collection(kim(r).db, "ogrenciler", ogr, "oturumlar"), where("bit", ">=", sinirMs)));
  return s.docs.flatMap(d => d.data().olaylar || []);
}
export async function ilerlemeOku(ogr, r) {
  const s = await getDoc(doc(kim(r).db, "ogrenciler", ogr, "ilerleme", "durum"));
  return s.exists() ? s.data().veri || {} : {};
}
export const ilerlemeYaz = (ogr, degisen) => setDoc(doc(O.db, "ogrenciler", ogr, "ilerleme", "durum"), { veri: degisen, t: Date.now() }, { merge: true });
