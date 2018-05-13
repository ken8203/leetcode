# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None

        l = []
        while l1 or l2:
            if l1:
                l.append(l1.val)
                l1 = l1.next
            if l2:
                l.append(l2.val)
                l2 = l2.next
        l.sort()

        ite = ret = ListNode(l[0])
        for val in l[1:]:
            ite.next = ListNode(val)
            ite = ite.next

        return ret
