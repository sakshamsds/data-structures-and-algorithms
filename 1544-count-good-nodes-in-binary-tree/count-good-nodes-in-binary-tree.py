# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(node, cur_max):
            if node.val >= cur_max:
                cur_max = node.val
                self.res += 1

            if node.left:
                dfs(node.left, cur_max)
            
            if node.right:
                dfs(node.right, cur_max)

        dfs(root, -1e5)
        return self.res