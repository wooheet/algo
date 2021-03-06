# def lengthOfLongestSubstring(s: str) -> int:
    # length = len(s)
    # if length <= 1:
    #     return length
    #
    # L, R = 0, 0
    # cur_s = set()
    # cur_s.add(s[L])
    # max_length = cur_length = 1
    #
    # while R < length:
    #     R += 1
    #     while L < R < length:
    #         if s[R] in cur_s:
    #             while s[L] != s[R]:
    #                 cur_s.remove(s[L])
    #                 L += 1
    #                 cur_length -= 1
    #             cur_s.remove(s[L])
    #             L += 1
    #             cur_length -= 1
    #
    #         cur_s.add(s[R])
    #         R += 1
    #         cur_length += 1
    #         max_length = max(max_length, cur_length)
    #
    # return max_length

def lengthOfLongestSubstring(s: str) -> int:
    max_length = start = 0
    hash_table = {}

    for idx, c in enumerate(s):
        if c in hash_table.keys() and hash_table[c] >= start:
            start = hash_table[c] + 1
        else:
            max_length = max(max_length, idx - start + 1)

        hash_table[c] = idx

    return max_length


# s = "abcabcbb"
# s = "aaaabc"
# s = "asdfas"
# s = "asxbcx"
# s = "tmmzuxt"
s = "aas"
# s = "ass"
# s = "abcabc"
print(lengthOfLongestSubstring(s))
