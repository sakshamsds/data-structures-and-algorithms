# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node, parent):
            if node is None:
                return 

            cur = parent * 10 + node.val

            if not node.left and not node.right:    # leaf node
                self.res += cur
            
            dfs(node.left, cur)
            dfs(node.right, cur)

        dfs(root, 0)
        return self.res