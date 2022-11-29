import re


def solution(files):
    answer = []

    find_num = re.compile(r'\d+')
    space = re.compile('[ \t\r\n\v\f]')

    temp = dict()

    for i, f in enumerate(files):
        num = find_num.findall(f)
        split_num = f.split(num[0])
        temp[(split_num[0], int(num[0]), i)] = f
    print(temp)

    # head 먼저 정렬
    # 숫자 정렬
    # for t in temp:
    #     print(t[0])
    #     print(t[1])
    #     # print(temp[t])

    # for i in sorted(files):
    #     num = find_num.findall(i)
    #     temp[num[0]] = i
    #
    # x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    #
    # print(dict(sorted(x.items(), key=lambda item: item[1])))
    # {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}


    return answer


files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
# ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
solution(files)