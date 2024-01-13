'''
leetcode ->     c1 d1 e3 l1 o1    t1
coats ->    a1  c1          o1 s1 t1

night   -> g1 h1 i1 n1 t1   
thing   -> g1 h1 i1 n1 t1
'''


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_freq = [0] * 26
        t_freq = [0] * 26

        for c in s:
            s_freq[ord(c) - 97] += 1
        for c in t:
            t_freq[ord(c) - 97] += 1

        additions = 0
        for i in range(26):
            additions += abs(s_freq[i] - t_freq[i])

        return additions