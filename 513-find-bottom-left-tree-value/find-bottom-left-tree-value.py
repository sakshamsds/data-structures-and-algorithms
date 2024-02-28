# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # level order traversal, right to left
        q = deque([root])
        while q:
            level_size = len(q)
            for _ in range(level_size):
                cur = q.popleft()
                if cur.right:
                    q.append(cur.right)
                if cur.left:
                    q.append(cur.left)
        return cur.val
