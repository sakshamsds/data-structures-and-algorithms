# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# time complexity = O(h)
class Solution:

    # recursively delete from the tree and return to the parent
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)         # delete in left subtree
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)       # delete in right subtree
        else:
            # delete the current node
            if root.left is None: 
                return root.right
            
            if root.right is None:
                return root.left
            
            # find min from right subtree
            cur = root.right
            while cur.left:
                cur = cur.left
            root.val = cur.val
            root.right = self.deleteNode(root.right, cur.val)             # replace the value and then delete from left subtree
        return root
    
# root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
# Solution().deleteNode(root, 3)
# print(Solution().get_min(root.left))