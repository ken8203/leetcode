class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = int(a, 2) + int(b, 2)
        return "{0:b}".format(result)