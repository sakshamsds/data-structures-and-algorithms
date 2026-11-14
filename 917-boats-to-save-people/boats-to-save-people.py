class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort(key=lambda x:x)
        l, r = 0, len(people) - 1
        boats = 0
        while l <= r:
            if people[r] + people[l] <= limit:
                r -= 1
                l += 1
            else:
                r -= 1
            boats += 1
        return boats            

