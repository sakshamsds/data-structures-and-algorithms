'''
1 - 1
11 - 2
111 - 3
1111 - 4
'''

class Solution:
    def numSub(self, s: str) -> int:
        cnt, res = 0, 0

        for i in range(len(s)):
            if s[i] == '1':
                cnt += 1
            else:       # when you encounter 0
                res += (cnt * (cnt + 1) // 2) % (10 ** 9 + 7)
                cnt = 0

        res += (cnt * (cnt + 1) // 2) % (10 ** 9 + 7)
        return res



