# Definition for a binary tree node.
# https://www.youtube.com/watch?v=zex8_82T46U
# checkout min heap

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if root is None or root.left is None:
            return -1
        left = root.left.val
        right = root.right.val

        if root.val == root.left.val:
            left = self.findSecondMinimumValue(root.left)
        if root.val == root.right.val:
            right = self.findSecondMinimumValue(root.right)

        if left != -1 and right != -1:
            return min(left, right)
        elif left != -1:
            return left
        else:
            return right