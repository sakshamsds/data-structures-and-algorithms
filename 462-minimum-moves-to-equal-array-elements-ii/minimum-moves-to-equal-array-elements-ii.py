class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        middleIdx = len(nums) // 2
        median = nums[middleIdx]
        moves = 0
        for num in nums:
            moves += abs(median - num)
        return moves