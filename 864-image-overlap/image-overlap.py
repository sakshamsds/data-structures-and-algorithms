class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        largestOverlap = 0
        n = len(img1)

        # top left r, c for the image
        for startRow in range(2 * n + 1):
            for startCol in range(2 * n + 1):
                overlap = 0

                # overlap the images
                for r in range(startRow, startRow + n):
                    for c in range(startCol, startCol + n):
                        
                        if r < n or c < n or r >= 2 * n or c >= 2 * n:
                            continue
                        
                        r1 = r - startRow
                        c1 = c - startCol

                        r2 = r - n
                        c2 = c - n

                        overlap += img1[r1][c1] * img2[r2][c2]

                largestOverlap = max(largestOverlap, overlap)

        return largestOverlap