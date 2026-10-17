'''
   1                        7
        2                      8
            3          5
            3   4
                            7               12     
                                        10          16
   
'''

class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key = lambda x : x[0])
        arrows = 1
        py = points[0][1]
        for x, y in points:
            if x <= py:
                py = min(y, py)
            else:
                arrows += 1
                py = y

        return arrows
            