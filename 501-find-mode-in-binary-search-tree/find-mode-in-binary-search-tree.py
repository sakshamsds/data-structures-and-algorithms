# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq_map = collections.defaultdict(int)

        def dfs(node):
            if node is None:
                return
            freq_map[node.val] += 1
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        # print(freq_map)

        max_cnt = -1
        res = []
        for k, v in freq_map.items():
            if v > max_cnt:
                max_cnt = v
                res = [k]
            elif v == max_cnt:
                res.append(k)

        return res