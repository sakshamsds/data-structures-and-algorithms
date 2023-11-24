class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        # brute force
        res = []

        for i, j in zip(l, r):
            subarray = nums[i:j + 1]
            subarray.sort()
            diff = subarray[1] - subarray[0]
            arithmetic = True
            # print(subarray)
            for k in range(1, j + 1 - i):
                if subarray[k] - subarray[k - 1] != diff:
                    arithmetic = False
                    break
            res.append(arithmetic)
        return res