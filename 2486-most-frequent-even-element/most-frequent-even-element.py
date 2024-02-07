class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        c = Counter(nums)
        freq_num, mx_freq = -1, -1
        for num, freq in c.items():
            if num % 2 == 1:
                continue
            if freq > mx_freq or (freq == mx_freq and num < freq_num):
                freq_num, mx_freq = num, freq
        return freq_num
