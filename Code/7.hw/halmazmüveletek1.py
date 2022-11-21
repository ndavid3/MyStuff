A = [1, 2, 99,99,99, 3,3, 5,5, "Python"]    #lista
B = ("Python", 99, 5,5,5, 42,42)    #sokasag
C = "Python 3"      #karakterlánc
D = {"Python", 99, 5, 42, "3"}      #készlet

print("Lista:", A, "\nSokaság", B, "\nKarakterlánc:", C, "\nKészlet:", D, "\n")

#Tartalmazás:
print("Tartalmazás:")
van = "t" in C
print(van)
print(99 in A)
print("Python" in B)
print("Python" in C)
print(2016 in A)
print()

#Két lista uniója:
U1 = A + list(B)
print("Unió listaként: ", U1)
U2 = set(U1)    #U2 = set(A + list(B))
print("Unió készletként: ", U2)
print()