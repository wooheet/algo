# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    c1 = convert(l1)
    c2 = convert(l2)
    r = str(int(c1) + int(c2))
    print(list(r[::-1]))

    l = ListNode(list(r[::-1])[0])

    for i in range(1, len(list(r[::-1]))):
        if l.next is None:
            l.next = ListNode(list(r[::-1])[i])
    print(l)


def convert(l):
    result = []
    while l.next is not None:
        result.append(str(l.val))
        if l.next is not None:
            l = l.next
    result.append(str(l.val))

    return "".join(result)

l1 = [2,4,3]
l2 = [5,6,4]
addTwoNumbers(l1,l2)
