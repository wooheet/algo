from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    answer = []
    info_dict = {}

    for i in range(len(info)):
        infol = info[i].split()  # info안의 문자열을 공백을 기준으로 분리
        mykey = infol[:-1]  # info의 점수제외부분을 key로 분류
        myval = infol[-1]  # info의 점수부분을 value로 분류

        for j in range(5):  # key들로 만들 수 있는 모든 조합 생성
            for c in combinations(mykey, j):
                tmp = ''.join(c)
                if tmp in info_dict:
                    info_dict[tmp].append(int(myval))  # 그 조합의 key값에 점수 추가
                else:
                    info_dict[tmp] = [int(myval)]

    for k in info_dict:
        info_dict[k].sort()  # dict안의 조합들을 점수순으로 정렬

    for qu in query:  # query도 마찬가지로 key와 value로 분리
        myqu = qu.split(' ')
        qu_key = myqu[:-1]
        qu_val = myqu[-1]

        while 'and' in qu_key:  # and 제거
            qu_key.remove('and')
        while '-' in qu_key:  # - 제거
            qu_key.remove('-')
        qu_key = ''.join(qu_key)  # dict의 key처럼 문자열로 변경

        if qu_key in info_dict:  # query의 key가 info_dict의 key로 존재하면
            scores = info_dict[qu_key]
            if scores:  # score리스트에 값이 존재하면
                enter = bisect_left(scores, int(qu_val))

                answer.append(len(scores) - enter)
        else:
            answer.append(0)

    return answer



# def solution(info, query):
#     data = dict()
#     for a in ['cpp', 'java', 'python', '-']:
#         for b in ['backend', 'frontend', '-']:
#             for c in ['junior', 'senior', '-']:
#                 for d in ['chicken', 'pizza', '-']:
#                     data.setdefault((a, b, c, d), list())
#     print(data)
#     for i in info:
#         i = i.split()
#         for a in [i[0], '-']:
#             for b in [i[1], '-']:
#                 for c in [i[2], '-']:
#                     for d in [i[3], '-']:
#                         data[(a, b, c, d)].append(int(i[4]))
#
#     for k in data:
#         data[k].sort()
#
#         # print(k, data[k])
#     print(data)
#     answer = list()
#     for q in query:
#         q = q.split()
#
#         pool = data[(q[0], q[2], q[4], q[6])]
#         find = int(q[7])
#         l = 0
#         r = len(pool)
#
#         while l < r:
#             mid = (r+l)//2
#             if pool[mid] >= find:
#                 r = mid
#             else:
#                 l = mid+1
#             # print(l, r, mid, answer)
#         # answer.append((pool, find, mid))
#         answer.append(len(pool)-l)
#
#     return answer


info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
         "- and - and - and - 150"]
solution(info, query)