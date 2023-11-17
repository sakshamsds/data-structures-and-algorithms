class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = collections.defaultdict(list)     # course -> prereq
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)

        visited = set()
        def dfs(course):
            if adj_list[course] == []:      # base condition 1
                return True
            if course in visited:           # base condition 2
                return False

            visited.add(course)
            for prereq in adj_list[course]:     # directed graph
                if not dfs(prereq):
                    return False

            visited.remove(course)
            adj_list[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
