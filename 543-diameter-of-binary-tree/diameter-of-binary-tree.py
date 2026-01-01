# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # for a given node, longest path on the left side + longest path on the right side
        self.diameter = 0

        def dfs(node):
            if node is None:
                return 0

            height_left = dfs(node.left)
            height_right = dfs(node.right)
            self.diameter = max(self.diameter, height_left + height_right)
            return 1 + max(height_left, height_right)

        dfs(root)
        return self.diameter