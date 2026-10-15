import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from ortak import Havuz, ONC
H = Havuz("tr1", 2, "t2"); a = H.add
K1, K2 = "(s. 77, 90, 92, 95)", "(s. 75–78, 101–104)"

# --- Konu 1: Kelimeler arası anlam ilişkileri
a("u2k1", "Eş Anlamlı Kelimeler", "eslestir", soru="Kelimeleri eş anlamlılarıyla eşleştir.", ciftler=[
  {"sol": "muhacir", "sag": "göçmen"},
  {"sol": "ziyan", "sag": "zarar"},
  {"sol": "zafer", "sag": "galibiyet"},
  {"sol": "huzur", "sag": "gönül rahatlığı"}],
  aciklama=f"Eş anlamlı kelimeler farklı yazılır, aynı anlamı verir {K1}.")
a("u2k1", "Zıt Anlamlı Kelimeler", "secim", soru="Hangi kelime çifti zıt anlamlı değildir?",
  secenekler=["esaret – özgürlük", "karanlık – aydınlık", "gelmek – gelmemek", "zafer – yenilgi"], dogru=2,
  aciklama=f"“-me” eki olumsuzluk yapar, zıt anlam yapmaz. “Gelmek”in zıttı “gitmek”tir {K1}.")
a("u2k1", "Somut ve Soyut Kelimeler", "dytablo", soru="Kelime somutsa D, soyutsa Y seç.", ifadeler=[
  {"s": "siper", "d": True}, {"s": "istiklal", "d": False}, {"s": "toprak", "d": True}, {"s": "cesaret", "d": False}],
  aciklama=f"Siper ve toprak duyularla algılanır; istiklal ve cesaret algılanmaz {K1}.")
a("u2k1", "Ölçüte Göre Sınıflandırma", "secim", soru="Sınıflandırma ile ilgili aşağıdaki ifadeler verilmiştir.",
  onculler=["Sınıflandırmaya başlamadan önce bir ölçüt seçilir.", "Ölçüt değişirse gruplar da değişebilir.", "Her grup için ayrı bir ölçüt kullanılır."],
  kok="Sınıflandırma ile ilgili yukarıdakilerden hangileri doğrudur?", secenekler=ONC, dogru=1,
  aciklama=f"Önce ölçüt seçilir ve bütün kelimelerde aynı ölçüt kullanılır {K1}.")
a("u2k1", "Anlamca Çelişen Kelimeler", "secim", soru="Hangi cümlede anlamca çelişen kelimeler birlikte kullanılmıştır?",
  secenekler=["Tören yaklaşık bir saat sürdü.", "Mutlaka erken gelmelisin.", "Belki yarın yağmur yağar.", "Hiç şüphesiz bu roman en güzeli olabilir."], dogru=3,
  aciklama=f"“Hiç şüphesiz” kesinlik, “olabilir” ihtimal bildirir; birlikte olmaz {K1}.")
a("u2k1", "Duyguyu Yansıtan Kelime Seçimi", "dy",
  ifade="Şair, “Kahroldu Elifçik” yerine “Üzüldü Elifçik” deseydi Elif'in acısı daha güçlü anlatılırdı.", dogru=False,
  duzeltme="“Kahrolmak” daha güçlü bir kelimedir; acıyı daha iyi anlatır.",
  aciklama="“Kahrolmak” çok büyük üzüntüdür. Kelime seçimi duygunun gücünü belirler (s. 102).")

# --- Konu 2: Çıkarım ve metnin mesajı
a("u2k2", "Yazılan ve Sezdirilen Anlam", "secim",
  metin=["Selin sınav kâğıdını alınca yüzü kıpkırmızı oldu.", "Kâğıdı hemen çantasına sakladı.", "Teneffüste kimseyle konuşmadı."],
  soru="Bu metinde sezdirilen (açıkça yazılmayan) bilgi hangisidir?",
  secenekler=["Selin sınavından düşük not almış olabilir.", "Selin sınav kâğıdını aldı.", "Selin kâğıdı çantasına koydu.", "Selin teneffüste kimseyle konuşmadı."], dogru=0,
  aciklama="Öbür şıklar metinde yazıyor. Kâğıdı saklaması düşük notu sezdiriyor.")
a("u2k2", "Çıkarım: İpucu + Bildiğin", "bosluk", havuz=["başlık", "yazar"], cumleler=[
  {"c": "Çıkarım yaparken metindeki ___ kullanırız.", "cevap": "ipuçlarını"},
  {"c": "İpuçlarına kendi ___ ekleriz.", "cevap": "bildiklerimizi"},
  {"c": "Çıkarımı metinden bir ___ ile destekleriz.", "cevap": "kanıt"}],
  aciklama="Çıkarım = ipucu + bildiğin; sonra kanıt cümlesi gösterilir.")
a("u2k2", "Kanıtını Göster", "secim", soru="“Hatice Nine için bayrak, evinden bile değerlidir.” çıkarımının kanıtı hangisi olabilir?",
  secenekler=["Ortalık ağarıyor, kadınlar gelip gidiyordu.", "Salihli'de birkaç ev yanmadan kalmıştı.", "Evi yansa da tek isteği, toprağının bayrağının altında olmasıydı.", "Oğlu onu bir eşekle getirdi."], dogru=2,
  aciklama=f"Evi yanan Nine'nin tek isteği bayrağının altında olmak; çıkarımı bu destekler {K2}.")
a("u2k2", "Sözün Asıl Anlamı", "secim", soru="Hatice Nine'nin “Ben elli senedir onu kovalıyorum.” sözüyle anlatmak istediği nedir?",
  secenekler=["Elli yıldır koşu yaptığını", "Yıllardır bayrağının altında yaşamayı özlediğini", "Bayrağı kaybettiğini", "Elli yaşında olduğunu"], dogru=1,
  aciklama=f"Nine yıllardır özgür bir yurtta, bayrağının altında yaşamayı özlemektedir {K2}.")
a("u2k2", "Karakterin Duygusunu Çıkarma", "eslestir", soru="Davranışları gösterdiği duyguyla eşleştir.", ciftler=[
  {"sol": "Koşarak gelip annesine sarıldı.", "sag": "sevinç"},
  {"sol": "Ellerini ovuşturup ikide bir yutkundu.", "sag": "heyecan"},
  {"sol": "Kapıyı çarpıp odasına kapandı.", "sag": "öfke"}],
  aciklama="Yazar duyguyu her zaman söylemez; davranışlardan çıkarırız.")
a("u2k2", "Metnin Mesajı", "kisa", soru="Yazarın metinle okura vermek istediği düşünceye ne ad verilir? (Bu konudaki adıyla yaz.)",
  yanit="mesaj", kabul=["ana fikir", "anafikir"],
  aciklama="Mesaj, yazarın vermek istediği düşüncedir; ana fikre çok benzer.")
H.yaz()
