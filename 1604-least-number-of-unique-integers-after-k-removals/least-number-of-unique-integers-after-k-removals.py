'''
https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/?envType=daily-question&envId=2024-02-16

buckets
2 - 1
4 - 1
1 - 2
3 - 3

buckets/freq  ->    1       2   3   4   5   6   7
elements      ->    2,4     1   3
num_elements  ->    2       1   1

freq = 3, num_ele = 3
k = 5, how many uniques ceil(4 / 3) = 2 uniques

k  3
'''

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freqs = collections.Counter(arr)
        buckets = [0] * (len(arr) + 1)
        uniques = len(freqs)
        for num, freq in freqs.items():
            buckets[freq] += 1

        for freq, uniq in enumerate(buckets):
            num_elements = freq * uniq
            if k < num_elements:  # break condition
                return uniques - k // freq
            else:
                k -= num_elements
                uniques -= uniq

        return 0