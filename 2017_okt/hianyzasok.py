file = open("naplo.txt")

adatok = []

for line in file:
    parts = line.strip().split(" ")
    if parts[0] == "#":
        honap = int(parts[1])
        nap = int(parts[2])
    else:
        vnev = parts[0]
        knev = parts[1]
        jelenlet = parts[2]
        adatok.append([honap, nap, vnev + " " + knev, jelenlet])

print("2. feladat")

print(f"A naplóban {adatok.__len__()} bejegyzés van.")

print("3. feladat")

igazolt = 0
igazolatlan = 0

for adat in adatok:
    igazolt += adat[3].count("X")
    igazolatlan += adat[3].count("I")

print(f"Az igazolt hiányzások száma {igazolt}, az igazolatlanoké {igazolatlan} óra.")

# 4.feladat

def hetnapja(honap, nap):
    napnev = ["vasarnap", "hetfo", "kedd", "szerda", "csutortok", "pentek", "szombat"]
    napszam = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]
    napsorszam = (napszam[honap - 1] + nap) % 7
    hetnapja = napnev[napsorszam]
    return hetnapja

print("5.feladat")

val_honap = int(input("A hónap sorszáma="))
val_nap = int(input("A nap sorszáma="))

print(f"Azon a napon {hetnapja(val_honap, val_nap)} volt.")

print("6.feladat")

val_nap_2 = input("A nap neve=")
val_oraszam = int(input("Az óra sorszáma="))

hianyzasok = 0

for adat in adatok:
    if hetnapja(adat[0], adat[1]) == val_nap_2:
        hianyzasok += adat[3][val_oraszam - 1].count("X")
        hianyzasok += adat[3][val_oraszam - 1].count("I")

print(f"Ekkor összesen {hianyzasok} óra hiányzás történt.")

print("7.feladat")

tanulok = set()
tanulok_hianyzassal = []

for adat in adatok:
    tanulok.add(adat[2])

for tanulo in tanulok:
    tanulo_adatok = [adat for adat in adatok if adat[2] == tanulo]
    tanulo_hianyzasok = 0
    for adat in tanulo_adatok:
        tanulo_hianyzasok += adat[3].count("X")
        tanulo_hianyzasok += adat[3].count("I")
    tanulok_hianyzassal.append([tanulo, tanulo_hianyzasok])

legtobb_hianyzas = 0

for adat in tanulok_hianyzassal:
    if adat[1] > legtobb_hianyzas:
        legtobb_hianyzas = adat[1]

legtobbet_hianyzok = []

for adat in tanulok_hianyzassal:
    if adat[1] == legtobb_hianyzas:
        legtobbet_hianyzok.append(adat[0])

print("A legtöbbet hiányzó tanulók: " + " ".join(legtobbet_hianyzok))