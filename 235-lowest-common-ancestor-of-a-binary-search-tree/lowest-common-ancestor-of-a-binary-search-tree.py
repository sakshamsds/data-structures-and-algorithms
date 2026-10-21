# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lower, upper = min(p.val, q.val), max(p.val, q.val)

        def dfs(node):
            if not node:
                return None

            if lower <= node.val <= upper:
                return node

            right = None
            if node.val < lower:
                right = dfs(node.right)

            left = None
            if node.val > upper:
                left =  dfs(node.left)

            return left or right

        return dfs(root)