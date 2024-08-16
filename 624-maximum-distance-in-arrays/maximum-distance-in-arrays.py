'''
                        -3
                -2      -2
    -1          -1      -1
    0            0      0
1   1                   1
2   2                   2
3   3       3           3
    4       4           4
    5                   5
                        6
        7               7    
        8               8
        9               9
                        10
                        11
'''

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        lowest, second_lowest = 10_000, 10_000
        highest, second_highest = -10_000, -10_000
        lowest_i, highest_i = -1, -1

        for i, array in enumerate(arrays):
            if array[0] < lowest:
                lowest, second_lowest = array[0], lowest
                lowest_i = i
            elif array[0] < second_lowest:
                second_lowest = array[0]

            if array[-1] > highest:
                highest, second_highest = array[-1], highest
                highest_i = i
            elif array[-1] > second_highest:
                second_highest = array[-1]

        if lowest_i != highest_i:
            return highest - lowest
        
        return max(highest - second_lowest, second_highest - lowest)