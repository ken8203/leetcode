# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        max_value = max(nums)
        max_index = nums.index(max_value)
        treeNode = TreeNode(max_value)
        treeNode.left = self.constructMaximumBinaryTree(nums[:max_index])
        treeNode.right = self.constructMaximumBinaryTree(nums[max_index+1:])
        return treeNode