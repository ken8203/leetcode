# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return []

        smaller = []
        bigger = []
        while head:
            if head.val < x:
                smaller.append(head.val)
            else:
                bigger.append(head.val)
            head = head.next

        merged = smaller + bigger
        newHead = ListNode(merged[0])
        ptr = newHead

        for val in merged:
            ptr.next = ListNode(val)
            ptr = ptr.next

        ptr = newHead.next
        return ptr
