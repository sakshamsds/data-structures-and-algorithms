class Solution:
    def partitionString(self, s: str) -> int:
        count, uniques = 0, set()
        for char in s:
            if char in uniques:
                count, uniques = count + 1, set(char)
            else:
                uniques.add(char)
        return count + 1
        