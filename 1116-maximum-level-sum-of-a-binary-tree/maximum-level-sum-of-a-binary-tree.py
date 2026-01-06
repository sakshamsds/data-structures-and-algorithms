# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = collections.deque([root])
        cur_level = 1
        level_max, max_value = 1, root.val

        while q:
            level_size = len(q)
            level_sum = 0
            for _ in range(level_size):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if level_sum > max_value:
                level_max, max_value = cur_level, level_sum
            cur_level += 1

        return level_max




        