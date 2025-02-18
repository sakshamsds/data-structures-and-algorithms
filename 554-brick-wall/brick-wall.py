'''
        4   5   3   2   4
    0   1   2   3   4   5   6
        1       3       5   6
                3   4       6
        1           4       6
            2               6
                3   4       6
        1           4   5   6
'''

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        height = len(wall)
        brick_total = sum(wall[0])
        num_bricks = {0: height}

        for row in wall:
            cur_length = 0
            for brick_size in row[:-1]:
                cur_length += brick_size
                num_bricks[cur_length] = num_bricks.get(cur_length, height) - 1

        return min(num_bricks.values())

