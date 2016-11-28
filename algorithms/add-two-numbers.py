class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    
    def extract_length(self, l):
        length = -1
        while l:
            l = l.next
            length += 1
        return length
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        length = max(self.extract_length(l1), self.extract_length(l2))
        head = current = ListNode(0)
        for i in range(length+1):
            current.next = ListNode(0)
            current = current.next
        current = head
        
        while current:
            sum = 0
            if l1 and l2:
                sum = l1.val + l2.val
            elif l1:
                sum = l1.val
            elif l2:
                sum = l2.val
                
            if current.next:
                current.next.val += (current.val + sum) / 10
            current.val = (current.val + sum) % 10
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
            if not l1 and not l2:
                if current.next:
                    if current.next.val == 0:
                        current.next = None
                        break
            current = current.next
        
        return head
