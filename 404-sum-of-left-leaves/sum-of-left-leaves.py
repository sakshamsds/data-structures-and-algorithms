# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node, left):
            if node is None:
                return

            if left and node.left is None and node.right is None:
                self.res += node.val

            dfs(node.left, True)
            dfs(node.right, False)

        dfs(root, False)
        return self.res