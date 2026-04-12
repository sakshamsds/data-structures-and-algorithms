'''
    W1  
    W2
    who gets the next letter
'''

class Solution:
    def minimumDistance(self, word: str) -> int:
        coord = {}
        k = 0
        for r in range(5):
            for c in range(6):
                coord[k] = (r, c)
                k += 1

        # print(coord)
        cache = {}

        def dfs(i, r1, c1, r2, c2):
            if i == len(word):
                return 0

            key = (i, r1, c1, r2, c2)
            if key in cache:
                return cache[key]

            minCost = float(inf)
            nr, nc = coord[ord(word[i]) - ord('A')]

            # pick f1
            costF1 = 0 if r1 == -1 else abs(r1 - nr) + abs(c1 - nc)
            minCost = min(minCost, dfs(i + 1, nr, nc, r2, c2) + costF1)

            # pick f2
            costF2 = 0 if r2 == -1 else abs(r2 - nr) + abs(c2 - nc)
            minCost = min(minCost, dfs(i + 1, r1, c1, nr, nc) + costF2)

            cache[key] = minCost
            return minCost

        return dfs(0, -1, -1, -1, -1)