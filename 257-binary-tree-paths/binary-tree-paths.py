# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []     

        def dfs(node, path):
            if not node:
                return
            path.append(str(node.val))
            if node.left is None and node.right is None:
                res.append('->'.join(path))
            else:
                dfs(node.left, path)
                dfs(node.right, path)
            path.pop()

        dfs(root, [])
        return res