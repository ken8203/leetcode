class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pool = set()
        table = {}
        for k, v in enumerate(nums):
            if v in pool:
                return [table[v], k]
                
            diff = target - v 
            if diff not in pool:
                pool.add(diff)
                table[diff] = k
        return [-1, -1]
