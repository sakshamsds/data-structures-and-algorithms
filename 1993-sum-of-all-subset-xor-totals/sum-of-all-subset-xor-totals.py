class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.total = 0
        subset = []

        def getXOR():
            xor = 0
            for num in subset:
                xor ^= num
            # print(subset, xor)
            return xor

        def backtrack(i):
            self.total += getXOR()

            for j in range(i, len(nums)):
                subset.append(nums[j])
                backtrack(j + 1)
                subset.pop()

        backtrack(0)
        return self.total