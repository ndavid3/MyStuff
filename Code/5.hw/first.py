rend = "{0:>4}{1:>4}{2:>4}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}{10:>4}{11:>4}"

print(end="    ")
print(rend.format("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"))

print(end="  :")
for i in range(1, 50):
    print(end="-")

print()
for i in range(1,13):
    if i <= 9:
        print(i, ":", end=" ")
    else:
        print(i, ":", end="")

    print(rend.format(i, i * 2, i * 3, i * 4, i * 5, i * 6, i * 7, i * 8, i * 9, i * 10, i * 11, i * 12))
