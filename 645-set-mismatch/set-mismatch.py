class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        res = [-1, -1]
        for i in range(1, len(nums) + 1):
            if c[i] == 0:
                res[1] = i
            if c[i] == 2:
                res[0] = i
        return res