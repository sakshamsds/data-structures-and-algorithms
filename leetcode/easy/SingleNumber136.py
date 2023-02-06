# https://leetcode.com/problems/single-number/
# 136. Single Number

# https://www.w3schools.com/python/ref_dictionary_get.asp

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # # solution 1
        # freq_dic = {}
        # for num in nums:
        #     freq_dic[num] = freq_dic.get(num, 0) + 1

        # for key, val in freq_dic.items():
        #     if val == 1:
        #         return key
        # return 0

        # solution 2
        # return sum(set(nums)) * 2 - sum(nums)

        # (1) that its a commutative operation (i.e. a xor b = b xor a).
        # (2) that something xor itself is 0. So a xor a = 0. And 
        # (3) 0 xor a = a.
        # XOR satisfy commutative law and associative law

        # solution 3
        output = 0

        for num in nums:
            output ^= num

        return output

# print(0^1)
# print(3^4)
# print(4^3)
# print(4^4)

# print(4^1)
# print(5^2)
# print(7^1)
# print(4^1^2^1^2)

