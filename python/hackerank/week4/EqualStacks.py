from collections import deque


def equalStacks(h1, h2, h3):
    # for i in range(len(h1)):
    #     for j in range(len(h2)):
    #         if sum(h1[i:]) == sum(h2[j:]):
    #             for k in range(len(h3)):
    #                 if sum(h2[j:]) == sum(h3[k:]):
    #                     print(sum(h3[k:]))
    #                     return sum(h3[k:])
    #                 else:
    #                     pass
    #         else:
    #             pass
    # return 0

    l1 = sum(h1)
    l2 = sum(h2)
    l3 = sum(h3)
    while l1 != 0 and l2 != 0 and l3 != 0 and (l1 != l2 or l2 != l3):
        if max(l1, l2, l3) == l1:
            l1 = l1 - h1[0]
            h1.pop(0)
        elif max(l1, l2, l3) == l2:
            l2 = l2 - h2[0]
            h2.pop(0)
        else:
            l3 = l3 - h3[0]
            h3.pop(0)
    else:
        if l1 == l2 and l2 == l3:
            return l1
        else:
            return 0


h1 = [3, 2, 1, 1, 1]
h2 = [4, 3, 2]
h3 = [1, 1, 4, 1]

# h1 = [1, 1, 1, 1, 2]
# h2 = [3, 7]
# h3 = [1, 3, 1]

equalStacks(h1, h2, h3)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     first_multiple_input = input().rstrip().split()
#
#     n1 = int(first_multiple_input[0])
#
#     n2 = int(first_multiple_input[1])
#
#     n3 = int(first_multiple_input[2])
#
# #     STDIN       Function
# # -----       --------
# # 5 3 4       h1[] size n1 = 5, h2[] size n2 = 3, h3[] size n3 = 4
# # 3 2 1 1 1   h1 = [3, 2, 1, 1, 1]
# # 4 3 2       h2 = [4, 3, 2]
# # 1 1 4 1     h3 = [1, 1, 4, 1]
# # stack에 넣고 동일한 길이가 되도록 STACK의 값을 빼서 길이의 값을 반환
#
#     h1 = list(map(int, input().rstrip().split()))
#
#     h2 = list(map(int, input().rstrip().split()))
#
#     h3 = list(map(int, input().rstrip().split()))
#
#     result = equalStacks(h1, h2, h3)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()
