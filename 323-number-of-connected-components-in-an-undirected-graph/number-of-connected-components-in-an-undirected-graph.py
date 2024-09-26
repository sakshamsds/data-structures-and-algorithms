class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(node: int) -> int:
            p = parent[node]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(n1: int, n2: int) -> int:
            p1, p2 = find(n1), find(n2)

            if p1 == p2:    # if already connected
                return 0

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return 1

        num_components = n
        for s, e in edges:
            num_components -= union(s, e)
        
        return num_components
