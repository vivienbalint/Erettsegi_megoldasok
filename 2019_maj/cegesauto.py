file = open("autok.txt")

adatok = []

for line in file:
    parts = line.strip().split(" ")
    adatok.append({"nap": int(parts[0]),
                   "idopont": parts[1],
                   "ora": int(parts[1][:2]),
                   "perc": int(parts[1][3:]),
                   "rendszam": parts[2],
                   "auto_szama": parts[2][3:],
                   "azonosito": int(parts[3]),
                   "km": int(parts[4]),
                   "ki_be": int(parts[5])})

print("2.feladat")

kivitt_autok = [adat for adat in adatok if adat["ki_be"] == 0]
print(f"{kivitt_autok[-1]['nap']}. nap rendszam: {kivitt_autok[-1]['rendszam']}")

print("3.feladat")

val_nap = input("Nap: ")

print(f"Forgalom a(z) {val_nap}. napon: ")

for adat in adatok:
    if adat["nap"] == int(val_nap):
        if adat["ki_be"] == 0:
            print(f"{adat['idopont']} {adat['rendszam']} {adat['azonosito']} ki")
        else:
            print(f"{adat['idopont']} {adat['rendszam']} {adat['azonosito']} be")

print("4. feladat")

kivitt = 0

for adat in adatok:
    if adat["ki_be"] == 0:
        kivitt += 1
    else:
        kivitt -= 1

print(f"A hónap végén {kivitt} autót nem hoztak vissza.")

print("5.feladat")

autok = set()

for adat in adatok:
    autok.add(adat["rendszam"])

for auto in autok:
    auto_adatok = [adat for adat in adatok if adat["rendszam"] == auto]
    km_allas = [adat["km"] for adat in auto_adatok]
    min_km = min(km_allas)
    max_km = max(km_allas)
    print(f"{auto} {max_km - min_km} km")

print("6.feladat")

max_km = 0
max_azonosito = 0
count = 0

for adat in adatok:
    if adat["ki_be"] == 1:
        for i in range(count - 1, -1, -1):
            if adatok[i]["ki_be"] == 0 and adat["rendszam"] == adatok[i]["rendszam"]:
                osszKm = adat["km"] - adatok[i]["km"]
                if osszKm > max_km:
                    max_km = osszKm
                    max_azonosito = adat["azonosito"]
                break

    count += 1

print(f"Leghosszabb út: {max_km} km, személy: {max_azonosito}")

print("7.feladat")

val_rendszam = input("Rendszám: ")

file = open(f"{val_rendszam}_menetlevel.txt", "w")

val_rendszam_adat = [adat for adat in adatok if adat["rendszam"] == val_rendszam]

for adat in val_rendszam_adat:
    if adat["ki_be"] == 0:
        file.write(f"{adat['azonosito']}\t{adat['nap']}. {adat['idopont']}\t{adat['km']}\t km\t")
    else:
        file.write(f"{adat['nap']}. {adat['idopont']}\t{adat['km']} km\n")

print("Menetlevél kész.")
