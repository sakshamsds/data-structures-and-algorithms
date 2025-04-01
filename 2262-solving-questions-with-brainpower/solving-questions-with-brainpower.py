'''
    0   1   2   3   
    5   4   4   2
'''

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        num_questions = len(questions)
        dp = [0] * num_questions
        dp[-1] = questions[-1][0]

        for i in range(num_questions - 2, -1, -1):
            if i + 1 + questions[i][1] >= num_questions:
                dp[i] = max(dp[i + 1], questions[i][0])
            else:
                dp[i] = max(dp[i + 1], questions[i][0] + dp[i + 1 + questions[i][1]])

        return dp[0]