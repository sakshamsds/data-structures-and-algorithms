class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        l, r = 0, 0
        cur_max = 1
        overall_max = 1

        while r < len(nums) - 1:
            if nums[r + 1] > nums[r]:
                cur_max += 1
            else:
                l = r + 1
                cur_max = 1

            r += 1
            overall_max = max(overall_max, cur_max)

        return overall_max