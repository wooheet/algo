def solution(X, Y, D):
    t = Y-X

    if t%D == 0:
        return t//D
    else:
        return t//D + 1


X = 101
Y = 888
D = 30

print(solution(X,Y,D))

# X=현재위치, Y위치까지 도달하기 위해서 D의 길이만큼 점프를 몇번 하면 되는지를 구하는 문제이다.