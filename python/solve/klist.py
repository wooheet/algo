# 리스트에서 자주 출현한 숫자 구하기
# 주사위를 굴려서 나온 숫자를 리스트에 순서대로 적은 값과 k를 입력받았을 때,
# 리스트에 자주 출현한 k개의 숫자를 리턴하는 코드를 작성해보세요.
# 예를들어, 주사위 던진 결과가 [3,2,3,1,2,5,3,6,2,4]이고, k가 2이면,
# 2가 세번, 3이 세번으로 자주 출현한 k (k=2)개의 숫자이므로 [2,3]을 출력합니다.
#
# 만약, 출현 횟수가 같은 숫자가 k개 이상 있을 경우, 출현 횟수가 높은 숫자부터 리스트에
# 포함시킵니다. 예를 들어, 주사위 던진 결과가 [1,1,1,2,2,3,3,4,4]이고, k가 3이면,
# [1,2,3] 또는 [1,2,4]을 출력합니다.

from collections import Counter


def top_k_frequent_number(nums, k):
    nums.sort()
    print([i[0] for i in Counter(nums).most_common(k)])

    num_map = {1:0,2:0,3:0,4:0,5:0,6:0}

    for num in nums:
        num_map[num] += 1

    ret = []

    while k > 0:
        max_freq = 0
        max_key = 0
        for key in num_map:
            if num_map[key] > max_freq:
                max_freq = num_map[key]
                max_key = key
        ret.append(max_key)
        del num_map[max_key]

        k -= 1

    print(ret)

    return ret


# nums = [1,1,2,1,3]
nums = [1,1,3,1,2]
k = 2

top_k_frequent_number(nums, k)