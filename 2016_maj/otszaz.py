adatok = []
kosar = []

with open("penztar.txt") as file:
    for line in file:
        if line.strip() != "F":
            kosar.append(line.strip())
        else:
            adatok.append(kosar)
            kosar = []

print("2.feladat")

print(f"A fizetések száma: {len(adatok)}")

print("3.feladat")

print(f"Az első vásárló {len(adatok[0])} darab árucikket vásárolt.")

print("4.feladat")

val_sorszam = int(input("Adja meg egy vásárlás sorszámát! "))
val_arucikk = input("Adja meg egy árucikk nevét! ")
val_darab = int(input("Adja meg a vásárolt darabszámot! "))

print("5.feladat")

elso = 1000
utolso = 0
ossz = 0

for count, adat in enumerate(adatok):
    if val_arucikk in adat:
        ossz += 1
        if count < elso:
            elso = count + 1
        if count > utolso:
            utolso = count + 1

print(f"Az első vásárlás sorszáma: {elso}")
print(f"Az utolsó vásárlás sorszáma: {utolso}")
print(f"{ossz} vásárlás során vettek belőle")

print("6.feladat")


def ertek(db):
    sum = 0
    if db == 1:
        sum = 500
    elif db == 2:
        sum = 950
    elif db > 2:
        sum = 950 + ((db - 2) * 400)
    return sum


print(f"{val_darab} darab vételekor fizetendő: {ertek(val_darab)}")

print("7.feladat")

lista = []
lista_dupl_nelkul = []

for count, adat in enumerate(adatok):
    if count + 1 == val_sorszam:
        darab = 0
        for termek in adat:
            darab += adat.count(termek)
            lista.append([darab, termek])
            darab = 0

for termek in lista:
    if termek not in lista_dupl_nelkul:
        lista_dupl_nelkul.append(termek)


for termek in lista_dupl_nelkul:
    print(termek[0], termek[1])


# 8.feladat

egesz_lista = []
temp_lista = []
egesz_lista_dupl_nelkul = []
temp_lista_dupl_nelkul = []

for adat in adatok:
    darab = 0
    for termek in adat:
        darab += adat.count(termek)
        temp_lista.append([darab, termek])
        darab = 0
    egesz_lista.append(temp_lista)
    temp_lista = []


for kosar in egesz_lista:
    for termek in kosar:
        if termek not in temp_lista_dupl_nelkul:
            temp_lista_dupl_nelkul.append(termek)
    egesz_lista_dupl_nelkul.append(temp_lista_dupl_nelkul)
    temp_lista_dupl_nelkul = []

with open("osszeg.txt", 'w') as file:
    for count, adat in enumerate(egesz_lista_dupl_nelkul):
        ossz = 0
        for termek in adat:
            termek_ertek = ertek(termek[0])
            ossz += termek_ertek
        file.write(f"{count + 1}: {ossz}\n")
