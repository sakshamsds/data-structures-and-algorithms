# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]
        cur_dir = 'R'
        r_low, r_high, c_low, c_high = 0, m - 1, 0, n - 1

        r, c = 0, 0
        while head:
            if cur_dir == 'R':      
                while c <= c_high and head:
                    matrix[r][c] = head.val
                    head, c = head.next, c + 1
                if c == c_high + 1:
                    r, c, cur_dir, r_low = r + 1, c - 1, 'D', r_low + 1
            elif cur_dir == 'D':    
                while r <= r_high and head:
                    matrix[r][c] = head.val
                    head, r = head.next, r + 1
                if r == r_high + 1:
                    r, c, cur_dir, c_high = r - 1, c - 1, 'L', c_high - 1
            elif cur_dir == 'L':    
                while c >= c_low and head:
                    matrix[r][c] = head.val
                    head, c = head.next, c - 1
                if c == c_low - 1:
                    r, c, cur_dir, r_high = r - 1, c + 1, 'U', r_high - 1
            else:           
                while r >= r_low and head:
                    matrix[r][c] = head.val
                    head, r = head.next, r - 1
                if r == r_low - 1:
                    r, c, cur_dir, c_low = r + 1, c + 1, 'R', c_low + 1

        return matrix