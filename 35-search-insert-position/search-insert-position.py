class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = l + (r - l) // 2
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid
        return l
