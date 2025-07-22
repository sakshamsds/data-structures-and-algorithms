class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l, cur_score, max_score = 0, 0, 0
        uniques = set()

        for num in nums:
            if num not in uniques:
                uniques.add(num)
                cur_score += num
                max_score = max(max_score, cur_score)
            else:
                while nums[l] != num:
                    uniques.remove(nums[l])
                    cur_score -= nums[l]
                    l += 1
                l += 1

        return max_score
