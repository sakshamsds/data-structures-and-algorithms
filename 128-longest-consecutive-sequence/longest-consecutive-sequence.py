class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniques = set(nums)
        mx = 0

        for num in nums:
            if num - 1 in uniques:      # not a good starting point
                continue
            else:
                cnt = 1
                while num + cnt in uniques:
                    cnt += 1
                mx = max(mx, cnt)
        return mx