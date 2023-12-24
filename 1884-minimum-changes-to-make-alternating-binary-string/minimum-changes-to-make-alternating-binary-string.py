class Solution:
    def minOperations(self, s: str) -> int:
        # start with 0, odd == 0, even == 1
        # start with 1, odd == 1, even == 0
        ops_w_zero_start, ops_w_one_start = 0, 0
        for i in range(len(s)):
            if i % 2 == 0:  # even idx
                if s[i] == '0':
                    ops_w_zero_start += 1
                else:
                    ops_w_one_start += 1
            else:       # odd idx
                if s[i] == '0':
                    ops_w_one_start += 1
                else:
                    ops_w_zero_start += 1
        return min(ops_w_zero_start, ops_w_one_start)