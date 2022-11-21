diakok = frozenset( { ("Etel", 18, 4.2),("János", 17, 4.9), ("Viola", 19, 4.1) } )

def hason(elem):
    nev, kor, atlag = elem
    return atlag
    #return nev

ldiak = list(diakok)
ldiak.sort(key = hason)     #(key = hason, reverse = True)
print(ldiak)

ldiak2 = sorted(diakok, key = hason, reverse = True)
print(ldiak2)