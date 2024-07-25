class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, l, r):
        if l == r:
            return [nums[l]]
        mid = l + (r - l) // 2
        arr_l = self.mergeSort(nums, l, mid)
        arr_r = self.mergeSort(nums, mid + 1, r)
        return self.merge(arr_l, arr_r)

    def merge(self, arr_l, arr_r):
        res = []
        i, j = 0, 0
        while i < len(arr_l) and j < len(arr_r):
            if arr_l[i] <= arr_r[j]:
                res.append(arr_l[i])
                i += 1
            else:
                res.append(arr_r[j])      
                j += 1
            
        res.extend(arr_l[i:])
        res.extend(arr_r[j:])
        return res
