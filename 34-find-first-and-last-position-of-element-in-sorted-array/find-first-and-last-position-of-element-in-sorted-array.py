class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def search(t):
            l, r = 0, len(nums)
            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] < t:
                    l = mid + 1
                else:
                    r = mid
            return l

        i = search(target)
        j = search(target + 1) - 1

        if i <= j:
            return [i, j]
        return [-1, -1]