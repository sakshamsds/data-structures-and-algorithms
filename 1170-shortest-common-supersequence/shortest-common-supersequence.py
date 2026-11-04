'''
    abac
    cab

    c ab ac
    ab

        0   a   b   a   c
    0   0   0   0   0   0
    c   0   0   0   0   1
    a   0   1   1   1   1
    b   0   1   2   2   2
'''

class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        # find the longest common subsequence        
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(m):
            for c in range(n):
                increment = 1 if s1[r] == s2[c] else 0
                dp[r + 1][c + 1] = max(
                    dp[r + 1][c],
                    dp[r][c + 1],
                    dp[r][c] + increment
                )

        # find lcs        
        r, c = m, n
        lcs = []
        while r > 0 and c > 0:
            if s1[r - 1] == s2[c - 1]:
                lcs.append(s1[r - 1])
                r -= 1
                c -= 1
            elif dp[r][c - 1] >= dp[r - 1][c]:
                c -= 1
            else:
                r -= 1

        # print(''.join(lcs[::-1]))
        lcsStr = ''.join(lcs[::-1])

        scs = []
        l, r = 0, 0
        k = 0
        while l < m and r < n and k < len(lcsStr):
            if s1[l] == lcsStr[k] and s2[r] == lcsStr[k]:
                scs.append(lcsStr[k])
                l += 1
                r += 1
                k += 1
            elif s1[l] == lcsStr[k]:
                scs.append(s2[r])
                r += 1
            else:            # elif s2[r] == lcsStr[k]:
                scs.append(s1[l])
                l += 1

        scs.append(s1[l:])
        scs.append(s2[r:])
            
        return ''.join(scs)