# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
1. first value in preorder traversal is the root
2. find root in inorder list and split 
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}
        for i, root in enumerate(inorder):
            inorder_map[root] = i

        def helper(preorder, inorder):
            if not preorder:
                return None

            root = TreeNode(preorder[0])
            i = inorder_map[root.val]

            root.left = self.buildTree(preorder[1:1 + i], inorder[:i])
            root.right = self.buildTree(preorder[i + 1:], inorder[i + 1:])
            return root

        return helper(preorder, inorder)