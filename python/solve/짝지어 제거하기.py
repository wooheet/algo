def solution(s):
    answer = [s[0]]

    for i in range(1,len(s)):
        # if not answer:
        #     answer.append(i)
        # else:
        if answer[-1] == s[i]:
            answer.pop()
        else:
            answer.append(s[i])

    if answer:
        return 0
    else:
        return 1