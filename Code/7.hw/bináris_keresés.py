def binkeres():
    A = [2, 5, 6, 8, 13, 32, 42, 50, 53, 62, 66, 70, 80, 89, 91]
    szm = 70

    lep = 0
    n = len(A)
    also = 0
    felso = n-1

    while(also <= felso):
        kozep = (also + felso) // 2
        if szm < A[kozep]:
            lep += 1
            felso = kozep - 1
        elif szm > A[kozep]:
            lep += 1
            also = kozep + 1
        else:
            lep += 1
            ki = True, szm
            break

    else:
        ki = False

    if ki != False:
        print(str(ki) +", a " + str(lep) + " lépésben találta meg" + ", alsó: " + str(also) + ", felsö: " + str(felso) +", a k értéke: " + str(kozep))
    else:
        print("Nem találta meg")
    

if __name__ == '__main__':
    binkeres()