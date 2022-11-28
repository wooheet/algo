from collections import deque


def solution(que1, que2):
    queSum = (sum(que1) + sum(que2))

    if queSum % 2:
        return -1
    target = queSum // 2

    n = len(que1)
    start = 0
    end = n - 1
    ans = 0

    cur = sum(que1)
    que3 = que1 + que2
    while cur != target:
        if cur < target:
            end += 1
            if end == n * 2:
                return -1
            cur += que3[end]
        else:
            cur -= que3[start]
            start += 1
        ans += 1
    return ans


queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]

r = solution(queue1, queue2)
print(r)