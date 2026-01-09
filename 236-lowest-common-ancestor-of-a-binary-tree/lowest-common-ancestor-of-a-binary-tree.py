# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # p in left, q in right
        # node is p and q in either left or right
        # node is q and p in either left or right

        lca = []

        def dfs(node):
            if not node:
                return False

            left = dfs(node.left)
            right = dfs(node.right)

            if (
                (node.val in [p.val, q.val] and (left or right)) or \
                (left and right)
            ):
                if len(lca) == 0:
                    lca.append(node)

            return left or right or node.val in [p.val, q.val]

        dfs(root)
        return lca[0]
