class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        candidates = []
        for h in citations:
            N = len([each for each in citations if each >= h])
            if N >= h:
                candidates.append(h)
            else:
                candidates.append(N)

        if 0 == len(candidates):
            return 0
        return max(candidates)