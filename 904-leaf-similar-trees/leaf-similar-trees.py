# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def getLeaves(node):  # pre order
            if node is None:
                return []

            if node.left is None and node.right is None:    # leaf node
                return [node.val]
            
            l = getLeaves(node.left)
            r = getLeaves(node.right)
            return l + r

        return getLeaves(root1) == getLeaves(root2)
        # leafs1 = getLeafNodes(root1, [])
        # leafs2 = getLeafNodes(root2, [])
        # print(leafs1)
        # print(leafs2)
        # return leafs1 == leafs2        