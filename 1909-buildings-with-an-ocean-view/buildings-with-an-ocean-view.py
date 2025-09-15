class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = [len(heights) - 1]
        max_height = heights[-1]

        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > max_height:
                res.append(i)
            max_height = max(max_height, heights[i])

        return res[::-1]