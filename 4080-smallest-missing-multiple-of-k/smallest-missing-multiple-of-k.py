class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)

        for x in range(1, len(nums) + 2):
            multiple = k * x
            if multiple not in nums:
                return multiple

        return -1