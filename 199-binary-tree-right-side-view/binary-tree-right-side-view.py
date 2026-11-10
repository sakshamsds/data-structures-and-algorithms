# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            res.append(q[0].val)
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.right:
                    q.append(cur.right)
                if cur.left:
                    q.append(cur.left)
        return res