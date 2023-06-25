from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = cur_sum = sum(nums[:k])
        for left in range(len(nums)-k):
            cur_sum += nums[left + k] - nums[left]
            max_sum = max(max_sum, cur_sum)

        return max_sum/k
    

print(Solution().findMaxAverage([1,12,-5,-6,50,3], 4))


# from typing import List

# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#         max_avg = 0
#         cur_sum = 0
#         for i in range(k):
#             cur_sum += nums[i]

#         max_avg = cur_sum / k

#         left = 0
#         right = k

#         while right < len(nums):
#             cur_sum += nums[right] - nums[left]
#             max_avg = max(max_avg, cur_sum/k)
#             left += 1
#             right += 1

#         return max_avg
    

# print(Solution().findMaxAverage([1,12,-5,-6,50,3], 4))