class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        if nums[-1] >= nums[0]:  # check for monotonic increasing
            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    return False
        else:                   # check for monotonic decreasing
            for i in range(1, len(nums)):
                if nums[i] > nums[i - 1]:
                    return False

        return True