class Solution:
    def checkValidString(self, s: str) -> bool:
        left_max, left_min = 0, 0

        for c in s:
            if c == '(':
                left_max, left_min = left_max + 1, left_min + 1
            elif c == ')':
                left_max, left_min = left_max - 1, left_min - 1
            else:
                left_max, left_min = left_max + 1, left_min - 1
            if left_max < 0:
                return False
            left_min = max(0, left_min)

        return left_min == 0