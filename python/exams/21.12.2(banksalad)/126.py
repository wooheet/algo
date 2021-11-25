# This problem was asked by Facebook.
#
# Write a function that rotates a list by k elements.
# For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2].
# Try solving this without creating a copy of the list. How many swap or move operations do you need?


def rotate(lst, k):
    reverse(lst, 0, k - 1)
    reverse(lst, k, len(lst) - 1)
    reverse(lst, 0, len(lst) - 1)


def reverse(lst, i, j):
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1


def test_p126_rotate():
    l = [1, 2, 3, 4, 5, 6]
    rotate(l, 2)
    assert l == [3, 4, 5, 6, 1, 2]


def solution(A, K):
    length = len(A)

    if not A or K == 0:
        return A

    K = K % length
    # K = 4

    new_A = [0 for _ in range(length)]

    i = 0
    while i < length:
        new_A[K] = A[i]
        i += 1
        K = (K + 1) % length

    return new_A


if __name__ == "__main__":
    # A = [1, 2, 3, 4, 5, 6, 7]
    # K = -3
    # print(solution(A, K))

    test_p126_rotate()
