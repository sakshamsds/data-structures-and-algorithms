# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.maxPath = root.val

        def dfs(node):
            if not node:
                return 0

            leftMax = dfs(node.left)
            rightMax = dfs(node.right)

            self.maxPath = max(
                self.maxPath,
                node.val + leftMax + rightMax,
            )

            return max(
                leftMax + node.val,
                rightMax + node.val,
                node.val,
                0
            )

        dfs(root)
        return self.maxPath