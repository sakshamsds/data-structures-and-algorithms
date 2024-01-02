class Solution:
    def longestPalindrome(self, s: str) -> int:
        # get freq of all elements
        # even freq will add to palindrom
        # get the largest odd freq
        freqDict = collections.Counter(s)
        longest = 0
        odd_exists = False
        for _, freq in freqDict.items():
            if freq % 2 == 0:
                longest += freq
            else:
                odd_exists = True
                longest += freq - 1
        return longest + int(odd_exists)