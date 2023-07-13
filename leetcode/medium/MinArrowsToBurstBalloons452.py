from typing import List

# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/solutions/93703/share-my-explained-greedy-solution/
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        # sort by left, choose the leftmost element
        # or sort by right, choose the rightmost element
        points.sort(key=lambda x:x[1])
        n = len(points)
        shots = 1
        shot_position = points[0][1]

        for i in range(n):
            if points[i][0] <= shot_position:            # left < right
                continue        
            else:
                shot_position = points[i][1]            # right of current interval
                shots+=1            # need to take another shot from a different position
        return shots
    

print(Solution().findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
print(Solution().findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))
print(Solution().findMinArrowShots([[1,2],[4,5],[1,5]]))