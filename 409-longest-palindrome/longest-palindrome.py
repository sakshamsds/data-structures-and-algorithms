class Solution:
    def longestPalindrome(self, s: str) -> int:
        # get freq of all elements
        # even freq will add to palindrom
        # get the largest odd freq
        freqs = collections.Counter(s).values()
        longest = 0
        odd_exists = False
        for freq in freqs:
            if freq % 2 == 0:
                longest += freq
            else:
                odd_exists = True
                longest += freq - 1
        return longest + int(odd_exists)