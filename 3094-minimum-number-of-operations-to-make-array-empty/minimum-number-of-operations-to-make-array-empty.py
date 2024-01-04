class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq_dict = collections.Counter(nums)
        ops = 0
        for _, freq in freq_dict.items():
            if freq == 1:
                return -1
            ops += ceil(freq / 3)
        return ops