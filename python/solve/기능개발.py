
from collections import Counter

# def solution(progresses, speeds):
#     answer = []
#
#     for i in range(len(progresses)):
#         maintain = 100 - progresses[i]
#         a, b = divmod(maintain, speeds[i])
#
#         if b > 0:
#             a = a + 1
#
#         if not answer:
#             answer.append(a)
#         else:
#             answer.append(max(answer[-1], a))
#
#     print(list(Counter(answer).values()))
#
#     return list(Counter(answer).values())


def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]


# progresses = [93, 30, 55]
# speeds = [1, 30, 5] # [2, 1]
progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1] #[1, 3, 2]
solution(progresses, speeds)



# Q. 기능 개발
# -> 어떤식으로 풀었는지 설명
# -> 사용한 자료구조를 왜 사용하였는지
# -> 개선해야할 점이 무엇인지