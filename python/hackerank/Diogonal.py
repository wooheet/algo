
# def diagonalDifference(arr):
#     len_arr = 3
#
#     result = 0
#
#     s1 = 0
#     for i in range(0, len(arr), 4):
#         s1 += arr[i]
#
#     for i in range(2, len(arr)-1, 2):
#         s1 -= arr[i]
#
#     print(abs(s1))

def diagonalDifference(arr):
    # Write your code here
    left_diagonal = 0
    right_diagonal = 0

    for i in range(len(arr[0])):
        left_diagonal = left_diagonal + arr[i][i]
        print(left_diagonal)
        right_diagonal = right_diagonal + arr[i][len(arr[0])-i-1]

    answer = abs(left_diagonal - right_diagonal)

    return answer


arr = [11, 2, 4,
        4, 5, 6,
        10, 8, -12]

# 4 - 19 = 15

diagonalDifference(arr)
