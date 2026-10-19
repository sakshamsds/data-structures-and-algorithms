# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode | None) -> list[list[int]]:
        leafNodes = collections.defaultdict(list)

        def dfs(node):
            if not node:
                return 0

            leftOrder = dfs(node.left)
            rightOrder = dfs(node.right)
            curOrder = 1 + max(leftOrder, rightOrder)
            leafNodes[curOrder].append(node.val)
            return curOrder
            
        dfs(root)

        res = []
        for i in range(1, 100):
            if i not in leafNodes:
                break
            res.append(leafNodes[i])
        return res
