'''
5 = 5
5 ^ x = 2
5 ^ x ^ y = 0, 2 ^ x = 0
0 ^ x = 3

5 ^ x = 2
=> 5 ^ 5 ^ x = 5 ^ 2
=> x = 5 ^ 2, 5 ^ 5 = 0 and 0 ^ x = x
'''

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = [pref[0]]
        for i in range(1, len(pref)):
            res.append(pref[i] ^ pref[i - 1])
        return res
    