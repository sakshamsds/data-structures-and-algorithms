# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # at every node, 
        # check height of node.left
        # check height of node.right
        # max_depth = h_left + h_right
        # cur_height = max(h_left, h_right)

        # self.diameter = 0
        diameter = 0

        def dfs(node):
            nonlocal diameter
            if node is None:
                return 0

            h_left = dfs(node.left)
            h_right = dfs(node.right)
            cur_height = 1 + max(h_left, h_right)
            diameter = max(diameter, h_left + h_right)
            return cur_height

        dfs(root)
        # print(res)
        return diameter
        