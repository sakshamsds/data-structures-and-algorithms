# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        MIN_NODE = TreeNode(float)

        def dfs(node):
            if not node:
                return MIN_NODE

            left = dfs(node.left)
            right = dfs(node.right)

            if node == p or node == q or (left != MIN_NODE and right != MIN_NODE):
            # if node.val == p.val or node.val == q.val:
                return node

            if left != MIN_NODE:
                return left
            
            return right

        return dfs(root)