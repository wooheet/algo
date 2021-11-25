# 애플에서 출제된 문제입니다.
# https://github.com/xissy/coderpad-interviews/tree/master/p135

# 주어진 이진 트리에서, 루트 (최상위 노드) 에서 리프 (자식이 없는 최하위 노드) 까지의 경로를 모두 더하였을 떄 가장 작은 값을 갖는 경로를 찾고, 그 합을 반환하세요.
# 예를 들어, 이 트리에서 최소 값을 갖는 경로는 [10, 5, 1, -1] 이며, 그 합인 15를 반환해야 합니다.

#   10
#  /  \
# 5    5
#  \     \
#    2    1
#        /
#      -1


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # def __str__(self):
    #     return f'<Node: value={self.value}, left={self.left}, right={self.right}>'


def min_path_sum(root):
    # 양의 무한
    m = float('inf')
    q = [(root, root.value)]

    while q:
        node, curr_sum = q.pop()

        # 1. 종료 지점 찾기
        if not node.left and not node.right:
            if m > curr_sum:
                m = curr_sum
            continue

        if node.left:
            q.append((node.left, curr_sum + node.left.value))
        if node.right:
            q.append((node.right, curr_sum + node.right.value))

    return m


if __name__ == "__main__":
    def test_p135_1():
        node = Node(10)
        print(node.__str__())
        assert (min_path_sum(node) == 10)


    def test_p135_2():
        node = Node(10, left=Node(5), right=Node(5))
        print(node.__str__())
        assert (min_path_sum(node) == 15)


    def test_p135_3():
        node = Node(10, left=Node(5, None, Node(2)), right=Node(5))
        print(node.__str__())
        assert (min_path_sum(node) == 15)


    def test_p135_4():
        node = Node(10, left=Node(5, None, right=Node(2)), right=Node(5, None, right=Node(1)))
        print(node.__str__())
        assert (min_path_sum(node) == 16)


    def test_p135_5():
        node = Node(10, left=Node(5, None, right=Node(2)), right=Node(5, None, Node(1, left=Node(-1), right=None)))
        print(node.__str__())
        assert (min_path_sum(node) == 15)

    # test_p135_1()
    # test_p135_2()
    # test_p135_3()
    # test_p135_4()
    test_p135_5()
