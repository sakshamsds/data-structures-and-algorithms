# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode | None) -> int:

        def dfs(node) -> tuple(int, int):  # rob, didn't rob
            if not node:
                return 0, 0

            lr, lnr = dfs(node.left)
            rr, rnr = dfs(node.right)

            return node.val + lnr + rnr, max(lr, lnr) + max(rr, rnr)

        return max(dfs(root))
