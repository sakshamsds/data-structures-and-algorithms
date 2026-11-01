'''
    1   2   3
    sorting required?
    # O(2n)?

    median?
    mean?

    1   2   9   01
5   4   3   4   5
6   5   4   3   4

    1   0   0   8   6
3   2   3   3   5   3
4   3   4   4   4   2
2   1   2   2   6   4
1   0   1   1   7   5
'''

class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)

        if n & 1 == 0:
            median = (nums[(n - 1) // 2] + nums[n // 2]) // 2
        else:
            median = nums[(n - 1) // 2]
        # print(median)

        moves = 0
        for num in nums:
            moves += abs(median - num)
        return moves