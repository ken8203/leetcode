class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums
        self.numSize = len(nums)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        import random
        ans = x = 0
        for idx, number in enumerate(self.nums):
            if number == target:
                seed = random.random()
                if seed > x:
                    ans = idx
                    x = seed
        return ans
