'''
longest common subsequence

delete
leet

lee
let

i, j

delete i, i + 1
delete j, j + 1
don't delete only if equal, i + 1, j + 1



'''


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        @cache
        def dfs(i, j):
            if i == len(s1) or j == len(s2):
                deleted = 0
                for k in range(i, len(s1)):
                    deleted += ord(s1[k])
                for k in range(j, len(s2)):
                    deleted += ord(s2[k])
                return deleted

            min_del = min(ord(s1[i]) + dfs(i + 1, j), ord(s2[j]) + dfs(i, j + 1))
            if s1[i] == s2[j]:
                min_del = min(min_del, dfs(i + 1, j + 1))

            return min_del
        return dfs(0, 0)