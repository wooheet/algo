def mergeKLists(lists):
    merge = [l for list in lists for l in list]
    merge.sort()
    print(merge)

lists = [[1,4,5],[1,3,4],[2,6]]
mergeKLists(lists)