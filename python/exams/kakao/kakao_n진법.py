#재귀함수 이용 - 10진수를 n진수로

def convert(n, base):
    arr = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return arr[r]
    else:
        return convert(q, base) + arr[r]


def solution(n, t, m, p):
    answer = ''
    test = ''

    for i in range(m*t):
        test += convert(i, n)

    print(test) # [0],[1],[10],[11],[100],[101],[110],[111]

    while len(answer) < t:
        answer += test[p-1]
        p += m

    return answer

r = solution(2, 4, 2, 1)
print(r)


# 10,2  0
# 5,2   1
# 2,2   0
# 1,2   1
#1010