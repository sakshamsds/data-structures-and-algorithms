class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        window = deque()

        for i in range(k - 1):
            while window and window[-1] < nums[i]:
                window.pop()
            window.append(nums[i])

        l = 0
        res = []
        for r in range(k - 1, len(nums)):
            while window and window[-1] < nums[r]:
                window.pop()
            window.append(nums[r])
            res.append(window[0])

            if window[0] == nums[l]:
                window.popleft()
            l += 1

        return res