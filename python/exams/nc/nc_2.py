# 종이 띠를 접어서 가장 큰 수를 만들려고 한다
# 종이 띠는 동일한 너비를 가진 칸으로 이루어져 있으며 각 칸에는 숫자가 적혀있다
# 칸과 칸 사이에는 구분선이 그어져 있고, 이 구분선을 따라 종이를 접을 수 있다
# 종이를 접어서 칸이 겹쳐지면 칸에 적힌 두 수 를 더한다
# 아래 그림은 종이 띠에 적힌 숫자가 [7,3,5,-2,9] 이고, 종이를 접을 수 있는 최대 횟수가 2회일 때, 종이를 접어 최댓값을 만드는 과정을 나타낸다.
#
# 화살표는 종이를 접는 방향을 나타내며, 화살표 중간에 있는 구분선을 따라 종이를 접는다

from itertools import combinations


def solution(paper, n):
    answer = 0
    paper_len = len(paper)
    half = int(paper_len / 2)

    # for i in range(half):
    #     if paper_len % 2 == 0:
    #         # 1. [10, 5, -2, 9]
    #         # 2. [5, 8, 9]
    #         # n = n-1
    #     else:
    #         # 1-1. [19, 3]
    #         # 2-1. [13, 9]
    #         # 2-2. [5, 17]
    #         print(paper[i], paper[-(i+1)])
    #         # n = n-1

    return answer


paper = [7, 3, 5, -2, 9]
n = 2


def climbStairs(n: int) -> int:
    c = [0]*(n+1)

    c[0] = 1
    c[1] = 2

    if n < 3:
        return c[n-1]

    for i in range(2, n):
        print(c)
        c[i] = c[i-1] + c[i-2]

    print(c[n-1])

    return c[n-1]

climbStairs(5)


# def cal(index, half):
    # last_index = (half * 2) - 1

    # [0,1] len > 2 [0,1], [-2,-1]
    # [0,3], [1,2]
    # 2n+1


    # 정진
    # 0+1 -> [10, 5, -2, 9]  -> [15, -2, 9]
    #                        -> [10, 5, 7]
    # 빠져나왔는데, result lenth가 3보다 크다 그리고 n을 모두 사용하지 않았으면?
    # 한번더 돌아
    # 0+3 / 1+2 -> [19, 3]

    # reverse
    # 0+1 -> [7, 3, 5, 7]    -> [10, 5, 7]
    #                        -> [7, 3, 12]
    # 0+3 / 1+2 -> [10, 12]


    # 0+5 / 1+4 / 2+3
    # 0+7 / 1+6 / 2+5 / 3+4
    # 0+9

    # for i, x in enumerate(paper):
    #     print(paper[i] + paper[-(i+2)])
    #
    #     i+(2i+1)
    #
    #     if (i+1) == half:
    #         break


# [10.-10] 1
# [1,2,4,8,16] 3
# [7,3,-7,5,-3] 2

solution(paper, n)
# print(solution(paper, n))