
def solution(x, y, z):

    # 동일(2) - 4,4,3 -> (+) -> 4 < 7
    # 4
    #[1] 4, 5
    #[2] 4
    #[3] 4


    # 동일(2) - 4,4,4 -> (+) -> 4 < 8
    # 4
    #[1] 4, 5
    #[2] 4, 5, 6
    #[3] 4, 5
    #[4] 4

    # 작을(1) - 8,5,3 -> (-) -> 8=8
    # 8
    #[1] 8, 7
    #[2] 8, 7, 6
    #[3] 8, 7, 6, 5

    # global max_result
    # answer = x
    # result = list()
    # result.append(x)
    #
    # for i in range(x, x+z):
    #     if x <= y:
    #         answer += 1
    #     else:
    #         answer -= 1
    #         result.append(answer)
    #
    # if x <= y:
    #     answer = answer - int(z/2)
    #     if answer != y:
    #         return -1
    #     return answer
    # else:
    #     if answer != y:
    #         return -1
    #     else:
    #         return max(result)

    answer = x
    result = list()
    result.append(x)

    if (y+z)%2 != 0:
        return -1
    for i in range(x, y+z):
        if x <= y:
            answer += 1
        else:
            answer -= 1
            result.append(answer)

    print(answer)

    if answer != y:
        return -1

    if x <= y:
        answer = answer - int(z/2)
        return answer
    else:
        return max(result)




    # if x <= y:
    #     answer = answer - int(z/2)
    #     if answer != y:
    #         return -1
    #     return answer
    # else:
    #     if answer != y:
    #         return -1
    #     else:
    #         return max(result)


    # print(x,y,z)
    # answer = x
    # result = list()
    # result.append(x)
    #
    # for i in range(x, y+z):
    #     if x <= y:
    #         answer += 1
    #     else:
    #         answer -= 1
    #         result.append(answer)
    #
    # if x <= y:
    #     answer = answer - int(z/2)
    #     return answer
    # else:
    #     return max(result)




x = 4
y = 4 # -> 목표 수
z = 3 # -> 이동 가능한 수




# x = 4
# y = 4 # -> 목표 수
# z = 4 # -> 이동 가능한 수

# x = 4
# y = 4 # -> 목표 수
# z = 6 # -> 이동 가능한 수
# 동일(3) - 4,4,6 -> (+) -> 4 < 10
# 4
#[1] 4, 5
#[2] 4, 5, 6
#[3] 4, 5, 6, 7
#[4] 4, 5, 6
#[5] 4, 5
#[6] 4


# x = 8
# y = 5
# z = 3


# x = 8
# y = 5
# z = 2

# x = 8
# y = 5
# z = 8

# x,y,z = 1892, 1896, 7
# 63910700 63910703 11
# 100000000 99999998 12
# 65913520 65913524 13
# 100000000 100000000 15
# 659076 759012 15

# 1892
#[1] 1892, 1893
#[2] 1892, 1893, 1894
#[3] 1892, 1893, 1894, 1895
#[4] 1892, 1893, 1894, 1895, 1896
#[5] 1892, 1893, 1894, 1895, 1896, 1897
#[6] 1892, 1893, 1894, 1895, 1896, 1897
#[7] 1892, 1893, 1894, 1895, 1896, 1897

print(solution(x,y,z))