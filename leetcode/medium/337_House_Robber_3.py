# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # post order traversal
        def dfs(root):
            if root is None:
                return [0, 0]
            
            #(looted, not looted)
            #(with root, not with root)
            left_pair = dfs(root.left)
            right_pair = dfs(root.right)
            with_root = root.val + left_pair[1] + right_pair[1]
            without_root = max(left_pair) + max(right_pair)
            return [with_root, without_root]

            #(not looted, looted)
            # not_rob_c = max(not_rob_l, rob_l) + max(not_rob_r, rob_r) 
            # not_rob_c = max(not_rob_l + not_rob_r,  # if we don't rob cur
            #                 rob_l + rob_r,          # then any comb will work
            #                 not_rob_l + rob_r,
            #                 rob_l + not_rob_r) 
            # rob_c = not_rob_l + not_rob_r + root.val
            # return not_rob_c, rob_c

        return max(dfs(root))