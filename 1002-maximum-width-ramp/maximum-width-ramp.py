class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        array = [(num, i) for i, num in enumerate(nums)]
        array.sort(key=lambda x: x[0])

        smallestIdx = array[0][1]
        maxRamp = 0
        for num, i in array:
            smallestIdx = min(smallestIdx, i)
            maxRamp = max(maxRamp, i - smallestIdx)
        
        return maxRamp