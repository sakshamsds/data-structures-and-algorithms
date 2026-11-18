# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode | None) -> TreeNode | None:
        # dfs(node) -> depth, node

        def dfs(node):
            if not node:
                return 0, node

            leftDepth, left = dfs(node.left)
            rightDepth, right = dfs(node.right)

            if leftDepth > rightDepth:
                return leftDepth + 1, left
            elif leftDepth < rightDepth:
                return rightDepth + 1, right
            else:
                return max(leftDepth, rightDepth) + 1, node

        return dfs(root)[1]