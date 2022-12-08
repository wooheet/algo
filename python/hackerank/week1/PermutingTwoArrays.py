
def twoArrays(k, A, B):
    result = False

    A.sort()
    B.sort(reverse=True)

    print(A)
    print(B)

    for a, b in zip(A, B):
        if a + b >= k:
            result = True
        else:
            result = False
            break

    return "YES" if result else "NO"




# A, B = [0,1], [0,2]
# k = 1

# A, B = [2, 1, 3], [7, 8, 9]
# k = 10

A, B = [1, 2, 2, 1], [3, 3, 3, 4]
k = 5
print(twoArrays(k, A, B))