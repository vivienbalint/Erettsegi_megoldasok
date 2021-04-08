import random

print("1.feladat")


def szimulacio():
    eredmenyek = ["F", "I"]
    return random.choice(eredmenyek)


print(f"A pénzfeldobás eredménye: {szimulacio()}")

print("2.feladat")

tipp = input("Tippeljen! (F/I)= ")

dobas_eredmeny = szimulacio()

print(f"A tipp {tipp}, a dobás eredménye {dobas_eredmeny} volt.")

if tipp == dobas_eredmeny:
    print("Ön eltalálta.")
else:
    print("Ön nem találta el.")

print("3.feladat")

dobasok_szama = 0
fej = 0
with open("kiserlet.txt") as file:
    for line in file:
        # 3.feladat
        dobasok_szama += 1
        # 4.feladat
        if line.strip() == "F":
            fej += 1

print(f"A kísérlet {dobasok_szama} dobásból állt.")

print("4.feladat")

fej_relativ_gyak = round((fej / dobasok_szama * 100), 2)

print(f"A kísérlet során a fej relatív gyakorisága {fej_relativ_gyak}% volt.")

print("5.feladat")

fej_dobasok_szama = 0
darab = 0
max = 0
kezdet = 0

with open("kiserlet.txt") as file2:
    for count, line in enumerate(file2):
        # 5.feladat
        if line.strip() == "F":
            darab += 1
        else:
            if darab == 2:
                fej_dobasok_szama += 1
            # 6.feladat
            if darab > max:
                max = darab
                kezdet = count - (max - 1)
            darab = 0

print(f"A kísérlet során {fej_dobasok_szama} alkalommal dobtak pontosan két fejet egymás után.")

print("6.feladat")

print(f"A leghosszabb tisztafej sorozat {max} tagból áll, kezdete a(z) {kezdet}. dobás.")

# 7.feladat


def dob():
    j = 0
    sorozat = ""
    while j < 4:
        dobas = szimulacio()
        sorozat += dobas
        j += 1
    return sorozat


i = 0
sorozatok = []

while i < 1000:
    sorozatok.append(dob())
    i += 1

tfej = 0
tiras = 0

for sorozat in sorozatok:
    if sorozat == "FFFF":
        tfej += 1
    elif sorozat == "FFFI":
        tiras += 1

with open("dobasok.txt", "w") as file:
    file.write(f"FFFF: {tfej}, FFFI: {tiras}\n")
    for sorozat in sorozatok:
        file.write(sorozat + " ")
