'''
aeiouAEIOU
'''

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = 'aeiouAEIOU'
        num_vowels_left, num_vowels_right = 0, 0
        mid = len(s) // 2
        for i in range(mid):
            if s[i] in vowels:
                num_vowels_left += 1
        for i in range(mid, len(s), 1):
            if s[i] in vowels:
                num_vowels_right += 1
        # print(num_vowels_left, num_vowels_right)
        return num_vowels_left == num_vowels_right
            