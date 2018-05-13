class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mapping = {}
        for num in nums:
            if num not in mapping.keys():
                mapping[num] = 0
            mapping[num] += 1

        return [num for num, count in mapping.items() if count == 1]