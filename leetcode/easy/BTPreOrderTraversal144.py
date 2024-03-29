# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # # recursive
        # results = []
        # def recursive_pre_order(root):
        #     if root is None:
        #         return
        #     results.append(root.val)
        #     recursive_pre_order(root.left)
        #     recursive_pre_order(root.right)

        # recursive_pre_order(root)

        # iterative
        if root is None: return []

        results = []
        stack = []
        stack.append(root)

        while stack:
            root = stack.pop()
            results.append(root.val)

            # push right first, so when we pop, left gets priority
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)

        return results