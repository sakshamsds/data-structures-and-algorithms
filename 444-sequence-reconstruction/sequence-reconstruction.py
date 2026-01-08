class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        n = len(nums)

        adj_list = collections.defaultdict(set)
        for seq in sequences:
            for i in range(len(seq) - 1):
                adj_list[seq[i]].add(seq[i + 1])
        # print(adj_list)

        indegree = [0] * (n + 1)
        for num, nbrs in adj_list.items():
            for node in nbrs:
                indegree[node] += 1
        # print(indegree)
        
        q = collections.deque()
        for num, degree in enumerate(indegree):
            if num != 0 and degree == 0:
                q.append(num)

        req_sequence = []
        while q:
            if len(q) > 1:  # more than 1 indegree element means more than 1 solution
                return False
            cur = q.popleft()
            req_sequence.append(cur)
            for nbr in adj_list[cur]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    q.append(nbr)

        # print('req', req_sequence)
        return req_sequence == nums