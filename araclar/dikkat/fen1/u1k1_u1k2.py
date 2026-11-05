"""Fen u1k1–u1k2 (pilot, 5 Kasım 2026). Kitap: kaynaklar/fen1/unite1.md"""
TEKRAR = {
    "u1k1": [
        ("Uzay, Dünya'nın {atmosferi dışında|içinde|altında} yer alan çok geniş bir ortamdır. {Tamamen boş değildir|Tamamen boştur}; çok az gaz, toz ve parçacık bulunur.", "s. 16"),
        ("Uzay roketi, uzay araçlarını yeryüzünden {yörüngeye|yeraltına|okyanusa} taşır. Önceden tek kullanımlıktı, artık {yeniden kullanılabilir|tek kullanımlık} biçimde üretiliyor.", "s. 18"),
        ("Yapay uydu, Dünya'nın çevresinde belirli bir {yörüngede dolanır|yüzeyinde yürür|çevresinde durur}. Enerjisini {güneş panellerinden|rüzgâr türbininden|yakıttan} alır.", "s. 18"),
        ("Uzay sondası, bir gök cismini incelemek için gönderilen {robotik|insanlı} bir araçtır; {Dünya'dan kontrol edilir|içindeki astronotlar kontrol eder}.", "s. 18"),
        ("Uzay mekiğini içindeki {astronotlar|Dünya'daki bilgisayarlar|robotlar} kontrol eder. Astronotları, büyük uyduları ve malzemeleri {uzay istasyonuna|Ay'ın yüzeyine|gözlemevine} taşır.", "s. 18"),
        ("Uzay istasyonunda astronotlar {düşük|yüksek} yer çekimli ortamda deney yapar. Yeniden kullanılamaz; ömrü {bakım ve onarımla|yakıt eklenerek|boyanarak} uzatılır.", "s. 19"),
        ("Teleskop, gök cisimlerini {gözlemlemek|taşımak|kontrol etmek} için kullanılır. Dünya'nın yörüngesine çıkarılırsa {daha net|daha bulanık} görüntü elde edilir.", "s. 19"),
    ],
    "u1k2": [
        ("Teleskoplar yerleştirildikleri yere göre {iki|üç|dört} sınıfa ayrılır: uzay teleskobu ve yer tabanlı teleskop.", "s. 22"),
        ("Atmosfer, uzaydan gelen ışınların büyük bölümünü engeller. Uzay teleskobu bu sorunla karşılaşmadığı için {daha net|daha bulanık} görüntü elde eder.", "s. 22"),
        ("Hubble'ın ilk görüntüleri net olmadığı için {1993'te|1997'de|2005'te} onarıldı. James Webb ise Hubble'dan {100|10|1000} kat daha güçlüdür.", "s. 22"),
        ("James Webb'in rokete sığması için {origami|çadır|yelken} tekniğiyle katlanmış, uzaya ulaşınca açılmıştır.", "s. 22"),
        ("Yer tabanlı teleskop bazı ışınları yakalayamasa da maliyeti {düşük|yüksek}, bakımı {kolay|zor} olduğu için tercih edilir.", "s. 23"),
        ("Işık kaynakları yanlış kullanılınca oluşan {ışık kirliliği|hava kirliliği|ses kirliliği} gözlemi zorlaştırır. Bu yüzden gözlemevi yerleşim merkezlerinden {uzak|yakın} ve {yüksek|alçak} rakımlı bir yere kurulur.", "s. 23"),
        ("Teleskopların yerleştirildiği kubbe benzeri yapıya {gözlemevi (rasathane)|uzay istasyonu|uydu merkezi} denir. Ülkemizin en büyük gözlemevi TUG, {Antalya'da|Erzurum'da|Ankara'da} kuruludur.", "s. 23"),
    ],
}

