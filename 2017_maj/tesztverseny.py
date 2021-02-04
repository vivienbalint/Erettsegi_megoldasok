file = open("valaszok.txt")

megoldas = file.readline().strip()
versenyzok = []

print("1.feladat: Az adatok beolvasása")

for line in file:
    parts = line.strip().split(" ")
    versenyzo = {"kod": parts[0],
                 "valasz": parts[1]}
    versenyzok.append(versenyzo)

print(f"2.feladat: A vetélkedőn {versenyzok.__len__()} versenyző indult.")

val_az = input("3.feladat: A versenyző azonosítója = ")
valasz = ""
for versenyzo in versenyzok:
    if versenyzo["kod"] == val_az:
        valasz = versenyzo["valasz"]

print(f"{valasz} (a versenyző válasza)")
print("4.feladat:")
print(f"{megoldas} (a helyes megoldás)")


def compare(a, b):
    for x, y in zip(a, b):
        if x == y:
            print("+", end="")
        else:
            print(" ", end="")


compare(megoldas, valasz)
print(" (a versenyző helyes válaszai)")

sorszam = int(input("5.feladat: A feladat sorszáma = "))

helyes_megoldas = 0

for versenyzo in versenyzok:
    if megoldas[sorszam - 1] == versenyzo["valasz"][sorszam - 1]:
        helyes_megoldas += 1

szazalek = round((helyes_megoldas / versenyzok.__len__() * 100), 2)

print(f"A feladatra {helyes_megoldas} fő, a versenyzők {szazalek}%-a adott helyes választ.")

print("6.feladat: A versenyzők pontszámának meghatározása")

elert_pontszamok = []

for v in versenyzok:
    pontszam = 0
    if megoldas[0] == v["valasz"][0]:
        pontszam += 3
    if megoldas[1] == v["valasz"][1]:
        pontszam += 3
    if megoldas[2] == v["valasz"][2]:
        pontszam += 3
    if megoldas[3] == v["valasz"][3]:
        pontszam += 3
    if megoldas[4] == v["valasz"][4]:
        pontszam += 3
    if megoldas[5] == v["valasz"][5]:
        pontszam += 4
    if megoldas[6] == v["valasz"][6]:
        pontszam += 4
    if megoldas[7] == v["valasz"][7]:
        pontszam += 4
    if megoldas[8] == v["valasz"][8]:
        pontszam += 4
    if megoldas[9] == v["valasz"][9]:
        pontszam += 4
    if megoldas[10] == v["valasz"][10]:
        pontszam += 5
    if megoldas[11] == v["valasz"][11]:
        pontszam += 5
    if megoldas[12] == v["valasz"][12]:
        pontszam += 5
    if megoldas[13] == v["valasz"][13]:
        pontszam += 6
    elert_pontszamok.append(pontszam)

file2 = open("pontok.txt", "w")

for pont, versenyzo in enumerate(versenyzok):
    file2.write(f"{versenyzo['kod']} {elert_pontszamok[pont]}\n")

print("7.feladat: A verseny legjobbjai: ")

versenyzo_kod = []

for versenyzo in versenyzok:
    versenyzo_kod.append(versenyzo["kod"])

versenyzok_pontszama = sorted(zip(versenyzo_kod, elert_pontszamok), key=lambda x: x[1], reverse=True)

for count, x in enumerate(versenyzok_pontszama, start=1):
    thisx = x
    nextx = versenyzok_pontszama[versenyzok_pontszama.index(x) - len(versenyzok_pontszama) + 1]
    if count > 1:
        prevx = versenyzok_pontszama[versenyzok_pontszama.index(x) - len(versenyzok_pontszama) - 1]
        if x[1] != nextx[1] and x[1] != prevx[1]:
            print(f"{count}. díj ({x[1]} pont): {x[0]}")
        if x[1] != nextx[1] and x[1] == prevx[1]:
            print(f"{count}. díj ({nextx[1]} pont): {nextx[0]}")
    if count <= 1:
        if x[1] != nextx[1]:
            print(f"{count}. díj ({x[1]} pont): {x[0]}")
    if x[1] == nextx[1]:
        print(f"{count}. díj ({x[1]} pont): {x[0]}")
        print(f"{count}. díj ({nextx[1]} pont): {nextx[0]}")
    if count == 3:
        break
