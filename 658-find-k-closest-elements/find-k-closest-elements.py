class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # find start of the binary search
        l, r = 0, len(arr) - k
        while l < r:
            mid = l + (r - l) // 2

            # if abs(arr[mid] - x) > abs(arr[mid + k] - x):
            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid

        return arr[l:l + k]