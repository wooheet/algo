def solution(s):
    char = s[0]
    answer = []

    for i in range(1, len(s)):
        if s[i] not in char:
            char += s[i]
        else:
            answer.append(char)
            char = s[i]

    print(len(max(answer)))




s = "abcabcaa"
# s = "bbbbb"
# s = "pwwkew"

solution(s)

def solution(n, arr1, arr2):

    ret = []
    for i in range(n):
        print(i)
        ret.append(i * (arr2[i] - arr1[i]))

    print(ret)

solution(4,[2,3,1,2], [3,1,1,2])


# [1,2,3], [10,10,10]