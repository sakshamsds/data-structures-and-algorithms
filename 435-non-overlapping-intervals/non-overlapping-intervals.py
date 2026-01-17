class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev_s, prev_e = intervals[0]
        removals = 0

        for i in range(1, len(intervals)):  # check over lap with previous            
            nxt_s, nxt_e = intervals[i]

            if prev_e <= nxt_s:     # no overlap
                prev_s, prev_e = nxt_s, nxt_e
                continue

            # overlap
            removals += 1

            # the one that ends first is to be removed
            if nxt_e < prev_e:
                prev_s, prev_e = nxt_s, nxt_e

        return removals