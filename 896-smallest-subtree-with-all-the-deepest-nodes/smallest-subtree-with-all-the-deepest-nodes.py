# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # find max depth and number of nodes at that depth
        q = collections.deque([root])
        lvl = 0
        while q:
            lvl += 1
            lvl_size = len(q)
            for _ in range(lvl_size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        max_depth, num_nodes = lvl, lvl_size
        # print(root.val, max_depth, num_nodes)
        self.deepest_subtree, self.subtree_depth = root, 1

        def dfs(node, depth):
            if not node:
                return 0
            depth_nodes = 1 if depth == max_depth else 0
            depth_nodes += dfs(node.left, 1 + depth) + dfs(node.right, 1 + depth)
            if depth_nodes == num_nodes and depth > self.subtree_depth:
                self.deepest_subtree, self.subtree_depth = node, depth
            return depth_nodes
        
        dfs(root, 1)
        return self.deepest_subtree
