class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        non_neg = [num for num in nums if num >= 0]

        if not non_neg:
            return nums

        # print(non_neg)
        k = k % len(non_neg)
        # print(k)

        for i, num in enumerate(nums):
            if num >= 0:
                nums[i] = non_neg[k]
                k += 1
                if k == len(non_neg):
                    k = 0

        return nums