class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # first pass to create the dict
        # second pass for checking
        cities = set()
        for src, _ in paths:
            cities.add(src)

        for _, dst in paths:
            if dst not in cities:
                return dst

        return '-1'