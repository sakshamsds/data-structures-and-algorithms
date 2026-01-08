class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj_list = collections.defaultdict(list)
        indegrees = [0] * n
        for prev, nxt in relations:
            prev, nxt = prev - 1, nxt - 1
            indegrees[nxt] += 1          
            adj_list[prev].append(nxt)

        q = collections.deque()
        for course, indegree in enumerate(indegrees):
            if indegree == 0:
                q.append(course)

        studied = len(q)
        num_semesters = 0
        while q:
            num_semesters += 1
            for _ in range(len(q)):         # take all in current semester
                course = q.popleft()
                for nxt in adj_list[course]:
                    indegrees[nxt] -= 1
                    if indegrees[nxt] == 0:
                        q.append(nxt)
                        studied += 1

        return num_semesters if studied == n else -1