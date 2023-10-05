class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        mjr_ele = -1
        cnt = 0

        for num in nums:
            if cnt == 0:
                mjr_ele = num
                cnt += 1
            else:
                if num == mjr_ele:
                    cnt += 1
                else:
                    cnt -= 1
        
        return mjr_ele