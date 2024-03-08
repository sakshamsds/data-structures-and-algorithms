class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqs = defaultdict(int)
        res, max_freq = 0, -1
        for num in nums:
            f = freqs[num] + 1
            freqs[num] = f
            if f > max_freq:
                res, max_freq = f, f
            elif f == max_freq:
                res += f
        return res
