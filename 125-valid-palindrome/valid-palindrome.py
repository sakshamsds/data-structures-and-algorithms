class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        def isAlphaNumeric(c):
            return 'a' <= c.lower() <= 'z' or '0' <= c <= '9'

        while l < r:
            if not isAlphaNumeric(s[l]):
                l += 1
                continue
            if not isAlphaNumeric(s[r]):
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True