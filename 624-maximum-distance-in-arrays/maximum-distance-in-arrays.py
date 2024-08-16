'''
                        -3
                -2      -2
    -1          -1      -1
    0            0      0
1   1                   1
2   2                   2
3   3       3           3
    4       4           4
    5                   5
                        6
        7               7    
        8               8
        9               9
                        10
                        11
'''

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mn, mx = arrays[0][0], arrays[0][-1]
        mx_dist = -1

        for arr in arrays[1:]:
            mx_dist = max(mx_dist, abs(arr[0] - mx), abs(arr[-1] - mn))
            mn = min(mn, arr[0])
            mx = max(mx, arr[-1])

        return mx_dist