# ing1 Ünite 2: u2k1 (Sporlar ve Ekipman), u2k2 (Maç ve Yarışma), u2t1 (Ara Durak 1), u2k3 (Rutinler ve Sıklık), u2t2 (Ünite Sonu) konu dosyalarını üretir.
# Çalıştır: python3 gen_ing1_u2.py
import json, os
KOK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public", "ing1", "konular")
BG = "<svg viewBox='0 0 120 120' xmlns='http://www.w3.org/2000/svg' role='img'><rect width='120' height='120' rx='22' fill='#1b2340'/>"
def svg(ic): return BG + ic + "</svg>"
YUZ = "#ffd6a5"
U = "Unit 2: Sports"

# ---------------- SVG çizimleri ----------------
S_SWIM = svg("<path d='M10 70q10-8 20 0t20 0t20 0t20 0t20 0' stroke='#4fb3ff' stroke-width='5' fill='none' stroke-linecap='round'/>"
  "<path d='M10 88q10-8 20 0t20 0t20 0t20 0t20 0' stroke='#2f86d6' stroke-width='5' fill='none' stroke-linecap='round'/>"
  "<path d='M10 104q10-8 20 0t20 0t20 0t20 0t20 0' stroke='#2364c7' stroke-width='5' fill='none' stroke-linecap='round'/>"
  "<circle cx='52' cy='58' r='10' fill='" + YUZ + "'/><path d='M44 54h16' stroke='#ff7a33' stroke-width='5' stroke-linecap='round'/>"
  "<path d='M62 60q14-30 32-14' stroke='" + YUZ + "' stroke-width='6' fill='none' stroke-linecap='round'/>"
  "<path d='M38 64q-10-6-18 2' stroke='" + YUZ + "' stroke-width='6' fill='none' stroke-linecap='round'/>")
S_BIKE = svg("<circle cx='34' cy='82' r='18' stroke='#f2c14e' stroke-width='5' fill='none'/><circle cx='86' cy='82' r='18' stroke='#f2c14e' stroke-width='5' fill='none'/>"
  "<path d='M34 82l18-26h26l8 26M52 56l12 26h22M64 82l-4-34' stroke='#ff7a33' stroke-width='4' fill='none' stroke-linejoin='round' stroke-linecap='round'/>"
  "<path d='M54 48h12' stroke='#e9ecf5' stroke-width='4' stroke-linecap='round'/><circle cx='64' cy='24' r='9' fill='" + YUZ + "'/>"
  "<path d='M55 21a9 9 0 0 1 18 0z' fill='#3cc47c'/><path d='M64 33l-4 15M62 38l14 12' stroke='#3cc47c' stroke-width='5' stroke-linecap='round'/>")
S_SKI = svg("<path d='M0 60L120 108V98q0 22-22 22H22Q0 120 0 98z' fill='#e9ecf5'/><path d='M26 70l-2-2M96 98l2 2' stroke='#e9ecf5' stroke-width='2'/>"
  "<circle cx='50' cy='30' r='9' fill='" + YUZ + "'/><path d='M41 27a9 9 0 0 1 18 0z' fill='#e0464e'/>"
  "<path d='M50 39l6 22-12 14M56 50l14 6M50 46l-14 4' stroke='#e0464e' stroke-width='6' stroke-linecap='round' stroke-linejoin='round' fill='none'/>"
  "<path d='M56 61l10 18' stroke='#e0464e' stroke-width='6' stroke-linecap='round'/>"
  "<path d='M30 74l50 22M46 70l44 20' stroke='#2364c7' stroke-width='4' stroke-linecap='round'/>"
  "<path d='M70 56l10 28M36 50l-4 26' stroke='#a9b0c8' stroke-width='3' stroke-linecap='round'/>")
S_SKATE = svg("<ellipse cx='60' cy='96' rx='48' ry='12' fill='#bfe6ff'/><path d='M30 94q20 6 40 0' stroke='#ffffff' stroke-width='2' fill='none'/>"
  "<circle cx='54' cy='22' r='9' fill='" + YUZ + "'/><path d='M54 31v28' stroke='#b46be0' stroke-width='8' stroke-linecap='round'/>"
  "<path d='M54 38l-18-8M54 38l20-10' stroke='#b46be0' stroke-width='5' stroke-linecap='round'/>"
  "<path d='M54 59l-4 22M54 59l26 6' stroke='#b46be0' stroke-width='6' stroke-linecap='round'/>"
  "<path d='M42 84h16M46 81v3' stroke='#e9ecf5' stroke-width='3' stroke-linecap='round'/><path d='M40 88h22' stroke='#a9b0c8' stroke-width='3' stroke-linecap='round'/>")
S_JUDO = svg("<path d='M10 104h100' stroke='#3cc47c' stroke-width='6' stroke-linecap='round'/>"
  "<circle cx='38' cy='30' r='9' fill='" + YUZ + "'/><path d='M30 42h16l4 34H26z' fill='#f4f4f8'/><path d='M27 62h22' stroke='#1b2340' stroke-width='4'/>"
  "<path d='M32 76l-4 24M44 76l4 24' stroke='#f4f4f8' stroke-width='7' stroke-linecap='round'/><path d='M46 48l22 6' stroke='#f4f4f8' stroke-width='6' stroke-linecap='round'/>"
  "<circle cx='82' cy='30' r='9' fill='#c98b5a'/><path d='M74 42h16l4 34H70z' fill='#4f8ff7'/><path d='M71 62h22' stroke='#f2c14e' stroke-width='4'/>"
  "<path d='M76 76l-4 24M88 76l4 24' stroke='#4f8ff7' stroke-width='7' stroke-linecap='round'/><path d='M74 48l-14 10' stroke='#4f8ff7' stroke-width='6' stroke-linecap='round'/>")
S_OUT = svg("<circle cx='88' cy='30' r='14' fill='#f2c14e'/><path d='M88 8v6M88 46v6M66 30h6M104 30h6M73 15l4 4M99 41l4 4M103 15l-4 4' stroke='#f2c14e' stroke-width='3' stroke-linecap='round'/>"
  "<path d='M0 86q60-14 120 0V98q0 22-22 22H22Q0 120 0 98z' fill='#3cc47c'/><rect x='24' y='54' width='6' height='30' fill='#8a5a3b'/><circle cx='27' cy='46' r='16' fill='#2f9a5e'/>"
  "<circle cx='70' cy='92' r='10' fill='#f4f4f8'/><path d='M62 88l8 4 8-4M70 82v20' stroke='#1b2340' stroke-width='2' fill='none'/>")
S_EQUIP = svg("<ellipse cx='44' cy='44' rx='22' ry='28' stroke='#ff7a33' stroke-width='5' fill='none' transform='rotate(-30 44 44)'/>"
  "<path d='M34 34l20 20M28 46l20 20M44 30l18 18M30 58l20-20M40 66l20-20M24 46l18-18' stroke='#ffd0b0' stroke-width='1.5' transform='rotate(-30 44 44)' opacity='.8'/>"
  "<path d='M58 66l20 24' stroke='#c45c2a' stroke-width='8' stroke-linecap='round'/>"
  "<circle cx='92' cy='38' r='11' fill='#d8f04a'/><path d='M82 33q10 6 20 0M82 43q10-6 20 0' stroke='#f4f4f8' stroke-width='2' fill='none'/>"
  "<path d='M14 104h92M14 94h92M24 94v10M40 94v10M56 94v10M72 94v10M88 94v10' stroke='#e9ecf5' stroke-width='2'/>")

S_SPECT = svg("<path d='M10 98h100M10 78h100' stroke='#5a6280' stroke-width='4'/>"
  + "".join(f"<circle cx='{x}' cy='68' r='8' fill='{c}'/>" for x, c in [(24, YUZ), (46, '#c98b5a'), (68, YUZ), (90, '#e8b48a')])
  + "".join(f"<circle cx='{x}' cy='88' r='8' fill='{c}'/>" for x, c in [(34, '#e8b48a'), (56, YUZ), (78, '#c98b5a'), (100, YUZ)])
  + "<path d='M46 60l-6-16M46 60l6-16M90 60l-6-18M90 60l6-18' stroke='#f2c14e' stroke-width='4' stroke-linecap='round'/>"
  "")
S_MEDAL = svg("<path d='M40 12l20 42 20-42' stroke='#e0464e' stroke-width='12' fill='none' stroke-linejoin='round'/>"
  "<path d='M52 12l8 18 8-18' stroke='#4f8ff7' stroke-width='6' fill='none'/>"
  "<circle cx='60' cy='76' r='26' fill='#f2c14e'/><circle cx='60' cy='76' r='19' fill='none' stroke='#c99a20' stroke-width='3'/>"
  "<path d='M60 63l4 9 10 1-7 7 2 10-9-5-9 5 2-10-7-7 10-1z' fill='#fff3c4'/>")
S_INJ = svg("<path d='M44 10v58q0 22 22 22h22' stroke='" + YUZ + "' stroke-width='22' fill='none' stroke-linecap='round'/>"
  "<rect x='30' y='38' width='28' height='22' rx='4' fill='#f4f4f8'/><path d='M36 44v10M42 44v10M48 44v10M54 44v10' stroke='#d8dbe6' stroke-width='2'/>"
  "<path d='M88 30v20M78 40h20' stroke='#e0464e' stroke-width='7' stroke-linecap='round'/>"
  "<path d='M90 98l6 6M96 98l-6 6' stroke='#e0464e' stroke-width='3' stroke-linecap='round'/>")
def tabela(sol, sag, renkSol, renkSag, orta):
    return svg("<rect x='14' y='26' width='92' height='56' rx='10' fill='#0e1428' stroke='#5a6280' stroke-width='3'/>"
      f"<text x='38' y='68' font-size='34' font-family='sans-serif' font-weight='700' text-anchor='middle' fill='{renkSol}'>{sol}</text>"
      f"<text x='82' y='68' font-size='34' font-family='sans-serif' font-weight='700' text-anchor='middle' fill='{renkSag}'>{sag}</text>"
      + orta + "<path d='M40 82v14M80 82v14' stroke='#5a6280' stroke-width='4'/>")
S_DRAW = tabela("1", "1", "#f2c14e", "#f2c14e", "<path d='M54 52h12M54 60h12' stroke='#e9ecf5' stroke-width='4' stroke-linecap='round'/>") \
  .replace("</svg>", "<path d='M30 104h20M70 104h20' stroke='#f2c14e' stroke-width='5' stroke-linecap='round'/></svg>")
S_BEAT = tabela("2", "0", "#3cc47c", "#a9b0c8", "<path d='M56 56h8' stroke='#e9ecf5' stroke-width='4' stroke-linecap='round'/>") \
  .replace("</svg>", "<path d='M38 8l-6 6M38 8l6 6M38 8v12' stroke='#3cc47c' stroke-width='4' stroke-linecap='round'/>"
           "<path d='M30 104h20' stroke='#3cc47c' stroke-width='5' stroke-linecap='round'/></svg>")
