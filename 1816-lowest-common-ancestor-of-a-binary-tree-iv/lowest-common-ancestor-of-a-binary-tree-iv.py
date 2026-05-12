# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes_set = set([node.val for node in nodes])

        def dfs(node):
            if node is None or node.val in nodes_set:
                return node

            left = dfs(node.left)
            right = dfs(node.right)
            if left and right:
                return node

            return left or right

        return dfs(root)
