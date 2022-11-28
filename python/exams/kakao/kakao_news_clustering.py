# isdisjoint() - 두 집합이 공통 원소를 갖지 않는가?
# issubset() - 부분집합(subset)인가?
# issuperset() - 확대집합(superset)인가?
# union() - 합집합을 만들어 리턴
# update() - 합집합을 만들어 원본 데이터를 갱신(수정)
# difference() - 차집합을 만들어 리턴
# intersection() - 교집합을 만들어 리턴


import re

def solution(str1, str2):
    p = re.compile('[a-z]+')

    answer = 0

    l_str1 = list(str1)
    l_str2 = list(str2)

    tmp_str1 = list()
    tmp_str2 = list()

    # 각각 {FR, RA, AN, NC, CE}, {FR, RE, EN, NC, CH}가 되며, 교집합은 {FR, NC}, 합집합은 {FR, RA, AN, NC, CE, RE, EN, CH}

    for i in range(len(l_str1)):
        for i in l_str2:
            if len(p.findall(i)):

                tmp_str1.append()


    return answer


solution('FRANCE', '=french')