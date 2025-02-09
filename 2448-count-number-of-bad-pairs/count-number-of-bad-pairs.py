'''
    4   1   3   3
    0   1   2   3
    4   0   1   0

1
6 - 1

3 * 2 - 1

0 - 2
4 - 1
1 - 1

'''

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        diffs = collections.defaultdict(int)
        for i, num in enumerate(nums):
            diffs[num - i] += 1

        n = len(nums)
        total = n * (n - 1) // 2
        for d in diffs.values():
            total -= d * (d - 1) // 2

        return total