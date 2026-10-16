import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from ortak import Havuz, ONC
H = Havuz("own1", 3, "o3"); a = H.add
WB24, SB130, WB92 = "(WB s. 24)", "(SB s. 130)", "(WB s. 92)"
EVER = "Have you ever …? / Did you …?"
HL = "How long have you …?"
NEG = "haven't / hasn't … for / since"

# --- Konu 1: Communicating 1 (gesture, greet, shake hands, smile, wave)
a("u3k1", "gesture", "secim", soru="{{A thumbs up sign is a ___ that means 'good'.}} Boşluğa hangisi gelir?",
  secenekler=["wave", "gesture", "smile", "greet"], dogru=1,
  aciklama=f"Anlamı olan el hareketi {{{{gesture}}}}: jest {WB24}.")
a("u3k1", "greet", "eslestir", soru="Kelimeleri Türkçeleriyle eşleştir.", ciftler=[
  {"sol": "greet", "sag": "selamlamak, karşılamak"},
  {"sol": "smile", "sag": "gülümsemek"},
  {"sol": "wave", "sag": "el sallamak"},
  {"sol": "shake hands", "sag": "el sıkışmak"}],
  aciklama=f"Yüz ve elle iletişim kelimeleri (SB s. 35).")
a("u3k1", "wave", "bosluk", havuz=["shout", "post"], cumleler=[
  {"c": "When their guests left, they came outside to ___ goodbye.", "cevap": "wave"},
  {"c": "Everyone understands when you ___ at them. It means you're happy.", "cevap": "smile"},
  {"c": "Sofia ___ us at the door.", "cevap": "greeted"}],
  aciklama=f"Vedalaşmak, mutluluk ve karşılama ipuçlarına bak {SB130}.")
a("u3k1", "shake hands", "dy", ifade="Kazue'ye göre Japonlar tanışırken genelde el sıkışır.", dogru=False,
  duzeltme="Japonlar tanışırken genelde el sıkışmaz.",
  aciklama=f"Kazue: Japonlar genelde {{{{shake hands}}}} yapmaz {WB24}.")
a("u3k1", "smile", "kisa", soru="Mutlu olduğunu yüzünle göstermek: gülümsemek. İngilizce yaz.", yanit="smile",
  aciklama=f"Gülümsemek: {{{{smile}}}} {WB24}.")
a("u3k1", "greet", "secim", soru="İletişim kelimeleri ve anlamları:", onculler=["{{greet}}: selamlamak", "{{wave}}: el sıkışmak", "{{gesture}}: jest, el işareti"],
  kok="Hangileri doğrudur?", secenekler=["Yalnız I", "I ve II", "I ve III", "II ve III"], dogru=2,
  aciklama="{{wave}} el sallamak; el sıkışmak {{shake hands}} (SB s. 35).")

# --- Konu 2: Communicating 2 (describe, interpret, post, shout, translate, whisper)
a("u3k2", "whisper", "secim", soru="{{Don't speak loudly. Please ___. You'll wake up the baby.}} Boşluğa hangisi gelir?",
  secenekler=["shout", "post", "describe", "whisper"], dogru=3,
  aciklama=f"Bebek uyanmasın: alçak sesle konuş, {{{{whisper}}}} {WB24}.")
a("u3k2", "interpret", "secim", soru="{{say what someone's saying in another language}} tanımı hangi kelimenindir?",
  secenekler=["interpret", "describe", "post", "shout"], dogru=0,
  aciklama="Konuşulanı başka dile söylemek: {{interpret}} (SB s. 35).")
a("u3k2", "post", "dytablo", soru="Cümleler doğru mu, yanlış mı?", ifadeler=[
  {"s": "{{post}}: bir bloga ya da siteye bir şey koymak.", "d": True},
  {"s": "{{shout}} ile {{whisper}} zıt anlamlıdır.", "d": True},
  {"s": "{{describe}}: başka bir dile çevirmek.", "d": False},
  {"s": "{{translate}} en çok yazılı metinler için kullanılır.", "d": True}],
  aciklama="{{describe}} tarif etmek; çevirmek {{translate}} (SB s. 35–36).")
