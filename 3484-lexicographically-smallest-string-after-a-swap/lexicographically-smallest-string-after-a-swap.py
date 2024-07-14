class Solution:
    def getSmallestString(self, s: str) -> str:
        # check all adjacent pairs
        res = list(s)
        for i in range(0, len(res) - 1):
            l, r = int(res[i]), int(res[i + 1])
            if l <= r:
                continue 
            
            if l % 2 == r % 2:
                res[i], res[i + 1] = res[i + 1], res[i]
                break
        return ''.join(res)
