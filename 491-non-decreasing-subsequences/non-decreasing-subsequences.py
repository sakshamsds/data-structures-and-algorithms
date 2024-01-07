class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        subset = []

        def backtrack(i, curMax, subSeq):
            if len(subSeq) > 1:
                res.add(tuple(subSeq))

            for j in range(i, len(nums)):
                if nums[j] >= curMax:
                    subSeq.append(nums[j])
                    backtrack(j + 1, nums[j], subSeq)
                    subSeq.pop()
                
        backtrack(0, -101, [])
        return [list(subSeq) for subSeq in res]

            