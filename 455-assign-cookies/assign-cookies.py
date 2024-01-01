class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        cookie_ptr = 0
        cnt = 0
        for i in range(len(g)):
            while cookie_ptr < len(s) and s[cookie_ptr] < g[i]:
                cookie_ptr += 1
            if cookie_ptr < len(s) and s[cookie_ptr] >= g[i]:   # current greed is statisfied:
                cnt += 1
                cookie_ptr += 1
            if cookie_ptr == len(s):
                return cnt

        return len(g)

            

             