class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freqs = [0] * 1001

        for num in arr1:
            freqs[num] += 1

        res = []
        for num in arr2:
            res.extend([num] * freqs[num])
            freqs[num] = 0

        for num in range(1001):
            res.extend([num] * freqs[num])

        return res