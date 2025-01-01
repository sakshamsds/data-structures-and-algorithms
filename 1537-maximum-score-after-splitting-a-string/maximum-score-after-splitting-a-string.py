class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count('1')
        left_zeros, right_ones = 0, ones

        max_score = 0
        for i in range(0, len(s) - 1):
            c = s[i]
            if c == '0':
                left_zeros += 1
            else:
                right_ones -= 1

            max_score = max(max_score, left_zeros + right_ones)
        return max_score