KISA = {
    "u1k1": [
        {"soru": "Uzay mekiği ile uzay roketi arasındaki bir benzerliği ve bir farkı yazınız.",
         "tetik": ["benzerliği", "farkı"],
         "okut": ["Önce benzerliği, sonra farkı yaz (iki parça).", "Yalnız bir tanım yaz: “X, … araçtır.”", "Evet ya da hayır yaz, sonra nedenini ekle."],
         "parcalar": [
             {"bas": "Benzerlik:", "ornek": "İkisi de yeniden kullanılabilir.", "havuz": ["İkisi de tek kullanımlıktır.", "İkisi de insansız araçtır."], "k": ["yeniden"]},
             {"bas": "Fark:", "ornek": "Mekiği içindeki astronotlar kontrol eder, roket ise Dünya'dan kontrol edilebilir.", "havuz": ["Mekik uyduları taşır, roket hiçbir şey taşımaz.", "Mekik tek kullanımlıktır, roket yeniden kullanılabilir."], "k": ["astronot", "dünya"]}],
         "kisa": "Benzerlik: ikisi de yeniden kullanılabilir. Fark: mekiği astronotlar, roketi Dünya'dan kontrol eder.",
         "cevap": "Benzerlik: İkisi de yeniden kullanılabilir. Fark: Mekiği içindeki astronotlar kontrol eder, roket ise Dünya'dan kontrol edilebilir.",
         "anahtarlar": [{"ad": "ikisi de yeniden kullanılabilir", "k": ["yeniden"]}, {"ad": "mekiği astronotlar kontrol eder", "k": ["astronot"]}, {"ad": "roket Dünya'dan kontrol edilir", "k": ["dünya"]}],
         "sayfa": "s. 18"},
        {"soru": "Uzay sondasının görevi nedir ve nasıl kontrol edilir? Yazınız.",
         "tetik": ["görevi nedir", "nasıl kontrol edilir"],
         "okut": ["Görevini yaz, sonra kim kontrol eder yaz (iki parça).", "Benzerlik ve fark yaz.", "Sebep ve sonuç yaz: “… çünkü …”"],
         "parcalar": [
             {"bas": "Görevi:", "ornek": "Bir gök cismini ya da uzaydaki olayları incelemek.", "havuz": ["Astronotları uzay istasyonuna taşımak.", "Dünya'nın çevresinde dolanarak haberleşmeyi sağlamak."], "k": ["incele"]},
             {"bas": "Kontrol:", "ornek": "Dünya'dan kontrol edilir.", "havuz": ["İçindeki astronotlar kontrol eder.", "Uzay istasyonundaki personel kontrol eder."], "k": ["dünya"]}],
         "kisa": "Gök cismini ya da uzaydaki olayları incelemek için gönderilir; Dünya'dan kontrol edilir.",
         "cevap": "Uzay sondası, bir gök cismini veya uzayda meydana gelen olayları incelemek için gönderilen robotik uzay aracıdır. Dünya'dan kontrol edilebilir.",
         "anahtarlar": [{"ad": "gök cismini / uzay olaylarını incelemek", "k": ["incele"]}, {"ad": "Dünya'dan kontrol edilir", "k": ["dünya"]}],
         "sayfa": "s. 18"},
    ],
    "u1k2": [
        {"soru": "Uzay teleskobu, yeryüzünden gözlem yapan teleskoba göre neden daha net görüntü elde eder? Yazınız.",
         "tetik": ["neden daha net"],
         "okut": ["Neden → engeli (sebep) yaz, sonra uzay teleskobunun ne yaptığını (sonuç) yaz.", "Karşılaştır: benzerlik ve fark yaz.", "Tanım yaz: “X, … teleskoptur.”"],
         "parcalar": [
             {"bas": "Yeryüzünde engel:", "ornek": "Atmosfer ışınların büyük bölümünü engeller; hava kirliliği ve uyduların ışık izleri de gözlemi zorlaştırır.", "havuz": ["Yeryüzünde ışınlar çok güçlü olduğu için.", "Yeryüzündeki teleskoplar çok küçük olduğu için."], "k": ["atmosfer"]},
             {"bas": "Uzay teleskobu:", "ornek": "Bu engellerle karşılaşmaz, bu yüzden görüntüyü daha net alır.", "havuz": ["Daha ucuz olduğu için.", "Daha küçük olduğu için."], "k": ["karşılaşmaz", "engel"]}],
         "kisa": "Atmosfer ışınları engeller; uzay teleskobu bu engelle karşılaşmaz, daha net görür.",
         "cevap": "Yeryüzünde atmosfer uzaydan gelen ışınların büyük bölümünü engeller; atmosfer kirliliği ve uyduların ışık izleri de gözlemi zorlaştırır. Uzay teleskobu bu sorunlarla karşılaşmadığı için çok daha net ve ayrıntılı görüntü elde eder.",
         "anahtarlar": [{"ad": "atmosfer ışınları engeller", "k": ["atmosfer"]}, {"ad": "uzay teleskobu bu engelle karşılaşmaz", "k": ["karşılaşmaz", "engel"]}],
         "sayfa": "s. 22"},
        {"soru": "Bir gözlemevi neden kalabalık bir şehrin ortasına kurulmaz? İki sebep yazınız.",
         "tetik": ["neden", "İki sebep"],
         "okut": ["Neden → iki ayrı sebep yaz.", "Evet ya da hayır yaz, sonra nedenini ekle.", "Önce tanım, sonra örnek yaz."],
         "parcalar": [
             {"bas": "Birinci sebep:", "ornek": "Şehirdeki ışıklar ışık kirliliği oluşturur, gökyüzü net görünmez.", "havuz": ["Şehirlerde teleskop satılmadığı için.", "Şehirlerde yıldız bulunmadığı için."], "k": ["kirli"]},
             {"bas": "İkinci sebep:", "ornek": "Gözlemevi yüksek rakımlı ve TV-radyo yayınlarından uzak bir yerde olmalıdır.", "havuz": ["Gözlemevinin kubbesi şehirde açılamaz.", "Şehirde gece olmaz."], "k": ["yüksek", "rakım", "yayın"]}],
         "kisa": "Işık kirliliği gökyüzünü bozar; ayrıca yüksek rakımlı, yayınlardan uzak yer gerekir.",
         "cevap": "Şehirdeki ışıklar ışık kirliliği oluşturur ve gökyüzü net görünmez. Ayrıca gözlemevi yüksek rakımlı ve TV-radyo yayınlarından uzak bir yerde olmalıdır.",
         "anahtarlar": [{"ad": "ışık kirliliği", "k": ["kirli"]}, {"ad": "yüksek rakım / yayınlardan uzak", "k": ["yüksek", "rakım", "yayın"]}],
         "sayfa": "s. 23"},
    ],
}

