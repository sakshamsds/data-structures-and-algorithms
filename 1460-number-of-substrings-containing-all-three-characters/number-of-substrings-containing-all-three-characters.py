class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freqs = defaultdict(int)
        left = total = 0
        for right in range(len(s)):
            freqs[s[right]] += 1

            while freqs['a'] > 0 and freqs['b'] > 0 and freqs['c'] > 0:
                total += len(s) - right
                freqs[s[left]] -= 1
                left += 1
        return total