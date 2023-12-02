# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if node == None:
                return 0
            l_height = helper(node.left)
            r_height = helper(node.right)
            if l_height < 0 or r_height < 0 or abs(l_height - r_height) > 1:
                return -1
            return max(l_height, r_height) + 1

        return helper(root) != -1
        

        