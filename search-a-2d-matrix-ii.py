class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            if self.bsearch(row, target):
                return True
        return False
        
    def bsearch(self, row, target):
        left, right = 0, len(row) - 1
        while left <= right:
            mid = (left + right) / 2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                right = mid - 1
            elif row[mid] < target:
                left = mid + 1
        return False
