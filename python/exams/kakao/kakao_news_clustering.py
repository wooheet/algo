# isdisjoint() - 두 집합이 공통 원소를 갖지 않는가?
# issubset() - 부분집합(subset)인가?
# issuperset() - 확대집합(superset)인가?

# union() - 합집합을 만들어 리턴
# update() - 합집합을 만들어 원본 데이터를 갱신(수정)
# difference() - 차집합을 만들어 리턴
# intersection() - 교집합을 만들어 리턴


import re
from collections import Counter

def solution(str1, str2):
    l_str1 = list(str1)
    l_str2 = list(str2)

    r_str1 = make(l_str1)
    r_str2 = make(l_str2)

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


def solution2(str1, str2):
    # 소문자로 변경
    str1, str2 = str1.lower(), str2.lower()

    # 문자열 조각들 만들기
    str1_set = list(str1[i:i + 2] for i in range(len(str1) - 1) if str1[i:i + 2].isalpha())
    str2_set = list(str2[i:i + 2] for i in range(len(str2) - 1) if str2[i:i + 2].isalpha())

    # 문자열 조각들 세기
    str1_counter, str2_counter = Counter(str1_set), Counter(str2_set)
    print(str1_counter)
    print(str2_counter)
    len_inter = sum((str1_counter & str2_counter).values())  # 교집합 개수
    len_union = sum((str1_counter | str2_counter).values())  # 합집합 개수

    return 65536 if len_union == 0 and len_inter == 0 else int(len_inter / len_union * 65536)

import re
import math

def solution3(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    # print(str2)

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)


# str1 = 'FRANCE'
# str2 = 'french'

str1 = "handshake"
str2 = "shake hands"

# str1 = '123'
# str2 = '234'
solution(str1, str2)
solution2(str1, str2)
print(solution3(str1, str2))





