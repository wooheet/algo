def canJump(nums):
    if 0 not in nums:
        return True

    m = 0
    tmp = None

    for i, x in enumerate(nums):
        # print((i + 1), x)
        # print(nums[i+1:x])

        if nums[nums[i]] == 0:
            tmp = nums[(i+1):nums[i]]

            print(sum(tmp))
        else:
            print(tmp)





    print(tmp)

    m = max(tmp)
    i = nums.index(m)
    print(i)

    # while True:
    #     nums[:nums[i]]

# nums = [2, 3, 1, 1, 4]
nums = [3, 2, 1, 0, 4]
# nums = [3, 2, 1, 2, 1, 0, 4]
# nums = [3, 2, 3, 2, 1, 0, 4]
# nums = [3, 2, 3, 2, 2, 0, 4]
# nums = [3, 2, 4, 2, 1, 0, 4]
# nums = [3, 4, 4, 2, 1, 0, 4]

x = canJump(nums)
print(x)
