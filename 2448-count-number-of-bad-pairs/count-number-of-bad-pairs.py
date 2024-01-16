'''
idxs - 0 1 2 3
nums - 4 1 3 3
diff - 4 0 1 0
total_pairs = 4 * 3 // 2 = 6
good_pairs = 2c2 = 1
bad_pairs = 4

nums[j] - j == nums[i] - i
'''

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total_pairs = n * (n - 1) // 2
        good_pairs = 0

        diffs = collections.defaultdict(int)
        for i, num in enumerate(nums):
            diffs[num - i] += 1

        for _, v in diffs.items():
            good_pairs += v * (v - 1) // 2

        return total_pairs - good_pairs
