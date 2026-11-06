class Solution:
    def makePalindrome(self, s: str) -> bool:
        operations = 0
        l, r = 0, len(s) - 1
        while l < r and operations < 3:
            if s[l] != s[r]:
                operations += 1
            l += 1
            r -= 1

        return operations <= 2