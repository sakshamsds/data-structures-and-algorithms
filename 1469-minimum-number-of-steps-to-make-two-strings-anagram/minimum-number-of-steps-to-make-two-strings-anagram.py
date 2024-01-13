'''
bab - a1 b2
aba - a2 b1

leetcode -    c1 d1 e3    l1 o1       t1
practice - a1 c2    e1 i1       p1 r1 t1 

(total chars - common char) / 2
1 + 1 + 1 + 2 + 1 + 1 + 1 + 1
5
'''

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return (Counter(s) - Counter(t)).total()
        # return sum((Counter(s) - Counter(t)).values())
        # s_freq = [0] * 26
        # t_freq = [0] * 26

        # for c1, c2 in zip(s, t):
        #     s_freq[ord(c1) - ord('a')] += 1
        #     t_freq[ord(c2) - ord('a')] += 1

        # diff = 0
        # for i in range(26):
        #     diff += abs(t_freq[i] - s_freq[i])

        # return diff // 2