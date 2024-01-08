# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        leftSum = self.rangeSumBST(root.left, low, high)
        rightSum = self.rangeSumBST(root.right, low, high)
        curSum = leftSum + rightSum
        if low <= root.val <= high:
            curSum += root.val
        return curSum
