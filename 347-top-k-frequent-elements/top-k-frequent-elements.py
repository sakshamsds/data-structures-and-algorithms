class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # bucket sort

        freqs = collections.Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in freqs.items():
            buckets[freq].append(num)

        topk = []
        for bucket in reversed(buckets):
            topk.extend(bucket)
            if len(topk) == k:
                return topk

        return []