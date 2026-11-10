# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.found = 0

        # post order traversal
        def dfs(node):
            if not node:
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if node == p or node == q:
                self.found += 1
                return node
            
            if left and right:
                return node
            return left or right

        lca = dfs(root)
        return lca if self.found == 2 else None