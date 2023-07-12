from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:

        # two pointers solutions, O(1)
        # https://www.youtube.com/watch?v=ZI2z5pq0TqA
        n = len(height)

        left_ptr, right_ptr = 0, n-1
        left_max, right_max = height[0], height[n-1]

        water_trapped = 0 

        while left_ptr <= right_ptr:
            if left_max < right_max:            # imp condition
                left_max = max(left_max, height[left_ptr])
                water_trapped += left_max - height[left_ptr]
                left_ptr += 1
            else:
                right_max = max(right_max, height[right_ptr])
                water_trapped += right_max - height[right_ptr]
                right_ptr -= 1

        return water_trapped

        # # max(0, min(left[i], right[i]) - a[i]))
        # # find water at every index
        # # https://www.youtube.com/watch?v=m18Hntz4go8

        # n = len(height)

        # # use prefix max and suffix max
        # left_max_at_i = 0
        # right_max_at_i = 0
        # left_list, right_list = [], []
        # for i in range(n):
        #     left_max_at_i = max(left_max_at_i, height[i])
        #     right_max_at_i = max(right_max_at_i, height[n - i - 1])
        #     left_list.append(left_max_at_i)
        #     right_list.append(right_max_at_i)
        #     # right_list.insert(0, right_max_at_i)

        # water_trapped = 0 
        # for i in range(n):
        #     water_trapped += max(0, min(left_list[i], right_list[n-i-1]) - height[i])
        #     # water_trapped += max(0, min(left_list[i], right_list[i]) - height[i])

        # return water_trapped
        
print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))