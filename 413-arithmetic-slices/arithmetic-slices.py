class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # calculate valid subarrays from an index
        res = 0
        i = 0
        while i < len(nums) - 2:
            curLen = 2
            diff = nums[i + 1] - nums[i]
            for j in range(i + 2, len(nums)):
                if nums[j] - nums[j - 1] != diff:
                    break
                curLen += 1
                if curLen > 2:
                    res += curLen - 2
            if curLen > 2:
                i = j - 1
            else:
                i += 1

        return res
                