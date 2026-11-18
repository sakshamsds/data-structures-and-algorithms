class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        target = 0
        nums.sort()
        N = len(nums)

        triplets = []
        prev = float('inf')
        for i in range(N):
            if nums[i] == prev:
                continue
            prev = nums[i]

            j, k = i + 1, N - 1
            while j < k:
                curSum = nums[i] + nums[j] + nums[k]
                if curSum > target:
                    k -= 1
                elif curSum < target:
                    j += 1
                else:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        return triplets