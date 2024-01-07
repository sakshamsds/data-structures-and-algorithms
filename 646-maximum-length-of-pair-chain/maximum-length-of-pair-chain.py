class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        # for every pair, we have two options, either take it or leave it
        cache = {}
        def dfs(i):
            if i == len(pairs):
                return 0

            if i in cache:
                return cache[i]

            length = dfs(i + 1)  # we didn't choose current pair

            j = i + 1       # we choose the current pair
            while j < len(pairs) and pairs[i][1] >= pairs[j][0]:
                j += 1
            length = max(length, 1 + dfs(j))
            cache[i] = length
            return length
        return dfs(0)