def beolvas():
    with open("playlist.csv", "r") as file:
        sor = file.readline()
        lista = []

        while sor:
            words = sor.split(";")
            nev = words[0]
            cim = words[1]
            mufaj = words[2]
            hossz = int(words[3])
            zenek = {"eloado": nev,
                     "cim": cim,
                     "mufaj": mufaj,
                     "hossz": hossz}
            lista.append(zenek)

            sor = file.readline()

    return lista


def teljes_hossz(ls):
    suma = 0
    for i in ls:
        suma += i.get("hossz")
    perc = suma / 60
    with open("02_hossz.txt", 'w') as ki:
        ki.write(str(perc))


def leghosszabb_rockzene(ls):
    maxh = -1
    with open("03_leghosszabb_rock.txt", 'w') as fout:
        for i in ls:
            if i.get("mufaj") == "rock":
                if i.get("hossz") > maxh:
                    cim = i.get("cim")

        fout.write(cim)


def leggyakoribb_mufaj(ls):
    with open("04_kedvenc_mufaj.txt", 'w') as fout:
        mufaj = {}
        for i in ls:
            if i.get("mufaj") not in mufaj:
                mufaj[i.get("mufaj")] = 1
            else:
                mufaj[i.get("mufaj")] += 1

        for key, value in mufaj.items():
            fout.write(str(key) + ";" + str(value) + "\n")

        maxdb = -1
        for key, value in mufaj.items():
            if value > maxdb:
                maxdb = value
                nv = key

        fout.write(nv.upper())

def zeneket_csoportosit(ls):
    with open("05_osszegzes.txt", 'w') as fout:
        eloadok = {}
        for i in ls:
            if i.get("eloado") not in eloadok:
                eloadok[i.get("eloado")] = i.get("hossz")
            else:
                eloadok[i.get("eloado")] += i.get("hossz")

        eloadok = dict(sorted(eloadok.items()))

        for key, value in eloadok.items():
            fout.write(str(key) + ";" + str(value) + "\n")


def zeneket_listaz(ls, eloadnev):
    k = eloadnev.lower()
    k = k.replace(" ", "_")
    boo = 0
    with open("06_" + str(k) + "_dalok.txt", 'w') as fout:
        for i in ls:
            if i.get("eloado").lower() == eloadnev.lower():
                boo = 1
                fout.write(i.get("cim") + ";" + i.get("mufaj") + ";" + str(i.get("hossz")) + "\n")

        if boo == 0:
            fout.write("Nincs ilyen eloado a lejatszasi listaban!")
        boo = 0


def zeneket_torol(ls, eloadoksor):
    with open("07_torolt.txt", 'w') as fout:
        for i in ls:
            if i.get("eloado") not in eloadoksor:
                fout.write(i.get("eloado") + ";" + i.get("cim") + ";" + i.get("mufaj") + ";" + str(i.get("hossz")) + "\n")


if __name__ == '__main__':
    k = beolvas()
    teljes_hossz(k)
    leghosszabb_rockzene(k)
    leggyakoribb_mufaj(k)
    zeneket_csoportosit(k)
    zeneket_listaz(k, "Imagine Dragons")

    trl = ["Imagine Dragons", "Boney M."]
    zeneket_torol(k, trl)