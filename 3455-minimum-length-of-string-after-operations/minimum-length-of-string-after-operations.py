'''
b, bbb, bbbbb, 1
bb, bbbb, bbbbbb, 2
'''

class Solution:
    def minimumLength(self, s: str) -> int:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1

        min_length = 0
        for cnt in count:
            if cnt > 0:
                min_length += 2 if cnt % 2 == 0 else 1

        return min_length