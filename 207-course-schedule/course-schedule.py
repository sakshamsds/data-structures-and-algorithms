class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # kahn's algorithm, topological sort

        adj_list = collections.defaultdict(list)
        indegree = [0] * numCourses                 # indegree for given courses
        for course, preq in prerequisites:
            indegree[preq] += 1
            adj_list[course].append(preq)

        q = collections.deque()                     # queue for processing
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            cur = q.popleft()
            for nbr in adj_list[cur]:               # remove indegree for the nbrs 
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    q.append(nbr)

        return sum(indegree) == 0

         


