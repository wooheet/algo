from itertools import combinations


def icecreamParlor(m, arr):

    for i in range(len(arr)):
        for j, x in enumerate(arr[i+1:]):
            sum = arr[i] + x
            if m == sum:
                print(i+1, (i+1)+(j+1))
                return

    # for i in combinations(arr, 2):
    #     print(i)
        # print(sum(i))



arr = [1, 4, 5, 3, 2]
# arr=[2, 2, 4, 3]
icecreamParlor(4, arr)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     t = int(input().strip())
#
#     for t_itr in range(t):
#         m = int(input().strip())
#
#         n = int(input().strip())
#
#         arr = list(map(int, input().rstrip().split()))
#
#         result = icecreamParlor(m, arr)
#
#         fptr.write(' '.join(map(str, result)))
#         fptr.write('\n')
#
#     fptr.close()
