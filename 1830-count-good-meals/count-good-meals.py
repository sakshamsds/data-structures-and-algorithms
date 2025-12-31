'''
using hint 1, modified two sum
max sum = 2 ** 22
'''

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        # store powers of 2
        powers = [2 ** power for power in range(22)]
        MOD = 10 ** 9 + 7
        freq_map = defaultdict(int)
        good_meals = 0
        for d in deliciousness:
            for power in powers:
                good_meals = (good_meals + freq_map[power - d]) % MOD
            freq_map[d] += 1
        return good_meals