import heapq


def solution(n, k, enemy):
    q = enemy[:k]

    heapq.heapify(q)
    print(q)
    print()
    for idx in range(k, len(enemy)):

        n -= heapq.heappushpop(q, enemy[idx])
        print(q)
        print(n)
        if n < 0:
            print("result", idx)
            return idx

    return len(enemy)


n = 7  # 병사 수
k = 3  # 무적
enemy = [4, 2, 4, 5, 3, 3, 1]

# n = 2
# k = 4
# enemy = [3, 3, 3, 3]


r = solution(n, k, enemy)
# print(r)
