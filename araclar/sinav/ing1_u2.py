import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from ortak import Havuz
H = Havuz("ing1", 2, "e2"); a = H.add
K = "(s. 27–44)"

# --- Konu 1: Sporlar ve Ekipman
a("u2k1", "swimming", "secim", soru="{{It is moving in water using your arms and legs.}} Hangi spor anlatılıyor?",
  secenekler=["cycling", "swimming", "skiing", "doing judo"], dogru=1,
  aciklama="Suda kollar ve bacaklarla ilerlemek {{swimming}}dir (s. 32).")
a("u2k1", "equipment", "secim", soru="{{If you want to play tennis, you need special ___.}} Boşluğa hangisi gelir?",
  secenekler=["diet", "injury", "score", "equipment"], dogru=3,
  aciklama="Tenis için raket, top gibi eşyalar gerekir: {{equipment}} (s. 43).")
a("u2k1", "outdoor sport", "dytablo", soru="Dışarıda, açık havada yapılan bir sporsa D, değilse Y seç.", ifadeler=[
  {"s": "Football is an outdoor sport.", "d": True},
  {"s": "Hiking is an outdoor sport.", "d": True},
  {"s": "Raymond prefers indoor sports because he likes sunny days.", "d": False}],
  aciklama="Futbol ve doğa yürüyüşü dışarıda yapılır. Raymond kapalı alanı her hava için seçer (s. 40–44).")
a("u2k1", "cycling", "eslestir", soru="Sporları Türkçe anlamlarıyla eşleştir.", ciftler=[
  {"sol": "cycling", "sag": "bisiklet sporu"},
  {"sol": "skiing", "sag": "kayak"},
  {"sol": "ice skating", "sag": "buz pateni"},
  {"sol": "swimming", "sag": "yüzme"}],
  aciklama="{{cycling}} bisiklet, {{skiing}} kayak, {{ice skating}} buz pateni, {{swimming}} yüzme (s. 34).")
a("u2k1", "doing judo", "bosluk", havuz=["play", "goes"], cumleler=[
  {"c": "I like ___ judo.", "cevap": "doing"},
  {"c": "I often go ___ in the sea.", "cevap": "swimming"},
  {"c": "I like ___ basketball.", "cevap": "playing"}],
  aciklama="Judo için {{doing}}, yüzme için {{go swimming}}, basketbol için {{playing}} (s. 29–36).")
a("u2k1", "skiing", "kisa", soru="Kayak sporunun İngilizcesini yaz.", yanit="skiing",
  aciklama="Kayak {{skiing}}tir (s. 34).")
a("u2k1", "equipment", "dy", ifade="Kitaptaki tenis paragrafına göre topa raketle vurulur.", dogru=True,
  aciklama="{{They hit a ball with a racket.}} (s. 32)")

# --- Konu 2: Maç ve Yarışma
a("u2k2", "spectator", "secim", soru="{{There were thousands of ___ in the stadium to watch the final match.}}",
  secenekler=["injuries", "spectators", "medals", "achievements"], dogru=1,
  aciklama="Maçı izleyenler seyircilerdir: {{spectators}} (s. 40).")
a("u2k2", "draw", "secim", soru="{{The score was a draw.}} Skor hangisi olabilir?",
  secenekler=["2-0", "3-1", "1-1", "0-2"], dogru=2,
  aciklama="Berabere: iki taraf eşit, örneğin 1-1 (s. 40).")
a("u2k2", "beat", "dy", ifade="{{Our school team beat the opponent team 2-0.}} cümlesinde okul takımı kaybetmiştir.", dogru=False,
  duzeltme="Okul takımı kazanmıştır; {{beat}} yenmek demektir.",
  aciklama="{{beat}} yenmek demektir; okul takımı 2-0 kazandı (s. 40).")
