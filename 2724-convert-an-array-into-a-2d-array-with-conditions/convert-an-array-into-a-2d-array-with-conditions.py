class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freqDict = collections.Counter(nums)
        arr2D = []
        for num, freq in freqDict.items():
            for i in range(freq):
                if i < len(arr2D):      # row already exits
                    arr2D[i].append(num)
                else:
                    arr2D.append([num])     # add new row
        return arr2D

        