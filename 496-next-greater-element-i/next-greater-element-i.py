class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nextGreater = {}
        #   1   3   4   2   3
        #           2   3   3
        stack = []
        for i in range(len(nums2) - 1, -1, -1):
            num = nums2[i]
            while stack and stack[-1] < num:
                stack.pop()
            nextGreater[num] = -1 if not stack else stack[-1]
            stack.append(num)

        res = []
        for num in nums1:
            res.append(nextGreater[num])
        return res