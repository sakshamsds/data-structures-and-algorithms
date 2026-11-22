class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        adjList = collections.defaultdict(list)
        indegree = [0] * (n + 1)

        for prevC, nextC in relations:
            adjList[prevC].append(nextC)
            indegree[nextC] += 1

        q = deque()
        for course, indeg in enumerate(indegree):
            if indeg == 0:
                q.append(course)

        finishTimes = [0] * (n + 1)
        while q:
            course = q.popleft()        # we finished this course
            finishTimes[course] += time[course - 1]
            for nbr in adjList[course]:
                indegree[nbr] -= 1
                finishTimes[nbr] = max(finishTimes[nbr], finishTimes[course])
                if indegree[nbr] == 0:  # we can start this course
                    q.append(nbr)
        return max(finishTimes)