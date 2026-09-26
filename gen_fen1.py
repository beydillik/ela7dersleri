"""Fen1 ders ayarlarını ve u1k1 konu dosyasını üretir (v2 şeması)."""
import json, os, shutil

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "public", "fen1")
os.makedirs(os.path.join(OUT, "konular"), exist_ok=True)

# Kavram çizimleri önceki sürümden alınır
v1 = json.load(open(os.path.join(BASE, "..", "fen_defteri", "konular", "u1k1.json"), encoding="utf-8"))
SVG = {k["ad"]: k["svg"] for k in v1["kavramlar"]}

KUARK = ("<svg viewBox='0 0 64 64' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Kuark'>"
         "<circle cx='32' cy='32' r='32' fill='#ff7a33'/>"
         "<ellipse cx='32' cy='36' rx='26' ry='9' fill='none' stroke='#f2c14e' stroke-width='2.5' transform='rotate(-18 32 36)'/>"
         "<path d='M32 8v8' stroke='#1b2340' stroke-width='3' stroke-linecap='round'/><circle cx='32' cy='7' r='4' fill='#f2c14e'/>"
         "<rect x='16' y='16' width='32' height='28' rx='10' fill='#f5f6fa'/>"
         "<rect x='20' y='22' width='24' height='13' rx='6' fill='#1b2340'/>"
         "<circle cx='27' cy='28.5' r='3.2' fill='#8ee3d6'/><circle cx='37' cy='28.5' r='3.2' fill='#8ee3d6'/>"
         "<path d='M27 39q5 3.5 10 0' stroke='#1b2340' stroke-width='2.2' fill='none' stroke-linecap='round'/>"
         "<rect x='22' y='44' width='20' height='10' rx='4' fill='#1b2340'/><circle cx='32' cy='49' r='2.5' fill='#f2c14e'/></svg>")

ders = {
  "kod": "fen1", "ders": "Fen Bilimleri", "sinif": "7. Sınıf", "donem": "1. Dönem",
  "bot": {
    "ad": "Kuark", "svg": KUARK,
    "karsilama": "Merhaba! Ben Kuark, Fen Bilimleri robotuyum. Şu an \"{konu}\" konusundayız. Ne merak ediyorsun?",
    "oneriler": ["Bu konuyu bana kısaca anlat", "Bir örnekle açıklar mısın?", "Bana kolay bir soru sor", "Hangi kavramlar önemli?"]
  },
  "uniteler": [
    {"ad": "1. Ünite: Uzay Çağı", "no": 1, "konular": [
      {"id": "u1k1", "baslik": "Uzay ve Uzay Araçları", "sayfalar": "s. 15–19", "kaynakSayfalar": [[15, 19], [24, 24]], "hazir": True},
      {"id": "u1k2", "baslik": "Teleskoplar ve Gözlemevleri", "sayfalar": "s. 19, 22–23", "kaynakSayfalar": [[19, 19], [22, 23]], "hazir": True},
      {"id": "u1k3", "baslik": "Türkiye Uzayda", "sayfalar": "s. 20–21, 26–28", "kaynakSayfalar": [[20, 21], [26, 28]], "hazir": True},
      {"id": "u1k4", "baslik": "Uzay Teknolojisinin Faydaları ve Uzay Kirliliği", "sayfalar": "s. 24–25, 30–32", "kaynakSayfalar": [[24, 25], [30, 32]], "hazir": False},
      {"id": "u1k5", "baslik": "Yıldızların Doğumu ve Yaşamı", "sayfalar": "s. 34–42", "kaynakSayfalar": [[34, 42]], "hazir": False},
      {"id": "u1k6", "baslik": "Takımyıldızlar", "sayfalar": "s. 43–45", "kaynakSayfalar": [[43, 45]], "hazir": False},
      {"id": "u1k7", "baslik": "Galaksi ve Evren", "sayfalar": "s. 46–50", "kaynakSayfalar": [[46, 50]], "hazir": False}]},
    {"ad": "2. Ünite: Kuvvet ve Enerjiyi Keşfedelim", "no": 2, "konular": []},
    {"ad": "3. Ünite: Vücudumuzdaki Sistemler", "no": 3, "konular": []}
  ]
}

def S(soru, secenekler, dogru, ipucu, aciklama):
    return {"soru": soru, "secenekler": secenekler, "dogru": dogru, "ipucu": ipucu, "aciklama": aciklama}

