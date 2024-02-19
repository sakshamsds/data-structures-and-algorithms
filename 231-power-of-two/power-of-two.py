class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        MAX = 2 ** 31 - 1
        store = set()
        for power in range(0, 30 + 1):
            store.add(2 ** power)
        return n in store

        