# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        cur = root

        if val < cur.val:
            # insert into left BST
            if cur.left:
                self.insertIntoBST(cur.left, val)
            else:
                cur.left = TreeNode(val)
        else:
            # insert into right BST
            if cur.right:
                self.insertIntoBST(cur.right, val)
            else:
                cur.right = TreeNode(val)

        return root