S_SCORE = svg("<path d='M60 30h48v66H60' stroke='#f4f4f8' stroke-width='5' fill='none' stroke-linejoin='round'/>"
  "<path d='M68 30v66M76 30v66M84 30v66M92 30v66M100 30v66M60 46h48M60 62h48M60 78h48' stroke='#a9b0c8' stroke-width='1.5'/>"
  "<circle cx='82' cy='70' r='10' fill='#f4f4f8'/><path d='M74 66l8 4 8-4M82 60v20' stroke='#1b2340' stroke-width='2' fill='none'/>"
  "<path d='M14 96q20-40 52-30' stroke='#f2c14e' stroke-width='3' stroke-dasharray='4 5' fill='none'/>"
  "<path d='M10 104h100' stroke='#3cc47c' stroke-width='6' stroke-linecap='round'/>")
S_ACH = svg("<path d='M38 22h44v18q0 26-22 26t-22-26z' fill='#f2c14e'/><path d='M38 28H24q0 20 18 22M82 28h14q0 20-18 22' stroke='#f2c14e' stroke-width='5' fill='none'/>"
  "<rect x='54' y='66' width='12' height='16' fill='#c99a20'/><rect x='40' y='82' width='40' height='12' rx='3' fill='#c99a20'/>"
  "<path d='M60 30l3 7 8 1-6 5 2 8-7-4-7 4 2-8-6-5 8-1z' fill='#fff3c4'/>"
  "<path d='M16 14l3 6 6 3-6 3-3 6-3-6-6-3 6-3zM102 72l2 4 4 2-4 2-2 4-2-4-4-2 4-2z' fill='#e9ecf5'/>")

def K(ad, renk, svg_, aciklama, akilda, soru, ek=None, ornek=None, ornekTr=None):
    k = {"ad": ad, "renk": renk, "svg": svg_, "aciklama": aciklama}
    if ek: k["ek"] = ek
    k["akilda"] = akilda
    if ornek: k["ornek"], k["ornekTr"] = ornek, ornekTr
    k["soru"] = soru
    return k
def Q(soru, sec, dogru, ipucu, aciklama, **ek):
    q = {"soru": soru, "secenekler": sec, "dogru": dogru, "ipucu": ipucu, "aciklama": aciklama}
    q.update(ek); return q

