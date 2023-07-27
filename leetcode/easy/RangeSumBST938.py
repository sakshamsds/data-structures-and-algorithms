# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum = 0

        if root is None:
            return 0
        
        if root.val < low:
            # look in right subtree 
            sum += self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            # look in left subtree
            sum += self.rangeSumBST(root.left, low, high)
        else:   # low <= root.val and root.val <= high
            sum += root.val
            sum += self.rangeSumBST(root.left, low, high)
            sum += self.rangeSumBST(root.right, low, high)

        return sum
