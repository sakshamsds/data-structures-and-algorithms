class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        N = len(arr)
        # remove prefix
        l, r = 0, N - 1
        while r > l and arr[r - 1] <= arr[r]:
            r -= 1

        res = r
        while l < r:
            # move r to to make the window valid
            while r < N and arr[r] < arr[l]:
                r += 1
            res = min(res, r - l - 1)
            if arr[l] > arr[l + 1]:     # left break condition
                break
            l += 1

        return res