'''
1 2 3 4 5 6 7
2 3 4 5 6 7 8
3 4 5 6
'''

class Solution:
    def totalMoney(self, n: int) -> int:
        num_weeks, extra_days = n // 7, n % 7 
        week_sum = 21 * num_weeks + num_weeks * (7 + 7 * num_weeks) // 2
        start_amt = num_weeks + 1
        for i in range(extra_days):
            week_sum += start_amt + i
        return week_sum


        

