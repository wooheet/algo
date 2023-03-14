# given a number of nodes and edges, construct an undirected graph. A connected component of the graph is any group of connected nodes. for each connected component, determine the difference between its maximum and minimum value, Return the maximum of all of these differences.
#
# for example, given a graph with 4 nodes, connected as follows: {1,2,3} and {4}. The only connected component has a difference 3-1=2.
#
# function description
# complete the function maximumDifference in the editor below. the function must return an integer denoting the maximum difference between the minimum and maximum node values in any connected component.
#
# maximumDifference has the follwing parameters(s):
# g_nodes: the number of nodes
# g_from[g_from[1],...g_from[g_edges]]: an array of edge start nodes
# g_to[g_to[1],... g_to[g_edges]]: an array of edge end nodes
#
#
# sample input 1
# 5 6
# 1 2
# 1 3
# 2 3
# 2 4
# 3 4
# 4 5
#
# sample output 1
# 4
#
#
#
# Explanation 1
#
# The graph has the follwing connected component:
# 1. A component consisting of nodes {1,2,3,4,5}. The maximal value node is 5 and the minimal value node is 1, so the difference is 5 - 1 = 4.
#
# Because there is only one component, we return 4 as our answer.
#
#
#
# sample input 2
# 5 3
# 1 2
# 3 4
# 4 5
#
# sample output 2
# 2
#
#
# Explanation 2
#
# the graph has the following connected components:
# 1. A component consisting of nodes {1,2}. The maximal value node is 2 and the minimal value node is 1, so the difference is 2 - 1 = 1.
# 2. A component consisting of nodes {3,4,5}. The maximal value node is 5 and the minimal value node is 3, so the difference is 5 - 3 = 2.
#
# We then return the maximum difference for any component, which is 2, as our answer.





def maximumDifference(g_nodes, g_from, g_to):
    # construct adjacency list
    adj_list = [[] for _ in range(g_nodes+1)]
    for i in range(len(g_from)):
        adj_list[g_from[i]].append(g_to[i])
        adj_list[g_to[i]].append(g_from[i])

    # depth-first search to find connected components
    visited = [False] * (g_nodes+1)
    components = []
    for i in range(1, g_nodes+1):
        if not visited[i]:
            component = set()
            min_val = float('inf')
            max_val = float('-inf')
            stack = [i]
            while stack:
                node = stack.pop()
                if not visited[node]:
                    visited[node] = True
                    component.add(node)
                    min_val = min(min_val, node)
                    max_val = max(max_val, node)
                    for neighbor in adj_list[node]:
                        stack.append(neighbor)
            if component:
                components.append((min_val, max_val))

    # find maximum difference between minimum and maximum node values
    max_diff = 0
    for component in components:
        max_diff = max(max_diff, component[1]-component[0])

    return max_diff









































