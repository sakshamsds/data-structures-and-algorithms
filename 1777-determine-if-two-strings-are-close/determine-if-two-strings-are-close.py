'''
cabbba -> 2a 3b 1c
abbccc -> 1a 2b 3c

a > b, b > a
3a 2b 1c
'''

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # if we can make them anagrams of each other, return true
        if len(word1) != len(word2):    
            return False

        if set(word1) != set(word2):    # 2nd op with existing letters only
            return False

        return sorted(Counter(word1).values()) == sorted(Counter(word2).values())