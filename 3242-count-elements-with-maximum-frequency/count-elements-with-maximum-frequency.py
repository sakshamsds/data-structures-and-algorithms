class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqs = collections.Counter(nums)
        max_freq = -1
        res = 0
        for k, f in freqs.items():
            if f > max_freq:
                max_freq, res = f, f
            elif f == max_freq:
                res += f
        return res