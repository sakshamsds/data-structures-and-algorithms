# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        low, high = min(p.val, q.val), max(p.val, q.val)

        def dfs(node):
            if node.val < low:
                return dfs(node.right)
            if node.val > high:
                return dfs(node.left)
            return node

        return dfs(root)