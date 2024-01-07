class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x : x[1])
        prevEnd, longest = -inf, 0
        for s, e in pairs:
            if s > prevEnd:
                prevEnd = e
                longest += 1
        return longest