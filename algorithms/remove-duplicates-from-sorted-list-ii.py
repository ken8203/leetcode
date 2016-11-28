class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
            
        s, vals = set(), []
        while head:
            if head.val not in s:
                s.add(head.val)
                vals.append(head.val)
            elif head.val in vals:
                vals.remove(head.val)
            head = head.next
        if not len(vals):
            return None
        _head = ListNode(vals[0])
        _result = _head
        for each in vals[1:]:
            _head.next = ListNode(each)
            _head = _head.next
        _head.next = None
        return _result
