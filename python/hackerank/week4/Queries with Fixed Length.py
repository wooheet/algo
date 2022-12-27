def solve(arr, queries):
    result = []
    result2 = []
    for query in queries:
        n = query-1
        result.append(min(arr[n:]))

        for i in range(len(arr)-n):
           result2.append(arr[i:i+query])

    print(result)
    print(result2)


# arr = [2,3,4,5,6]
arr = [33, 11, 44, 11, 55]
# queries = [2,3]
# queries = [1,2,3,4,5]
queries = [2]
solve(arr, queries)