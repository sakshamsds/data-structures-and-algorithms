class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happyStrings = ["dummy"]
        cur = []

        adjList = {
            'a' : 'bc',
            'b' : 'ac',
            'c' : 'ab'
        }

        def dfs():
            if len(cur) == n:
                happyStrings.append(''.join(cur))
                return

            prev = cur[-1]
            for nbr in adjList[prev]:
                cur.append(nbr)
                dfs()
                cur.pop()

        for c in 'abc':
            cur.append(c)
            dfs()
            cur.pop()

        # print(happyStrings)

        return happyStrings[k] if k < len(happyStrings) else ""
