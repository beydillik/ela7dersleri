"""Türkçe (tr1) okuma yaklaşımı — 3. tema u3k1–u3k8 (17 Kasım 2026, Kemal'in onayı).
İlk dönem kapsamı (ders ders anlaşıldı): konu başına 3 ikiz çift; "Bu soru senden ne istiyor?" (NE) yalnız ikizlere.
NE'siz test sorularında motor dokunma yerine soru kelimesini sarı gösterir. Kanıtlı sorular testte hep sorulur (TESTSORU).
İkiz kuralı: eşin doğru cevabı çeldiricilerden birinde (gerekirse eski sorunun çeldiricisi _eski ile değiştirildi);
ipucu eşin cevabını söylemez. Sayfalar kavram kartlarından ve kitap metninden (kaynaklar/tr1/unite3.md)."""
import json

def _q(konu, bas):
    d = json.load(open(f"public/tr1/konular/{konu}.json", encoding="utf-8"))
    l = [q for q in d["sorular"] if q["soru"].startswith(bas)]
    assert len(l) == 1, (konu, bas, len(l))
    return l[0]

def _S(konu, bas): return _q(konu, bas)["soru"]

def _eski(konu, bas, degis, aciklama=None):
    """Eski sorunun bir çeldiricisini ikiz eşinin cevabıyla değiştirir (doğru şık ve öteki alanlar aynı kalır)."""
    q = _q(konu, bas)
    y = {k: q[k] for k in ("soru", "secenekler", "dogru", "ipucu", "aciklama", "kavram", "yardim") if k in q}
    if aciklama: y["aciklama"] = aciklama
    y["secenekler"] = [degis.get(s, s) for s in q["secenekler"]]
    assert y["secenekler"][y["dogru"]] == q["secenekler"][q["dogru"]]
    return y

# --- eski sorular (tam metin) ---
K1a, K1b, K1c = _S("u3k1", "Hangisi bir hikâye unsuru değil"), _S("u3k1", "Hasan'ın eskici gidince"), _S("u3k1", "Yalnız ve kırgın")
K2a, K2b, K2c = _S("u3k2", "Hangisi öznel bir"), _S("u3k2", "Hangi cümlede “yüz” kelimesi sayı"), _S("u3k2", "Hangisi bir deyimdir")
K3a, K3b, K3c = _S("u3k3", "Bir metnin giriş"), _S("u3k3", "“Yazın günler"), _S("u3k3", "“Kış geldi")
K4a, K4b = _S("u3k4", "Kitaptaki grafiğe göre arama sayısının en yüksek"), _S("u3k4", "Hangisi bir farklılık")
K5a, K5b, K5c = _S("u3k5", "Hangi cümlede yargı gerçekleşme anında oluyor"), _S("u3k5", "Hangi cümle bir alışkanlığı"), _S("u3k5", "“Bu akşam komşularımız")
K6a, K6b, K6c = _S("u3k6", "Hangi cümlede pekiştirmeli"), _S("u3k6", "“Mavi” kelimesinin pekiştirilmiş"), _S("u3k6", "Hangi cümlede yazım yanlışı vardır")
K7a, K7b, K7c = _S("u3k7", "Hangi cümlede kısa çizgi"), _S("u3k7", "Hangisinde eğik çizgi bir ekin"), _S("u3k7", "Hangi cümlede işaret yanlış")
K8a, K8b, K8c = _S("u3k8", "Hangi dizede benzetme"), _S("u3k8", "“Ağlamaktan gözlerimden"), _S("u3k8", "Kitaptaki “Söz Söyle”")

