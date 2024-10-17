'''
.......................
                i
pF      W, E
'''

class Solution:
    def countWinningSequences(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        memo = {}
        n = len(s)

        def getPoints(a, b):
            if ((a == 'F' and b == 'E') or 
                (a == 'W' and b == 'F') or 
                (a == 'E' and b == 'W')):
                return -1

            if ((a == 'F' and b == 'W') or 
                (a == 'W' and b == 'E') or 
                (a == 'E' and b == 'F')):
                return 1
            return 0            

        # bob wins, add 1, alice wins, subtract 1
        def dfs(i, b_score, prev):   # O(n**2)
            # if remaining does not add up for negative, can stop here
            if n - i + b_score <= 0:
                return 0

            if i == n:
                return 1 if b_score > 0 else 0

            key = (i, b_score, prev)
            if key in memo:
                return memo[key]

            cnt = 0
            for b in 'FWE':
                if b != prev:
                    cnt += dfs(i + 1, b_score + getPoints(s[i], b), b)
            cnt %= MOD
            memo[key] = cnt
            return cnt

        return dfs(0, 0, None)