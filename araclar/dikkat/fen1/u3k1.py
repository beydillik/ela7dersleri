TEKRAR = {"u3k1": [
 ("Sindirimde görevli yapı ve organların uyum içinde çalıştığı yapıya {sindirim sistemi|dolaşım sistemi|solunum sistemi} denir.", "s. 92"),
 ("Ağız yoluyla alınan besinlerin {kana geçebilecek|kemiğe dönüşebilecek|havaya karışabilecek} kadar küçük parçalara ayrılmasına sindirim denir.", "s. 92"),
 ("Besinlerin çiğneme ve kas hareketleriyle küçük parçalara ayrılması {fiziksel|kimyasal} sindirimdir; enzimler ve su yardımıyla yapı taşlarına ayrılması {kimyasal|fiziksel} sindirimdir.", "s. 92"),
 ("Fiziksel ve kimyasal sindirim {ağızda|midede|kalın bağırsakta} başlar. Yutakta ve yemek borusunda sindirim {gerçekleşmez|gerçekleşir}.", "s. 95"),
 ("Midede {proteinlerin|yağların|vitaminlerin} kimyasal sindirimi başlar. Besinlerin sindirimi {ince bağırsakta|kalın bağırsakta|yemek borusunda} tamamlanır.", "s. 95"),
 ("İnce bağırsağın iç yüzeyindeki {villuslar|tüyler|kıllar} temas yüzeyini artırarak emilimi hızlandırır. Kalın bağırsakta {su|protein|yağ} emilir.", "s. 95"),
 ("Karaciğerin salgıladığı {safra sıvısı|mide öz suyu|tükürük} yağların fiziksel sindirimine yardımcı olur. Pankreas öz suyu ise {kimyasal|fiziksel} sindirime yardımcı olur.", "s. 95"),
]}
KISA = {"u3k1": [
 {"soru": "Fiziksel sindirim ile kimyasal sindirim arasındaki farkı yazınız.",
  "tetik": ["farkı"],
  "okut": ["İki sindirimi ayrı ayrı tanımla (iki parça).", "Neden-sonuç yaz: “… çünkü …”", "Yalnız bir organın adını yaz."],
  "parcalar": [
   {"bas": "Fiziksel sindirim:", "ornek": "Besinler çiğneme ve kas hareketleriyle küçük parçalara ayrılır.", "havuz": ["Besinler enzimler ve su yardımıyla yapı taşlarına ayrılır.", "Besinler kana geçer."], "k": ["kas", "çiğne"]},
   {"bas": "Kimyasal sindirim:", "ornek": "Besinler enzimler ve su yardımıyla yapı taşlarına ayrılır.", "havuz": ["Besinler çiğnenerek parçalanır.", "Besinler kas hareketleriyle ezilir."], "k": ["enzim"]}],
  "kisa": "Fiziksel: çiğneme ve kas hareketleriyle parçalama. Kimyasal: enzimler ve suyla yapı taşlarına ayırma.",
  "cevap": "Fiziksel sindirimde besinler çiğneme, kas hareketleri ve özel sıvılarla küçük parçalara ayrılır. Kimyasal sindirimde ise besinler enzimler ve su yardımıyla kana geçebilecek kadar küçük yapı taşlarına ayrılır.",
  "anahtarlar": [{"ad": "fiziksel: çiğneme / kas hareketi", "k": ["kas", "çiğne"]}, {"ad": "kimyasal: enzim ve su", "k": ["enzim"]}],
  "sayfa": "s. 92"},
 {"soru": "İnce bağırsaktaki villuslar emilimi nasıl hızlandırır? Yazınız.",
  "tetik": ["nasıl"],
  "okut": ["Villusun yapısını ve bunun sonucunu yaz (iki parça).", "Benzerlik ve fark yaz.", "Evet ya da hayır yaz."],
  "parcalar": [
   {"bas": "Yapısı:", "ornek": "Girintili çıkıntılıdır, bu yüzden iç yüzeyi genişletir.", "havuz": ["Düz ve kaygandır, besini kaydırır.", "Mide öz suyu salgılar."], "k": ["yüzey", "genişlet"]},
   {"bas": "Sonucu:", "ornek": "Temas yüzeyi arttığı için besinler hızlı emilerek kana geçer.", "havuz": ["Besinler daha yavaş sindirilir.", "Su kalın bağırsağa geçer."], "k": ["emil"]}],
  "kisa": "Villuslar iç yüzeyi genişletir; temas yüzeyi artınca emilim hızlanır.",
  "cevap": "Villuslar girintili çıkıntılı yapısıyla ince bağırsağın iç yüzeyini genişletir ve temas yüzeyini artırır. Böylece sindirilen besinler hızlı emilerek kana geçer.",
  "anahtarlar": [{"ad": "iç yüzeyi genişletir", "k": ["yüzey", "genişlet"]}, {"ad": "emilim hızlanır", "k": ["emil"]}],
  "sayfa": "s. 95"},
]}
ELLE = {"Yutak ve yemek borusunda sindirim olur mu?": "olur mu"}
OKUT = {"u3k1": [
 ["fiziksel sindirimi ve kimyasal sindirimi ayrı ayrı anlatıp farkını göstermeni", "sindirimin hangi organda başladığını söylemeni", "kimyasal sindirimin neden önemli olduğunu anlatmanı"],
 ["villusların emilimi nasıl hızlandırdığını (yapısını ve sonucunu) anlatmanı", "villusların nerede bulunduğunu söylemeni", "emilimin ne demek olduğunu tanımlamanı"]]}
