import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from ortak import Havuz, ONC
H = Havuz("sos1", 1, "s1"); a = H.add
K1, K2, K3, K4, K5, K6 = "(s. 12–17)", "(s. 18–21)", "(s. 22–29)", "(s. 30–39)", "(s. 40–45)", "(s. 46–50)"

# --- Konu 1: İletişim ve türleri
a("u1k1", "İletişim", "secim", soru="Duygu, düşünce, bilgi ve deneyimlerin karşılıklı olarak paylaşılmasına ne denir?",
  secenekler=["Kültür", "İletişim", "Empati", "Dayanışma"], dogru=1,
  aciklama=f"Karşılıklı paylaşmak iletişimdir {K1}.")
a("u1k1", "Sözsüz İletişim", "eslestir", soru="Örnekleri iletişim türleriyle eşleştir.", ciftler=[
  {"sol": "Arkadaşına telefonda “Günaydın!” demek", "sag": "Sözlü iletişim"},
  {"sol": "Öğretmenine e-posta göndermek", "sag": "Yazılı iletişim"},
  {"sol": "Özür dilerken göz teması kurmak", "sag": "Sözsüz iletişim"}],
  aciklama=f"Konuşma sözlü, yazı yazılı, beden hareketi sözsüz iletişimdir {K1}.")
a("u1k1", "İleti", "kisa", soru="İletişimde karşı tarafa aktarılmak istenen duygu, düşünce veya bilgiye ne denir?", yanit="ileti", kabul=["mesaj"],
  aciklama=f"Aktarılan mesaja ileti denir {K1}.")
a("u1k1", "Kitle İletişim Araçları", "secim", soru="Aşağıdakilerden hangisi bir kitle iletişim aracı değildir?",
  secenekler=["Televizyon", "Gazete", "Radyo", "Okul defteri"], dogru=3,
  aciklama=f"Kitle iletişim araçları geniş kitlelere hızla ulaşır. Defter öyle değildir {K1}.")
a("u1k1", "Birlikte Yaşama", "dy", ifade="Kitap, toplumda birlikte yaşamayı yapboz parçalarının bir bütün oluşturmasına benzetir.", dogru=True,
  aciklama=f"Toplum, yapboz parçaları gibi bir bütündür {K1}.")

# --- Konu 2: Etkili iletişimin yolları
a("u1k2", "Ben Dili", "secim", soru="Aşağıdakilerden hangisi ben dili ile kurulmuş bir cümledir?",
  secenekler=["Sen hep dağınıksın!", "Odanın dağınık olmasından rahatsız oluyorum.", "Beni hiç dinlemiyorsun!", "Sen tembelin tekisin."], dogru=1,
  aciklama=f"Ben dili suçlamaz; davranışı ve kendi duygunu anlatır {K2}.")
a("u1k2", "Empati", "kisa", soru="Kendini karşındaki kişinin yerine koyup olaylara onun gözünden bakmaya ne denir?", yanit="empati",
  aciklama=f"Onun gözünden bakmak empatidir {K2}.")
a("u1k2", "Etkin Dinleme", "dytablo", soru="Etkin dinlemenin göstergesi olanlara D, olmayanlara Y seç.", ifadeler=[
  {"s": "Konuşan kişiyle göz teması kurmak", "d": True},
  {"s": "Arkadaşının sözünü kesmek", "d": False},
  {"s": "Gerektiğinde “Seni anlıyorum.” demek", "d": True},
  {"s": "Dinlerken telefona bakmak", "d": False}],
  aciklama=f"Etkin dinlemede göz teması kurulur, söz kesilmez {K2}.")
a("u1k2", "Beden Dili", "secim", soru="Beden diliyle ilgili aşağıdaki ifadeler verilmiştir.",
  onculler=["Yüzdeki ifadelere mimik denir.", "El, kol ve baş hareketlerine jest denir.", "Gülümsemek olumsuz beden dilidir."],
  kok="Bu ifadelerden hangileri doğrudur?", secenekler=ONC, dogru=1,
  aciklama=f"Gülümsemek, göz teması ve baş sallamak olumlu beden dilidir {K2}.")
a("u1k2", "Farklılıklara Saygı", "secim", soru="Sınıfa İspanya'dan gelen Maria'ya arkadaşları Türkçe öğretti, Maria da kendi kültürünü anlattı. Bu durum en çok hangisine örnektir?",
  secenekler=["Farklılıklara saygı", "Sen dili", "İletişim engeli", "Kitle iletişimi"], dogru=0,
  aciklama=f"Farklılığı zenginlik olarak görmek farklılıklara saygıdır {K2}.")

