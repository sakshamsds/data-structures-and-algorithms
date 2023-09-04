class Solution:
    def reverseVowels(self, s: str) -> str:
        
        res = [char for char in s]
        l, r = 0, len(s) - 1

        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        # print(res)
        while l < r:
            # print(l, r)
            if res[l] in vowels:
                if res[r] in vowels:
                    res[l], res[r] = res[r], res[l]
                    l += 1
                r -= 1
            else:
                l += 1

        return ''.join(res)
            