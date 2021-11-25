# This problem was asked by Amazon.
#
# Given a node in a binary search tree, return the next bigger element, also known as the inorder successor.
#
# For example, the inorder successor of 22 is 30.
#
#    10
#   /  \
#  5    30
#      /  \
#    22    35


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # def __str__(self):
    #     return f'<Node: value={self.value}, left={self.left}, right={self.right}>'


def get_path(root, value):
    path = [root]

    while True:
        node = path[-1]

        if value < node.value:
            if not node.left:
                return None
            path.append(node.left)
        elif value > node.value:
            if not node.right:
                return None
            path.append(node.right)
        else:
            return path


def get_most_left(node):
    while node and node.left:
        node = node.left
    return node


def get_next_bigger(root, value):
    if not root:
        return None

    path = get_path(root, value)
    if not path:
        return None

    node = path[-1]
    most_left_of_right = get_most_left(node.right)
    if most_left_of_right:
        return most_left_of_right

    for parent in path[:-1][::-1]:
        if parent.left:
            return parent

    return None


if __name__ == "__main__":
    def test_p133_get_path():
        node = Node(5)
        assert get_path(node, 5) == [node]
        assert get_path(node, 4) == None
        assert get_path(node, 6) == None

        node2 = Node(2)
        node3 = Node(3, node2)
        node8 = Node(8)
        node7 = Node(7, None, node8)
        node5 = Node(5, node3, node7)
        assert get_path(node5, 2) == [node5, node3, node2]
        assert get_path(node5, 8) == [node5, node7, node8]
        assert get_path(node5, 1) == None
        assert get_path(node5, 4) == None
        assert get_path(node5, 6) == None


    def test_p133_get_most_left():
        node = Node(5)
        assert get_most_left(node).value == 5

        node = Node(5, Node(3, Node(1)))
        assert get_most_left(node).value == 1

        node = Node(5, Node(3, None, Node(1)))
        assert get_most_left(node).value == 3


    def test_p133_get_next_bigger():
        node = Node(5, None, Node(7, Node(6)))
        assert get_next_bigger(node, 5).value == 6

        node = Node(5, Node(3))
        assert get_next_bigger(node, 3).value == 5

        node = Node(5, Node(3, Node(1)))
        assert get_next_bigger(node, 1).value == 3

        node = Node(5, None, Node(8, Node(6, None, Node(7))))
        assert get_next_bigger(node, 6).value == 7

        node = Node(10, Node(5), Node(30, Node(22), Node(35)))
        assert get_next_bigger(node, 22).value == 30

        node = Node(10, Node(5), Node(30, Node(22, None, Node(25)), Node(35)))
        assert get_next_bigger(node, 25).value == 30


    test_p133_get_path()
    test_p133_get_most_left()
    test_p133_get_next_bigger()
