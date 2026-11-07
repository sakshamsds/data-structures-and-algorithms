class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        l = 0
        for num in nums:
            if num != val:
                nums[l] = num
                l += 1
        return l