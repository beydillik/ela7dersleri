import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from ortak import Havuz, ONC
H = Havuz("own1", 2, "o2"); a = H.add
K1, K2, K3 = "(WB s. 16, 22)", "(SB s. 23)", "(WB s. 90)"
SUF = "-ist / -er / -or"

# --- Konu 1: Visual arts
a("u2k1", "architecture", "secim", soru="{{to design, plan and make buildings}} tanımı hangi kelimenindir?",
  secenekler=["sculpture", "architecture", "photography", "illustration"], dogru=1,
  aciklama=f"Binaları tasarlamak {{{{architecture}}}}: mimarlık {K1}.")
a("u2k1", "illustration", "secim", soru="{{The ___ in this book are in black and white, not colour.}} Boşluğa hangisi gelir?",
  secenekler=["sculptures", "buildings", "illustrations", "clothes"], dogru=2,
  aciklama=f"Kitaptaki çizimler {{{{illustrations}}}} {K1}.")
a("u2k1", "sculpture", "eslestir", soru="Kelimeleri Türkçeleriyle eşleştir.", ciftler=[
  {"sol": "architecture", "sag": "mimarlık"},
  {"sol": "sculpture", "sag": "heykel"},
  {"sol": "photography", "sag": "fotoğrafçılık"},
  {"sol": "fashion design", "sag": "moda tasarımı"}],
  aciklama=f"Görsel sanatların adları {K1}.")
a("u2k1", "photography", "bosluk", havuz=["architecture", "sculpture"], cumleler=[
  {"c": "I bought a new camera for my ___ class.", "cevap": "photography"},
  {"c": "Some ___ is OK, but I really don't like graffiti.", "cevap": "street art"},
  {"c": "He loved making clothes and wanted to study ___.", "cevap": "fashion design"}],
  aciklama=f"Kamera, grafiti ve giysi ipuçlarına bak {K1}.")
a("u2k1", "street art", "dy", ifade="{{street art}} şehirlerde dışarıda yapılan resim ve grafitilerdir.", dogru=True,
  aciklama=f"Tanım: {{{{outside in urban areas}}}} {K1}.")
a("u2k1", "sculpture", "kisa", soru="İnsanları ya da nesneleri anlatan cisimler yapma sanatı hangisidir? İngilizce yaz.", yanit="sculpture",
  aciklama=f"Heykel: {{{{sculpture}}}} {K1}.")

# --- Konu 2: Performing arts ve -ist / -er / -or
a("u2k2", "gallery", "secim", soru="{{a room or building where you can see art}} tanımı hangi kelimenindir?",
  secenekler=["exhibition", "performance", "gallery", "filmmaking"], dogru=2,
  aciklama=f"Sanat görülen oda ya da bina {{{{gallery}}}} {K2}.")
a("u2k2", "exhibition", "dy", ifade="{{gallery}} bir etkinlik, {{exhibition}} bir yerdir.", dogru=False,
  duzeltme="gallery bir yer, exhibition bir etkinliktir (sergi).",
  aciklama=f"{{{{gallery}}}} oda ya da bina; {{{{exhibition}}}} etkinlik {K2}.")
a("u2k2", SUF, "eslestir", soru="Sanat dalını onu yapan kişiyle eşleştir.", ciftler=[
  {"sol": "photography", "sag": "photographer"},
  {"sol": "sculpture", "sag": "sculptor"},
  {"sol": "street art", "sag": "street artist"},
  {"sol": "filmmaking", "sag": "filmmaker"}],
  aciklama=f"Kişi ekleri: {{{{-ist}}}}, {{{{-er}}}}, {{{{-or}}}} {K2}.")
a("u2k2", SUF, "secim", soru="Sanatı yapan kişilerin adları:", onculler=["photographer", "sculptor", "illustrationist"],
  kok="Yukarıdaki kişi adlarından hangileri doğru yazılmıştır?", secenekler=ONC, dogru=1,
  aciklama=f"Doğrusu {{{{illustrator}}}}; {{{{-ist}}}} değil {{{{-or}}}} alır {K2}.")
a("u2k2", "performance", "bosluk", havuz=["sculpture", "architecture"], cumleler=[
  {"c": "We went to the theatre to see his ___ in the play.", "cevap": "performance"},
  {"c": "Eduardo goes to the cinema a lot. He's interested in ___.", "cevap": "filmmaking"},
  {"c": "They saw a wonderful ___ of paintings by a local artist.", "cevap": "exhibition"}],
  aciklama="Tiyatro, sinema ve resim ipuçlarına bak (SB s. 129, WB s. 22).")
a("u2k2", "contemporary dance", "kisa", soru="{{moving to music in a modern style}} tanımı hangi dansın? İngilizce yaz.", yanit="contemporary dance",
  aciklama="Modern tarzda dans: {{contemporary dance}} (WB s. 16).")

# --- Konu 3: Present perfect
a("u2k3", "have / has + V3", "secim", soru="{{Fans ___ seen his creations at exhibitions.}} Boşluğa hangisi gelir?",
  secenekler=["has", "have", "is", "did"], dogru=1,
  aciklama="{{Fans}} çoğul: {{have seen}} (SB s. 25).")
a("u2k3", "düzensiz fiil: V3", "eslestir", soru="Fiilleri V3 hâlleriyle eşleştir.", ciftler=[
  {"sol": "see", "sag": "seen"},
  {"sol": "make", "sag": "made"},
  {"sol": "go", "sag": "gone"},
  {"sol": "hear", "sag": "heard"}],
  aciklama=f"Düzensiz fiillerin V3'ü ezberlenir {K3}.")
a("u2k3", "been / gone", "secim", soru="{{She is at school now.}} Bu durumu anlatan cümle hangisi?",
  secenekler=["She has been to school.", "She has gone to school.", "She have gone to school.", "She has go to school."], dogru=1,
  aciklama="Hâlâ okulda: {{has gone}}. Dönseydi {{has been}} (SB s. 25).")
a("u2k3", "Have / Has … V3?", "dytablo", soru="Cümleler doğru mu, yanlış mı?", ifadeler=[
  {"s": "{{Has he been to art school?}}", "d": True},
  {"s": "{{Have she won a prize?}}", "d": False},
  {"s": "{{Have you ever been to the theatre?}}", "d": True},
  {"s": "{{Yes, I has.}}", "d": False}],
  aciklama=f"{{{{he / she}}}} ile {{{{Has}}}}; {{{{I}}}} ile {{{{have}}}} {K3}.")
a("u2k3", "haven't / hasn't + V3", "kisa", soru="{{Kristian Mensa ___ been to art school.}} (Gitmedi.) Boşluğa ne gelir? İngilizce yaz.", yanit="hasn't", kabul=["has not"],
  aciklama="{{He}} ile olumsuz: {{hasn't been}} (SB s. 24).")
a("u2k3", "ever / never", "bosluk", havuz=["been", "has"], cumleler=[
  {"c": "Have you ___ been to the theatre?", "cevap": "ever"},
  {"c": "I have ___ met a street artist.", "cevap": "never"},
  {"c": "Bordalo II has ___ rubbish and spray paint.", "cevap": "used"}],
  aciklama="Soruda {{ever}}, olumluda 'hiçbir zaman' {{never}}; {{has}} + V3 (WB s. 18, 90).")
H.yaz()
