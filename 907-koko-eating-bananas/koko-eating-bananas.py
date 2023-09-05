class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # brute force search range = 1, max(piles)
        # binary search 
        # math.ceil will give the hours it take to eat certain pile

        l = 1
        r = max(piles)
        res = r

        while l <= r:
            k = l + (r - l)//2

            time = 0
            for pile in piles:
                time += math.ceil(pile / k)

            # see if following k works
            # if time taken > h, then increase speed, l = k + 1
            # if time taken < h, then decrese speed, r = k - 1
            # if time taken == h, then found optimal solution, no, can be optimized further
            if time > h:
                l = k + 1
            else:
                res = min(res, k)
                r = k - 1

            # print(res)
        return res
