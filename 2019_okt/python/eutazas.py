file = open("utasadat.txt")
adatok = []
for line in file:
    parts = line.strip().split(" ")
    adatok.append({"megallo": int(parts[0]),
                   "datum": int(parts[1][:8]),
                   "ev": int(parts[1][:4]),
                   "honap": int(parts[1][4:6]),
                   "nap": int(parts[1][6:8]),
                   "ido": parts[1][9:],
                   "azonosito": int(parts[2]),
                   "tipus": parts[3],
                   "ervenyesseg": int(parts[4])})

print("2.feladat")
print(f"A buszra {adatok.__len__()} utas akart felszállni.")

print("3.feladat")

nem_ervenyes = 0
ervenyes_utazok = []

for adat in adatok:
    if adat["ervenyesseg"] == 0 or 10 < adat["ervenyesseg"] < adat["datum"]:
        nem_ervenyes += 1
    else:
        ervenyes_utazok.append(adat)

print(f"A buszra {nem_ervenyes} utas nem szállhatott fel.")

print("4.feladat")

megallok = set()
utasok_szama = []

for adat in adatok:
    megallok.add(adat["megallo"])

for megallo in megallok:
    utas_szam = 0
    for adat in adatok:
        if adat["megallo"] == megallo:
            utas_szam += 1
    utasok_szama.append([utas_szam, megallo])

max_utas = utasok_szama[0]

for utas in utasok_szama:
    if utas[0] > max_utas[0]:
        max_utas = utas

print(f"A legtöbb utas ({max_utas[0]} fő) a {max_utas[1]}. megállóban próbált fellszállni.")

print("5.feladat")

ingyenes = 0
kedvezmenyes = 0

for adat in ervenyes_utazok:
    if adat["tipus"] == "NYP" or adat["tipus"] == "RVS" or adat["tipus"] == "GYK":
        ingyenes += 1
    if adat["tipus"] == "TAB" or adat["tipus"] == "NYB":
        kedvezmenyes += 1

print(f"Ingyenesen utazók száma: {ingyenes} fő")
print(f"Kedvezményesen utazók száma: {kedvezmenyes} fő")


# 6.feladat

def napokszama(e1, h1, n1, e2, h2, n2):
    h1 = (h1 + 9) % 12
    e1 = e1 - h1 / 10
    d1 = 365 * e1 + e1 / 4 - e1 / 100 + e1 / 400 + (h1 * 306 + 5) / 10 + n1 - 1
    h2 = (h2 + 9) % 12
    e2 = e2 - h2 / 10
    d2 = 365 * e2 + e2 / 4 - e2 / 100 + e2 / 400 + (h2 * 306 + 5) / 10 + n2 - 1
    return d2 - d1


# 7.feladat

file = open("figyelmeztetes.txt", "w")

for adat in adatok:
    if adat["tipus"] != "JGY":
        ev2 = str(adat["ervenyesseg"])[:4]
        ho2 = str(adat["ervenyesseg"])[4:6]
        nap2 = str(adat["ervenyesseg"])[6:]
        kulonbseg = int(napokszama(adat["ev"], adat["honap"], adat["nap"], int(ev2), int(ho2), int(nap2)))
        if 0 <= kulonbseg <= 3:
            file.write(f"{adat['azonosito']} {ev2}-{ho2}-{nap2}\n")
