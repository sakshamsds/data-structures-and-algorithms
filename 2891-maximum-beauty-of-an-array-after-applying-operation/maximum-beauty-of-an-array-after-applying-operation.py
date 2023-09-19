class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # use hint
        nums.sort()
        l = 0
        res = 1
        for r in range(1, len(nums)):
            if nums[r] - nums[l] > 2 * k:
                l += 1
            res = max(res, r - l + 1)
            # print(l, r)
            
        # return r - l + 1
        return res