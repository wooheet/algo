from heapq import heappop, heappush, heapify


def cookies(k, A):
    heapify(A)

    answer = 0

    while True:
        if len(A) == 1 and A[0] < k:
            return -1

        if A[0] >= k:
            return answer
        else:
            print(A)
            a, b = heappop(A), heappop(A)
            print(A)
            print(a, b)
            new_one = a + 2 * b
            print(new_one)
            heappush(A, new_one)
            answer += 1


k = 9
A = [2, 7, 3, 6, 4, 6]
r = cookies(k, A)
print(r)

# https://www.daleseo.com/python-heapq/