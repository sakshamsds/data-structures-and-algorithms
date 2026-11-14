'''
    Case 1, if num exists
    1   2   3   3   4   5
            i

    Case 2, if num does not exists
    num < lowest
    num > highest

    1   2   4   5
    logN * k
'''


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # if this is not sorted, we make a heap
        n = len(arr)
        i = bisect.bisect_left(arr, x)
        # print(i, arr[i])
        # print(bisect.bisect_left([1, 2, 4, 5], 3))
        # print(bisect.bisect_left([1, 2, 4, 5], 6))
        # print(bisect.bisect_left([1, 2, 4, 5], -1))
        # print(bisect.bisect_left([1, 2, 3, 3, 4, 5], 3))
    
        if i == len(arr):
            return arr[-k:]
        if i == 0:
            return arr[:k]

        def getClosest(start):
            l, r = start - 1, start + 1
            while r - l - 1 < k:
                if l == -1:
                    r += 1
                elif r == n:
                    l -= 1
                else:
                    if abs(arr[r] - x) < abs(arr[l] - x):
                        r += 1
                    else:
                        l -= 1
            return arr[l + 1:r]

        if arr[i] != x and abs(arr[i] - x) >= abs(arr[i - 1] - x):
            i -= 1
        return getClosest(i)

    