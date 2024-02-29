# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        level = 0
        while q:
            level_size = len(q)
            odd_lvl = level % 2 
            prev = float('inf') if odd_lvl else 0
            # print(lvl_num, prev)
            for _ in range(level_size):
                cur = q.popleft()
                if odd_lvl:
                    if cur.val % 2 == 1 or prev <= cur.val:
                        return False
                else:       # even lvl
                    if cur.val % 2 == 0 or prev >= cur.val:
                        return False
                if cur.left: 
                    q.append(cur.left)
                if cur.right: 
                    q.append(cur.right)
                prev = cur.val
            level += 1
        return True