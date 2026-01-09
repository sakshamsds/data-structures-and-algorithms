# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):  # returns depth, lca
            if not node:
                return 0, None

            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)

            if left_depth > right_depth:    # lca lies in left
                return 1 + left_depth, left_lca
            
            if right_depth > left_depth:
                return 1 + right_depth, right_lca

            return 1 + left_depth, node     # cur node is the lca

        return dfs(root)[1]