class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.arr.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        self.arr.pop(len(self.arr)-1)

    def top(self):
        """
        :rtype: int
        """
        return self.arr[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.arr) == 0
        
