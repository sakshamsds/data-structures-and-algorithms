# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = collections.deque([root])
        sums = []

        while q:        #O(N * logK + logN * logK)
            lvl_sum = 0
            for _ in range(len(q)):
                cur = q.popleft()
                lvl_sum += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            heapq.heappush(sums, lvl_sum)
            if len(sums) > k:
                heapq.heappop(sums)

        return -1 if len(sums) < k else sums[0]
        
