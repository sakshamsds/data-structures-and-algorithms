from collections import deque, namedtuple

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        all_mask = (1 << n) - 1
        visited = set()
        Node = namedtuple('Node', ['node', 'mask', 'cost'])

        q = deque()
        for i in range(n):
            mask_value = (1 << i)
            this_node = Node(i, mask_value, 1)
            q.append(this_node)
            visited.add((i, mask_value))

        # print(q)
        # print(visited)

        while q:
            cur = q.popleft()
            if cur.mask == all_mask:
                return cur.cost - 1

            for adj in graph[cur.node]:
                both_visited_mask = cur.mask | (1 << adj)
                this_node = Node(adj, both_visited_mask, cur.cost + 1)

                if (adj, both_visited_mask) not in visited:
                    visited.add((adj, both_visited_mask))
                    q.append(this_node)
        return -1