from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = list(zip(heights, names))
        res = sorted(res, reverse=True)
        return [name for _, name in res]
    
print(Solution().sortPeople(["Mary","John","Emma"], [180,165,170]))
