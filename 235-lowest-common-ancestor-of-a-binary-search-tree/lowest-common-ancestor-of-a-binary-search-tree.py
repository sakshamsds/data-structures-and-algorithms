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

            if node.val < lower:
                return dfs(node.right)

            if node.val > upper:
                return dfs(node.left)

        return dfs(root)