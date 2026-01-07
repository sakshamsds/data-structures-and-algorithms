# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        def dfs_total(node):
            if not node:
                return 0
            return node.val + dfs_total(node.left) + dfs_total(node.right)

        total_sum = dfs_total(root)

        self.max_pdt = root.val
        MOD = 10 ** 9 + 7

        def dfs(node):
            if not node:
                return 0
            node_sum = node.val + dfs(node.left) + dfs(node.right)
            self.max_pdt = max(self.max_pdt, node_sum * (total_sum - node_sum))
            return node_sum

        dfs(root)
        return self.max_pdt % MOD

            