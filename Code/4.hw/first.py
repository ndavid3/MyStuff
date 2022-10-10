class Team:
    def __init__(self, nev, pr, szk):
        self._nev = nev
        self._pr = pr
        self._szk = szk

    @property
    def nev(self):
        return self._nev

    @property
    def pr(self):
        return self._pr

    @property
    def szk(self):
        return self._szk

    @nev.setter
    def nev(self, ertek):
        self._nev = ertek


def kiir(ala):
    print("--Develpoer létrehozva--")
    print(ala.nev + " a " + ala.pr + "-en dolgozik " + ala.szk + " szerepkörben.")


def kiir2(nevk):
    if len(nevk) == 2:
        print(nevk[0] + " és " + nevk[1] + " dolgoznak egy projekten.")

    elif len(nevk) > 2:
        for i in range(0, len(nevk) - 2):
            print(nevk[i], end=', ')
        print(nevk[len(nevk) - 2] + " és " + nevk[len(nevk) - 1] + " dolgoznak egy projekten.")


def vizsg(k):
    nevk = []
    for i in range(0, len(k)-1):
        nevk.append(k[i].nev)
        for j in range(i+1, len(k)):
            if (k[i].pr == k[j].pr) and (k[j].nev not in nevk) and (k[i].nev != "1"):
                nevk.append(k[j].nev)
                k[j].nev = "1"
        kiir2(nevk)

        nevk = []


def peld():
    alk = []

    alk.append(Team("Ricsi", "SolArch", "Frontend"))
    kiir(alk[0])

    alk.append(Team("Angéla", "ZerTeng", "Tesztelő"))
    kiir(alk[1])

    alk.append(Team("Peti", "KefERP", "Backedn"))
    kiir(alk[2])

    alk.append(Team("Éva", "KefERP", "Frontend"))
    kiir(alk[3])

    print()
    vizsg(alk)


if __name__ == '__main__':
    peld()
