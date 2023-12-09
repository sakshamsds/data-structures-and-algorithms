# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []

        def preorder(node):
            if node is None:
                return
            res.append(str(node.val))
            if node.right:
                res.append('(')
                preorder(node.left)
                res.append(')(')
                preorder(node.right)
                res.append(')')
            elif node.left:
                res.append('(')
                preorder(node.left)
                res.append(')')

        preorder(root)
        return ''.join(res)