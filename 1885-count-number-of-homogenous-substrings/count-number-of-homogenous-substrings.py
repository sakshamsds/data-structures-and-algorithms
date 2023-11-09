'''
zzzzz - 5
5 + 4 + 3 + 2 + 1
n * (n + 1) // 2
'''

class Solution:
    def countHomogenous(self, s: str) -> int:
        res = 0
        cnt = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cnt += 1
            else:       # once homogenity breaks add to res
                res += cnt * (cnt + 1) // 2
                # print(cnt)
                cnt = 1

        # print(cnt)
        res += cnt * (cnt + 1) // 2
        return int(res % (1e9 + 7))