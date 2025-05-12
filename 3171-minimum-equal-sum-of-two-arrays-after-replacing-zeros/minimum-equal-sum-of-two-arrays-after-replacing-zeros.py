class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:

        def getSumAndZeros(nums):
            total, zeros = 0, 0
            for num in nums:
                if num == 0:
                    zeros += 1
                total += num
            return total, zeros

        total_1, zeros_1 = getSumAndZeros(nums1)
        total_2, zeros_2 = getSumAndZeros(nums2)

        min_possible_1 = total_1 + zeros_1
        min_possible_2 = total_2 + zeros_2

        if min_possible_1 == min_possible_2:
            return min_possible_1
        elif min_possible_1 < min_possible_2:
            if zeros_1 == 0:
                return -1
            return min_possible_2
        else:
            if zeros_2 == 0:
                return -1
            return min_possible_1