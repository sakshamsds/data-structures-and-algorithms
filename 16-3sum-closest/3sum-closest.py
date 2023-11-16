class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('inf')

        n = len(nums)
        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                sum_3 = nums[i] + nums[l] + nums[r]
                if sum_3 > target:
                    r -= 1
                else:
                    l += 1
                if abs(target - sum_3) < abs(target - res):
                    res = sum_3

        return res
