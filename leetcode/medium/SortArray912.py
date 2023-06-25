from pyparsing import List

"""
MergeSort(arr, left, right):
    if left > right 
        return
    mid = (left+right)/2
    mergeSort(arr, left, mid)
    mergeSort(arr, mid+1, right)
    merge(arr, left, mid, right)
end

Inner functions, also known as nested functions, are functions that you define inside other functions. 
In Python, this kind of function has direct access to variables and names defined in the enclosing function. 
Inner functions have many uses, most notably as closure factories and decorator functions.
"""

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge_sort(arr, l, r):
            if l == r:             
                return arr
            
            m = (l+r) // 2
            merge_sort(arr, l, m)
            merge_sort(arr, m+1, r)
            merge(arr, l, m, r)
            return arr

        def merge(arr, l, m, r):
            left, right = arr[l:m+1], arr[m+1:r+1]
            i, j, k = l, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j+=1
                else:
                    arr[i] = right[k]
                    k+=1
                i+=1

            # arr[i:] = left[j:] if j < len(left) else right[k:]

            while j < len(left):
                    arr[i] = left[j]
                    j+=1
                    i+=1

            while k < len(right):
                    arr[i] = right[k]
                    k+=1
                    i+=1

        return merge_sort(nums, 0, len(nums)-1)


"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        if len(nums) <= 1:
            return nums

        middle = len(nums)//2
        left = self.sortArray(nums[:middle])
        right = self.sortArray(nums[middle:])
        return self.merge(left, right)

    def merge(self, left, right):
        new_list = []

        left_idx = 0
        right_idx = 0

        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] <= right[right_idx]:
                new_list.append(left[left_idx])
                left_idx+=1
            else:
                new_list.append(right[right_idx])
                right_idx+=1

        if left_idx == len(left):
            while right_idx < len(right):
                new_list.append(right[right_idx])
                right_idx+=1
        
        if right_idx == len(right):
            while left_idx < len(left):
                new_list.append(left[left_idx])
                left_idx+=1

        return new_list
"""
    
if __name__ == "__main__":
    obj = Solution()
    print(obj.sortArray([-2, 3, -5]))
    print(obj.sortArray([5, 2, 3, 1]))