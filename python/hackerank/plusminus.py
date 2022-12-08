from decimal import *


def plusMinus(arr):
    # Write your code here
    len_arr = len(arr)
    arr.sort()
    isZero = True

    try:
        split_index = arr.index(0)
        len_split_index = arr.count(0)
    except:
        isZero = False

        for i in range(100):
            try:
                split_index = arr.index(i)
                len_split_index = arr.count(i)
                split_num = i
                break
            except:
                pass

    if len_split_index != 1:
        if split_num != 0:
            len_p = len(arr[split_index:])
            len_n = len(arr[:split_index])
        else:
            len_p = len(arr[split_index + len_split_index:])
            len_n = len(arr[:split_index])
    else:
        if split_num != 0:
            len_p = len(arr[split_index:])
            len_n = len(arr[:split_index])
        else:
            len_p = len(arr[split_index + len_split_index:])
            len_n = len(arr[:split_index])



    p = '{:.6f}'.format(Decimal(len_p / len_arr))
    n = '{:.6f}'.format(Decimal(len_n / len_arr))
    z = '{:.6f}'.format(Decimal(len_split_index / len_arr if isZero else 0))
    result = f"{p}\n{n}\n{z}\n"

    print(result)
    return result


# arr = [-1,-1,0,1,1]
# arr = [-4, 3, -9, 0, 4, 1]
# arr = [1, 2, 3, -1, -2, -3, 0, 0]

# arr = [1, -2, -7, 9, 1, -8, -5]
arr = [55, 48, 48, 45, 91, 97, 45, 1, 39, 54, 36, 6, 19, 35, 66, 36, 72, 93, 38, 21, 65, 70, 36, 63, 39, 76, 82, 26, 67, 29, 24, 82, 62, 53, 1, 50, 47, 65, 67, 19, 66, 90, 77]
plusMinus(arr)
