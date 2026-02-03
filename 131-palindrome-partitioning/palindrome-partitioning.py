class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        palindromes = []
        
        def backtrack(i):
            if i >= len(s):
                res.append(palindromes.copy())

            for j in range(i + 1, len(s) + 1):
                cur = s[i:j]
                if cur == cur[::-1]:
                    palindromes.append(cur)
                    backtrack(j)
                    palindromes.pop()

        backtrack(0)
        return res