# def solution(n, k, enemy):
#     answer = 0
#
#     half = n // 2
#
#     for i, x in enumerate(enemy):
#
#         if x > half:
#             k -= 1
#             continue
#
#         n -= x
#
#         if n < x or n <= 0:
#             answer = i + 1
#             break
#
#     if answer == 0:
#         answer = len(enemy)
#     print(answer)
#     return answer


import heapq


def solution(n, k, enemy):
    heap = []

    if len(enemy) == k:
        return len(enemy)

    for i in range(len(enemy)):
        if n >= enemy[i]:
            heapq.heappush(heap, -enemy[i])
            n -= enemy[i]
        else:
            if k > 0:
                if heap:
                    a = -heapq.heappop(heap)
                    k -= 1
                    if a > enemy[i]:
                        n += a - enemy[i]
                        heapq.heappush(heap, -enemy[i])
                    elif a == enemy[i]:
                        heapq.heappush(heap, -enemy[i])
                    else:
                        heapq.heappush(heap, -a)
                else:
                    k -= 1
            else:
                return i
    return len(enemy)


# n = 7
# k = 3
# enemy = [4, 2, 4, 5, 3, 3, 1]

n = 2
k = 4
enemy = [3, 3, 3, 3]


solution(n,k,enemy)