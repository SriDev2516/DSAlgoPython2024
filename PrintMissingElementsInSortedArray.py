A = [6, 7, 8, 9, 11, 12, 15, 16, 17, 18, 19]

diff = A[0]-0

for i in range(len(A)):
    if A[i]-i != diff:
        while diff < A[i]-i:
            print(i+diff, end=", ")
            diff += 1


