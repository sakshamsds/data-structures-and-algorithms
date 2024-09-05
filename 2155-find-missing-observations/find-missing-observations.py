'''
3   2   4   3   _   _         
                6   6

sum(m) + sum(n) = mean * (m + n)
sum(n) = mean * (m + n) - sum(m)
        = 4 * (6) - 12
        = 12

sum = 21 - 12 = 9
_ _ _ _
6 * n < sum
n > sum

9 // 4 = 2

3 _ _ _
'''

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        target_sum = mean * (n + m) - sum(rolls)

        if target_sum < n or target_sum > 6 * n:
            return []

        missing = []
        for num_missing in range(n, 0, -1):
            if target_sum % num_missing == 0:
                missing.extend([target_sum // num_missing] * num_missing)
                break
            missing.append(math.ceil(target_sum / num_missing))
            target_sum -= missing[-1]
        return missing
