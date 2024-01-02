class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
        while l < r:
            mid = l + (r - l) // 2
            if letters[mid] <= target: # cond does not satisfy, ignore left half
                l = mid + 1
            else:           # condition satisfied by keep looking for better 
                r = mid
        return letters[l] if letters[l] > target else letters[0]