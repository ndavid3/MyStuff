# lista: iterálható, módositható

bejar = [1, 2, 3, 4, 5, 6, 16]

for elem in bejar:
    if elem % 3 == 1 and elem > 5:
        kimen = True, elem
        break
    else:
        kimen = False

print(kimen)