# =================== u2k1 ===================
u2k1 = {
 "id": "u2k1", "unite": U, "baslik": "Sporlar ve Ekipman", "sayfalar": "s. 27–44",
 "giris": "Bu konuda sporların İngilizce adlarını öğreneceğiz: yüzme, bisiklet, kayak, buz pateni ve judo. Bir sporun dışarıda mı yapıldığını ({{outdoor}}) ve hangi eşyalarla yapıldığını ({{equipment}}) da anlatacağız. Kelimelere dokunarak dinleyebilirsin. Bu konunun sorusu: {{Which sport do you do?}} Yani: Hangi sporu yapıyorsun?",
 "kavramlar": [
  K("swimming", "#4fb3ff", S_SWIM, "Yüzme demektir. Kitapta: kollarını ve bacaklarını kullanarak suda ilerlemek.",
    "yüzme",
    Q("{{It is moving in water using your arms and legs.}} Hangi sporu anlatıyor?", ["Cycling", "Swimming", "Skiing"], 1,
      "Bilgi kartında suda yapılan spor vardı.", "Suda kollar ve bacaklarla ilerlemek {{swimming}}, yani yüzmedir. (s. 32)"),
    ek="Kitapta yüzmeye gitmek için {{go swimming}} denir. Havuz: {{swimming pool}}.",
    ornek="Then, I go to the gym and the swimming pool to train.", ornekTr="Sonra antrenman yapmak için spor salonuna ve yüzme havuzuna giderim. (s. 31)"),
  K("cycling", "#f2c14e", S_BIKE, "Bisiklet sürme sporudur.", "bisiklet sporu",
    Q("{{Burcu is a professional cyclist.}} Burcu hangi sporu yapıyor?", ["Ice skating", "Doing judo", "Cycling"], 2,
      "{{cyclist}} kelimesi {{cycling}} kelimesine benziyor.", "{{cyclist}} bisikletçi demektir. Burcu {{cycling}} yapar. (s. 44)"),
    ek="Bisiklet yapan kişi {{cyclist}}. Kitapta Mark şöyle der: {{I like riding my bike.}}",
    ornek="She prefers outdoor sports like climbing, cycling and surfing.", ornekTr="Tırmanma, bisiklet ve sörf gibi dış mekân sporlarını tercih eder. (s. 44)"),
  K("skiing", "#e9ecf5", S_SKI, "Kayak demektir. Karla kaplı dağda, ayağa takılan uzun kayaklarla kayılır.", "kayak",
    Q("Hangi spor karda yapılır?", ["Skiing", "Swimming", "Cycling"], 0,
      "Bilgi kartındaki resimde kar ve dağ vardı.", "{{skiing}} kayaktır; karla kaplı dağda yapılır. (s. 34)"),
    ek="Kayak yapmak: {{go skiing}}. Kitapta kayak, resimli sporlar listesinde geçer."),
  K("ice skating", "#b46be0", S_SKATE, "Buz pateni demektir. {{ice}} buz, {{skating}} paten kaymak.", "buz pateni",
    Q("{{ice skating}} kelimesindeki {{ice}} ne demek?", ["Kar", "Buz", "Su"], 1,
      "Kartta iki kelimenin anlamı ayrı ayrı yazıyordu.", "{{ice}} buz demektir. {{ice skating}} buz pateni. (s. 34)"),
    ek="İki kelimeden oluşur: {{ice}} + {{skating}}."),
  K("doing judo", "#4f8ff7", S_JUDO, "Judo yapmak demektir. Judo, iki kişinin karşılıklı yaptığı bir dövüş sporudur.", "judo yapmak",
    Q("Kitapta judo hangi fiille yazılmış?", ["going judo", "doing judo", "playing judo"], 1,
      "Kavramın adına bak: judonun önünde hangi kelime var?", "Kitapta {{doing judo}} yazar: judo yapmak. (s. 34)"),
    ek="Dikkat: yüzmeye {{go swimming}} deriz ama judo için {{do}} kullanılır: {{doing judo}}."),
  K("outdoor sport", "#3cc47c", S_OUT, "Dış mekân sporu demektir. Açık havada, dışarıda yapılan spor.", "dış mekân sporu",
    Q("{{Zeynep does outdoor sports such as hiking.}} Zeynep sporu nerede yapıyor?", ["Dışarıda, açık havada", "Evde", "Spor salonunda"], 0,
      "{{out}} dışarı demek. Kartı hatırla.", "{{outdoor}} dışarıda, açık havada demektir. Doğa yürüyüşü ({{hiking}}) dışarıda yapılır. (s. 42)"),
    ek="Zıttı {{indoor sport}}: kapalı alanda, salonda yapılan spor.",
    ornek="Zeynep does outdoor sports such as hiking.", ornekTr="Zeynep doğa yürüyüşü gibi dış mekân sporları yapar. (s. 42)"),
  K("equipment", "#ff7a33", S_EQUIP, "Ekipman, spor eşyası demektir. Bir sporu yapmak için gereken eşyalar.", "ekipman, eşya",
    Q("{{If you want to play tennis, you need special ___.}} Boşluğa hangisi gelir?", ["diet", "equipment", "injury"], 1,
      "Tenis için raket ve top gerekir. Bunlara ne deniyordu?", "Tenis için raket, top gibi özel eşyalar gerekir: {{equipment}}. (s. 43)"),
    ek="Kitaptaki tenis paragrafında ekipman: {{racket}} raket, {{ball}} top, {{net}} file.",
    ornek="If you want to play tennis, you need special equipment.", ornekTr="Tenis oynamak istiyorsan özel ekipmana ihtiyacın var. (s. 43)"),
 ],
 "gruplar": [{"soru": "Bu spor nerede yapılır?", "kutular": [
   {"etiket": "Suda", "uyeler": ["swimming"]},
   {"etiket": "Karda, buzda", "uyeler": ["skiing", "ice skating"]},
   {"etiket": "Yerde, karada", "uyeler": ["cycling", "doing judo"]}]}],
 "biliyorMusun": [
   "Kitaptaki tenis paragrafına göre bir oyuncu, rakibini yenmek için genellikle iki set kazanmalıdır: {{A player usually needs to win two sets.}} (s. 32)",
   "Kitapta Raymond kapalı alan sporlarını seçiyor, çünkü onları her havada yapabiliyor. Ona {{squash}} öneriliyor. (s. 44)"],
 "akildaKalsin": [
   "Sporlar: {{swimming}} yüzme, {{cycling}} bisiklet, {{skiing}} kayak, {{ice skating}} buz pateni.",
   "Fiillere dikkat: {{go swimming}}, {{go jogging}}, ama {{doing judo}} ve {{playing basketball}}.",
   "{{outdoor sport}} dışarıda, {{indoor sport}} kapalı alanda yapılır.",
   "{{equipment}}: sporun eşyaları. Tenis için {{racket}}, {{ball}}, {{net}}.",
   "Takım oyunu {{team game}}: basketbol. Tek kişilik spor {{individual sport}}: yüzme."],
 "merakKutusu": [
   {"soru": "{{go swimming}} mi, {{do swimming}} mi?", "cevap": "Kitapta {{go swimming}}, {{go running}}, {{go jogging}} geçer (s. 29–30). Judo için {{doing judo}} (s. 34), basketbol için {{playing basketball}} (s. 36) kullanılır."},
   {"soru": "{{indoor}} ve {{outdoor}} nereden geliyor?", "cevap": "{{door}} kapı demek. {{in}} içeri, {{out}} dışarı. {{indoor}} kapının içinde, yani kapalı alanda; {{outdoor}} dışarıda, açık havada."},
   {"soru": "Kapalı alan sporunun iyi yanı ne?", "cevap": "Kitapta Raymond şöyle diyor: kapalı alan sporlarını her havada yapabilirim. (s. 44)"},
   {"soru": "{{team game}} ile {{individual sport}} farkı ne?", "cevap": "Basketbol bir takım oyunudur; her takımda beş oyuncu vardır. Yüzme tek kişilik, bireysel bir spordur. (s. 32)"},
   {"soru": "{{athlete}} ne demek?", "cevap": "Sporcu demektir. Kitapta Doris kendini şöyle tanıtır: {{I'm an athlete.}} (s. 29)"}],
 "dusunVeYaz": [{"soru": "En sevdiğin sporu İngilizce iki cümleyle anlat. Birinci cümle {{My favourite sport is}} ile başlasın. İkinci cümlede dışarıda mı, kapalı alanda mı yapıldığını yaz.",
   "ornekCevap": "My favourite sport is swimming. It is an indoor sport.", "anahtarlar": ["favourite", "sport", "door"]}],
 "sorular": [
  Q("Dinle. Hangi kelimeyi duydun?", ["skiing", "cycling", "swimming"], 1, "Bisikletle ilgili kelimeyi duydun. Yavaş dinle düğmesini dene.",
    "Duyduğun kelime {{cycling}}: bisiklet sporu. (s. 34)", dinle="cycling", kavram="cycling"),
  Q("Dinle. Hangi kelimeyi duydun?", ["skiing", "surfing", "swimming"], 0, "Karda yapılan sporun adını duydun. Bir daha dinle.",
    "Duyduğun kelime {{skiing}}: kayak. (s. 34)", dinle="skiing", kavram="skiing"),
  Q("Dinle. Hangi cümleyi duydun?", ["You need special medals.", "You need a special diet.", "You need special equipment."], 2,
    "Cümlenin sonundaki kelimeyi dinle: spor eşyaları.", "Duyduğun cümle {{You need special equipment.}}: Özel ekipmana ihtiyacın var. (s. 43)",
    dinle="You need special equipment.", kavram="equipment"),
  Q("Tenis oynamak için hangi ekipman gerekir?", ["A medal", "A swimming pool", "A racket"], 2,
    "Kitaptaki tenis paragrafında topa ne ile vuruluyordu?", "{{They hit a ball with a racket.}} Topa raketle vurulur. (s. 32)", kavram="equipment"),
  Q("{{It's an individual sport. You should do it in a pool or in the sea.}} Hangi spor?", ["Cycling", "Swimming", "Doing judo"], 1,
    "Havuzda ya da denizde yapılan sporu düşün.", "Havuzda ya da denizde yapılan bireysel spor {{swimming}}dir. (s. 32)", kavram="swimming"),
  Q("Burcu bisiklet sporcusudur. Hangi cümle onu anlatır?", ["She is a professional cyclist.", "She is a professional skier.", "She is a swimmer."], 0,
    "{{cycling}} yapan kişiye ne denir?", "{{She is a professional cyclist.}} Profesyonel bisikletçidir. (s. 44)", kavram="cycling",
    yardim={"adimlar": ["Burcu hangi sporu yapıyor? Bisiklet.", "Bisiklet sporu {{cycling}}.", "Bu spor yapan kişinin adı {{cycl-}} ile başlar."]}),
  Q("Buz pateni İngilizce nasıl söylenir?", ["skiing", "surfing", "ice skating"], 2,
    "Buz {{ice}} demekti.", "Buz pateni {{ice skating}}dir. (s. 34)", kavram="ice skating"),
  Q("Hangisi doğru yazılmış?", ["I like going judo.", "I like doing judo.", "I like playing judo."], 1,
    "Judo hangi fiille kullanılıyordu? Kavramın adına bak.", "Judo için {{do}} kullanılır: {{doing judo}}. (s. 34)", kavram="doing judo"),
  Q("{{Zeynep does outdoor sports such as hiking.}} {{outdoor}} ne demek?", ["Kapalı alanda", "Suda", "Dışarıda, açık havada"], 2,
    "{{out}} kelimesinin anlamını hatırla.", "{{outdoor}} dışarıda, açık havada demektir. (s. 42)", kavram="outdoor sport"),
  Q("Raymond: {{I prefer indoor sports because ___.}} Hangisi uygun?", ["I like sunny and hot days", "I can do it in all kinds of weather condition", "I prefer exercising in open air"], 1,
    "Kapalı alanda yağmur, kar sorun olur mu?", "Kapalı alan sporu her havada yapılabilir. Açık hava ve güneş dış mekânı anlatır. (s. 44)", kavram="outdoor sport",
    yardim={"adimlar": ["{{indoor}} kapalı alan demek.", "Şıklardan hangileri açık havayı, güneşi anlatıyor? Onları ele.", "Kalan şık kapalı alanın iyi yanını söylüyor mu?"]}),
 ],
 "kelimeler": [
  {"en": "indoor sport", "tr": "kapalı alan sporu", "ornek": "I prefer indoor sports because I can do it in all kinds of weather condition.", "ornekTr": "Kapalı alan sporlarını tercih ederim, çünkü her havada yapabilirim. (s. 44)"},
  {"en": "jogging", "tr": "koşu (hafif tempolu)", "ornek": "I like doing jogging in the park.", "ornekTr": "Parkta koşu yapmayı severim. (s. 42)"},
  {"en": "surfing", "tr": "sörf", "ornek": "She prefers outdoor sports like climbing, cycling and surfing.", "ornekTr": "Tırmanma, bisiklet ve sörf gibi dış mekân sporlarını tercih eder. (s. 44)"},
  {"en": "climbing", "tr": "tırmanma"},
  {"en": "hiking", "tr": "doğa yürüyüşü", "ornek": "Zeynep does outdoor sports such as hiking.", "ornekTr": "Zeynep doğa yürüyüşü gibi dış mekân sporları yapar. (s. 42)"},
  {"en": "tennis", "tr": "tenis", "ornek": "If you want to play tennis, you need special equipment.", "ornekTr": "Tenis oynamak istiyorsan özel ekipmana ihtiyacın var. (s. 43)"},
  {"en": "basketball", "tr": "basketbol", "ornek": "I play basketball twice a week, but I often ride my bike.", "ornekTr": "Haftada iki kez basketbol oynarım, ama sık sık bisiklete binerim. (s. 36)"},
  {"en": "gym", "tr": "spor salonu", "ornek": "I'm going to the gym to work out.", "ornekTr": "Spor yapmak için spor salonuna gidiyorum. (s. 43)"},
  {"en": "court", "tr": "kort, saha", "ornek": "You can see the players playing this sport in a court.", "ornekTr": "Bu sporu oynayan oyuncuları bir kortta görebilirsin. (s. 32)"},
  {"en": "racket", "tr": "raket", "ornek": "They hit a ball with a racket to throw it over the net.", "ornekTr": "Topu filenin üstünden atmak için ona raketle vururlar. (s. 32)"},
  {"en": "net", "tr": "file"},
  {"en": "team game", "tr": "takım oyunu", "ornek": "It is a team game.", "ornekTr": "Bu bir takım oyunudur. (s. 32)"},
 ],
 "cumleler": [
  {"en": "I like doing jogging in the park.", "tr": "Parkta koşu yapmayı severim. (s. 42)"},
  {"en": "Zeynep does outdoor sports such as hiking.", "tr": "Zeynep doğa yürüyüşü gibi dış mekân sporları yapar. (s. 42)"},
  {"en": "It is a team game.", "tr": "Bu bir takım oyunudur. (s. 32)"},
  {"en": "It's an individual sport.", "tr": "Bu bireysel bir spordur. (s. 32)"},
  {"en": "It's an outdoor sport.", "tr": "Bu bir dış mekân sporudur. (s. 44)"},
  {"en": "You can play squash, then.", "tr": "O zaman squash oynayabilirsin. (s. 44)"},
 ],
 "hatalar": [
  {"cumle": "Football is an indoor sport.", "yanlis": "indoor", "secenekler": ["outdoor", "individual", "special"], "dogru": 0,
   "tr": "Futbol bir dış mekân sporudur.", "aciklama": "Futbol dışarıda, sahada oynanır: {{Football is an outdoor sport.}} (s. 40)"},
  {"cumle": "I like do jogging in the park.", "yanlis": "do", "secenekler": ["does", "doing", "did"], "dogru": 1,
   "tr": "Parkta koşu yapmayı severim.", "aciklama": "{{like}} kelimesinden sonra fiil {{-ing}} alır: {{I like doing jogging.}} (s. 42)"},
  {"cumle": "She prefer outdoor sports like climbing and surfing.", "yanlis": "prefer", "secenekler": ["preferring", "is prefer", "prefers"], "dogru": 2,
   "tr": "Tırmanma ve sörf gibi dış mekân sporlarını tercih eder.", "aciklama": "{{She}} ile fiil {{-s}} alır: {{She prefers}}. (s. 44)"},
  {"cumle": "If you want to play tennis, you need special injury.", "yanlis": "injury", "secenekler": ["equipment", "spectator", "medal"], "dogru": 0,
   "tr": "Tenis oynamak istiyorsan özel ekipmana ihtiyacın var.", "aciklama": "Tenis için gereken eşyalar {{equipment}}tır. {{injury}} sakatlık demek. (s. 43)"},
  {"cumle": "They hit a ball with a racket to throw it over the gym.", "yanlis": "gym", "secenekler": ["court", "net", "pool"], "dogru": 1,
   "tr": "Topu filenin üstünden atmak için ona raketle vururlar.", "aciklama": "Tenis topu filenin, yani {{net}}in üstünden atılır. (s. 32)"},
 ],
 "resimEslestir": True,
 "okuma": {
  "baslik": "Which sport is it?", "sayfa": "s. 32",
  "sozluk": {"court": "kort, saha", "racket": "raket", "net": "file", "opponent": "rakip", "make a point": "sayı yapmak", "sets": "setler", "beat": "yenmek",
             "team game": "takım oyunu", "cheering for": "-e tezahürat yapıyorlar", "threw": "attı", "final score": "son skor",
             "individual sport": "bireysel spor", "arms and legs": "kollar ve bacaklar", "breaststroke": "kurbağalama (yüzme stili)", "freestyle": "serbest stil", "pool": "havuz"},
  "bolumler": [
   {"baslik": "Raket ve top", "cumleler": [
     {"en": "You can see the players playing this sport in a court.", "tr": "Bu sporu oynayan oyuncuları bir kortta görebilirsin."},
     {"en": "They hit a ball with a racket to throw it over the net.", "tr": "Topu filenin üstünden atmak için ona raketle vururlar."},
     {"en": "The ball must touch the opponent's side to make a point.", "tr": "Sayı yapmak için top rakibin tarafına değmelidir."},
     {"en": "A player usually needs to win two sets to beat his/her opponent.", "tr": "Bir oyuncu rakibini yenmek için genellikle iki set kazanmalıdır."},
     {"en": "It is a team game.", "tr": "Bu bir takım oyunudur."},
     {"en": "The players' goal is to make as many scores as they can.", "tr": "Oyuncuların amacı yapabildikleri kadar çok sayı yapmaktır."},
     {"en": "Five players in each team play the game.", "tr": "Oyunu her takımda beş oyuncu oynar."},
     {"en": "Listen!", "tr": "Dinle!"},
     {"en": "Spectators are cheering for Roger.", "tr": "Seyirciler Roger'a tezahürat yapıyor."},
     {"en": "He threw the ball, and the final score is 63-64 now.", "tr": "Topu attı ve şimdi son skor 63-64."}],
    "sorular": [
     Q("İlk paragraftaki sporda top neyin üstünden atılıyor?", ["Filenin", "Duvarın", "Kalenin"], 0,
       "{{over the net}} kalıbını bul.", "{{They hit a ball with a racket to throw it over the net.}} Top filenin üstünden atılır; bu spor tenistir."),
     Q("İkinci paragraftaki oyunda her takımda kaç oyuncu var?", ["Üç", "On bir", "Beş"], 2,
       "{{players in each team}} cümlesine bak.", "{{Five players in each team play the game.}} Her takımda beş oyuncu var; bu oyun basketboldur.")]},
   {"baslik": "Suda", "cumleler": [
     {"en": "It's an individual sport.", "tr": "Bu bireysel bir spordur."},
     {"en": "It is moving in water using your arms and legs.", "tr": "Kollarını ve bacaklarını kullanarak suda ilerlemektir."},
     {"en": "There are different styles in that sport like breaststroke or freestyle.", "tr": "Bu sporda kurbağalama ya da serbest stil gibi farklı stiller vardır."},
     {"en": "You should do it in a pool or in the sea.", "tr": "Bunu havuzda ya da denizde yapmalısın."}],
    "sorular": [
     Q("Bu paragraf hangi sporu anlatıyor?", ["Cycling", "Swimming", "Skiing"], 1,
       "{{moving in water}}: suda ilerlemek.", "Suda kollar ve bacaklarla ilerlemek yüzmedir: {{swimming}}."),
     Q("Bu spor nerede yapılır?", ["Havuzda ya da denizde", "Kortta", "Karla kaplı dağda"], 0,
       "Son cümleye bak: {{in a pool or in the sea}}.", "{{You should do it in a pool or in the sea.}} Havuzda ya da denizde yapılır.")]}]}
}

