# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Edge Case
        if not root:
            return 0

        f1 = self.maxDepth(root.left) 
        f2 = self.maxDepth(root.right)

        return 1 + max(f1, f2)