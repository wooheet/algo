# def solution(A):
#     A = set(A)
#
#     num = 1
#     while True:
#         if num not in A:
#             break
#
#         num += 1
#
#     return num
#
#
# A = [2, 3, 1, 5]
# solution(A)

def solution(A):

    print(len(A)+2)
    print(range(len(A) + 2))
    print(sum (range(len(A)+2)))

    print(sum(A))
    return sum (range(len(A)+2)) - sum(A)

A = [2, 3, 1, 5]
print(solution(A))