# def solution(paper, n):
#     # sort the paper in descending order
#     # paper.sort(reverse=True)
#
#     # keep track of the maximum value
#     max_value = 0
#
#     # iterate through the paper and fold it n-1 times
#     for i in range(n-1):
#         # fold the paper
#         paper = fold_paper(paper)
#
#         # calculate the maximum value
#         max_value = max(max_value, sum(paper))
#
#     return max_value
#
# def fold_paper(paper):
#     # create a new array to store the folded paper
#     folded_paper = []
#
#     # iterate through the paper and fold it
#     for i in range(len(paper) // 2):
#         # add the sum of the two numbers on the paper to the folded paper
#         folded_paper.append(paper[i] + paper[len(paper)-1-i])
#
#     return folded_paper

# def solution(paper, n):
#     # If the paper can only be folded once, find the maximum value
#     # by adding the numbers on the overlapping cells
#     if n == 1:
#         return max([paper[i] + paper[-i-1] for i in range(len(paper) // 2)])
#
#     # If the paper can be folded more than once, we can try to
#     # fold it in all possible ways and see which one produces
#     # the maximum value
#     else:
#         max_value = 0
#         for i in range(1, len(paper)):
#             left = paper[:i]
#             right = paper[i:]
#             # Recursively call the function with the left and right
#             # halves of the paper and the remaining number of folds
#             value = solution(left, n-1) + solution(right, n-1)
#             max_value = max(max_value, value)
#         return max_value

# def solution(paper, n):
#     # Base case: if the strip of paper can no longer be folded, return the largest number on the strip
#     if n == 0 or len(paper) == 1:
#         return max(paper)
#
#     # Fold the strip of paper in half and add the two numbers on the overlapping cells
#     half = len(paper) // 2
#     folded = [paper[i] + paper[half+i] for i in range(half)]
#
#     # Recursively compute the maximum value for each half of the strip of paper
#     max1 = solution(folded, n-1)
#     max2 = solution(paper[half:], n-1)
#
#     # Return the maximum value we have seen so far
#     return max(max1, max2)


def solution(paper, n):
    # base case: if we've reached the maximum number of folds, return the largest number in the paper
    # if there is an unused cell at the end, also return the maximum value of the entire paper
    if n == 0:
        if len(paper) % 2 == 1:
            return max(max(paper), solution(paper[:-1], n))
        else:
            return max(paper)

    # fold the paper in half and add the numbers on the overlapping cells
    half = len(paper) // 2
    folded = [paper[i] + paper[half + i] for i in range(half)]

    # keep track of the maximum sum we've seen so far
    max_sum = max(folded)
    print(max_sum)


print(solution([7,3,5,-2,9], 2))
# assert solution([7,3,5,-2,9], 2) == 19



# paper = [7, 3, 5, -2, 9]
# n = 2

# paper = [10, -10]
# n = 1

# paper = [1, 2, 4, 8, 16]
# n = 2

# print(solution(paper, n))









# 종이 띠를 접어서 가장 큰 수를 만들려고 합니다. 종이 띠는 동일한 너비를 가진 칸으로 이루어져 있으며 각 칸에는 숫자가 적혀있습니다. 칸과 칸 사이에는 구분선이 그어져 있고, 이 구분선을 따라 종이를 접을 수 있습니다. 종이를 접어서 칸이 겹쳐지면, 칸에 적힌 두 수를 더합니다. 종이 띠에 적힌 숫자가 [7,3,5,-2,9]이고, 종이를 접을 수 있는 최대 횟수가 2회일 때, 종이를 접어 최댓값을 만드는 과정을 나타냅니다. 화살표는 종이를 접는 방향을 나타내며, 화살표 중간에 있는 구분선을 따라 종이를 접습니다. 종이 띠에 적힌 수를 나타내는 1차원 배열 paper와 종이 띠를 접을 수 있는 최대 횟수 n이 매개변수로 주어집니다. n번 이하로 paper를 접어서 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.
#
# 제한사항
# paper의 길이는 1이상 50 이하입니다
# paper의 원소는 -100000 이상 100000 이하인 정수입니다.
#
#
# 입출력 예
# paper          n        result
# ———           ———         ———
# [7,3,5,-2,9]    2          19
# [10, -10]       1          10
# [1,2,4,8,16]    2          31
# [7,3,-7,5,-3]   2          12
#
#
# 입출력 예 설명
#
# 입출력 예 [10, -10]
# 최대 1번 접을 수 있지만, 접을 경우 두 수의 합이 0이 되기 때문에 접지 않습니다. 접지 않는 경우, 남은 수 중에서 가장 큰 값은 10 입니다
#
# 입출력 예 [1,2,4,8,16]
# paper의 길이가 5이고, 최대 3번까지 ㅈ버을 수 있기 때문에 모든 수를 한 칸에 합칠 수 있습니다. 또한 paper의 모든 원소가 0보다 크기 때문에 답은 모든 원소의 합과 같습니다. 따라서 31을 return합니다.
#
# 입출력 예 [7,3,-7,5,-3]
# 3과 -7 사이를 접으면 7과 5를 합쳐 12를 만들 수 있으며, 이것이 최댓값입니다. 최대 2번 접을 수 있지만, 어떤 방법으로 2번 접더라도 12보다 큰 수를 만들 수 없습니다.