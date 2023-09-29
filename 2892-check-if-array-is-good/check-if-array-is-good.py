"""
base1 = [1, 1]
base3 = [1, 2, 3, 3]

"""

class Solution:
    def isGood(self, nums: List[int]) -> bool:

        # find max element
        max_num = -1
        for num in nums:
            max_num = max(max_num, num)

        # sanity check
        if len(nums) != max_num + 1:
            return False

        # create freq map
        freq_map = dict()
        for i in range(1, max_num + 1):
            freq_map[i] = 1
        freq_map[max_num] += 1

        for num in nums:
            if freq_map.get(num, 0) == 0:
                return False
            freq_map[num] -= 1
        
        return True


        