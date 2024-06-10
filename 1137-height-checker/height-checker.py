class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        mismatch = 0
        for exp, act in zip(expected, heights):
            if exp != act:
                mismatch += 1
        return mismatch