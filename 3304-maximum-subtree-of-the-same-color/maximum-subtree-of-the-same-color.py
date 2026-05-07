'''
all the neighbors should have same color
'''

class Solution:
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
        adjList = collections.defaultdict(list)
        for s, e in edges:
            adjList[s].append(e)
            adjList[e].append(s)

        visited = set()
        self.max = 1

        def dfs(node):
            parentColor = colors[node]
            subtreeNodes = 1        # include parent
            parentMatch = True
            visited.add(node)
            for nbr in adjList[node]:
                if nbr not in visited:
                    cValid, cNodes, cColor = dfs(nbr)
                    if cValid and cColor == parentColor:
                        subtreeNodes += cNodes
                    else:
                        parentMatch = False

            if parentMatch == True:
                self.max = max(self.max, subtreeNodes)
                return True, subtreeNodes, parentColor
            return False, subtreeNodes, parentColor

        dfs(0)
        return self.max
