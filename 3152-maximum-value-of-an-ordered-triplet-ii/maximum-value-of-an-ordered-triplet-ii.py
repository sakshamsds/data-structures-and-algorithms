class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        res, imax, dmax = 0, 0, 0
        for num in nums:
            res = max(res, dmax * num)
            dmax = max(dmax, imax - num)
            imax = max(imax, num)
        return res