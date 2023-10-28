'''
find max number and idx
numbers left to it should be in decreasing order
numbers right to it should in decreasing order
'''

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        max_num_idx = len(arr) // 2
        for i in range(1, len(arr) - 1):
            if arr[i] > arr[max_num_idx]:
                max_num_idx = i

        max_num = arr[max_num_idx]
        # print(max_num_idx, max_num)

        # number left to idx should be smaller 
        l = max_num_idx - 1
        prev = max_num
        while l >= 0:
            if arr[l] >= prev:
                return False
            prev = arr[l]
            l -= 1

        # numbers on right should be smaller
        r = max_num_idx + 1
        prev = max_num
        while r < len(arr):
            if arr[r] >= prev:
                return False
            prev = arr[r]
            r += 1

        return True

        