# =================== u2k2 ===================
u2k2 = {
 "id": "u2k2", "unite": U, "baslik": "Maç ve Yarışma", "sayfalar": "s. 27–44",
 "giris": "Bu konuda maç ve yarışmaları anlatan İngilizce kelimeleri öğreneceğiz: seyirci, madalya, sakatlık, berabere, yenmek, skor ve başarı. Kelimelere dokunarak dinleyebilirsin. Bu konunun sorusu: {{What was the score?}} Yani: Skor neydi?",
 "kavramlar": [
  K("spectator", "#f2c14e", S_SPECT, "Seyirci demektir. Maçı tribünden izleyen kişi.", "seyirci",
    Q("{{More than fifty thousand spectators watched the final match.}} {{spectators}} ne yapıyor?", ["Maçı oynuyor", "Maçı izliyor", "Maçı yönetiyor"], 1,
      "Kartta seyirci kelimesinin anlamı vardı.", "{{spectators}} seyircilerdir; maçı izlerler: {{watched the final match}}. (s. 42)"),
    ek="Çoğulu {{spectators}}. Kitapta: {{Spectators are cheering for Roger.}} Seyirciler Roger'a tezahürat yapıyor.",
    ornek="More than fifty thousand spectators watched the final match.", ornekTr="Elli binden fazla seyirci final maçını izledi. (s. 42)"),
  K("medal", "#c99a20", S_MEDAL, "Madalya demektir. Yarışmada dereceye girene verilir.", "madalya",
    Q("{{Sheila won the gold medal.}} Sheila ne kazandı?", ["Altın madalya", "Kupa", "Para"], 0,
      "{{gold}} altın, {{medal}} madalya.", "{{gold medal}} altın madalyadır. (s. 42)"),
    ek="Altın madalya {{gold medal}}. Madalya kazanmak: {{win a medal}}; geçmişte {{won}}.",
    ornek="Sheila won the gold medal in the National Swimming Championship.", ornekTr="Sheila Ulusal Yüzme Şampiyonası'nda altın madalyayı kazandı. (s. 42)"),
  K("injury", "#e0464e", S_INJ, "Sakatlık demektir. Spor yaparken vücudun incinmesi.", "sakatlık",
    Q("{{Sportsmen may have some injuries while doing exercises.}} {{injuries}} ne demek?", ["Madalyalar", "Sakatlıklar", "Seyirciler"], 1,
      "Kartta yara bandı vardı.", "{{injuries}} sakatlıklardır. Spor yaparken sakatlanabiliriz. (s. 40)"),
    ek="Çoğulu {{injuries}}. Kitapta: {{Sportsmen may have some injuries.}}",
    ornek="Sportsmen may have some injuries while doing exercises.", ornekTr="Sporcular egzersiz yaparken bazı sakatlıklar yaşayabilir. (s. 40)"),
  K("draw", "#a9b0c8", S_DRAW, "Sporda berabere demektir. İki takımın skoru eşit olunca maç berabere biter.", "berabere",
    Q("{{The score was a draw.}} Maç nasıl bitti?", ["Biz kazandık", "Biz kaybettik", "Berabere"], 2,
      "Kartta skor tabelasında iki sayı eşitti.", "{{draw}} berabere demektir; skor eşittir. (s. 40)"),
    ek="Dikkat: {{draw}} resim çizmek de demektir. Maçta ise berabere.",
    ornek="The score was a draw.", ornekTr="Skor berabereydi. (s. 42)"),
  K("beat", "#3cc47c", S_BEAT, "Yenmek demektir. Bir takımı ya da rakibi maçta yenmek.", "yenmek",
    Q("{{Our school team beat the opponent team 2-0.}} Kim kazandı?", ["Okul takımımız", "Rakip takım", "Kimse"], 0,
      "{{beat}} yenmek demekti. Kim kimi yendi?", "Okul takımımız rakibi 2-0 yendi. (s. 40)"),
    ek="{{beat}} + rakip: {{beat the opponent}}. Zıttı {{lose}}: kaybetmek.",
    ornek="Our school team beat the opponent team 2-0.", ornekTr="Okul takımımız rakip takımı 2-0 yendi. (s. 40)"),
  K("score", "#ff7a33", S_SCORE, "Skor demektir. Fiil olarak sayı ya da gol atmak.", "skor, gol atmak",
    Q("{{The final score is 63-64 now.}} {{score}} burada ne demek?", ["Seyirci", "Skor", "Takım"], 1,
      "Cümlede sayılar var: 63-64.", "{{final score}} son skordur: 63-64. (s. 32)"),
    ek="Gol atmak: {{score a goal}}. Kitapta {{hit three goals}} de geçer: üç gol attı.",
    ornek="None of the teams could score a goal.", ornekTr="Takımların hiçbiri gol atamadı. (s. 40)"),
  K("achievement", "#b46be0", S_ACH, "Başarı demektir. Çok emek verip elde edilen güzel sonuç.", "başarı",
    Q("{{Katie won five gold medals last year. It was a great ___.}}", ["injury", "draw", "achievement"], 2,
      "Beş altın madalya kazanmak iyi bir şey mi, kötü mü?", "Beş altın madalya büyük bir başarıdır: {{achievement}}. (s. 40)"),
    ek="Büyük başarı: {{a great achievement}}.",
    ornek="It was a great achievement.", ornekTr="Büyük bir başarıydı. (s. 40)"),
 ],
 "gruplar": [{"soru": "Bu kelime iyi bir şey mi, kötü bir şey mi, yoksa ikisi de değil mi?", "kutular": [
   {"etiket": "İyi sonuç", "uyeler": ["medal", "beat", "achievement"]},
   {"etiket": "Kötü olay", "uyeler": ["injury"]},
   {"etiket": "Ne iyi ne kötü", "uyeler": ["draw", "spectator", "score"]}]}],
 "biliyorMusun": [
   "Kitaptaki röportajda yüzücü Emma'nın hayali, altı Olimpiyatta yarışarak altı altın madalya kazanan ilk kadın yüzücü olmak. (s. 31)",
   "Naim Süleymanoğlu kısa boylu ama çok güçlü olduğu için {{Pocket Hercules}} diye anılır. (s. 36)"],
 "akildaKalsin": [
   "{{spectator}} seyirci, {{medal}} madalya, {{injury}} sakatlık.",
   "Skor eşitse {{draw}}: berabere.",
   "Rakibi yenmek {{beat}}; madalya ya da maç kazanmak {{win}} ({{won}}).",
   "{{score}} skor; {{score a goal}} gol atmak.",
   "Büyük başarı: {{a great achievement}}."],
 "merakKutusu": [
   {"soru": "{{draw}} resim çizmek değil miydi?", "cevap": "Evet, ama sporda berabere demektir. Kitapta: {{The score was a draw. None of the teams could score a goal.}} (s. 40)"},
   {"soru": "{{beat}} ile {{win}} farkı ne?", "cevap": "{{beat}} birini yenmektir: {{beat the opponent team}}. {{win}} bir şeyi kazanmaktır: {{won five gold medals}}. (s. 40)"},
   {"soru": "{{opponent}} kim?", "cevap": "Rakip demektir; maçta karşı taraf. Tenis paragrafında top rakibin tarafına değince sayı olur. (s. 32)"},
   {"soru": "{{score}} hem isim hem fiil mi?", "cevap": "Evet. İsim: {{the final score is 63-64}} son skor. Fiil: {{score a goal}} gol atmak. (s. 32, s. 40)"},
   {"soru": "{{champion}} ne demek?", "cevap": "Şampiyon demektir. Kitapta: {{Naim became a champion in many competitions.}} (s. 36)"}],
 "dusunVeYaz": [{"soru": "İzlediğin ya da oynadığın bir maçı İngilizce iki cümleyle anlat. Skor neydi? Kim kazandı ya da berabere mi bitti?",
   "ornekCevap": "The score was 2-0. Our team beat the other team.", "anahtarlar": ["score", "team", "beat"]}],
 "sorular": [
  Q("Dinle. Hangi kelimeyi duydun?", ["medal", "match", "racket"], 0, "Yarışmada kazanılan bir şey. Yavaş dinle düğmesini dene.",
    "Duyduğun kelime {{medal}}: madalya. (s. 42)", dinle="medal", kavram="medal"),
  Q("Dinle. Hangi cümleyi duydun?", ["The score was a goal.", "The score was a draw.", "The match was long."], 1,
    "Cümlenin son kelimesine dikkat et: berabere.", "Duyduğun cümle {{The score was a draw.}}: Skor berabereydi. (s. 42)", dinle="The score was a draw.", kavram="draw"),
  Q("{{There were thousands of ___ in the stadium to watch the final match.}}", ["spectators", "injuries", "medals"], 0,
    "Stadyumda maçı izleyen kim?", "Maçı izleyenler seyircilerdir: {{spectators}}. (s. 40)", kavram="spectator"),
  Q("{{James trains very hard because ___.}} Hangisi uygun?", ["he made a goal", "he's very healthy", "he wants to get the gold medal"], 2,
    "Neden çok çalışır? Bir şey kazanmak istiyor.", "{{James trains very hard because he wants to get the gold medal.}} Altın madalyayı istediği için çok çalışır. (s. 39)", kavram="medal"),
  Q("{{Sportsmen may have some ___ while doing exercises.}}", ["achievements", "injuries", "spectators"], 1,
    "Egzersiz yaparken başımıza gelebilecek kötü bir şey.", "Egzersiz yaparken sakatlık olabilir: {{injuries}}. (s. 40)", kavram="injury"),
  Q("{{The score was a draw. None of the teams could score a goal.}} Skor ne olabilir?", ["2-0", "0-0", "1-0"], 1,
    "Hiçbir takım gol atamadıysa iki taraf da kaç gol attı?", "Hiçbir takım gol atamadı: 0-0, yani berabere. (s. 40)", kavram="draw",
    yardim={"adimlar": ["{{draw}} berabere demek: iki taraf eşit.", "{{None of the teams could score a goal.}} Hiçbir takım gol atamadı.", "İki taraf da eşit ve hiç gol yok. Hangi skor böyle?"]}),
  Q("Takımımız rakibi 2-0 yendi. {{Our team ___ the opponent team 2-0.}}", ["lost", "drew", "beat"], 2,
    "Yenmek hangi kelimeydi?", "Yenmek {{beat}}tir: {{Our school team beat the opponent team 2-0.}} (s. 40)", kavram="beat"),
  Q("{{beat}} kelimesinin zıt anlamlısı hangisi?", ["lose", "win", "train"], 0,
    "Yenmenin tersi ne olur?", "{{beat}} yenmek, {{lose}} kaybetmektir. (s. 40)", kavram="beat"),
  Q("{{He threw the ball, and the final score is 63-64 now.}} {{final score}} ne demek?", ["Son oyuncu", "Son maç", "Son skor"], 2,
    "{{final}} son demek. {{score}} kartta neydi?", "{{final score}} son skor demektir. (s. 32)", kavram="score"),
  Q("{{Katie won five gold medals last year.}} Bu ne anlatıyor?", ["A great achievement", "A bad injury", "A draw"], 0,
    "Beş altın madalya iyi bir sonuç mu?", "Beş altın madalya büyük bir başarıdır: {{It was a great achievement.}} (s. 40)", kavram="achievement"),
 ],
 "kelimeler": [
  {"en": "win", "tr": "kazanmak (geçmiş: won)", "ornek": "He won three Olympic gold medals and many other prizes.", "ornekTr": "Üç Olimpiyat altın madalyası ve başka birçok ödül kazandı. (s. 36)"},
  {"en": "lose", "tr": "kaybetmek"},
  {"en": "opponent", "tr": "rakip", "ornek": "The ball must touch the opponent's side to make a point.", "ornekTr": "Sayı yapmak için top rakibin tarafına değmelidir. (s. 32)"},
  {"en": "champion", "tr": "şampiyon"},
  {"en": "gold medal", "tr": "altın madalya", "ornek": "Sheila won the gold medal in the National Swimming Championship.", "ornekTr": "Sheila Ulusal Yüzme Şampiyonası'nda altın madalyayı kazandı. (s. 42)"},
  {"en": "match", "tr": "maç", "ornek": "More than fifty thousand spectators watched the final match.", "ornekTr": "Elli binden fazla seyirci final maçını izledi. (s. 42)"},
  {"en": "compete", "tr": "yarışmak"},
  {"en": "train", "tr": "antrenman yapmak", "ornek": "I train six days a week.", "ornekTr": "Haftada altı gün antrenman yaparım. (s. 31)"},
  {"en": "work out", "tr": "spor yapmak, egzersiz yapmak", "ornek": "I'm going to the gym to work out.", "ornekTr": "Spor yapmak için spor salonuna gidiyorum. (s. 43)"},
  {"en": "athlete", "tr": "sporcu", "ornek": "I'm an athlete.", "ornekTr": "Ben bir sporcuyum. (s. 29)"},
 ],
 "cumleler": [
  {"en": "The score was a draw.", "tr": "Skor berabereydi. (s. 42)"},
  {"en": "Larry hit three goals in the last match.", "tr": "Larry son maçta üç gol attı. (s. 42)"},
  {"en": "Sheila won the gold medal.", "tr": "Sheila altın madalyayı kazandı. (s. 42)"},
  {"en": "It was a great achievement.", "tr": "Büyük bir başarıydı. (s. 40)"},
  {"en": "Spectators are cheering for Roger.", "tr": "Seyirciler Roger'a tezahürat yapıyor. (s. 32)"},
  {"en": "Our school team beat the opponent team.", "tr": "Okul takımımız rakip takımı yendi. (s. 40)"},
 ],
 "hatalar": [
  {"cumle": "There were thousands of medals in the stadium to watch the match.", "yanlis": "medals", "secenekler": ["spectators", "injuries", "rackets"], "dogru": 0,
   "tr": "Maçı izlemek için stadyumda binlerce seyirci vardı.", "aciklama": "Maçı izleyenler seyircilerdir: {{spectators}}. (s. 40)"},
  {"cumle": "The score was a beat. None of the teams could score a goal.", "yanlis": "beat", "secenekler": ["medal", "draw", "win"], "dogru": 1,
   "tr": "Skor berabereydi. Takımların hiçbiri gol atamadı.", "aciklama": "Kimse gol atamadıysa maç berabere biter: {{draw}}. (s. 40)"},
  {"cumle": "Katie win five gold medals last year.", "yanlis": "win", "secenekler": ["wins", "winning", "won"], "dogru": 2,
   "tr": "Katie geçen yıl beş altın madalya kazandı.", "aciklama": "{{last year}} geçmişi anlatır; {{win}} geçmişte {{won}} olur. (s. 40)"},
  {"cumle": "Sportsmen may have some achievements while doing exercises.", "yanlis": "achievements", "secenekler": ["injuries", "spectators", "draws"], "dogru": 0,
   "tr": "Sporcular egzersiz yaparken bazı sakatlıklar yaşayabilir.", "aciklama": "Egzersizde başa gelebilecek kötü şey sakatlıktır: {{injuries}}. (s. 40)"},
  {"cumle": "Our school team lose the opponent team 2-0.", "yanlis": "lose", "secenekler": ["draw", "beat", "score"], "dogru": 1,
   "tr": "Okul takımımız rakip takımı 2-0 yendi.", "aciklama": "Rakibi yenmek {{beat}}tir. (s. 40)"},
 ],
 "okuma": {
  "baslik": "Naim Süleymanoğlu", "sayfa": "s. 36",
  "sozluk": {"weightlifting": "halter", "talented": "yetenekli", "champion": "şampiyon", "competitions": "yarışmalar", "world championship": "dünya şampiyonası",
             "represented": "temsil etti", "prizes": "ödüller", "Pocket Hercules": "Cep Herkülü", "short but very strong": "kısa ama çok güçlü",
             "inspired": "ilham verdi", "athletes": "sporcular", "worked hard": "çok çalıştı", "anything is possible": "her şey mümkündür", "passed away": "vefat etti"},
  "bolumler": [
   {"baslik": "Küçük yaşta şampiyon", "cumleler": [
     {"en": "Naim Süleymanoğlu was born on January 23, 1967, in Bulgaria.", "tr": "Naim Süleymanoğlu 23 Ocak 1967'de Bulgaristan'da doğdu."},
     {"en": "He started weightlifting when he was very young.", "tr": "Çok küçükken haltere başladı."},
     {"en": "He was very strong and talented.", "tr": "Çok güçlü ve yetenekliydi."},
     {"en": "Naim became a champion in many competitions and won his first world championship at the age of 15.", "tr": "Naim birçok yarışmada şampiyon oldu ve ilk dünya şampiyonluğunu 15 yaşında kazandı."},
     {"en": "In 1986, he moved to Türkiye and represented the country in the Olympics.", "tr": "1986'da Türkiye'ye taşındı ve Olimpiyatlarda ülkeyi temsil etti."}],
    "sorular": [
     Q("Naim hangi sporu yaptı?", ["Yüzme", "Halter", "Judo"], 1,
       "{{He started weightlifting}} cümlesini bul.", "{{weightlifting}} halterdir. Naim çok küçükken haltere başladı."),
     Q("Naim ilk dünya şampiyonluğunu kaç yaşında kazandı?", ["15", "23", "19"], 0,
       "{{at the age of}} kalıbından sonraki sayıya bak.", "{{won his first world championship at the age of 15}}: 15 yaşında.")]},
   {"baslik": "Cep Herkülü", "cumleler": [
     {"en": "He won three Olympic gold medals and many other prizes.", "tr": "Üç Olimpiyat altın madalyası ve başka birçok ödül kazandı."},
     {"en": "People called him the \"Pocket Hercules\" because he was short but very strong.", "tr": "İnsanlar ona \"Cep Herkülü\" dedi, çünkü kısa boyluydu ama çok güçlüydü."},
     {"en": "Naim Süleymanoğlu inspired many young athletes.", "tr": "Naim Süleymanoğlu birçok genç sporcuya ilham verdi."},
     {"en": "He worked hard and showed that anything is possible.", "tr": "Çok çalıştı ve her şeyin mümkün olduğunu gösterdi."},
     {"en": "He passed away on November 18, 2017.", "tr": "18 Kasım 2017'de vefat etti."}],
    "sorular": [
     Q("Naim kaç Olimpiyat altın madalyası kazandı?", ["Altı", "Bir", "Üç"], 2,
       "{{gold medals}} kelimesinden önceki sayıya bak.", "{{He won three Olympic gold medals.}} Üç altın madalya kazandı."),
     Q("Ona neden \"Cep Herkülü\" dediler?", ["Kısa ama çok güçlü olduğu için", "Çok uzun olduğu için", "Çok hızlı koştuğu için"], 0,
       "{{because}} kelimesinden sonrasını oku.", "{{because he was short but very strong}}: kısa ama çok güçlü olduğu için.")]}]}
}

