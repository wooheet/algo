from decimal import *


def plusMinus(arr):
    # Write your code here
    len_arr = len(arr)
    arr.sort()
    isZero = True

    try:
        zero = arr.index(0)
        len_zero = arr.count(0)
    except:
        isZero = False

        for i in range(100):
            try:
                zero = arr.index(i)
                len_zero = arr.count(i)
                break
            except:
                pass

    if len_zero != 1:
        len_p = len(arr[zero:])
        len_n = len(arr[:zero])

    else:
        len_p = len(arr[zero + len_zero:])
        len_n = len(arr[:zero])

    p = '{:.6f}'.format(Decimal(len_p / len_arr))
    n = '{:.6f}'.format(Decimal(len_n / len_arr))
    z = '{:.6f}'.format(Decimal(len_zero / len_arr if isZero else 0))

    return f"{p}\n{n}\n{z}\n"


# arr = [-1,-1,0,1,1]
# arr = [-4, 3, -9, 0, 4, 1]
# arr = [1, 2, 3, -1, -2, -3, 0, 0]
arr = [1, -2, -7, 9, 1, -8, -5]
print(plusMinus(arr))
