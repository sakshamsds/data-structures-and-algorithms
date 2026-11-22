class Solution:
    def minMoves(self, nums: list[int]) -> int:
        # make larger numbers smallers
        # one pass
        moves = 0
        minNum = nums[0]
        for i, num in enumerate(nums):
            if num < minNum:
                moves += (minNum - num) * i
                minNum = num
            else:
                moves += num - minNum
            # print(moves)
        return moves

