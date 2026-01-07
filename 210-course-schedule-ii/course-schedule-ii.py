class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # preq -> course, b -> a

        # adj_list = collections.defaultdict(list)
        # indegrees = [0] * numCourses
        # for course, preq in prerequisites:
        #     indegrees[course] += 1
        #     adj_list[preq].append(course)

        # q = collections.deque()
        # for course, indegree in enumerate(indegrees):
        #     if indegree == 0:
        #         q.append(course)

        # topo_sort = []
        # while q:
        #     preq = q.popleft()
        #     for course in adj_list[preq]:
        #         indegrees[course] -= 1
        #         if indegrees[course] == 0:
        #             q.append(course)
        #     topo_sort.append(preq)

        # if sum(indegrees) == 0:
        #     return topo_sort
        # return []

        adj_list = collections.defaultdict(list)
        indegree = [0] * numCourses                 # indegree for given courses
        for course, preq in prerequisites:
            indegree[preq] += 1
            adj_list[course].append(preq)

        q = collections.deque()                     # queue for processing
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        topo_sort = []
        while q:
            cur = q.popleft()
            for nbr in adj_list[cur]:               # remove indegree for the nbrs 
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    q.append(nbr)
            topo_sort.append(cur)

        if sum(indegree) == 0:
            return topo_sort[::-1]
        return []