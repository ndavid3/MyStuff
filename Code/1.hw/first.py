def main():
    txt = input("Adjon meg egy mondatot: \n")
    wl = {}

    for k in txt:
        if k in wl:
            wl[k] += 1
        else:
            wl[k] = 1

    print("Betűk gyakorisága:", wl)

    print("Fordítva: ", txt[::-1])

    rev = {}
    rev = txt.split()

    print("Listába rendezve szavanként: ", rev)


if __name__ == '__main__':
    main()