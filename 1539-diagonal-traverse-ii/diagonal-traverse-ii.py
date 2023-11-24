class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagDict = collections.defaultdict(list)
        for i, row in enumerate(nums):
            for j in range(len(row)):
                diagDict[i + j].append(row[j])

        res = []
        for k, v in diagDict.items():
            res.extend(v[::-1])

        return res
