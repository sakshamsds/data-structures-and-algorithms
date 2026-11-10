"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        l, r = p, q

        while l != r:
            l = l.parent
            r = r.parent
            if not l:
                l = q
            if not r:
                r = p

        return l