from heapq import heappop, heappush, heapify


# def cookies(k, A):
#     smallest = []
#     iter_cnt = 0
#
#     while True:
#         for i in range(2):
#             a = min(A)
#             smallest.append(a)
#             A.remove(a)
#
#         result = smallest[0] + 2 * smallest[1]
#         A.insert(0, result)
#         A.sort()
#
#         iter_cnt += 1
#
#         if A[0] >= k:
#             break
#
#         smallest.clear()
#
#     return iter_cnt

def cookies(k, A):
    heapify(A)
    answer = 0

    while True:
        if len(A) == 1 and A[0] < k:
            return -1

        if A[0] >= k:
            return answer
        else:
            a, b = heappop(A), heappop(A)
            new_one = a + 2 * b
            heappush(A, new_one)
            answer += 1


k = 9
A = [2,7,3,6,4,6]
cookies(k, A)