# --- yeni ikiz soruları ---
N1a = "Hangisi bir hikâye unsurudur?"
N1b = "Hasan'ın vapurda bir durgunluk yaşamasının sebebi nedir?"
N1c = "Sevinen ve kendini güvende hisseden biri çoğunlukla nasıl davranır?"
N2a = "Hangisi nesnel bir ifadedir?"
N2b = "Hangi cümlede “yüz” kelimesi surat anlamında kullanılmıştır?"
N2c = "Hangisi bir kalıp ifadedir?"
N3a = "Bir metnin sonuç bölümüyle ilgili hangisi doğrudur?"
N3b = "“Bulutlar pamuk gibi beyazdı.” cümlesinde hangi yol kullanılmıştır?"
N3c = "“Hava çok soğuktu. ___ Ali montunu giymedi.” Boşluğa hangisi gelirse akış bozulmaz?"
N4a = "Kitaptaki grafiğe göre arama sayısının en düşük olduğu yıl hangisidir?"
N4b = "Hangisi bir benzerlik cümlesidir?"
N4c = "Kitaptaki grafikte yatay eksende ne gösterilir?"
N4d = "Kitaptaki grafikte dikey eksende ne gösterilir?"
N5a = "Hangi cümlede yargı gerçekleşme anından sonrasını gösteriyor?"
N5b = "Hangi cümle yargının gerçekleşme anından öncesini anlatır?"
N5c = "“Dün akşam komşularımız bize .......” Boşluğa hangisi gelirse yargı gerçekleşme anından öncesini gösterir?"
N6a = "Hangi cümlede ikileme vardır?"
N6b = "“Mavi” kelimesinin ikilemeli hâli hangisidir?"
N6c = "Hangi cümlede yazım yanlışı yoktur?"
N7a = "Hangi cümlede eğik çizgi adreste kullanılmıştır?"
N7b = "Hangisinde eğik çizgi bir tarihi göstermektedir?"
N7c = "Hangi cümlede işaret doğru kullanılmıştır?"
N8a = "Hangi dizede kişileştirme vardır?"
N8b = "“Annem bir melek gibi uyuyordu.” cümlesindeki söz sanatı hangisidir?"
N8c = "Karacaoğlan'ın “Öğüt” şiiri kaç dörtlükten oluşur?"

