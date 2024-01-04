'''
time, freq
-1 -> 1
1 -> 2, 3
2 -> 4, 5, 6
3 -> 7, 8, 9
'''

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        difficulty_freq = collections.Counter(tasks)
        rounds = 0
        for _, freq in difficulty_freq.items():
            if freq == 1:       # can't finish the task
                return -1
            rounds += ceil(freq / 3)
        return rounds