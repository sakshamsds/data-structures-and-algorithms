class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freqs = collections.Counter(nums)

        # handle edge case
        maxLength = freqs[1] - 1 + (freqs[1] & 1)
        freqs.pop(1, None)
        
        for start, freq in freqs.items():
            length = 0
            while start in freqs:
                if freqs[start] == 1:
                    length += 1
                    break
                length += 2
                start *= start
            maxLength = max(maxLength, length - 1 + (length & 1))

        return maxLength