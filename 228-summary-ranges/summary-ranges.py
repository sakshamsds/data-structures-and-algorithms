class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) <= 1:
            return [str(num) for num in nums]

        res = []
        l = 0 
        for r in range(1, len(nums)):
            if nums[r] == nums[r - 1] + 1:
                continue
            if l != r - 1:
                res.append(f'{nums[l]}->{nums[r - 1]}')
            else:
                res.append(f'{nums[l]}')
            l = r

        if l != r:
            res.append(f'{nums[l]}->{nums[r]}')
        else:
            res.append(f'{nums[l]}')
        return res            