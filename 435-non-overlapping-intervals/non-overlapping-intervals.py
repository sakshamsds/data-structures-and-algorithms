class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        removals, prevEnd = 0, -float('inf')
        for s, e in intervals:
            # if overlap with prev, remove one with larger end
            if s < prevEnd: # overlap
                removals += 1
                prevEnd = min(prevEnd, e)
            else:
                prevEnd = e
        return removals