EKSORU = {
 "u3k1": [
  {"soru": N1a, "secenekler": ["Sayfa numarası", "Zaman", "Kitabın fiyatı"], "dogru": 1,
   "ipucu": "Hikâye Unsurları kartındaki dört soruyu hatırla: Ne, kim, nerede, ne zaman?",
   "aciklama": "Hikâyenin dört unsuru vardır: olay, şahıs ve varlık kadrosu, mekân ve zaman (s. 130).", "kavram": "Hikâye Unsurları"},
  {"soru": N1b, "secenekler": ["Kalan yolcuların bilmediği bir dilde konuşması", "Bir daha Türkçe konuşacak kimse bulamayacağını düşünmesi", "Halasının ona kızması"], "dogru": 0,
   "ipucu": "Vapurda önce eğleniyordu. Çevresinde ne değişti?",
   "aciklama": "Kalan yolcular bilmediği bir dilde konuşmaya başlayınca Hasan'ı bir durgunluk alır (s. 122).", "kavram": "Duygunun Sebebi"},
  _eski("u3k1", "Hasan'ın eskici gidince", {"Ayakkabıları beğenmemesi": "Kalan yolcuların bilmediği bir dilde konuşması", "Yolcuların bilmediği bir dilde konuşmaya başlaması": "Kalan yolcuların bilmediği bir dilde konuşması"}),
  {"soru": N1c, "secenekler": ["Konuşur, anlatır.", "Susar, az konuşur.", "Herkesten saklanır."], "dogru": 0,
   "ipucu": "Eskici Türkçe konuşunca Hasan ne yaptı?",
   "aciklama": "Sevinen ve güvenen kişi konuşur; eskici Türkçe konuşunca altı aydır susan Hasan durmadan konuştu (s. 125).", "kavram": "Duygunun İletişime Etkisi"},
  _eski("u3k1", "Yalnız ve kırgın", {"Sürekli şarkı söyler.": "Konuşur, anlatır."}),
 ],
 "u3k2": [
  {"soru": N2a, "secenekler": ["Bu şiir okuduğum en etkileyici şiir.", "Şiir dört dörtlükten oluşuyor.", "Bence bu şiirin başlığı çok güzel."], "dogru": 1,
   "ipucu": "Hangisinin doğruluğunu herkes sayarak kontrol edebilir?",
   "aciklama": "Dörtlük sayısı herkesçe kontrol edilebilir; nesneldir. “En etkileyici” ve “bence” kişisel görüştür (s. 138).", "kavram": "Öznel ve Nesnel İfade"},
  {"soru": N2b, "secenekler": ["Yüz sayfalık kitabı bitirdi.", "Yüzünü soğuk suyla yıkadı.", "Yüz metre koştu."], "dogru": 1,
   "ipucu": "Hangisinde “yüz” bir sayı değil?",
   "aciklama": "“Yüzünü yıkadı”da yüz surat demektir; öbürlerinde sayıdır. Yazılışı aynı, anlamı farklı: eş sesli (s. 136).", "kavram": "Eş Sesli Kelimeler"},
  {"soru": N2c, "secenekler": ["göz kulak olmak", "Geçmiş olsun", "kitap okumak"], "dogru": 1,
   "ipucu": "Belli bir durumda hep aynı biçimde söylenen hazır söz hangisi?",
   "aciklama": "“Geçmiş olsun” hasta birine hep aynı biçimde söylenen hazır bir sözdür; “göz kulak olmak” deyimdir. Kitapta «hayırlı olsun», «günaydın» gibi kalıp ifadeler var (s. 134–135); ayrım s. 138'de.", "kavram": "Kalıp İfade"},
  _eski("u3k2", "Hangisi bir deyimdir", {"su içmek": "Geçmiş olsun"}, "“Göz kulak olmak” korumak, kollamak demektir; kalıplaşmış bir deyimdir. “Geçmiş olsun” ise kalıp ifadedir; yazar metinde dilek sözlerine “deyim” dese de kitap bu ikisini ayırır (s. 134, 138)."),
 ],
 "u3k3": [
  {"soru": N3a, "secenekler": ["Konuyu tanıtır, ilgi çeker.", "Ana fikri toparlayarak bitirir.", "Metnin en uzun bölümüdür."], "dogru": 1,
   "ipucu": "“Sonuç olarak” ile başlayan paragraf ne yapıyordu?",
   "aciklama": "Sonuç anlatılanları toparlar ve ana fikri bir kez daha vurgular (s. 167).", "kavram": "Sonuç"},
  {"soru": N3b, "secenekler": ["Benzetme", "Karşılaştırma", "Tanımlama"], "dogru": 0,
   "ipucu": "Cümledeki ipucu kelimeyi bul.",
   "aciklama": "“gibi” benzetmenin ipucudur: Bulutlar beyazlıkta pamuğa benzetilmiş (s. 137).", "kavram": "Yolu Metinde Bulma"},
  {"soru": N3c, "secenekler": ["Bu yüzden", "Oysa", "Örneğin"], "dogru": 1,
   "ipucu": "Soğukta mont giymemek beklenen bir şey mi?",
   "aciklama": "Soğukta mont giymemek beklenenin tersidir; karşıt düşünceyi “oysa” bağlar (s. 167).", "kavram": "Bölümler Arası Akış"},
 ],
 "u3k4": [
  {"soru": N4a, "secenekler": ["2016", "2014", "2010"], "dogru": 0,
   "ipucu": "En kısa çubuğa bak.",
   "aciklama": "En düşük değer 2016'daki 2.223'tür; en yüksek 2010'daki 45.172'dir (s. 151).", "kavram": "Grafik Okuma"},
  {"soru": N4b, "secenekler": ["İki metin de saygıyı önemser.", "Birinci metin aileyi anlatır; ikincisi ise sanal ortamı.", "Birinci metin kısa, ikincisi ise uzundur."], "dogru": 0,
   "ipucu": "Ortak yönü gösteren kelimeyi ara.",
   "aciklama": "“İki metin de” ortak bir yönü gösterir; bu bir benzerliktir. “ise” ile kurulanlar farklılıktır (s. 150).", "kavram": "Benzerlik ve Farklılık"},
  {"soru": N4c, "secenekler": ["Yıllar", "Arama sayısı", "Grafiğin başlığı"], "dogru": 0,
   "ipucu": "Yatay eksen grafiğin altında, soldan sağa uzanır. Altında ne yazıyordu?",
   "aciklama": "Kitaptaki grafikte yatay eksende yıllar, dikey eksende arama sayısı vardır (s. 151).", "kavram": "Grafik Okuma"},
  {"soru": N4d, "secenekler": ["Yıllar", "Arama sayısı", "Grafiğin başlığı"], "dogru": 1,
   "ipucu": "Dikey eksen grafiğin solunda, aşağıdan yukarı uzanır. Üzerinde hangi sayılar vardı?",
   "aciklama": "Kitaptaki grafikte yatay eksende yıllar, dikey eksende arama sayısı vardır (s. 151).", "kavram": "Grafik Okuma"},
 ],
 "u3k5": [
  {"soru": N5a, "secenekler": ["Kardeşim dün resim yaptı.", "Kardeşim şu an resim yapıyor.", "Kardeşim yarın resim yapacak."], "dogru": 2,
   "ipucu": "Henüz olmamış işi anlatan fiil ekini bul.",
   "aciklama": "“yap-acak” ve “yarın”: İş henüz olmadı, sonra olacak (s. 141).", "kavram": "Gerçekleşme Anından Sonrası"},
  {"soru": N5b, "secenekler": ["Ali bu sabah erken kalktı.", "Ali şimdi kahvaltı ediyor.", "Ali her sabah erken kalkar."], "dogru": 0,
   "ipucu": "Konuştuğumuz andan önce olmuş, bitmiş işi bul.",
   "aciklama": "“kalk-tı” ve “bu sabah”: İş konuştuğumuz andan önce olmuş (s. 141).", "kavram": "Gerçekleşme Anından Öncesi"},
  {"soru": N5c, "secenekler": ["geldi", "gelir", "gelecek"], "dogru": 0,
   "ipucu": "“Dün akşam” ne zamanı gösterir? Fiilin eki de aynı zamanı göstermeli.",
   "aciklama": "“gel-di” ve “dün akşam”: İş önceden olmuş; gerçekleşme anından öncesi (s. 141).", "kavram": "Gerçekleşme Anından Öncesi"},
 ],
 "u3k6": [
  {"soru": N6a, "secenekler": ["Odası tertemiz olmuştu.", "Odası temiz temiz kokuyordu.", "Odası çok güzeldi."], "dogru": 1,
   "ipucu": "Aynı kelimenin ayrı ayrı iki kez yazıldığı cümleyi ara.",
   "aciklama": "“temiz temiz” ikilemedir, ayrı yazılır; “tertemiz” pekiştirmedir, bitişik yazılır (pekiştirme: s. 131; ikileme: 1. Tema).", "kavram": "Pekiştirmeler Bitişik Yazılır"},
  {"soru": N6b, "secenekler": ["mavi mavi", "masmavi", "mavimsi"], "dogru": 0,
   "ipucu": "İkilemede kelime ayrı ayrı iki kez söylenir.",
   "aciklama": "“mavi mavi” ikilemedir, ayrı yazılır; “masmavi” pekiştirmedir (pekiştirme: s. 131; ikileme: 1. Tema).", "kavram": "Pekiştirmeler Bitişik Yazılır"},
  {"soru": N6c, "secenekler": ["Düşüncelerini dos doğru anlattı.", "Kitabın sayfaları sap sarı olmuştu.", "Gökyüzü masmavi görünüyordu."], "dogru": 2,
   "ipucu": "Pekiştirmeler nasıl yazılıyordu: ayrı mı, bitişik mi?",
   "aciklama": "Pekiştirmeler bitişik yazılır: dosdoğru, sapsarı, masmavi (s. 131).", "kavram": "Pekiştirmeler Bitişik Yazılır"},
 ],
 "u3k7": [
  {"soru": N7a, "secenekler": ["Türk-Japon dostluğu çok eskidir.", "Öğretmen kelimeyi a-ğaç diye heceledi.", "Adresi Kızılay/Ankara diye yazdı."], "dogru": 2,
   "ipucu": "Adreste semt ile şehir arasına hangi işaret konuyordu?",
   "aciklama": "Adreste semt ile şehir arasına eğik çizgi konur: Kızılay/Ankara (s. 163).", "kavram": "Eğik Çizgi: Adres"},
  {"soru": N7b, "secenekler": ["-madan/-meden", "Kurtuluş/Ankara", "12/04/2025"], "dogru": 2,
   "ipucu": "Gün, ay ve yıl hangisinde var?",
   "aciklama": "12/04/2025 gün, ay ve yılı gösterir: 12 Nisan 2025 (s. 163).", "kavram": "Eğik Çizgi: Tarih"},
  {"soru": N7c, "secenekler": ["Toplantı 10.00/12.00 arasında yapılacak.", "İstanbul/İzmir otobüsü kalktı.", "Mektubu 05/09/2026 tarihinde yazdım."], "dogru": 2,
   "ipucu": "Saat aralığı ve iki şehir arası hangi işaretle yazılıyordu?",
   "aciklama": "Tarihte eğik çizgi kullanılır. Saat aralığı ve iki şehir arası kısa çizgiyle yazılır: 10.00-12.00, İstanbul-İzmir (s. 142, 163).", "kavram": "Kısa Çizgi mi, Eğik Çizgi mi?"},
 ],
 "u3k8": [
  {"soru": N8a, "secenekler": ["Bulutlar pamuk gibi yumuşacıktı.", "Yıldızlar bize göz kırptı.", "Bin yıl bekledim seni."], "dogru": 1,
   "ipucu": "İnsana ait bir davranış hangi varlığa verilmiş?",
   "aciklama": "Göz kırpmak insana aittir; yıldızlara verilmiş: kişileştirme (s. 160).", "kavram": "Dizede Kişileştirme"},
  {"soru": N8b, "secenekler": ["Benzetme", "Kişileştirme", "Abartma"], "dogru": 0,
   "ipucu": "Cümlede “gibi” var mı?",
   "aciklama": "“gibi” var; anne uyurken meleğe benzetilmiş: benzetme (s. 160).", "kavram": "Dizede Benzetme"},
  {"soru": N8c, "secenekler": ["Dört", "Beş", "Altı"], "dogru": 1,
   "ipucu": "Soru bir dörtlükteki mısraları değil, dörtlüklerin sayısını soruyor.",
   "aciklama": "“Öğüt” 5 dörtlükten oluşur; her dörtlükte 4 mısra vardır (s. 156).", "kavram": "Şiirin Bölümleri ve Mısra Sayısı"},
  _eski("u3k8", "Kitaptaki “Söz Söyle”", {"Altı": "Beş"}),
 ],
}

