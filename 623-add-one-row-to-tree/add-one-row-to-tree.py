# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)
        
        q = deque([root])
        lvl = 1

        while q:
            lvl_size = len(q)

            if lvl == depth - 1:
                for _ in range(lvl_size):
                    cur = q.popleft()
                    cur.left = TreeNode(val, cur.left, None)
                    cur.right = TreeNode(val, None, cur.right)
                return root

            for _ in range(lvl_size):
                cur = q.popleft()

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            lvl += 1

        return root



            
