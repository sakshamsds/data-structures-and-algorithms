# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        col_nodes = collections.defaultdict(list)
        q = collections.deque([(root, 0)])
        min_col, max_col = 0, 0

        while q:
            lvl_size = len(q)
            for _ in range(lvl_size):
                node, col = q.popleft()
                col_nodes[col].append(node.val)
                min_col, max_col = min(min_col, col), max(max_col, col)

                if node.left:
                    q.append((node.left, col - 1))
                if node.right:
                    q.append((node.right, col + 1))

        vertical_order = []
        for col in range(min_col, max_col + 1):
            vertical_order.append(col_nodes[col])
        
        return vertical_order