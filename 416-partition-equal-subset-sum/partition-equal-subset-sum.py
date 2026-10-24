'''
        0   1   2   3   4   5   6   7   8   9   10  11
    0   T   F   F   F   F   F   F   F   F   F   F   F
    1   T   T   F   F   F   F   F   F   F   F   F   F
    5   T                   T   T   
    11  T                   T   T                   T
    5   T                   T   T               T   T

    1   5   11  5
    1   5   11    
        6   12
'''


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total & 1 == 1:  # odd total
            return False
        target = total // 2
        prev_dp = [True] + [False] * target

        for num in nums:
            new_dp = prev_dp.copy()
            for cur_total in range(1, target + 1):
                diff = cur_total - num
                if diff >= 0:
                    if prev_dp[diff]:
                        new_dp[cur_total] = True

            if new_dp[-1]:
                return True
            # print(new_dp)
            prev_dp = new_dp

        return new_dp[-1]
            