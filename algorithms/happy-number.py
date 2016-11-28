class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        while True:
            n = sum([int(each) ** 2 for each in str(n)])
            if n == 1 or n in s:
                break
            else:
                s.add(n)
        return n == 1
