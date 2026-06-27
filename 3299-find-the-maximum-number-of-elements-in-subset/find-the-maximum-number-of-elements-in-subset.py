class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        dp = dict()         # start -> maxLength
        freqs = collections.Counter(nums)

        # handle edge case
        maxOnes = freqs[1] if freqs[1] & 1 == 1 else freqs[1] - 1
        freqs.pop(1, None)
        dp[1] = maxOnes

        # print (freqs)
        for start, freq in freqs.items():
            # print(start, freq)
            if freq == 1:
                dp[start] = 1
                continue

            length = 1
            nxt = start * start
            while nxt in freqs:
                length += 1
                if freqs[nxt] == 1:
                    break
                nxt *= nxt

            dp[start] = 2 * length - 1

        # print(dp)
        return max(dp.values())