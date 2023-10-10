class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = dict()
        for i, num in enumerate(nums):
            if target - num in store:
                return [store[target - num], i] 
            else:
                store[num] = i
        return [-1, -1]