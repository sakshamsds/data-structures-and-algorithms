class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freqs = {c: 0 for c in 'abc'}
        left = total = 0
        for right in range(len(s)):
            freqs[s[right]] += 1
            while all(freqs.values()):
                total += len(s) - right
                freqs[s[left]] -= 1
                left += 1
        return total