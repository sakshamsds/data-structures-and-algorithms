class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev_e = intervals[0][1]
        removals = 0

        for i in range(1, len(intervals)):  # check over lap with previous            
            nxt_s, nxt_e = intervals[i]

            if prev_e <= nxt_s:     # no overlap
                prev_e = nxt_e
            else:
                removals += 1
                prev_e = min(prev_e, nxt_e)

        return removals