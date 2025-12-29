class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:

        mapping = collections.defaultdict(list)
        for pattern in allowed:
            mapping[pattern[:2]].append(pattern[2])

        @cache
        def backtrack(i, cur_row, upper_row):
            if len(cur_row) == 1:
                return True

            if i == len(cur_row) - 1:
                return backtrack(0, upper_row, "")

            key = cur_row[i:i + 2]
            for top in mapping[key]:
                if backtrack(i + 1, cur_row, upper_row + top):
                    return True
            return False

        return backtrack(0, bottom, "")