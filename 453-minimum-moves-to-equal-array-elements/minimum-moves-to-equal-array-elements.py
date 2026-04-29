'''
    1   2   3
    1   2   1   2
    1   1   1   3

    1   2   3   4
    1   1   1   1   6

    1   2   2   3
    1   2   2   1   2
    2   3   3   3
    3   4   4   3
    4   5   4   4
    5   5   5   5

    1   3   3  (2 + 2)
'''

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # decrease one element by 1
        operations = 0
        min_num = min(nums)
        for num in nums:
            operations += num - min_num
        return operations
