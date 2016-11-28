class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dig(root)

    def dig(self, node):
        if node is None:
            return 0
        
        left = right = 0
        if node.left is not None:
            left = self.dig(node.left)
        else:
            return self.dig(node.right) + 1
        
        if node.right is not None:
            right = self.dig(node.right)
        else:
            return left + 1
        
        return min(right, left) + 1
