class Solution:
    def countSuffix(self, nums: list[int], target: list[int]) -> int:
        if collections.Counter(nums) != collections.Counter(target):
            return 0

        n = len(nums)
        p = 0
        while p < n and nums[p] == target[p]:
            p += 1

        q = n - 1
        while q > 0 and target[q - 1] >= target[q]:
            q -= 1

        highBound = min(p, n - 1)
        return max(0, highBound - q + 1)