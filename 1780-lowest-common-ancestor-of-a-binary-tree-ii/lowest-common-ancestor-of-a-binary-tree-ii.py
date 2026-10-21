# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        nodes_exists = [0]

        def dfs(node):
            if not node:
                return None

            left = dfs(node.left)
            right = dfs(node.right)

            if node == p or node == q:
                nodes_exists[0] += 1
                return node

            if left and right:
                return node

            return left or right

        lca = dfs(root)
        return lca if nodes_exists[0] == 2 else None 