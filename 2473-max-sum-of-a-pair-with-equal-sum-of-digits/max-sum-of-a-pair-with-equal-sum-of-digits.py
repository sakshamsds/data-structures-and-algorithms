'''
    18  43  36  13  7
    9   7   9   4   7
'''

class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        digits_sum_map = dict()     # digit_sum -> two largest numbers

        for num in nums:
            digit_sum = sum(map(int, str(num)))

            if digit_sum not in digits_sum_map:
                digits_sum_map[digit_sum] = (num, None)
            else:
                max1, max2 = digits_sum_map[digit_sum]
                if num > max1:
                    digits_sum_map[digit_sum] = (num, max1)
                elif (not max2) or (max2 and max2 < num):
                    digits_sum_map[digit_sum] = (max1, num)

        max_sum = -1
        for m1, m2 in digits_sum_map.values():
            if m1 and m2:
                max_sum = max(max_sum, m1 + m2)
        return max_sum


                    

            
