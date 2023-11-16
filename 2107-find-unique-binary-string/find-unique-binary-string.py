# Cantor's diagonal argument

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # make the res differ from every num in nums by 1 place
        res = []
        for i in range(len(nums)):
            cur = nums[i][i]
            res.append("1" if cur == "0" else "0")
        return "".join(res)
        