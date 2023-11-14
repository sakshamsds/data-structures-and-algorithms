class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        vowels_in_s = []
        for char in s:
            if char in vowels:
                vowels_in_s.append(char)

        vowels_in_s.sort()
        # print(vowels_in_s)

        res = []
        i = 0
        for char in s:
            if char in vowels:
                res.append(vowels_in_s[i])
                i += 1
            else:
                res.append(char)

        return ''.join(res)
