class Solution:
    def clearDigits(self, s: str) -> str:
        res = []
        cnt = 0
        for c in reversed(s):
            if 'a' <= c <= 'z':
                if cnt > 0:
                    cnt -= 1
                else:
                    res.append(c)
            else:
                cnt += 1
        return ''.join(res[::-1])
                