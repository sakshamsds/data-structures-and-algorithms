class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = []
        larger = []
        count_pivot = 0

        for num in nums:
            if num < pivot:
                smaller.append(num)
            elif pivot < num:
                larger.append(num)
            else:
                count_pivot += 1

        return smaller + [pivot] * count_pivot + larger
        