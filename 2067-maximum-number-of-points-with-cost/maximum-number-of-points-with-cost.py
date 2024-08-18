class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # find max at each cell
        rows, cols = len(points), len(points[0])

        for r in range(1, rows):

            scores_l, scores_r = [0] * cols, [0] * cols
            scores_l[0], scores_r[-1] = points[r - 1][0], points[r - 1][-1]

            # calculate contributions 
            for c in range(1, cols):
                scores_l[c] = max(points[r - 1][c], scores_l[c - 1] - 1)
            
            for c in range(cols - 2, -1, -1):
                scores_r[c] = max(points[r - 1][c], scores_r[c + 1] - 1)

            for c in range(cols):
                points[r][c] += max(scores_l[c], scores_r[c])

        # print(points)

        return max(points[-1])