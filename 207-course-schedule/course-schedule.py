class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # find a cycle in a directed graph

        indegree = [0] * numCourses
        adjList = collections.defaultdict(list)
        for course, prereq in prerequisites:            # end, start
            adjList[prereq].append(course)
            indegree[course] += 1                       # indegree[end] += 1

        q = deque()
        for prereq, indeg in enumerate(indegree):
            if indeg == 0:
                q.append(prereq)

        taken = 0
        while q:
            prereq = q.popleft()
            taken += 1
            for course in adjList[prereq]:
                indegree[course] -= 1
                if indegree[course] == 0:       # all prereq are taken/cleared
                    q.append(course)

        return taken == numCourses