# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # calculate max path sum for a each node
        self.max_path_sum = root.val

        def dfs(node):
            if node is None:
                return 0

            l_sum = dfs(node.left)
            r_sum = dfs(node.right)
            self.max_path_sum = max(self.max_path_sum, l_sum + r_sum + node.val)
            return max(node.val + max(l_sum, r_sum, 0), 0)

        dfs(root)
        return self.max_path_sum


