# 1. 전체배열을 순회하며 속도만큼 더한다
# 2. 맨 앞을 확인하여 배포 가능한지 본다
# 3. 배포가 가능하다면 순회하며, 하나씩 제거하며 배포수를 증가시킨다.
# 4. 배포가 끝나면 결과에 배포수를 넣는다

from collections import deque

# def solution(progresses, speeds):
#     answer = []
#     progresses = deque(progresses)
#     speeds = deque(speeds)
#
#     while progresses:
#         # 진행
#         while progresses[0] < 100:
#             for si in range(len(speeds)):
#                 progresses[si] += speeds[si]
#
#         # 배포 확인
#         count = 0
#         for progress in progresses:
#             if progress >= 100:
#                 count += 1
#             else:
#                 break
#         if count > 0:
#             answer.append(count)
#
#             for j in range(count):
#                 progresses.popleft()
#                 speeds.popleft()
#
#     return answer

# def solution(progresses, speeds):
#     progresses = deque(progresses)
#     speeds = deque(speeds)
#
#     ans = []
#     while progresses:
#         while progresses[0] < 100:
#             for i in range(len(progresses)):
#                 progresses[i] += speeds[i]
#
#         res = 0
#         while progresses and progresses[0] >= 100:
#             res += 1
#             progresses.popleft()
#             speeds.popleft()
#         ans.append(res)
#
#     # print(ans)
#     return ans
#
# solution([93, 30, 55],[1, 30, 5])
# solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])


# class ginueng:
#
#     def __init__(self, speed, progress, deploy_day=0, is_deploy=False):
#         self.speed = speed
#         self.progress = progress
#         self.deploy_day = deploy_day
#         self.is_deploy = is_deploy
#
#     def available_deploy(self):
#         p = self.progress
#
#         while p < 100:
#             p += self.speed
#             self.deploy_day += 1
#
#         return True
#
#
# def solution(progresses, speeds):
#     answer = []
#
#     g = list()
#
#     for i in range(0, len(progresses)):
#         c = ginueng(speeds[i], progresses[i])
#         c.available_deploy()
#         g.append(c)
#
#     deploy_day = [i.deploy_day for i in g]
#     deploy_day = deque(deploy_day)
#
#     while len(deploy_day) > 0:
#         answer.append(1)
#
#         if deploy_day:
#             first = deploy_day.popleft()
#
#             if deploy_day:
#                 second = deploy_day.popleft()
#                 if first > second:
#                     answer[0] += 1
#             else:
#                 break
#         else:
#             break
#     return answer


def solution(progresses, speeds):
    Q = []

    for p, s in zip(progresses, speeds):
        if len(Q) == 0 or Q[-1][0] < -((p-100)//s):
            Q.append([-((p-100)//s), 1])
        else:
            Q[-1][1] += 1

    return [q[1] for q in Q]


if __name__ == "__main__":
    print(solution([93, 30, 55], [1, 30, 5]))
    print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))