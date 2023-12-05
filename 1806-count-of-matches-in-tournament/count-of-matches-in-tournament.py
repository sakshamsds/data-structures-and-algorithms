class Solution:
    def numberOfMatches(self, n: int) -> int:
        # n teams, 1 winner, n - 1 losers
        # each match eliminates 1 team
        return n - 1

        # res = 0
        # while n > 1:
            # res += n // 2
            # n = ceil(n / 2)
        # return res