'''
42, 11, 1, 97
18, 0, 0, 18

2 3 4 2 1 2 1
1 + 2 + .. + (n - 1)
'''

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        # cal nums[i] - rev(nums[i])
        # store freqs in hashmap
        freqs = collections.defaultdict(int)

        for num in nums:
            diff = num - int(str(num)[::-1])
            freqs[diff] += 1

        res = 0
        for k, v in freqs.items():
            res += v * (v - 1) // 2    # sum upto v - 1
            res = int(res % (1e9 + 7))

        return res