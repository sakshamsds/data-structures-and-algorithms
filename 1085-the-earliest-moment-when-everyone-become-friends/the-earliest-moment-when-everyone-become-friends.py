class Solution:
    def earliestAcq(self, logs: list[list[int]], n: int) -> int:
        
        def find(n):
            if n != parent[n]:
                parent[n] = find(parent[n])
            return parent[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 != p2:
                if size[p1] > size[p2]:
                    parent[p2] = p1
                    size[p1] += size[p2]
                else:
                    parent[p1] = p2
                    size[p2] += size[p1]
            return size[p1] == n or size[p2] == n

        parent = [i for i in range(n)]
        size = [1 for i in range(n)]

        logs.sort(key = lambda x : x[0])
        for ts, person1, person2 in logs:
            if union(person1, person2):
                return ts
        return -1