# 문자열 source가 매개변수로 주어진다.
# 다음과 같은 방식을 통해 source로 부터 새로운 문자열을 만들어 return 하도록 solution 함수를 완성해 주세요.
#
# 1. 새로운 빈 문자열 dest를 만듦
# 2. source가 빈 문자열인 경우, dest를 return하고 과정을 종료
# 3. source에 있는 모든 알파벳을 종류별로 1개씩만 제거한 뒤 해당 알파벳들을 dest의 맨 뒤에 알파벳 순서대로 이어 붙인다.
# 4. 2번 과정으로 돌아온다.
#
# execute     “”
# “ee”       xcute -> cetux
# “e”        cetux+e
#            cetuxe+e

# cucumber     ""
# "cu"         cumber -> bcemru
# "u"          bcemru+c
# ""           bcemruc+u -> bcemrucu


# bbaabd       ""
# bba          "abd"    'a', 'b', 'd'
# b            "abdab"  'a', 'b'
#              "abdab"  'b'

# dup = [x for i, x in enumerate(l) if x in l[:i]]
# dup_sort = sorted(dup)


def solution(str):
    source = list(str)
    dest = list()
    find_dup(source, dest, len(dest))

    return ''.join(dest)


def find_dup(source, dest, n):
    if len(source) == 0:
        return

    dup = list()

    for i in range(len(source)):
        if source[i] in source[:i]:
            dup.append(source[i])
        else:
            source.sort()
            dest.append(source[i])

    find_dup(dup, dest, len(dest))

# str = "execute"
str = "cucumber"
# str = "bbaabd"
# str = "bbaaabbd"

print(solution(str))