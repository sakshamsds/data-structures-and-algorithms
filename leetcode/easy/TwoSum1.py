from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = {}
        for i, num in enumerate(nums):
            if num not in idx_map:
                idx_map[target - num] = i            # find this number later
            else:
                return [idx_map[num], i]
        
        return False

