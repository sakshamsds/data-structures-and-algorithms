'''
    0   1   2   3   4   5
0   0   1   2   3   4   5
1   1   2   3   4   5   6
2   2   3   4   5   6   7
3   3   4   5   6   7   8
4   4   5   6   7   8   9
5   5   6   7   8   9   10
'''

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagDict = collections.defaultdict(list)
        for r in range(len(nums) - 1, -1, -1):
            for c in range(len(nums[r])):
                diagDict[r + c].append(nums[r][c])

        print(diagDict.keys())
        res = []
        key = 0
        while key in diagDict:
            res.extend(diagDict[key])
            key += 1

        return res
