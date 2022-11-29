import re


def solution(files):
    find_num = re.compile(r'\d+')
    space = re.compile('[ \t\r\n\v\f]')

    temp = dict()

    for i, f in enumerate(files):
        num = find_num.findall(f)
        split_num = f.split(num[0])
        temp[(split_num[0].upper(), float(num[0]) + float(i/10))] = f

    sort_dic = dict(sorted(temp.items(), key=lambda item: item[0]))

    return [sort_dic[i] for i in sort_dic]


def solution2(files):
    temp = [re.split(r"([0-9]+)", s) for s in files]

    sort = sorted(temp, key = lambda x: (x[0].lower(), int(x[1])))

    return [''.join(s) for s in sort]

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
# files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
# ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
# ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
print(solution(files))
print(solution2(files))