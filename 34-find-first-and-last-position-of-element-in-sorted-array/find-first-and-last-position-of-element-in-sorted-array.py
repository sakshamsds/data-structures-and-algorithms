class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 or target < nums[0] or target > nums[-1]:
            return [-1, -1]
        
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        if nums[l] != target:
            return [-1, -1]

        res = [l, -1]

        r = len(nums) - 1
        while l < r:
            mid = l + (r - l + 1) // 2      # use mid biased to the right
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid

        res[1] = r
        return res