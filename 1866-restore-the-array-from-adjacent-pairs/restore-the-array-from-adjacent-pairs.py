class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # make adj list
        adj_list = collections.defaultdict(list)
        for x, y in adjacentPairs:
            adj_list[x].append(y)
            adj_list[y].append(x)

        root = -1
        for k, v in adj_list.items():
            if len(v) == 1:
                root = k
                break

        res = []
        
        def dfs(node, prev):
            res.append(node)
            for neighbor in adj_list[node]:
                if neighbor != prev:
                    dfs(neighbor, node)

        dfs(root, None)
        return res


        