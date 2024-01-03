class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = prev = 0
        for s in bank:
            c = s.count('1')
            if c:
                res += c * prev
                prev = c
        return res