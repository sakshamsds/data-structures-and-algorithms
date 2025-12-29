class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:

        mapping = collections.defaultdict(list)
        for pattern in allowed:
            mapping[pattern[:2]].append(pattern[2])

        def backtrack(i_cur, cur_row, upper_row):
            # print(i_cur, cur_row, upper_row)
            if len(cur_row) == 1:
                return True

            if i_cur == len(cur_row) - 1:
                return backtrack(0, upper_row, list())

            cur_key = cur_row[i_cur] + cur_row[i_cur + 1]
            if cur_key not in mapping:
                return False

            for top in mapping[cur_key]:
                upper_row.append(top)
                if backtrack(i_cur + 1, cur_row, upper_row):
                    return True
                upper_row.pop()

            if len(upper_row) > 0:
                backtrack(0, upper_row, list())

            return False

        return backtrack(0, list(bottom), list())