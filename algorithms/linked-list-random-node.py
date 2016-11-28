class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        
    def getLength(self):
        length = 0
        _head = self.head
        while _head:
            _head = _head.next
            length += 1
        return length

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        import random
        _head = self.head
        length = self.getLength()
        seed = [random.random() for x in range(length)]
        pos = seed.index(min(seed))
        for i in range(pos):
            _head = _head.next
        return _head.val
