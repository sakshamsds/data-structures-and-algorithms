class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        count_odd_sums, count_even_sums = 0, 0      # starting from zero idx
        total_sums = 0      # not starting from zero idx
        MOD = 10 ** 9 + 7
        prefix_sum = 0
        for num in arr:
            prefix_sum += num
            if prefix_sum & 1 == 1:
                count_odd_sums += 1
                total_sums += count_even_sums
            else:
                count_even_sums += 1
                total_sums += count_odd_sums
            total_sums %= MOD

        return (count_odd_sums + total_sums) % MOD

