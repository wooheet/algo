def solution(m, n, board):
    x = []

    for i in board:
        x.append(list(i))
    print(x)

    point = 1
    while point != 0:
        x_list = []
        point = 0

        for i in range(m - 1):
            for j in range(n - 1):

                if x[i][j] == x[i][j + 1] == x[i + 1][j] == x[i + 1][j + 1] != '팡!':
                    x_list.append([i, j])
                    point += 1

        for i2 in x_list:
            i, j = i2[0], i2[1]
            x[i][j], x[i][j + 1], x[i + 1][j], x[i + 1][j + 1] = '팡!', '팡!', '팡!', '팡!'

        print(x_list)

        for i3 in range(m):
            for i in range(m - 1):
                for j in range(n):
                    if x[i + 1][j] == '팡!':
                        x[i + 1][j], x[i][j] = x[i][j], '팡!'

    cnt = 0
    for i in x:
        cnt += i.count('팡!')
    return cnt


# CCBDE
# AAADE
# AAABF
# CCBBF


# 아래 리스트가 공백이면 현재 위치에 있는 배열 컬럼 위치에서 빈 위치로 옮겨준다.


m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]

solution(m,n,board)