IKIZ = {
 "u3k1": [[K1a, N1a], [K1b, N1b], [K1c, N1c]],
 "u3k2": [[K2a, N2a], [K2b, N2b], [K2c, N2c]],
 "u3k3": [[K3a, N3a], [K3b, N3b], [K3c, N3c]],
 "u3k4": [[K4a, N4a], [K4b, N4b], [N4c, N4d]],
 "u3k5": [[K5a, N5a], [K5b, N5b], [K5c, N5c]],
 "u3k6": [[K6a, N6a], [K6b, N6b], [K6c, N6c]],
 "u3k7": [[K7a, N7a], [K7b, N7b], [K7c, N7c]],
 "u3k8": [[K8a, N8a], [K8b, N8b], [K8c, N8c]],
}

# Testte sorulan sayı eskisi gibi 10 (kanıtlı 3 soru hep sorulur, kalan 7 havuzdan; en çok 2–3 ikiz çifti)
TESTSORU = {k: 10 for k in IKIZ}

NE = {
 K1a: ["Hikâye unsuru olmayanı", "Hikâye unsuru olanı"], N1a: ["Hikâye unsuru olanı", "Hikâye unsuru olmayanı"],
 K1b: ["Hasan'ın eskici gidince ağlama sebebini", "Hasan'ın vapurda durgunlaşma sebebini"], N1b: ["Hasan'ın vapurda durgunlaşma sebebini", "Hasan'ın eskici gidince ağlama sebebini"],
 K1c: ["Yalnız ve kırgın birinin davranışını", "Sevinen ve güvenen birinin davranışını"], N1c: ["Sevinen ve güvenen birinin davranışını", "Yalnız ve kırgın birinin davranışını"],
 K2a: ["Öznel olan ifadeyi", "Nesnel olan ifadeyi"], N2a: ["Nesnel olan ifadeyi", "Öznel olan ifadeyi"],
 K2b: ["“Yüz”ün sayı anlamında geçtiği cümleyi", "“Yüz”ün surat anlamında geçtiği cümleyi"], N2b: ["“Yüz”ün surat anlamında geçtiği cümleyi", "“Yüz”ün sayı anlamında geçtiği cümleyi"],
 K2c: ["Deyim olanı", "Kalıp ifade olanı"], N2c: ["Kalıp ifade olanı", "Deyim olanı"],
 K3a: ["Giriş bölümü hakkında doğru bilgiyi", "Sonuç bölümü hakkında doğru bilgiyi"], N3a: ["Sonuç bölümü hakkında doğru bilgiyi", "Giriş bölümü hakkında doğru bilgiyi"],
 K3b: ["“Daha uzundur” cümlesindeki yolu", "“Pamuk gibi” cümlesindeki yolu"], N3b: ["“Pamuk gibi” cümlesindeki yolu", "“Daha uzundur” cümlesindeki yolu"],
 K3c: ["Kış ve kar cümlelerini bağlayan ifadeyi", "Soğuk ve mont cümlelerini bağlayan ifadeyi"], N3c: ["Soğuk ve mont cümlelerini bağlayan ifadeyi", "Kış ve kar cümlelerini bağlayan ifadeyi"],
 K4a: ["Arama sayısının en yüksek olduğu yılı", "Arama sayısının en düşük olduğu yılı"], N4a: ["Arama sayısının en düşük olduğu yılı", "Arama sayısının en yüksek olduğu yılı"],
 K4b: ["Farklılık anlatan cümleyi", "Benzerlik anlatan cümleyi"], N4b: ["Benzerlik anlatan cümleyi", "Farklılık anlatan cümleyi"],
 N4c: ["Yatay eksenin gösterdiğini", "Dikey eksenin gösterdiğini"], N4d: ["Dikey eksenin gösterdiğini", "Yatay eksenin gösterdiğini"],
 K5a: ["Şu an olan işi anlatan cümleyi", "Sonra olacak işi anlatan cümleyi"], N5a: ["Sonra olacak işi anlatan cümleyi", "Şu an olan işi anlatan cümleyi"],
 K5b: ["Her zaman olan işi anlatan cümleyi", "Önceden olmuş işi anlatan cümleyi"], N5b: ["Önceden olmuş işi anlatan cümleyi", "Her zaman olan işi anlatan cümleyi"],
 K5c: ["Akşam olacak işi gösteren fiili", "Dün olmuş işi gösteren fiili"], N5c: ["Dün olmuş işi gösteren fiili", "Akşam olacak işi gösteren fiili"],
 K6a: ["Pekiştirmeli kelimenin geçtiği cümleyi", "İkilemenin geçtiği cümleyi"], N6a: ["İkilemenin geçtiği cümleyi", "Pekiştirmeli kelimenin geçtiği cümleyi"],
 K6b: ["“Mavi”nin pekiştirilmiş hâlini", "“Mavi”nin ikilemeli hâlini"], N6b: ["“Mavi”nin ikilemeli hâlini", "“Mavi”nin pekiştirilmiş hâlini"],
 K6c: ["Yazım yanlışı olan cümleyi", "Yazım yanlışı olmayan cümleyi"], N6c: ["Yazım yanlışı olmayan cümleyi", "Yazım yanlışı olan cümleyi"],
 K7a: ["Kısa çizginin “ile” anlamında geçtiği cümleyi", "Eğik çizginin adreste geçtiği cümleyi"], N7a: ["Eğik çizginin adreste geçtiği cümleyi", "Kısa çizginin “ile” anlamında geçtiği cümleyi"],
 K7b: ["Bir ekin biçimlerini gösteren eğik çizgiyi", "Bir tarihi gösteren eğik çizgiyi"], N7b: ["Bir tarihi gösteren eğik çizgiyi", "Bir ekin biçimlerini gösteren eğik çizgiyi"],
 K7c: ["İşaretin yanlış kullanıldığı cümleyi", "İşaretin doğru kullanıldığı cümleyi"], N7c: ["İşaretin doğru kullanıldığı cümleyi", "İşaretin yanlış kullanıldığı cümleyi"],
 K8a: ["Benzetme olan dizeyi", "Kişileştirme olan dizeyi"], N8a: ["Kişileştirme olan dizeyi", "Benzetme olan dizeyi"],
 K8b: ["Irmak cümlesindeki söz sanatını", "Melek cümlesindeki söz sanatını"], N8b: ["Melek cümlesindeki söz sanatını", "Irmak cümlesindeki söz sanatını"],
 K8c: ["Bir bölümdeki mısra sayısını", "Şiirdeki bölüm sayısını"], N8c: ["Şiirdeki dörtlük sayısını", "Bir dörtlükteki mısra sayısını"],
}