konu = {
  "id": "u1k1", "unite": "1. Ünite: Uzay Çağı", "baslik": "Uzay ve Uzay Araçları", "sayfalar": "s. 15–19",
  "giris": "Uzay, Dünya'nın atmosferinin dışında kalan çok geniş bir ortamdır. Güneş, Ay, yıldızlar ve gezegenler buradadır. İnsanlar uzayı tanımak için 6 önemli araç geliştirdi. Şimdi onları tek tek tanıyacağız.",
  "kavramlar": [
    {"ad": "Uzay Roketi", "renk": "#e63946", "svg": SVG["Uzay Roketi"],
     "aciklama": "Uzay araçlarını yeryüzünden yörüngeye veya daha uzağa taşır.",
     "ek": "Yakıt, motor ve egzoz bölümleri vardır. Önceden tek kullanımlıktı, artık yeniden kullanılabiliyor. Dünya'dan kontrol edilir.",
     "akilda": "Uzay taksisi",
     "soru": S("Uzay roketinin görevi nedir?", ["Gök cisimlerini gözlemlemek", "Uzay araçlarını uzaya taşımak", "Astronotlara ev olmak"], 1,
               "\"Akılda kalsın\" ifadesini hatırla: uzay taksisi. Taksi ne yapar?", "Roket, uzay araçlarını yeryüzünden yörüngeye veya daha uzağa taşır. (s. 18)")},
    {"ad": "Yapay Uydu", "renk": "#c99a06", "svg": SVG["Yapay Uydu"],
     "aciklama": "Dünya'nın veya başka bir gök cisminin çevresinde belirli bir yörüngede döner.",
     "ek": "İletişim, gözlem ve keşif için kullanılır. Enerjisini güneş panellerinden alır. Dünya'dan kontrol edilir.",
     "akilda": "Televizyon, harita, hava durumu",
     "soru": S("Yapay uydu uzayda ne yapar?", ["Bir gök cisminin çevresinde belirli bir yörüngede döner", "Gezegenlerin yüzeyine iner", "Astronotları istasyona taşır"], 0,
               "Uydunun hareketini düşün: bir şeyin etrafında ne yapıyordu?", "Yapay uydular belirli bir yörüngede dolanır; iletişim, gözlem ve keşif için kullanılır. (s. 18)")},
    {"ad": "Uzay Sondası", "renk": "#d9602b", "svg": SVG["Uzay Sondası"],
     "aciklama": "Bir gök cismini ya da uzaydaki olayları incelemek için gönderilen robot araçtır.",
     "ek": "İçinde insan yoktur, Dünya'dan kontrol edilir. Enerjisi güneş panellerinden gelir.",
     "akilda": "Robot kâşif",
     "soru": S("Uzay sondasını kim kontrol eder?", ["İçindeki astronotlar", "Dünya'daki kontrol merkezi", "Uzay istasyonundaki pilot"], 1,
               "Sonda bir robottur. Robotun içinde insan var mı?", "Uzay sondası robotik bir araçtır, içinde insan yoktur ve Dünya'dan kontrol edilir. (s. 18)")},
    {"ad": "Uzay Mekiği", "renk": "#5b6475", "svg": SVG["Uzay Mekiği"],
     "aciklama": "Astronotları, büyük uyduları ve malzemeleri uzay istasyonuna taşır.",
     "ek": "Yeniden kullanılabilir. Onu içindeki astronotlar kontrol eder.",
     "akilda": "Astronot servisi",
     "soru": S("Uzay mekiği neleri uzay istasyonuna taşır?", ["Sadece yakıt", "Hiçbir şey taşımaz, sadece gözlem yapar", "Astronotları, büyük uyduları ve malzemeleri"], 2,
               "\"Astronot servisi\" ifadesini hatırla. Servis kimleri taşır?", "Uzay mekiği astronotları, büyük uyduları ve gerekli malzemeleri uzay istasyonuna taşır. (s. 18)")},
    {"ad": "Uzay İstasyonu", "renk": "#1d6fa3", "svg": SVG["Uzay İstasyonu"],
     "aciklama": "Yörüngede dolanan, astronotların yaşayıp deney yaptığı araçtır.",
     "ek": "Düşük yer çekimli ortamda deney yapılır. Yeniden kullanılamaz ama bakım ve onarımla ömrü uzatılır.",
     "akilda": "Uzaydaki ev + laboratuvar",
     "soru": S("Astronotlar uzay istasyonunda ne yapar?", ["Yaşar ve bilimsel deney yapar", "Sadece fotoğraf çeker", "Roket yakıtı üretir"], 0,
               "\"Ev + laboratuvar\" ifadesini düşün. Evde ne yapılır, laboratuvarda ne yapılır?", "Uzay istasyonunda astronotlar yaşar ve düşük yer çekimli ortamda deney yapar. (s. 19)")},
    {"ad": "Teleskop", "renk": "#2d6a4f", "svg": SVG["Teleskop"],
     "aciklama": "Gök cisimlerini gözlemlemek için kullanılır.",
     "ek": "Artık Dünya'nın yörüngesine de çıkarılabiliyor. Orada daha net görüntü alır.",
     "akilda": "Uzayın dürbünü",
     "soru": S("Teleskop ne için kullanılır?", ["Uyduları uzaya taşımak için", "Gök cisimlerini gözlemlemek için", "Astronotların yaşaması için"], 1,
               "Dürbünle ne yaparız?", "Teleskoplar gök cisimlerini gözlemlemek için kullanılır. (s. 19)")}
  ],
  "gruplar": [
    {"soru": "Kim kontrol eder?", "kutular": [
      {"etiket": "Dünya'dan kontrol edilir", "uyeler": ["Uzay Roketi", "Yapay Uydu", "Uzay Sondası"]},
      {"etiket": "İçindeki insanlar kontrol eder", "uyeler": ["Uzay Mekiği", "Uzay İstasyonu"]}]},
    {"soru": "Güneş paneli kullanır mı?", "kutular": [
      {"etiket": "Evet", "uyeler": ["Yapay Uydu", "Uzay Sondası", "Uzay İstasyonu"]},
      {"etiket": "Hayır", "uyeler": ["Uzay Roketi"]}]},
    {"soru": "Yeniden kullanılabilir mi?", "kutular": [
      {"etiket": "Evet", "uyeler": ["Uzay Mekiği", "Uzay Roketi"]},
      {"etiket": "Hayır (bakımla ömrü uzar)", "uyeler": ["Uzay İstasyonu"]}]}
  ],
  "biliyorMusun": [
    "Türkiye'nin ilk yerli ve millî haberleşme uydusu Türksat 6A, 9 Temmuz 2024'te uzaya gönderildi. (s. 15)",
    "Uydularımız sayesinde hava olayları gözlenir, fay hatları belirlenir, navigasyonla yol bulunur. (s. 15)"
  ],
  "akildaKalsin": [
    "Uzay boş değildir: az miktarda gaz, toz ve parçacık vardır.",
    "Roket taşır, uydu döner, sonda keşfeder.",
    "Mekikte ve istasyonda astronot vardır.",
    "Güneş paneli: uydu, sonda, istasyon. Roket kullanmaz.",
    "Uzaya çıkarılan teleskop daha net görür."
  ],
  "merakKutusu": [
    {"soru": "Uzay gerçekten bomboş mu?", "cevap": "Hayır. Uzayda çok az miktarda gaz, toz ve küçük parçacıklar vardır. (s. 16)"},
    {"soru": "Roketler tekrar kullanılabilir mi?", "cevap": "Eskiden tek kullanımlıktı. Yeni teknolojiler sayesinde artık yeniden kullanılabilen roketler üretiliyor. (s. 18)"},
    {"soru": "Uydular günlük hayatımızda ne işe yarar?", "cevap": "Hava olaylarını gözlemek, deprem bilimi için fay hatlarını belirlemek ve navigasyonla yol bulmak uydular sayesinde olur. (s. 15)"},
    {"soru": "Uzay araçları enerjiyi nereden alır?", "cevap": "Yapay uydu, uzay sondası ve uzay istasyonu, güneş enerjisini elektrik enerjisine çeviren güneş panellerini kullanır. (s. 18–19)"},
    {"soru": "Teleskop neden uzaya gönderilir?", "cevap": "Dünya'nın yörüngesine çıkarılan teleskoplar daha net görüntü elde eder. Nedenini bir sonraki konuda öğreneceğiz. (s. 19)"},
    {"soru": "Uzay istasyonu eskirse ne olur?", "cevap": "Uzay istasyonu yeniden kullanılamaz ama bakım ve onarım yapılarak ömrü uzatılabilir. (s. 19)"}
  ],
  "dusunVeYaz": [
    {"soru": "Uzay mekiği ile uzay roketi arasındaki bir benzerliği ve bir farkı yaz.",
     "ornekCevap": "Benzerlik: İkisi de uzaya bir şeyler taşır ve yeniden kullanılabilir. Fark: Mekiği içindeki astronotlar kontrol eder, roket ise Dünya'dan kontrol edilir.",
     "anahtarlar": ["taşı", "astronot", "Dünya'dan", "kontrol", "yeniden"]}
  ],
  "sorular": [
    S("Uzay için hangisi doğrudur?", ["Tamamen boştur", "Az miktarda gaz, toz ve parçacık vardır", "Sadece yıldızlar vardır"], 1,
      "Uzayın tanımında \"tamamen boş olmayan\" ifadesi geçiyordu.", "Uzay tamamen boş değildir; çok az miktarda gaz, toz ve çeşitli parçacıklar bulunur. (s. 16)"),
    S("Uzay araçlarını yeryüzünden yörüngeye taşıyan araç hangisidir?", ["Uzay roketi", "Teleskop", "Uzay sondası"], 0,
      "Uzay taksisi hangisiydi?", "Uzay roketi, uzay araçlarını yörüngeye veya daha uzak bölgelere taşır. (s. 18)"),
    S("Bir gök cismini incelemek için gönderilen, Dünya'dan kontrol edilen robot araç hangisidir?", ["Uzay mekiği", "Uzay sondası", "Uzay istasyonu"], 1,
      "\"Robot kâşif\" hangisiydi?", "Uzay sondası robotik bir araçtır ve Dünya'dan kontrol edilir. (s. 18)"),
    S("İletişim, gözlem ve keşif için Dünya'nın çevresinde dolanan araç hangisidir?", ["Uzay mekiği", "Uzay roketi", "Yapay uydu"], 2,
      "Televizyon ve hava durumu hangi araç sayesinde çalışıyordu?", "Yapay uydular belirli bir yörüngede dolanır ve Dünya'dan kontrol edilir. (s. 18)"),
    S("Uzay mekiğini kim kontrol eder?", ["Dünya'daki bilgisayarlar", "İçindeki astronotlar", "Uzay istasyonu"], 1,
      "Mekik bir \"astronot servisi\". Servisi kim kullanır?", "Mekiğin kontrolünü içinde görev alan astronotlar yapar. (s. 18)"),
    S("Astronotların düşük yer çekimli ortamda deney yaptığı araç hangisidir?", ["Uzay istasyonu", "Yapay uydu", "Teleskop"], 0,
      "Uzaydaki ev + laboratuvar hangisiydi?", "Uzay istasyonunda astronotların yaşam alanı ve deney donanımı vardır. (s. 19)"),
    S("Hangisi güneş paneli kullanmaz?", ["Yapay uydu", "Uzay istasyonu", "Uzay roketi"], 2,
      "Gruplayalım bölümündeki \"Güneş paneli kullanır mı?\" sorusunu hatırla.", "Kitaptaki örnek: Yapay uyduda güneş panelleri kullanılır, uzay roketinde kullanılmaz. (s. 24)"),
    S("Önceden tek kullanımlık olan, artık yeniden kullanılabilen araç hangisidir?", ["Uzay roketi", "Uzay istasyonu", "Uzay sondası"], 0,
      "Uzay istasyonu yeniden kullanılamıyordu. Diğer iki seçeneği düşün.", "Yeni teknolojiler sayesinde uzay roketleri yeniden kullanılabilir şekilde üretiliyor. (s. 18)"),
    S("Teleskoplar Dünya'nın yörüngesine çıkarılınca ne olur?", ["Görüntü bulanıklaşır", "Sadece gündüz çalışır", "Daha net görüntü elde edilir"], 2,
      "Uzaya çıkarmanın amacı daha iyi görmektir.", "Yörüngedeki teleskoplar daha net görüntüler elde eder. (s. 19)")
  ]
}

