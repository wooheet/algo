def miniMaxSum(arr):
    arr.sort()
    print(f"{sum(arr[:4])} {sum(arr[-4:])}")


arr = [1, 2, 3, 4, 5]
# arr = [9, 1, 3 ,5,7]
miniMaxSum(arr)