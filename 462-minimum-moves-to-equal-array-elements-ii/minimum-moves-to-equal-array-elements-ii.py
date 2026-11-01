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
        # two pointers, we select k in between
        # contribution is (k - min) + (max - k) = max - min

        nums.sort()
        l, r, moves = 0, len(nums) - 1, 0
        while l < r:
            moves += nums[r] - nums[l]
            l += 1
            r -= 1
        
        return moves