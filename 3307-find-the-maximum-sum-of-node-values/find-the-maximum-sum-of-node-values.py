class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        min_pos = float(inf)
        max_neg = -float(inf)
        max_sum = sum(nums)
        num_pos_changes = 0

        for num in nums:
            change = (num ^ k) - num
            if change > 0:
                num_pos_changes += 1
                min_pos = min(min_pos, change)
                max_sum += change
            else:
                max_neg = max(max_neg, change)

        # print(min_pos, max_neg, max_sum, num_pos_changes)

        if num_pos_changes & 1 == 0:
            return max_sum

        return max_sum + max_neg if min_pos + max_neg > 0 else max_sum - min_pos