a("u3k2", "describe", "bosluk", havuz=["wave", "smile"], cumleler=[
  {"c": "I don't know what Jackie looks like. Can you ___ her to me?", "cevap": "describe"},
  {"c": "These instructions are in French. I need someone to ___ them for me.", "cevap": "translate"},
  {"c": "I only ___ when I'm very angry.", "cevap": "shout"}],
  aciklama=f"Görünüş, Fransızca talimat ve kızgınlık ipuçlarına bak {WB24}.")
a("u3k2", "translate", "dy", ifade="1950'lerde makineler konuşulan dili çevirebiliyordu ({{interpret}}).", dogru=False,
  duzeltme="Yazılı metinleri çevirebiliyordu ama konuşulan dili çeviremiyordu.",
  aciklama="{{could translate written texts}}, {{could not interpret spoken language}} (SB s. 36).")
a("u3k2", "shout", "kisa", soru="Çok yüksek sesle konuşmak: bağırmak. İngilizce yaz.", yanit="shout",
  aciklama=f"Bağırmak: {{{{shout}}}}; zıddı {{{{whisper}}}} {WB24}.")

# --- Konu 3: can, could, will be able to
a("u3k3", "could", "secim", soru="{{Many Ancient Romans ___ speak both Latin and Greek.}} Boşluğa hangisi gelir?",
  secenekler=["can", "will be able to", "could", "won't be able to"], dogru=2,
  aciklama="Geçmişteki yetenek: {{could}} (SB s. 37).")
a("u3k3", "will be able to", "eslestir", soru="Kalıbı anlattığı zamanla eşleştir.", ciftler=[
  {"sol": "can", "sag": "şimdi"},
  {"sol": "could", "sag": "geçmiş"},
  {"sol": "will be able to", "sag": "gelecek"}],
  aciklama=f"{{{{can}}}} şimdi, {{{{could}}}} geçmiş, {{{{will be able to}}}} gelecek {WB92}.")
a("u3k3", "Will … be able to …?", "dytablo", soru="Cümleler doğru mu, yanlış mı?", ifadeler=[
  {"s": "{{Will you can help me tomorrow?}}", "d": False},
  {"s": "{{I couldn't speak until I was three years old.}}", "d": True},
  {"s": "{{The school will be able let me know.}}", "d": False},
  {"s": "{{Will you be able to phone me when you get home?}}", "d": True}],
  aciklama="{{will can}} olmaz; {{be able}}'dan sonra {{to}} gelir (WB s. 30).")
a("u3k3", "couldn't", "bosluk", havuz=["will be able to", "could"], cumleler=[
  {"c": "When she was younger, she ___ speak Spanish.", "cevap": "couldn't"},
  {"c": "Today, you ___ see the Rosetta Stone in the British Museum.", "cevap": "can"},
  {"c": "Don't speak too quietly tomorrow. People ___ hear you.", "cevap": "won't be able to"}],
  aciklama="Geçmiş olumsuz, bugün, gelecek olumsuz: zaman ipuçlarına bak (SB s. 37, WB s. 93).")
a("u3k3", "will be able to", "secim", soru="Yetenek kalıpları:", onculler=["{{can}}'in gelecek hâli yoktur.", "{{could}} geçmişteki yeteneği anlatır.", "{{will be able to}}'dan sonra fiil {{-ing}} alır."],
  kok="Hangileri doğrudur?", secenekler=ONC, dogru=1,
  aciklama="{{will be able to}}'dan sonra fiil yalın gelir: {{will be able to chat}} (WB s. 92).")
