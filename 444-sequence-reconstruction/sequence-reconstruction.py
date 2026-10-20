class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        n = len(nums)
        indegree = [0] * (n + 1)
        adj_list = collections.defaultdict(list)

        for seq in sequences:
            for i in range(len(seq) - 1):
                start, end = seq[i], seq[i + 1]
                indegree[end] += 1
                adj_list[start].append(end)

        q = deque()
        for i in range(1, n + 1):
            if indegree[i] == 0:
                q.append(i)

        res = []
        while q:
            if len(q) > 1:
                return False
            cur = q.popleft()
            res.append(cur)
            for nbr in adj_list[cur]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    q.append(nbr)

        return res == nums




        