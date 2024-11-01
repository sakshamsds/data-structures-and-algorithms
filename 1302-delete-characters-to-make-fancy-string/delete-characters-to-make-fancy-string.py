class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s

        res = [s[0], s[1]]
        for i in range(2, len(s)):
            if s[i] == res[-1] and s[i] == res[-2]:
                continue
            res.append(s[i])

        return ''.join(res)
