'''
010
001
011
100

100

001

print(1 ^ 1 ^ 1 ^ 0)
print(1 ^ 1 ^ 0 ^ 0)
print(1 ^ 0 ^ 0 ^ 0)
print(1 ^ 1 ^ 1 ^ 0 ^ 0)
print(1 ^ 1 ^ 1 ^ 1 ^ 0)
print(1 ^ 2 ^ 3 ^ 4)
'''

# use hint
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums_xor = 0
        for num in nums:
            nums_xor = nums_xor^num

        diff = 0

        while nums_xor > 0 and k > 0:
            if nums_xor % 2 != k % 2:
                diff += 1
            nums_xor = nums_xor >> 1
            k = k >> 1

        # print('common', diff)

        while nums_xor > 0:
            nums_xor = nums_xor & (nums_xor - 1)
            diff += 1

        while k > 0:
            k = k & (k - 1)
            diff += 1

        return diff

