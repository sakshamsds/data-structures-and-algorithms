'''
    2   2   1   1   1   2   2
num     2   
freq    1
'''

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        curMaj, freq = 0, 0

        for num in nums:
            if freq == 0:
                curMaj, freq = num, 1
            else:
                if curMaj == num:
                    freq += 1
                else:
                    freq -= 1
        
        return curMaj