a("u2k2", "achievement", "bosluk", havuz=["equipment", "court"], cumleler=[
  {"c": "Katie won five gold medals. It was a great ___.", "cevap": "achievement"},
  {"c": "Sportsmen may have some ___ while doing exercises.", "cevap": "injuries"},
  {"c": "None of the teams could ___ a goal.", "cevap": "score"}],
  aciklama="Başarı {{achievement}}, sakatlıklar {{injuries}}, gol atmak {{score a goal}} (s. 40).")
a("u2k2", "medal", "eslestir", soru="Kelimeleri Türkçe anlamlarıyla eşleştir.", ciftler=[
  {"sol": "medal", "sag": "madalya"},
  {"sol": "injury", "sag": "sakatlık"},
  {"sol": "spectator", "sag": "seyirci"},
  {"sol": "draw", "sag": "berabere"}],
  aciklama="{{medal}} madalya, {{injury}} sakatlık, {{spectator}} seyirci, {{draw}} berabere (s. 40–42).")
a("u2k2", "beat", "kisa", soru="{{beat}} (yenmek) kelimesinin zıt anlamlısını İngilizce yaz: kaybetmek.", yanit="lose",
  aciklama="Yenmek {{beat}}, kaybetmek {{lose}} (s. 40).")
a("u2k2", "score", "secim", soru="{{He threw the ball, and the final score is 63-64 now.}} {{final score}} ne demektir?",
  secenekler=["Son skor", "Son oyuncu", "Son maç", "Son madalya"], dogru=0,
  aciklama="{{final}} son, {{score}} skor: son skor (s. 32).")

# --- Konu 3: Rutinler ve Sıklık
a("u2k3", "always", "secim", soru="Hangisi doğru yazılmıştır?",
  secenekler=["I wake up always early.", "Always I wake up early.", "I always wake up early.", "I wake always up early."], dogru=2,
  aciklama="Sıklık kelimesi fiilin önüne gelir: {{I always wake up early.}} (s. 31).")
a("u2k3", "How often …?", "secim", soru="{{___ do you train? Six days a week.}} Boşluğa ne gelir?",
  secenekler=["Where", "How often", "What", "Who"], dogru=1,
  aciklama="Sıklığı sormak için {{How often}} (s. 31).")
a("u2k3", "usually", "eslestir", soru="Sıklık kelimelerini yüzdeleriyle eşleştir.", ciftler=[
  {"sol": "always", "sag": "%100"},
  {"sol": "usually", "sag": "%80"},
  {"sol": "sometimes", "sag": "%40"},
  {"sol": "never", "sag": "%0"}],
  aciklama="Kitaptaki tablo: {{always}} %100, {{usually}} %80, {{sometimes}} %40, {{never}} %0 (s. 38).")
a("u2k3", "twice a week", "bosluk", havuz=["two", "much"], cumleler=[
  {"c": "I work out at the gym ___ a week.", "cevap": "twice"},
  {"c": "I swim ___ day.", "cevap": "every"},
  {"c": "How ___ do you swim?", "cevap": "often"}],
  aciklama="{{twice a week}} haftada iki kez, {{every day}} her gün, {{How often}} ne sıklıkla (s. 31).")
a("u2k3", "never", "dy", ifade="{{Terry never eats junk food.}} cümlesine göre Terry bazen abur cubur yer.", dogru=False,
  duzeltme="Terry hiç abur cubur yemez; {{never}} asla demektir.",
  aciklama="{{never}} %0'dır: hiç yemez (s. 39).")
a("u2k3", "sometimes", "dytablo", soru="Kitaptaki Emma röportajına göre D ya da Y seç.", ifadeler=[
  {"s": "Emma always wakes up early.", "d": True},
  {"s": "Emma swims every day.", "d": True},
  {"s": "Emma sometimes eats healthy food.", "d": False}],
  aciklama="Emma her zaman erken kalkar, her gün yüzer ve sağlıklı beslenir (s. 31).")
a("u2k3", "often", "kisa", soru="Sık sık anlamına gelen sıklık kelimesini İngilizce yaz. ({{I ___ walk to school.}})", yanit="often",
  aciklama="Sık sık {{often}}: {{I often walk to school.}} (s. 36).")

H.yaz()
