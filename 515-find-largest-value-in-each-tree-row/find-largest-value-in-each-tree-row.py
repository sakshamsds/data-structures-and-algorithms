# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        # bfs
        q = collections.deque([root])
        res = []
        while q:
            level_size = len(q)
            row_max = float('-inf')
            for _ in range(level_size):
                cur = q.popleft()
                row_max = max(row_max, cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(row_max)
        return res
                