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