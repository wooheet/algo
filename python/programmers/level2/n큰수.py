from heapq import heapify, heappop


def nth_smallest(nums, n):
    heapify(nums)

    nth_min = None
    for _ in range(n):
        nth_min = heappop(nums)

    return nth_min


nums = [10,2,11,4,15]

print(nth_smallest(nums, 5))