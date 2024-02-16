class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in freqs.items():
            buckets[freq].append(num) 

        res = []
        for bucket in buckets[::-1]:
            res.extend(bucket)
            if len(res) == k:
                break
        return res
            

