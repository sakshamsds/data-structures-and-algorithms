'''
aababbab

00011233    b's on the left
32211100    a's on the right
'''

class Solution:
    def minimumDeletions(self, s: str) -> int:
        right_a = s.count('a')
        left_b = 0
        min_deletions = right_a + left_b

        for c in s:
            if c == 'a':
                right_a -= 1
            min_deletions = min(min_deletions, right_a + left_b)
            if c == 'b':
                left_b += 1
        return min_deletions