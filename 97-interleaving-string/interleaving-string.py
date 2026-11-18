class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        cache = {}

        def dfs(i, j, k):
            if k == len(s3):
                return True
            key = (i, j, k)
            if key in cache:
                return cache[key]

            valid = i < len(s1) and s1[i] == s3[k] and dfs(i + 1, j, k + 1) or \
                j < len(s2) and s2[j] == s3[k] and dfs(i, j + 1, k + 1)
            
            cache[key] = valid
            return valid

        return dfs(0, 0, 0)

