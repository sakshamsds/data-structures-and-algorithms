# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def getLeafNodes(node, leafs):  # pre order
            if node is None:
                return leafs

            if node.left is None and node.right is None:    # leaf node
                leafs.append(node.val)
            
            new_leafs = getLeafNodes(node.left, leafs)
            return getLeafNodes(node.right, new_leafs)

        return getLeafNodes(root1, []) == getLeafNodes(root2, [])
        # leafs1 = getLeafNodes(root1, [])
        # leafs2 = getLeafNodes(root2, [])
        # print(leafs1)
        # print(leafs2)
        # return leafs1 == leafs2        