json.dump(ders, open(os.path.join(OUT, "ders.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(konu, open(os.path.join(OUT, "konular", "u1k1.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# Kitap metinleri: yalnızca bot fonksiyonuna paketlenir, sitede yayımlanmaz
KAY = os.path.join(BASE, "kaynaklar", "fen1"); os.makedirs(KAY, exist_ok=True)
SRC = os.path.join(BASE, "..", "fen_proje")
for n, f in [(1, "Fen7_Unite1_Uzay_Cagi.md"), (2, "Fen7_Unite2_Kuvvet_ve_Enerji.md"), (3, "Fen7_Unite3_Vucudumuzdaki_Sistemler.md")]:
    shutil.copy(os.path.join(SRC, f), os.path.join(KAY, f"unite{n}.md"))

dogrular = [q["dogru"] for q in konu["sorular"]] + [k["soru"]["dogru"] for k in konu["kavramlar"]]
print("kavram:", len(konu["kavramlar"]), "| kavram sorusu:", sum(1 for k in konu["kavramlar"] if "soru" in k),
      "| test sorusu:", len(konu["sorular"]), "| merak:", len(konu["merakKutusu"]), "| düşün-yaz:", len(konu["dusunVeYaz"]),
      "| doğru şık dağılımı:", {i: dogrular.count(i) for i in range(3)})
uyeler = {m for g in konu["gruplar"] for b in g["kutular"] for m in b["uyeler"]}
print("grup üyeleri kavramlarla eşleşiyor:", uyeler <= {k["ad"] for k in konu["kavramlar"]})
