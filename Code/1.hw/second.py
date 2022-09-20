def main():
    ln = int(input("Adjon meg egy számot és egy mértékegységet (cm/inch): \n"))
    tp = input()

    if tp == "cm":
        print(ln/2.54, "inches")
    elif tp == "inch":
        print(ln*2.54, "cm")
    else:
        print("Not correct unit!")

if __name__ == '__main__':
    main()