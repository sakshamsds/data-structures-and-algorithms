from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # print(nums)
        low, high = 0, len(nums) - 1
        found = False

        while low <= high:
            mid = (low + high)//2
            if nums[mid] == 0:
                found = True
                break
            elif nums[mid] > 0:
                high = mid - 1
            else:
                low = mid + 1
            
        # print("mid", mid)
        if nums[mid] > 0:
            mid -= 1
        if not found:
            return max(len(nums) - mid - 1, mid + 1)

        # get the first and last index of 0
        neg_idx, pos_idx = mid, mid

        for i in range(neg_idx, -1, -1):
            if nums[i] != 0:
                neg_idx = i
                break
        neg_size = 0 if nums[neg_idx] >= 0 else neg_idx + 1

        for i in range(pos_idx, len(nums), 1):
            if nums[i] != 0:
                pos_idx = i
                break 
        pos_size = 0 if nums[pos_idx] <= 0 else len(nums) - pos_idx
        # print(neg_size, pos_size)
        return max(neg_size, pos_size)
    
print(Solution().maximumCount([-1563,-236,-114,-55,427,447,687,752,1021,1636]))
print(Solution().maximumCount([-2,-1,-1,1,2,3]))
print(Solution().maximumCount([5,20,66,1314]))

# print(Solution().maximumCount([-3,-2,-1,0,0,1,2]))
# print(Solution().maximumCount([-3,-1,0, 0, 0,1]))
# print(Solution().maximumCount([0]))
# print(Solution().maximumCount([-1]))
# print(Solution().maximumCount([0, 0]))
