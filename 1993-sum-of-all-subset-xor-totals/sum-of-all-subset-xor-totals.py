class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.total = 0

        def backtrack(i, cur_xor):
            if i == len(nums):
                self.total += cur_xor
                return

            backtrack(i + 1, cur_xor)
            backtrack(i + 1, cur_xor ^ nums[i])

        backtrack(0, 0)
        return self.total
            