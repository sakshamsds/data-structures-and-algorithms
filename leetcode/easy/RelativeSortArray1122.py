from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = [0] * 1001

        for num in arr1:
            freq[num] += 1

        i = 0
        for num in arr2:
            while freq[num] > 0:
                arr1[i] = num
                i += 1
                freq[num] -= 1

        for j in range(len(freq)):
            while freq[j] > 0:
                arr1[i] = j
                i += 1
                freq[j] -= 1

        return arr1