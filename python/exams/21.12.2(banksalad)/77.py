# https://github.com/xissy/coderpad-interviews/tree/master/p77
# 중첩될 수 있는 인터벌들을 갖는 리스트가 있습니다. 중첩되는 인터벌들을 하나로 합친 새로운 리스트를 반환하세요.
# 입력 리스트는 정렬되어 있지 않습니다.
# 예를 들어, [(1, 3), (5, 8), (4, 10), (20, 25)] 가 주어지면, [(1, 3), (4, 10), (20, 25)] 를 반환해야 합니다


def merge(intervals):
    sorted_intervals = sorted(intervals, key=lambda i: i[0])
    merged_intervals = []
    for interval in sorted_intervals:
        if merged_intervals and interval[0] <= merged_intervals[-1][1]:
            merged_intervals[-1] = (merged_intervals[-1][0], max(merged_intervals[-1][1], interval[1]))
        else:
            merged_intervals.append(interval)

    return merged_intervals


def test_p77_merge():
    intervals = [(1, 3), (5, 8), (4, 10), (20, 25)]
    assert merge(intervals) == [(1, 3), (4, 10), (20, 25)]

    intervals = [(1, 3), (5, 8), (4, 10), (20, 25), (22, 27)]
    assert merge(intervals) == [(1, 3), (4, 10), (20, 27)]


if __name__ == '__main__':
    test_p77_merge()
