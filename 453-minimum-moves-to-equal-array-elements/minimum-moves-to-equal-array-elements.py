'''
    1   2   3
1   1   2   2
2   1   1   2
3   1   1   1

    5       -10     0       2
    15      0       10      12

    1   2
    2   2

    1   1   10
    0   0   9

    1   3   3
    0   2   2

    2   4   3
    3   4   4
    4   5   4
    5   5   5
'''


class Solution:
    def minMoves(self, nums: list[int]) -> int:
        # increment n-1 elements == decrement 1 element by 1
        # make all the elemnts to the smalles
        smallest = min(nums)

        moves = 0
        for num in nums:
            moves += num - smallest

        return moves