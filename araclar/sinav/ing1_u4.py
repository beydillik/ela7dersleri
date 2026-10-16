import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from ortak import Havuz
H = Havuz("ing1", 4, "e4"); a = H.add

# --- Konu 1: Hayvan Grupları ve Yaşam Alanları
a("u4k1", "mammal", "secim", soru="{{Whales are ___ mammals.}} Boşluğa hangisi GELMEZ?",
  secenekler=["big", "enormous", "huge", "poisonous"], dogru=3,
  aciklama="{{poisonous}} zehirli demek; diğerleri büyük anlamında (s. 79).")
a("u4k1", "reptile", "secim", soru="{{There are four animal species. These are ___, birds, ___ and insects.}}",
  secenekler=["deserts / cages", "habitats / jungles", "mammals / reptiles", "crocodiles / lizards"], dogru=2,
  aciklama="Dört grup: memeliler, kuşlar, sürüngenler ve böcekler (s. 79).")
a("u4k1", "bird", "dytablo", soru="Okuma metnine göre D ya da Y seç.", ifadeler=[
  {"s": "Birds can fly because they have wings.", "d": True},
  {"s": "Ostriches can fly very well.", "d": False},
  {"s": "Reptiles have scales on their bodies.", "d": True}],
  aciklama="Devekuşları uçamaz; kuşların kanadı, sürüngenlerin pulu var (s. 67).")
a("u4k1", "habitat", "eslestir", soru="Kelimeleri Türkçe anlamlarıyla eşleştir.", ciftler=[
  {"sol": "mammal", "sag": "memeli"},
  {"sol": "reptile", "sag": "sürüngen"},
  {"sol": "habitat", "sag": "yaşam alanı"},
  {"sol": "desert", "sag": "çöl"}],
  aciklama="{{mammal}} memeli, {{reptile}} sürüngen, {{habitat}} yaşam alanı, {{desert}} çöl (s. 64, s. 74).")
a("u4k1", "desert", "bosluk", havuz=["cages", "milk"], cumleler=[
  {"c": "Forests are the ___ of the animals.", "cevap": "habitat"},
  {"c": "Camels can survive in the ___ for a long time.", "cevap": "deserts"},
  {"c": "Wild animals live in the ___.", "cevap": "jungle"}],
  aciklama="Yaşam alanı {{habitat}}, çöl {{deserts}}, orman {{jungle}} (s. 74).")
a("u4k1", "reptile", "dy", ifade="{{Reptiles are cold-blooded animals because they don't have a constant body temperature.}} cümlesine göre sürüngenlerin vücut sıcaklığı hep aynıdır.", dogru=False,
  duzeltme="Sürüngenlerin vücut sıcaklığı sabit değildir, değişir.",
  aciklama="{{constant}} sabit demek; sürüngenlerde sıcaklık sabit değil (s. 67).")
a("u4k1", "wildlife", "kisa", soru="Yaban hayatı kelimesinin İngilizcesini yaz.", yanit="wildlife",
  aciklama="Yaban hayatı {{wildlife}}: evcil olmayan hayvanlar (s. 72).")

# --- Konu 2: Nesli Tükenen Hayvanlar
a("u4k2", "extinct", "secim", soru="{{Katie: Do you know any extinct animals? Ronald: Umm... ___! There aren't any of them in the world.}}",
  secenekler=["Tigers", "Elephants", "Dodo birds", "Eagles"], dogru=2,
  aciklama="Dünyada hiç Dodo kuşu kalmadı; nesli tükendi (s. 79).")
a("u4k2", "hunt", "secim", soru="Hangisi hayvanların neslinin tükenme sebeplerinden biri DEĞİLDİR?",
  secenekler=["Global warming", "Climate change", "Human activities", "Space travels"], dogru=3,
  aciklama="Uzay yolculukları bir sebep değil; diğer üçü sebep (s. 80).")
a("u4k2", "endangered", "dytablo", soru="Kaplan metnine göre D ya da Y seç.", ifadeler=[
  {"s": "Tigers belong to the cat family.", "d": True},
  {"s": "Tigers are extinct.", "d": False},
  {"s": "People hunt tigers for their fur.", "d": True}],
  aciklama="Kaplanlar kedigildir, nesli tehlikededir; kürkleri için avlanır (s. 70).")
a("u4k2", "tusk", "eslestir", soru="Kelimeleri Türkçe anlamlarıyla eşleştir.", ciftler=[
  {"sol": "extinct", "sag": "nesli tükenmiş"},
  {"sol": "endangered", "sag": "nesli tehlikede"},
  {"sol": "fur", "sag": "kürk"},
  {"sol": "tusk", "sag": "fildişi"},
  {"sol": "pollute", "sag": "kirletmek"}],
  aciklama="Kelimeler kitabın 68–79. sayfalarında geçiyor (s. 68, s. 70, s. 79).")
a("u4k2", "destroy", "bosluk", havuz=["protected", "fed"], cumleler=[
  {"c": "Men ___ wild animals for their skins, fur or teeth.", "cevap": "hunted"},
  {"c": "They ___ their habitats to make fields.", "cevap": "destroyed"},
  {"c": "They also ___ the environment.", "cevap": "polluted"}],
  aciklama="Avladılar {{hunted}}, yok ettiler {{destroyed}}, kirlettiler {{polluted}} (s. 68).")
a("u4k2", "endangered", "dy", ifade="{{Tigers are endangered.}} cümlesi dünyada çok az kaplan kaldığını anlatır.", dogru=True,
  aciklama="{{This means there aren't many tigers in the world.}} (s. 70).")
a("u4k2", "fur", "kisa", soru="Boşluğa gelen kelimeyi yaz: {{People hunt tigers because they want to take their beautiful ___.}}", yanit="fur",
  aciklama="Kaplanlar güzel kürkleri ({{fur}}) için avlanıyor (s. 70).")

H.yaz()
