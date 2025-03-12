class Solution:
    def maximumCount(self, nums: List[int]) -> int:      
        if nums[-1] < 0 or nums[0] > 0:
            return len(nums)

        # find index of first positive
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] <= 0:
                l = mid + 1
            else:
                r = mid
        pos = len(nums) - l if nums[l] > 0 else 0

        # idx of last negative number
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + 1 + (r - l) // 2
            if nums[mid] < 0:
                l = mid
            else:
                r = mid - 1

        neg = r + 1 if nums[r] < 0 else 0
        return max(neg, pos)