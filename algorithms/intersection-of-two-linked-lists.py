# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        a, b = [], []
        iterA, iterB = headA, headB
        while iterA or iterB:
            if iterA:
                a.append(iterA.val)
                iterA = iterA.next
            if iterB:
                b.append(iterB.val)
                iterB = iterB.next

        intersection = list(set(a) & set(b))
        if len(intersection) == 0:
            return None
        else:
            intersection.sort()
            while headA:
                if headA.val == intersection[0]:
                    return headA
                headA = headA.next