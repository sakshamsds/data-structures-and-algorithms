class Solution:

    def all_palindromes(self, substrings):
        for s in substrings:
            if s != s[::-1]:
                return False
        return True

    def partition(self, s: str) -> List[List[str]]:
        valid = []
        res = []

        def backtrack(i):
            if i == len(s):
                if self.all_palindromes(res):
                    valid.append(res.copy())
                return

            # case 1
            res.append(s[i])
            backtrack(i + 1)
            res.pop()

            # case 2
            if res:
                res[-1] = res[-1] + s[i]
                backtrack(i + 1)
                res[-1] = res[-1][:-1]
            return

        backtrack(0)
        return valid

