class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freqs = collections.defaultdict(int)
        l, res = 0, 0
        for r in range(len(nums)):
            freqs[nums[r]] += 1
            while freqs[nums[r]] > k and l <= r :
                freqs[nums[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res