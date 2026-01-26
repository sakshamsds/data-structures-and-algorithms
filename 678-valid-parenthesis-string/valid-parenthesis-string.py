class Solution:
    def checkValidString(self, s: str) -> bool:
        
        @cache
        def dfs(i, left):
            if i == len(s):
                return left == 0
            if left < 0:
                return False

            if s[i] == '(':
                return dfs(i + 1, left + 1)

            if s[i] == ')':
                return dfs(i + 1, left - 1)

            # if s[i] = '*':
            return dfs(i + 1, left + 1) or dfs(i + 1, left) or dfs(i + 1, left - 1)

        return dfs(0, 0)