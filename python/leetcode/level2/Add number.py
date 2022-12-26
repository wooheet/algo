from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, val):
        self.head = ListNode(val)
        self.list = []

    def append(self, val):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = ListNode(val)

    def get(self):
        cur = self.head

        while cur is not None:
            self.list.append(cur.val)
            cur = cur.next

        return self.list

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        list2 = []

        while l1 is not None:
            list1.append(l1.val)
            l1 = l1.next

        while l2 is not None:
            list2.append(l2.val)
            l2 = l2.next
        Q = 0
        result = []

        if len(list1) > len(list2):
            l = len(list1) - len(list2)
            for i in range(l):
                list2.append(0)
        elif len(list1) < len(list2):
            l = len(list2) - len(list1)
            for i in range(l):
                list1.append(0)

        for i in range(len(list1)):
            S = list1[i] + list2[i]

            if Q > 0:
                S += Q
                Q = 0
            if S >= 10:
                Q, R = divmod(S, 10)
                result.append(R)
            else:
                result.append(S)

        if Q > 0:
            result.append(Q)

        lkl = LinkedList(result[0])

        for i in range(1, len(result)):
            lkl.append(result[i])

        return lkl.head

# # l1 = [2,4,3]
# # l2 = [5,6,4]
# # [7,0,8]
#
#
# ListNode
# # [8,9,9,9,0,0,0,1]


s = Solution() #.addTwoNumbers(l1=lkl1.head, l2=lkl1.head)
# s.addTwoNumbers(lkl1.head, lkl2.head)


# var addTwoNumbers = function(l1, l2) {
#     const result = [];
#     let carryNum = 0;
#
#     while(l1 !== null || l2 !== null) {
#         const sum = (l1?.val ?? 0) + (l2?.val ?? 0) + carryNum;
#         result.push(sum%10);
#         carryNum = Math.floor(sum / 10) || 0;
#         l1 = l1?.next || null;
#         l2 = l2?.next || null;
#     }
#
#     if(carryNum > 0) result.push(carryNum);
#
#     return makeListNode(result);
# };
#
# function makeListNode(values) {
#     const link = new ListNode(values[0]);
#     if(values.length > 1) {
#         link.next = makeListNode(values.slice(1))
#     }
#
# return link;
# }


