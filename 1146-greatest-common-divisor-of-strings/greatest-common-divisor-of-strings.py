class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        cur = ""
        res = cur
        for i in range(min(m, n)):
            cur += str1[i]
            # print(cur)

            if m % (i + 1) != 0 or n % (i + 1) != 0:
                continue

            if cur * (m // (i + 1)) == str1 and cur * (n // (i + 1)) == str2:
                res = cur

        return res
