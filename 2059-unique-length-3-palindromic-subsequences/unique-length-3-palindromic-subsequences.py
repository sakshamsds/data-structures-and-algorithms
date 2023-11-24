class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)

        count = 0
        for letter in letters:
            l, r = s.index(letter), s.rindex(letter)
            count += len(set(s[l + 1:r]))

        return count