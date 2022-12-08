# import numpy as np
from functools import reduce


def lonelyinteger(a):
    result = 0

    for i in a:
        result = result ^ i
        print(result)

    # 0 ^ 1: 1
    # 1 ^ 2: 3
    # 3 ^ 3: 0
    # 0 ^ 4: 4
    # 4 ^ 3: 7
    # 7 ^ 2: 5
    # 5 ^ 1: 4

    # lonely_integer = reduce(lambda x, y: x ^ y, a)
    # print(lonely_integer)

    return result

a = [1,2,3,4,3,2,1]
lonelyinteger(a)

