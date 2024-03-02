class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # find the smallest positive element idx
        for i, num in enumerate(nums):
            if num > 0:
                break

        sqrs = []
        l, r = i - 1, i
        while l >= 0 and r < len(nums):
            if -nums[l] < nums[r]:
                sqrs.append(nums[l] ** 2)
                l -= 1
            else:
                sqrs.append(nums[r] ** 2)
                r += 1

        while l >= 0:
            sqrs.append(nums[l] ** 2)
            l -= 1

        while r < len(nums):
            sqrs.append(nums[r] ** 2)
            r += 1
        
        return sqrs