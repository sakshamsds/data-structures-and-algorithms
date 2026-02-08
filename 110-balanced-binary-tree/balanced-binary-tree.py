# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return True, 0

            left_valid, left_height = dfs(node.left)
            right_valid, right_height = dfs(node.right)
            subtree_height = 1 + max(left_height, right_height)

            if not left_valid or not right_valid or abs(left_height - right_height) > 1:
                return False, subtree_height
            return True, subtree_height

        return dfs(root)[0]
        