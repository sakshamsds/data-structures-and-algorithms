class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(target):
            l, cur_sum, res = 0, 0, 0
            for r in range(len(nums)):
                cur_sum += nums[r]
                while l <= r and cur_sum > target:
                    cur_sum -= nums[l]
                    l += 1
                res += r - l + 1
            return res
        return atMost(goal) - atMost(goal - 1)                 