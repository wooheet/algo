def bs(data, l, r):
    if len(data) <= 0 :
        return -1

    while l < r:
        mid = (l+r) // 2
        print(mid)

        if data[mid] == 'f':
            r = mid
        else:
            l = mid + 1

    print(l)

data = ['s','s','s','f','f','f','f','f','f','f']
bs(data, 0, len(data)-1)
