class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        odd_freq = collections.defaultdict(int)
        even_freq = collections.defaultdict(int)

        for i, num in enumerate(nums):
            if i & 1 == 0:
                even_freq[num] += 1
            else:
                odd_freq[num] += 1

        def getMostFreq(freq_map, skip=-1):
            max_freq, most_occ = 0, -1
            for num, freq in freq_map.items():
                if num != skip and freq > max_freq:
                    max_freq, most_occ = freq, num
            return most_occ, max_freq

        most_freq_odd, max_freq_odd = getMostFreq(odd_freq)
        most_freq_even, max_freq_even = getMostFreq(even_freq)

        if most_freq_even != most_freq_odd:
            return len(nums) - max_freq_odd - max_freq_even

        _, second_max_odd_freq = getMostFreq(odd_freq, most_freq_odd)
        _, second_max_even_freq = getMostFreq(even_freq, most_freq_even)

        return len(nums) - max(max_freq_odd + second_max_even_freq, max_freq_even + second_max_odd_freq)
