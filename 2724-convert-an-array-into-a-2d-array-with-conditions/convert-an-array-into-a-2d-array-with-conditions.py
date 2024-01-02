class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freqDict = defaultdict(int)
        arr2D = []
        for num in nums:
            freq = freqDict[num]
            if freq == len(arr2D):
                arr2D.append([])
            arr2D[freq].append(num)
            freqDict[num] += 1
        return arr2D

        