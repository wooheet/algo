from collections import Counter


def solution(progresses, speeds):
    answer = []

    for i in range(len(progresses)):
        maintain = 100 - progresses[i]
        a, b = divmod(maintain, speeds[i])

        if b > 0:
            a = a + 1

        if not answer:
            answer.append(a)
        else:
            answer.append(max(answer[-1], a))

    print(list(Counter(answer).values()))

    return list(Counter(answer).values())


# def solution(progresses, speeds):
#     Q=[]
#     for p, s in zip(progresses, speeds):
#         if len(Q)==0 or Q[-1][0]<-((p-100)//s):
#             Q.append([-((p-100)//s),1])
#         else:
#             Q[-1][1]+=1
#     return [q[1] for q in Q]


# progresses = [93, 30, 55]
# speeds = [1, 30, 5] # [2, 1]
progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1] #[1, 3, 2]
solution(progresses, speeds)



# Q. 기능 개발
# -> 어떤식으로 풀었는지 설명
# 진행도를 100으로 남은 진행도를 추출하여, 진행도에 따라 배포 가능한 날짜를 추출하였다.
# 배포 가능한 날짜는 앞의 배포날짜보다 크면 중복으로 배포 날짜를 배열로 저장해둔다.
# 저장해둔 배포날짜의 카운터를 샌다.
#
# -> 사용한 자료구조를 왜 사용하였는지
# 각 프로그레스별 배포 날짜를 저장하기 위해 배열을 사용했다.
# 배포 날짜가 중복되면 카운터를 사용하기 위한 카운터 함수를 사용하였다.
#
# -> 시간 복잡도는?
# counter 함수 시간복잡 O(N)
#
# -> 개선해야할 점이 무엇인지
# 카운터 함수 없이 시간복잡도를 낮추어서 풀어보자