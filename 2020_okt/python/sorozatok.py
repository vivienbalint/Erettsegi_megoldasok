import math

file = open("lista.txt")
lines = file.readlines()
lines = [line.strip() for line in lines]

sorozatok = []

for count, line in enumerate(lines):
    if count % 5 == 0:
        sorozatok.append({"air_date": lines[count],
                          "title": lines[count + 1],
                          "season_episode": lines[count + 2],
                          "length": int(lines[count + 3]),
                          "seen": int(lines[count + 4])})

print("2.feladat")

known_air_date_sorozatok = []

for known_air_date in sorozatok:
    if known_air_date["air_date"] != "NI":
        known_air_date_sorozatok.append(known_air_date)

print(f"A listában {known_air_date_sorozatok.__len__()} db vetítési dátummal rendelkező epizód van.")

print("3.feladat")

seen = 0
not_seen = 0
latott_sorozatok = []
nem_latott_sorozatok = []

for sorozat in sorozatok:
    if sorozat["seen"] == 1:
        seen += 1
        latott_sorozatok.append(sorozat)
    else:
        not_seen += 1
        nem_latott_sorozatok.append(sorozat)

percentage = round((seen / (seen + not_seen)) * 100, 2)

print(f"A listában lévő epizódok {percentage}%-át látta.")

print("4.feladat")

length = 0

for sorozat in latott_sorozatok:
    length += sorozat["length"]

minute = length % 60
hour = length / 60
day = hour / 24
hour = hour % 24

print(f"Sorozatnézéssel {math.floor(day)} napot {math.floor(hour)} órát és {math.floor(minute)} percet töltött.")

print("5.feladat")

date = input("Adjon meg egy dátumot! Dátum= ")

datumig_nem_latott_sorozatok = [sorozat for sorozat in nem_latott_sorozatok if sorozat["air_date"] <= date]

for sorozat in datumig_nem_latott_sorozatok:
    print(f"{sorozat['season_episode']}\t{sorozat['title']}")


# 6.feladat

def hetnapja(ev, ho, nap):
    napok = ["v", "h", "k", "sze", "cs", "p", "szo"]
    honapok = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if ho < 3:
        ev -= 1
    return napok[math.floor((ev + ev / 4 - ev / 100 + ev / 400 + honapok[ho - 1] + nap) % 7)]


print("7.feladat")

val_nap = input("Adja meg a hét egy napját (például cs)! Nap= ")

titles = set()

for sorozat in known_air_date_sorozatok:
    datum = sorozat["air_date"].split(".")
    ev = int(datum[0])
    ho = int(datum[1])
    nap = int(datum[2])
    if hetnapja(ev, ho, nap) == val_nap:
        titles.add(sorozat["title"])

if titles.__len__() > 0:
    for title in titles:
        print(title)
else:
    print("Az adott napon nem kerül adásba sorozat.")

# 8.feladat

film_list = set()
episode_count = []
sum_length = []

for sorozat in sorozatok:
    film_list.add(sorozat["title"])

for film in film_list:
    length = 0
    count = 0
    data_from_film = [sorozat for sorozat in sorozatok if sorozat["title"] == film]
    for data in data_from_film:
        if data["title"] == film:
            length += data["length"]
            count += 1
    sum_length.append(length)
    episode_count.append(count)

file = open("summa.txt", "w")

for count, film in enumerate(film_list):
    file.write(f"{film} {sum_length[count]} {episode_count[count]}\n")