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
                if cur_length not in num_bricks:
                    num_bricks[cur_length] = height
                num_bricks[cur_length] -= 1

        return min(num_bricks.values())

