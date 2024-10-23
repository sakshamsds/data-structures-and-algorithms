# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumLevel(self, root: Optional[TreeNode]) -> int:
        
        q = deque([root])
        min_sum, min_sum_lvl = float('inf'), 0
        lvl = 1

        while q:
            lvl_sum = 0
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                lvl_sum += cur.val
            if lvl_sum < min_sum:
                min_sum, min_sum_lvl = lvl_sum, lvl
            lvl += 1

        return min_sum_lvl
            
                