a("u3k3", "can", "kisa", soru="{{Carlos is bilingual. He ___ speak Spanish and English perfectly.}} Boşluğa ne gelir? İngilizce yaz.", yanit="can",
  aciklama="Şimdiki yetenek: {{can}} (SB s. 37).")

# --- Konu 4: say ve tell
a("u3k4", "tell the truth", "secim", soru="Hangisi doğru bir kalıptır?",
  secenekler=["say the truth", "tell hello", "tell the truth", "say a joke"], dogru=2,
  aciklama=f"Doğruyu söylemek {{{{tell the truth}}}} {SB130}.")
a("u3k4", "say hello", "eslestir", soru="Kalıbı Türkçesiyle eşleştir.", ciftler=[
  {"sol": "say sorry", "sag": "özür dilemek"},
  {"sol": "tell a lie", "sag": "yalan söylemek"},
  {"sol": "tell a joke", "sag": "fıkra anlatmak"},
  {"sol": "say hello", "sag": "merhaba demek"}],
  aciklama="{{say}} ve {{tell}} kalıpları (SB s. 38).")
a("u3k4", "tell a joke", "bosluk", havuz=["spoke", "talked"], cumleler=[
  {"c": "Daniel ___ us a really funny joke.", "cevap": "told"},
  {"c": "I ___ sorry to Luisa yesterday.", "cevap": "said"},
  {"c": "Paula didn't ___ hello to me at the party.", "cevap": "say"}],
  aciklama="{{a joke}} → {{told}}; {{sorry}} → {{said}}; {{didn't}}'ten sonra {{say}} (SB s. 130, WB s. 30).")
a("u3k4", "tell a lie", "dy", ifade="{{I said her a lie.}} cümlesi doğrudur.", dogru=False,
  duzeltme="I told her a lie.",
  aciklama=f"Yalan {{{{tell}}}} ile: {{{{I told her a lie.}}}} {SB130}.")
a("u3k4", "say something in Italian", "secim", soru="{{say}} ile kullanılanlar:", onculler=["{{hello}}", "{{a story}}", "{{something in Italian}}"],
  kok="Hangileri {{say}} ile kullanılır?", secenekler=["Yalnız I", "I ve II", "I ve III", "I, II ve III"], dogru=2,
  aciklama="{{a story}} {{tell}} ile kullanılır: {{tell a story}} (SB s. 130).")
a("u3k4", "say yes/no", "kisa", soru="{{When you don't want to do something, you can always ___ no.}} Boşluğa ne gelir? İngilizce yaz.", yanit="say",
  aciklama="Hayır demek: {{say no}} (WB s. 30).")

# --- Konu 5: for / since, How long…?
a("u3k5", "since", "secim", soru="{{Mr Wilson has worked here ___ 2015.}} Boşluğa hangisi gelir?",
  secenekler=["for", "since", "ago", "in"], dogru=1,
  aciklama="Başlangıç yılı: {{since 2015}} (SB s. 39).")
a("u3k5", "for", "dytablo", soru="Cümleler doğru mu, yanlış mı?", ifadeler=[
  {"s": "{{I've been here for hours.}}", "d": True},
  {"s": "{{I've been here for 1 pm.}}", "d": False},
  {"s": "{{We've been best friends since 2009.}}", "d": True},
  {"s": "{{She has lived here since six months.}}", "d": False}],
  aciklama="Süre {{for}}, başlangıç {{since}} (SB s. 39, WB s. 92).")
a("u3k5", "for", "bosluk", havuz=["ago", "yet"], cumleler=[
  {"c": "I've lived here ___ about six months.", "cevap": "for"},
  {"c": "I haven't eaten anything ___ this morning.", "cevap": "since"},
  {"c": "___ long have you known your best friend?", "cevap": "How"}],
  aciklama="Süre {{for}}, başlangıç {{since}}, soru {{How long}} (SB s. 39).")
