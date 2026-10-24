'''
    a   -   8
    b   -   5
    c   -   7
    d   -   14
    e   - 15
    f
    k
    l
                      r r  
    l               r l
    0 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 
    a b a b c b a c a d e  f e g d e 
'''


class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        l = 0
        last_idx = {}
        for i, c in enumerate(s):
            last_idx[c] = i

        r = 0
        sizes = []
        for i, c in enumerate(s):
            r = max(r, last_idx[c])

            if r == i:
                sizes.append(r - l + 1)
                l = i + 1
                r = i + 1
                
        return sizes