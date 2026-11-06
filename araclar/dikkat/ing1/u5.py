# ing1 — Unit 5: Television (u5k1–u5k2). Kitap: kaynaklar/ing1/unite5.md. İngilizce farkları: u3.py başındaki not.
TEKRAR = {
"u5k1": [
 ("The {news|commercial|sitcom} informs people about the latest events happening all over the world.", "s. 87"),
 ("In a {sitcom|documentary|commercial}, a group of people usually appear in funny situations in every episode.", "s. 87"),
 ("In a {reality show|commercial|quiz show}, you can follow the lives of real people.", "s. 87"),
 ("Companies try to sell their products by introducing them in very short films. These are {commercials|documentaries|quiz shows}.", "s. 87"),
 ("I could answer only five questions out of ten. It was a difficult {quiz show|soap opera|commercial}.", "s. 87"),
 ("A {soap opera|documentary|quiz show} is a kind of TV show. You can watch it daytime. It is usually melodramatic.", "s. 87"),
 ("I watched an interesting {documentary|commercial|soap opera} about space.", "s. 89"),
],
"u5k2": [
 ("I prefer {watching|watch|watches} the news to the discussion programmes.", "s. 93"),
 ("I prefer sitcoms {to|than|from} reality shows because they are funny.", "s. 84"),
 ("Tom {prefers|prefer|preferring} watching talk shows to reality shows.", "s. 94"),
 ("I never watch soap operas. They are {boring|amusing|educational}.", "s. 84"),
 ("I like documentaries and quiz shows. They are {educational|boring|silly}.", "s. 85"),
 ("My {favourite|boring|silly} TV programme is the news. To be honest, I never miss it.", "s. 84"),
 ("I find them boring. I prefer {amusing|boring|dull} programmes.", "s. 85"),
],
}

KISA = {
"u5k1": [
 {"soru": "En sevdiğin TV programı türü hangisi ve onu neden seviyorsun? İki İngilizce cümleyle yaz.",
  "tetik": ["hangisi"],
  "okut": ["en sevdiğin TV programı türünü ve onu neden sevdiğini yazmanı", "dün akşam ne izlediğini anlatmanı", "bütün TV programı türlerini sıralamanı"],
  "parcalar": [
   {"bas": "My favourite TV programme is", "ornek": "the news.", "havuz": ["the remote control.", "the TV set."], "k": ["news", "sitcom", "documentar", "quiz", "reality", "soap", "talk show", "series"]},
   {"bas": "I watch it because", "ornek": "I learn new things.", "havuz": ["it is on TV.", "my TV is big."], "k": ["learn", "funny", "amusing", "educational", "interesting", "laugh", "myself"]}],
  "kisa": "My favourite is the news because I learn new things.",
  "cevap": "My favourite TV programme is the news. I watch it because it is good to know what is going on in the world, and I learn new things.",
  "anahtarlar": [{"ad": "program türü (news, sitcom…)", "k": ["news", "sitcom", "documentar", "quiz", "reality", "soap", "talk show", "series"]},
                 {"ad": "sebep (I learn…, it is funny…)", "k": ["learn", "funny", "amusing", "educational", "interesting", "laugh", "myself"]}],
  "sayfa": "s. 84"}],
"u5k2": [
 {"soru": "Hangi programları neden tercih ettiğini iki İngilizce cümleyle yaz.",
  "tetik": ["Hangi programları"],
  "okut": ["hangi programları tercih ettiğini ve nedenini yazmanı", "hangi programları sevmediğini sıralamanı", "en sevdiğin kanalın adını yazmanı"],
  "parcalar": [
   {"bas": "I prefer", "ornek": "documentaries to soap operas.", "havuz": ["the remote control.", "on TV last night."], "k": ["documentar", "sitcom", "quiz", "news", "reality", "soap", "talk show", "series"]},
   {"bas": "I think they are", "ornek": "educational.", "havuz": ["on Channel 5.", "next to the TV set."], "k": ["educational", "amusing", "funny", "interesting", "fantastic", "exciting"]}],
  "kisa": "I prefer documentaries. They are educational.",
  "cevap": "I prefer documentaries to soap operas. I think documentaries are educational, and I learn a lot of things.",
  "anahtarlar": [{"ad": "prefer + program türü", "k": ["documentar", "sitcom", "quiz", "news", "reality", "soap", "talk show", "series"]},
                 {"ad": "sıfat (educational, amusing…)", "k": ["educational", "amusing", "funny", "interesting", "fantastic", "exciting"]}],
  "sayfa": "s. 90"}],
}