a("u3k5", HL, "secim", soru="{{Igor / live in Moscow}} Doğru soru hangisi?",
  secenekler=["How long does Igor live in Moscow?", "How long Igor has lived in Moscow?", "How long is Igor living in Moscow?", "How long has Igor lived in Moscow?"], dogru=3,
  aciklama="{{How long}} + {{has}} + özne + V3 (SB s. 39).")
a("u3k5", "since + cümle", "eslestir", soru="Cümle başlarını sonlarıyla eşleştir.", ciftler=[
  {"sol": "I've lived here for", "sag": "two years."},
  {"sol": "I've had this phone since", "sag": "2015."},
  {"sol": "Max has been on the computer since", "sag": "he woke up."},
  {"sol": "I've been able to speak French since", "sag": "I was a child."}],
  aciklama="Süre {{for}}; başlangıç ya da cümle {{since}} (WB s. 28).")
a("u3k5", "since", "kisa", soru="{{The Japanese have used emoji ___ 1999.}} Boşluğa ne gelir? İngilizce yaz.", yanit="since",
  aciklama="Başlangıç yılı: {{since 1999}} (WB s. 25).")

# --- Konu 6: Present perfect / past simple ve zaman ifadeleri
a("u3k6", "past simple", "secim", soru="{{He ___ me the same joke yesterday.}} Boşluğa hangisi gelir?",
  secenekler=["has told", "told", "have told", "tells"], dogru=1,
  aciklama="{{yesterday}} bitmiş zaman: {{told}} (WB s. 93).")
a("u3k6", "present perfect", "dytablo", soru="Cümleler doğru mu, yanlış mı?", ifadeler=[
  {"s": "{{My mother has worked at this museum since 2004.}}", "d": True},
  {"s": "{{They didn't begin the exam yet.}}", "d": False},
  {"s": "{{I fell off my bike yesterday.}}", "d": True},
  {"s": "{{I haven't done any exercise last week.}}", "d": False}],
  aciklama="{{since}}, {{yet}} present perfect; {{yesterday}}, {{last week}} past simple (WB s. 31, 93).")
a("u3k6", "all my life", "eslestir", soru="Zaman ifadesini anlamıyla eşleştir.", ciftler=[
  {"sol": "all my life", "sag": "since I was born"},
  {"sol": "over the last few years", "sag": "recently"},
  {"sol": "these days", "sag": "at the moment"},
  {"sol": "soon", "sag": "in the very near future"}],
  aciklama="Kitaptaki anlam eşleştirmesi (WB s. 29).")
a("u3k6", EVER, "secim", soru="{{Have you ever told a lie?}} – {{Yes, I have.}} Sonraki soru hangisi?",
  secenekler=["Who have you told the lie to yesterday?", "Who did you tell the lie to?", "Who you told the lie to?", "Have you ever told a lie?"], dogru=1,
  aciklama="Ayrıntı past simple ile sorulur: {{did}} + fiil yalın (WB s. 28).")
a("u3k6", "past simple", "secim", soru="Past simple ve present perfect:", onculler=["{{yesterday}} past simple ister.", "{{I've been to Liverpool.}} ne zaman gittiğini söylemez.", "{{last week}} past simple ister."],
  kok="Hangileri doğrudur?", secenekler=ONC, dogru=3,
  aciklama="Üçü de doğru: bitmiş zaman past simple; zaman söylenmezse present perfect (WB s. 92–93).")
a("u3k6", "present perfect", "kisa", soru="{{I ___ lived in London for about ten years – I love it here.}} Boşluğa ne gelir? İngilizce yaz.", yanit="have", kabul=["'ve"],
  aciklama="Hâlâ orada yaşıyor: {{have lived}} (WB s. 31).")
a("u3k6", "past simple", "dy", ifade="Languages metnine göre Steven Bird Tembé dili için bir telefon uygulaması geliştirdi.", dogru=True,
  aciklama="{{He developed a phone app to translate Tembé}} (SB s. 43).")
H.yaz()
