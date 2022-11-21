# befagyasztott készlet 
# iterálható, nem indexelhető, nem módositható

bejar = frozenset({1, 3, 42, 2.7, 5, 42, 42, 3.14})

for sorsz, elem in enumerate(bejar):
    if elem > 3 and elem < 4:
        kimen = True, elem, sorsz
        break
    else:
        kimen = False

print(kimen)