ELLE = {
    "Uzay için hangisi doğrudur?": "hangisi doğrudur",
    "Teleskoplar yerleştirildikleri yere göre kaç sınıfa ayrılır?": "kaç sınıfa",
    "Hangisi güneş paneli kullanmaz?": "kullanmaz",
    "Hangisi yeryüzünden gözlem yapmayı zorlaştıran bir etken DEĞİLDİR?": "DEĞİLDİR",
    "Gözlemevi kurulacak yerde hangisi ARANMAZ?": "ARANMAZ",
    "Uzay mekiğini kim kontrol eder?": "kim",
    "Uzay sondasını kim kontrol eder?": "kim",
    "Yapay uydu uzayda ne yapar?": "ne yapar",
    "Uzay mekiği neleri uzay istasyonuna taşır?": "neleri",
    "Astronotlar uzay istasyonunda ne yapar?": "ne yapar",
    "Hubble'ın ilk görüntüleri net gelmeyince ne yapıldı?": "ne yapıldı",
    "Şehirde teleskopla net görüntü almayı en çok ne zorlaştırır?": "ne zorlaştırır",
}
OKUT = {
 "u1k1": [["mekik ile roketin bir benzer yanını ve bir farklı yanını yazmanı", "mekiğin ne işe yaradığını anlatmanı", "hangisinin daha büyük olduğunu söylemeni"],
          ["sondanın ne işe yaradığını ve onu kimin, nereden yönettiğini yazmanı", "sondanın nasıl bir şekli olduğunu anlatmanı", "sondanın ne zaman icat edildiğini söylemeni"]],
 "u1k2": [["uzay teleskobunun görüntüsünün neden daha net olduğunu, sebebiyle yazmanı", "uzay teleskobunun nerede durduğunu söylemeni", "iki teleskoptan hangisinin daha ucuz olduğunu yazmanı"],
          ["gözlemevinin şehir ortasına kurulmamasının iki sebebini yazmanı", "gözlemevinin nasıl bir bina olduğunu anlatmanı", "Türkiye'deki en büyük gözlemevinin adını söylemeni"]],
}
