class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        partitions = 1
        left = nums[0]

        for num in nums:
            if num - left > k:
                left = num
                partitions += 1

        return partitions