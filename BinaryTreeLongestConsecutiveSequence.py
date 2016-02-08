# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    maxLen = 0
    
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.helper(root, 1)
        return self.maxLen
        
    def helper(self, node, length):
        self.maxLen = max(self.maxLen, length)
        for child in [node.left, node.right]:
            if child:
                l = length+1 if child.val == node.val+1 else 1
                self.helper(child, l)
        