# =================== u2t1 ===================
u2t1 = {
 "id": "u2t1", "tur": "tarama", "unite": U, "baslik": "Ara Durak 1: Spor Dünyası", "sayfalar": "Konu 1–2 · s. 27–44",
 "giris": "İki konu bitti! Kısa bir mola verelim. Önce özetleri oku ve kartlara dokun. Sonra tarama testini çöz. Not yok; neyi iyi bildiğini ve neye tekrar bakacağını bulacağız.",
 "buyukResim": "Önce sporların adlarını ve eşyalarını öğrendik, sonra o sporların maçlarını. Kitaptaki basketbol paragrafı ikisini birleştiriyor: bir takım oyunu, seyirciler ve skor. Bu durağın sırrı: sporun adı ile maçın sonucunu birlikte anlatmak.",
 "kapsar": ["u2k1", "u2k2"],
 "hatirla": [
  {"konu": "u2k1", "maddeler": ["Sporlar: {{swimming}}, {{cycling}}, {{skiing}}, {{ice skating}}, {{doing judo}}.", "{{outdoor sport}} dışarıda, {{indoor sport}} kapalı alanda.", "{{equipment}}: sporun eşyaları. Tenis için {{racket}}, {{ball}}, {{net}}."]},
  {"konu": "u2k2", "maddeler": ["{{spectator}} seyirci, {{medal}} madalya, {{injury}} sakatlık.", "Eşit skor {{draw}}; rakibi yenmek {{beat}}.", "{{score}} skor; büyük başarı {{a great achievement}}."]}],
 "eskiSoru": 4, "oyunKavram": 10,
 "gruplar": [{"soru": "Sporun adı mı, maç kelimesi mi?", "kutular": [
   {"etiket": "Sporun adı", "uyeler": ["swimming", "cycling", "skiing", "doing judo"]},
   {"etiket": "Maç ve yarışma", "uyeler": ["spectator", "medal", "draw", "score"]}]}],
 "sorular": [
  Q("Dinle. Hangi cümleyi duydun?", ["Spectators are cheering for Roger.", "Spectators are cycling with Roger.", "Players are cheering for Roger."], 0,
    "Cümlenin başında maçı izleyenler var. Yavaş dinle düğmesini dene.", "Duyduğun cümle {{Spectators are cheering for Roger.}}: Seyirciler Roger'a tezahürat yapıyor. (s. 32)",
    dinle="Spectators are cheering for Roger.", kaynak=[{"konu": "u2k2", "kavram": "spectator"}, {"konu": "u2k2", "kavram": "score"}]),
  Q("Dinle. Hangi cümleyi duydun?", ["Sheila won the gold medal in swimming.", "Sheila won the gold medal in skiing.", "Sheila lost the medal in swimming."], 0,
    "İki şeye dikkat et: kazandı mı, kaybetti mi? Hangi sporda?", "Duyduğun cümle {{Sheila won the gold medal in swimming.}} Yüzmede altın madalya kazandı. (s. 42)",
    dinle="Sheila won the gold medal in swimming.", kaynak=[{"konu": "u2k2", "kavram": "medal"}, {"konu": "u2k1", "kavram": "swimming"}]),
  Q("{{Burcu is a professional cyclist. She won a race last year. It was a great ___.}}", ["injury", "achievement", "equipment"], 1,
    "Yarış kazanmak iyi bir sonuç. İyi sonuca ne deniyordu?", "Yarış kazanmak büyük bir başarıdır: {{achievement}}. (s. 40, s. 44)",
    kaynak=[{"konu": "u2k2", "kavram": "achievement"}, {"konu": "u2k1", "kavram": "cycling"}]),
  Q("{{If you want to go skiing, you need special ___.}}", ["spectators", "medals", "equipment"], 2,
    "Kayak yapmak için kayak gibi eşyalar gerekir. Spor eşyasına ne deniyordu?", "Bir sporu yapmak için gereken eşyalar {{equipment}}tır. (s. 43)",
    kaynak=[{"konu": "u2k1", "kavram": "equipment"}, {"konu": "u2k1", "kavram": "skiing"}]),
  Q("Hangisi doğru?", ["Our team draw the opponent team 2-0.", "Our team beat the opponent team 2-0.", "Our team lose the opponent team 2-0."], 1,
    "2-0 eşit bir skor mu? Takımımız ne yaptı?", "2-0 eşit değil; takımımız kazandı. Rakibi yenmek {{beat}}: {{Our school team beat the opponent team 2-0.}} (s. 40)",
    kaynak=[{"konu": "u2k2", "kavram": "beat"}, {"konu": "u2k2", "kavram": "draw"}],
    yardim={"adimlar": ["Skor 2-0: iki taraf eşit mi?", "Eşit değilse {{draw}} olmaz.", "Takımımız 2 gol attı. Rakibi ne yaptı: yendi mi, kaybetti mi?"]}),
  Q("Hangisi doğru yazılmış?", ["I like going swimming and doing judo.", "I like doing swimming and going judo.", "I like playing swimming and going judo."], 0,
    "Yüzme hangi fiille, judo hangi fiille kullanılıyordu?", "Kitapta {{go swimming}} (s. 29) ve {{doing judo}} (s. 34) geçer.",
    kaynak=[{"konu": "u2k1", "kavram": "swimming"}, {"konu": "u2k1", "kavram": "doing judo"}]),
  Q("{{It is a team game. Five players in each team play the game. The final score is 63-64.}} Bu metne göre hangisi doğru?",
    ["Bu bir bireysel spor.", "Maç berabere.", "Takımlardan biri bir sayı farkla önde."], 2,
    "Skor eşit mi? 63 ile 64'ü karşılaştır.", "63-64 eşit değil, yani berabere değil. Takım oyunu olduğu için bireysel de değil; bir takım bir sayı önde. (s. 32)",
    kaynak=[{"konu": "u2k2", "kavram": "score"}, {"konu": "u2k2", "kavram": "draw"}],
    yardim={"adimlar": ["İlk cümle: {{team game}} takım oyunu. Bireysel mi?", "Skor 63-64. İki sayı eşit mi?", "Eşit değilse berabere olmaz. Kalan şıkka bak."]}),
 ]
}


