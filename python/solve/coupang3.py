# def solution(n, arr1, arr2):
#     arr1.sort(reverse=True)
#     arr2.sort()
#
#     ret = []
#     k = 1
#     print(arr1)
#     print(arr2)
#
#     for i in range(len(arr1)):
#         r = k * (arr2[i] - arr1[i])
#         # ret.append(r)
#         ret.append(r)
#         k += 1
#
#     print(ret)
#     print(sum(ret))
#     print(sum(ret) % (10**9 + 7))
#
#     return sum(ret)
#
# # solution(4,[2,1,3,4], [2,3,2,3])
# # solution(4,[3,1,2,4], [2,3,2,3])
# solution(4,[3,2,2,3], [3,1,2,4])
# # solution(3,[1,2,3], [10,10,10])


import re


# def solution(s):
#     n = []
#     sc = ""
#     ret = ""
#     open = False
#
#     for i, x in enumerate(s):
#
#         numbers = re.findall("\d+", x)
#         if numbers:
#             n.append(x)
#
#         if len(n) > 0:
#             if numbers:
#                 n.append(x)
#                 pass
#
#             if open and x != ']':
#                 sc += x
#
#             if x == '[':
#                 open = True
#                 pass
#
#             if x == ']':
#                 for r in range(int(n[-1])):
#                     ret += sc
#
#                 n = []
#                 open = False
#                 sc = ""
#         else:
#
#             ret += x
#
#     print(ret)


def solution(s):
    n = []
    ret = ""
    c = []
    open = False

    for i, x in enumerate(s):
        numbers = re.findall("\d+", x)
        if numbers:
            n.append(x)
            pass

        if open and not numbers and x != '[' and x != ']':
            c.append(x)
            pass

        if x == '[':
            open = True
            pass

        if x == ']':
            open = False
            temp = ""
            for r in range(int(n[-1])):
                if len(ret) > 0:
                    ret
                temp += c[-1]
            c[-1] = temp
            ret = "".join(c)
            pass






# def solve(n, sc, ret, open):



# s = "3[a]2[bc]"
# "aaabcbc"

s = "3[a2[c]]"
# "accaccacc"
#
# s = "2[abc]3[cd]ef"
# "abcabccdcdcdef"
#
# s = "abc3[cd]xyz"
# "abccdcdcdxyz"

solution(s)