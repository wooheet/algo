# import heapq
#
# def solution(scoville, k):
#     answer = 0
#
#     heapq.heapify(scoville)
#
#     while len(scoville) > 1 and scoville[0] < k:
#         answer += 1
#         fir = heapq.heappop(scoville)
#         sec = heapq.heappop(scoville)
#
#         # 새로운 스코빌 넣기
#         new_one = fir + (sec * 2)
#         heapq.heappush(scoville, new_one)
#
#     if scoville[0] < k:
#         return -1
#
#     return answer
#
# solution([1, 2, 3, 9, 10, 12], 7)
# solution([1, 2], 3)
# solution([1, 2], 10)


import heapq as hq


def solution(scoville, K):
    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1

    return answer




# class ScovilleClass:
#
#     def __init__(self, k, scoville, new_scoville=[]):
#         self.k = k
#         self.scoville = scoville
#         self.new_scoville = new_scoville
#
#     def new_scoville_factor(self):
#         answer = 0
#
#         sort_scoville = sorted(self.scoville)
#         while len(sort_scoville) > 1 and sort_scoville[0] < self.k:
#             self.scoville = sort_scoville
#
#             if sort_scoville[0] < self.k:
#                 sort_scoville[0] = sort_scoville[0] + (sort_scoville[1] * 2)
#                 del sort_scoville[1]
#                 sort_scoville = sorted(self.scoville)
#                 answer += 1
#             else:
#                 break
#         return answer
#
#
# def solution(scoville, K):
#     sv = ScovilleClass(K, scoville)
#     answer = sv.new_scoville_factor()
#     return answer


if __name__ == "__main__":
    print(solution([1, 2, 3, 9, 10, 12], 7))