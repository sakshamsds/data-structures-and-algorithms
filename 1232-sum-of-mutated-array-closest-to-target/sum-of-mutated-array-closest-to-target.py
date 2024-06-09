'''
3   4   9

val     sum             diff
0       0               10
3       0 + 3*3         1
4       3 + 4*2         1
9       3 + 4 + 9       8

abs(target - prefixSum + value * (n - i))
'''

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        value, prefixSum, closestDiff = 0, 0, float('inf')
        n = len(arr)
        i = 0
        for num in range(10**5 + 1):
            if num > arr[-1]:
                break
            while arr[i] < num:
                prefixSum += arr[i]
                i += 1
            arrSum = prefixSum + (n - i) * num 
            curDiff = abs(target - arrSum)
            if curDiff < closestDiff:
                value = num
                closestDiff = curDiff
        return value