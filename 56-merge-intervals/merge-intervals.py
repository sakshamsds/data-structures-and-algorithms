class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()   
        merged_intervals = []
        i = 0
        while i < len(intervals):
            c_start, c_end = intervals[i]
            j = i + 1
            while j < len(intervals):
                n_start, n_end = intervals[j]
                if c_end < n_start: # doesn't overlap
                    break
                c_end = max(c_end, n_end)
                j += 1
            i = j       # overlaps till j - 1
            merged_intervals.append([c_start, c_end])
        return merged_intervals




