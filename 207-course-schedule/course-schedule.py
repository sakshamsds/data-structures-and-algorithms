class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # iterate through all the courses
        # adj list, course -> [preq1, preq2]
        # if preq is [], return True
        # Time complexity O(N + E)

        adjList = collections.defaultdict(list)
        for course, preq in prerequisites:
            adjList[course].append(preq)
        visited = set()

        def dfs(course):
            if course in visited:       # chain detected
                return False
            if not adjList[course]:
                return True
            visited.add(course)

            for preq in adjList[course]:
                if not dfs(preq):
                    return False
            adjList[course] = []
            visited.remove(course)
            return True

        for i in range(numCourses):
            if i not in visited and not dfs(i):
                return False

        return True