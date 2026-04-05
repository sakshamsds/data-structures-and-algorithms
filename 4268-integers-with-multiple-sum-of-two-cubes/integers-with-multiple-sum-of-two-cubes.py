class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        
        # num -> (a, b)
        pairs = collections.defaultdict(set)
        cubes = {1:1}

        for a in range(1, n + 1):
            if a not in cubes:
                cubes[a] = a ** 3
            a_cube = cubes[a]
            if a_cube > n:
                break
            for b in range(a, n + 1):
                if b not in cubes:
                    cubes[b] = b ** 3
                b_cube = cubes[b]
                num = a_cube + b_cube
                if num > n:
                    break
                pairs[a_cube + b_cube].add((a_cube, b_cube))

        res = []
        for num, p in pairs.items():
            if len(p) > 1:
                res.append(num)

        return sorted(res)

