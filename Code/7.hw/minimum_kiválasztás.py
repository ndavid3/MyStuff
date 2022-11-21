bejar = [10, 1, 5, 0.2, 3]
print(min(bejar))

#_________________________

diakok = [ ("János", 17, 4.9), ("Etel", 18, 4.2), ("Viola", 19, 4.1) ]

def hason(elem):
    nev, kor, atlag = elem
    return atlag
    #return elem[2]
    #return nev

print(min(diakok, key = hason))