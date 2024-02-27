# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(node):
            if node is None:
                return 0
            l_height = dfs(node.left)
            r_height = dfs(node.right)
            cur_diameter = l_height + r_height
            self.diameter = max(self.diameter, cur_diameter)
            return max(l_height, r_height) + 1

        dfs(root)
        return self.diameter
