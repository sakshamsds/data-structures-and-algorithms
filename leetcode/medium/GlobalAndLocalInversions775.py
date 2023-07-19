
from typing import List

"""
https://www.geeksforgeeks.org/inversion-count-in-array-using-merge-sort/#

Traverse through the array, and for every index, find the number of smaller elements on its right side of the array. 
This can be done using a nested loop. Sum up the counts for all indices in the array and print the sum.

Use Merge sort with modification that every time an unsorted pair is found increment count by one and return count at the end.
"""

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True

        local_inv = 0
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                local_inv += 1

        global_inv = self.merge_sort(nums, 0, n-1)
        print(local_inv, global_inv)
        return local_inv == global_inv

    def merge_sort(self, nums, l, r):
        if l == r:
            return 0
        mid = (l + r) // 2
        left_count = self.merge_sort(nums, l, mid)
        right_count = self.merge_sort(nums, mid + 1, r)
        merge_count = self.merge(nums, l, mid, r)           # left and right are sorted
        return left_count + right_count + merge_count
    
    def merge(self, nums, l, m, r):
        left, right = nums[l:m+1], nums[m+1:r+1]
        i, j, k = l, 0, 0
        count = 0

        while j < len(left) and k < len(right):
            if left[j] <= right[k]:
                nums[i] = left[j]
                j += 1
            else:
                nums[i] = right[k]
                k += 1
                count += len(left[j:])
            i += 1

        while j < len(left):
            nums[i] = left[j]
            j += 1
            i += 1
        
        while k < len(right):
            nums[i] = right[k]
            k += 1
            i += 1

        return count

# print(Solution().isIdealPermutation([2, 3, 9, 2, 9]))
# print(Solution().isIdealPermutation([1,0,2]))
# print(Solution().isIdealPermutation([1,2,0]))
# print(Solution().isIdealPermutation([0,1,3,2]))

        