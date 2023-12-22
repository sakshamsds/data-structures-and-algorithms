'''
score = zeros_in_left + ones_in_right
score = zeros_in_left + ones_in_total(const) - ones_in_left
'''

class Solution:
    def maxScore(self, s: str) -> int:
        ones, zeros = 0, 0
        best = -500

        for i in range(len(s) - 1):
            if s[i] == '1':
                ones += 1
            else:
                zeros += 1
            best = max(best, zeros - ones)
        if s[-1] == '1':
            ones += 1
        return best + ones