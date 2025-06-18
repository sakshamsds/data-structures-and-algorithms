class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        subarray = []
        for num in nums:
            subarray.append(num)
            if len(subarray) == 3:
                if subarray[2] - subarray[0] > k:
                    return []
                res.append(subarray)
                subarray = []

        return res
                
