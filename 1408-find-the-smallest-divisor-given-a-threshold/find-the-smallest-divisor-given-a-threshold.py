class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)

        def divisorSum(div):
            d_sum = 0
            for num in nums:
                d_sum += ceil(num/div)
            return d_sum

        while l < r:
            mid = l + (r - l) // 2
            cur_sum = divisorSum(mid)
            if cur_sum > threshold:
                l = mid + 1
            else:
                r = mid

        return l