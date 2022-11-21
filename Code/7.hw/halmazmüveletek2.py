#Metszetek, amelyek az ismétlődésekben különbözhetnek
A = [1, 2, 99,99,99, 3,3, 5,5, "Python"]    #lista
B = ("Python", 99, 5,5,5, 42,42)    #sokasag
C = "Python 3"      #karakterlánc
D = {"Python", 99, 5, 42, "3"}      #készlet


M1 = [elem for elem in A if elem in B]
print("Metszet ismétlödésekkel(1) listában:", M1)
M2 = [elem for elem in B if elem in A]
print("Metszet ismétlödésekkel(2) listában:", M2)
M3 = {elem for elem in A if elem in B}
print("Metszet ismétlödések nélkül készletben:", M3)
M4 = list(M3)
print("Metszet ismétlödések nélküli listában:", M4)

#Különbségek, amelyek az ismétlödésekben eltérhetnek:
S = [elem for elem in A if elem not in B]
print("A-B ismétlödésekkel listában:", S)
S = [elem for elem in B if elem not in A]
print("B-A ismétlödésekkel listában:", S)
print()

#Készletek uniója készletként:
U = set(A) | set(B) | D
print("Készletek uniója készletként:", U)

#Készletek metszete készletként:
U = set(A) & set(B) & D
print("Készletek metszete készletként:", U)