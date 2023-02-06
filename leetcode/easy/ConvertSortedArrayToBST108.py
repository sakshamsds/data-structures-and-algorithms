# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# 108. Convert Sorted Array to Binary Search Tree
# https://www.youtube.com/watch?v=0K0uCMYq5ng

# Binary Search Tree is a node-based binary tree data structure which has the following properties:
# The left subtree of a node contains only nodes with keys lesser than the node’s key.
# The right subtree of a node contains only nodes with keys greater than the node’s key.
# The left and right subtree each must also be a binary search tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # SOLUTION 1
        # # time complexity - O(nLogn)
        # # space complexity - O(logn) - height of balanced tree
        # if not nums:
        #     return None
        # else:
        #     # start from the middle element
        #     middle_idx = len(nums)//2
        #     root = TreeNode(nums[middle_idx])
        #     root.left = self.sortedArrayToBST(nums[:middle_idx])            # not good, use pointers instead
        #     root.right = self.sortedArrayToBST(nums[middle_idx+1:])           # slicing uses some time complexity
        #     return root

        # SOLUTION 2
        def helper(l, r):
            if l > r:
                return None
            else:
                m = (l + r) // 2
                root = TreeNode(nums[m])
                root.left = helper(l, m - 1)
                root.right = helper(m + 1, r)
                return root

        return helper(0, len(nums) - 1)
