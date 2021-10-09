# import sys, heapq
# from collections import defaultdict
#
#
# def solve():
#     global v, e, i, g
#
#     queue = [[0, i]]
#     min_distances = defaultdict(int)
#
#     while queue:
#         cur_w, cur_node = heapq.heappop(queue)
#
#         # 방문한 경우 다음으로
#         if cur_node in min_distances:
#             continue
#
#         min_distances[cur_node] = cur_w
#
#         for next_node, w in g[cur_node].items():
#             heapq.heappush(queue, [(cur_w + w), next_node])
#
#     for j in range(1, v + 1):
#         if j not in min_distances.keys():
#             print("INF")
#         else:
#             print(min_distances[j])
#
#
# v, e = map(int, sys.stdin.readline().strip().split(" "))
# i = int(sys.stdin.readline().strip())
# g = defaultdict(dict)
# g[i][i] = 0
# for _ in range(e):
#     f, t, w = map(int, sys.stdin.readline().strip().split(" "))
#
#     if t not in g[f].keys():
#         g[f][t] = w
#     else:
#         g[f][t] = min(g[f][t], w)
#
# solve()


import sys, heapq
from collections import defaultdict


def solve():
    global v, e, s, g

    INF = sys.maxsize
    visited = [False for _ in range(v)]
    visited[s] = True

    dis = [INF for _ in range(v)]
    dis[s] = 0

    hq = []
    for dest, w in g[s].items():
        heapq.heappush(hq, (w, dest))

    while hq:
        w, dest = heapq.heappop(hq)

        if visited[dest]:
            continue

        visited[dest] = True
        dis[dest] = w

        for n_dest, nw in g[dest].items():
            if visited[n_dest]:
                continue

            heapq.heappush(hq, (w + nw, n_dest))

    for d in dis:
        if d == INF:
            print('INF')
        else:
            print(d)



v, e = map(int, sys.stdin.readline().strip().split(' '))
s = int(sys.stdin.readline().strip()) - 1
g = defaultdict(dict)

for _ in range(e):
    f, t, w = map(int, sys.stdin.readline().strip().split(" "))
    f, t = f-1, t-1

    if t in g[f].keys():
        g[f][t] = min(g[f][t], w)
    else:
        g[f][t] = w

solve()


# 5 9
# 1
# 5 1 1
# 1 2 2
# 1 3 3
# 2 3 4
# 2 4 5
# 3 4 6
# 1 4 1
# 3 5 1
# 4 3 1
