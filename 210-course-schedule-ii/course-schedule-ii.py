class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adjList = collections.defaultdict(list)
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            adjList[prereq].append(course)
            indegree[course] += 1

        q = deque([])
        for node, deg in enumerate(indegree):
            if deg == 0:
                q.append(node)

        order = []
        while q:
            cur = q.popleft()
            order.append(cur)
            for nbr in adjList[cur]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    q.append(nbr)
        return order if len(order) == numCourses else []