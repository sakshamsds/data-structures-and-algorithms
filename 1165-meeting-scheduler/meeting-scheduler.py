class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        p1, p2 = 0, 0
        slots1.sort()
        slots2.sort()

        while p1 < len(slots1) and p2 < len(slots2):
            s1, e1 = slots1[p1]
            s2, e2 = slots2[p2]

            # take intersection of two slots
            # see if intersection > duration
            s, e = max(s1, s2), min(e1, e2) 
            if e - s >= duration:
                return [s, s + duration]

            # increase the pointer for person whose slot ends first
            if e1 < e2:
                p1 += 1
            else:
                p2 += 1

        return []          