# İkizlerde farkı yaratan sözcük + soru kelimesi sarı
VURGU = {
 K1a: ["Hangisi", "değildir"], N1a: ["Hangisi", "hikâye unsurudur"],
 K1b: ["eskici gidince", "sebebi nedir"], N1b: ["vapurda", "sebebi nedir"],
 K1c: ["Yalnız ve kırgın", "nasıl davranır"], N1c: ["Sevinen ve kendini güvende", "nasıl davranır"],
 K2a: ["Hangisi", "öznel"], N2a: ["Hangisi", "nesnel"],
 K2b: ["sayı anlamında"], N2b: ["surat anlamında"],
 K2c: ["Hangisi", "deyimdir"], N2c: ["Hangisi", "kalıp ifadedir"],
 K3a: ["giriş bölümüyle", "hangisi doğrudur"], N3a: ["sonuç bölümüyle", "hangisi doğrudur"],
 K3b: ["göre daha uzundur", "hangi yol"], N3b: ["pamuk gibi", "hangi yol"],
 K3c: ["Kış geldi", "karla kaplandı", "Boşluğa hangisi"], N3c: ["çok soğuktu", "giymedi", "Boşluğa hangisi"],
 K4a: ["en yüksek", "hangisidir"], N4a: ["en düşük", "hangisidir"],
 K4b: ["Hangisi", "farklılık"], N4b: ["Hangisi", "benzerlik"],
 N4c: ["yatay eksende", "ne gösterilir"], N4d: ["dikey eksende", "ne gösterilir"],
 K5a: ["gerçekleşme anında"], N5a: ["gerçekleşme anından sonrasını"],
 K5b: ["alışkanlığı", "sürekliliğini"], N5b: ["gerçekleşme anından öncesini"],
 K5c: ["Bu akşam", "sonrasını"], N5c: ["Dün akşam", "öncesini"],
 K6a: ["pekiştirmeli"], N6a: ["ikileme"],
 K6b: ["pekiştirilmiş hâli"], N6b: ["ikilemeli hâli"],
 K6c: ["yazım yanlışı vardır"], N6c: ["yazım yanlışı yoktur"],
 K7a: ["kısa çizgi", "“ile” anlamında"], N7a: ["eğik çizgi", "adreste"],
 K7b: ["ekin farklı biçimlerini"], N7b: ["tarihi"],
 K7c: ["yanlış kullanılmıştır"], N7c: ["doğru kullanılmıştır"],
 K8a: ["benzetme"], N8a: ["kişileştirme"],
 K8b: ["ırmaklar aktı", "söz sanatı"], N8b: ["melek", "söz sanatı"],
 K8c: ["bir bölümde kaç mısra"], N8c: ["kaç dörtlükten"],
}

