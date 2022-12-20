# #!/bin/python3
#
# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(L):
    max_so_far = max_ending_here = -2**31
    c_sum = 0
    max_neg = -2**31

    for i in range(len(L)):
        max_ending_here = max(L[i], max_ending_here + L[i])
        print("max_ending_here", max_ending_here)
        max_so_far = max(max_so_far, max_ending_here)
        print("max_so_far", max_so_far)
        if L[i] > 0:
            c_sum += L[i]
            print(c_sum)
        else:
            if L[i] > max_neg:
                max_neg = L[i]
    if c_sum == 0: # All values were negative so just pick the largest
        c_sum = max_neg
    print(' '.join(map(str, (max_so_far, c_sum))))
    return ' '.join(map(str, (max_so_far, c_sum)))


arr = [1, 2, 3, 4]
# arr = [2, -1, 2, 3, 4, -5]
maxSubarray(arr)


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     t = int(input().strip())
#
#     for t_itr in range(t):
#         n = int(input().strip())
#
#         arr = list(map(int, input().rstrip().split()))
#
#         result = maxSubarray(arr)
#
#         fptr.write(' '.join(map(str, result)))
#         fptr.write('\n')
#
#     fptr.close()
