# https://leetcode.com/problems/longest-happy-string/
# https://github.com/knhngchn/leetcode-practice/blob/master/Python/longest-happy-string.py

# A string is called happy if it does not have any of the strings 'aaa', 'bbb' or 'ccc' as a substring.
# Given three integers a, b and c, return any string s, which satisfies following conditions:
# s is happy and longest possible.
# s contains at most a occurrences of the letter 'a', at most b occurrences of the letter 'b' and at most c occurrences of the letter 'c'.
# s will only contain 'a', 'b' and 'c' letters.
# If there is no such string s return the empty string "".


def valid(s, c):
    return len(s) < 2 or not (s[-1] == c and s[-2] == c)


def solution(A, B, C):
    s = ""
    x, y, z = [A, 'a'], [B, 'b'], [C, 'c']

    while x[0] or y[0] or z[0]:
        x, y, z = sorted([x, y, z], reverse=True)
        if x[0] and valid(s, x[1]):
            s += x[1]
            x[0] -= 1
        elif y[0] and valid(s, y[1]):
            s += y[1]
            y[0] -= 1
        elif z[0] and valid(s, z[1]):
            s += z[1]
            z[0] -= 1
        else:
            return s
    return s


if __name__ == '__main__':
    a, b, c = 1, 1, 7
    print(solution(a, b, c))
    # assert solution(a, b, c) == "ccaccbcc"

    # a, b, c = 2, 2, 1
    # print(solution(a, b, c))
    # assert solution(a, b, c) == "aabbc"

    # a, b, c = 7, 1, 0
    # print(solution(a, b, c))
    # assert solution(a, b, c) == "aabaa"
