'''
    unionfind won't tell us the answer

    adjList = dict() prereq -> nextCourse
    course -> set() of prereq
    prereq = {
        0: [1, 2],
        1: [],
        2: [1]
    }

    worst case scenario: 1 -> 2 -> 3 -> 4 -> 5
'''

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        adjList = collections.defaultdict(list)
        indegree = [0] * numCourses
        for src, dst in prerequisites:
            adjList[src].append(dst)
            indegree[dst] += 1

        q = deque()
        for node, indeg in enumerate(indegree):
            if indeg == 0:
                q.append(node)

        prereq = collections.defaultdict(set)

        while q:
            cur = q.popleft()
            for nbr in adjList[cur]:
                # extra step, add the prereqs of cur to nbr
                for pre in prereq[cur]:
                    prereq[nbr].add(pre)
                prereq[nbr].add(cur)

                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    q.append(nbr)

        res = []
        for src, dst in queries:
            if src in prereq[dst]:
                res.append(True)
            else:
                res.append(False)
        return res