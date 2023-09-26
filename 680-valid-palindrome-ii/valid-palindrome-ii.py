class Solution:
    def validPalindrome(self, s: str) -> bool:

        def helper(inpt):
            # print(inpt)
            n = len(inpt)
            for j in range(n // 2):
                if inpt[j] != inpt[n - 1 - j]:
                    return False
            return True

        size = len(s)
        for i in range(size // 2):
            if s[i] != s[size - i - 1]:
                return helper(s[i:size - i - 1]) or helper(s[i + 1: size - i])

        return True



