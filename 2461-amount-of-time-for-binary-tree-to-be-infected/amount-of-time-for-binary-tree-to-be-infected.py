# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # create an undirected graph
        adj_list = collections.defaultdict(list)

        def dfs(node):
            if node.left is not None:
                adj_list[node.left.val].append(node.val)
                adj_list[node.val].append(node.left.val)
                dfs(node.left)
            
            if node.right is not None:
                adj_list[node.right.val].append(node.val)
                adj_list[node.val].append(node.right.val)
                dfs(node.right)
            return

        dfs(root)
        # print(adj_list)

        # bfs from the start node
        minutes = -1
        q = collections.deque([start])
        visited = {start}

        while q:
            minutes += 1
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                visited.add(cur)
                for nbr in adj_list[cur]:
                    if nbr not in visited:
                        q.append(nbr)
                        # visited.add(nbr)

        return minutes

        