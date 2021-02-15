file = open("kerites.txt")

adatok = []
hsz1 = -1
hsz2 = 0

for line in file:
    split = line.strip().split(" ")

    if split[0] == "0":
        hsz2 += 2
        adatok.append({"hazszam": int(hsz2),
                       "oldal": int(split[0]),
                       "hossz": int(split[1]),
                       "allapot": split[2]
                       })

    elif split[0] == "1":
        hsz1 += 2
        adatok.append({"hazszam": int(hsz1),
                       "oldal": int(split[0]),
                       "hossz": int(split[1]),
                       "allapot": split[2]
                       })

print("2.feladat")

print(f"Az eladott telkek száma: {adatok.__len__()}")

print("3.feladat")

if adatok[-1]["oldal"] == 0:
    oldal = "páros"
else:
    oldal = "páratlan"

print(f"A {oldal} oldalon adták el az utolsó telket.")

print(f"Az utolsó telek házszáma: {adatok[-1]['hazszam']}")

print("4.feladat")

paratlanKeritesek = [adat for adat in adatok if adat["oldal"] == 1]

for adat in paratlanKeritesek:
    nextAdat = paratlanKeritesek[paratlanKeritesek.index(adat) - len(paratlanKeritesek) + 1]
    if adat["allapot"] != "#" and adat["allapot"] != ":":
        if adat["allapot"] == nextAdat["allapot"]:
            hazszam = adat["hazszam"]
            break

print(f"A szomszédossal egyezik a kerítés színe: {hazszam}")

print("5.feladat")

valHsz = input("Adjon meg egy házszámot: ")

for adat in adatok:
    if adat["hazszam"] == int(valHsz):
        allapot = adat["allapot"]

print(f"A kerítés színe / állapota: {allapot}")

szinek = {"Q", "W", "E", "R", "T", "Z", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Y", "X", "C", "V", "B", "N", "M"}

parosKeritesek = [adat for adat in adatok if adat["oldal"] == 0]
tiltottSzin1 = ""
tiltottSzin2 = ""
tiltottSzin3 = ""

for count, adat in enumerate(adatok):
    if adat["hazszam"] == int(valHsz):
        if adat["allapot"] != "#" and adat["allapot"] != ":":
            tiltottSzin1 = adat["allapot"]
        if adat["oldal"] == 0:
            for kerites in parosKeritesek:
                nextAdat = parosKeritesek[parosKeritesek.index(adat) - len(parosKeritesek) + 1]
                if nextAdat["allapot"] != "#" and nextAdat["allapot"] != ":":
                    tiltottSzin2 = nextAdat["allapot"]
            if count > 1:
                prevAdat = parosKeritesek[parosKeritesek.index(adat) - len(parosKeritesek) - 1]
                if prevAdat["allapot"] != "#" and prevAdat["allapot"] != ":":
                    tiltottSzin3 = prevAdat["allapot"]
        else:
            for kerites in paratlanKeritesek:
                nextAdat = paratlanKeritesek[paratlanKeritesek.index(adat) - len(paratlanKeritesek) + 1]
                if nextAdat["allapot"] != "#" and nextAdat["allapot"] != ":":
                    tiltottSzin2 = nextAdat["allapot"]
            if count > 1:
                prevAdat = paratlanKeritesek[paratlanKeritesek.index(adat) - len(paratlanKeritesek) - 1]
                if prevAdat["allapot"] != "#" and prevAdat["allapot"] != ":":
                    tiltottSzin3 = prevAdat["allapot"]
        for szin in szinek:
            if szin != tiltottSzin1 and szin != tiltottSzin2 and szin != tiltottSzin3:
                lehetsegesSzin = szin
                break

print(f"Egy lehetséges festési szín: {lehetsegesSzin}")

# 6.feladat

file = open("utcakep.txt", "w")

elsoSor = ""
masodikSor = ""

for adat in paratlanKeritesek:
    i = 1
    j = 1
    masodikSor += str(adat["hazszam"])
    while i <= adat["hossz"]:
        elsoSor += adat["allapot"]
        i += 1
    while j <= (adat["hossz"] - len((str(adat["hazszam"])))):
        masodikSor += " "
        j += 1

file.write(f"{elsoSor}\n")
file.write(masodikSor)
