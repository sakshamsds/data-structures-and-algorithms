# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        store = collections.defaultdict(list)
        min_col, max_col = 0, 0
        q = collections.deque([(root, 0)])
        while q:
            lvl_size = len(q)
            for _ in range(lvl_size):
                node, col = q.popleft()
                store[col].append(node.val)

                if node.left:
                    min_col = min(min_col, col - 1)
                    q.append((node.left, col - 1))
                if node.right:
                    max_col = max(max_col, col + 1)
                    q.append((node.right, col + 1))

        res = []
        for i in range(min_col, max_col + 1):
            res.append(store[i])
        return res

