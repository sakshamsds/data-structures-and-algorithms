class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        removals = 0
        prev_e = -1_000_000

        for s, e in sorted(intervals):
            if s < prev_e:
                removals += 1
                prev_e = min(e, prev_e)
            else:
                prev_e = e
        return removals
