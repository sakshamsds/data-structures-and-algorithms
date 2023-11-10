class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        r = len(s) - 1
        res = []

        while r >= 0:
            if s[r] == '-':
                r -= 1
                continue

            size = 0
            while size < k and r >= 0:
                if s[r] != '-':
                    res.append(s[r].upper())
                    size += 1
                r -= 1
            res.append('-')

        # print(res)

        if len(res) > 0 and res[-1] == '-':
            res = res[:-1]

        return ''.join(res[::-1])