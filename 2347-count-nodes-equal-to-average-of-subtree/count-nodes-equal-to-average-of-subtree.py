# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        # post order traversal
        res = 0

        def dfs(node):
            nonlocal res 
        
            if node is None:
                return 0, 0

            l_sum, l_cnt = dfs(node.left)
            r_sum, r_cnt = dfs(node.right)

            subtree_sum = node.val + l_sum + r_sum
            subtree_cnt = 1 + l_cnt + r_cnt

            avg = subtree_sum // subtree_cnt
            if avg == node.val:
                res += 1
            
            return subtree_sum, subtree_cnt
            
        dfs(root)
        return res