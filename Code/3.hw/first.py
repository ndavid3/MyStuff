def div():

    while 1:
        try:
            a = float(input("Enter 'a' value: "))
            b = float(input("Enter 'b' value: "))

            print(round(a/b, 3))

        except ZeroDivisionError:
            print("Zero division not allowed.")

        finally:
            print("Out of try except blocks.")

if __name__ == '__main__':
    div()
