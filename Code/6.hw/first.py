import string
magh = "aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ\n"

with open("hazi.txt", "r", encoding='UTF-8') as f:
    with open("ki.txt", "w", encoding='UTF-8') as fout:
        sor = f.readline()
        i = 1
        sor = sor.translate(str.maketrans('', '', string.punctuation))

        for k in sor:
            if k in magh:
                sor = sor.replace(k, "")

        while sor:
            sor = f.readline()
            if sor.isspace():
                continue
            i += 1
            sor = sor.translate(str.maketrans('', '', string.punctuation))
            for k in sor:
                if k in magh:
                    sor = sor.replace(k, "")
            if i % 3 == 0:
                fout.write(sor + "\n")
