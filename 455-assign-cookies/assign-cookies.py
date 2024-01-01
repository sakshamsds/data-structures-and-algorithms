class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        cookie_ptr = 0
        for i in range(len(g)):
            while cookie_ptr < len(s) and s[cookie_ptr] < g[i]:
                cookie_ptr += 1
            if cookie_ptr == len(s):    # not able to find cookie for cur child
                return i
            cookie_ptr += 1         # cur cookie given to the child

        return len(g)

            

             