# --- Konu 3: İletişim engelleri ve olumlu iletişim
a("u1k3", "Sen Dili", "secim", soru="“Beni hiç dinlemiyorsun!” cümlesi hangisine örnektir?",
  secenekler=["Ben dili", "Sen dili", "Empati", "Etkin dinleme"], dogru=1,
  aciklama=f"Sen dili karşıdakini suçlar ve kişiye odaklanır {K3}.")
a("u1k3", "Günlük Hayatta Engeller", "secim", soru="Aşağıdakilerden hangisi etkili iletişimi bozan bir davranış değildir?",
  secenekler=["Sürekli telefonu kontrol etmek", "Sözü kesmek", "Alaycı konuşmak", "Göz teması kurmak"], dogru=3,
  aciklama=f"Göz teması iletişimi güçlendirir. Telefon, söz kesmek, alay bozar {K3}.")
a("u1k3", "Dijital Ortamda Engeller", "dy", ifade="Dijital ortamda net olmayan mesajlar iletişimi engelleyebilir.", dogru=True,
  aciklama=f"Dijitalde mesajın net olmalı; bağlantı kopması da engeldir {K3}.")
a("u1k3", "Barışçıl İletişim", "secim", soru="Kardeşi Ali'nin defterini yanlışlıkla yırttı. Barışçıl iletişime uygun söz hangisidir?",
  secenekler=["Sen hiçbir şeye dikkat etmiyorsun!", "Bir dahaki sefere daha dikkatli ol, olur mu?", "Bir daha odama girme!", "Hep böylesin zaten."], dogru=1,
  aciklama=f"Barışçıl iletişimde kızmak yerine sevgi ve saygıyla konuşulur {K3}.")
a("u1k3", "İletişim Engeli", "bosluk", havuz=["empati", "ileti"], cumleler=[
  {"c": "Mesajın doğru aktarılmasını zorlaştıran her şeye iletişim ___ denir.", "cevap": "engeli"},
  {"c": "Karşıdakini suçlayan konuşma biçimine ___ dili denir.", "cevap": "sen"},
  {"c": "Sabırsızlık ve dikkatsizlik iletişim ___ yol açabilir.", "cevap": "çatışmalarına"}],
  aciklama=f"Engeller ve sen dili iletişimi bozar, çatışma doğurur {K3}.")

# --- Konu 4: Özel gereksinimli bireyler ve fırsat eşitliği
a("u1k4", "Temel İnsan Hakları", "secim", soru="Temel insan haklarıyla ilgili aşağıdaki ifadeler verilmiştir.",
  onculler=["İnsan bu haklara doğduğu andan itibaren sahiptir.", "Bu haklar devredilemez.", "Bu haklardan istenirse vazgeçilebilir."],
  kok="Bu ifadelerden hangileri doğrudur?", secenekler=ONC, dogru=1,
  aciklama=f"Temel haklar doğuştan gelir; devredilemez ve vazgeçilemez {K4}.")
a("u1k4", "Kanun Önünde Eşitlik", "kisa", soru="Herkesin kanun önünde eşit olduğunu söyleyen madde Anayasa'nın kaçıncı maddesidir?", yanit="10", sayi=True,
  aciklama=f"Anayasa'nın 10. maddesi kanun önünde eşitliği düzenler {K4}.")
a("u1k4", "Erişilebilirlik Düzenlemeleri", "secim", soru="Aşağıdakilerden hangisi bir erişilebilirlik düzenlemesi değildir?",
  secenekler=["Rampa", "Asansör", "Kaldırımdaki takip şeridi", "Basamaklı giriş kapısı"], dogru=3,
  aciklama=f"Rampa, asansör ve takip şeridi hareketi kolaylaştırır. Basamak zorlaştırır {K4}.")
a("u1k4", "Fırsat Eşitliği", "dy", ifade="Kız ve erkek öğrencilerin aynı şartlarda eğitim görmesi fırsat eşitliğine örnektir.", dogru=True,
  aciklama=f"Kim olursa olsun herkese aynı fırsat: fırsat eşitliği {K4}.")
a("u1k4", "Sevgi, Şefkat, Merhamet", "eslestir", soru="Değerleri açıklamalarıyla eşleştir.", ciftler=[
  {"sol": "Sevgi", "sag": "İnsanları olduğu gibi kabul etmek"},
  {"sol": "Şefkat", "sag": "İhtiyaç duyulan anda destek olmak"},
  {"sol": "Merhamet", "sag": "Başkalarının zorluklarını anlayıp duyarlı davranmak"}],
  aciklama=f"Kabul et, destek ol, anla {K4}.")

