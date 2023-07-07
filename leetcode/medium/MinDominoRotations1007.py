from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        size = len(tops)
        if size == 1:
            return 1
        
        values = [tops[0], bottoms[0]]
        for val in values:
            missing_top, missing_bot = 0, 0
            for i in range(size):
                if tops[i] != val and bottoms[i] != val: break
                if tops[i] != val: missing_top += 1
                if bottoms[i] != val: missing_bot += 1
                if i == size - 1:
                    return min(missing_bot, missing_top)
        return -1


print(Solution().minDominoRotations([2,1,2,4,2,2], [5,2,6,2,3,2]))
print(Solution().minDominoRotations([5,2,6,2,3,2], [2,1,2,4,2,2]))
print(Solution().minDominoRotations([3,5,1,2,3], [3,6,3,3,4]))
print(Solution().minDominoRotations([1,2,1,1,1,2,2,2], [2,1,2,2,2,2,2,2]))      # 1