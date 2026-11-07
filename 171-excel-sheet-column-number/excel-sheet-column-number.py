class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        base = 26
        power = 0
        for c in columnTitle[::-1]:
            res += (ord(c) - ord('A') + 1) * base ** power
            power += 1
        return res