from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        threshold *= k
        cur_sum = sum(arr[:k-1])            # sum of first k-1 elements
        for right in range(k-1, len(arr)):
            cur_sum += arr[right]
            if cur_sum >= threshold:
                count+=1
            cur_sum -= arr[right-k+1]
        return count
    
    # def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
    #     threshold *= k
    #     cur_sum = sum(arr[:k])
    #     count = 1 if cur_sum >= threshold else 0
    #     for i in range(1, len(arr) - k + 1):
    #         cur_sum += arr[i+k-1] - arr[i-1]
    #         print(i, cur_sum)
    #         if cur_sum >= threshold:
    #             count+=1
    #     return count
    
# print(Solution().numOfSubarrays([1,1,1,1,1], 1, 0))