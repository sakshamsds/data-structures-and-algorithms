class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        # get max continuous zeros
        max_zeros = 0
        cur_zeros = 0

        for seat in seats:
            if seat == 1:
                cur_zeros = 1
            else:
                cur_zeros += 1
            
            max_zeros = max(cur_zeros, max_zeros)

        # print(max_zeros)
        res = max_zeros//2

        # check first 1 from left side
        cnt = 0
        for seat in seats:
            if seat == 1:
                break
            cnt += 1

        res = max(max_zeros//2, cnt)

        # check first 1 from right side
        cnt = 0
        for i in range(len(seats) - 1, -1, -1):
            if seats[i] == 1:
                break
            cnt += 1

        res = max(res, cnt)
        return res