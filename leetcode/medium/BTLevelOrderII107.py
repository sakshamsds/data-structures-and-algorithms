# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        q = deque()
        q.appendleft(root)
        res = []

        while q:
            size = len(q)
            level = []
            for _ in range(size):
                cur = q.pop()
                level.append(cur.val)
                if cur.left:
                    q.appendleft(cur.left)
                if cur.right:
                    q.appendleft(cur.right)
            if level:
                res.append(level)
        return res[::-1]