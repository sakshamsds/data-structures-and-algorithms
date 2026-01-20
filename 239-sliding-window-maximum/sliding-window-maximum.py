'''
        1   3   -1  -3  5   3   6   7
i=2         3   -1                          q[0] = 3
i=3         3   -1  -3                      q[0] = 3     
i=4                     5                   q[0] = 5
i=5                     5   3               q[0] = 5
i=6                             6           q[0] = 6
i=7                                 7       q[0] = 7

add elements into deque in non increasing order
once larger elemnt is found remove other from deq
'''

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque([-10**4 - 1])
        for i in range(k - 1):
            while q and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])

        res = []
        for i in range(k - 1, len(nums)):
            # print(i, nums[i], q)
            while q and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])
            res.append(q[0])

            if nums[i - k + 1] == q[0]:
                q.popleft()

        return res
