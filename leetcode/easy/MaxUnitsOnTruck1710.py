from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        # sort using number of units per box
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        idx = 0
        total_units = 0
        while truckSize>0:          # start filling
            if idx == len(boxTypes):
                break
            num_boxes = min(truckSize, boxTypes[idx][0])
            total_units += num_boxes * boxTypes[idx][1]
            truckSize -= num_boxes
            idx += 1

        return total_units

print(Solution().maximumUnits([[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]], 35))