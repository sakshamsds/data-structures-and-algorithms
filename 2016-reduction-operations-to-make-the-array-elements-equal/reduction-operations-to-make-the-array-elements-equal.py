'''
5 3 1
3 1
1

3 2 2 1 1
2 1 1
1
'''

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:  
        nums_set = set()
        # distinct = []
        res = 0
        nums.sort()
        for num in nums:
            nums_set.discard(num)
            # distinct.append(len(nums_set))
            res += len(nums_set)
            nums_set.add(num)

        print(nums)
        # print(distinct)

        return res
        
