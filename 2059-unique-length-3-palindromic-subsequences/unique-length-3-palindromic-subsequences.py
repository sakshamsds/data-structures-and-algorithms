class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # precompute indices
        left_indices, right_indices = [-1] * 26, [-1] * 26

        for i, c in enumerate(s):
            char_idx = ord(c) - ord('a')
            if left_indices[char_idx] == -1:
                left_indices[char_idx] = i
            else:
                right_indices[char_idx] = i

        total = 0
        for i in range(26):
            if left_indices[i] != -1 and right_indices[i] != -1:
                l, r = left_indices[i], right_indices[i]
                total += len(set(s[l + 1:r]))

        return total
