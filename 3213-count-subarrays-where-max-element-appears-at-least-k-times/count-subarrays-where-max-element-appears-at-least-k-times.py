class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n, mx = len(nums), max(nums)
        l, cnt, res = 0, 0, 0
        # n ** 2 - bad subarray
        # bad subarray => freq < k
        for r in range(len(nums)): 
            if nums[r] == mx:
                cnt += 1

            while cnt >= k and l <= r:
                if nums[l] == mx:
                    cnt -= 1
                l += 1
            
            res += r - l + 1
        return n * (n + 1) // 2 - res
            

                