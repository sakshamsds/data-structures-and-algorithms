class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        ns, ne = newInterval

        for i, interval in enumerate(intervals):
            s, e = interval
            if ns > e:      # cur < new
                res.append(interval)
            elif ne < s:    # new < cur
                res.append([ns, ne])
                res.extend(intervals[i:])
                return res
            else:       # overlaps
                ns, ne = min(ns, s), max(ne, e)

        res.append([ns, ne])
        return res
            
