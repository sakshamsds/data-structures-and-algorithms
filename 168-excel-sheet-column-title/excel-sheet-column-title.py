class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        # 1 -> A
        # 2 -> B
        # .
        # .
        # 26 -> Z
        # chr(ord('A') + )
        while columnNumber > 0:
            digit = columnNumber % 26
            if digit == 0:
                digit = 26
            c = chr(ord('A') + digit - 1)
            res.append(c)
            columnNumber = (columnNumber - 1) // 26

        return ''.join(res[::-1])