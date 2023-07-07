# Definition for a Node.
from typing import List
from collections import deque

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        tree_res = []
        q = deque()
        q.appendleft(root)
        while q:
            level_size = len(q)
            level_res = []
            for _ in range(level_size):
                cur = q.pop()
                level_res.append(cur.val)
                for child in cur.children:
                    q.appendleft(child)
            tree_res.append(level_res)
        return tree_res
    
