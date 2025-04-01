class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        cache = {}

        def dfs(i):
            if i >= len(questions):
                return 0
            
            if i in cache:
                return cache[i]
            
            # choose i
            pts = questions[i][0] + dfs(i + questions[i][1] + 1)

            # do no choose i
            pts = max(pts, dfs(i + 1))

            cache[i] = pts
            return pts

        return dfs(0)


