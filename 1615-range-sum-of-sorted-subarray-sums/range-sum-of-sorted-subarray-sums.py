class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        pq = []
        for i, num in enumerate(nums):  # maintain sum at current index
            pq.append((num, i))
        heapq.heapify(pq)

        k, res = 1, 0   # 1-indexed
        while pq:
            cur_sum, i = heapq.heappop(pq)
            if k >= left:
                res = (res + cur_sum) % 1_000_000_007
            if k == right:
                break
            if i + 1 < len(nums):
                new_sum = cur_sum + nums[i + 1]
                heapq.heappush(pq, (cur_sum + nums[i + 1], i + 1))
            k += 1

        return res