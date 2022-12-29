def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)


def solution(s):
    return min(compress(s, tok_len) for tok_len in list(range(1, len(s)//2 + 1)) + [len(s)])

print(list(range(1, len("aabbaccc")//2 + 1)) + [len("aabbaccc")])

# def solution(s):
#     answer = 0
#
#
#     i = 1
#     is_pass = False
#
#     while len(s) % i == 0:
#         for c in range(len(s)):
#             print(i*c, i*(c+1), s[i*c:i*(c+1)])
#             print(i*(c+1), i*(c+2), s[i*(c+1):i*(c+2)])
#             print()
#             if is_pass:
#                 is_pass = False
#                 pass
#
#             if s[i*c:i*(c+1)] == s[i*c:i*(c+1)]:
#                 answer += f'{i+1}' + s[i*c:i*(c+1)]
#                 is_pass = True
#             else:
#                 answer +=
#
#             if i*(c+1)+1 > len(s): break
#         print()
#         i += 1
#
#     return answer

s = "aabbaccc"
# s = "ababcdcdababcdcd"
# s = "abcabcdede"
# s = "abcabcabcabcdededededede"
# s = "xababcdcdababcdcd"
solution(s)