METINLI = {
"u5k1": [
 {"metin": ["Jim: {{What did you do last night?}}", "Kate: {{I watched an interesting documentary about space. What about you?}}",
            "Jim: {{My favourite sitcom was on. I watched it. It was very funny.}}"],
  "soru": "Metne göre Jim dün akşam ne izledi?", "bolge": ["Jim", "ne izledi"],
  "serit": "Jim'in dün akşam izlediği program", "kanit": [2],
  "secenekler": ["his favourite sitcom", "a documentary about space", "the news"], "dogru": 0, "tuzak": [1],
  "ipucu": "Soru Kate'i değil, Jim'i soruyor.", "kanitIpucu": "Jim'in cevap verdiği cümle hangisi?",
  "aciklama": "“My favourite sitcom was on. I watched it.” Jim en sevdiği komedi dizisini izledi. Uzay belgeselini Kate izledi (s. 89).", "kavram": "sitcom"},
 {"metin": ["{{Hello! I'm Samuel. I watch TV almost every day.}}", "{{After school, I like to watch a few episodes of my favourite sitcom.}}",
            "{{On Mondays, I watch a reality show about cooking, where different chefs compete.}}",
            "{{In the evenings, I usually watch a documentary on animals or space.}}",
            "{{I find these shows very interesting because I learn a lot of new things.}}",
            "{{Sometimes, I watch the news to see what's happening in the world.}}"],
  "soru": "Metne göre Samuel akşamları genellikle ne izler?", "bolge": ["akşamları genellikle ne izler"],
  "serit": "Samuel'in akşamları izlediği program", "kanit": [3],
  "secenekler": ["a documentary on animals or space", "a reality show about cooking", "the news"], "dogru": 0, "tuzak": [1, 2],
  "ipucu": "“akşamları” İngilizcede “in the evenings” demek.", "kanitIpucu": "“In the evenings” hangi cümlede?",
  "aciklama": "“In the evenings, I usually watch a documentary on animals or space.” Yemek yarışmasını pazartesi, haberleri ara sıra izliyor (s. 98).", "kavram": "documentary"},
],
"u5k2": [
 {"metin": ["Jane: {{Well... I don't like talk shows. I think they are boring.}}", "Nora: {{Really? Which programmes do you prefer watching?}}",
            "Jane: {{I like documentaries and quiz shows. They are educational.}}"],
  "soru": "Metne göre Jane belgeselleri ve bilgi yarışmalarını neden seviyor?", "bolge": ["neden seviyor"],
  "serit": "Jane'in bu programları sevme sebebi", "kanit": [2],
  "secenekler": ["They are educational.", "They are boring.", "She doesn't like talk shows."], "dogru": 0, "tuzak": [1, 2],
  "ipucu": "“documentaries and quiz shows” cümlesinden sonra ne yazıyor?", "kanitIpucu": "“documentaries” hangi cümlede geçiyor?",
  "aciklama": "“I like documentaries and quiz shows. They are educational.” Eğitici oldukları için seviyor. Sıkıcı bulduğu programlar talk show'lar (s. 85).", "kavram": "educational"},
 {"metin": ["{{Did you watch the documentary last night that I recommended you?}}", "{{I did. It was fantastic.}}",
            "{{You know I prefer watching such educational TV programmes to those reality shows or soap operas.}}",
            "{{I also like quiz shows.}}", "{{Mum's watching a soap opera right now. I never watch them.}}",
            "{{I think they're silly and dull.}}"],
  "soru": "Metne göre Rob, gerçeklik şovları ve pembe diziler yerine hangi programları izlemeyi tercih ediyor?", "bolge": ["hangi programları izlemeyi tercih ediyor"],
  "serit": "Rob'un tercih ettiği programlar", "kanit": [2],
  "secenekler": ["educational TV programmes", "soap operas", "reality shows"], "dogru": 0, "tuzak": [1, 2],
  "ipucu": "“prefer X to Y”: tercih edilen X, “to”dan önce gelir.", "kanitIpucu": "“prefer” hangi cümlede geçiyor?",
  "aciklama": "“I prefer watching such educational TV programmes to those reality shows or soap operas.” “to”dan önceki eğitici programları tercih ediyor (s. 94).", "kavram": "prefer … to …"},
],
}
