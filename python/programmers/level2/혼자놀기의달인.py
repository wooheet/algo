# def solution(cards):
#     groups = [[cards[0]], []]
#
#     for i in range(len(cards)):
#         if cards[groups[0][-1] - 1] not in groups[0]:
#             groups[0].append(cards[groups[0][-1] - 1])
#         if cards[i] not in groups[0]:
#             if not groups[1]:
#                 groups[1].append(cards[i])
#             elif cards[groups[1][-1] - 1] not in groups[1]:
#                 groups[1].append(cards[groups[1][-1] - 1])
#
#     return len(groups[0]) * len(groups[1])


def solution(cards):
    boxes = {i+1: c for i, c in enumerate(cards)}
    groups = []

    while boxes:
        visited = set()
        pos = list(boxes.keys())[0]

        while pos not in visited:
            visited.add(pos)
            temp = boxes[pos]
            del boxes[pos]
            pos = temp
        groups.append(len(visited))

    groups.sort(reverse=True)
    return groups[0] * groups[1] if len(groups) > 1 else 0


cards = [8,6,3,7,2,5,1,4]
solution(cards)