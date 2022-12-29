# 1. list에 0을 가지는 인덱스 추출
# 2. for 돌려 0을 가지는 인덱스 숫자 만큼 돌림
# 3. 역순으로 0 인덱스 숫자만큼 -1하여 숫자 추출
# 4. 0을 가지는 인덱스와 역순 인덱스 -(뺴기) 하여 추출되는 값이 크면 통과 아니면 못통과

def canJump(nums):
    # if 0 not in nums or \
    #         (len(nums) == 1 and 0 in nums):
    #     return True
    # else:
    #     idx = []
    #     result = False
    #
    #     while 0 in nums:
    #         i = nums.index(0)
    #         nums[i] = -1
    #         idx.append(i)
    #
    #     for index in idx:
    #         for i in range(index, 0, -1):
    #             if nums[i-1] - (index-(i-1)) <= 0:
    #                 pass
    #             else:
    #                 result = True
    #                 break
    # return result

    i = 0
    distance = 0

    while i <= distance:
        distance = max(distance, i + nums[i])
        if distance >= len(nums) - 1:
            return True
        i += 1

    return False

# nums = [2, 3, 1, 1, 4]
# nums = [3, 2, 1, 0, 4]
# nums = [3, 2, 1, 2, 1, 0, 4]
# nums = [3, 2, 3, 2, 1, 0, 4]
# nums = [3, 2, 3, 2, 2, 0, 4]
# nums = [3, 2, 4, 2, 1, 0, 4, 0]
nums = [3, 4, 4, 2, 1, 0, 4]
# nums = [0]
# nums = [2, 0]
# nums = [1, 1, 1, 0]

x = canJump(nums)
print(x)
