class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        ptr_a, ptr_b = 0, 0
        intersection = []	

        while ptr_a < len(firstList) and ptr_b < len(secondList):
            start_a, end_a = firstList[ptr_a]	
            start_b, end_b = secondList[ptr_b]
            
            if not (end_a < start_b or end_b < start_a):	# find intersection
                intersection.append([max(start_a, start_b), min(end_a, end_b)])
            
            # update ptr based on the end 
            if end_a < end_b:
                ptr_a += 1
            else:
                ptr_b += 1

        return intersection
