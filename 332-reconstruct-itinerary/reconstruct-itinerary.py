'''
jfk: atl, sfo
atl: jfk, sfo
sfo: atl

jfk -> atl -> jfk -> sfo -> atl -> sfo
           -> sfo -> atl -> jfk -> sfo
    -> sfo -> atl -> jfk -> atl -> sfo
                  -> sfo
'''

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # TC: O(E^2)
        # SC: O(E)

        # sort the tickets
        tickets.sort()

        adj_map = collections.defaultdict(list)
        for src, dst in tickets:
            adj_map[src].append(dst)      
            # adj_map[start].sort()     # need this list in sorted order
        print(adj_map)

        res = ['JFK']
        def dfs(src):
            if len(res) == len(tickets) + 1:    # base case 1
                return True
            if src not in adj_map:      # no outgoing edges remaining
                return False

            # iterate neighbors, backtrack
            dsts = adj_map[src].copy()
            for i, dst in enumerate(dsts):
                adj_map[src].pop(i)
                res.append(dst)
                if dfs(dst): return True
                # back track our decision
                adj_map[src].insert(i, dst)
                res.pop()
            return False

        dfs('JFK')
        return res
