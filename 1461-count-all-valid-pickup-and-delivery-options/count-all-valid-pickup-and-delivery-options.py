class Solution:
    def countOrders(self, n: int) -> int:
        # how many slots we have, 2 * n
        # for each order, select two slots
            # 2n * (2n - 1), choose 1 slot for p, then from 2n-1 choose 1 for d
            # half of them would have reverse order so // 2

        # _ _ _ _ _ _
        # P1, D1 in 6 * 5 ways and then // 2 for our constraint

        slots = 2 * n
        res = 1
        for _ in range(1, n):
            ways = slots * (slots - 1) // 2     # uniques for this order
            res = (res * ways) % (1e9 + 7)
            slots -= 2

        return int(res)