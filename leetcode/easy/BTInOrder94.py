# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # # Recursive
        # elements = []

        # def recursive_inorder(root):
        #     if root is None:
        #         return
        #     recursive_inorder(root.left)
        #     elements.append(root.val)
        #     recursive_inorder(root.right)

        # recursive_inorder(root)
        
        # Iterative Solution
        elements = []
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            elements.append(cur.val)
            cur = cur.right

        return elements