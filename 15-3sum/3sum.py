class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        nums.sort()
        res = []

        prev = None
        for i in range(len(nums)):
            if nums[i] == prev:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]
                if cur_sum > target:
                    r -= 1
                elif cur_sum < target:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    cur = nums[l]
                    while nums[l] == cur and l < r:
                        l += 1
            prev = nums[i]
        return res