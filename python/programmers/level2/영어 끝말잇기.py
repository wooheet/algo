def solution(n, words):
    # answer = []
    #
    # for i in range(len(words)):
    #     if words[i] in words[i+1:]:
    #         idx = (words[i+1:].index(words[i])) + (i+1)
    #
    #         div = divmod((idx+1), n)
    #
    #         if div[1] > 0:
    #             answer.append(div[1])
    #             answer.append(div[0]+1)
    #         else:
    #             answer.append(div[0])
    #             answer.append(n)
    #         break
    #     else:
    #         if i+1 < len(words) and words[i][-1] != words[i+1][0]:
    #
    #             div = divmod((i+2), n)
    #
    #             if div[1] > 0:
    #                 answer.append(div[1])
    #                 answer.append(div[0]+1)
    #             else:
    #                 answer.append(div[0])
    #                 answer.append(n)
    #             break
    # print(answer)
    #
    # return answer

    # answer = [0,0]
    # stack = [words[0]]
    #
    # for i in range(1, len(words)):
    #     if stack[-1][-1] == words[i][0] and words[i] not in stack:
    #         stack.append(words[i])
    #     else:
    #         answer[0] = (i % n) + 1
    #         answer[1] = i // n + 1
    #         break
    #
    # return answer

    for p in range(1, len(words)):
        if words[p][0] != words[p - 1][-1] or words[p] in words[:p]:
            return [(p % n) + 1, (p // n) + 1]
    else:
        return [0, 0]


n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
# words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tankt", "tanktt", "tanktttt", "tankt"]
# words = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
# words = ["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n, words))
