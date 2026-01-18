'''
    0   3   5   8   10      12
    1   3   1   4   2
'''


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        num_pos = len(position)
        speed_map = {position[i]:speed[i] for i in range(num_pos)}  # all pos are unique
        position.sort(key=lambda x:x)

        fleets = 0
        prev_time = -1
        for pos in position[::-1]:
            cur_time = (target - pos) / speed_map[pos]
            if cur_time > prev_time:
                fleets += 1
                prev_time = cur_time

        return fleets
                
