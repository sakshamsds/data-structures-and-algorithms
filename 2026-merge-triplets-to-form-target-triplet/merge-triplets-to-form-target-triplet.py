'''
    2   5   3
    1   7   5    
'''

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        mx, my, mz = target
        px, py, pz = 0, 0, 0
        for x, y, z in triplets:
            if x <= mx and y <= my and z <= mz:     # otherwise discard cur triplet
                px, py, pz = max(px, x), max(py, y), max(pz, z)
            if px == mx and py == my and pz == mz:
                return True

        return False