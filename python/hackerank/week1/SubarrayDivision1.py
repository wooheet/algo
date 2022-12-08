from functools import reduce
from itertools import combinations


def birthday(s, d, m):
    # m개 만큼 더해서 d의 수를 구하라

    # result = list()
    #
    # for i in list(combinations(s, m)):
    #     if sum(i) == d:
    #         result.append(i)
    #
    # return len(set(result))

    cnt = 0

    for i in range(len(s) - m + 1):
        subset = sum(s[i:i + m])
        if subset == d:
            cnt += 1

    return cnt


# s,d,m = [2,2,1,3,2], 4, 2
s,d,m = [5, 1, 2, 4, 4, 2, 4, 2, 2, 5, 1, 4, 3, 1, 1, 1, 2, 1, 4, 1], 18, 6
print(birthday(s, d, m))
