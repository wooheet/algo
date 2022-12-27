# def solution(s):
#     stack = list(s)
#     new_stack = []
#
#     for i in range(len(s)):
#         new_stack.append(stack.pop())
#
#         if len(new_stack) >= 2 and new_stack[-1] == new_stack[-2]:
#             new_stack.pop()
#             new_stack.pop()
#
#     if len(new_stack) == 0:
#         return 1
#     else:
#         return 0


# def solution(s):
#     answer = [s[0]]
#
#     for i in range(1, len(s)):
#         if answer[-1] == s[i]:
#             answer.pop()
#         else:
#             answer.append(s[i])
#
#     return not(answer)


# def solution(s):
#     answer = [s[0]]
#
#     for i in range(1, len(s)):
#         if answer[-1] == s[i]:
#             answer.pop()
#         else:
#             answer.append(s[i])
#
#     if answer:
#         return 0
#     else:
#         return 1


def solution(s):
    answer = []

    for i in s:
        if not answer:
            answer.append(i)
        else:
            if answer[-1] == i:
                answer.pop()
            else:
                answer.append(i)

    if answer:
        return 0
    else:
        return 1


# print(solution('cbaabaac'))
print(solution('baabaa'))
