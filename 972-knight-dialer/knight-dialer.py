class Solution:
    def knightDialer(self, n: int) -> int:
        adj_list = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [4, 2]
        }

        prev_dp = [1] * 10
        MOD = 1e9 + 7
        # print(1, prev_dp)


        for i in range(2, n + 1):
            next_dp = [0] * 10
            for num in range(10):
                for nbr in adj_list[num]:
                    next_dp[num] = int((next_dp[num] + prev_dp[nbr]) % MOD)
            prev_dp = next_dp
            # print(i, prev_dp)

        return int(sum(prev_dp) % MOD)