# =================== u2k3 ===================
def takvim(dolu, renk, ek=""):
    """Haftanın 7 günü: dolu gün sayısı kadar tik. dolu=0 ise kırmızı çarpı."""
    s = "<rect x='12' y='26' width='96' height='16' rx='5' fill='" + renk + "'/>"
    s += "<path d='M30 20v10M90 20v10' stroke='#e9ecf5' stroke-width='4' stroke-linecap='round'/>"
    gun = [1, 1, 1, 1, 1, 1, 1]
    sira = {7: [0, 1, 2, 3, 4, 5, 6], 6: [0, 1, 2, 3, 4, 5], 5: [0, 1, 2, 4, 5], 3: [1, 3, 5], 2: [1, 4], 0: []}[dolu]
    for i in range(7):
        x = 13 + i * 13.5
        s += f"<rect x='{x:.1f}' y='50' width='11' height='14' rx='3' fill='#2b3556'/>"
        if i in sira:
            s += f"<path d='M{x+2:.1f} 57l3 3 5-6' stroke='#3cc47c' stroke-width='2.4' fill='none' stroke-linecap='round' stroke-linejoin='round'/>"
    return svg(s + ek)
def olcek(oran, renk):
    w = int(92 * oran)
    return (f"<rect x='14' y='80' width='92' height='12' rx='6' fill='#2b3556'/>"
            + (f"<rect x='14' y='80' width='{max(w, 12)}' height='12' rx='6' fill='{renk}'/>" if w else ""))
S_ALW = takvim(7, "#3cc47c", olcek(1, "#3cc47c"))
S_USU = takvim(6, "#4fb3ff", olcek(.8, "#4fb3ff"))
S_OFT = takvim(5, "#f2c14e", olcek(.62, "#f2c14e"))
S_SOM = takvim(3, "#ff7a33", olcek(.4, "#ff7a33"))
S_NEV = takvim(0, "#e0464e", olcek(0, "#e0464e") + "<circle cx='60' cy='104' r='0'/>"
               "<path d='M48 47l24 20M72 47l-24 20' stroke='#e0464e' stroke-width='5' stroke-linecap='round'/>")
S_HOW = svg("<circle cx='48' cy='62' r='32' fill='#f4f4f8'/><circle cx='48' cy='62' r='27' fill='none' stroke='#5a6280' stroke-width='3'/>"
  "<path d='M48 62V44M48 62l12 8' stroke='#1b2340' stroke-width='4' stroke-linecap='round'/>"
  "<path d='M86 38q0-12 12-12t12 12q0 8-12 12v8' stroke='#f2c14e' stroke-width='6' fill='none' stroke-linecap='round'/><circle cx='98' cy='72' r='4' fill='#f2c14e'/>"
  "<path d='M20 104h56' stroke='#4fb3ff' stroke-width='5' stroke-linecap='round'/>")
S_TWICE = takvim(2, "#b46be0", "<text x='60' y='100' font-size='26' font-family='sans-serif' font-weight='700' text-anchor='middle' fill='#b46be0'>2 ×</text>")

