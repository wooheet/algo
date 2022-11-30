# isdisjoint() - 두 집합이 공통 원소를 갖지 않는가?
# issubset() - 부분집합(subset)인가?
# issuperset() - 확대집합(superset)인가?

# union() - 합집합을 만들어 리턴
# update() - 합집합을 만들어 원본 데이터를 갱신(수정)
# difference() - 차집합을 만들어 리턴
# intersection() - 교집합을 만들어 리턴


import re


def solution(str1, str2):
    l_str1 = list(str1)
    l_str2 = list(str2)

    r_str1 = make(l_str1)
    r_str2 = make(l_str2)

    print(r_str1)
    print(r_str2)

    s_s1 = set(r_str1)
    s_s2 = set(r_str2)

    inter_section = s_s1.intersection(s_s2)
    union = s_s1.union(s_s2)

    jacard = len(inter_section) / len(union)

    if 0 < jacard or 1 > jacard:
        return 65536

    answer = jacard * 65536

    return int(answer)


def make(source):
    p = re.compile('[a-zA-Z]+')

    make_str_list = list()

    for i in range(len(source)):
        if len(p.findall(source[i])):
            item = source[i:i + 2]
            join_str = ''.join((item)).upper()

            if len(join_str.strip()) == 2:
                make_str_list.append(join_str)

    return make_str_list


# str1 = 'FRANCE'
# str2 = 'french'

str1 = "handshake"
str2 = "shake hands"

# str1 = '123'
# str2 = '234'

print(solution(str1, str2))





