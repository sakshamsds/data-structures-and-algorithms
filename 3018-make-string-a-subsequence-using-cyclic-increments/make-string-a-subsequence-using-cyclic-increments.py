class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        p1, p2 = 0, 0
        acceptable_diffs = [0, 1, -25]

        # greedy
        while p1 < len(str1) and p2 < len(str2):
            diff = ord(str2[p2]) - ord(str1[p1])
            if diff in acceptable_diffs:
                p2 += 1
            p1 += 1

        return p2 == len(str2)      # covered everything before this index

            