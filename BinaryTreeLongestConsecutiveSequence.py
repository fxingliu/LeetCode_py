# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        maxLen = 0
        dq = deque([[root, 1]])
        while dq:
            node, len = dq.popleft()
            maxLen = max(maxLen, len)
            for child in [node.left, node.right]:
                if child :
                    newLen = len+1 if child.val == node.val+1 else 1
                    dq.append([child, newLen])
        return maxLen
                    
        
