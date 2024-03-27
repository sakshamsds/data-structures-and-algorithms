class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l, pdt, res = 0, 1, 0
        for r in range(len(nums)):
            # print(l, r, res)
            pdt *= nums[r]
            while pdt >= k and l <= r:
                pdt /= nums[l]
                l += 1
            res += r - l + 1
            # how many valid subarrays ending at the r
        return res