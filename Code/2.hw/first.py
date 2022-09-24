def main():
    print("Adja meg a háromszög három oldalát cm-ben: ")
    a = float(input("a oldal (cm): "))
    b = float(input("b oldal (cm): "))
    c = float(input("c oldal (cm): "))

    if (a + b > c) and (a + c > b) and (c + b > a):
        print("A(z) " + str(a) + ", " + str(b) + " és " + str(c) + " oldalú háromszög szerkeszthető.")

    else:
        print("A(z) " + str(a) + ", " + str(b) + " és " + str(c) + " oldalú háromszög NEM szerkeszthető.")

if __name__ == '__main__':
    main()
