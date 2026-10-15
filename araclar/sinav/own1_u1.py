import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from ortak import Havuz
H = Havuz("own1", 1, "o1"); a = H.add
K1, K2, K4 = "(SB s. 11, 17)", "(SB s. 11–12, 17)", "(WB s. 11)"

# --- Konu 1: calm, cheerful, confident…
a("u1k1", "cheerful", "secim", soru="{{is happy}} tanımı hangi kelimenindir?",
  secenekler=["calm", "cheerful", "patient", "shy"], dogru=1,
  aciklama=f"Mutlu, neşeli kişi {{{{cheerful}}}} {K1}.")
a("u1k1", "confident", "secim", soru="{{shy}} kelimesinin zıt anlamlısı hangisidir?",
  secenekler=["confident", "grumpy", "anxious", "helpful"], dogru=0,
  aciklama=f"Utangaç {{{{shy}}}}, kendine güvenen {{{{confident}}}} {K1}.")
a("u1k1", "patient", "eslestir", soru="Kelimeleri zıt anlamlılarıyla eşleştir.", ciftler=[
  {"sol": "calm", "sag": "anxious"},
  {"sol": "cheerful", "sag": "grumpy"},
  {"sol": "patient", "sag": "impatient"},
  {"sol": "helpful", "sag": "unhelpful"}],
  aciklama=f"Bazı zıtlar ayrı kelime, bazıları {{{{im-}}}} ya da {{{{un-}}}} ile yapılır {K1}.")
a("u1k1", "sociable", "bosluk", havuz=["but", "so"], cumleler=[
  {"c": "I'm sociable ___ I love making friends.", "cevap": "because"},
  {"c": "She is never angry. She is very ___.", "cevap": "calm"},
  {"c": "He always helps other people. He is ___.", "cevap": "helpful"}],
  aciklama=f"Nedeni {{{{because}}}} ile söyleriz {K1}.")
a("u1k1", "helpful", "kisa", soru="{{helps other people}} tanımı hangi kelimenindir? İngilizce yaz.", yanit="helpful",
  aciklama=f"Başkalarına yardım eden kişi {{{{helpful}}}} {K1}.")
a("u1k1", "calm", "dy", ifade="{{calm}} kelimesi “endişeli, kaygılı” demektir.", dogru=False,
  duzeltme="calm sakin demektir; endişeli anxious'tır.",
  aciklama=f"{{{{calm}}}} sakin, {{{{anxious}}}} endişeli {K1}.")

# --- Konu 2: sensible, sensitive, talented…
a("u1k2", "sensible", "secim", soru="{{makes good decisions}} tanımı hangi kelimenindir?",
  secenekler=["sensitive", "sensible", "silly", "lazy"], dogru=1,
  aciklama=f"İyi karar veren kişi {{{{sensible}}}}. {{{{sensitive}}}} ile karıştırma {K2}.")
a("u1k2", "sensitive", "secim", soru="Hangi kelimenin zıttı {{in-}} ile yapılır?",
  secenekler=["talented", "ambitious", "sensitive", "inspiring"], dogru=2,
  aciklama=f"{{{{sensitive}}}} → {{{{insensitive}}}}. Diğerleri {{{{un-}}}} alır {K2}.")
a("u1k2", "talented", "eslestir", soru="Kelimeleri anlamlarıyla eşleştir.", ciftler=[
  {"sol": "talented", "sag": "yetenekli"},
  {"sol": "ambitious", "sag": "hırslı"},
  {"sol": "inspiring", "sag": "ilham veren"},
  {"sol": "sensitive", "sag": "duyarlı"}],
  aciklama=f"Kişiliği anlatan kelimeler {K2}.")
a("u1k2", "active", "kisa", soru="{{active}} kelimesinin zıt anlamlısını İngilizce yaz.", yanit="lazy",
  aciklama=f"{{{{active}}}} hareketli, {{{{lazy}}}} tembel {K2}.")
a("u1k2", "inspiring", "secim", soru="{{In my ___, Anoka should win.}} Boşluğa hangisi gelir?",
  secenekler=["opinion", "because", "talented", "look"], dogru=0,
  aciklama=f"Fikir bildirmek için {{{{In my opinion}}}} ya da {{{{In my view}}}} {K2}.")
a("u1k2", "sensible", "dy", ifade="{{silly}} kelimesi {{sensible}} kelimesinin zıt anlamlısıdır.", dogru=True,
  aciklama=f"{{{{sensible}}}} mantıklı, {{{{silly}}}} saçma davranan {K2}.")

# --- Konu 4: Phrasal verbs
a("u1k4", "give up", "secim", soru="{{This is so difficult!}} diyen arkadaşına ne dersin? {{Don't ___!}}",
  secenekler=["give up", "hang out", "cheer up", "take care of"], dogru=0,
  aciklama=f"{{{{give up}}}} pes etmek demektir. {{{{Don't give up!}}}} Pes etme! {K4}.")
a("u1k4", "look up to", "eslestir", soru="Phrasal verb'leri anlamlarıyla eşleştir.", ciftler=[
  {"sol": "look up to", "sag": "örnek almak"},
  {"sol": "get on with", "sag": "iyi anlaşmak"},
  {"sol": "take care of", "sag": "bakmak, ilgilenmek"},
  {"sol": "deal with", "sag": "başa çıkmak"}],
  aciklama=f"Fiil + küçük kelime = yeni anlam {K4}.")
a("u1k4", "depend on", "secim", soru="{{Babies ___ adults for everything.}} Boşluğa hangisi gelir?",
  secenekler=["give up", "depend on", "cheer up", "hang out"], dogru=1,
  aciklama=f"Bebekler her şey için yetişkinlere muhtaçtır: {{{{depend on}}}} {K4}.")
a("u1k4", "hang out", "bosluk", havuz=["give up", "look"], cumleler=[
  {"c": "Do you want to ___ after school?", "cevap": "hang out"},
  {"c": "My grandfather is sad, so I'm trying to ___ him up.", "cevap": "cheer"},
  {"c": "How do you ___ so much homework?", "cevap": "deal with"}],
  aciklama=f"Takılmak {{{{hang out}}}}, neşelendirmek {{{{cheer up}}}}, başa çıkmak {{{{deal with}}}} {K4}.")
a("u1k4", "cheer up", "dy", ifade="{{She cheers me up.}} cümlesinde kişi {{cheer}} ile {{up}} arasına girmiştir.", dogru=True,
  aciklama=f"{{{{cheer up}}}}'ta kişi ortaya girer: {{{{cheer me up}}}} {K4}.")
a("u1k4", "get on with", "kisa", soru="“İyi anlaşmak” anlamına gelen phrasal verb nedir? İngilizce yaz.", yanit="get on with", kabul=["get on"],
  aciklama=f"Biriyle iyi anlaşmak: {{{{get on with}}}} {K4}.")
H.yaz()
