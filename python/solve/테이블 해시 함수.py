from functools import reduce


def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x: (x[col - 1], -x[0]))

    result = []
    i = row_begin

    for row in data[row_begin - 1:row_end]:
        result.append(sum([r % i for r in row]))
        i += 1

    answer = reduce(lambda x, y: x ^ y, result)
    # reduce(lambda x, y: x ^ y, [sum(map(lambda x: x%(i+1), data[i])) for i in range(row_begin-1, row_end)])
    return answer


solution([[2, 2, 6], [1, 5, 10], [4, 2, 9], [3, 8, 3]], 2, 2, 3)
