class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        uniques = set()
        self.mx_count = 1

        def backtrack(i):
            if len(s) - i + len(uniques) <= self.mx_count:
                return

            if i == len(s):
                self.mx_count = max(self.mx_count, len(uniques))

            for j in range(i + 1, len(s) + 1):
                if s[i:j] not in uniques:
                    uniques.add(s[i:j])
                    backtrack(j)
                    uniques.remove(s[i:j])

            return 

        backtrack(0)
        return self.mx_count
        