# --- Konu 5: Millî meseleler ve birlik ruhu
a("u1k5", "Millî Mücadele", "secim", soru="Mustafa Kemal Millî Mücadele'yi başlatmak için hangi tarihte Samsun'a çıktı?",
  secenekler=["23 Nisan 1920", "19 Mayıs 1919", "29 Ekim 1923", "30 Ağustos 1922"], dogru=1,
  aciklama=f"19 Mayıs 1919'da Samsun'a çıkıldı {K5}.")
a("u1k5", "Tekâlif-i Millîye Emirleri", "secim", soru="Millî Mücadele'de halkın yiyecek, giyecek ve araçlarını orduyla paylaşmasını sağlayan düzenleme hangisidir?",
  secenekler=["Tekâlif-i Millîye Emirleri", "Orhun Yazıtları", "Anayasa'nın 10. maddesi", "Mavi Vatan"], dogru=0,
  aciklama=f"Tekâlif-i Millîye ile halk elindekini orduyla paylaştı {K5}.")
a("u1k5", "Millî Mesele", "dy", ifade="Millî meseleler yalnızca devlet yöneticilerini ilgilendirir.", dogru=False,
  duzeltme="Millî meseleler toplumun tüm bireylerini ilgilendirir.",
  aciklama=f"Millî mesele hepimizi ilgilendirir {K5}.")
a("u1k5", "Darbe Girişimine Karşı Birlik", "secim", soru="Her yıl 15 Temmuz hangi adla anılır?",
  secenekler=["Demokrasi ve Millî Birlik Günü", "Cumhuriyet Bayramı", "Zafer Bayramı", "Gençlik ve Spor Bayramı"], dogru=0,
  aciklama=f"15 Temmuz, Demokrasi ve Millî Birlik Günü olarak anılır {K5}.")
a("u1k5", "Afetlerde Dayanışma", "secim", soru="6 Şubat 2023 depremlerinden sonra yaşananlar en çok hangisine örnektir?",
  secenekler=["İletişim engeli", "Birlik ve dayanışma", "Sen dili", "Erişilebilirlik"], dogru=1,
  aciklama=f"Devlet, kurumlar ve vatandaşlar birlikte çalıştı: tüm Türkiye tek yürek oldu {K5}.")

# --- Konu 6: Millî başarılar, kimlik, vatan sevgisi
a("u1k6", "Bilim ve Teknolojide Millî Başarılar", "secim", soru="DNA onarımı çalışmalarıyla Nobel Kimya Ödülü kazanan Türk bilim insanı kimdir?",
  secenekler=["Alper Gezeravcı", "Aziz Sancar", "Mete Gazoz", "Derya Türkan"], dogru=1,
  aciklama=f"Aziz Sancar Nobel Kimya Ödülü kazandı {K6}.")
a("u1k6", "Mavi, Yeşil ve Gök Vatan", "eslestir", soru="Kavramları anlamlarıyla eşleştir.", ciftler=[
  {"sol": "Mavi Vatan", "sag": "Denizlerimiz"},
  {"sol": "Yeşil Vatan", "sag": "Ormanlarımız"},
  {"sol": "Gök Vatan", "sag": "Hava sahamız"}],
  aciklama=f"Mavi deniz, yeşil orman, gök hava sahasıdır {K6}.")
a("u1k6", "Millî Kimlik", "secim", soru="Aşağıdakilerden hangisi millî kimliği oluşturan unsurlardan biri değildir?",
  secenekler=["Dil", "Tarih", "Kültür", "Ayakkabı numarası"], dogru=3,
  aciklama=f"Millî kimlik soy, dil, din, tarih, vatan ve kültürden oluşur {K6}.")
a("u1k6", "Vatanseverlik", "dy", ifade="Vatanseverlik yalnızca savaş zamanında gösterilir.", dogru=False,
  duzeltme="Vatanseverlik barış zamanında da vatandaşlık sorumluluklarını yerine getirmektir.",
  aciklama=f"Barışta da vatan sevgisi gösterilir: spor, sanat, bilimde {K6}.")
a("u1k6", "Orhun Yazıtları", "secim", soru="Türk milletinin birliğini, yöneticilerin sorumluluklarını ve vatan sevgisini anlatan yazıtlar hangileridir?",
  secenekler=["Orhun Yazıtları", "Tekâlif-i Millîye", "Braille alfabesi", "Anayasa"], dogru=0,
  aciklama=f"Orhun Yazıtları millî kimlik bilincinin güzel bir örneğidir {K6}.")
H.yaz()
