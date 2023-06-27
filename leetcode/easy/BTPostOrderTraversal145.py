# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # # recursive
        # results = []
        # def recursive_post_order(root):
        #     if root is None:
        #         return
        #     recursive_post_order(root.left)
        #     recursive_post_order(root.right)
        #     results.append(root.val)

        # recursive_post_order(root)

        # iterative
        if root is None: return []
        results = []
        stack = []
        stack.append(root)
        while stack:
            root = stack.pop()
            results.insert(0, root.val)

            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)

        return results