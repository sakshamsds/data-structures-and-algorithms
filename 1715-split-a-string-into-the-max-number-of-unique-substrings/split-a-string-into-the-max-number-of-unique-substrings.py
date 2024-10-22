class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        uniques = set()

        def backtrack(i):
            if i == len(s):
                return len(uniques)

            mx_uniques = 0
            for j in range(i + 1, len(s) + 1):
                if s[i:j] not in uniques:
                    uniques.add(s[i:j])
                    mx_uniques = max(mx_uniques, backtrack(j))
                    uniques.remove(s[i:j])

            return mx_uniques

        return backtrack(0)

        