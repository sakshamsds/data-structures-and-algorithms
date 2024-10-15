class Solution:
    def minimumSteps(self, s: str) -> int:
        zeros, res = 0, 0
        for i in range(len(s)):
            if s[i] == '0':
                res += i - zeros
                zeros += 1
        return res
