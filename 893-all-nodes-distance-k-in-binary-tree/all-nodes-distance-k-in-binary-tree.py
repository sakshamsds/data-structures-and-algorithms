# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj_list = collections.defaultdict(list)

        def dfs(node):
            if node.left:
                adj_list[node.val].append(node.left.val)
                adj_list[node.left.val].append(node.val)
                dfs(node.left)
            
            if node.right:
                adj_list[node.val].append(node.right.val)
                adj_list[node.right.val].append(node.val)
                dfs(node.right)

        dfs(root)
        # print(adj_list)
        q = collections.deque([target.val])
        visited = {target.val}
        while k > 0 and q:
            # print(q)
            level_size = len(q)
            for _ in range(level_size):
                cur = q.popleft()
                for nbr in adj_list[cur]:
                    if nbr not in visited:
                        q.append(nbr)
                        visited.add(nbr)
            k -= 1
        # print(q)
        return list(q)
