from typing import List
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        
        def find_max_digit(n):
            max_digit = 0
            while n > 0:
                max_digit = max(max_digit, n % 10)
                n //= 10
            return max_digit
                
        store = [[] for _ in range(10)]
        
        for num in nums:
            max_digit = find_max_digit(num)
            # compare at i digit index at store
            if len(store[max_digit]) < 2:
                store[max_digit].append(num)
            else:
                # find the smaller number and replace with that
                if store[max_digit][0] <= store[max_digit][1]:
                    if store[max_digit][0] < num:
                        store[max_digit][0] = num
                else:
                    if store[max_digit][1] < num:
                        store[max_digit][1] = num

                
        max_sum = -1
        for pair in store:
            if len(pair) == 2:
                max_sum = max(max_sum, pair[0] + pair[1])
            
        print(store)
        return max_sum
                    
                
        
                    
                
print(Solution().maxSum([1,2,3,4]))
print(Solution().maxSum([51,71,17,24,42]))
print(Solution().maxSum([68,8,100,84,80,14,88]))
        