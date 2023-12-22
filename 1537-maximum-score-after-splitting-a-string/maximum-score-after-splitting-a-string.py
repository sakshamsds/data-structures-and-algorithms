class Solution:
    def maxScore(self, s: str) -> int:
        left_score = 1 if s[0] == '0' else 0
        right_score = 1 if s[-1] == '1' else 0         
        for i in range(1, len(s) - 1):
            if s[i] == '1':
                right_score += 1
        res = left_score + right_score

        for i in range(1, len(s) - 1):
            if s[i] == '1':
                right_score -= 1
            else:
                left_score += 1
            res = max(res, left_score + right_score)
        return res