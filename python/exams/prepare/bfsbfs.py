from collections import deque
import sys

read = sys.stdin.readline


def bfs(v):
    q = deque()
    q.append(v)
    visit_list[v] = 1

    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, n + 1):
            if visit_list[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visit_list[i] = 1


def dfs(v):
    visit_list2[v] = 1
    print(v, end=" ")
    for i in range(1, n + 1):
        if visit_list2[i] == 0 and graph[v][i] == 1:
            dfs(i)



n, m, v = map(int, read().split())
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

# graph = [
#     [],
#     [2, 3],
#     [1, 8],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7, 8],
#     [6, 8],
#     [2, 6, 7]
# ]

graph = [[0] * (n + 1) for _ in range(n + 1)]
visit_list = [0] * (n + 1)
visit_list2 = [0] * (n + 1)

print(graph)

for _ in range(m):
    a, b = map(int, read().split())
    graph[a][b] = graph[b][a] = 1
    # print(graph)

print(graph)
# print(visit_list)
print(visit_list2)

dfs(v)
# print()
# bfs(v)

