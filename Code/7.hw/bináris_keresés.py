def binkeres():
    A = [2, 5, 6, 8, 13, 32, 42, 50, 53, 62, 66, 70, 80, 89, 91]
    szm = 70

    n = len(A)
    also = 0
    felso = n-1

    while(also <= felso):
        kozep = (also + felso) // 2
        if szm < A[kozep]:
            felso = kozep - 1
        elif szm > A[kozep]:
            also = kozep + 1
        else:
            ki = True, szm
            break

    else:
        ki = False
    
    return ki

if __name__ == '__main__':
    print(binkeres())