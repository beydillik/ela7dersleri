"""Bir ünitenin konu içeriğini kısa metin olarak döker (havuz yazarken okumak için). python3 araclar/sinav/dok.py fen1 2"""
import json, sys, os
kod, un = sys.argv[1], int(sys.argv[2]); KOK = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
d = json.load(open(f"{KOK}/public/{kod}/ders.json"))
u = [x for x in d["uniteler"] if x.get("no") == un][0]
for k in u["konular"]:
    f = f"{KOK}/public/{kod}/konular/{k['id']}.json"; j = json.load(open(f))
    if k.get("tur") == "tarama": print(f"## {k['id']} DURAK {k['baslik']} kapsar={j.get('kapsar')}"); continue
    print(f"## {k['id']} {k['baslik']} | {j.get('sayfalar')}")
    for kv in j.get("kavramlar", []):
        print(f"- [{kv['ad']}] {kv.get('aciklama','')} {kv.get('ek','') or ''} | Akılda: {kv.get('akilda','')}")
    for a in j.get("akildaKalsin", []) or []: print("  * " + a)
    print("  sorular:", " / ".join(q.get("soru", "")[:70] for q in j.get("sorular", [])))
