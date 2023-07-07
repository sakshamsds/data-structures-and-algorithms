# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # level order traversal
        max_sum = float("-inf")
        max_level, cur_level = 1, 0
        q = deque()
        q.appendleft(root)
        while q:
            cur_level += 1
            size = len(q)
            # size = len(q)
            cur_level_sum = 0
            for _ in range(size):
                cur = q.pop()
                cur_level_sum += cur.val
                if cur.left:
                    q.appendleft(cur.left)
                if cur.right:
                    q.appendleft(cur.right)

            print(cur_level, cur_level_sum, max_sum)
            
            if cur_level_sum > max_sum:
                max_sum = cur_level_sum
                max_level = cur_level

        return max_level
    
# print(Solution().maxLevelSum(TreeNode(1, TreeNode(7, TreeNode(7), TreeNode(-8)), TreeNode(0))))
# print(Solution().maxLevelSum(TreeNode(989, left=None, right=TreeNode(10250, TreeNode(98693), TreeNode(-89388, left=None, right=TreeNode(-32127))))))
# print(Solution().maxLevelSum(TreeNode(-100, TreeNode(-200, TreeNode(-20), TreeNode(-5)), TreeNode(-300, TreeNode(-10)))))