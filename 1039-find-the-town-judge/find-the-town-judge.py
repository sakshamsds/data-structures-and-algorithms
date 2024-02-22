class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # incoming edges = n - 1
        # outgoing edges = 0
        incoming_edges = [0] * n
        outgoing_edges = [0] * n

        for start, end in trust:
            outgoing_edges[start - 1] += 1
            incoming_edges[end - 1] += 1

        for p in range(n):
            if incoming_edges[p] == n - 1 and outgoing_edges[p] == 0:
                return p + 1
        return -1