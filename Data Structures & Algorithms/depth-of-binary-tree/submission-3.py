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

        #Iterative DFS
        stack = [[root, 1]]
        res = 1

        while stack:
            node, depth = stack.pop()
            if node:
                res = max(depth, res)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res


        #Iterative BFS
        # q = deque([root])
        # level = 0

        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level +=1
        # return level


        #Calculate Depth of it's children
        #Recursive DFS
        # left_depth = self.maxDepth(root.left) 
        # right_depth = self.maxDepth(root.right)

        # return 1 + max(left_depth, right_depth)