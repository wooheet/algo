from itertools import combinations


def solution(cost, x):
    # combi = list()

    result = list()

    for i in range(1, len(cost)+1):
        for c in combinations(cost, i):

            if sum(c) <= x:
                # combi.append(list(c))

                combi_index = [cost.index(j) for j in list(c)]
                print(list(c))
                cnt = [2**i for i in combi_index]
                result.append(sum(cnt))




    # for r in combi:
    #     combi_index = [cost.index(j) for j in r]
    #     cnt = [2**i for i in combi_index]
    #     # print(cnt)
    #     result.append(sum(cnt))

    max_cnt = max(result)
    # print(result)
    print(max_cnt % (10**9 + 7))
    return max_cnt % (10**9 + 7)


# cost = [10, 20, 14, 40, 50]
# x = 70 # 예산

# cost = [3,4,1]
# x = 8

# cost = [19, 78, 27, 18, 20]
# x = 25

cost = [2, 5, 6, 25, 22, 21, 7, 9, 7, 22]
x = 95

def gen_combinations(arr, n):
    result =[]

    if n == 0:
        return [[]]

    for i in range(0, len(arr)):
        elem = arr[i]
        rest_arr = arr[i + 1:]
        for C in gen_combinations(rest_arr, n-1):
            result.append([elem]+C)

    return result


solution(cost, x)