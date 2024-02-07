'''
 0 1 2 3 4 5 6 7
[1,0,0,0,0,7,7,5]

[10,0,0,0,0,7,0,11]
'''
import numpy as np

class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        scores = [0] * len(edges)
        for start, end in enumerate(edges):
            scores[end] += start
        return np.argmax(scores)
        