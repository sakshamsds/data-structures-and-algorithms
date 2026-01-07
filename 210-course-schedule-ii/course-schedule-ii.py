class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # preq -> course, b -> a

        adj_list = collections.defaultdict(list)
        indegrees = [0] * numCourses
        for course, preq in prerequisites:
            indegrees[course] += 1
            adj_list[preq].append(course)

        q = collections.deque()
        for course, indegree in enumerate(indegrees):
            if indegree == 0:
                q.append(course)

        topo_sort = []
        while q:
            preq = q.popleft()
            for course in adj_list[preq]:
                indegrees[course] -= 1
                if indegrees[course] == 0:
                    q.append(course)
            topo_sort.append(preq)

        if sum(indegrees) == 0:
            return topo_sort
        return []