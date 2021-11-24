
def merge(intervals):
    sorted_intervals = sorted(intervals, key=lambda i: i[0])
    merge_intervals = list()

    for interval in sorted_intervals:
        if merge_intervals and interval[0] <= merge_intervals[-1][1]:
            merge_intervals[-1] = (merge_intervals[-1][0], max(interval[1], merge_intervals[-1][1]))
        else:
            merge_intervals.append(interval)
    return merge_intervals


def test_p77_merge():
    intervals = [(1, 3), (5, 8), (4, 10), (20, 25)]
    assert merge(intervals) == [(1, 3), (4, 10), (20, 25)]

    intervals = [(1, 3), (5, 8), (4, 10), (20, 25), (22, 27)]
    assert merge(intervals) == [(1, 3), (4, 10), (20, 27)]


if __name__ == '__main__':
    test_p77_merge()
