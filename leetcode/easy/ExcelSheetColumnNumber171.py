# https://leetcode.com/problems/excel-sheet-column-number/
# 171. Excel Sheet Column Number


# print(ord("A")) = 65


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        for idx, alphabet in enumerate(reversed(columnTitle)):
            # print("idx: ", idx, alphabet)
            num += pow(26, idx) * (ord(alphabet) - 64)
            # print(num)
        return num


print(Solution().titleToNumber("A"))
print(Solution().titleToNumber("AB"))
print(Solution().titleToNumber("ZY"))
