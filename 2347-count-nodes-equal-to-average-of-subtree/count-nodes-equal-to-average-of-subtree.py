# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        # post order traversal
        self.cnt = 0

        def dfs(node):
            subtree_sum = node.val
            subtree_cnt = 1

            if node.left:
                l_sum, l_cnt = dfs(node.left)
                subtree_sum += l_sum
                subtree_cnt += l_cnt

            if node.right:
                r_sum, r_cnt = dfs(node.right)
                subtree_sum += r_sum
                subtree_cnt += r_cnt

            avg = subtree_sum // subtree_cnt
            if avg == node.val:
                self.cnt += 1
            
            return subtree_sum, subtree_cnt
            
        dfs(root)
        return self.cnt