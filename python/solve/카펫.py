def solution(brown, yellow):
    answer = []
    nums = brown + yellow

    for n in range(brown // 2, 2, -1):
        for x in range(3, brown//2):
            if n >= x and (n * x) == nums:
                y = (n - 2) * (x - 2)
                b = nums - y
                if y == yellow and b == brown:
                    answer.append(n)
                    answer.append(x)
                    break

    return answer


# def solution(brown, red):
#     for i in range(1, int(red**(1/2))+1):
#         if red % i == 0:
#             if 2*(i + red//i) == brown-4:
#                 return [red//i+2, i+2]