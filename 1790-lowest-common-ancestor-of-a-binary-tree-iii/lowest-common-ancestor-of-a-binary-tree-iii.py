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
        p_parents = set([p])
        q_parents = set([q])

        while p.parent and q.parent:
            p_parents.add(p.parent)
            q_parents.add(q.parent)
            if q.parent in p_parents:
                return q.parent
            if p.parent in q_parents:
                return p.parent
            p = p.parent
            q = q.parent

        while p.parent:
            if p.parent in q_parents:
                return p.parent
            p = p.parent

        while q.parent:
            if q.parent in p_parents:
                return q.parent
            q = q.parent

        return None