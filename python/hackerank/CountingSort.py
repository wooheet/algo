def countingSort(arr):
    result = [0] * (max(arr) + 1)

    for i, x in enumerate(arr):
        result[x] += 1

    return result

    # return [arr.count(i) for i in range(max(arr)+1)]
    # return [arr.count(i) for i in range(100)]


arr = [1, 1, 3, 2, 1]
result = countingSort(arr)
print(result)

# i	arr[i]	result
# 0	1	[0, 1, 0, 0]
# 1	1	[0, 2, 0, 0]
# 2	3	[0, 2, 0, 1]
# 3	2	[0, 2, 1, 1]
# 4	1	[0, 3, 1, 1]
