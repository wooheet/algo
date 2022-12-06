

def solution(box):


    # for i in range(2, len(box)+1):
    #
    #     print()
    #     for x in range(1, box[i-1]+1):
    #         print(x)
            # box[i] = box[i] - x
            # box[i-1] = box[i-1] + b

            # for i, b in enumerate(box, start=1):
            #     print(i, b)


        # box[i] = box[i] - b
        # box[i-1] = box[i-1] + b
    # box = [1, 9, 3, 6]
    # box = [5, 5, 3, 6]


    max_idx = box.index(max(box))

    test(max_idx + 1, box)

    # for i in range(2, len(box)+1):
    #
    #     if i == 3:
    #
    #         for x in range(1, box[i-1]+1):
    #             if x == 4:
    #                 box[i-1] = box[i-1] - x
    #                 box[i-2] = box[i-2] + x
    # print(box)


def test(idx, box):
    for x in range(1, box[idx-1]+1):
        if x == 4:
            box[idx-1] = box[idx-1] - x
            box[idx-2] = box[idx-2] + x
    return box


box = [1,5,7,6]
solution(box)