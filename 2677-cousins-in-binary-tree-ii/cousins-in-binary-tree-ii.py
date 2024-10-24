# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        lvl_sums = []

        while q:
            total = 0
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                total += cur.val
            lvl_sums.append(total)

        def dfs(node, lvl):
            if not node.left and not node.right:
                pass
            elif not node.left:
                node.right.val = lvl_sums[lvl + 1] - node.right.val
                dfs(node.right, lvl + 1)
            elif not node.right:
                node.left.val = lvl_sums[lvl + 1] - node.left.val
                dfs(node.left, lvl + 1)
            else:
                siblings_sum = node.left.val + node.right.val
                node.right.val = lvl_sums[lvl + 1] - siblings_sum
                node.left.val = node.right.val
                dfs(node.left, lvl + 1)
                dfs(node.right, lvl + 1)
            return
        
        dfs(root, 0)
        root.val = 0
        return root



            

        

                

