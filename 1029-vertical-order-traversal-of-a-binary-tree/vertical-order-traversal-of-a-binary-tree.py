# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
        store = collections.defaultdict(list)       # (r, c) -> nodes

        mn_col, mx_col = float('inf'), float('-inf')
        q = deque([(root, 0)])     # node, col
        rows = 0
        while q:
            for _ in range(len(q)):
                node, col = q.popleft()
                store[(rows, col)].append(node.val)
                mn_col = min(mn_col, col)
                mx_col = max(mx_col, col)
                if node.left:
                    q.append((node.left, col - 1))
                if node.right:
                    q.append((node.right, col + 1))
            rows += 1

        # print(store)

        res = []
        for c in range(mn_col, mx_col + 1):
            column = []
            for r in range(rows):
                if (r, c) in store:
                    column.extend(sorted(store[(r, c)]))
            res.append(column)
        return res
        