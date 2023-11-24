class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # precompute the indices
        startIdxs = [-1] * 26
        endIdxs = [-1] * 26

        for i, char in enumerate(s):
            idx = ord('a') - ord(char)
            if startIdxs[idx] == -1:
                startIdxs[idx] = i

        for i in range(len(s) - 1, -1, -1):
            idx = ord('a') - ord(s[i])
            if endIdxs[idx] == -1:
                endIdxs[idx] = i

        count = 0
        for i in range(26):
            l, r = startIdxs[i], endIdxs[i]
            if l == -1:
                continue
            count += len(set(s[l + 1:r]))

        return count