A = [54, 76, 23, 45, 21, 5, 67, 22, 12, 64, 26, 59, 82, 99]

n = len(A)
for k in range(0, n):
    for i in range(1, n-k):
        if A[i-1] > A[i]:
            A[i], A[i-1] = A[i-1], A[i]

print(A)