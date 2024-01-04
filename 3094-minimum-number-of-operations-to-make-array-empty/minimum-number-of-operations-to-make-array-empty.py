class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freqDict = collections.Counter(nums)
        total_ops = 0
        # print(freqDict)
        for _, freq in freqDict.items():
            ops = self.getOps(freq)
            if ops == -1:
                return -1
            else:
                total_ops += ops
        return total_ops

    # 10
    # 2, 2, 2, 2, 2
    # 3, 3, 2, 2

    def getOps(self, freq):
        ops = 0
        while freq > 0:
            if freq == 1:
                return -1
            if freq % 3 == 0:
                ops += freq // 3
                return ops
            freq -= 2           # keep subtracting by 2, reach either 0 or 1
            ops += 1
        return ops

    # 2 2 2 2 2 2 2 2 2 2 | 2 2