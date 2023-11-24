class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, k - 1

        for i in range(k, len(arr)):
            distLeft = abs(x - arr[l])
            distRight = abs(x - arr[i])
            if distRight < distLeft or arr[l] == arr[i]:
                l += 1
                r += 1
            else:
                break

        return arr[l:r + 1]