# Yeni soruların "sorunun kalbi" bölgeleri
BOLGE = {
 N1a: "TUM", N1b: ["durgunluk yaşamasının sebebi nedir"], N1c: ["çoğunlukla nasıl davranır"],
 N2a: "TUM", N2b: ["surat anlamında kullanılmıştır"], N2c: "TUM",
 N3a: ["sonuç bölümüyle ilgili hangisi doğrudur"], N3b: ["hangi yol kullanılmıştır"], N3c: ["Boşluğa hangisi gelirse akış bozulmaz"],
 N4a: ["en düşük olduğu yıl hangisidir"], N4b: "TUM", N4c: ["yatay eksende ne gösterilir"], N4d: ["dikey eksende ne gösterilir"],
 N5a: ["gerçekleşme anından sonrasını gösteriyor"], N5b: ["gerçekleşme anından öncesini anlatır"], N5c: ["gerçekleşme anından öncesini gösterir"],
 N6a: "TUM", N6b: ["ikilemeli hâli hangisidir"], N6c: ["yazım yanlışı yoktur"],
 N7a: ["eğik çizgi adreste kullanılmıştır"], N7b: ["eğik çizgi bir tarihi göstermektedir"], N7c: ["işaret doğru kullanılmıştır"],
 N8a: "TUM", N8b: ["söz sanatı hangisidir"], N8c: ["kaç dörtlükten oluşur"],
}
