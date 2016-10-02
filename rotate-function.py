class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 1 or len(A) == 0:
            return 0
        ans = []
        prev = sum([i*v for i, v in enumerate(A) ])
        s = sum(A)
        for i in range(len(A) - 1, -1, -1):
            tmp = prev + s - len(A) * A[i]
            ans.append(tmp)
            prev = tmp
        return max(ans)
