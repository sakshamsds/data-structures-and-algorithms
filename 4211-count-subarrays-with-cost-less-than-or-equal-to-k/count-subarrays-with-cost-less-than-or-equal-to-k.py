class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = 0       # as we shorten the window, the cost will come down
        q_max = collections.deque()
        q_min = collections.deque()
        res = 0

        for r in range(len(nums)):
            while q_max and q_max[-1] < nums[r]:
                q_max.pop()
            q_max.append(nums[r])

            while q_min and q_min[-1] > nums[r]:
                q_min.pop()
            q_min.append(nums[r])

            while l < r and (q_max[0] - q_min[0]) * (r - l + 1) > k:
                if nums[l] == q_max[0]:
                    q_max.popleft()
                if nums[l] == q_min[0]:
                    q_min.popleft()
                l += 1

            res += r - l + 1

        return res