def F(*b): return [{"t": t, "r": r, **({"alt": a} if a else {})} for t, r, a in b]
u2k3 = {
 "id": "u2k3", "unite": U, "baslik": "Rutinler ve Sıklık (always … never)", "sayfalar": "s. 27–44",
 "giris": "Bu konuda bir işi ne sıklıkla yaptığımızı anlatacağız: her zaman, genellikle, sık sık, bazen, asla. Bu kelimeler cümlede fiilden önce gelir. Bu konunun sorusu: {{How often do you train?}} Yani: Ne sıklıkla antrenman yaparsın?",
 "kavramlar": [
  K("always", "#3cc47c", S_ALW, "Her zaman demektir. Kitaptaki tabloda %100: her gün, hiç atlamadan.", "her zaman",
    Q("{{I always wake up early.}} Bu kişi ne sıklıkla erken kalkıyor?", ["Her zaman", "Bazen", "Asla"], 0,
      "Kartta takvimin bütün günleri işaretliydi.", "{{always}} her zaman demektir (%100). (s. 31, s. 38)"),
    ek="Kelime fiilden önce gelir: {{I always wake up early.}}",
    ornek="I always wake up early and have a big breakfast.", ornekTr="Her zaman erken kalkar ve büyük bir kahvaltı yaparım. (s. 31)"),
  K("usually", "#4fb3ff", S_USU, "Genellikle demektir. Kitaptaki tabloda %80: çoğu zaman.", "genellikle",
    Q("{{I usually eat meat, fruit and vegetables.}} {{usually}} ne demek?", ["Hiçbir zaman", "Genellikle", "Bazen"], 1,
      "Kartta takvimin neredeyse bütün günleri işaretliydi.", "{{usually}} genellikle demektir (%80). (s. 31, s. 38)"),
    ek="{{always}} kadar değil ama çoğu zaman.",
    ornek="I usually eat meat, fruit and vegetables.", ornekTr="Genellikle et, meyve ve sebze yerim. (s. 31)"),
  K("often", "#f2c14e", S_OFT, "Sık sık demektir. {{usually}} kadar değil ama {{sometimes}}'dan daha sık.", "sık sık",
    Q("{{I often walk to school.}} Bu kişi okula nasıl gidiyor?", ["Hiç yürümüyor", "Bir kez yürüdü", "Sık sık yürüyor"], 2,
      "Kartta {{often}} kelimesinin anlamı vardı.", "{{often}} sık sık demektir: okula sık sık yürür. (s. 36)"),
    ek="Mark'ın blogunda: {{I often ride my bike.}} Sık sık bisiklete binerim.",
    ornek="I often walk to school.", ornekTr="Okula sık sık yürürüm. (s. 36)"),
  K("sometimes", "#ff7a33", S_SOM, "Bazen demektir. Kitaptaki tabloda %40: arada bir.", "bazen",
    Q("{{We sometimes run in the park.}} Ne sıklıkla koşuyorlar?", ["Bazen", "Her zaman", "Asla"], 0,
      "Kartta takvimde yalnız birkaç gün işaretliydi.", "{{sometimes}} bazen demektir (%40). (s. 35, s. 38)"),
    ek="Daha da seyrek: {{seldom}} (%20), nadiren.",
    ornek="We sometimes run in the park or do exercises in the gym.", ornekTr="Bazen parkta koşarız ya da spor salonunda egzersiz yaparız. (s. 35)"),
  K("never", "#e0464e", S_NEV, "Asla, hiçbir zaman demektir. Kitaptaki tabloda %0.", "asla, hiç",
    Q("{{Terry never eats junk food.}} Terry abur cubur yer mi?", ["Her gün yer", "Hiç yemez", "Bazen yer"], 1,
      "Kartta takvimin üstünde kırmızı çarpı vardı.", "{{never}} asla demektir: hiç yemez (%0). (s. 39)"),
    ek="Cümle olumlu görünür ama anlamı olumsuzdur: {{I never go on a heavy diet.}}",
    ornek="I never go on a heavy diet.", ornekTr="Asla ağır bir diyet yapmam. (s. 36)"),
  K("How often …?", "#4f8ff7", S_HOW, "Ne sıklıkla? demektir. Bir işin ne kadar sık yapıldığını sorar.", "ne sıklıkla",
    Q("{{How often do you train?}} sorusuna hangisi cevap olur?", ["At the gym.", "Six days a week.", "With my coach."], 1,
      "Soru yeri ya da kişiyi değil, sıklığı soruyor.", "{{How often}} sıklığı sorar: {{Six days a week.}} Haftada altı gün. (s. 31)"),
    ek="Cevap ya sıklık kelimesiyle ({{always}}, {{never}}) ya da bir süreyle verilir ({{twice a week}}).",
    ornek="How often do you train?", ornekTr="Ne sıklıkla antrenman yaparsın? (s. 31)"),
  K("twice a week", "#b46be0", S_TWICE, "Haftada iki kez demektir. {{twice}} iki kez, {{a week}} haftada.", "haftada iki kez",
    Q("{{I work out at the gym twice a week.}} Haftada kaç kez spor salonuna gidiyor?", ["Bir kez", "Üç kez", "İki kez"], 2,
      "{{twice}} kelimesinin anlamını hatırla.", "{{twice a week}} haftada iki kez demektir. (s. 31)"),
    ek="Bir kez {{once}}, üç kez {{three times}}. Her gün {{every day}}.",
    ornek="I work out at the gym twice a week, and I swim every day.", ornekTr="Haftada iki kez spor salonunda çalışırım ve her gün yüzerim. (s. 31)"),
 ],
 "gruplar": [{"soru": "Bu kelime çoğu zaman mı, yoksa ara sıra ya da hiç mi?", "kutular": [
   {"etiket": "Çoğu zaman", "uyeler": ["always", "usually", "often"]},
   {"etiket": "Ara sıra ya da hiç", "uyeler": ["sometimes", "never"]}]}],
 "biliyorMusun": [
   "Kitaptaki tabloda sıklık yüzdeyle gösteriliyor: {{always}} %100, {{usually}} %80, {{sometimes}} %40, {{seldom}} %20, {{never}} %0. (s. 38)",
   "Yüzücü Laura günde dört saat, haftada altı gün antrenman yapıyor. (s. 41)"],
 "akildaKalsin": [
   "Sıralama: {{always}} > {{usually}} > {{often}} > {{sometimes}} > {{never}}.",
   "Sıklık kelimesi fiilden önce gelir: {{I always wake up early.}}",
   "Sıklığı sormak için: {{How often do you train?}}",
   "Kaç kez: {{once}} bir kez, {{twice}} iki kez, {{three times}} üç kez + {{a week}} haftada.",
   "{{every day}} her gün demektir ve cümlenin sonuna gelir: {{I swim every day.}}"],
 "merakKutusu": [
   {"soru": "{{always}} cümlenin neresine gelir?", "cevap": "Fiilin hemen önüne: {{I always wake up early.}} {{I usually eat meat.}} (s. 31)"},
   {"soru": "{{every day}} neden sona geliyor?", "cevap": "Çünkü bu bir kelime değil, kelime grubu. Kitapta: {{I swim every day.}} (s. 31) Aynı şekilde {{twice a week}} de sona gelir."},
   {"soru": "{{often}} ile {{usually}} hangisi daha sık?", "cevap": "{{usually}} daha sık. Sıralama: {{always}}, {{usually}}, {{often}}, {{sometimes}}, {{never}}."},
   {"soru": "{{seldom}} ne demek?", "cevap": "Nadiren demektir. Kitaptaki tabloda %20; {{sometimes}} ile {{never}} arasında. (s. 38)"},
   {"soru": "Bir kez, iki kez nasıl söylenir?", "cevap": "Bir kez {{once}}, iki kez {{twice}}, üç kez {{three times}}. Kitapta: {{Three times a week.}} (s. 30)"}],
 "dusunVeYaz": [{"soru": "Haftalık rutinini İngilizce iki cümleyle anlat. Bir cümlede {{always}} ya da {{usually}}, diğerinde {{a week}} kullan.",
   "ornekCevap": "I always get up early on weekdays. I play basketball twice a week.", "anahtarlar": ["always", "usually", "week"]}],
 "sorular": [
  Q("Dinle. Hangi kelimeyi duydun?", ["often", "never", "always"], 2, "Yüzde yüz anlamına gelen kelimeyi duydun. Yavaş dinle düğmesini dene.",
    "Duyduğun kelime {{always}}: her zaman. (s. 38)", dinle="always", kavram="always"),
  Q("Dinle. Hangi cümleyi duydun?", ["I never go on a heavy diet.", "I often go on a heavy diet.", "I never go on a special diet."], 0,
    "İki şeye dikkat et: sıklık kelimesi ve diyetin türü.", "Duyduğun cümle {{I never go on a heavy diet.}}: Asla ağır bir diyet yapmam. (s. 36)",
    dinle="I never go on a heavy diet.", kavram="never"),
  Q("Dinle. Hangi cümleyi duydun?", ["I swim twice a week.", "I work out at the gym twice a week.", "I work out at the gym once a week."], 1,
    "Nerede ve kaç kez? İkisini birlikte dinle.", "Duyduğun cümle {{I work out at the gym twice a week.}} (s. 31)",
    dinle="I work out at the gym twice a week.", kavram="twice a week"),
  Q("Hangisi doğru yazılmış?", ["I wake up always early.", "Always I wake up early.", "I always wake up early."], 2,
    "Sıklık kelimesi fiilin neresine geliyordu?", "Sıklık kelimesi fiilden önce gelir: {{I always wake up early.}} (s. 31)", kavram="always",
    yardim={"adimlar": ["Cümlenin fiili hangisi? {{wake up}}.", "Sıklık kelimesi fiilin önüne gelir.", "{{always}} hangi şıkta {{wake up}}'tan hemen önce?"]}),
  Q("{{How often do you swim?}} Hangisi uygun cevap?", ["In the pool.", "Once or twice in a week.", "Because it is fun."], 1,
    "{{How often}} neyi sorar: yeri mi, sıklığı mı, nedeni mi?", "{{How often}} sıklığı sorar: {{Once or twice in a week.}} (s. 39)", kavram="How often …?"),
  Q("Robert her gün koşuyor. Hangisi doğru?", ["Robert always runs.", "Robert never runs.", "Robert sometimes runs."], 0,
    "Her gün yapılan iş: yüzde kaç?", "Her gün = her zaman: {{Robert always runs.}} (s. 33)", kavram="always"),
  Q("{{I usually have my breakfast with my parents.}} {{usually}} yerine anlamı en yakın olan hangisi?", ["never", "seldom", "always"], 2,
    "{{usually}} %80. Hangisi ona en yakın?", "{{usually}} %80, {{always}} %100; en yakını {{always}}. {{never}} %0, {{seldom}} %20. (s. 36, s. 38)", kavram="usually",
    yardim={"adimlar": ["{{usually}} tabloda yüzde kaç? %80.", "Şıkların yüzdelerini düşün: {{never}} %0, {{seldom}} %20.", "Kalan şık %80'e en yakın mı?"]}),
  Q("{{I often ride my bike.}} Bu kişi bisiklete ne sıklıkla biniyor?", ["Hiç binmiyor", "Sık sık biniyor", "Yalnız bir kez bindi"], 1,
    "{{often}} kartını hatırla.", "{{often}} sık sık demektir. (s. 36)", kavram="often"),
  Q("{{We ___ run in the park.}} Arada bir koşuyorlar. Boşluğa ne gelir?", ["sometimes", "always", "never"], 0,
    "Arada bir = %40. Hangi kelimeydi?", "Arada bir {{sometimes}}tır: {{We sometimes run in the park.}} (s. 35)", kavram="sometimes"),
  Q("{{Terry never eats junk food, so ___.}} Hangisi uygun?", ["he's very unhealthy", "he's very healthy", "he eats burgers every day"], 1,
    "Abur cubur yemeyen biri sağlıklı mı olur?", "{{Terry never eats junk food, so he's very healthy.}} Hiç abur cubur yemez, bu yüzden çok sağlıklıdır. (s. 39)", kavram="never"),
 ],
 "kelimeler": [
  {"en": "seldom", "tr": "nadiren"},
  {"en": "once a week", "tr": "haftada bir kez", "ornek": "Once or twice in a week.", "ornekTr": "Haftada bir ya da iki kez. (s. 39)"},
  {"en": "three times a week", "tr": "haftada üç kez", "ornek": "Three times a week.", "ornekTr": "Haftada üç kez. (s. 30)"},
  {"en": "every day", "tr": "her gün", "ornek": "I get up early every day.", "ornekTr": "Her gün erken kalkarım. (s. 41)"},
  {"en": "get up early", "tr": "erken kalkmak"},
  {"en": "eat healthy food", "tr": "sağlıklı yiyecekler yemek", "ornek": "I always eat healthy food, never drink energy drinks.", "ornekTr": "Her zaman sağlıklı yiyecekler yerim, asla enerji içeceği içmem. (s. 41)"},
  {"en": "junk food", "tr": "abur cubur"},
  {"en": "go on a diet", "tr": "diyet yapmak", "ornek": "Do you often go on a diet?", "ornekTr": "Sık sık diyet yapar mısın? (s. 39)"},
  {"en": "keep fit", "tr": "formda kalmak", "ornek": "I always do exercises to keep fit.", "ornekTr": "Formda kalmak için her zaman egzersiz yaparım. (s. 36)"},
  {"en": "routine", "tr": "rutin, her zamanki düzen"},
 ],
 "cumleler": [
  {"en": "I always wake up early.", "tr": "Her zaman erken kalkarım. (s. 31)"},
  {"en": "I train six days a week.", "tr": "Haftada altı gün antrenman yaparım. (s. 31)"},
  {"en": "I swim every day.", "tr": "Her gün yüzerim. (s. 31)"},
  {"en": "I often walk to school.", "tr": "Okula sık sık yürürüm. (s. 36)"},
  {"en": "I never go on a heavy diet.", "tr": "Asla ağır bir diyet yapmam. (s. 36)"},
  {"en": "How often do you train?", "tr": "Ne sıklıkla antrenman yaparsın? (s. 31)"},
 ],
 "hatalar": [
  {"cumle": "Terry always eats junk food, so he's very healthy.", "yanlis": "always", "secenekler": ["never", "usually", "often"], "dogru": 0,
   "tr": "Terry asla abur cubur yemez, bu yüzden çok sağlıklıdır.", "aciklama": "Sağlıklıysa abur cuburu hiç yemez: {{never}}. (s. 39)"},
  {"cumle": "How many do you swim? Once or twice a week.", "yanlis": "many", "secenekler": ["much", "often", "long"], "dogru": 1,
   "tr": "Ne sıklıkla yüzersin? Haftada bir ya da iki kez.", "aciklama": "Sıklığı sormak için {{How often}}. (s. 39)"},
  {"cumle": "Katie always wake up early when she goes to the gym.", "yanlis": "wake", "secenekler": ["woke", "waking", "wakes"], "dogru": 2,
   "tr": "Katie spor salonuna gittiğinde her zaman erken kalkar.", "aciklama": "{{Katie}} (o) ile fiil {{-s}} alır: {{wakes up}}. (s. 39)"},
  {"cumle": "I work out at the gym two a week.", "yanlis": "two", "secenekler": ["twice", "second", "double"], "dogru": 0,
   "tr": "Haftada iki kez spor salonunda çalışırım.", "aciklama": "İki kez {{twice}}: {{twice a week}}. (s. 31)"},
  {"cumle": "I always do exercises to keep fat.", "yanlis": "fat", "secenekler": ["fast", "fit", "thin"], "dogru": 1,
   "tr": "Formda kalmak için her zaman egzersiz yaparım.", "aciklama": "Formda kalmak {{keep fit}}. {{fat}} şişman demek. (s. 36)"},
 ],
 "okuma": {
  "baslik": "An interview with Emma", "sayfa": "s. 31",
  "sozluk": {"Olympic": "Olimpik, Olimpiyat", "World Championship": "Dünya Şampiyonası", "start the day": "güne başlamak", "wake up early": "erken uyanmak",
             "big breakfast": "büyük kahvaltı", "spend most of the day": "günün çoğunu geçirmek", "rest": "dinlenmek", "train": "antrenman yapmak",
             "work out": "spor yapmak", "special diet": "özel diyet", "healthy food": "sağlıklı yiyecek", "give energy": "enerji vermek",
             "plans for the future": "gelecek planları", "gold medals": "altın madalyalar", "Good luck": "İyi şanslar"},
  "bolumler": [
   {"baslik": "Emma'nın günü", "cumleler": [
     {"en": "Interviewer: Today I'm talking to Emma Robins, the Olympic and World Championship swimmer.", "tr": "Muhabir: Bugün Olimpiyat ve Dünya Şampiyonası yüzücüsü Emma Robins ile konuşuyorum."},
     {"en": "Interviewer: How do you start the day?", "tr": "Muhabir: Güne nasıl başlıyorsun?"},
     {"en": "Emma: I always wake up early and have a big breakfast.", "tr": "Emma: Her zaman erken uyanır ve büyük bir kahvaltı yaparım."},
     {"en": "Then, I go to the gym and the swimming pool to train.", "tr": "Sonra antrenman yapmak için spor salonuna ve yüzme havuzuna giderim."},
     {"en": "I spend most of the day by doing exercises.", "tr": "Günün çoğunu egzersiz yaparak geçiririm."},
     {"en": "In the evenings, I watch TV, listen to music and rest.", "tr": "Akşamları televizyon izler, müzik dinler ve dinlenirim."}],
    "sorular": [
     Q("Emma her sabah ne yapar?", ["Geç kalkar", "Erken uyanır ve büyük kahvaltı yapar", "Hemen yüzmeye gider"], 1,
       "{{I always wake up early}} cümlesini bul.", "{{I always wake up early and have a big breakfast.}} Her zaman erken uyanır, büyük kahvaltı yapar."),
     Q("Emma akşamları ne yapar?", ["Televizyon izler, müzik dinler, dinlenir", "Spor salonuna gider", "Arkadaşlarıyla yüzer"], 0,
       "{{In the evenings}} ile başlayan cümleye bak.", "{{In the evenings, I watch TV, listen to music and rest.}}")]},
   {"baslik": "Antrenman ve diyet", "cumleler": [
     {"en": "Interviewer: How often do you train?", "tr": "Muhabir: Ne sıklıkla antrenman yapıyorsun?"},
     {"en": "Emma: I train six days a week.", "tr": "Emma: Haftada altı gün antrenman yaparım."},
     {"en": "I work out at the gym twice a week, and I swim every day.", "tr": "Haftada iki kez spor salonunda çalışırım ve her gün yüzerim."},
     {"en": "Interviewer: Do you go on a special diet?", "tr": "Muhabir: Özel bir diyet yapıyor musun?"},
     {"en": "Emma: Of course, I do. I eat healthy food.", "tr": "Emma: Elbette. Sağlıklı yiyecekler yerim."},
     {"en": "I usually eat meat, fruit and vegetables.", "tr": "Genellikle et, meyve ve sebze yerim."},
     {"en": "They make me strong and give energy.", "tr": "Beni güçlü yapar ve enerji verirler."},
     {"en": "Interviewer: What are your plans for the future?", "tr": "Muhabir: Gelecek planların neler?"},
     {"en": "Emma: I'm planning to be the first woman swimmer with six gold medals by racing at six Olympics.", "tr": "Emma: Altı Olimpiyatta yarışarak altı altın madalyalı ilk kadın yüzücü olmayı planlıyorum."},
     {"en": "Interviewer: Good luck, Emma. I'm sure you can do it.", "tr": "Muhabir: İyi şanslar Emma. Eminim yapabilirsin."}],
    "sorular": [
     Q("Emma ne sıklıkla spor salonuna gidiyor?", ["Her gün", "Haftada altı gün", "Haftada iki kez"], 2,
       "{{at the gym}} kalıbının olduğu cümleye bak.", "{{I work out at the gym twice a week.}} Haftada iki kez. Yüzmeyi ise her gün yapar."),
     Q("Emma genellikle ne yer?", ["Abur cubur", "Et, meyve ve sebze", "Yalnız meyve"], 1,
       "{{I usually eat}} cümlesini bul.", "{{I usually eat meat, fruit and vegetables.}}")]}]}
}
for k in u2k3["kavramlar"]:
    k["formul"] = {
      "always": [F(("I", "ozne", None), ("always", "kelime", "%100"), ("wake up early", "fiil", "fiil"))],
      "usually": [F(("I", "ozne", None), ("usually", "kelime", "%80"), ("eat meat", "fiil", "fiil"))],
      "often": [F(("I", "ozne", None), ("often", "kelime", "sık sık"), ("walk to school", "fiil", "fiil"))],
      "sometimes": [F(("We", "ozne", None), ("sometimes", "kelime", "%40"), ("run in the park", "fiil", "fiil"))],
      "never": [F(("I", "ozne", None), ("never", "olumsuz", "%0"), ("go on a heavy diet", "fiil", "fiil"))],
      "How often …?": [F(("How often", "kelime", "ne sıklıkla"), ("do", "yard", None), ("you", "ozne", None), ("train?", "fiil", "fiil")),
                       F(("How often", "kelime", "ne sıklıkla"), ("does", "yard", "o için"), ("she", "ozne", None), ("swim?", "fiil", "fiil"))],
      "twice a week": [F(("I", "ozne", None), ("work out", "fiil", "fiil"), ("twice a week", "kelime", "haftada iki kez"))],
    }[k["ad"]]

