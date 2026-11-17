class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        pairs.sort(key = lambda x:(x[0], x[1]))
        chain = 0
        prev_end = -10000
        for start, end in pairs:
            if start <= prev_end:
                prev_end = min(prev_end, end)
            else:
                chain += 1
                prev_end = end
        return chain