METINLI = {"u3k1": [
 {"metin": ["Mert öğle yemeğinde köfte yedi.", "Köftedeki proteinlerin kimyasal sindirimi midede başladı.", "Sindirimi tamamlanan besinler ince bağırsaktaki villuslar sayesinde kana geçti."],
  "soru": "Köftedeki besinler hangi yapılar sayesinde kana geçmiştir?", "bolge": ["hangi yapılar sayesinde kana geçmiştir"],
  "serit": "Besinlerin kana geçmesini sağlayan yapılar", "kanit": [2],
  "secenekler": ["İnce bağırsaktaki villuslar", "Midedeki enzimler", "Yemek borusundaki kaslar"], "dogru": 0, "tuzak": [1],
  "ipucu": "Metinde “kana geçti” ifadesinin geçtiği cümleyi bul.", "kanitIpucu": "“Kana geçti” ifadesi hangi cümlede?",
  "aciklama": "Sindirimi tamamlanan besinler, ince bağırsağın iç yüzeyindeki villuslar sayesinde emilerek kana geçer (s. 95).", "kavram": "İnce Bağırsak"},
 {"metin": ["Ayşe bahçeden kopardığı elmayı ısırıp çiğnemeye başladı.", "Elma ağızda hem fiziksel hem kimyasal sindirime uğradı.", "Yutaktan geçen lokmalar yemek borusuyla mideye ulaştı.", "Midede bulamaç hâline gelen parçalar ince bağırsağa gönderildi.", "İnce bağırsakta sindirim tamamlandı ve gerekli kısımlar emildi.", "Geriye kalan posadaki fazla su ve mineraller kalın bağırsakta emildi."],
  "soru": "Metne göre elmanın sindirimi hangi organda tamamlanmıştır?", "bolge": ["sindirimi hangi organda tamamlanmıştır"],
  "serit": "Sindirimin tamamlandığı organ", "kanit": [4],
  "secenekler": ["İnce bağırsak", "Mide", "Kalın bağırsak"], "dogru": 0, "tuzak": [1, 2],
  "ipucu": "“Tamamlandı” kelimesinin geçtiği cümleyi oku.", "kanitIpucu": "Metinde “tamamlandı” kelimesi hangi cümlede?",
  "aciklama": "Besinlerin fiziksel ve kimyasal sindirimi ince bağırsakta tamamlanır. Kalın bağırsakta ise su ve bazı mineraller emilir (s. 94–95).", "kavram": "İnce Bağırsak"}]}
