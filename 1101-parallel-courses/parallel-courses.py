class Solution:
    def minimumSemesters(self, n: int, relations: list[list[int]]) -> int:
        adjList = collections.defaultdict(list)
        indegree = [0] * (n + 1)

        for prevC, nextC in relations:
            adjList[prevC].append(nextC)
            indegree[nextC] += 1

        q = deque()
        for course, indeg in enumerate(indegree):
            if indeg == 0:
                q.append(course)

        semesters = 0
        while q:
            semesters += 1
            for _ in range(len(q)):
                course = q.popleft()
                for nbr in adjList[course]:
                    indegree[nbr] -= 1
                    if indegree[nbr] == 0:
                        q.append(nbr)
        return semesters if sum(indegree) == 0 else -1