# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # bottom up doesn't work
        # top down does
        # propagate the strings downwards and then compare the results

        def dfs(node, cur):
            if not node:
                return 

            cur = chr(ord('a') + node.val) + cur
            if not node.left and not node.right:        # if leaf node
                return cur

            left = dfs(node.left, cur)
            right = dfs(node.right, cur)

            if left and right:
                return min(left, right) 
            elif left:
                return left
            else:
                return right

        return dfs(root, '')