# =================== u2t2 ===================
u2t2 = {
 "id": "u2t2", "tur": "tarama", "unite": U, "baslik": "Ünite 2 Sonu Taraması", "sayfalar": "Konu 1–3 · s. 27–44",
 "giris": "Ünite 2 bitti! Şimdi bütün üniteye kısaca bakalım. Önce özetleri oku ve kartlara dokun. Sonra tarama testini çöz. Not yok; neyi iyi bildiğini ve neye tekrar bakacağını bulacağız.",
 "buyukResim": "Bir sporcuyu üç yönden anlatabiliyoruz: hangi sporu yapıyor, ne sıklıkla antrenman yapıyor ve maçlarda ne oluyor. Kitaptaki Emma ve Laura röportajları üçünü birlikte kullanıyor: yüzme, haftada altı gün, altın madalya.",
 "kapsar": ["u2k1", "u2k2", "u2k3"],
 "hatirla": [
  {"konu": "u2k1", "maddeler": ["Sporlar: {{swimming}}, {{cycling}}, {{skiing}}, {{ice skating}}, {{doing judo}}.", "{{go swimming}} ama {{doing judo}}.", "{{outdoor sport}} dışarıda; {{equipment}} sporun eşyaları."]},
  {"konu": "u2k2", "maddeler": ["{{spectator}} seyirci, {{medal}} madalya, {{injury}} sakatlık.", "Eşit skor {{draw}}; rakibi yenmek {{beat}}.", "{{score}} skor; {{achievement}} başarı."]},
  {"konu": "u2k3", "maddeler": ["{{always}} > {{usually}} > {{often}} > {{sometimes}} > {{never}}.", "Sıklık kelimesi fiilden önce: {{I always wake up early.}}", "{{How often …?}} sorusuna cevap: {{twice a week}}, {{every day}}."]}],
 "eskiSoru": 4, "oyunKavram": 10,
 "gruplar": [{"soru": "Bu kelime hangi konudan?", "kutular": [
   {"etiket": "Sporun adı", "uyeler": ["swimming", "cycling", "skiing"]},
   {"etiket": "Maç ve yarışma", "uyeler": ["medal", "draw", "spectator"]},
   {"etiket": "Ne sıklıkla?", "uyeler": ["always", "sometimes", "never"]}]}],
 "sorular": [
  Q("Dinle. Hangi cümleyi duydun?", ["I swim every day.", "I ski every day.", "I swim every week."], 0,
    "Hangi spor ve ne sıklıkla? İkisini birlikte dinle.", "Duyduğun cümle {{I swim every day.}}: Her gün yüzerim. (s. 31)",
    dinle="I swim every day.", kaynak=[{"konu": "u2k1", "kavram": "swimming"}, {"konu": "u2k3", "kavram": "always"}]),
  Q("Dinle. Hangi cümleyi duydun?", ["Our team never wins a medal.", "Our team often wins a medal.", "Our team often loses a match."], 1,
    "Sıklık kelimesine ve kazanma mı kaybetme mi olduğuna dikkat et.", "Duyduğun cümle {{Our team often wins a medal.}}: Takımımız sık sık madalya kazanır.",
    dinle="Our team often wins a medal.", kaynak=[{"konu": "u2k3", "kavram": "often"}, {"konu": "u2k2", "kavram": "medal"}]),
  Q("{{How often do you go cycling?}} Hangisi uygun cevap?", ["I like cycling.", "I go cycling in the park.", "I go cycling twice a week."], 2,
    "{{How often}} sıklığı sorar. Hangi şık sıklık söylüyor?", "Sıklık sorusuna sıklıkla cevap verilir: {{twice a week}}. (s. 31)",
    kaynak=[{"konu": "u2k3", "kavram": "How often …?"}, {"konu": "u2k1", "kavram": "cycling"}]),
  Q("Laura: {{I train four hours in a day and six days in a week.}} Hangisi doğru?",
    ["Laura never trains.", "Laura trains once a week.", "Laura usually trains."], 2,
    "Haftada altı gün çok mu, az mı? Yüzdesi {{usually}}'ye mi yakın?", "Haftada altı gün antrenman çoğu zaman demektir: {{usually}}. (s. 41)",
    kaynak=[{"konu": "u2k3", "kavram": "usually"}, {"konu": "u2k1", "kavram": "swimming"}],
    yardim={"adimlar": ["Bir haftada kaç gün var? Yedi.", "Laura yedi günün altısında antrenman yapıyor.", "Bu, çoğu zaman mı, yoksa hiç mi?"]}),
  Q("Hangisi doğru yazılmış?", ["Always we beat the opponent team.", "We always beat the opponent team.", "We beat always the opponent team."], 1,
    "Sıklık kelimesi fiilin önüne gelir. Fiil {{beat}}.", "{{always}} fiilin önüne gelir: {{We always beat the opponent team.}}",
    kaynak=[{"konu": "u2k3", "kavram": "always"}, {"konu": "u2k2", "kavram": "beat"}],
    yardim={"adimlar": ["Cümlenin fiili hangisi? {{beat}} yenmek.", "Sıklık kelimesi fiilin hemen önüne gelir.", "Hangi şıkta {{always}}, {{beat}}'ten hemen önce?"]}),
  Q("{{Burcu is a professional cyclist. That's why she trains every day.}} Burcu ne sıklıkla antrenman yapar?", ["Her gün, her zaman", "Asla", "Haftada bir kez"], 0,
    "{{every day}} ne demekti?", "{{every day}} her gün demektir; her gün yapılan iş {{always}} ile anlatılır. (s. 44)",
    kaynak=[{"konu": "u2k1", "kavram": "cycling"}, {"konu": "u2k3", "kavram": "always"}]),
  Q("Emma: {{I'm planning to be the first woman swimmer with six gold medals.}} Emma'nın hedefi ne?", ["Altı Olimpiyat altın madalyası", "Haftada altı gün yüzmek", "Bir maçta berabere kalmak"], 0,
    "{{gold medals}} kelimesinden önceki sayıya ve cümlenin konusuna bak.", "Emma altı altın madalyalı ilk kadın yüzücü olmak istiyor. (s. 31)",
    kaynak=[{"konu": "u2k2", "kavram": "medal"}, {"konu": "u2k1", "kavram": "swimming"}]),
 ]
}

for d in (u2k1, u2k2, u2t1, u2k3, u2t2):
    with open(f"{KOK}/{d['id']}.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(d, ensure_ascii=False, indent=1))
print("yazıldı")
