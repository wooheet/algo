lower = 2
upper = 10000
prime = [i for i in range(lower, upper + 1) if all(i % j != 0 for j in range(2, i))]

def waiter(number, n, q):
    A = [number]
    B = []
    for i in range(q):
        A_pile = []
        B_pile = []
        while len(A[i]) != 0:
            n = A[i].pop()
            if n%prime[i] == 0:
                B_pile.append(n)
            else:
                A_pile.append(n)
        A.append(A_pile)
        B.append(B_pile)
    print(A, B)
    for i in range(len(B)):
        if B[i] != []:
            print(*B[i][::-1], sep="\n")
    for i in range(len(A)):
        if A[i] != []:
            print(*A[i][::-1], sep="\n")

number = [2,3,4,5,6,7]
q = 3

print(waiter(number, len(number), q))