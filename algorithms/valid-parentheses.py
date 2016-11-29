class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        table = {')': '(', '}': '{', ']': '['}
        result = []
        for word in s:
            if word in ['(', '{', '[']:
                result.append(word)
            else:
                if len(result) == 0:
                    return False
                if table[word] != result[-1]:
                    return False
                result.pop()
        return len(result) == 0
