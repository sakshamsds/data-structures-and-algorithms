class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        # sort the array and divide into arrays of 3 elements
        nums.sort()
        res = []
        for i in range(0, len(nums), 3):
            f, s, t = nums[i], nums[i + 1], nums[i + 2]
            if abs(f - s) > k or abs(f - t) > k or abs(s - t) > k:
                return []
            res.append([f, s, t])
        return res
