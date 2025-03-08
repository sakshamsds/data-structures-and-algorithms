class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        cur_vowels = max_vowels = 0
        for i in range(k - 1):
            if s[i] in vowels:
                cur_vowels += 1

        for i in range(k - 1, len(s)):
            if s[i] in vowels:
                cur_vowels += 1
            max_vowels = max(max_vowels, cur_vowels)
            if s[i - k + 1] in vowels:
                cur_vowels -= 1

        return max_vowels
