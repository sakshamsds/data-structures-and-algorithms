# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        sizes = []

        def dfs(node):
            if not node:
                return -1 

            if not node.left and not node.right:    # leaf node
                heapq.heappush(sizes, 1)
                if len(sizes) > k:
                    heapq.heappop(sizes)
                return 1

            lSize, rSize = -1, -1
            lSize = dfs(node.left)
            rSize = dfs(node.right)
            if lSize != rSize or lSize == -1:
                return -1

            curSize = 2 * lSize + 1
            heapq.heappush(sizes, curSize)
            if len(sizes) > k:
                heapq.heappop(sizes)
            return curSize

        dfs(root)
        if len(sizes) < k:
            return -1

        return heapq.heappop(sizes)