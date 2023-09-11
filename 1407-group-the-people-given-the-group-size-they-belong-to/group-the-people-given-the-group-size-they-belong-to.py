class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        group_map = collections.defaultdict(list) 
        # group_size - elements pairs

        for i, size in enumerate(groupSizes):
            group_map[size].append(i)
        # print(group_map)

        res = []
        for size, elements in group_map.items():
            for i in range(0, len(elements), size):
                res.append(elements[i:i+size])

        return res