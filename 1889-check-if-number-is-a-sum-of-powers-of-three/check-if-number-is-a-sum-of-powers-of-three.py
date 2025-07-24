'''
    1   2   3   4   5   6   7   8   9   10  11  12
    y       y                       y
'''

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # available
        powers = [3 ** i for i in range(20)]

        @cache
        def dfs(i, num):
            if num == 0:
                return True

            if num < powers[i]:
                return False

            return dfs(i + 1, num) or dfs(i + 1, num - powers[i])

        return dfs(0, n)