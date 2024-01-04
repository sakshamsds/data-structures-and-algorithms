# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # traversal: right, left, root
        self.total = 0

        def traverse(node):
            if node is None:
                return
            traverse(node.right)
            self.total += node.val
            node.val = self.total
            traverse(node.left)

        traverse(root)
        return root
