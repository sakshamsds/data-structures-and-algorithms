# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        child = set()
        nodes = dict()

        for p, c, l in descriptions:
            if p not in nodes:
                nodes[p] = TreeNode(val=p)

            if c not in nodes:
                nodes[c] = TreeNode(val=c)

            if l == 1:
                nodes[p].left = nodes[c]
            else:
                nodes[p].right = nodes[c]

            child.add(c)

        for root in (set(nodes.keys()) - child):
            return nodes[root]
        
        return None
            