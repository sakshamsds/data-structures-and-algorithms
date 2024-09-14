class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = max(nums)
        longest, cur_len = 1, 0
        for num in nums:
            if num == mx:
                cur_len += 1
            else:
                cur_len = 0
            longest = max(longest, cur_len)
        return longest