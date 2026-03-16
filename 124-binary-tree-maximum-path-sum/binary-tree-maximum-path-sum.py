# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.pathSum = root.val

        def dfs(node):
            if not node:
                return 0

            leftSum = dfs(node.left)
            rightSum = dfs(node.right)

            self.pathSum = max(self.pathSum, node.val + max(
                leftSum, rightSum, 0, leftSum + rightSum
            ))

            return max(leftSum, rightSum, 0) + node.val

        dfs(root)
        return self.pathSum

