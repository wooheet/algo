def solution(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2

    # while a != b:
    #     answer += 1
    #     a, b = (a//2)+(a%2), (b//2)+(b%2)

    return answer

solution(8,4,7)
